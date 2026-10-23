"""Purchase-order lifecycle and receiving workflow."""
import sqlite3
from .audit import record_event
from .inventory import receive_stock
from .validation import ValidationError, required_text, optional_text, integer, money, iso_date

PO_STATUSES = {'Draft', 'Approved', 'Partially received', 'Received', 'Cancelled'}

def create_purchase_order(cx, data):
    supplier_id = integer(data, 'supplier_id', minimum=1)
    supplier = cx.execute('SELECT id,name FROM suppliers WHERE id=? AND active=1', (supplier_id,)).fetchone()
    if not supplier:
        raise ValidationError('Select an active supplier.')
    lines = data.get('lines')
    if not isinstance(lines, list) or not lines:
        raise ValidationError('Add at least one purchase-order line.')
    expected_date = iso_date(data, 'expected_date')
    notes = optional_text(data, 'notes', 500)
    number = required_text(data, 'po_number', maximum=40).upper()
    normalized = []
    for line in lines:
        if not isinstance(line, dict):
            raise ValidationError('Each purchase-order line must be an object.')
        sku = required_text(line, 'sku', maximum=40).upper()
        product = cx.execute('SELECT sku,unit_cost FROM products WHERE sku=?', (sku,)).fetchone()
        if not product:
            raise ValidationError(f'Unknown product SKU: {sku}.')
        qty = integer(line, 'quantity', minimum=1)
        cost = money(line, 'unit_cost', minimum=0) if line.get('unit_cost') is not None else product['unit_cost']
        normalized.append((sku, qty, cost))
    try:
        cur = cx.execute('INSERT INTO purchase_orders(po_number,supplier_id,status,expected_date,notes) VALUES(?,?,?,?,?)',
                         (number, supplier_id, 'Approved', expected_date, notes))
    except sqlite3.IntegrityError as exc:
        raise ValidationError('Purchase-order number already exists.') from exc
    po_id = cur.lastrowid
    cx.executemany('INSERT INTO purchase_order_lines(purchase_order_id,sku,ordered_qty,unit_cost) VALUES(?,?,?,?)',
                   [(po_id, sku, qty, cost) for sku, qty, cost in normalized])
    record_event(cx, 'procurement.po_created', 'purchase_order', po_id, f'Created {number} for {supplier["name"]}.')
    return po_id

def receive_purchase_order_line(cx, po_id, sku, quantity, receipt_number, actor='Warehouse team', note='Purchase order receipt'):
    po = cx.execute('SELECT * FROM purchase_orders WHERE id=?', (po_id,)).fetchone()
    if not po:
        raise LookupError('Purchase order not found.')
    if po['status'] in {'Draft', 'Cancelled', 'Received'}:
        raise ValidationError(f'Cannot receive items for a {po["status"].lower()} purchase order.')
    line = cx.execute('SELECT * FROM purchase_order_lines WHERE purchase_order_id=? AND sku=?', (po_id, sku)).fetchone()
    if not line:
        raise ValidationError('SKU is not part of this purchase order.')
    remaining = line['ordered_qty'] - line['received_qty']
    if quantity <= 0 or quantity > remaining:
        raise ValidationError(f'Receive a quantity from 1 to {remaining}.')
    cx.execute('INSERT INTO receipts(receipt_number,purchase_order_id,sku,quantity,received_by,note) VALUES(?,?,?,?,?,?)',
               (receipt_number, po_id, sku, quantity, actor, note))
    receive_stock(cx, sku, quantity, note, actor)
    cx.execute('UPDATE purchase_order_lines SET received_qty=received_qty+? WHERE id=?', (quantity, line['id']))
    outstanding = cx.execute('SELECT COUNT(*) FROM purchase_order_lines WHERE purchase_order_id=? AND received_qty<ordered_qty', (po_id,)).fetchone()[0]
    status = 'Received' if outstanding == 0 else 'Partially received'
    cx.execute('UPDATE purchase_orders SET status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?', (status, po_id))
    record_event(cx, 'procurement.received', 'purchase_order', po_id, f'Received {quantity} units of {sku} under {po["po_number"]}.', actor)
    return {'purchase_order_id': po_id, 'sku': sku, 'received': quantity, 'status': status}
