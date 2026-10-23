"""Decision-support functions for warehouse capacity, slotting, and order waves.

These functions are deliberately data-driven and side-effect free so the same
rules can be used by the Flask API, scheduled jobs, and offline reports.
"""
from collections import defaultdict
from datetime import date
from math import ceil
from statistics import mean

from .validation import ValidationError


def _number(value, field, *, minimum=0.0, maximum=1_000_000_000.0):
    try:
        result = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"{field} must be numeric.")
    if result < minimum or result > maximum:
        raise ValidationError(f"{field} must be between {minimum:g} and {maximum:g}.")
    return result


def _whole(value, field, *, minimum=0, maximum=2_000_000_000):
    number = _number(value, field, minimum=minimum, maximum=maximum)
    if int(number) != number:
        raise ValidationError(f"{field} must be a whole number.")
    return int(number)


def warehouse_capacity(locations):
    """Summarize occupancy and flag bins at or above their capacity limit.

    Each location accepts ``location``, ``capacity_units``, and ``on_hand``.
    Missing location labels are rejected instead of silently merging bins.
    """
    result = []
    seen = set()
    for row in locations:
        name = str(row.get("location", "")).strip()
        if not name:
            raise ValidationError("Every location needs a location label.")
        key = name.casefold()
        if key in seen:
            raise ValidationError(f"Location {name} appears more than once.")
        seen.add(key)
        capacity = _whole(row.get("capacity_units"), "Capacity units", minimum=1)
        occupied = _whole(row.get("on_hand", 0), "On-hand units")
        percent = occupied / capacity * 100
        result.append({
            "location": name,
            "capacity_units": capacity,
            "on_hand": occupied,
            "available_units": max(0, capacity - occupied),
            "utilization_percent": round(percent, 2),
            "over_capacity": occupied > capacity,
            "status": "Over capacity" if occupied > capacity else (
                "Near capacity" if percent >= 85 else "Available"
            ),
        })
    total_capacity = sum(row["capacity_units"] for row in result)
    total_occupied = sum(row["on_hand"] for row in result)
    return {
        "location_count": len(result),
        "total_capacity_units": total_capacity,
        "total_occupied_units": total_occupied,
        "available_units": max(0, total_capacity - total_occupied),
        "utilization_percent": round(total_occupied / total_capacity * 100, 2) if total_capacity else 0,
        "over_capacity_locations": sum(row["over_capacity"] for row in result),
        "locations": sorted(result, key=lambda row: (-row["utilization_percent"], row["location"].casefold())),
    }


def slotting_recommendations(items, fast_mover_threshold=5.0):
    """Suggest forward-pick, reserve, or review zones from velocity and size.

    The method intentionally returns recommendations only; it does not move
    stock. A manager can review the proposed changes before a transfer is made.
    """
    threshold = _number(fast_mover_threshold, "Fast-mover threshold", minimum=0.01)
    recommendations = []
    for item in items:
        sku = str(item.get("sku", "")).strip().upper()
        if not sku:
            raise ValidationError("Every slotting item needs a SKU.")
        daily = _number(item.get("average_daily_demand", 0), "Average daily demand")
        quantity = _whole(item.get("quantity", 0), "Quantity")
        cube = _number(item.get("unit_cube", 1), "Unit cube", minimum=0.0001)
        current = str(item.get("location", "Unassigned")).strip() or "Unassigned"
        if daily >= threshold:
            zone, reason = "Forward pick", "High demand velocity reduces pick travel."
        elif quantity * cube >= 100:
            zone, reason = "Bulk reserve", "Large combined cube benefits from reserve storage."
        elif daily == 0 and quantity > 0:
            zone, reason = "Slow-mover review", "No recorded demand; review ageing and replenishment."
        else:
            zone, reason = "Standard storage", "Demand and cube do not trigger a special zone."
        recommendations.append({
            "sku": sku, "current_location": current, "recommended_zone": zone,
            "average_daily_demand": round(daily, 3), "on_hand": quantity,
            "estimated_cube": round(quantity * cube, 3), "reason": reason,
        })
    priority = {"Forward pick": 0, "Slow-mover review": 1, "Bulk reserve": 2, "Standard storage": 3}
    return sorted(recommendations, key=lambda row: (priority[row["recommended_zone"]], -row["average_daily_demand"], row["sku"]))


