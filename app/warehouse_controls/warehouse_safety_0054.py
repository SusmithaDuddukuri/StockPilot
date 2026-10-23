"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_sso_success_pct_01(record):
    """Evaluate supplier SSO success for control WP-0054-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sso_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-01", "metric": "supplier_sso_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-01", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-01", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-01", "metric": "supplier_sso_success_pct", "label": "supplier SSO success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SSO success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_anonymization_score_02(record):
    """Evaluate supplier anonymization score for control WP-0054-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_anonymization_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-02", "metric": "supplier_anonymization_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-02", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-02", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-02", "metric": "supplier_anonymization_score", "label": "supplier anonymization score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier anonymization score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_framework_coverage_pct_03(record):
    """Evaluate supplier framework coverage for control WP-0054-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_framework_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-03", "metric": "supplier_framework_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-03", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-03", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-03", "metric": "supplier_framework_coverage_pct", "label": "supplier framework coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "supplier framework coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_rebate_capture_pct_04(record):
    """Evaluate supplier rebate capture for control WP-0054-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-04", "metric": "supplier_rebate_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-04", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-04", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-04", "metric": "supplier_rebate_capture_pct", "label": "supplier rebate capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier rebate capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_cycle_count_age_days_05(record):
    """Evaluate supplier cycle-count age for control WP-0054-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-05", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-05", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-05", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-05", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cycle-count age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_data_migration_match_pct_06(record):
    """Evaluate supplier data migration match for control WP-0054-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-06", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-06", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-06", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-06", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier data migration match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_reserved_qty_07(record):
    """Evaluate reserved quantity for control WP-0054-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-07", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-07", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-07", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-07", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "reserved quantity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_truck_fill_pct_08(record):
    """Evaluate truck fill rate for control WP-0054-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-08", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-08", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-08", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-08", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "truck fill rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_proof_of_delivery_pct_09(record):
    """Evaluate proof of delivery for control WP-0054-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-09", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-09", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-09", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-09", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "proof of delivery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_duplicate_sku_count_10(record):
    """Evaluate duplicate SKUs for control WP-0054-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-10", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "SKUs",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-10", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-10", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-10", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "critical", "unit": "SKUs",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "duplicate SKUs exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_restockable_return_pct_11(record):
    """Evaluate restockable returns for control WP-0054-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-11", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-11", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-11", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-11", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "restockable returns falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_scale_calibration_age_days_12(record):
    """Evaluate scale calibration age for control WP-0054-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-12", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-12", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-12", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-12", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scale calibration age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_mobile_scan_success_pct_13(record):
    """Evaluate mobile scan success for control WP-0054-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_scan_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-13", "metric": "mobile_scan_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-13", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-13", "metric": "mobile_scan_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-13", "metric": "mobile_scan_success_pct", "label": "mobile scan success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "mobile scan success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_dimension_capture_pct_14(record):
    """Evaluate dimension capture rate for control WP-0054-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimension_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-14", "metric": "dimension_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-14", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-14", "metric": "dimension_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-14", "metric": "dimension_capture_pct", "label": "dimension capture rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "dimension capture rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_chain_of_custody_pct_15(record):
    """Evaluate chain of custody for control WP-0054-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_of_custody_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-15", "metric": "chain_of_custody_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-15", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-15", "metric": "chain_of_custody_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-15", "metric": "chain_of_custody_pct", "label": "chain of custody",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "chain of custody falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_product_core_temp_c_16(record):
    """Evaluate product core temperature for control WP-0054-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_core_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-16", "metric": "product_core_temp_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-16", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-16", "metric": "product_core_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-16", "metric": "product_core_temp_c", "label": "product core temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product core temperature must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_return_fraud_score_17(record):
    """Evaluate return fraud score for control WP-0054-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_fraud_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-17", "metric": "return_fraud_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-17", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-17", "metric": "return_fraud_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-17", "metric": "return_fraud_score", "label": "return fraud score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "return fraud score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_pedestrian_separation_pct_18(record):
    """Evaluate pedestrian separation compliance for control WP-0054-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pedestrian_separation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-18", "metric": "pedestrian_separation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-18", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-18", "metric": "pedestrian_separation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-18", "metric": "pedestrian_separation_pct", "label": "pedestrian separation compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "pedestrian separation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_robot_safety_stop_count_19(record):
    """Evaluate robot safety stops for control WP-0054-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_safety_stop_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-19", "metric": "robot_safety_stop_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-19", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-19", "metric": "robot_safety_stop_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-19", "metric": "robot_safety_stop_count", "label": "robot safety stops",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "robot safety stops falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_runbook_test_age_days_20(record):
    """Evaluate runbook test age for control WP-0054-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-20", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-20", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-20", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-20", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "runbook test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_warehouse_sync_age_minutes_21(record):
    """Evaluate warehouse sync age for control WP-0054-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-21", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-21", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-21", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-21", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "warehouse sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_recall_notification_pct_22(record):
    """Evaluate recall notification completion for control WP-0054-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-22", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-22", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-22", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-22", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "recall notification completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_receiving_queue_orders_23(record):
    """Evaluate receiving queue for control WP-0054-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-23", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-23", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-23", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-23", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "low", "unit": "orders",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "receiving queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_customer_retention_pct_24(record):
    """Evaluate customer retention for control WP-0054-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0054-24", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0054-24", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0054-24", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0054-24", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer retention must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_supplier_sso_success_pct_01, assess_supplier_anonymization_score_02, assess_supplier_framework_coverage_pct_03, assess_supplier_rebate_capture_pct_04, assess_supplier_cycle_count_age_days_05, assess_supplier_data_migration_match_pct_06, assess_reserved_qty_07, assess_truck_fill_pct_08, assess_proof_of_delivery_pct_09, assess_duplicate_sku_count_10, assess_restockable_return_pct_11, assess_scale_calibration_age_days_12, assess_mobile_scan_success_pct_13, assess_dimension_capture_pct_14, assess_chain_of_custody_pct_15, assess_product_core_temp_c_16, assess_return_fraud_score_17, assess_pedestrian_separation_pct_18, assess_robot_safety_stop_count_19, assess_runbook_test_age_days_20, assess_warehouse_sync_age_minutes_21, assess_recall_notification_pct_22, assess_receiving_queue_orders_23, assess_customer_retention_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

