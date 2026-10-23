"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_process_change_notice_days_01(record):
    """Evaluate supplier process-change notice for control WP-0550-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-01", "metric": "supplier_process_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-01", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-01", "metric": "supplier_process_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-01", "metric": "supplier_process_change_notice_days", "label": "supplier process-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process-change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_rohs_compliance_pct_02(record):
    """Evaluate supplier RoHS compliance for control WP-0550-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rohs_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-02", "metric": "supplier_rohs_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-02", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-02", "metric": "supplier_rohs_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-02", "metric": "supplier_rohs_compliance_pct", "label": "supplier RoHS compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "supplier RoHS compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_adverse_media_review_age_days_03(record):
    """Evaluate supplier adverse-media review age for control WP-0550-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adverse_media_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-03", "metric": "supplier_adverse_media_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-03", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-03", "metric": "supplier_adverse_media_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-03", "metric": "supplier_adverse_media_review_age_days", "label": "supplier adverse-media review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "supplier adverse-media review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_water_storage_hours_04(record):
    """Evaluate supplier water storage for control WP-0550-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-04", "metric": "supplier_water_storage_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-04", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-04", "metric": "supplier_water_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-04", "metric": "supplier_water_storage_hours", "label": "supplier water storage",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water storage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_data_quality_score_05(record):
    """Evaluate supplier data quality for control WP-0550-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-05", "metric": "supplier_data_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-05", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-05", "metric": "supplier_data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-05", "metric": "supplier_data_quality_score", "label": "supplier data quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_release_canary_error_pct_06(record):
    """Evaluate supplier canary error rate for control WP-0550-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_canary_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-06", "metric": "supplier_release_canary_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-06", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-06", "metric": "supplier_release_canary_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-06", "metric": "supplier_release_canary_error_pct", "label": "supplier canary error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "supplier canary error rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_mfa_coverage_pct_07(record):
    """Evaluate supplier MFA coverage for control WP-0550-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-07", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-07", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-07", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-07", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier MFA coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_breach_notification_minutes_08(record):
    """Evaluate supplier breach notification time for control WP-0550-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-08", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-08", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-08", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-08", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier breach notification time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_waiver_expiry_days_09(record):
    """Evaluate supplier waiver validity for control WP-0550-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-09", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-09", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-09", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-09", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier waiver validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_early_payment_discount_capture_pct_10(record):
    """Evaluate early-payment discount capture for control WP-0550-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-10", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-10", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-10", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-10", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "early-payment discount capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_finished_goods_cover_days_11(record):
    """Evaluate supplier finished-goods cover for control WP-0550-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-11", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-11", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-11", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-11", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier finished-goods cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_migration_rehearsal_age_days_12(record):
    """Evaluate supplier migration rehearsal age for control WP-0550-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_migration_rehearsal_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-12", "metric": "supplier_migration_rehearsal_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-12", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-12", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-12", "metric": "supplier_migration_rehearsal_age_days", "label": "supplier migration rehearsal age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier migration rehearsal age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_exit_signoff_pct_13(record):
    """Evaluate supplier exit signoff for control WP-0550-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-13", "metric": "supplier_exit_signoff_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-13", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-13", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-13", "metric": "supplier_exit_signoff_pct", "label": "supplier exit signoff",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit signoff must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_labor_hours_14(record):
    """Evaluate labor hours for control WP-0550-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-14", "metric": "labor_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-14", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-14", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-14", "metric": "labor_hours", "label": "labor hours",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "labor hours exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_worker_load_pct_15(record):
    """Evaluate worker load for control WP-0550-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_load_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-15", "metric": "worker_load_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-15", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-15", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-15", "metric": "worker_load_pct", "label": "worker load",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "worker load falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_backup_age_hours_16(record):
    """Evaluate backup age for control WP-0550-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-16", "metric": "backup_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-16", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-16", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-16", "metric": "backup_age_hours", "label": "backup age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_carrier_claim_rate_pct_17(record):
    """Evaluate carrier claim rate for control WP-0550-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_claim_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-17", "metric": "carrier_claim_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-17", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-17", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-17", "metric": "carrier_claim_rate_pct", "label": "carrier claim rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carrier claim rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_yard_dwell_hours_18(record):
    """Evaluate yard dwell for control WP-0550-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-18", "metric": "yard_dwell_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-18", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-18", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-18", "metric": "yard_dwell_hours", "label": "yard dwell",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "yard dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_dashboard_load_ms_19(record):
    """Evaluate dashboard load time for control WP-0550-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dashboard_load_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-19", "metric": "dashboard_load_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-19", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-19", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-19", "metric": "dashboard_load_ms", "label": "dashboard load time",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "dashboard load time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_batch_release_age_minutes_20(record):
    """Evaluate batch release age for control WP-0550-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-20", "metric": "batch_release_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-20", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-20", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-20", "metric": "batch_release_age_minutes", "label": "batch release age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "batch release age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_high_value_cage_open_minutes_21(record):
    """Evaluate high-value cage open time for control WP-0550-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_cage_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-21", "metric": "high_value_cage_open_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-21", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-21", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-21", "metric": "high_value_cage_open_minutes", "label": "high-value cage open time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "high-value cage open time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_compressor_runtime_hours_22(record):
    """Evaluate compressor runtime for control WP-0550-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("compressor_runtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-22", "metric": "compressor_runtime_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-22", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-22", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-22", "metric": "compressor_runtime_hours", "label": "compressor runtime",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "compressor runtime exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_authentication_scan_pct_23(record):
    """Evaluate authentication scan rate for control WP-0550-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("authentication_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-23", "metric": "authentication_scan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-23", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-23", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-23", "metric": "authentication_scan_pct", "label": "authentication scan rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "authentication scan rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_contractor_induction_pct_24(record):
    """Evaluate contractor induction completion for control WP-0550-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contractor_induction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0550-24", "metric": "contractor_induction_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0550-24", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0550-24", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0550-24", "metric": "contractor_induction_pct", "label": "contractor induction completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "contractor induction completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_supplier_process_change_notice_days_01, assess_supplier_rohs_compliance_pct_02, assess_supplier_adverse_media_review_age_days_03, assess_supplier_water_storage_hours_04, assess_supplier_data_quality_score_05, assess_supplier_release_canary_error_pct_06, assess_supplier_mfa_coverage_pct_07, assess_supplier_breach_notification_minutes_08, assess_supplier_waiver_expiry_days_09, assess_supplier_early_payment_discount_capture_pct_10, assess_supplier_finished_goods_cover_days_11, assess_supplier_migration_rehearsal_age_days_12, assess_supplier_exit_signoff_pct_13, assess_labor_hours_14, assess_worker_load_pct_15, assess_backup_age_hours_16, assess_carrier_claim_rate_pct_17, assess_yard_dwell_hours_18, assess_dashboard_load_ms_19, assess_batch_release_age_minutes_20, assess_high_value_cage_open_minutes_21, assess_compressor_runtime_hours_22, assess_authentication_scan_pct_23, assess_contractor_induction_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

