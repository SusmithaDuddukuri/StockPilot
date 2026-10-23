"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_vehicle_insurance_days_left_01(record):
    """Evaluate vehicle insurance validity for control WP-0031-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-01", "metric": "vehicle_insurance_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-01", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-01", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-01", "metric": "vehicle_insurance_days_left", "label": "vehicle insurance validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle insurance validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_vendor_invoice_age_days_02(record):
    """Evaluate vendor invoice age for control WP-0031-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vendor_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-02", "metric": "vendor_invoice_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-02", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-02", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-02", "metric": "vendor_invoice_age_days", "label": "vendor invoice age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vendor invoice age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_tooling_risk_score_03(record):
    """Evaluate supplier tooling risk for control WP-0031-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-03", "metric": "supplier_tooling_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-03", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-03", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-03", "metric": "supplier_tooling_risk_score", "label": "supplier tooling risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier tooling risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_gauge_calibration_age_days_04(record):
    """Evaluate supplier gauge calibration age for control WP-0031-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gauge_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-04", "metric": "supplier_gauge_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-04", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-04", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-04", "metric": "supplier_gauge_calibration_age_days", "label": "supplier gauge calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "supplier gauge calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_customs_code_accuracy_pct_05(record):
    """Evaluate supplier customs-code accuracy for control WP-0031-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customs_code_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-05", "metric": "supplier_customs_code_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-05", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-05", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-05", "metric": "supplier_customs_code_accuracy_pct", "label": "supplier customs-code accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customs-code accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_data_return_age_days_06(record):
    """Evaluate supplier data-return age for control WP-0031-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-06", "metric": "supplier_data_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-06", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-06", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-06", "metric": "supplier_data_return_age_days", "label": "supplier data-return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data-return age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_warranty_compliance_pct_07(record):
    """Evaluate supplier warranty compliance for control WP-0031-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warranty_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-07", "metric": "supplier_warranty_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-07", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-07", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-07", "metric": "supplier_warranty_compliance_pct", "label": "supplier warranty compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier warranty compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_delivery_exception_age_hours_08(record):
    """Evaluate supplier delivery exception age for control WP-0031-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-08", "metric": "supplier_delivery_exception_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-08", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-08", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-08", "metric": "supplier_delivery_exception_age_hours", "label": "supplier delivery exception age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier delivery exception age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_concession_expiry_days_09(record):
    """Evaluate supplier concession validity for control WP-0031-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concession_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-09", "metric": "supplier_concession_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-09", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-09", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-09", "metric": "supplier_concession_expiry_days", "label": "supplier concession validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier concession validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_emergency_contact_age_days_10(record):
    """Evaluate supplier emergency-contact age for control WP-0031-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-10", "metric": "supplier_emergency_contact_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-10", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-10", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-10", "metric": "supplier_emergency_contact_age_days", "label": "supplier emergency-contact age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier emergency-contact age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_credit_limit_utilization_pct_11(record):
    """Evaluate supplier credit limit utilization for control WP-0031-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_limit_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-11", "metric": "supplier_credit_limit_utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-11", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-11", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-11", "metric": "supplier_credit_limit_utilization_pct", "label": "supplier credit limit utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "supplier credit limit utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_skill_matrix_age_days_12(record):
    """Evaluate supplier skill-matrix age for control WP-0031-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_skill_matrix_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-12", "metric": "supplier_skill_matrix_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-12", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-12", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-12", "metric": "supplier_skill_matrix_age_days", "label": "supplier skill-matrix age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "supplier skill-matrix age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_explainability_compliance_pct_13(record):
    """Evaluate supplier explainability compliance for control WP-0031-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_explainability_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-13", "metric": "supplier_explainability_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-13", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-13", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-13", "metric": "supplier_explainability_compliance_pct", "label": "supplier explainability compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier explainability compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_event_replay_test_age_days_14(record):
    """Evaluate supplier event replay test age for control WP-0031-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_replay_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-14", "metric": "supplier_event_replay_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-14", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-14", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-14", "metric": "supplier_event_replay_test_age_days", "label": "supplier event replay test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier event replay test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_security_event_review_age_hours_15(record):
    """Evaluate supplier security-event review age for control WP-0031-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_event_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-15", "metric": "supplier_security_event_review_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-15", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-15", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-15", "metric": "supplier_security_event_review_age_hours", "label": "supplier security-event review age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "supplier security-event review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_clean_desk_pct_16(record):
    """Evaluate supplier clean-desk compliance for control WP-0031-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clean_desk_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-16", "metric": "supplier_clean_desk_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-16", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-16", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-16", "metric": "supplier_clean_desk_pct", "label": "supplier clean-desk compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier clean-desk compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_workflow_bypass_count_17(record):
    """Evaluate supplier workflow bypasses for control WP-0031-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_workflow_bypass_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-17", "metric": "supplier_workflow_bypass_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-17", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-17", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-17", "metric": "supplier_workflow_bypass_count", "label": "supplier workflow bypasses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier workflow bypasses must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_minimum_commitment_variance_pct_18(record):
    """Evaluate minimum commitment variance for control WP-0031-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-18", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-18", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-18", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-18", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum commitment variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_pack_accuracy_pct_19(record):
    """Evaluate supplier pack accuracy for control WP-0031-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-19", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-19", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-19", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-19", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier pack accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_open_invoice_transfer_pct_20(record):
    """Evaluate open-invoice transfer completeness for control WP-0031-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_invoice_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-20", "metric": "supplier_open_invoice_transfer_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-20", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-20", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-20", "metric": "supplier_open_invoice_transfer_pct", "label": "open-invoice transfer completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "open-invoice transfer completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_unit_cost_21(record):
    """Evaluate unit cost for control WP-0031-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-21", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-21", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-21", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-21", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "unit cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_scan_compliance_pct_22(record):
    """Evaluate scan compliance for control WP-0031-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-22", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-22", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-22", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-22", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scan compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_seasonality_index_23(record):
    """Evaluate seasonality index for control WP-0031-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-23", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-23", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-23", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-23", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "seasonality index exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_reconciliation_delta_24(record):
    """Evaluate reconciliation delta for control WP-0031-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0031-24", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0031-24", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0031-24", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0031-24", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "reconciliation delta falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_vehicle_insurance_days_left_01, assess_vendor_invoice_age_days_02, assess_supplier_tooling_risk_score_03, assess_supplier_gauge_calibration_age_days_04, assess_supplier_customs_code_accuracy_pct_05, assess_supplier_data_return_age_days_06, assess_supplier_warranty_compliance_pct_07, assess_supplier_delivery_exception_age_hours_08, assess_supplier_concession_expiry_days_09, assess_supplier_emergency_contact_age_days_10, assess_supplier_credit_limit_utilization_pct_11, assess_supplier_skill_matrix_age_days_12, assess_supplier_explainability_compliance_pct_13, assess_supplier_event_replay_test_age_days_14, assess_supplier_security_event_review_age_hours_15, assess_supplier_clean_desk_pct_16, assess_supplier_workflow_bypass_count_17, assess_supplier_minimum_commitment_variance_pct_18, assess_supplier_pack_accuracy_pct_19, assess_supplier_open_invoice_transfer_pct_20, assess_unit_cost_21, assess_scan_compliance_pct_22, assess_seasonality_index_23, assess_reconciliation_delta_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

