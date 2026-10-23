"""REST endpoints for procurement, warehouse controls, returns and reporting."""
import csv
import io
import sqlite3
from flask import Blueprint, current_app, jsonify, request, Response
from ..store import connect
from ..services.audit import record_event, recent_events
from ..services.inventory import inventory_health, reorder_recommendations, adjust_stock
from ..services.procurement import create_purchase_order, receive_purchase_order_line
from ..services.fulfilment import create_transfer, create_return, resolve_return, create_shipment, update_shipment
from ..services.validation import ValidationError, required_text, optional_text, integer, money, iso_date
from ..services.policy_engine import list_packs, evaluate_records

bp = Blueprint('operations', __name__, url_prefix='/api/ops')

def db():
    return connect(current_app.config['DATABASE'])

def handle_error(fn):
    try:
        return fn()
    except ValidationError as exc:
        return jsonify(error=str(exc)), 400
    except LookupError as exc:
        return jsonify(error=str(exc)), 404
    except sqlite3.IntegrityError:
        return jsonify(error='The operation conflicts with existing data.'), 409

def body():
    data = request.get_json(silent=True)
    return data if isinstance(data, dict) else {}

def rows(sql, params=()):
    with db() as cx:
        return [dict(row) for row in cx.execute(sql, params).fetchall()]

@bp.get('/health')
def operations_health():
    with db() as cx:
        return jsonify({'status':'ok','inventory':inventory_health(cx),'subsystems':['procurement','receiving','transfers','returns','shipping','cycle-counts','audit']})

@bp.get('/suppliers')
def suppliers_list():
    active = request.args.get('active')
    sql = 'SELECT * FROM suppliers'
    params = ()
    if active in {'0','1'}:
        sql += ' WHERE active=?'; params = (int(active),)
    sql += ' ORDER BY name'
    return jsonify(rows(sql, params))

@bp.post('/suppliers')
def suppliers_create():
    data = body()
    def work():
        code = required_text(data,'code',maximum=40).upper()
        name = required_text(data,'name',maximum=120)
        contact = optional_text(data,'contact_name',120)
        email = optional_text(data,'email',160)
        phone = optional_text(data,'phone',40)
        lead = integer(data,'lead_days',minimum=0,maximum=365) if data.get('lead_days') is not None else 7
        with db() as cx:
            cur = cx.execute('INSERT INTO suppliers(code,name,contact_name,email,phone,lead_days) VALUES(?,?,?,?,?,?)',(code,name,contact,email,phone,lead))
            record_event(cx,'supplier.created','supplier',cur.lastrowid,f'Supplier {name} created.')
            return jsonify(dict(cx.execute('SELECT * FROM suppliers WHERE id=?',(cur.lastrowid,)).fetchone())),201
    return handle_error(work)

@bp.patch('/suppliers/<int:supplier_id>')
def suppliers_update(supplier_id):
    data = body()
    def work():
        allowed = {'name','contact_name','email','phone','lead_days','active'}
        if not data or set(data)-allowed: raise ValidationError('Provide supported supplier fields.')
        with db() as cx:
            old = cx.execute('SELECT * FROM suppliers WHERE id=?',(supplier_id,)).fetchone()
            if not old: raise LookupError('Supplier not found.')
            values = dict(old)
            for key in ('name','contact_name','email','phone'):
                if key in data:
                    values[key] = required_text(data,key,maximum=160) if key=='name' else optional_text(data,key,160)
            if 'lead_days' in data: values['lead_days'] = integer(data,'lead_days',minimum=0,maximum=365)
            if 'active' in data:
                if data['active'] not in (True,False,0,1): raise ValidationError('Active must be true or false.')
                values['active'] = int(data['active'])
            cx.execute('UPDATE suppliers SET name=?,contact_name=?,email=?,phone=?,lead_days=?,active=?,updated_at=CURRENT_TIMESTAMP WHERE id=?',
                       (values['name'],values['contact_name'],values['email'],values['phone'],values['lead_days'],values['active'],supplier_id))
            record_event(cx,'supplier.updated','supplier',supplier_id,f'Supplier {values["name"]} updated.')
            return jsonify(dict(cx.execute('SELECT * FROM suppliers WHERE id=?',(supplier_id,)).fetchone()))
    return handle_error(work)

@bp.get('/customers')
def customers_list():
    return jsonify(rows('SELECT * FROM customers ORDER BY name'))

@bp.post('/customers')
def customers_create():
    data=body()
    def work():
        values=(required_text(data,'code',maximum=40).upper(),required_text(data,'name',maximum=120),optional_text(data,'email',160),optional_text(data,'phone',40),optional_text(data,'address',240))
        with db() as cx:
            cur=cx.execute('INSERT INTO customers(code,name,email,phone,address) VALUES(?,?,?,?,?)',values)
            record_event(cx,'customer.created','customer',cur.lastrowid,f'Customer {values[1]} created.')
            return jsonify(dict(cx.execute('SELECT * FROM customers WHERE id=?',(cur.lastrowid,)).fetchone())),201
    return handle_error(work)

