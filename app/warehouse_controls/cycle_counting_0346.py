"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_fuel_surcharge_variance_pct_01(record):
    """Evaluate fuel surcharge variance for control WP-0346-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-01", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-01", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-01", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-01", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fuel surcharge variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_highway_restriction_match_count_02(record):
    """Evaluate highway restriction matches for control WP-0346-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-02", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-02", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-02", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-02", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "highway restriction matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_recovery_plan_age_days_03(record):
    """Evaluate supplier recovery plan age for control WP-0346-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-03", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-03", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-03", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-03", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier recovery plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_energy_intensity_04(record):
    """Evaluate supplier energy intensity for control WP-0346-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-04", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-04", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-04", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-04", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy intensity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_route_risk_score_05(record):
    """Evaluate supplier route risk for control WP-0346-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-05", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-05", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-05", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-05", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier route risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_training_record_pct_06(record):
    """Evaluate supplier training-record completeness for control WP-0346-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-06", "metric": "supplier_training_record_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-06", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-06", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-06", "metric": "supplier_training_record_pct", "label": "supplier training-record completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier training-record completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_payment_delay_days_07(record):
    """Evaluate supplier payment delay for control WP-0346-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-07", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-07", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-07", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-07", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "supplier payment delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_takeback_compliance_pct_08(record):
    """Evaluate supplier take-back compliance for control WP-0346-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-08", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-08", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-08", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-08", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier take-back compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_inventory_visibility_pct_09(record):
    """Evaluate supplier inventory visibility for control WP-0346-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-09", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-09", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-09", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-09", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier inventory visibility must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_capability_study_age_days_10(record):
    """Evaluate supplier capability-study age for control WP-0346-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-10", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-10", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-10", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-10", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier capability-study age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_worker_grievance_age_days_11(record):
    """Evaluate supplier worker grievance age for control WP-0346-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-11", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-11", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-11", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-11", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "supplier worker grievance age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_credit_rating_score_12(record):
    """Evaluate supplier credit rating for control WP-0346-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-12", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-12", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-12", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-12", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier credit rating must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_internal_audit_age_days_13(record):
    """Evaluate supplier internal audit age for control WP-0346-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_internal_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-13", "metric": "supplier_internal_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-13", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-13", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-13", "metric": "supplier_internal_audit_age_days", "label": "supplier internal audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier internal audit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_prompt_injection_test_age_days_14(record):
    """Evaluate supplier prompt-injection test age for control WP-0346-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prompt_injection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-14", "metric": "supplier_prompt_injection_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-14", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-14", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-14", "metric": "supplier_prompt_injection_test_age_days", "label": "supplier prompt-injection test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier prompt-injection test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_correlation_id_missing_pct_15(record):
    """Evaluate supplier correlation ID missing for control WP-0346-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_correlation_id_missing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-15", "metric": "supplier_correlation_id_missing_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-15", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-15", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-15", "metric": "supplier_correlation_id_missing_pct", "label": "supplier correlation ID missing",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier correlation ID missing falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_static_analysis_pct_16(record):
    """Evaluate supplier static analysis coverage for control WP-0346-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_static_analysis_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-16", "metric": "supplier_static_analysis_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-16", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-16", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-16", "metric": "supplier_static_analysis_pct", "label": "supplier static analysis coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier static analysis coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_joiner_mover_leaver_age_hours_17(record):
    """Evaluate supplier JML processing time for control WP-0346-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joiner_mover_leaver_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-17", "metric": "supplier_joiner_mover_leaver_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-17", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-17", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-17", "metric": "supplier_joiner_mover_leaver_age_hours", "label": "supplier JML processing time",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier JML processing time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_unusual_price_signal_18(record):
    """Evaluate supplier unusual-price signal for control WP-0346-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_unusual_price_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-18", "metric": "supplier_unusual_price_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-18", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-18", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-18", "metric": "supplier_unusual_price_signal", "label": "supplier unusual-price signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier unusual-price signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_delivery_window_change_count_19(record):
    """Evaluate delivery-window changes for control WP-0346-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_window_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-19", "metric": "supplier_delivery_window_change_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-19", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-19", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-19", "metric": "supplier_delivery_window_change_count", "label": "delivery-window changes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "delivery-window changes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_invoice_upload_age_hours_20(record):
    """Evaluate supplier invoice upload age for control WP-0346-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-20", "metric": "supplier_invoice_upload_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-20", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-20", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-20", "metric": "supplier_invoice_upload_age_hours", "label": "supplier invoice upload age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice upload age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_dns_cutover_age_hours_21(record):
    """Evaluate supplier DNS cutover age for control WP-0346-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dns_cutover_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-21", "metric": "supplier_dns_cutover_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-21", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-21", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-21", "metric": "supplier_dns_cutover_age_hours", "label": "supplier DNS cutover age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier DNS cutover age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_pack_rate_22(record):
    """Evaluate packing rate for control WP-0346-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-22", "metric": "pack_rate",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders/hour",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-22", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-22", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-22", "metric": "pack_rate", "label": "packing rate",
        "status": "breach", "severity": "critical", "unit": "orders/hour",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "packing rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_forklift_inspection_age_days_23(record):
    """Evaluate inspection age for control WP-0346-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-23", "metric": "forklift_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-23", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-23", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-23", "metric": "forklift_inspection_age_days", "label": "inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_audit_gap_count_24(record):
    """Evaluate audit gaps for control WP-0346-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0346-24", "metric": "audit_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0346-24", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0346-24", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0346-24", "metric": "audit_gap_count", "label": "audit gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_fuel_surcharge_variance_pct_01, assess_highway_restriction_match_count_02, assess_supplier_recovery_plan_age_days_03, assess_supplier_energy_intensity_04, assess_supplier_route_risk_score_05, assess_supplier_training_record_pct_06, assess_supplier_payment_delay_days_07, assess_supplier_takeback_compliance_pct_08, assess_supplier_inventory_visibility_pct_09, assess_supplier_capability_study_age_days_10, assess_supplier_worker_grievance_age_days_11, assess_supplier_credit_rating_score_12, assess_supplier_internal_audit_age_days_13, assess_supplier_prompt_injection_test_age_days_14, assess_supplier_correlation_id_missing_pct_15, assess_supplier_static_analysis_pct_16, assess_supplier_joiner_mover_leaver_age_hours_17, assess_supplier_unusual_price_signal_18, assess_supplier_delivery_window_change_count_19, assess_supplier_invoice_upload_age_hours_20, assess_supplier_dns_cutover_age_hours_21, assess_pack_rate_22, assess_forklift_inspection_age_days_23, assess_audit_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