def build_pick_waves(order_lines, *, max_lines=50, max_units=500):
    """Group compatible order lines into bounded pick waves without losing lines."""
    max_lines = _whole(max_lines, "Maximum lines", minimum=1, maximum=10_000)
    max_units = _whole(max_units, "Maximum units", minimum=1, maximum=2_000_000_000)
    normalized = []
    for line in order_lines:
        order_id = str(line.get("order_id", "")).strip()
        sku = str(line.get("sku", "")).strip().upper()
        location = str(line.get("location", "Unassigned")).strip() or "Unassigned"
        quantity = _whole(line.get("quantity"), "Line quantity", minimum=1)
        priority = _whole(line.get("priority", 100), "Priority")
        if not order_id or not sku:
            raise ValidationError("Each order line requires an order ID and SKU.")
        normalized.append({**line, "order_id": order_id, "sku": sku, "location": location, "quantity": quantity, "priority": priority})
    normalized.sort(key=lambda row: (row["priority"], row["location"].casefold(), row["order_id"], row["sku"]))
    waves, current, units = [], [], 0
    for line in normalized:
        if current and (len(current) >= max_lines or units + line["quantity"] > max_units):
            waves.append(current)
            current, units = [], 0
        current.append(line)
        units += line["quantity"]
    if current:
        waves.append(current)
    output = []
    for index, wave in enumerate(waves, 1):
        output.append({
            "wave_number": f"WAVE-{index:04d}",
            "line_count": len(wave),
            "order_count": len({line["order_id"] for line in wave}),
            "unit_count": sum(line["quantity"] for line in wave),
            "locations": sorted({line["location"] for line in wave}, key=str.casefold),
            "lines": wave,
        })
    return {"wave_count": len(output), "line_count": len(normalized), "waves": output}


def cycle_count_variances(counts, *, tolerance_percent=0.0):
    """Compute count variances and prioritize the largest absolute discrepancies."""
    tolerance = _number(tolerance_percent, "Tolerance percent", minimum=0, maximum=100)
    results = []
    for row in counts:
        sku = str(row.get("sku", "")).strip().upper()
        if not sku:
            raise ValidationError("Each count requires a SKU.")
        expected = _whole(row.get("expected"), "Expected quantity")
        counted = _whole(row.get("counted"), "Counted quantity")
        variance = counted - expected
        percent = (abs(variance) / expected * 100) if expected else (100.0 if variance else 0.0)
        results.append({
            "sku": sku, "expected": expected, "counted": counted,
            "variance": variance, "absolute_variance": abs(variance),
            "variance_percent": round(percent, 2),
            "status": "Match" if variance == 0 else ("Within tolerance" if percent <= tolerance else "Investigate"),
        })
    results.sort(key=lambda row: (-row["absolute_variance"], row["sku"]))
    return {
        "counted_skus": len(results),
        "matched_skus": sum(row["variance"] == 0 for row in results),
        "investigate_skus": sum(row["status"] == "Investigate" for row in results),
        "net_variance_units": sum(row["variance"] for row in results),
        "absolute_variance_units": sum(row["absolute_variance"] for row in results),
        "items": results,
    }


