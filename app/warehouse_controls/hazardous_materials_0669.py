"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_route_risk_score_01(record):
    """Evaluate supplier route risk for control WP-0669-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-01", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-01", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-01", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-01", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier route risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_training_record_pct_02(record):
    """Evaluate supplier training-record completeness for control WP-0669-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-02", "metric": "supplier_training_record_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-02", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-02", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-02", "metric": "supplier_training_record_pct", "label": "supplier training-record completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier training-record completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_payment_delay_days_03(record):
    """Evaluate supplier payment delay for control WP-0669-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-03", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-03", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-03", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-03", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_takeback_compliance_pct_04(record):
    """Evaluate supplier take-back compliance for control WP-0669-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-04", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-04", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-04", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-04", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier take-back compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_inventory_visibility_pct_05(record):
    """Evaluate supplier inventory visibility for control WP-0669-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-05", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-05", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-05", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-05", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier inventory visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_capability_study_age_days_06(record):
    """Evaluate supplier capability-study age for control WP-0669-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-06", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-06", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-06", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-06", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier capability-study age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_worker_grievance_age_days_07(record):
    """Evaluate supplier worker grievance age for control WP-0669-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-07", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-07", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-07", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-07", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier worker grievance age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_credit_rating_score_08(record):
    """Evaluate supplier credit rating for control WP-0669-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-08", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-08", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-08", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-08", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit rating must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_internal_audit_age_days_09(record):
    """Evaluate supplier internal audit age for control WP-0669-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_internal_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-09", "metric": "supplier_internal_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-09", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-09", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-09", "metric": "supplier_internal_audit_age_days", "label": "supplier internal audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier internal audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_prompt_injection_test_age_days_10(record):
    """Evaluate supplier prompt-injection test age for control WP-0669-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prompt_injection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-10", "metric": "supplier_prompt_injection_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-10", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-10", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-10", "metric": "supplier_prompt_injection_test_age_days", "label": "supplier prompt-injection test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier prompt-injection test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_correlation_id_missing_pct_11(record):
    """Evaluate supplier correlation ID missing for control WP-0669-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_correlation_id_missing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-11", "metric": "supplier_correlation_id_missing_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-11", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-11", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-11", "metric": "supplier_correlation_id_missing_pct", "label": "supplier correlation ID missing",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier correlation ID missing must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_static_analysis_pct_12(record):
    """Evaluate supplier static analysis coverage for control WP-0669-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_static_analysis_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-12", "metric": "supplier_static_analysis_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-12", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-12", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-12", "metric": "supplier_static_analysis_pct", "label": "supplier static analysis coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier static analysis coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_joiner_mover_leaver_age_hours_13(record):
    """Evaluate supplier JML processing time for control WP-0669-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joiner_mover_leaver_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-13", "metric": "supplier_joiner_mover_leaver_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-13", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-13", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-13", "metric": "supplier_joiner_mover_leaver_age_hours", "label": "supplier JML processing time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier JML processing time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_unusual_price_signal_14(record):
    """Evaluate supplier unusual-price signal for control WP-0669-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_unusual_price_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-14", "metric": "supplier_unusual_price_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-14", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-14", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-14", "metric": "supplier_unusual_price_signal", "label": "supplier unusual-price signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier unusual-price signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_delivery_window_change_count_15(record):
    """Evaluate delivery-window changes for control WP-0669-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_window_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-15", "metric": "supplier_delivery_window_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-15", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-15", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-15", "metric": "supplier_delivery_window_change_count", "label": "delivery-window changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery-window changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_invoice_upload_age_hours_16(record):
    """Evaluate supplier invoice upload age for control WP-0669-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-16", "metric": "supplier_invoice_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-16", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-16", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-16", "metric": "supplier_invoice_upload_age_hours", "label": "supplier invoice upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier invoice upload age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dns_cutover_age_hours_17(record):
    """Evaluate supplier DNS cutover age for control WP-0669-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dns_cutover_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-17", "metric": "supplier_dns_cutover_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-17", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-17", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-17", "metric": "supplier_dns_cutover_age_hours", "label": "supplier DNS cutover age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier DNS cutover age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_pack_rate_18(record):
    """Evaluate packing rate for control WP-0669-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-18", "metric": "pack_rate",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders/hour",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-18", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-18", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-18", "metric": "pack_rate", "label": "packing rate",
        "status": "breach", "severity": "high", "unit": "orders/hour",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "packing rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_forklift_inspection_age_days_19(record):
    """Evaluate inspection age for control WP-0669-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-19", "metric": "forklift_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-19", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-19", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-19", "metric": "forklift_inspection_age_days", "label": "inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inspection age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_audit_gap_count_20(record):
    """Evaluate audit gaps for control WP-0669-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-20", "metric": "audit_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-20", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-20", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-20", "metric": "audit_gap_count", "label": "audit gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_stockout_hours_21(record):
    """Evaluate stockout duration for control WP-0669-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stockout_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-21", "metric": "stockout_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-21", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-21", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-21", "metric": "stockout_hours", "label": "stockout duration",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "stockout duration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_driver_hours_remaining_22(record):
    """Evaluate driver hours remaining for control WP-0669-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_hours_remaining")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-22", "metric": "driver_hours_remaining",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-22", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-22", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-22", "metric": "driver_hours_remaining", "label": "driver hours remaining",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "driver hours remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_privileged_account_count_23(record):
    """Evaluate privileged accounts for control WP-0669-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privileged_account_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-23", "metric": "privileged_account_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "accounts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-23", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-23", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-23", "metric": "privileged_account_count", "label": "privileged accounts",
        "status": "breach", "severity": "critical", "unit": "accounts",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "privileged accounts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_handover_gap_count_24(record):
    """Evaluate handover gaps for control WP-0669-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0669-24", "metric": "handover_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0669-24", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0669-24", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0669-24", "metric": "handover_gap_count", "label": "handover gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "handover gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_route_risk_score_01, assess_supplier_training_record_pct_02, assess_supplier_payment_delay_days_03, assess_supplier_takeback_compliance_pct_04, assess_supplier_inventory_visibility_pct_05, assess_supplier_capability_study_age_days_06, assess_supplier_worker_grievance_age_days_07, assess_supplier_credit_rating_score_08, assess_supplier_internal_audit_age_days_09, assess_supplier_prompt_injection_test_age_days_10, assess_supplier_correlation_id_missing_pct_11, assess_supplier_static_analysis_pct_12, assess_supplier_joiner_mover_leaver_age_hours_13, assess_supplier_unusual_price_signal_14, assess_supplier_delivery_window_change_count_15, assess_supplier_invoice_upload_age_hours_16, assess_supplier_dns_cutover_age_hours_17, assess_pack_rate_18, assess_forklift_inspection_age_days_19, assess_audit_gap_count_20, assess_stockout_hours_21, assess_driver_hours_remaining_22, assess_privileged_account_count_23, assess_handover_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

