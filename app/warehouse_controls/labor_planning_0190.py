"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_reserved_qty_01(record):
    """Evaluate reserved quantity for control WP-0190-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-01", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-01", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-01", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-01", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reserved quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_truck_fill_pct_02(record):
    """Evaluate truck fill rate for control WP-0190-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-02", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-02", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-02", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-02", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "truck fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_proof_of_delivery_pct_03(record):
    """Evaluate proof of delivery for control WP-0190-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-03", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-03", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-03", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-03", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "proof of delivery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_duplicate_sku_count_04(record):
    """Evaluate duplicate SKUs for control WP-0190-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-04", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-04", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-04", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-04", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "medium", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_restockable_return_pct_05(record):
    """Evaluate restockable returns for control WP-0190-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-05", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-05", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-05", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-05", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restockable returns must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_scale_calibration_age_days_06(record):
    """Evaluate scale calibration age for control WP-0190-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-06", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-06", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-06", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-06", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "scale calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_mobile_scan_success_pct_07(record):
    """Evaluate mobile scan success for control WP-0190-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_scan_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-07", "metric": "mobile_scan_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-07", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-07", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-07", "metric": "mobile_scan_success_pct", "label": "mobile scan success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "mobile scan success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_dimension_capture_pct_08(record):
    """Evaluate dimension capture rate for control WP-0190-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimension_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-08", "metric": "dimension_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-08", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-08", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-08", "metric": "dimension_capture_pct", "label": "dimension capture rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dimension capture rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_chain_of_custody_pct_09(record):
    """Evaluate chain of custody for control WP-0190-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_of_custody_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-09", "metric": "chain_of_custody_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-09", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-09", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-09", "metric": "chain_of_custody_pct", "label": "chain of custody",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "chain of custody must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_product_core_temp_c_10(record):
    """Evaluate product core temperature for control WP-0190-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_core_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-10", "metric": "product_core_temp_c",
            "status": "insufficient_data",
            "severity": "critical", "unit": "C",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-10", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-10", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-10", "metric": "product_core_temp_c", "label": "product core temperature",
        "status": "breach", "severity": "critical", "unit": "C",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "product core temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_return_fraud_score_11(record):
    """Evaluate return fraud score for control WP-0190-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_fraud_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-11", "metric": "return_fraud_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-11", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-11", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-11", "metric": "return_fraud_score", "label": "return fraud score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "return fraud score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_pedestrian_separation_pct_12(record):
    """Evaluate pedestrian separation compliance for control WP-0190-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pedestrian_separation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-12", "metric": "pedestrian_separation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-12", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-12", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-12", "metric": "pedestrian_separation_pct", "label": "pedestrian separation compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pedestrian separation compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_robot_safety_stop_count_13(record):
    """Evaluate robot safety stops for control WP-0190-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_safety_stop_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-13", "metric": "robot_safety_stop_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-13", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-13", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-13", "metric": "robot_safety_stop_count", "label": "robot safety stops",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "robot safety stops must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_runbook_test_age_days_14(record):
    """Evaluate runbook test age for control WP-0190-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-14", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-14", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-14", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-14", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "runbook test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_warehouse_sync_age_minutes_15(record):
    """Evaluate warehouse sync age for control WP-0190-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-15", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-15", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-15", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-15", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "warehouse sync age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_recall_notification_pct_16(record):
    """Evaluate recall notification completion for control WP-0190-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-16", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-16", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-16", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-16", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recall notification completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_receiving_queue_orders_17(record):
    """Evaluate receiving queue for control WP-0190-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-17", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-17", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-17", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-17", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "receiving queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_customer_retention_pct_18(record):
    """Evaluate customer retention for control WP-0190-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-18", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-18", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-18", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-18", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "customer retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_railcar_dwell_hours_19(record):
    """Evaluate railcar dwell for control WP-0190-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-19", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-19", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-19", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-19", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "railcar dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_cost_per_line_20(record):
    """Evaluate cost per line for control WP-0190-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-20", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-20", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-20", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-20", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cost per line must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_labor_audit_gap_count_21(record):
    """Evaluate supplier labor audit gaps for control WP-0190-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-21", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-21", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-21", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-21", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier labor audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_cyber_maturity_score_22(record):
    """Evaluate supplier cyber maturity for control WP-0190-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-22", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-22", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-22", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-22", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier cyber maturity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_alternate_source_test_age_days_23(record):
    """Evaluate alternate-source test age for control WP-0190-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-23", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-23", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-23", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-23", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "alternate-source test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_incident_notification_minutes_24(record):
    """Evaluate supplier incident notification time for control WP-0190-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0190-24", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0190-24", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0190-24", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0190-24", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier incident notification time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_reserved_qty_01, assess_truck_fill_pct_02, assess_proof_of_delivery_pct_03, assess_duplicate_sku_count_04, assess_restockable_return_pct_05, assess_scale_calibration_age_days_06, assess_mobile_scan_success_pct_07, assess_dimension_capture_pct_08, assess_chain_of_custody_pct_09, assess_product_core_temp_c_10, assess_return_fraud_score_11, assess_pedestrian_separation_pct_12, assess_robot_safety_stop_count_13, assess_runbook_test_age_days_14, assess_warehouse_sync_age_minutes_15, assess_recall_notification_pct_16, assess_receiving_queue_orders_17, assess_customer_retention_pct_18, assess_railcar_dwell_hours_19, assess_cost_per_line_20, assess_supplier_labor_audit_gap_count_21, assess_supplier_cyber_maturity_score_22, assess_supplier_alternate_source_test_age_days_23, assess_supplier_incident_notification_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

