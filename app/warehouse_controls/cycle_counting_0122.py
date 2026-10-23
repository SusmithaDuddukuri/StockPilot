"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_rebate_capture_pct_01(record):
    """Evaluate supplier rebate capture for control WP-0122-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-01", "metric": "supplier_rebate_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-01", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-01", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-01", "metric": "supplier_rebate_capture_pct", "label": "supplier rebate capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier rebate capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_cycle_count_age_days_02(record):
    """Evaluate supplier cycle-count age for control WP-0122-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-02", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-02", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-02", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-02", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier cycle-count age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_data_migration_match_pct_03(record):
    """Evaluate supplier data migration match for control WP-0122-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-03", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-03", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-03", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-03", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier data migration match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_reserved_qty_04(record):
    """Evaluate reserved quantity for control WP-0122-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-04", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-04", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-04", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-04", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reserved quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_truck_fill_pct_05(record):
    """Evaluate truck fill rate for control WP-0122-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-05", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-05", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-05", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-05", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "truck fill rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_proof_of_delivery_pct_06(record):
    """Evaluate proof of delivery for control WP-0122-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-06", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-06", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-06", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-06", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "proof of delivery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_duplicate_sku_count_07(record):
    """Evaluate duplicate SKUs for control WP-0122-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-07", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "SKUs",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-07", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-07", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-07", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "low", "unit": "SKUs",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "duplicate SKUs falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_restockable_return_pct_08(record):
    """Evaluate restockable returns for control WP-0122-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-08", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-08", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-08", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-08", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restockable returns must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_scale_calibration_age_days_09(record):
    """Evaluate scale calibration age for control WP-0122-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-09", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-09", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-09", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-09", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scale calibration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_mobile_scan_success_pct_10(record):
    """Evaluate mobile scan success for control WP-0122-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_scan_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-10", "metric": "mobile_scan_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-10", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-10", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-10", "metric": "mobile_scan_success_pct", "label": "mobile scan success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "mobile scan success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_dimension_capture_pct_11(record):
    """Evaluate dimension capture rate for control WP-0122-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimension_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-11", "metric": "dimension_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-11", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-11", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-11", "metric": "dimension_capture_pct", "label": "dimension capture rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "dimension capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_chain_of_custody_pct_12(record):
    """Evaluate chain of custody for control WP-0122-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_of_custody_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-12", "metric": "chain_of_custody_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-12", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-12", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-12", "metric": "chain_of_custody_pct", "label": "chain of custody",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "chain of custody must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_product_core_temp_c_13(record):
    """Evaluate product core temperature for control WP-0122-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_core_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-13", "metric": "product_core_temp_c",
            "status": "insufficient_data",
            "severity": "high", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-13", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-13", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-13", "metric": "product_core_temp_c", "label": "product core temperature",
        "status": "breach", "severity": "high", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product core temperature must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_return_fraud_score_14(record):
    """Evaluate return fraud score for control WP-0122-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_fraud_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-14", "metric": "return_fraud_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-14", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-14", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-14", "metric": "return_fraud_score", "label": "return fraud score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "return fraud score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_pedestrian_separation_pct_15(record):
    """Evaluate pedestrian separation compliance for control WP-0122-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pedestrian_separation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-15", "metric": "pedestrian_separation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-15", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-15", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-15", "metric": "pedestrian_separation_pct", "label": "pedestrian separation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "pedestrian separation compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_robot_safety_stop_count_16(record):
    """Evaluate robot safety stops for control WP-0122-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_safety_stop_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-16", "metric": "robot_safety_stop_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-16", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-16", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-16", "metric": "robot_safety_stop_count", "label": "robot safety stops",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "robot safety stops must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_runbook_test_age_days_17(record):
    """Evaluate runbook test age for control WP-0122-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-17", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-17", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-17", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-17", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "runbook test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_warehouse_sync_age_minutes_18(record):
    """Evaluate warehouse sync age for control WP-0122-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-18", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-18", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-18", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-18", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "warehouse sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_recall_notification_pct_19(record):
    """Evaluate recall notification completion for control WP-0122-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-19", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-19", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-19", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-19", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "recall notification completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_receiving_queue_orders_20(record):
    """Evaluate receiving queue for control WP-0122-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-20", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-20", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-20", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-20", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receiving queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_customer_retention_pct_21(record):
    """Evaluate customer retention for control WP-0122-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-21", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-21", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-21", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-21", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_railcar_dwell_hours_22(record):
    """Evaluate railcar dwell for control WP-0122-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-22", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-22", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-22", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-22", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "railcar dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_cost_per_line_23(record):
    """Evaluate cost per line for control WP-0122-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-23", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-23", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-23", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-23", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "cost per line falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_labor_audit_gap_count_24(record):
    """Evaluate supplier labor audit gaps for control WP-0122-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0122-24", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0122-24", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0122-24", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0122-24", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier labor audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_rebate_capture_pct_01, assess_supplier_cycle_count_age_days_02, assess_supplier_data_migration_match_pct_03, assess_reserved_qty_04, assess_truck_fill_pct_05, assess_proof_of_delivery_pct_06, assess_duplicate_sku_count_07, assess_restockable_return_pct_08, assess_scale_calibration_age_days_09, assess_mobile_scan_success_pct_10, assess_dimension_capture_pct_11, assess_chain_of_custody_pct_12, assess_product_core_temp_c_13, assess_return_fraud_score_14, assess_pedestrian_separation_pct_15, assess_robot_safety_stop_count_16, assess_runbook_test_age_days_17, assess_warehouse_sync_age_minutes_18, assess_recall_notification_pct_19, assess_receiving_queue_orders_20, assess_customer_retention_pct_21, assess_railcar_dwell_hours_22, assess_cost_per_line_23, assess_supplier_labor_audit_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

