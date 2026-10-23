"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_role_review_age_days_01(record):
    """Evaluate role review age for control WP-0402-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-01", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-01", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-01", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-01", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "role review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_dimensioning_error_pct_02(record):
    """Evaluate dimensioning error for control WP-0402-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-02", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-02", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-02", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-02", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "dimensioning error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_blind_count_compliance_pct_03(record):
    """Evaluate blind count compliance for control WP-0402-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-03", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-03", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-03", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-03", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "blind count compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_pick_short_count_04(record):
    """Evaluate pick shorts for control WP-0402-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-04", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-04", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-04", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-04", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "medium", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick shorts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_broker_response_hours_05(record):
    """Evaluate broker response time for control WP-0402-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-05", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-05", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-05", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-05", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "broker response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_route_emissions_variance_pct_06(record):
    """Evaluate route emissions variance for control WP-0402-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-06", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-06", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-06", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-06", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "route emissions variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_lines_per_labor_hour_07(record):
    """Evaluate lines per labor hour for control WP-0402-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-07", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "lines/hour",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-07", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-07", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-07", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "low", "unit": "lines/hour",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "lines per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_corrective_action_age_days_08(record):
    """Evaluate supplier corrective-action age for control WP-0402-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-08", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-08", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-08", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-08", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier corrective-action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_quality_escape_count_09(record):
    """Evaluate supplier quality escapes for control WP-0402-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-09", "metric": "supplier_quality_escape_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-09", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-09", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-09", "metric": "supplier_quality_escape_count", "label": "supplier quality escapes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier quality escapes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_payment_dispute_age_days_10(record):
    """Evaluate supplier payment dispute age for control WP-0402-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-10", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-10", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-10", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-10", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier payment dispute age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_problem_record_age_days_11(record):
    """Evaluate supplier problem-record age for control WP-0402-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-11", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-11", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-11", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-11", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "supplier problem-record age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_packaging_spec_match_pct_12(record):
    """Evaluate supplier packaging specification match for control WP-0402-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-12", "metric": "supplier_packaging_spec_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-12", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-12", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-12", "metric": "supplier_packaging_spec_match_pct", "label": "supplier packaging specification match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier packaging specification match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_tamper_control_pct_13(record):
    """Evaluate supplier tamper control for control WP-0402-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tamper_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-13", "metric": "supplier_tamper_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-13", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-13", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-13", "metric": "supplier_tamper_control_pct", "label": "supplier tamper control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tamper control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_process_change_notice_days_14(record):
    """Evaluate supplier process-change notice for control WP-0402-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-14", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-14", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-14", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-14", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier process-change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_rohs_compliance_pct_15(record):
    """Evaluate supplier RoHS compliance for control WP-0402-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-15", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-15", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-15", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-15", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "supplier RoHS compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_adverse_media_review_age_days_16(record):
    """Evaluate supplier adverse-media review age for control WP-0402-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-16", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-16", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-16", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-16", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier adverse-media review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_water_storage_hours_17(record):
    """Evaluate supplier water storage for control WP-0402-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-17", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-17", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-17", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-17", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier water storage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_data_quality_score_18(record):
    """Evaluate supplier data quality for control WP-0402-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-18", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-18", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-18", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-18", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier data quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_release_canary_error_pct_19(record):
    """Evaluate supplier canary error rate for control WP-0402-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_canary_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-19", "metric": "supplier_release_canary_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-19", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-19", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-19", "metric": "supplier_release_canary_error_pct", "label": "supplier canary error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "supplier canary error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_mfa_coverage_pct_20(record):
    """Evaluate supplier MFA coverage for control WP-0402-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-20", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-20", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-20", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-20", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier MFA coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_breach_notification_minutes_21(record):
    """Evaluate supplier breach notification time for control WP-0402-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-21", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-21", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-21", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-21", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier breach notification time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_waiver_expiry_days_22(record):
    """Evaluate supplier waiver validity for control WP-0402-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-22", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-22", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-22", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-22", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier waiver validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_early_payment_discount_capture_pct_23(record):
    """Evaluate early-payment discount capture for control WP-0402-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-23", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-23", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-23", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-23", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "early-payment discount capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_finished_goods_cover_days_24(record):
    """Evaluate supplier finished-goods cover for control WP-0402-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0402-24", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0402-24", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0402-24", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0402-24", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier finished-goods cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_role_review_age_days_01, assess_dimensioning_error_pct_02, assess_blind_count_compliance_pct_03, assess_pick_short_count_04, assess_broker_response_hours_05, assess_route_emissions_variance_pct_06, assess_lines_per_labor_hour_07, assess_supplier_corrective_action_age_days_08, assess_supplier_quality_escape_count_09, assess_supplier_payment_dispute_age_days_10, assess_supplier_problem_record_age_days_11, assess_supplier_packaging_spec_match_pct_12, assess_supplier_tamper_control_pct_13, assess_supplier_process_change_notice_days_14, assess_supplier_rohs_compliance_pct_15, assess_supplier_adverse_media_review_age_days_16, assess_supplier_water_storage_hours_17, assess_supplier_data_quality_score_18, assess_supplier_release_canary_error_pct_19, assess_supplier_mfa_coverage_pct_20, assess_supplier_breach_notification_minutes_21, assess_supplier_waiver_expiry_days_22, assess_supplier_early_payment_discount_capture_pct_23, assess_supplier_finished_goods_cover_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

