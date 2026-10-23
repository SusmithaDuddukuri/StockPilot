"""Demand planning, replenishment prioritization, and service-level calculations."""
from collections import defaultdict
from datetime import date, timedelta
from statistics import mean, pstdev
from .validation import ValidationError


def _positive(value, label, allow_zero=False):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f'{label} must be numeric.')
    if number < 0 or (number == 0 and not allow_zero):
        raise ValidationError(f'{label} must be {'non-negative' if allow_zero else 'greater than zero'}.')
    return number


def demand_velocity(daily_units, periods=30):
    """Return robust descriptive demand statistics from daily unit observations."""
    if not isinstance(daily_units, (list, tuple)):
        raise ValidationError('Daily demand must be a list of numeric observations.')
    values = [_positive(value, 'Demand', allow_zero=True) for value in daily_units]
    if not values:
        values = [0.0]
    values = values[-max(1, int(periods)):]
    avg = mean(values)
    deviation = pstdev(values) if len(values) > 1 else 0.0
    return {
        'observations': len(values),
        'total_units': sum(values),
        'average_daily_units': round(avg, 3),
        'weekly_run_rate': round(avg * 7, 2),
        'monthly_run_rate': round(avg * 30, 2),
        'standard_deviation': round(deviation, 3),
        'coefficient_of_variation': round(deviation / avg, 3) if avg else 0,
        'peak_day_units': max(values),
        'zero_demand_days': sum(1 for value in values if value == 0),
    }


def forecast_sma(daily_units, horizon=14, window=7):
    """Forecast using a trailing simple moving average with non-negative output."""
    horizon = int(horizon)
    window = int(window)
    if not 1 <= horizon <= 180:
        raise ValidationError('Forecast horizon must be between 1 and 180 days.')
    if not 1 <= window <= 90:
        raise ValidationError('Moving-average window must be between 1 and 90 days.')
    values = [_positive(value, 'Demand', allow_zero=True) for value in daily_units]
    if not values:
        raise ValidationError('At least one demand observation is required.')
    baseline = mean(values[-window:])
    today = date.today()
    return [
        {'date': (today + timedelta(days=offset)).isoformat(), 'forecast_units': round(baseline, 2), 'method': 'trailing_moving_average'}
        for offset in range(1, horizon + 1)
    ]


def reorder_point(average_daily_demand, lead_time_days, safety_stock=0):
    demand = _positive(average_daily_demand, 'Average daily demand', allow_zero=True)
    lead = _positive(lead_time_days, 'Lead time', allow_zero=True)
    safety = _positive(safety_stock, 'Safety stock', allow_zero=True)
    return int(round(demand * lead + safety))


def safety_stock(service_factor, demand_stddev, lead_time_days):
    factor = _positive(service_factor, 'Service factor', allow_zero=True)
    deviation = _positive(demand_stddev, 'Demand deviation', allow_zero=True)
    lead = _positive(lead_time_days, 'Lead time', allow_zero=True)
    return int(round(factor * deviation * (lead ** 0.5)))


def economic_order_quantity(annual_demand, order_cost, annual_holding_cost):
    demand = _positive(annual_demand, 'Annual demand', allow_zero=True)
    order = _positive(order_cost, 'Order cost')
    holding = _positive(annual_holding_cost, 'Annual holding cost')
    if demand == 0:
        return 0
    return int(round((2 * demand * order / holding) ** 0.5))


def inventory_abc(items):
    """Classify items by cumulative extended value using the ABC method."""
    normalized = []
    for item in items:
        quantity = _positive(item.get('quantity', 0), 'Quantity', allow_zero=True)
        cost = _positive(item.get('unit_cost', 0), 'Unit cost', allow_zero=True)
        normalized.append({**item, 'extended_value': quantity * cost})
    normalized.sort(key=lambda item: item['extended_value'], reverse=True)
    total = sum(item['extended_value'] for item in normalized)
    cumulative = 0.0
    result = []
    for item in normalized:
        cumulative += item['extended_value']
        share = cumulative / total if total else 0
        category = 'A' if share <= 0.8 else ('B' if share <= 0.95 else 'C')
        result.append({**item, 'value_share': round(item['extended_value'] / total, 4) if total else 0, 'cumulative_value_share': round(share, 4), 'abc_class': category})
    return result


def supplier_scorecard(receipts):
    """Score a supplier's receipts for timeliness, quantity accuracy, and defects."""
    if not receipts:
        return {'receipt_count': 0, 'on_time_rate': None, 'quantity_accuracy': None, 'defect_rate': None, 'score': None, 'grade': 'Unrated'}
    total = len(receipts)
    on_time = sum(bool(row.get('on_time')) for row in receipts) / total
    ordered = sum(max(0, float(row.get('ordered_qty', 0))) for row in receipts)
    received = sum(max(0, float(row.get('received_qty', 0))) for row in receipts)
    defects = sum(max(0, float(row.get('defective_qty', 0))) for row in receipts)
    accuracy = min(received, ordered) / ordered if ordered else 1.0
    defect_rate = defects / received if received else 0.0
    score = max(0, min(100, 45 * on_time + 35 * accuracy + 20 * (1 - min(1, defect_rate))))
    grade = 'A' if score >= 95 else ('B' if score >= 85 else ('C' if score >= 70 else 'D'))
    return {'receipt_count': total, 'on_time_rate': round(on_time, 4), 'quantity_accuracy': round(accuracy, 4), 'defect_rate': round(defect_rate, 4), 'score': round(score, 1), 'grade': grade}


