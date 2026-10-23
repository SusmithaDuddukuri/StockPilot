"""Inventory domain operations with transaction-safe quantity changes."""
from .audit import record_event
from .validation import ValidationError, integer, required_text, optional_text, normalized_code, money

def receive_stock(cx, sku, quantity, note='Goods received', actor='Warehouse team'):
    item = cx.execute('SELECT sku,quantity FROM products WHERE sku=?', (sku,)).fetchone()
    if not item:
        raise LookupError('Product not found.')
    if quantity <= 0:
        raise ValidationError('Received quantity must be greater than zero.')
    cx.execute('UPDATE products SET quantity=quantity+?,updated_at=CURRENT_TIMESTAMP WHERE sku=?', (quantity, sku))
    cx.execute('INSERT INTO movements(sku,delta,note) VALUES(?,?,?)', (sku, quantity, note[:160]))
    record_event(cx, 'stock.received', 'product', sku, f'Received {quantity} units. {note}', actor)
    return item['quantity'] + quantity

def issue_stock(cx, sku, quantity, note='Stock issued', actor='Warehouse team'):
    item = cx.execute('SELECT sku,quantity FROM products WHERE sku=?', (sku,)).fetchone()
    if not item:
        raise LookupError('Product not found.')
    if quantity <= 0:
        raise ValidationError('Issued quantity must be greater than zero.')
    if item['quantity'] < quantity:
        raise ValidationError(f'Insufficient stock: {item["quantity"]} units available.')
    cx.execute('UPDATE products SET quantity=quantity-?,updated_at=CURRENT_TIMESTAMP WHERE sku=?', (quantity, sku))
    cx.execute('INSERT INTO movements(sku,delta,note) VALUES(?,?,?)', (sku, -quantity, note[:160]))
    record_event(cx, 'stock.issued', 'product', sku, f'Issued {quantity} units. {note}', actor)
    return item['quantity'] - quantity

def adjust_stock(cx, sku, counted_quantity, actor='Warehouse team', note='Cycle count adjustment'):
    item = cx.execute('SELECT sku,quantity FROM products WHERE sku=?', (sku,)).fetchone()
    if not item:
        raise LookupError('Product not found.')
    delta = counted_quantity - item['quantity']
    if delta:
        cx.execute('UPDATE products SET quantity=?,updated_at=CURRENT_TIMESTAMP WHERE sku=?', (counted_quantity, sku))
        cx.execute('INSERT INTO movements(sku,delta,note) VALUES(?,?,?)', (sku, delta, note[:160]))
        record_event(cx, 'stock.adjusted', 'product', sku, f'Count adjustment {delta:+d}; new quantity {counted_quantity}.', actor)
    return {'previous': item['quantity'], 'current': counted_quantity, 'delta': delta}

def inventory_health(cx):
    row = cx.execute('''SELECT COUNT(*) AS sku_count, COALESCE(SUM(quantity),0) AS units,
        SUM(CASE WHEN quantity<=reorder_level THEN 1 ELSE 0 END) AS low_count,
        SUM(CASE WHEN quantity=0 THEN 1 ELSE 0 END) AS out_count,
        COALESCE(SUM(quantity*unit_cost),0) AS value FROM products''').fetchone()
    return dict(row)

def reorder_recommendations(cx, limit=100):
    rows = cx.execute('''SELECT sku,name,quantity,reorder_level,supplier,location,
        MAX(reorder_level*2-quantity, 0) AS suggested_order,
        ROUND(MAX(reorder_level*2-quantity,0)*unit_cost,2) AS estimated_cost
        FROM products WHERE quantity<=reorder_level ORDER BY (reorder_level-quantity) DESC,name LIMIT ?''',
        (max(1,min(int(limit),500)),)).fetchall()
    return [dict(row) for row in rows]