def inventory_health_score(products, movements=()):
    """Return a transparent 0-100 score and component-level warehouse signals."""
    products = list(products)
    if not products:
        return {"score": 0, "grade": "No data", "components": {}, "alerts": ["No products are recorded."]}
    low = sum(int(row.get("quantity", 0)) <= int(row.get("reorder_level", 0)) for row in products)
    empty = sum(int(row.get("quantity", 0)) == 0 for row in products)
    total_value = sum(max(0, int(row.get("quantity", 0))) * max(0, float(row.get("unit_cost", 0))) for row in products)
    categories = defaultdict(int)
    for row in products:
        categories[str(row.get("category", "Uncategorized"))] += 1
    movement_rows = list(movements)
    negative = sum(abs(min(0, int(row.get("delta", 0)))) for row in movement_rows)
    positive = sum(max(0, int(row.get("delta", 0))) for row in movement_rows)
    stock_score = max(0, 100 - 70 * low / len(products) - 30 * empty / len(products))
    score = round(stock_score, 1)
    alerts = []
    if empty:
        alerts.append(f"{empty} SKU(s) are out of stock.")
    if low:
        alerts.append(f"{low} SKU(s) are at or below reorder level.")
    if not movement_rows:
        alerts.append("No stock movement history is available yet.")
    return {
        "score": score,
        "grade": "A" if score >= 95 else ("B" if score >= 85 else ("C" if score >= 70 else "D")),
        "components": {
            "stock_availability": score,
            "sku_count": len(products),
            "low_stock_skus": low,
            "out_of_stock_skus": empty,
            "inventory_value": round(total_value, 2),
            "category_count": len(categories),
            "movement_rows": len(movement_rows),
            "inbound_units": positive,
            "outbound_units": negative,
        },
        "category_mix": [{"category": key, "sku_count": value} for key, value in sorted(categories.items())],
        "alerts": alerts,
    }


def supplier_lead_time_summary(receipts):
    """Summarize lead-time reliability from dated receipt observations."""
    valid = []
    for row in receipts:
        try:
            ordered = date.fromisoformat(str(row["ordered_date"])[:10])
            received = date.fromisoformat(str(row["received_date"])[:10])
        except (KeyError, ValueError, TypeError):
            continue
        if received < ordered:
            continue
        valid.append({**row, "lead_time_days": (received - ordered).days})
    if not valid:
        return {"receipt_count": 0, "average_lead_time_days": None, "median_lead_time_days": None, "on_time_rate": None, "observations": []}
    lead_times = sorted(row["lead_time_days"] for row in valid)
    mid = len(lead_times) // 2
    median = lead_times[mid] if len(lead_times) % 2 else (lead_times[mid - 1] + lead_times[mid]) / 2
    on_time = [row for row in valid if row.get("promised_days") is not None and row["lead_time_days"] <= int(row["promised_days"])]
    return {
        "receipt_count": len(valid),
        "average_lead_time_days": round(mean(lead_times), 2),
        "median_lead_time_days": median,
        "on_time_rate": round(len(on_time) / len(valid), 4) if any(row.get("promised_days") is not None for row in valid) else None,
        "observations": sorted(valid, key=lambda row: row["lead_time_days"], reverse=True),
    }


def replenishment_batch(items, *, review_horizon_days=14):
    """Calculate reorder recommendations and an aggregate purchase estimate."""
    horizon = _whole(review_horizon_days, "Review horizon", minimum=1, maximum=180)
    recommendations = []
    for row in items:
        sku = str(row.get("sku", "")).strip().upper()
        if not sku:
            raise ValidationError("Each replenishment item needs a SKU.")
        quantity = _whole(row.get("quantity", 0), "Quantity")
        reorder = _whole(row.get("reorder_level", 0), "Reorder level")
        daily = _number(row.get("average_daily_demand", 0), "Average daily demand")
        lead = _whole(row.get("lead_days", 0), "Lead days", maximum=365)
        cost = _number(row.get("unit_cost", 0), "Unit cost")
        target = ceil(daily * (lead + horizon))
        suggested = max(0, target - quantity, reorder - quantity)
        urgency = "Critical" if quantity == 0 else ("High" if quantity <= reorder else ("Watch" if quantity < target else "Normal"))
        recommendations.append({
            "sku": sku, "quantity": quantity, "reorder_level": reorder,
            "target_stock": target, "suggested_order_qty": suggested,
            "estimated_order_cost": round(suggested * cost, 2), "urgency": urgency,
        })
    ranks = {"Critical": 0, "High": 1, "Watch": 2, "Normal": 3}
    recommendations.sort(key=lambda row: (ranks[row["urgency"]], -row["suggested_order_qty"], row["sku"]))
    return {
        "review_horizon_days": horizon,
        "sku_count": len(recommendations),
        "skus_to_reorder": sum(row["suggested_order_qty"] > 0 for row in recommendations),
        "total_suggested_units": sum(row["suggested_order_qty"] for row in recommendations),
        "estimated_purchase_cost": round(sum(row["estimated_order_cost"] for row in recommendations), 2),
        "items": recommendations,
    }
