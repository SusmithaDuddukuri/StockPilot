"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_eyewash_test_age_days_01(record):
    """Evaluate eyewash test age for control WP-0645-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-01", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-01", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-01", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-01", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "eyewash test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_return_authorization_age_hours_02(record):
    """Evaluate return authorization age for control WP-0645-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-02", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-02", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-02", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-02", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "return authorization age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_quality_hold_age_days_03(record):
    """Evaluate quality hold age for control WP-0645-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-03", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-03", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-03", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-03", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality hold age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_battery_charge_pct_04(record):
    """Evaluate battery charge for control WP-0645-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-04", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-04", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-04", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-04", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "battery charge must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_first_aid_response_minutes_05(record):
    """Evaluate first aid response time for control WP-0645-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-05", "metric": "first_aid_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-05", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-05", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-05", "metric": "first_aid_response_minutes", "label": "first aid response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "first aid response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_ups_runtime_minutes_06(record):
    """Evaluate UPS runtime for control WP-0645-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ups_runtime_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-06", "metric": "ups_runtime_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-06", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-06", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-06", "metric": "ups_runtime_minutes", "label": "UPS runtime",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "UPS runtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_role_review_age_days_07(record):
    """Evaluate role review age for control WP-0645-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-07", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-07", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-07", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-07", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "role review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_dimensioning_error_pct_08(record):
    """Evaluate dimensioning error for control WP-0645-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-08", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-08", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-08", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-08", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dimensioning error must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_blind_count_compliance_pct_09(record):
    """Evaluate blind count compliance for control WP-0645-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-09", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-09", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-09", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-09", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "blind count compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_pick_short_count_10(record):
    """Evaluate pick shorts for control WP-0645-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-10", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-10", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-10", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-10", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "high", "unit": "lines",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "pick shorts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_broker_response_hours_11(record):
    """Evaluate broker response time for control WP-0645-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-11", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-11", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-11", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-11", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "broker response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_route_emissions_variance_pct_12(record):
    """Evaluate route emissions variance for control WP-0645-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-12", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-12", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-12", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-12", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route emissions variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_lines_per_labor_hour_13(record):
    """Evaluate lines per labor hour for control WP-0645-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-13", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines/hour",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-13", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-13", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-13", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "medium", "unit": "lines/hour",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "lines per labor hour exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_corrective_action_age_days_14(record):
    """Evaluate supplier corrective-action age for control WP-0645-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-14", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-14", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-14", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-14", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier corrective-action age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_quality_escape_count_15(record):
    """Evaluate supplier quality escapes for control WP-0645-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-15", "metric": "supplier_quality_escape_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-15", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-15", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-15", "metric": "supplier_quality_escape_count", "label": "supplier quality escapes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier quality escapes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_payment_dispute_age_days_16(record):
    """Evaluate supplier payment dispute age for control WP-0645-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-16", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-16", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-16", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-16", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment dispute age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_problem_record_age_days_17(record):
    """Evaluate supplier problem-record age for control WP-0645-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-17", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-17", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-17", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-17", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier problem-record age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_packaging_spec_match_pct_18(record):
    """Evaluate supplier packaging specification match for control WP-0645-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-18", "metric": "supplier_packaging_spec_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-18", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-18", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-18", "metric": "supplier_packaging_spec_match_pct", "label": "supplier packaging specification match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier packaging specification match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_tamper_control_pct_19(record):
    """Evaluate supplier tamper control for control WP-0645-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tamper_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-19", "metric": "supplier_tamper_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-19", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-19", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-19", "metric": "supplier_tamper_control_pct", "label": "supplier tamper control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tamper control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_process_change_notice_days_20(record):
    """Evaluate supplier process-change notice for control WP-0645-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-20", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-20", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-20", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-20", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process-change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_rohs_compliance_pct_21(record):
    """Evaluate supplier RoHS compliance for control WP-0645-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-21", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-21", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-21", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-21", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier RoHS compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_adverse_media_review_age_days_22(record):
    """Evaluate supplier adverse-media review age for control WP-0645-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-22", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-22", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-22", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-22", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier adverse-media review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_water_storage_hours_23(record):
    """Evaluate supplier water storage for control WP-0645-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-23", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-23", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-23", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-23", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water storage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_data_quality_score_24(record):
    """Evaluate supplier data quality for control WP-0645-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0645-24", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0645-24", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0645-24", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0645-24", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_eyewash_test_age_days_01, assess_return_authorization_age_hours_02, assess_quality_hold_age_days_03, assess_battery_charge_pct_04, assess_first_aid_response_minutes_05, assess_ups_runtime_minutes_06, assess_role_review_age_days_07, assess_dimensioning_error_pct_08, assess_blind_count_compliance_pct_09, assess_pick_short_count_10, assess_broker_response_hours_11, assess_route_emissions_variance_pct_12, assess_lines_per_labor_hour_13, assess_supplier_corrective_action_age_days_14, assess_supplier_quality_escape_count_15, assess_supplier_payment_dispute_age_days_16, assess_supplier_problem_record_age_days_17, assess_supplier_packaging_spec_match_pct_18, assess_supplier_tamper_control_pct_19, assess_supplier_process_change_notice_days_20, assess_supplier_rohs_compliance_pct_21, assess_supplier_adverse_media_review_age_days_22, assess_supplier_water_storage_hours_23, assess_supplier_data_quality_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

