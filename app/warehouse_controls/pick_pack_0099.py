"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_gauge_calibration_age_days_01(record):
    """Evaluate supplier gauge calibration age for control WP-0099-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gauge_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-01", "metric": "supplier_gauge_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-01", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-01", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-01", "metric": "supplier_gauge_calibration_age_days", "label": "supplier gauge calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier gauge calibration age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_customs_code_accuracy_pct_02(record):
    """Evaluate supplier customs-code accuracy for control WP-0099-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customs_code_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-02", "metric": "supplier_customs_code_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-02", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-02", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-02", "metric": "supplier_customs_code_accuracy_pct", "label": "supplier customs-code accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customs-code accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_data_return_age_days_03(record):
    """Evaluate supplier data-return age for control WP-0099-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-03", "metric": "supplier_data_return_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-03", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-03", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-03", "metric": "supplier_data_return_age_days", "label": "supplier data-return age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier data-return age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_warranty_compliance_pct_04(record):
    """Evaluate supplier warranty compliance for control WP-0099-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warranty_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-04", "metric": "supplier_warranty_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-04", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-04", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-04", "metric": "supplier_warranty_compliance_pct", "label": "supplier warranty compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "supplier warranty compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_delivery_exception_age_hours_05(record):
    """Evaluate supplier delivery exception age for control WP-0099-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-05", "metric": "supplier_delivery_exception_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-05", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-05", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-05", "metric": "supplier_delivery_exception_age_hours", "label": "supplier delivery exception age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier delivery exception age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_concession_expiry_days_06(record):
    """Evaluate supplier concession validity for control WP-0099-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concession_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-06", "metric": "supplier_concession_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-06", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-06", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-06", "metric": "supplier_concession_expiry_days", "label": "supplier concession validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier concession validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_emergency_contact_age_days_07(record):
    """Evaluate supplier emergency-contact age for control WP-0099-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-07", "metric": "supplier_emergency_contact_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-07", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-07", "metric": "supplier_emergency_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-07", "metric": "supplier_emergency_contact_age_days", "label": "supplier emergency-contact age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier emergency-contact age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_credit_limit_utilization_pct_08(record):
    """Evaluate supplier credit limit utilization for control WP-0099-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_limit_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-08", "metric": "supplier_credit_limit_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-08", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-08", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-08", "metric": "supplier_credit_limit_utilization_pct", "label": "supplier credit limit utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "supplier credit limit utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_skill_matrix_age_days_09(record):
    """Evaluate supplier skill-matrix age for control WP-0099-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_skill_matrix_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-09", "metric": "supplier_skill_matrix_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-09", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-09", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-09", "metric": "supplier_skill_matrix_age_days", "label": "supplier skill-matrix age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier skill-matrix age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_explainability_compliance_pct_10(record):
    """Evaluate supplier explainability compliance for control WP-0099-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_explainability_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-10", "metric": "supplier_explainability_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-10", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-10", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-10", "metric": "supplier_explainability_compliance_pct", "label": "supplier explainability compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier explainability compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_event_replay_test_age_days_11(record):
    """Evaluate supplier event replay test age for control WP-0099-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_replay_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-11", "metric": "supplier_event_replay_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-11", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-11", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-11", "metric": "supplier_event_replay_test_age_days", "label": "supplier event replay test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier event replay test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_security_event_review_age_hours_12(record):
    """Evaluate supplier security-event review age for control WP-0099-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_event_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-12", "metric": "supplier_security_event_review_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-12", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-12", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-12", "metric": "supplier_security_event_review_age_hours", "label": "supplier security-event review age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier security-event review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_clean_desk_pct_13(record):
    """Evaluate supplier clean-desk compliance for control WP-0099-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clean_desk_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-13", "metric": "supplier_clean_desk_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-13", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-13", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-13", "metric": "supplier_clean_desk_pct", "label": "supplier clean-desk compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier clean-desk compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_workflow_bypass_count_14(record):
    """Evaluate supplier workflow bypasses for control WP-0099-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_workflow_bypass_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-14", "metric": "supplier_workflow_bypass_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-14", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-14", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-14", "metric": "supplier_workflow_bypass_count", "label": "supplier workflow bypasses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier workflow bypasses must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_minimum_commitment_variance_pct_15(record):
    """Evaluate minimum commitment variance for control WP-0099-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-15", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-15", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-15", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-15", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "minimum commitment variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_pack_accuracy_pct_16(record):
    """Evaluate supplier pack accuracy for control WP-0099-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-16", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-16", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-16", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-16", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier pack accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_open_invoice_transfer_pct_17(record):
    """Evaluate open-invoice transfer completeness for control WP-0099-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_invoice_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-17", "metric": "supplier_open_invoice_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-17", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-17", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-17", "metric": "supplier_open_invoice_transfer_pct", "label": "open-invoice transfer completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-invoice transfer completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_unit_cost_18(record):
    """Evaluate unit cost for control WP-0099-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-18", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-18", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-18", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-18", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unit cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_scan_compliance_pct_19(record):
    """Evaluate scan compliance for control WP-0099-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-19", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-19", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-19", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-19", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "scan compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_seasonality_index_20(record):
    """Evaluate seasonality index for control WP-0099-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-20", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-20", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-20", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-20", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "seasonality index falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_reconciliation_delta_21(record):
    """Evaluate reconciliation delta for control WP-0099-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-21", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-21", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-21", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-21", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reconciliation delta must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_recycling_rate_pct_22(record):
    """Evaluate recycling rate for control WP-0099-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-22", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-22", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-22", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-22", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recycling rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_expiry_capture_pct_23(record):
    """Evaluate expiry capture rate for control WP-0099-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-23", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-23", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-23", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-23", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "expiry capture rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_api_quota_pct_24(record):
    """Evaluate API quota utilization for control WP-0099-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0099-24", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0099-24", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0099-24", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0099-24", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "API quota utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_gauge_calibration_age_days_01, assess_supplier_customs_code_accuracy_pct_02, assess_supplier_data_return_age_days_03, assess_supplier_warranty_compliance_pct_04, assess_supplier_delivery_exception_age_hours_05, assess_supplier_concession_expiry_days_06, assess_supplier_emergency_contact_age_days_07, assess_supplier_credit_limit_utilization_pct_08, assess_supplier_skill_matrix_age_days_09, assess_supplier_explainability_compliance_pct_10, assess_supplier_event_replay_test_age_days_11, assess_supplier_security_event_review_age_hours_12, assess_supplier_clean_desk_pct_13, assess_supplier_workflow_bypass_count_14, assess_supplier_minimum_commitment_variance_pct_15, assess_supplier_pack_accuracy_pct_16, assess_supplier_open_invoice_transfer_pct_17, assess_unit_cost_18, assess_scan_compliance_pct_19, assess_seasonality_index_20, assess_reconciliation_delta_21, assess_recycling_rate_pct_22, assess_expiry_capture_pct_23, assess_api_quota_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

