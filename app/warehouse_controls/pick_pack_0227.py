"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_payment_dispute_age_days_01(record):
    """Evaluate supplier payment dispute age for control WP-0227-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-01", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-01", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-01", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-01", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment dispute age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_problem_record_age_days_02(record):
    """Evaluate supplier problem-record age for control WP-0227-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-02", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-02", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-02", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-02", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier problem-record age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_packaging_spec_match_pct_03(record):
    """Evaluate supplier packaging specification match for control WP-0227-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-03", "metric": "supplier_packaging_spec_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-03", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-03", "metric": "supplier_packaging_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-03", "metric": "supplier_packaging_spec_match_pct", "label": "supplier packaging specification match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier packaging specification match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_tamper_control_pct_04(record):
    """Evaluate supplier tamper control for control WP-0227-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tamper_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-04", "metric": "supplier_tamper_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-04", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-04", "metric": "supplier_tamper_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-04", "metric": "supplier_tamper_control_pct", "label": "supplier tamper control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier tamper control falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_process_change_notice_days_05(record):
    """Evaluate supplier process-change notice for control WP-0227-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-05", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-05", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-05", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-05", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_rohs_compliance_pct_06(record):
    """Evaluate supplier RoHS compliance for control WP-0227-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-06", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-06", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-06", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-06", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier RoHS compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_adverse_media_review_age_days_07(record):
    """Evaluate supplier adverse-media review age for control WP-0227-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-07", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-07", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-07", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-07", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier adverse-media review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_water_storage_hours_08(record):
    """Evaluate supplier water storage for control WP-0227-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-08", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-08", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-08", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-08", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "supplier water storage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_data_quality_score_09(record):
    """Evaluate supplier data quality for control WP-0227-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-09", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-09", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-09", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-09", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_release_canary_error_pct_10(record):
    """Evaluate supplier canary error rate for control WP-0227-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_canary_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-10", "metric": "supplier_release_canary_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-10", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-10", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-10", "metric": "supplier_release_canary_error_pct", "label": "supplier canary error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier canary error rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_mfa_coverage_pct_11(record):
    """Evaluate supplier MFA coverage for control WP-0227-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-11", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-11", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-11", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-11", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier MFA coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_breach_notification_minutes_12(record):
    """Evaluate supplier breach notification time for control WP-0227-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-12", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-12", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-12", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-12", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "supplier breach notification time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_waiver_expiry_days_13(record):
    """Evaluate supplier waiver validity for control WP-0227-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-13", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-13", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-13", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-13", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier waiver validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_early_payment_discount_capture_pct_14(record):
    """Evaluate early-payment discount capture for control WP-0227-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-14", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-14", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-14", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-14", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "early-payment discount capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_finished_goods_cover_days_15(record):
    """Evaluate supplier finished-goods cover for control WP-0227-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-15", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-15", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-15", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-15", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier finished-goods cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_migration_rehearsal_age_days_16(record):
    """Evaluate supplier migration rehearsal age for control WP-0227-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_migration_rehearsal_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-16", "metric": "supplier_migration_rehearsal_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-16", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-16", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-16", "metric": "supplier_migration_rehearsal_age_days", "label": "supplier migration rehearsal age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier migration rehearsal age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_exit_signoff_pct_17(record):
    """Evaluate supplier exit signoff for control WP-0227-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-17", "metric": "supplier_exit_signoff_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-17", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-17", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-17", "metric": "supplier_exit_signoff_pct", "label": "supplier exit signoff",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exit signoff must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_labor_hours_18(record):
    """Evaluate labor hours for control WP-0227-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-18", "metric": "labor_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-18", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-18", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-18", "metric": "labor_hours", "label": "labor hours",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor hours must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_worker_load_pct_19(record):
    """Evaluate worker load for control WP-0227-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_load_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-19", "metric": "worker_load_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-19", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-19", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-19", "metric": "worker_load_pct", "label": "worker load",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "worker load exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_backup_age_hours_20(record):
    """Evaluate backup age for control WP-0227-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-20", "metric": "backup_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-20", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-20", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-20", "metric": "backup_age_hours", "label": "backup age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "backup age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_carrier_claim_rate_pct_21(record):
    """Evaluate carrier claim rate for control WP-0227-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_claim_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-21", "metric": "carrier_claim_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-21", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-21", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-21", "metric": "carrier_claim_rate_pct", "label": "carrier claim rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier claim rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_yard_dwell_hours_22(record):
    """Evaluate yard dwell for control WP-0227-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-22", "metric": "yard_dwell_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-22", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-22", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-22", "metric": "yard_dwell_hours", "label": "yard dwell",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "yard dwell must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_dashboard_load_ms_23(record):
    """Evaluate dashboard load time for control WP-0227-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dashboard_load_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-23", "metric": "dashboard_load_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-23", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-23", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-23", "metric": "dashboard_load_ms", "label": "dashboard load time",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "dashboard load time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_batch_release_age_minutes_24(record):
    """Evaluate batch release age for control WP-0227-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0227-24", "metric": "batch_release_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0227-24", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0227-24", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0227-24", "metric": "batch_release_age_minutes", "label": "batch release age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "batch release age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_payment_dispute_age_days_01, assess_supplier_problem_record_age_days_02, assess_supplier_packaging_spec_match_pct_03, assess_supplier_tamper_control_pct_04, assess_supplier_process_change_notice_days_05, assess_supplier_rohs_compliance_pct_06, assess_supplier_adverse_media_review_age_days_07, assess_supplier_water_storage_hours_08, assess_supplier_data_quality_score_09, assess_supplier_release_canary_error_pct_10, assess_supplier_mfa_coverage_pct_11, assess_supplier_breach_notification_minutes_12, assess_supplier_waiver_expiry_days_13, assess_supplier_early_payment_discount_capture_pct_14, assess_supplier_finished_goods_cover_days_15, assess_supplier_migration_rehearsal_age_days_16, assess_supplier_exit_signoff_pct_17, assess_labor_hours_18, assess_worker_load_pct_19, assess_backup_age_hours_20, assess_carrier_claim_rate_pct_21, assess_yard_dwell_hours_22, assess_dashboard_load_ms_23, assess_batch_release_age_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

