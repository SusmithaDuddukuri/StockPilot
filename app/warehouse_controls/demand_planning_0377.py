"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_cycle_count_age_days_01(record):
    """Evaluate supplier cycle-count age for control WP-0377-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-01", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-01", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-01", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-01", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier cycle-count age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_data_migration_match_pct_02(record):
    """Evaluate supplier data migration match for control WP-0377-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-02", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-02", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-02", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-02", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier data migration match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_reserved_qty_03(record):
    """Evaluate reserved quantity for control WP-0377-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-03", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-03", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-03", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-03", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reserved quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_truck_fill_pct_04(record):
    """Evaluate truck fill rate for control WP-0377-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-04", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-04", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-04", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-04", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "truck fill rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_proof_of_delivery_pct_05(record):
    """Evaluate proof of delivery for control WP-0377-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-05", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-05", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-05", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-05", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "proof of delivery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_duplicate_sku_count_06(record):
    """Evaluate duplicate SKUs for control WP-0377-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-06", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "SKUs",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-06", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-06", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-06", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "high", "unit": "SKUs",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "duplicate SKUs falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_restockable_return_pct_07(record):
    """Evaluate restockable returns for control WP-0377-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-07", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-07", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-07", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-07", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restockable returns must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_scale_calibration_age_days_08(record):
    """Evaluate scale calibration age for control WP-0377-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-08", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-08", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-08", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-08", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scale calibration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_mobile_scan_success_pct_09(record):
    """Evaluate mobile scan success for control WP-0377-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_scan_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-09", "metric": "mobile_scan_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-09", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-09", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-09", "metric": "mobile_scan_success_pct", "label": "mobile scan success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "mobile scan success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_dimension_capture_pct_10(record):
    """Evaluate dimension capture rate for control WP-0377-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimension_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-10", "metric": "dimension_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-10", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-10", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-10", "metric": "dimension_capture_pct", "label": "dimension capture rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "dimension capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_chain_of_custody_pct_11(record):
    """Evaluate chain of custody for control WP-0377-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_of_custody_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-11", "metric": "chain_of_custody_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-11", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-11", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-11", "metric": "chain_of_custody_pct", "label": "chain of custody",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "chain of custody must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_product_core_temp_c_12(record):
    """Evaluate product core temperature for control WP-0377-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_core_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-12", "metric": "product_core_temp_c",
            "status": "insufficient_data",
            "severity": "low", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-12", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-12", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-12", "metric": "product_core_temp_c", "label": "product core temperature",
        "status": "breach", "severity": "low", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product core temperature must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_return_fraud_score_13(record):
    """Evaluate return fraud score for control WP-0377-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_fraud_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-13", "metric": "return_fraud_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-13", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-13", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-13", "metric": "return_fraud_score", "label": "return fraud score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "return fraud score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_pedestrian_separation_pct_14(record):
    """Evaluate pedestrian separation compliance for control WP-0377-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pedestrian_separation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-14", "metric": "pedestrian_separation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-14", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-14", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-14", "metric": "pedestrian_separation_pct", "label": "pedestrian separation compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "pedestrian separation compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_robot_safety_stop_count_15(record):
    """Evaluate robot safety stops for control WP-0377-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_safety_stop_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-15", "metric": "robot_safety_stop_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-15", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-15", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-15", "metric": "robot_safety_stop_count", "label": "robot safety stops",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "robot safety stops must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_runbook_test_age_days_16(record):
    """Evaluate runbook test age for control WP-0377-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-16", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-16", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-16", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-16", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "runbook test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_warehouse_sync_age_minutes_17(record):
    """Evaluate warehouse sync age for control WP-0377-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-17", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-17", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-17", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-17", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "warehouse sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_recall_notification_pct_18(record):
    """Evaluate recall notification completion for control WP-0377-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-18", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-18", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-18", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-18", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "recall notification completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_receiving_queue_orders_19(record):
    """Evaluate receiving queue for control WP-0377-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-19", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-19", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-19", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-19", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receiving queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_customer_retention_pct_20(record):
    """Evaluate customer retention for control WP-0377-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-20", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-20", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-20", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-20", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_railcar_dwell_hours_21(record):
    """Evaluate railcar dwell for control WP-0377-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-21", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-21", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-21", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-21", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "railcar dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_cost_per_line_22(record):
    """Evaluate cost per line for control WP-0377-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-22", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-22", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-22", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-22", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "cost per line falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_labor_audit_gap_count_23(record):
    """Evaluate supplier labor audit gaps for control WP-0377-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-23", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-23", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-23", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-23", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier labor audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_cyber_maturity_score_24(record):
    """Evaluate supplier cyber maturity for control WP-0377-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0377-24", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0377-24", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0377-24", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0377-24", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cyber maturity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_supplier_cycle_count_age_days_01, assess_supplier_data_migration_match_pct_02, assess_reserved_qty_03, assess_truck_fill_pct_04, assess_proof_of_delivery_pct_05, assess_duplicate_sku_count_06, assess_restockable_return_pct_07, assess_scale_calibration_age_days_08, assess_mobile_scan_success_pct_09, assess_dimension_capture_pct_10, assess_chain_of_custody_pct_11, assess_product_core_temp_c_12, assess_return_fraud_score_13, assess_pedestrian_separation_pct_14, assess_robot_safety_stop_count_15, assess_runbook_test_age_days_16, assess_warehouse_sync_age_minutes_17, assess_recall_notification_pct_18, assess_receiving_queue_orders_19, assess_customer_retention_pct_20, assess_railcar_dwell_hours_21, assess_cost_per_line_22, assess_supplier_labor_audit_gap_count_23, assess_supplier_cyber_maturity_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

