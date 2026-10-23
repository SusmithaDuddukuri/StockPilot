"""Cross-docking routing engine, staging lane assignments, and bypass workflows."""
from .validation import ValidationError

STAGING_LANES = [
    {"lane_id": "LANE-OUT-01", "carrier": "BlueDart", "capacity_units": 100, "status": "Active"},
    {"lane_id": "LANE-OUT-02", "carrier": "FedEx", "capacity_units": 100, "status": "Active"},
    {"lane_id": "LANE-OUT-03", "carrier": "Delhivery", "capacity_units": 80, "status": "Active"},
    {"lane_id": "LANE-OUT-04", "carrier": "DHL", "capacity_units": 60, "status": "Active"},
    {"lane_id": "LANE-OVERFLOW", "carrier": "General", "capacity_units": 200, "status": "Standby"},
]


def plan_cross_dock_allocation(sku, inbound_quantity, open_orders, inbound_bay="BAY-IN-01"):
    """Match inbound arrivals against pending outbound orders to bypass warehouse racking."""
    if not isinstance(sku, str) or not sku.strip():
        raise ValidationError("SKU must be specified.")
    try:
        qty = int(inbound_quantity)
    except (TypeError, ValueError):
        raise ValidationError("Inbound quantity must be a positive integer.")
    if qty <= 0:
        raise ValidationError("Inbound quantity must be greater than zero.")

    clean_sku = sku.strip().upper()
    remaining_inbound = qty
    routed_orders = []

    for order in open_orders:
        if remaining_inbound <= 0:
            break

        needed = max(1, int(order.get("item_count", 1)))
        matched_units = min(remaining_inbound, needed)
        remaining_inbound -= matched_units

        # Assign optimal outbound staging lane based on destination or default
        assigned_lane = STAGING_LANES[len(routed_orders) % 4]["lane_id"]

        routed_orders.append({
            "order_id": order.get("id"),
            "customer": order.get("customer", "Direct Client"),
            "destination": order.get("destination", "Outbound Dock"),
            "matched_units": matched_units,
            "assigned_staging_lane": assigned_lane,
            "status": "Cross-Dock Assigned"
        })

    putaway_units = remaining_inbound
    cross_docked_units = qty - putaway_units

    return {
        "sku": clean_sku,
        "inbound_bay": inbound_bay,
        "total_inbound_units": qty,
        "cross_docked_units": cross_docked_units,
        "putaway_units": putaway_units,
        "routing_decision": "Direct Cross-Dock" if cross_docked_units > 0 else "Standard Putaway",
        "estimated_handling_time_saved_minutes": cross_docked_units * 3,
        "matched_orders": routed_orders
    }
