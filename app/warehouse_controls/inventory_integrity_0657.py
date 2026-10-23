"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_dimensioning_error_pct_01(record):
    """Evaluate dimensioning error for control WP-0657-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-01", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-01", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-01", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-01", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "dimensioning error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_blind_count_compliance_pct_02(record):
    """Evaluate blind count compliance for control WP-0657-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-02", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-02", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-02", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-02", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "blind count compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_pick_short_count_03(record):
    """Evaluate pick shorts for control WP-0657-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-03", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-03", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-03", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-03", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "critical", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick shorts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_broker_response_hours_04(record):
    """Evaluate broker response time for control WP-0657-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-04", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-04", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-04", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-04", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "broker response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_route_emissions_variance_pct_05(record):
    """Evaluate route emissions variance for control WP-0657-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-05", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-05", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-05", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-05", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "route emissions variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_lines_per_labor_hour_06(record):
    """Evaluate lines per labor hour for control WP-0657-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-06", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines/hour",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-06", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-06", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-06", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "high", "unit": "lines/hour",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "lines per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_corrective_action_age_days_07(record):
    """Evaluate supplier corrective-action age for control WP-0657-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-07", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-07", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-07", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-07", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier corrective-action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_quality_escape_count_08(record):
    """Evaluate supplier quality escapes for control WP-0657-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-08", "metric": "supplier_quality_escape_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-08", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-08", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-08", "metric": "supplier_quality_escape_count", "label": "supplier quality escapes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier quality escapes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_payment_dispute_age_days_09(record):
    """Evaluate supplier payment dispute age for control WP-0657-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-09", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-09", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-09", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-09", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier payment dispute age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_problem_record_age_days_10(record):
    """Evaluate supplier problem-record age for control WP-0657-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-10", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-10", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-10", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-10", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier problem-record age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_packaging_spec_match_pct_11(record):
    """Evaluate supplier packaging specification match for control WP-0657-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-11", "metric": "supplier_packaging_spec_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-11", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-11", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-11", "metric": "supplier_packaging_spec_match_pct", "label": "supplier packaging specification match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier packaging specification match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_tamper_control_pct_12(record):
    """Evaluate supplier tamper control for control WP-0657-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tamper_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-12", "metric": "supplier_tamper_control_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-12", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-12", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-12", "metric": "supplier_tamper_control_pct", "label": "supplier tamper control",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tamper control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_process_change_notice_days_13(record):
    """Evaluate supplier process-change notice for control WP-0657-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-13", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-13", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-13", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-13", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier process-change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_rohs_compliance_pct_14(record):
    """Evaluate supplier RoHS compliance for control WP-0657-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-14", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-14", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-14", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-14", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "supplier RoHS compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_adverse_media_review_age_days_15(record):
    """Evaluate supplier adverse-media review age for control WP-0657-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-15", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-15", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-15", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-15", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier adverse-media review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_water_storage_hours_16(record):
    """Evaluate supplier water storage for control WP-0657-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-16", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-16", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-16", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-16", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier water storage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_data_quality_score_17(record):
    """Evaluate supplier data quality for control WP-0657-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-17", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-17", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-17", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-17", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier data quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_release_canary_error_pct_18(record):
    """Evaluate supplier canary error rate for control WP-0657-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_canary_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-18", "metric": "supplier_release_canary_error_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-18", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-18", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-18", "metric": "supplier_release_canary_error_pct", "label": "supplier canary error rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier canary error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_mfa_coverage_pct_19(record):
    """Evaluate supplier MFA coverage for control WP-0657-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-19", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-19", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-19", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-19", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier MFA coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_breach_notification_minutes_20(record):
    """Evaluate supplier breach notification time for control WP-0657-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-20", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-20", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-20", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-20", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier breach notification time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_waiver_expiry_days_21(record):
    """Evaluate supplier waiver validity for control WP-0657-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-21", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-21", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-21", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-21", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier waiver validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_early_payment_discount_capture_pct_22(record):
    """Evaluate early-payment discount capture for control WP-0657-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-22", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-22", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-22", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-22", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "early-payment discount capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_finished_goods_cover_days_23(record):
    """Evaluate supplier finished-goods cover for control WP-0657-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-23", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-23", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-23", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-23", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier finished-goods cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_migration_rehearsal_age_days_24(record):
    """Evaluate supplier migration rehearsal age for control WP-0657-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_migration_rehearsal_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0657-24", "metric": "supplier_migration_rehearsal_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0657-24", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0657-24", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0657-24", "metric": "supplier_migration_rehearsal_age_days", "label": "supplier migration rehearsal age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier migration rehearsal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_dimensioning_error_pct_01, assess_blind_count_compliance_pct_02, assess_pick_short_count_03, assess_broker_response_hours_04, assess_route_emissions_variance_pct_05, assess_lines_per_labor_hour_06, assess_supplier_corrective_action_age_days_07, assess_supplier_quality_escape_count_08, assess_supplier_payment_dispute_age_days_09, assess_supplier_problem_record_age_days_10, assess_supplier_packaging_spec_match_pct_11, assess_supplier_tamper_control_pct_12, assess_supplier_process_change_notice_days_13, assess_supplier_rohs_compliance_pct_14, assess_supplier_adverse_media_review_age_days_15, assess_supplier_water_storage_hours_16, assess_supplier_data_quality_score_17, assess_supplier_release_canary_error_pct_18, assess_supplier_mfa_coverage_pct_19, assess_supplier_breach_notification_minutes_20, assess_supplier_waiver_expiry_days_21, assess_supplier_early_payment_discount_capture_pct_22, assess_supplier_finished_goods_cover_days_23, assess_supplier_migration_rehearsal_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