@bp.get('/purchase-orders')
def purchase_orders_list():
    return jsonify(rows('''SELECT po.*,s.name AS supplier_name,
        COUNT(pol.id) AS line_count,COALESCE(SUM(pol.ordered_qty*pol.unit_cost),0) AS total_cost,
        COALESCE(SUM(pol.received_qty),0) AS received_units
        FROM purchase_orders po JOIN suppliers s ON s.id=po.supplier_id
        LEFT JOIN purchase_order_lines pol ON pol.purchase_order_id=po.id
        GROUP BY po.id ORDER BY po.id DESC'''))

@bp.post('/purchase-orders')
def purchase_orders_create():
    data=body()
    def work():
        with db() as cx:
            po_id=create_purchase_order(cx,data)
            return jsonify(dict(cx.execute('SELECT * FROM purchase_orders WHERE id=?',(po_id,)).fetchone())),201
    return handle_error(work)

@bp.get('/purchase-orders/<int:po_id>')
def purchase_order_detail(po_id):
    with db() as cx:
        po=cx.execute('''SELECT po.*,s.name AS supplier_name FROM purchase_orders po JOIN suppliers s ON s.id=po.supplier_id WHERE po.id=?''',(po_id,)).fetchone()
        if not po: return jsonify(error='Purchase order not found.'),404
        lines=cx.execute('''SELECT pol.*,p.name AS product_name,p.location FROM purchase_order_lines pol JOIN products p USING(sku) WHERE pol.purchase_order_id=? ORDER BY pol.id''',(po_id,)).fetchall()
        return jsonify({'purchase_order':dict(po),'lines':[dict(x) for x in lines]})

@bp.post('/purchase-orders/<int:po_id>/receive')
def purchase_order_receive(po_id):
    data=body()
    def work():
        sku=required_text(data,'sku',maximum=40).upper()
        qty=integer(data,'quantity',minimum=1)
        number=required_text(data,'receipt_number',maximum=40).upper()
        actor=optional_text(data,'received_by',100) or 'Warehouse team'
        note=optional_text(data,'note',160) or 'Purchase order receipt'
        with db() as cx:
            result=receive_purchase_order_line(cx,po_id,sku,qty,number,actor,note)
            return jsonify(result),201
    return handle_error(work)

@bp.get('/receipts')
def receipts_list():
    return jsonify(rows('''SELECT r.*,p.name AS product_name,po.po_number FROM receipts r JOIN products p USING(sku) LEFT JOIN purchase_orders po ON po.id=r.purchase_order_id ORDER BY r.id DESC LIMIT 500'''))

@bp.post('/transfers')
def transfers_create():
    data=body()
    def work():
        with db() as cx:
            number=create_transfer(cx,data)
            return jsonify(dict(cx.execute('SELECT * FROM stock_transfers WHERE transfer_number=?',(number,)).fetchone())),201
    return handle_error(work)

@bp.get('/transfers')
def transfers_list():
    return jsonify(rows('SELECT * FROM stock_transfers ORDER BY id DESC LIMIT 500'))

@bp.post('/returns')
def returns_create():
    data=body()
    def work():
        with db() as cx:
            number=create_return(cx,data)
            return jsonify(dict(cx.execute('SELECT * FROM returns WHERE return_number=?',(number,)).fetchone())),201
    return handle_error(work)

@bp.get('/returns')
def returns_list():
    return jsonify(rows('SELECT * FROM returns ORDER BY id DESC LIMIT 500'))

@bp.patch('/returns/<number>')
def returns_resolve(number):
    data=body()
    def work():
        status=required_text(data,'status',maximum=40)
        with db() as cx:
            return jsonify(resolve_return(cx,number,status))
    return handle_error(work)

@bp.post('/shipments')
def shipments_create():
    data=body()
    def work():
        with db() as cx:
            shipment_id=create_shipment(cx,data)
            return jsonify(dict(cx.execute('SELECT * FROM shipments WHERE id=?',(shipment_id,)).fetchone())),201
    return handle_error(work)

@bp.get('/shipments')
def shipments_list():
    return jsonify(rows('''SELECT sh.*,o.customer,o.destination FROM shipments sh LEFT JOIN orders o ON o.id=sh.order_id ORDER BY sh.id DESC LIMIT 500'''))

@bp.patch('/shipments/<number>')
def shipments_update(number):
    data=body()
    def work():
        status=required_text(data,'status',maximum=40)
        with db() as cx:
            return jsonify(update_shipment(cx,number,status))
    return handle_error(work)

