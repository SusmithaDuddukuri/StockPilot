"""Carrier Service Level Agreement (SLA) compliance tracking and scorecard analysis."""
from .validation import ValidationError

TARGET_SLA_ON_TIME_PCT = 95.0
MAX_ACCEPTABLE_EXCEPTION_PCT = 3.0


def compute_carrier_scorecard(carrier_name, shipments):
    """Compute KPI scorecards, on-time rate, and compliance rating for a carrier."""
    if not isinstance(carrier_name, str) or not carrier_name.strip():
        raise ValidationError("Carrier name is required.")

    total_shipments = len(shipments)
    if total_shipments == 0:
        return {
            "carrier": carrier_name,
            "total_shipments": 0,
            "delivered_count": 0,
            "exception_count": 0,
            "in_transit_count": 0,
            "on_time_percentage": 100.0,
            "exception_rate_percentage": 0.0,
            "sla_compliance": "No Activity",
            "tier_rating": "N/A",
            "penalty_rebate_applicable": False
        }

    delivered = sum(1 for s in shipments if str(s.get("status", "")).lower() == "delivered")
    exceptions = sum(1 for s in shipments if str(s.get("status", "")).lower() in ("exception", "returned"))
    in_transit = sum(1 for s in shipments if str(s.get("status", "")).lower() == "in transit")

    # Evaluated basis
    delivered_or_failed = delivered + exceptions
    on_time_pct = round((delivered / delivered_or_failed) * 100, 1) if delivered_or_failed > 0 else 100.0
    exception_pct = round((exceptions / total_shipments) * 100, 1)

    if on_time_pct >= 98.0 and exception_pct <= 1.0:
        tier = "Tier 1 - Preferred Partner"
        compliance = "Compliant"
        rebate = False
    elif on_time_pct >= TARGET_SLA_ON_TIME_PCT and exception_pct <= MAX_ACCEPTABLE_EXCEPTION_PCT:
        tier = "Tier 2 - Standard Compliance"
        compliance = "Compliant"
        rebate = False
    elif on_time_pct >= 90.0:
        tier = "Tier 3 - Needs Improvement"
        compliance = "Conditional Warning"
        rebate = False
    else:
        tier = "Tier 4 - SLA Breach"
        compliance = "Non-Compliant"
        rebate = True

    return {
        "carrier": carrier_name,
        "total_shipments": total_shipments,
        "delivered_count": delivered,
        "exception_count": exceptions,
        "in_transit_count": in_transit,
        "on_time_percentage": on_time_pct,
        "exception_rate_percentage": exception_pct,
        "sla_target_on_time": TARGET_SLA_ON_TIME_PCT,
        "sla_compliance": compliance,
        "tier_rating": tier,
        "penalty_rebate_applicable": rebate
    }
