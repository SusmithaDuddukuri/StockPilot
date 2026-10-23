"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_pick_accuracy_pct_01(record):
    """Evaluate supplier pick accuracy for control WP-0124-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pick_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-01", "metric": "supplier_pick_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-01", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-01", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-01", "metric": "supplier_pick_accuracy_pct", "label": "supplier pick accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier pick accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_open_claim_transfer_pct_02(record):
    """Evaluate open-claim transfer completeness for control WP-0124-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_claim_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-02", "metric": "supplier_open_claim_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-02", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-02", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-02", "metric": "supplier_open_claim_transfer_pct", "label": "open-claim transfer completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-claim transfer completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_days_of_cover_03(record):
    """Evaluate stock cover for control WP-0124-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("days_of_cover")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-03", "metric": "days_of_cover",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-03", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-03", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-03", "metric": "days_of_cover", "label": "stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_sla_breach_count_04(record):
    """Evaluate SLA breaches for control WP-0124-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-04", "metric": "sla_breach_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-04", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-04", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-04", "metric": "sla_breach_count", "label": "SLA breaches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "SLA breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_promo_lift_pct_05(record):
    """Evaluate promotion lift for control WP-0124-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("promo_lift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-05", "metric": "promo_lift_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-05", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-05", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-05", "metric": "promo_lift_pct", "label": "promotion lift",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "promotion lift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_orphan_shipment_count_06(record):
    """Evaluate orphan shipments for control WP-0124-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_shipment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-06", "metric": "orphan_shipment_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-06", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-06", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-06", "metric": "orphan_shipment_count", "label": "orphan shipments",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "orphan shipments must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_waste_weight_kg_07(record):
    """Evaluate waste weight for control WP-0124-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-07", "metric": "waste_weight_kg",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-07", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-07", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-07", "metric": "waste_weight_kg", "label": "waste weight",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "waste weight must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_lot_mismatch_count_08(record):
    """Evaluate lot mismatches for control WP-0124-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-08", "metric": "lot_mismatch_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-08", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-08", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-08", "metric": "lot_mismatch_count", "label": "lot mismatches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "lot mismatches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_webhook_retry_count_09(record):
    """Evaluate webhook retries for control WP-0124-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("webhook_retry_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-09", "metric": "webhook_retry_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-09", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-09", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-09", "metric": "webhook_retry_count", "label": "webhook retries",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "webhook retries falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_dunnage_weight_pct_10(record):
    """Evaluate dunnage weight share for control WP-0124-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dunnage_weight_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-10", "metric": "dunnage_weight_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-10", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-10", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-10", "metric": "dunnage_weight_pct", "label": "dunnage weight share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dunnage weight share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_chargeback_rate_pct_11(record):
    """Evaluate chargeback rate for control WP-0124-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chargeback_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-11", "metric": "chargeback_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-11", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-11", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-11", "metric": "chargeback_rate_pct", "label": "chargeback rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "chargeback rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_reefer_service_age_days_12(record):
    """Evaluate reefer service age for control WP-0124-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_service_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-12", "metric": "reefer_service_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-12", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-12", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-12", "metric": "reefer_service_age_days", "label": "reefer service age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "reefer service age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_repair_queue_age_days_13(record):
    """Evaluate repair queue age for control WP-0124-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_queue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-13", "metric": "repair_queue_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-13", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-13", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-13", "metric": "repair_queue_age_days", "label": "repair queue age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "repair queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_sprinkler_obstruction_count_14(record):
    """Evaluate sprinkler obstructions for control WP-0124-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-14", "metric": "sprinkler_obstruction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-14", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-14", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-14", "metric": "sprinkler_obstruction_count", "label": "sprinkler obstructions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sprinkler obstructions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_amr_battery_pct_15(record):
    """Evaluate AMR battery for control WP-0124-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-15", "metric": "amr_battery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-15", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-15", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-15", "metric": "amr_battery_pct", "label": "AMR battery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "AMR battery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_monitoring_coverage_pct_16(record):
    """Evaluate monitoring coverage for control WP-0124-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("monitoring_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-16", "metric": "monitoring_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-16", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-16", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-16", "metric": "monitoring_coverage_pct", "label": "monitoring coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "monitoring coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_device_enrollment_pct_17(record):
    """Evaluate device enrollment for control WP-0124-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_enrollment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-17", "metric": "device_enrollment_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-17", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-17", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-17", "metric": "device_enrollment_pct", "label": "device enrollment",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "device enrollment falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_order_line_duplicate_count_18(record):
    """Evaluate duplicate order lines for control WP-0124-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_line_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-18", "metric": "order_line_duplicate_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-18", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-18", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-18", "metric": "order_line_duplicate_count", "label": "duplicate order lines",
        "status": "breach", "severity": "medium", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate order lines must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_putaway_task_queue_19(record):
    """Evaluate putaway task queue for control WP-0124-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-19", "metric": "putaway_task_queue",
            "status": "insufficient_data",
            "severity": "high", "unit": "tasks",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-19", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-19", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-19", "metric": "putaway_task_queue", "label": "putaway task queue",
        "status": "breach", "severity": "high", "unit": "tasks",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "putaway task queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_credit_hold_age_hours_20(record):
    """Evaluate credit hold age for control WP-0124-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_hold_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-20", "metric": "credit_hold_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-20", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-20", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-20", "metric": "credit_hold_age_hours", "label": "credit hold age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "credit hold age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_crossdock_miss_count_21(record):
    """Evaluate cross-dock misses for control WP-0124-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-21", "metric": "crossdock_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-21", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-21", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-21", "metric": "crossdock_miss_count", "label": "cross-dock misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "cross-dock misses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_space_cost_per_pallet_22(record):
    """Evaluate space cost per pallet for control WP-0124-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("space_cost_per_pallet")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-22", "metric": "space_cost_per_pallet",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-22", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-22", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-22", "metric": "space_cost_per_pallet", "label": "space cost per pallet",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "space cost per pallet must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_order_ack_pct_23(record):
    """Evaluate supplier order acknowledgement for control WP-0124-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-23", "metric": "supplier_order_ack_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-23", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-23", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-23", "metric": "supplier_order_ack_pct", "label": "supplier order acknowledgement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier order acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_recovery_test_age_days_24(record):
    """Evaluate supplier recovery test age for control WP-0124-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0124-24", "metric": "supplier_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0124-24", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0124-24", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0124-24", "metric": "supplier_recovery_test_age_days", "label": "supplier recovery test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier recovery test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_pick_accuracy_pct_01, assess_supplier_open_claim_transfer_pct_02, assess_days_of_cover_03, assess_sla_breach_count_04, assess_promo_lift_pct_05, assess_orphan_shipment_count_06, assess_waste_weight_kg_07, assess_lot_mismatch_count_08, assess_webhook_retry_count_09, assess_dunnage_weight_pct_10, assess_chargeback_rate_pct_11, assess_reefer_service_age_days_12, assess_repair_queue_age_days_13, assess_sprinkler_obstruction_count_14, assess_amr_battery_pct_15, assess_monitoring_coverage_pct_16, assess_device_enrollment_pct_17, assess_order_line_duplicate_count_18, assess_putaway_task_queue_19, assess_credit_hold_age_hours_20, assess_crossdock_miss_count_21, assess_space_cost_per_pallet_22, assess_supplier_order_ack_pct_23, assess_supplier_recovery_test_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