@bp.post('/cycle-counts')
def cycle_count_create():
    data=body()
    def work():
        sku=required_text(data,'sku',maximum=40).upper()
        counted=integer(data,'counted_qty',minimum=0)
        number=required_text(data,'count_number',maximum=40).upper()
        actor=optional_text(data,'counted_by',100) or 'Warehouse team'
        note=optional_text(data,'note',200)
        with db() as cx:
            item=cx.execute('SELECT quantity FROM products WHERE sku=?',(sku,)).fetchone()
            if not item: raise LookupError('Product not found.')
            variance=counted-item['quantity']
            cx.execute('INSERT INTO cycle_counts(count_number,sku,expected_qty,counted_qty,variance,counted_by,note) VALUES(?,?,?,?,?,?,?)',
                       (number,sku,item['quantity'],counted,variance,actor,note))
            adjust_stock(cx,sku,counted,actor,f'Cycle count {number}: {note or "physical count"}')
            record_event(cx,'inventory.cycle_count','cycle_count',number,f'Counted {sku}: expected {item["quantity"]}, actual {counted}, variance {variance:+d}.',actor)
            return jsonify(dict(cx.execute('SELECT * FROM cycle_counts WHERE count_number=?',(number,)).fetchone())),201
    return handle_error(work)

@bp.get('/cycle-counts')
def cycle_counts_list():
    return jsonify(rows('SELECT cc.*,p.name AS product_name FROM cycle_counts cc JOIN products p USING(sku) ORDER BY cc.id DESC LIMIT 500'))

@bp.get('/reorder-recommendations')
def reorder_list():
    with db() as cx:
        return jsonify(reorder_recommendations(cx,request.args.get('limit',100)))

@bp.get('/audit')
def audit_list():
    try: limit=int(request.args.get('limit',100))
    except ValueError: limit=100
    with db() as cx:
        return jsonify(recent_events(cx,limit))

@bp.get('/reports/summary')
def reports_summary():
    with db() as cx:
        inventory=inventory_health(cx)
        statuses=[dict(row) for row in cx.execute('SELECT status,COUNT(*) AS count FROM orders GROUP BY status ORDER BY status')]
        purchase_statuses=[dict(row) for row in cx.execute('SELECT status,COUNT(*) AS count FROM purchase_orders GROUP BY status ORDER BY status')]
        return jsonify({'inventory':inventory,'orders_by_status':statuses,'purchase_orders_by_status':purchase_statuses,
                        'receipts_last_30_days':cx.execute("SELECT COUNT(*) FROM receipts WHERE created_at>=datetime('now','-30 days')").fetchone()[0],
                        'returns_open':cx.execute("SELECT COUNT(*) FROM returns WHERE status IN ('Open','Inspected')").fetchone()[0],
                        'shipments_in_transit':cx.execute("SELECT COUNT(*) FROM shipments WHERE status='In transit'").fetchone()[0]})

