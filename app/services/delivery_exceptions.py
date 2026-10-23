"""Delivery exception workflows, courier resolution matrices, and rerouting rules."""
from .validation import ValidationError

EXCEPTION_CATEGORIES = {
    "INCORRECT_ADDRESS": {
        "max_hold_days": 3,
        "default_action": "Contact customer for address amendment",
        "requires_address_update": True
    },
    "CUSTOMER_UNAVAILABLE": {
        "max_attempts": 3,
        "default_action": "Schedule automatic next-day redelivery attempt",
        "requires_address_update": False
    },
    "WEATHER_DELAY": {
        "max_hold_days": 5,
        "default_action": "Hold parcel at carrier sorting hub awaiting terminal clearance",
        "requires_address_update": False
    },
    "DAMAGED_IN_TRANSIT": {
        "max_hold_days": 1,
        "default_action": "Initiate reverse logistics return to origin and dispatch replacement order",
        "requires_address_update": False
    },
    "REROUTE_REQUESTED": {
        "max_hold_days": 2,
        "default_action": "Update carrier waypoint manifest with customer amended destination",
        "requires_address_update": True
    }
}


def evaluate_exception_action(exception_type, attempt_count=1, amended_address=None):
    """Determine standardized carrier routing action for a delivery exception."""
    cat = str(exception_type).strip().upper()
    rule = EXCEPTION_CATEGORIES.get(cat)
    if not rule:
        raise ValidationError(f"Invalid exception type: {exception_type}. Valid: {', '.join(EXCEPTION_CATEGORIES.keys())}")

    try:
        attempts = int(attempt_count)
    except (TypeError, ValueError):
        attempts = 1

    if cat == "CUSTOMER_UNAVAILABLE" and attempts >= rule["max_attempts"]:
        return {
            "exception_type": cat,
            "attempts": attempts,
            "resolution_action": "Return to Sender (RTS)",
            "shipment_state_target": "Returned",
            "instruction": f"Maximum delivery attempts ({rule['max_attempts']}) reached. Returning parcel to origin distribution hub."
        }

    if rule["requires_address_update"] and amended_address:
        return {
            "exception_type": cat,
            "attempts": attempts,
            "resolution_action": "Reroute with Amended Destination",
            "shipment_state_target": "In transit",
            "new_destination": str(amended_address).strip(),
            "instruction": f"Destination amended to '{amended_address}'. Resuming parcel transit."
        }

    return {
        "exception_type": cat,
        "attempts": attempts,
        "resolution_action": "Transit Hold / Scheduled Redelivery",
        "shipment_state_target": "Exception",
        "instruction": rule["default_action"]
    }
