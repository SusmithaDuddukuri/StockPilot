"""Shipment, return, and warehouse transfer workflows."""
import sqlite3
from .audit import record_event
from .inventory import issue_stock, receive_stock
from .validation import ValidationError, required_text, optional_text, integer, one_of

SHIPMENT_STATES = {'Label created', 'Ready for pickup', 'In transit', 'Delivered', 'Exception', 'Returned'}
RETURN_STATES = {'Open', 'Inspected', 'Restocked', 'Scrapped', 'Rejected'}
RETURN_DISPOSITIONS = {'Inspection', 'Restock', 'Scrap', 'Supplier claim'}

def create_transfer(cx, data):
    number = required_text(data, 'transfer_number', maximum=40).upper()
    sku = required_text(data, 'sku', maximum=40).upper()
    quantity = integer(data, 'quantity', minimum=1)
    origin = required_text(data, 'from_location', maximum=80)
    destination = required_text(data, 'to_location', maximum=80)
    if origin.casefold() == destination.casefold():
        raise ValidationError('Source and destination locations must be different.')
    item = cx.execute('SELECT quantity,location FROM products WHERE sku=?', (sku,)).fetchone()
    if not item:
        raise LookupError('Product not found.')
    if item['quantity'] < quantity:
        raise ValidationError(f'Insufficient stock: {item["quantity"]} units available.')
    try:
        cx.execute('INSERT INTO stock_transfers(transfer_number,sku,quantity,from_location,to_location,note) VALUES(?,?,?,?,?,?)',
                   (number, sku, quantity, origin, destination, optional_text(data,'note',200)))
    except sqlite3.IntegrityError as exc:
        raise ValidationError('Transfer number already exists.') from exc
    # The single-location prototype records the movement and updates the product's current bin.
    issue_stock(cx, sku, quantity, f'Transfer {number} out of {origin}')
    receive_stock(cx, sku, quantity, f'Transfer {number} into {destination}')
    cx.execute('UPDATE products SET location=?,updated_at=CURRENT_TIMESTAMP WHERE sku=?', (destination, sku))
    record_event(cx, 'warehouse.transfer', 'transfer', number, f'Moved {quantity} units of {sku} from {origin} to {destination}.')
    return number

def create_return(cx, data):
    number = required_text(data, 'return_number', maximum=40).upper()
    sku = required_text(data, 'sku', maximum=40).upper()
    quantity = integer(data, 'quantity', minimum=1)
    reason = required_text(data, 'reason', maximum=240)
    disposition = one_of(data, 'disposition', RETURN_DISPOSITIONS)
    customer = optional_text(data, 'customer_name', 120)
    if not cx.execute('SELECT 1 FROM products WHERE sku=?', (sku,)).fetchone():
        raise LookupError('Product not found.')
    try:
        cx.execute('INSERT INTO returns(return_number,sku,quantity,reason,disposition,customer_name) VALUES(?,?,?,?,?,?)',
                   (number, sku, quantity, reason, disposition, customer))
    except sqlite3.IntegrityError as exc:
        raise ValidationError('Return number already exists.') from exc
    record_event(cx, 'returns.created', 'return', number, f'Return opened for {quantity} units of {sku}: {reason}.')
    return number

def resolve_return(cx, number, status):
    status = status if status in RETURN_STATES else None
    if not status or status == 'Open':
        raise ValidationError('Choose a resolution state other than Open.')
    row = cx.execute('SELECT * FROM returns WHERE return_number=?', (number,)).fetchone()
    if not row:
        raise LookupError('Return not found.')
    if row['status'] in {'Restocked','Scrapped','Rejected'}:
        raise ValidationError('This return has already been closed.')
    if status == 'Restocked':
        receive_stock(cx, row['sku'], row['quantity'], f'Return {number} restocked')
    cx.execute('UPDATE returns SET status=?,disposition=? WHERE return_number=?', (status, status, number))
    record_event(cx, 'returns.resolved', 'return', number, f'Return resolved as {status}.')
    return dict(cx.execute('SELECT * FROM returns WHERE return_number=?',(number,)).fetchone())

def create_shipment(cx, data):
    number = required_text(data, 'shipment_number', maximum=40).upper()
    carrier = required_text(data, 'carrier', maximum=80)
    tracking = optional_text(data, 'tracking_number', 120)
    order_id = data.get('order_id')
    if order_id not in (None, ''):
        order_id = integer({'order_id': order_id}, 'order_id', minimum=1)
        if not cx.execute('SELECT 1 FROM orders WHERE id=?', (order_id,)).fetchone():
            raise LookupError('Order not found.')
    else:
        order_id = None
    try:
        cur = cx.execute('INSERT INTO shipments(shipment_number,order_id,carrier,tracking_number) VALUES(?,?,?,?)',
                         (number, order_id, carrier, tracking))
    except sqlite3.IntegrityError as exc:
        raise ValidationError('Shipment number already exists.') from exc
    record_event(cx, 'fulfilment.shipment_created', 'shipment', number, f'Shipment created with {carrier}.')
    return cur.lastrowid

def update_shipment(cx, number, status):
    if status not in SHIPMENT_STATES:
        raise ValidationError(f'Status must be one of: {", ".join(sorted(SHIPMENT_STATES))}.')
    row = cx.execute('SELECT * FROM shipments WHERE shipment_number=?', (number,)).fetchone()
    if not row:
        raise LookupError('Shipment not found.')
    if row['status'] == 'Delivered' and status != 'Delivered':
        raise ValidationError('Delivered shipments cannot move backwards.')
    if status == 'Delivered':
        cx.execute("UPDATE shipments SET status=?,delivered_at=CURRENT_TIMESTAMP WHERE shipment_number=?", (status, number))
    elif status == 'In transit' and not row['shipped_at']:
        cx.execute("UPDATE shipments SET status=?,shipped_at=CURRENT_TIMESTAMP WHERE shipment_number=?", (status, number))
    else:
        cx.execute('UPDATE shipments SET status=? WHERE shipment_number=?', (status, number))
    record_event(cx, 'fulfilment.shipment_status', 'shipment', number, f'Shipment status changed to {status}.')
    return dict(cx.execute('SELECT * FROM shipments WHERE shipment_number=?', (number,)).fetchone())