@bp.get('/reports/valuation.csv')
def valuation_csv():
    with db() as cx:
        items=cx.execute('SELECT sku,name,category,quantity,unit_cost,ROUND(quantity*unit_cost,2) AS extended_value,location,supplier FROM products ORDER BY category,name').fetchall()
    output=io.StringIO(); writer=csv.writer(output)
    writer.writerow(['SKU','Product','Category','On hand','Unit cost','Extended value','Location','Supplier'])
    writer.writerows([tuple(item) for item in items])
    return Response(output.getvalue(),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=stockpilot-valuation.csv'})

@bp.get('/reports/activity.csv')
def activity_csv():
    with db() as cx:
        events=cx.execute('SELECT created_at,event_type,entity_type,entity_id,summary,actor FROM audit_events ORDER BY id DESC LIMIT 10000').fetchall()
    output=io.StringIO(); writer=csv.writer(output)
    writer.writerow(['Created at','Event','Entity type','Entity ID','Summary','Actor'])
    writer.writerows([tuple(item) for item in events])
    return Response(output.getvalue(),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=stockpilot-activity.csv'})

# Planning endpoints are deliberately backed by the same operational database so
# the dashboard and API report consistent quantities and valuations.
from ..services.planning import (
    demand_velocity, forecast_sma, reorder_point, safety_stock,
    economic_order_quantity, inventory_abc, prioritize_replenishment,
    warehouse_kpis, inventory_variance, classify_velocity,
)


@bp.get('/planning/kpis')
def planning_kpis():
    with db() as cx:
        products = [dict(row) for row in cx.execute('SELECT sku,name,quantity,reorder_level,unit_cost,category,location,supplier FROM products').fetchall()]
        orders = [dict(row) for row in cx.execute('SELECT id,status,item_count,destination FROM orders').fetchall()]
        movements = [dict(row) for row in cx.execute('SELECT delta FROM movements ORDER BY id DESC LIMIT 1000').fetchall()]
    return jsonify(warehouse_kpis(products, orders, movements))


@bp.get('/planning/abc')
def planning_abc():
    with db() as cx:
        products = [dict(row) for row in cx.execute('SELECT sku,name,category,quantity,unit_cost,location,supplier FROM products').fetchall()]
    return jsonify(inventory_abc(products))


@bp.get('/planning/replenishment')
def planning_replenishment():
    try:
        horizon = int(request.args.get('horizon_days', 14))
        if not 1 <= horizon <= 180:
            raise ValueError
    except ValueError:
        return jsonify(error='horizon_days must be between 1 and 180.'), 400
    with db() as cx:
        products = cx.execute('''SELECT p.sku,p.name,p.quantity,p.reorder_level,p.unit_cost,p.supplier,
            COALESCE(s.lead_days,7) AS lead_days FROM products p
            LEFT JOIN suppliers s ON s.name=p.supplier AND s.active=1''').fetchall()
    items = []
    for row in products:
        item = dict(row)
        item['average_daily_demand'] = item['reorder_level'] / 14 if item['reorder_level'] else 0
        items.append(item)
    return jsonify(prioritize_replenishment(items, horizon))


@bp.post('/planning/forecast')
def planning_forecast():
    data = body()
    def work():
        history = data.get('daily_units')
        forecast = forecast_sma(history, data.get('horizon', 14), data.get('window', 7))
        return jsonify({'statistics': demand_velocity(history), 'forecast': forecast})
    return handle_error(work)


@bp.post('/planning/velocity')
def planning_velocity():
    data = body()
    def work():
        history = data.get('daily_units')
        return jsonify(classify_velocity(history))
    return handle_error(work)


@bp.post('/planning/stock-policy')
def planning_stock_policy():
    data = body()
    def work():
        average = data.get('average_daily_demand', 0)
        lead = data.get('lead_time_days', 0)
        deviation = data.get('demand_stddev', 0)
        factor = data.get('service_factor', 1.65)
        safety = safety_stock(factor, deviation, lead)
        point = reorder_point(average, lead, safety)
        annual_demand = float(average) * 365
        eoq = economic_order_quantity(annual_demand, data.get('order_cost', 25), data.get('annual_holding_cost', 2))
        return jsonify({'safety_stock': safety, 'reorder_point': point, 'economic_order_quantity': eoq})
    return handle_error(work)


@bp.post('/planning/variance')
def planning_variance():
    data = body()
    def work():
        if 'expected' not in data or 'counted' not in data:
            raise ValidationError('Expected and counted quantities are required.')
        try:
            expected = int(data['expected'])
            counted = int(data['counted'])
        except (TypeError, ValueError) as exc:
            raise ValidationError('Expected and counted quantities must be integers.') from exc
        if expected < 0 or counted < 0:
            raise ValidationError('Quantities cannot be negative.')
        return jsonify(inventory_variance(expected, counted))
    return handle_error(work)

# Decision-support endpoints use the same validation/error envelope as the
# transactional workflows above. They return recommendations and never mutate
# inventory unless a separate transaction endpoint is explicitly called.
from ..services.warehouse_intelligence import (
    warehouse_capacity,
    slotting_recommendations,
    build_pick_waves,
    cycle_count_variances,
    inventory_health_score,
    supplier_lead_time_summary,
    replenishment_batch,
)


def intelligence_payload(key):
    data = body()
    value = data.get(key, [])
    if not isinstance(value, list):
        raise ValidationError(f'{key.replace("_", " ").title()} must be a list.')
    return value


@bp.post('/intelligence/capacity')
def intelligence_capacity():
    def work():
        return jsonify(warehouse_capacity(intelligence_payload('locations')))
    return handle_error(work)


@bp.post('/intelligence/slotting')
def intelligence_slotting():
    def work():
        data = body()
        items = data.get('items', [])
        if not isinstance(items, list):
            raise ValidationError('Items must be a list.')
        return jsonify({'recommendations': slotting_recommendations(items, data.get('fast_mover_threshold', 5))})
    return handle_error(work)


@bp.post('/intelligence/pick-waves')
def intelligence_pick_waves():
    def work():
        data = body()
        lines = data.get('order_lines', [])
        if not isinstance(lines, list):
            raise ValidationError('Order lines must be a list.')
        return jsonify(build_pick_waves(lines, max_lines=data.get('max_lines', 50), max_units=data.get('max_units', 500)))
    return handle_error(work)


@bp.post('/intelligence/cycle-counts')
def intelligence_cycle_counts():
    def work():
        data = body()
        counts = data.get('counts', [])
        if not isinstance(counts, list):
            raise ValidationError('Counts must be a list.')
        return jsonify(cycle_count_variances(counts, tolerance_percent=data.get('tolerance_percent', 0)))
    return handle_error(work)


@bp.get('/intelligence/health-score')
def intelligence_health_score():
    with db() as cx:
        products = [dict(row) for row in cx.execute('SELECT sku,name,category,quantity,reorder_level,unit_cost,location FROM products ORDER BY sku').fetchall()]
        movements = [dict(row) for row in cx.execute('SELECT sku,delta,note,created_at FROM movements ORDER BY id DESC LIMIT 1000').fetchall()]
    return jsonify(inventory_health_score(products, movements))


@bp.post('/intelligence/replenishment')
def intelligence_replenishment():
    def work():
        data = body()
        items = data.get('items')
        if items is None:
            with db() as cx:
                items = [dict(row) for row in cx.execute('SELECT sku,quantity,reorder_level,unit_cost FROM products ORDER BY sku').fetchall()]
        if not isinstance(items, list):
            raise ValidationError('Items must be a list.')
        return jsonify(replenishment_batch(items, review_horizon_days=data.get('review_horizon_days', 14)))
    return handle_error(work)


@bp.post('/intelligence/supplier-lead-times')
def intelligence_supplier_lead_times():
    def work():
        return jsonify(supplier_lead_time_summary(intelligence_payload('receipts')))
    return handle_error(work)


@bp.get('/analytics/alerts')
def analytics_alerts():
    """Return actionable warehouse alerts derived from live operational records."""
    alerts = []
    with db() as cx:
        for row in cx.execute("SELECT sku,name,quantity,reorder_level FROM products WHERE quantity<=reorder_level ORDER BY quantity-reorder_level, name"):
            severity = 'critical' if row['quantity'] == 0 else 'high'
            alerts.append({'type':'stockout' if row['quantity'] == 0 else 'low_stock','severity':severity,'title':f"{'Out of stock' if row['quantity'] == 0 else 'Below reorder point'}: {row['name']}",'detail':f"{row['sku']} has {row['quantity']} units; reorder point is {row['reorder_level']}.",'reference':row['sku']})
        for row in cx.execute("SELECT po_number,expected_date,status FROM purchase_orders WHERE expected_date<>'' AND expected_date<date('now') AND status NOT IN ('Received','Cancelled','Closed') ORDER BY expected_date"):
            alerts.append({'type':'overdue_purchase_order','severity':'high','title':f"Overdue purchase order {row['po_number']}",'detail':f"Expected {row['expected_date']}; current status: {row['status']}.",'reference':row['po_number']})
        for row in cx.execute("SELECT return_number,sku,quantity,reason FROM returns WHERE status IN ('Open','Inspected') ORDER BY created_at"):
            alerts.append({'type':'return_pending','severity':'medium','title':f"Return needs review: {row['return_number']}",'detail':f"{row['quantity']} units of {row['sku']} · {row['reason']}",'reference':row['return_number']})
        for row in cx.execute("SELECT shipment_number,carrier,status FROM shipments WHERE status NOT IN ('Delivered','Cancelled') ORDER BY created_at DESC LIMIT 100"):
            if row['status'] in ('In transit','Delayed','Exception'):
                alerts.append({'type':'shipment_watch','severity':'medium' if row['status']=='In transit' else 'high','title':f"Shipment {row['shipment_number']} · {row['status']}",'detail':f"Carrier: {row['carrier'] or 'Not assigned'}.",'reference':row['shipment_number']})
    priority={'critical':0,'high':1,'medium':2,'low':3}
    alerts.sort(key=lambda item:(priority.get(item['severity'],4),item['type'],item['title']))
    return jsonify({'count':len(alerts),'critical':sum(a['severity']=='critical' for a in alerts),'high':sum(a['severity']=='high' for a in alerts),'alerts':alerts})

@bp.get('/analytics/locations')
def analytics_locations():
    """Summarize active inventory by storage location and value."""
    with db() as cx:
        locations=[dict(row) for row in cx.execute("""SELECT location,COUNT(*) AS sku_count,SUM(quantity) AS units,
            ROUND(SUM(quantity*unit_cost),2) AS inventory_value,
            SUM(CASE WHEN quantity<=reorder_level THEN 1 ELSE 0 END) AS at_risk_skus
            FROM products GROUP BY location ORDER BY inventory_value DESC, location""")]
    total_value=round(sum(float(row['inventory_value'] or 0) for row in locations),2)
    for row in locations:
        row['value_share_percent']=round((float(row['inventory_value'] or 0)/total_value*100),1) if total_value else 0
        row['health']='Needs attention' if row['at_risk_skus'] else 'Healthy'
    return jsonify({'location_count':len(locations),'inventory_value':total_value,'locations':locations})

@bp.get('/analytics/suppliers')
def analytics_suppliers():
    """Build supplier scorecards from purchase-order and receipt evidence."""
    with db() as cx:
        suppliers=[dict(row) for row in cx.execute("""SELECT s.id,s.code,s.name,s.lead_days,s.active,
            COUNT(DISTINCT po.id) AS purchase_orders,
            SUM(CASE WHEN po.status='Received' THEN 1 ELSE 0 END) AS completed_orders,
            SUM(CASE WHEN po.expected_date<>'' AND po.expected_date<date('now') AND po.status NOT IN ('Received','Cancelled','Closed') THEN 1 ELSE 0 END) AS overdue_orders,
            COUNT(DISTINCT r.id) AS receipts,COALESCE(SUM(r.quantity),0) AS units_received
            FROM suppliers s LEFT JOIN purchase_orders po ON po.supplier_id=s.id
            LEFT JOIN receipts r ON r.purchase_order_id=po.id
            GROUP BY s.id ORDER BY s.active DESC,s.name""")]
    for row in suppliers:
        total=int(row['purchase_orders'] or 0); done=int(row['completed_orders'] or 0); overdue=int(row['overdue_orders'] or 0)
        row['completion_rate']=round(done/total*100,1) if total else None
        row['on_time_proxy']=round(max(0,(total-overdue)/total*100),1) if total else None
        row['rating']='Needs attention' if overdue else ('Established' if total else 'No order history')
    return jsonify(suppliers)

@bp.get('/analytics/orders')
def analytics_orders():
    """Return fulfillment distribution, backlog size, and destination concentration."""
    with db() as cx:
        statuses=[dict(row) for row in cx.execute('SELECT status,COUNT(*) AS orders,COALESCE(SUM(item_count),0) AS units FROM orders GROUP BY status ORDER BY orders DESC,status')]
        destinations=[dict(row) for row in cx.execute('SELECT destination,COUNT(*) AS orders,COALESCE(SUM(item_count),0) AS units FROM orders GROUP BY destination ORDER BY orders DESC,destination LIMIT 20')]
        total=int(cx.execute('SELECT COUNT(*) FROM orders').fetchone()[0])
        shipped=int(cx.execute("SELECT COUNT(*) FROM orders WHERE status='Shipped'").fetchone()[0])
        open_orders=int(cx.execute("SELECT COUNT(*) FROM orders WHERE status!='Shipped'").fetchone()[0])
        open_units=int(cx.execute("SELECT COALESCE(SUM(item_count),0) FROM orders WHERE status!='Shipped'").fetchone()[0])
    return jsonify({'total_orders':total,'shipped_orders':shipped,'open_orders':open_orders,'open_units':open_units,'ship_rate_percent':round(shipped/total*100,1) if total else 0,'statuses':statuses,'destinations':destinations})

@bp.get('/analytics/movement')
def analytics_movement():
    """Summarize stock movement by SKU and calendar day."""
    try: days=max(1,min(365,int(request.args.get('days',30))))
    except (TypeError,ValueError): days=30
    with db() as cx:
        daily=[dict(row) for row in cx.execute("SELECT date(created_at) AS day,SUM(CASE WHEN delta>0 THEN delta ELSE 0 END) AS inbound_units,SUM(CASE WHEN delta<0 THEN -delta ELSE 0 END) AS outbound_units,COUNT(*) AS transactions FROM movements WHERE created_at>=datetime('now',?) GROUP BY date(created_at) ORDER BY day",(f'-{days} days',))]
        movers=[dict(row) for row in cx.execute("SELECT p.sku,p.name,COUNT(m.id) AS transactions,SUM(CASE WHEN m.delta>0 THEN m.delta ELSE 0 END) AS inbound_units,SUM(CASE WHEN m.delta<0 THEN -m.delta ELSE 0 END) AS outbound_units,SUM(m.delta) AS net_units FROM movements m JOIN products p USING(sku) WHERE m.created_at>=datetime('now',?) GROUP BY p.sku,p.name ORDER BY transactions DESC,p.name LIMIT 30",(f'-{days} days',))]
    return jsonify({'window_days':days,'daily':daily,'top_movers':movers})


@bp.get('/policies')
def policy_catalog():
    """List available executable warehouse policy packs with pagination."""
    try:
        offset = max(0, int(request.args.get('offset', 0)))
        limit = max(1, min(100, int(request.args.get('limit', 50))))
    except (TypeError, ValueError):
        return jsonify(error='offset and limit must be integers.'), 400
    return jsonify(list_packs(offset, limit))


@bp.post('/policies/<int:pack_id>/evaluate')
def policy_evaluate(pack_id):
    """Evaluate operational records against one selected warehouse policy pack."""
    data = body()
    records = data.get('records')
    if not isinstance(records, list):
        return jsonify(error='records must be a list.'), 400
    try:
        return jsonify(evaluate_records(pack_id, records))
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
@bp.get('/suppliers/performance-tiers')
def suppliers_performance_tiers():
    """Calculate supplier fulfillment metrics and assign tier rankings."""
    with db() as cx:
        suppliers = cx.execute(
            """
            SELECT
                s.id,
                s.code,
                s.name,
                s.lead_days,
                s.active,
                COUNT(DISTINCT po.id) AS total_pos,
                SUM(CASE WHEN po.status = 'Received' THEN 1 ELSE 0 END) AS completed_pos,
                SUM(CASE WHEN po.expected_date != '' AND po.expected_date < date('now')
                         AND po.status NOT IN ('Received', 'Cancelled', 'Closed') THEN 1 ELSE 0 END) AS overdue_pos,
                COALESCE(SUM(r.quantity), 0) AS units_supplied
            FROM suppliers s
            LEFT JOIN purchase_orders po ON po.supplier_id = s.id
            LEFT JOIN receipts r ON r.purchase_order_id = po.id
            GROUP BY s.id
            ORDER BY s.name ASC
            """
        ).fetchall()

    results = []
    for s in suppliers:
        total = int(s['total_pos'] or 0)
        completed = int(s['completed_pos'] or 0)
        overdue = int(s['overdue_pos'] or 0)
        lead = int(s['lead_days'] or 0)

        fulfillment_pct = round((completed / total * 100), 1) if total else 100.0
        on_time_pct = round(max(0.0, (total - overdue) / total * 100), 1) if total else 100.0
        composite_score = round((fulfillment_pct * 0.6) + (on_time_pct * 0.4), 1)

        if total == 0:
            tier = "Provisional"
            tier_status = "No order history yet"
        elif composite_score >= 90.0:
            tier = "Gold"
            tier_status = "Preferred partner"
        elif composite_score >= 75.0:
            tier = "Silver"
            tier_status = "Standard partner"
        elif composite_score >= 60.0:
            tier = "Bronze"
            tier_status = "Monitored partner"
        else:
            tier = "Needs Review"
            tier_status = "Escalated performance review"

        results.append({
            "supplier_id": s["id"],
            "code": s["code"],
            "name": s["name"],
            "lead_days": lead,
            "total_orders": total,
            "completed_orders": completed,
            "overdue_orders": overdue,
            "fulfillment_rate_percent": fulfillment_pct,
            "on_time_rate_percent": on_time_pct,
            "composite_score": composite_score,
            "tier": tier,
            "tier_status": tier_status
        })

    return jsonify({
        "supplier_count": len(results),
        "tiers": results
    })
@bp.get('/analytics/fulfillment-velocity')
def analytics_fulfillment_velocity():
    """Analyze fulfillment flow velocity, status ratios, and order backlog age."""
    with db() as cx:
        orders = [dict(row) for row in cx.execute(
            """
            SELECT
                id,
                customer,
                status,
                item_count,
                destination,
                created_at
            FROM orders
            ORDER BY id DESC
            """
        ).fetchall()]

    total_orders = len(orders)
    total_units = sum(int(o["item_count"]) for o in orders)
    status_counts = {}
    dest_counts = {}
    open_orders_list = []

    for o in orders:
        st = o["status"]
        status_counts[st] = status_counts.get(st, 0) + 1
        dest = o["destination"]
        dest_counts[dest] = dest_counts.get(dest, 0) + 1

        if st != "Shipped":
            open_orders_list.append(o)

    shipped_count = status_counts.get("Shipped", 0)
    shipped_pct = round((shipped_count / total_orders * 100), 1) if total_orders else 0.0
    backlog_count = len(open_orders_list)
    backlog_pct = round((backlog_count / total_orders * 100), 1) if total_orders else 0.0

    return jsonify({
        "total_orders": total_orders,
        "total_units": total_units,
        "shipped_orders": shipped_count,
        "shipped_rate_percent": shipped_pct,
        "backlog_orders": backlog_count,
        "backlog_rate_percent": backlog_pct,
        "status_distribution": status_counts,
        "destination_distribution": dest_counts,
        "backlog_sample": open_orders_list[:10]
    })
@bp.get('/inspections')
def inspections_list():
    """Retrieve history of warehouse safety inspections."""
    return jsonify(rows('SELECT * FROM safety_inspections ORDER BY id DESC LIMIT 500'))


@bp.post('/inspections')
def inspections_create():
    """Record a warehouse safety walk audit inspection."""
    data = body()
    def work():
        number = required_text(data, 'inspection_number', maximum=40).upper()
        zone = required_text(data, 'zone', maximum=60)
        inspector = optional_text(data, 'inspector', 100) or 'Safety Officer'
        status = data.get('status', 'Passed')
        if status not in {'Passed', 'Failed', 'Needs Attention', 'Corrected'}:
            raise ValidationError('Invalid inspection status.')
        findings = optional_text(data, 'findings', 500)
        action_required = optional_text(data, 'action_required', 500)

        with db() as cx:
            cur = cx.execute(
                """
                INSERT INTO safety_inspections
                (inspection_number, zone, inspector, status, findings, action_required)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (number, zone, inspector, status, findings, action_required)
            )
            record_event(cx, 'safety.inspection', 'safety_inspection', number, f'Safety inspection {number} in zone {zone} recorded with status {status}.', inspector)
            return jsonify(dict(cx.execute('SELECT * FROM safety_inspections WHERE id = ?', (cur.lastrowid,)).fetchone())), 201

    return handle_error(work)
@bp.get('/quarantine')
def quarantine_list():
    """List inventory lots held in quarantine inspection."""
    return jsonify(rows('SELECT q.*, p.name AS product_name FROM inventory_quarantine q JOIN products p USING(sku) ORDER BY q.id DESC LIMIT 500'))


@bp.post('/quarantine')
def quarantine_create():
    """Place inventory lot into quarantine hold for inspection."""
    data = body()
    def work():
        number = required_text(data, 'quarantine_number', maximum=40).upper()
        sku = required_text(data, 'sku', maximum=40).upper()
        qty = integer(data, 'quantity', minimum=1)
        reason = required_text(data, 'reason', maximum=200)
        inspector = optional_text(data, 'inspector', 100) or 'Quality Assurance'
        note = optional_text(data, 'note', 300)

        with db() as cx:
            item = cx.execute('SELECT quantity FROM products WHERE sku = ?', (sku,)).fetchone()
            if not item:
                raise LookupError('Product not found.')
            if item['quantity'] < qty:
                raise ValidationError('Quarantine quantity exceeds available on-hand stock.')

            cx.execute('UPDATE products SET quantity = quantity - ?, updated_at = CURRENT_TIMESTAMP WHERE sku = ?', (qty, sku))
            cx.execute('INSERT INTO movements (sku, delta, note) VALUES (?, ?, ?)', (sku, -qty, f'Quarantine hold: {number}'))

            cur = cx.execute(
                """
                INSERT INTO inventory_quarantine
                (quarantine_number, sku, quantity, reason, inspector, status, disposition, note)
                VALUES (?, ?, ?, ?, ?, 'Under Inspection', 'Pending', ?)
                """,
                (number, sku, qty, reason, inspector, note)
            )
            record_event(cx, 'inventory.quarantine_hold', 'quarantine', number, f'Quarantined {qty} units of {sku} for: {reason}.', inspector)
            return jsonify(dict(cx.execute('SELECT * FROM inventory_quarantine WHERE id = ?', (cur.lastrowid,)).fetchone())), 201

    return handle_error(work)


@bp.patch('/quarantine/<number>')
def quarantine_resolve(number):
    """Resolve quarantine inspection by releasing to stock or scrapping."""
    data = body()
    def work():
        status = required_text(data, 'status', maximum=40)
        disposition = required_text(data, 'disposition', maximum=40)
        actor = optional_text(data, 'resolved_by', 100) or 'Quality Assurance'

        if disposition not in {'Release to Stock', 'Scrap', 'Return to Vendor'}:
            raise ValidationError('Invalid quarantine disposition.')

        with db() as cx:
            lot = cx.execute('SELECT * FROM inventory_quarantine WHERE quarantine_number = ?', (number,)).fetchone()
            if not lot:
                raise LookupError('Quarantine record not found.')
            if lot['status'] in {'Released', 'Scrapped', 'Closed'}:
                raise ValidationError('Quarantine record is already resolved.')

            qty = lot['quantity']
            sku = lot['sku']

            if disposition == 'Release to Stock':
                cx.execute('UPDATE products SET quantity = quantity + ?, updated_at = CURRENT_TIMESTAMP WHERE sku = ?', (qty, sku))
                cx.execute('INSERT INTO movements (sku, delta, note) VALUES (?, ?, ?)', (sku, qty, f'Quarantine release: {number}'))

            cx.execute(
                """
                UPDATE inventory_quarantine
                SET status = ?, disposition = ?, updated_at = CURRENT_TIMESTAMP
                WHERE quarantine_number = ?
                """,
                (status, disposition, number)
            )
            record_event(cx, 'inventory.quarantine_resolved', 'quarantine', number, f'Quarantine {number} resolved as {disposition}.', actor)
            return jsonify(dict(cx.execute('SELECT * FROM inventory_quarantine WHERE quarantine_number = ?', (number,)).fetchone()))

    return handle_error(work)
