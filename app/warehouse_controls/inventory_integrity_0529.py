"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_schema_drift_count_01(record):
    """Evaluate schema drift events for control WP-0529-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("schema_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-01", "metric": "schema_drift_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-01", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-01", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-01", "metric": "schema_drift_count", "label": "schema drift events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "schema drift events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_sku_master_gap_count_02(record):
    """Evaluate SKU master gaps for control WP-0529-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sku_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-02", "metric": "sku_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-02", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-02", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-02", "metric": "sku_master_gap_count", "label": "SKU master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "SKU master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_dead_stock_value_03(record):
    """Evaluate dead stock value for control WP-0529-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-03", "metric": "dead_stock_value",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-03", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-03", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-03", "metric": "dead_stock_value", "label": "dead stock value",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dead stock value must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_label_purchase_cost_04(record):
    """Evaluate label purchase cost for control WP-0529-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_purchase_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-04", "metric": "label_purchase_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-04", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-04", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-04", "metric": "label_purchase_cost", "label": "label purchase cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "label purchase cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_country_risk_score_05(record):
    """Evaluate country risk score for control WP-0529-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-05", "metric": "country_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-05", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-05", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-05", "metric": "country_risk_score", "label": "country risk score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "country risk score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_vehicle_insurance_days_left_06(record):
    """Evaluate vehicle insurance validity for control WP-0529-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-06", "metric": "vehicle_insurance_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-06", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-06", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-06", "metric": "vehicle_insurance_days_left", "label": "vehicle insurance validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "vehicle insurance validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_vendor_invoice_age_days_07(record):
    """Evaluate vendor invoice age for control WP-0529-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vendor_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-07", "metric": "vendor_invoice_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-07", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-07", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-07", "metric": "vendor_invoice_age_days", "label": "vendor invoice age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vendor invoice age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_tooling_risk_score_08(record):
    """Evaluate supplier tooling risk for control WP-0529-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-08", "metric": "supplier_tooling_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-08", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-08", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-08", "metric": "supplier_tooling_risk_score", "label": "supplier tooling risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tooling risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_gauge_calibration_age_days_09(record):
    """Evaluate supplier gauge calibration age for control WP-0529-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gauge_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-09", "metric": "supplier_gauge_calibration_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-09", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-09", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-09", "metric": "supplier_gauge_calibration_age_days", "label": "supplier gauge calibration age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier gauge calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_customs_code_accuracy_pct_10(record):
    """Evaluate supplier customs-code accuracy for control WP-0529-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customs_code_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-10", "metric": "supplier_customs_code_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-10", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-10", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-10", "metric": "supplier_customs_code_accuracy_pct", "label": "supplier customs-code accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier customs-code accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_data_return_age_days_11(record):
    """Evaluate supplier data-return age for control WP-0529-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-11", "metric": "supplier_data_return_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-11", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-11", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-11", "metric": "supplier_data_return_age_days", "label": "supplier data-return age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-return age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_warranty_compliance_pct_12(record):
    """Evaluate supplier warranty compliance for control WP-0529-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warranty_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-12", "metric": "supplier_warranty_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-12", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-12", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-12", "metric": "supplier_warranty_compliance_pct", "label": "supplier warranty compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier warranty compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_delivery_exception_age_hours_13(record):
    """Evaluate supplier delivery exception age for control WP-0529-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-13", "metric": "supplier_delivery_exception_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-13", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-13", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-13", "metric": "supplier_delivery_exception_age_hours", "label": "supplier delivery exception age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier delivery exception age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_concession_expiry_days_14(record):
    """Evaluate supplier concession validity for control WP-0529-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concession_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-14", "metric": "supplier_concession_expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-14", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-14", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-14", "metric": "supplier_concession_expiry_days", "label": "supplier concession validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "supplier concession validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_emergency_contact_age_days_15(record):
    """Evaluate supplier emergency-contact age for control WP-0529-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-15", "metric": "supplier_emergency_contact_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-15", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-15", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-15", "metric": "supplier_emergency_contact_age_days", "label": "supplier emergency-contact age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier emergency-contact age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_credit_limit_utilization_pct_16(record):
    """Evaluate supplier credit limit utilization for control WP-0529-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_limit_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-16", "metric": "supplier_credit_limit_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-16", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-16", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-16", "metric": "supplier_credit_limit_utilization_pct", "label": "supplier credit limit utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit limit utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_skill_matrix_age_days_17(record):
    """Evaluate supplier skill-matrix age for control WP-0529-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_skill_matrix_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-17", "metric": "supplier_skill_matrix_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-17", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-17", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-17", "metric": "supplier_skill_matrix_age_days", "label": "supplier skill-matrix age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier skill-matrix age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_explainability_compliance_pct_18(record):
    """Evaluate supplier explainability compliance for control WP-0529-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_explainability_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-18", "metric": "supplier_explainability_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-18", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-18", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-18", "metric": "supplier_explainability_compliance_pct", "label": "supplier explainability compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "supplier explainability compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_event_replay_test_age_days_19(record):
    """Evaluate supplier event replay test age for control WP-0529-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_replay_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-19", "metric": "supplier_event_replay_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-19", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-19", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-19", "metric": "supplier_event_replay_test_age_days", "label": "supplier event replay test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier event replay test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_security_event_review_age_hours_20(record):
    """Evaluate supplier security-event review age for control WP-0529-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_event_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-20", "metric": "supplier_security_event_review_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-20", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-20", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-20", "metric": "supplier_security_event_review_age_hours", "label": "supplier security-event review age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier security-event review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_clean_desk_pct_21(record):
    """Evaluate supplier clean-desk compliance for control WP-0529-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clean_desk_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-21", "metric": "supplier_clean_desk_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-21", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-21", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-21", "metric": "supplier_clean_desk_pct", "label": "supplier clean-desk compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier clean-desk compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_workflow_bypass_count_22(record):
    """Evaluate supplier workflow bypasses for control WP-0529-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_workflow_bypass_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-22", "metric": "supplier_workflow_bypass_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-22", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-22", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-22", "metric": "supplier_workflow_bypass_count", "label": "supplier workflow bypasses",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier workflow bypasses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_minimum_commitment_variance_pct_23(record):
    """Evaluate minimum commitment variance for control WP-0529-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-23", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-23", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-23", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-23", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "minimum commitment variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_pack_accuracy_pct_24(record):
    """Evaluate supplier pack accuracy for control WP-0529-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0529-24", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0529-24", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0529-24", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0529-24", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier pack accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_schema_drift_count_01, assess_sku_master_gap_count_02, assess_dead_stock_value_03, assess_label_purchase_cost_04, assess_country_risk_score_05, assess_vehicle_insurance_days_left_06, assess_vendor_invoice_age_days_07, assess_supplier_tooling_risk_score_08, assess_supplier_gauge_calibration_age_days_09, assess_supplier_customs_code_accuracy_pct_10, assess_supplier_data_return_age_days_11, assess_supplier_warranty_compliance_pct_12, assess_supplier_delivery_exception_age_hours_13, assess_supplier_concession_expiry_days_14, assess_supplier_emergency_contact_age_days_15, assess_supplier_credit_limit_utilization_pct_16, assess_supplier_skill_matrix_age_days_17, assess_supplier_explainability_compliance_pct_18, assess_supplier_event_replay_test_age_days_19, assess_supplier_security_event_review_age_hours_20, assess_supplier_clean_desk_pct_21, assess_supplier_workflow_bypass_count_22, assess_supplier_minimum_commitment_variance_pct_23, assess_supplier_pack_accuracy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