def inventory_ageing(lots, as_of=None):
    as_of = as_of or date.today()
    buckets = {'0_30_days': [], '31_60_days': [], '61_90_days': [], 'over_90_days': []}
    for lot in lots:
        try:
            received = date.fromisoformat(str(lot['received_date'])[:10])
        except (KeyError, ValueError, TypeError):
            continue
        age = max(0, (as_of - received).days)
        key = '0_30_days' if age <= 30 else ('31_60_days' if age <= 60 else ('61_90_days' if age <= 90 else 'over_90_days'))
        buckets[key].append({**lot, 'age_days': age})
    return {key: {'count': len(value), 'lots': value, 'units': sum(int(row.get('quantity', 0)) for row in value)} for key, value in buckets.items()}


def prioritize_replenishment(items, horizon_days=14):
    horizon = max(1, min(180, int(horizon_days)))
    ranked = []
    for item in items:
        qty = int(item.get('quantity') or 0)
        reorder = int(item.get('reorder_level') or 0)
        velocity = max(0.0, float(item.get('average_daily_demand') or 0))
        lead = max(0, int(item.get('lead_days') or 0))
        cover = qty / velocity if velocity else float('inf')
        target = int(round(velocity * (lead + horizon)))
        shortfall = max(0, target - qty)
        urgency = 'Critical' if qty == 0 or (velocity and cover <= lead) else ('High' if qty <= reorder else ('Watch' if velocity and cover <= lead + horizon else 'Normal'))
        ranked.append({**item, 'days_of_cover': round(cover, 2) if cover != float('inf') else None, 'target_stock': target, 'suggested_order_qty': shortfall, 'urgency': urgency})
    weights = {'Critical': 0, 'High': 1, 'Watch': 2, 'Normal': 3}
    return sorted(ranked, key=lambda row: (weights[row['urgency']], row.get('days_of_cover') if row.get('days_of_cover') is not None else 10**9, row.get('sku', '')))


def allocation_plan(order_lines, stock_by_sku):
    """Allocate available stock in priority order without overcommitting inventory."""
    available = {sku: max(0, int(qty)) for sku, qty in stock_by_sku.items()}
    plan = []
    for line in sorted(order_lines, key=lambda row: (int(row.get('priority', 100)), str(row.get('order_id', '')))):
        sku = str(line.get('sku', '')).strip().upper()
        requested = max(0, int(line.get('quantity', 0)))
        allocated = min(requested, available.get(sku, 0))
        available[sku] = available.get(sku, 0) - allocated
        plan.append({**line, 'sku': sku, 'requested_qty': requested, 'allocated_qty': allocated, 'backorder_qty': requested - allocated, 'status': 'Allocated' if allocated == requested else ('Partially allocated' if allocated else 'Backordered')})
    return {'lines': plan, 'remaining_stock': available}


def warehouse_kpis(products, orders, movements):
    quantities = [max(0, int(item.get('quantity', 0))) for item in products]
    values = [max(0, int(item.get('quantity', 0))) * max(0, float(item.get('unit_cost', 0))) for item in products]
    low = [item for item in products if int(item.get('quantity', 0)) <= int(item.get('reorder_level', 0))]
    open_orders = [order for order in orders if str(order.get('status', '')).lower() not in {'shipped', 'cancelled', 'delivered'}]
    positive = sum(max(0, int(row.get('delta', 0))) for row in movements)
    negative = sum(abs(min(0, int(row.get('delta', 0)))) for row in movements)
    return {
        'sku_count': len(products), 'units_on_hand': sum(quantities), 'inventory_value': round(sum(values), 2),
        'low_stock_skus': len(low), 'out_of_stock_skus': sum(1 for item in products if int(item.get('quantity', 0)) == 0),
        'open_orders': len(open_orders), 'inbound_units_recorded': positive, 'outbound_units_recorded': negative,
        'net_movement': positive - negative, 'average_units_per_sku': round(mean(quantities), 2) if quantities else 0,
    }


def inventory_variance(expected, counted):
    expected = int(expected)
    counted = int(counted)
    delta = counted - expected
    return {'expected': expected, 'counted': counted, 'variance': delta, 'variance_percent': round(delta / expected * 100, 2) if expected else (100.0 if delta else 0.0), 'result': 'Match' if delta == 0 else ('Surplus' if delta > 0 else 'Shortage')}


def classify_velocity(daily_units):
    stats = demand_velocity(daily_units)
    average = stats['average_daily_units']
    cv = stats['coefficient_of_variation']
    velocity = 'Fast' if average >= 5 else ('Medium' if average >= 1 else 'Slow')
    variability = 'Erratic' if cv >= 1.5 else ('Variable' if cv >= 0.75 else 'Stable')
    return {**stats, 'velocity_class': velocity, 'variability_class': variability}
