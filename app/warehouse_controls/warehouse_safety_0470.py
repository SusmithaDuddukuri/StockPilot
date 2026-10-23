"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_pick_short_count_01(record):
    """Evaluate pick shorts for control WP-0470-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-01", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-01", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-01", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-01", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "high", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick shorts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_broker_response_hours_02(record):
    """Evaluate broker response time for control WP-0470-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-02", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-02", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-02", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-02", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "broker response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_route_emissions_variance_pct_03(record):
    """Evaluate route emissions variance for control WP-0470-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-03", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-03", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-03", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-03", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "route emissions variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_lines_per_labor_hour_04(record):
    """Evaluate lines per labor hour for control WP-0470-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-04", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-04", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-04", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-04", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "medium", "unit": "lines/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lines per labor hour must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_corrective_action_age_days_05(record):
    """Evaluate supplier corrective-action age for control WP-0470-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-05", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-05", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-05", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-05", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier corrective-action age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_quality_escape_count_06(record):
    """Evaluate supplier quality escapes for control WP-0470-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-06", "metric": "supplier_quality_escape_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-06", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-06", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-06", "metric": "supplier_quality_escape_count", "label": "supplier quality escapes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier quality escapes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_payment_dispute_age_days_07(record):
    """Evaluate supplier payment dispute age for control WP-0470-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-07", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-07", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-07", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-07", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "supplier payment dispute age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_problem_record_age_days_08(record):
    """Evaluate supplier problem-record age for control WP-0470-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-08", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-08", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-08", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-08", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier problem-record age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_packaging_spec_match_pct_09(record):
    """Evaluate supplier packaging specification match for control WP-0470-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-09", "metric": "supplier_packaging_spec_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-09", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-09", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-09", "metric": "supplier_packaging_spec_match_pct", "label": "supplier packaging specification match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging specification match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_tamper_control_pct_10(record):
    """Evaluate supplier tamper control for control WP-0470-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tamper_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-10", "metric": "supplier_tamper_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-10", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-10", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-10", "metric": "supplier_tamper_control_pct", "label": "supplier tamper control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "supplier tamper control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_process_change_notice_days_11(record):
    """Evaluate supplier process-change notice for control WP-0470-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-11", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-11", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-11", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-11", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier process-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_rohs_compliance_pct_12(record):
    """Evaluate supplier RoHS compliance for control WP-0470-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-12", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-12", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-12", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-12", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier RoHS compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_adverse_media_review_age_days_13(record):
    """Evaluate supplier adverse-media review age for control WP-0470-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-13", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-13", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-13", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-13", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier adverse-media review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_water_storage_hours_14(record):
    """Evaluate supplier water storage for control WP-0470-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-14", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-14", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-14", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-14", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier water storage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_data_quality_score_15(record):
    """Evaluate supplier data quality for control WP-0470-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-15", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-15", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-15", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-15", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier data quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_release_canary_error_pct_16(record):
    """Evaluate supplier canary error rate for control WP-0470-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_canary_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-16", "metric": "supplier_release_canary_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-16", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-16", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-16", "metric": "supplier_release_canary_error_pct", "label": "supplier canary error rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier canary error rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_mfa_coverage_pct_17(record):
    """Evaluate supplier MFA coverage for control WP-0470-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-17", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-17", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-17", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-17", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier MFA coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_breach_notification_minutes_18(record):
    """Evaluate supplier breach notification time for control WP-0470-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-18", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-18", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-18", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-18", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier breach notification time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_waiver_expiry_days_19(record):
    """Evaluate supplier waiver validity for control WP-0470-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-19", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-19", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-19", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-19", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "supplier waiver validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_early_payment_discount_capture_pct_20(record):
    """Evaluate early-payment discount capture for control WP-0470-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-20", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-20", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-20", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-20", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "early-payment discount capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_finished_goods_cover_days_21(record):
    """Evaluate supplier finished-goods cover for control WP-0470-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-21", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-21", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-21", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-21", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier finished-goods cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_migration_rehearsal_age_days_22(record):
    """Evaluate supplier migration rehearsal age for control WP-0470-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_migration_rehearsal_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-22", "metric": "supplier_migration_rehearsal_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-22", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-22", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-22", "metric": "supplier_migration_rehearsal_age_days", "label": "supplier migration rehearsal age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "supplier migration rehearsal age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_exit_signoff_pct_23(record):
    """Evaluate supplier exit signoff for control WP-0470-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-23", "metric": "supplier_exit_signoff_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-23", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-23", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-23", "metric": "supplier_exit_signoff_pct", "label": "supplier exit signoff",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier exit signoff falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_labor_hours_24(record):
    """Evaluate labor hours for control WP-0470-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0470-24", "metric": "labor_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0470-24", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0470-24", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0470-24", "metric": "labor_hours", "label": "labor hours",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "labor hours must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_pick_short_count_01, assess_broker_response_hours_02, assess_route_emissions_variance_pct_03, assess_lines_per_labor_hour_04, assess_supplier_corrective_action_age_days_05, assess_supplier_quality_escape_count_06, assess_supplier_payment_dispute_age_days_07, assess_supplier_problem_record_age_days_08, assess_supplier_packaging_spec_match_pct_09, assess_supplier_tamper_control_pct_10, assess_supplier_process_change_notice_days_11, assess_supplier_rohs_compliance_pct_12, assess_supplier_adverse_media_review_age_days_13, assess_supplier_water_storage_hours_14, assess_supplier_data_quality_score_15, assess_supplier_release_canary_error_pct_16, assess_supplier_mfa_coverage_pct_17, assess_supplier_breach_notification_minutes_18, assess_supplier_waiver_expiry_days_19, assess_supplier_early_payment_discount_capture_pct_20, assess_supplier_finished_goods_cover_days_21, assess_supplier_migration_rehearsal_age_days_22, assess_supplier_exit_signoff_pct_23, assess_labor_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

