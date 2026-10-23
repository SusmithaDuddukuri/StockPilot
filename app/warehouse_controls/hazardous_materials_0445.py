"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_truck_fill_pct_01(record):
    """Evaluate truck fill rate for control WP-0445-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-01", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-01", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-01", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-01", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "truck fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_proof_of_delivery_pct_02(record):
    """Evaluate proof of delivery for control WP-0445-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-02", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-02", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-02", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-02", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "proof of delivery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_duplicate_sku_count_03(record):
    """Evaluate duplicate SKUs for control WP-0445-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-03", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-03", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-03", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-03", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "critical", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_restockable_return_pct_04(record):
    """Evaluate restockable returns for control WP-0445-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-04", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-04", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-04", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-04", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restockable returns must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_scale_calibration_age_days_05(record):
    """Evaluate scale calibration age for control WP-0445-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-05", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-05", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-05", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-05", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "scale calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_mobile_scan_success_pct_06(record):
    """Evaluate mobile scan success for control WP-0445-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_scan_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-06", "metric": "mobile_scan_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-06", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-06", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-06", "metric": "mobile_scan_success_pct", "label": "mobile scan success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "mobile scan success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_dimension_capture_pct_07(record):
    """Evaluate dimension capture rate for control WP-0445-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimension_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-07", "metric": "dimension_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-07", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-07", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-07", "metric": "dimension_capture_pct", "label": "dimension capture rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dimension capture rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_chain_of_custody_pct_08(record):
    """Evaluate chain of custody for control WP-0445-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_of_custody_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-08", "metric": "chain_of_custody_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-08", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-08", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-08", "metric": "chain_of_custody_pct", "label": "chain of custody",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "chain of custody must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_product_core_temp_c_09(record):
    """Evaluate product core temperature for control WP-0445-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_core_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-09", "metric": "product_core_temp_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-09", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-09", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-09", "metric": "product_core_temp_c", "label": "product core temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "product core temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_return_fraud_score_10(record):
    """Evaluate return fraud score for control WP-0445-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_fraud_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-10", "metric": "return_fraud_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-10", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-10", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-10", "metric": "return_fraud_score", "label": "return fraud score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "return fraud score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_pedestrian_separation_pct_11(record):
    """Evaluate pedestrian separation compliance for control WP-0445-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pedestrian_separation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-11", "metric": "pedestrian_separation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-11", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-11", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-11", "metric": "pedestrian_separation_pct", "label": "pedestrian separation compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pedestrian separation compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_robot_safety_stop_count_12(record):
    """Evaluate robot safety stops for control WP-0445-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_safety_stop_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-12", "metric": "robot_safety_stop_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-12", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-12", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-12", "metric": "robot_safety_stop_count", "label": "robot safety stops",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "robot safety stops must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_runbook_test_age_days_13(record):
    """Evaluate runbook test age for control WP-0445-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-13", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-13", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-13", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-13", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "runbook test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_warehouse_sync_age_minutes_14(record):
    """Evaluate warehouse sync age for control WP-0445-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-14", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-14", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-14", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-14", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "warehouse sync age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_recall_notification_pct_15(record):
    """Evaluate recall notification completion for control WP-0445-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-15", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-15", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-15", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-15", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recall notification completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_receiving_queue_orders_16(record):
    """Evaluate receiving queue for control WP-0445-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-16", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-16", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-16", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-16", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "low", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "receiving queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_customer_retention_pct_17(record):
    """Evaluate customer retention for control WP-0445-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-17", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-17", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-17", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-17", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "customer retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_railcar_dwell_hours_18(record):
    """Evaluate railcar dwell for control WP-0445-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-18", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-18", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-18", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-18", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "railcar dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_cost_per_line_19(record):
    """Evaluate cost per line for control WP-0445-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-19", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-19", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-19", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-19", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cost per line must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_labor_audit_gap_count_20(record):
    """Evaluate supplier labor audit gaps for control WP-0445-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-20", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-20", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-20", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-20", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier labor audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_cyber_maturity_score_21(record):
    """Evaluate supplier cyber maturity for control WP-0445-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-21", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-21", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-21", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-21", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier cyber maturity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_alternate_source_test_age_days_22(record):
    """Evaluate alternate-source test age for control WP-0445-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-22", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-22", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-22", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-22", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "alternate-source test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_incident_notification_minutes_23(record):
    """Evaluate supplier incident notification time for control WP-0445-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-23", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-23", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-23", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-23", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier incident notification time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_energy_security_score_24(record):
    """Evaluate supplier energy security for control WP-0445-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0445-24", "metric": "supplier_energy_security_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0445-24", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0445-24", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0445-24", "metric": "supplier_energy_security_score", "label": "supplier energy security",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier energy security must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_truck_fill_pct_01, assess_proof_of_delivery_pct_02, assess_duplicate_sku_count_03, assess_restockable_return_pct_04, assess_scale_calibration_age_days_05, assess_mobile_scan_success_pct_06, assess_dimension_capture_pct_07, assess_chain_of_custody_pct_08, assess_product_core_temp_c_09, assess_return_fraud_score_10, assess_pedestrian_separation_pct_11, assess_robot_safety_stop_count_12, assess_runbook_test_age_days_13, assess_warehouse_sync_age_minutes_14, assess_recall_notification_pct_15, assess_receiving_queue_orders_16, assess_customer_retention_pct_17, assess_railcar_dwell_hours_18, assess_cost_per_line_19, assess_supplier_labor_audit_gap_count_20, assess_supplier_cyber_maturity_score_21, assess_supplier_alternate_source_test_age_days_22, assess_supplier_incident_notification_minutes_23, assess_supplier_energy_security_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

