"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_model_availability_pct_01(record):
    """Evaluate supplier model availability for control WP-0367-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-01", "metric": "supplier_model_availability_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-01", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-01", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-01", "metric": "supplier_model_availability_pct", "label": "supplier model availability",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model availability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_event_schema_age_days_02(record):
    """Evaluate supplier event-schema age for control WP-0367-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_schema_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-02", "metric": "supplier_event_schema_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-02", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-02", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-02", "metric": "supplier_event_schema_age_days", "label": "supplier event-schema age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier event-schema age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_admin_session_age_minutes_03(record):
    """Evaluate supplier admin session age for control WP-0367-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_admin_session_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-03", "metric": "supplier_admin_session_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-03", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-03", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-03", "metric": "supplier_admin_session_age_minutes", "label": "supplier admin session age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier admin session age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_confidentiality_breach_count_04(record):
    """Evaluate supplier confidentiality breaches for control WP-0367-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_confidentiality_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-04", "metric": "supplier_confidentiality_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-04", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-04", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-04", "metric": "supplier_confidentiality_breach_count", "label": "supplier confidentiality breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier confidentiality breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_record_signoff_pct_05(record):
    """Evaluate supplier record signoff for control WP-0367-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-05", "metric": "supplier_record_signoff_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-05", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-05", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-05", "metric": "supplier_record_signoff_pct", "label": "supplier record signoff",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier record signoff must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_take_or_pay_exposure_06(record):
    """Evaluate take-or-pay exposure for control WP-0367-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_take_or_pay_exposure")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-06", "metric": "supplier_take_or_pay_exposure",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-06", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-06", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-06", "metric": "supplier_take_or_pay_exposure", "label": "take-or-pay exposure",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "take-or-pay exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_pick_accuracy_pct_07(record):
    """Evaluate supplier pick accuracy for control WP-0367-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pick_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-07", "metric": "supplier_pick_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-07", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-07", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-07", "metric": "supplier_pick_accuracy_pct", "label": "supplier pick accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier pick accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_open_claim_transfer_pct_08(record):
    """Evaluate open-claim transfer completeness for control WP-0367-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_claim_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-08", "metric": "supplier_open_claim_transfer_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-08", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-08", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-08", "metric": "supplier_open_claim_transfer_pct", "label": "open-claim transfer completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "open-claim transfer completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_days_of_cover_09(record):
    """Evaluate stock cover for control WP-0367-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("days_of_cover")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-09", "metric": "days_of_cover",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-09", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-09", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-09", "metric": "days_of_cover", "label": "stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "stock cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_sla_breach_count_10(record):
    """Evaluate SLA breaches for control WP-0367-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-10", "metric": "sla_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-10", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-10", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-10", "metric": "sla_breach_count", "label": "SLA breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "SLA breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_promo_lift_pct_11(record):
    """Evaluate promotion lift for control WP-0367-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("promo_lift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-11", "metric": "promo_lift_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-11", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-11", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-11", "metric": "promo_lift_pct", "label": "promotion lift",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "promotion lift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_orphan_shipment_count_12(record):
    """Evaluate orphan shipments for control WP-0367-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_shipment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-12", "metric": "orphan_shipment_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-12", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-12", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-12", "metric": "orphan_shipment_count", "label": "orphan shipments",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "orphan shipments falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_waste_weight_kg_13(record):
    """Evaluate waste weight for control WP-0367-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-13", "metric": "waste_weight_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-13", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-13", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-13", "metric": "waste_weight_kg", "label": "waste weight",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "waste weight must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_lot_mismatch_count_14(record):
    """Evaluate lot mismatches for control WP-0367-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-14", "metric": "lot_mismatch_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-14", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-14", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-14", "metric": "lot_mismatch_count", "label": "lot mismatches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lot mismatches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_webhook_retry_count_15(record):
    """Evaluate webhook retries for control WP-0367-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("webhook_retry_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-15", "metric": "webhook_retry_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-15", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-15", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-15", "metric": "webhook_retry_count", "label": "webhook retries",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "webhook retries exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_dunnage_weight_pct_16(record):
    """Evaluate dunnage weight share for control WP-0367-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dunnage_weight_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-16", "metric": "dunnage_weight_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-16", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-16", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-16", "metric": "dunnage_weight_pct", "label": "dunnage weight share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "dunnage weight share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_chargeback_rate_pct_17(record):
    """Evaluate chargeback rate for control WP-0367-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chargeback_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-17", "metric": "chargeback_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-17", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-17", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-17", "metric": "chargeback_rate_pct", "label": "chargeback rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "chargeback rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_reefer_service_age_days_18(record):
    """Evaluate reefer service age for control WP-0367-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_service_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-18", "metric": "reefer_service_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-18", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-18", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-18", "metric": "reefer_service_age_days", "label": "reefer service age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reefer service age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_repair_queue_age_days_19(record):
    """Evaluate repair queue age for control WP-0367-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_queue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-19", "metric": "repair_queue_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-19", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-19", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-19", "metric": "repair_queue_age_days", "label": "repair queue age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "repair queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_sprinkler_obstruction_count_20(record):
    """Evaluate sprinkler obstructions for control WP-0367-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-20", "metric": "sprinkler_obstruction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-20", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-20", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-20", "metric": "sprinkler_obstruction_count", "label": "sprinkler obstructions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "sprinkler obstructions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_amr_battery_pct_21(record):
    """Evaluate AMR battery for control WP-0367-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-21", "metric": "amr_battery_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-21", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-21", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-21", "metric": "amr_battery_pct", "label": "AMR battery",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "AMR battery must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_monitoring_coverage_pct_22(record):
    """Evaluate monitoring coverage for control WP-0367-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("monitoring_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-22", "metric": "monitoring_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-22", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-22", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-22", "metric": "monitoring_coverage_pct", "label": "monitoring coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "monitoring coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_device_enrollment_pct_23(record):
    """Evaluate device enrollment for control WP-0367-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_enrollment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-23", "metric": "device_enrollment_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-23", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-23", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-23", "metric": "device_enrollment_pct", "label": "device enrollment",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "device enrollment exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_order_line_duplicate_count_24(record):
    """Evaluate duplicate order lines for control WP-0367-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_line_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0367-24", "metric": "order_line_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0367-24", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0367-24", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0367-24", "metric": "order_line_duplicate_count", "label": "duplicate order lines",
        "status": "breach", "severity": "high", "unit": "lines",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "duplicate order lines falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_model_availability_pct_01, assess_supplier_event_schema_age_days_02, assess_supplier_admin_session_age_minutes_03, assess_supplier_confidentiality_breach_count_04, assess_supplier_record_signoff_pct_05, assess_supplier_take_or_pay_exposure_06, assess_supplier_pick_accuracy_pct_07, assess_supplier_open_claim_transfer_pct_08, assess_days_of_cover_09, assess_sla_breach_count_10, assess_promo_lift_pct_11, assess_orphan_shipment_count_12, assess_waste_weight_kg_13, assess_lot_mismatch_count_14, assess_webhook_retry_count_15, assess_dunnage_weight_pct_16, assess_chargeback_rate_pct_17, assess_reefer_service_age_days_18, assess_repair_queue_age_days_19, assess_sprinkler_obstruction_count_20, assess_amr_battery_pct_21, assess_monitoring_coverage_pct_22, assess_device_enrollment_pct_23, assess_order_line_duplicate_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

