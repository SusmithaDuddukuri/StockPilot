"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_waste_weight_kg_01(record):
    """Evaluate waste weight for control WP-0260-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-01", "metric": "waste_weight_kg",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-01", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-01", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-01", "metric": "waste_weight_kg", "label": "waste weight",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "waste weight falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_lot_mismatch_count_02(record):
    """Evaluate lot mismatches for control WP-0260-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-02", "metric": "lot_mismatch_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-02", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-02", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-02", "metric": "lot_mismatch_count", "label": "lot mismatches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lot mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_webhook_retry_count_03(record):
    """Evaluate webhook retries for control WP-0260-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("webhook_retry_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-03", "metric": "webhook_retry_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-03", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-03", "metric": "webhook_retry_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-03", "metric": "webhook_retry_count", "label": "webhook retries",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "webhook retries must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_dunnage_weight_pct_04(record):
    """Evaluate dunnage weight share for control WP-0260-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dunnage_weight_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-04", "metric": "dunnage_weight_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-04", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-04", "metric": "dunnage_weight_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-04", "metric": "dunnage_weight_pct", "label": "dunnage weight share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "dunnage weight share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_chargeback_rate_pct_05(record):
    """Evaluate chargeback rate for control WP-0260-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chargeback_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-05", "metric": "chargeback_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-05", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-05", "metric": "chargeback_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-05", "metric": "chargeback_rate_pct", "label": "chargeback rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "chargeback rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_reefer_service_age_days_06(record):
    """Evaluate reefer service age for control WP-0260-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_service_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-06", "metric": "reefer_service_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-06", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-06", "metric": "reefer_service_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-06", "metric": "reefer_service_age_days", "label": "reefer service age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reefer service age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_repair_queue_age_days_07(record):
    """Evaluate repair queue age for control WP-0260-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_queue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-07", "metric": "repair_queue_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-07", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-07", "metric": "repair_queue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-07", "metric": "repair_queue_age_days", "label": "repair queue age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "repair queue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_sprinkler_obstruction_count_08(record):
    """Evaluate sprinkler obstructions for control WP-0260-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-08", "metric": "sprinkler_obstruction_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-08", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-08", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-08", "metric": "sprinkler_obstruction_count", "label": "sprinkler obstructions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "sprinkler obstructions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_amr_battery_pct_09(record):
    """Evaluate AMR battery for control WP-0260-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-09", "metric": "amr_battery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-09", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-09", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-09", "metric": "amr_battery_pct", "label": "AMR battery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "AMR battery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_monitoring_coverage_pct_10(record):
    """Evaluate monitoring coverage for control WP-0260-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("monitoring_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-10", "metric": "monitoring_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-10", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-10", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-10", "metric": "monitoring_coverage_pct", "label": "monitoring coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "monitoring coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_device_enrollment_pct_11(record):
    """Evaluate device enrollment for control WP-0260-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_enrollment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-11", "metric": "device_enrollment_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-11", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-11", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-11", "metric": "device_enrollment_pct", "label": "device enrollment",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "device enrollment must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_order_line_duplicate_count_12(record):
    """Evaluate duplicate order lines for control WP-0260-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_line_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-12", "metric": "order_line_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "lines",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-12", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-12", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-12", "metric": "order_line_duplicate_count", "label": "duplicate order lines",
        "status": "breach", "severity": "critical", "unit": "lines",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "duplicate order lines exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_putaway_task_queue_13(record):
    """Evaluate putaway task queue for control WP-0260-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-13", "metric": "putaway_task_queue",
            "status": "insufficient_data",
            "severity": "low", "unit": "tasks",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-13", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-13", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-13", "metric": "putaway_task_queue", "label": "putaway task queue",
        "status": "breach", "severity": "low", "unit": "tasks",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "putaway task queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_credit_hold_age_hours_14(record):
    """Evaluate credit hold age for control WP-0260-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_hold_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-14", "metric": "credit_hold_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-14", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-14", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-14", "metric": "credit_hold_age_hours", "label": "credit hold age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "credit hold age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_crossdock_miss_count_15(record):
    """Evaluate cross-dock misses for control WP-0260-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-15", "metric": "crossdock_miss_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-15", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-15", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-15", "metric": "crossdock_miss_count", "label": "cross-dock misses",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cross-dock misses must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_space_cost_per_pallet_16(record):
    """Evaluate space cost per pallet for control WP-0260-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("space_cost_per_pallet")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-16", "metric": "space_cost_per_pallet",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-16", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-16", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-16", "metric": "space_cost_per_pallet", "label": "space cost per pallet",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "space cost per pallet exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_order_ack_pct_17(record):
    """Evaluate supplier order acknowledgement for control WP-0260-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-17", "metric": "supplier_order_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-17", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-17", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-17", "metric": "supplier_order_ack_pct", "label": "supplier order acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier order acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_recovery_test_age_days_18(record):
    """Evaluate supplier recovery test age for control WP-0260-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-18", "metric": "supplier_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-18", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-18", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-18", "metric": "supplier_recovery_test_age_days", "label": "supplier recovery test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_buffer_inventory_units_19(record):
    """Evaluate supplier buffer inventory for control WP-0260-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_buffer_inventory_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-19", "metric": "supplier_buffer_inventory_units",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-19", "metric": "supplier_buffer_inventory_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-19", "metric": "supplier_buffer_inventory_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-19", "metric": "supplier_buffer_inventory_units", "label": "supplier buffer inventory",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier buffer inventory must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_encryption_compliance_pct_20(record):
    """Evaluate supplier encryption compliance for control WP-0260-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-20", "metric": "supplier_encryption_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-20", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-20", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-20", "metric": "supplier_encryption_compliance_pct", "label": "supplier encryption compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier encryption compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_port_alternative_count_21(record):
    """Evaluate supplier port alternatives for control WP-0260-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-21", "metric": "supplier_port_alternative_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "ports",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-21", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-21", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-21", "metric": "supplier_port_alternative_count", "label": "supplier port alternatives",
        "status": "breach", "severity": "low", "unit": "ports",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier port alternatives falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_natural_hazard_score_22(record):
    """Evaluate supplier natural-hazard exposure for control WP-0260-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_natural_hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-22", "metric": "supplier_natural_hazard_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-22", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-22", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-22", "metric": "supplier_natural_hazard_score", "label": "supplier natural-hazard exposure",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier natural-hazard exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_recovery_contact_pct_23(record):
    """Evaluate supplier recovery contact completeness for control WP-0260-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_contact_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-23", "metric": "supplier_recovery_contact_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-23", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-23", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-23", "metric": "supplier_recovery_contact_pct", "label": "supplier recovery contact completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery contact completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_major_finding_count_24(record):
    """Evaluate supplier major findings for control WP-0260-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_major_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0260-24", "metric": "supplier_major_finding_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0260-24", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0260-24", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0260-24", "metric": "supplier_major_finding_count", "label": "supplier major findings",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier major findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_waste_weight_kg_01, assess_lot_mismatch_count_02, assess_webhook_retry_count_03, assess_dunnage_weight_pct_04, assess_chargeback_rate_pct_05, assess_reefer_service_age_days_06, assess_repair_queue_age_days_07, assess_sprinkler_obstruction_count_08, assess_amr_battery_pct_09, assess_monitoring_coverage_pct_10, assess_device_enrollment_pct_11, assess_order_line_duplicate_count_12, assess_putaway_task_queue_13, assess_credit_hold_age_hours_14, assess_crossdock_miss_count_15, assess_space_cost_per_pallet_16, assess_supplier_order_ack_pct_17, assess_supplier_recovery_test_age_days_18, assess_supplier_buffer_inventory_units_19, assess_supplier_encryption_compliance_pct_20, assess_supplier_port_alternative_count_21, assess_supplier_natural_hazard_score_22, assess_supplier_recovery_contact_pct_23, assess_supplier_major_finding_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

