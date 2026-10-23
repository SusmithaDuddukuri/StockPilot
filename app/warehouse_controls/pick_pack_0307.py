"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_mfa_coverage_pct_01(record):
    """Evaluate supplier MFA coverage for control WP-0307-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mfa_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-01", "metric": "supplier_mfa_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-01", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-01", "metric": "supplier_mfa_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-01", "metric": "supplier_mfa_coverage_pct", "label": "supplier MFA coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier MFA coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_breach_notification_minutes_02(record):
    """Evaluate supplier breach notification time for control WP-0307-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_breach_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-02", "metric": "supplier_breach_notification_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-02", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-02", "metric": "supplier_breach_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-02", "metric": "supplier_breach_notification_minutes", "label": "supplier breach notification time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier breach notification time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_waiver_expiry_days_03(record):
    """Evaluate supplier waiver validity for control WP-0307-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waiver_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-03", "metric": "supplier_waiver_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-03", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-03", "metric": "supplier_waiver_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-03", "metric": "supplier_waiver_expiry_days", "label": "supplier waiver validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier waiver validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_early_payment_discount_capture_pct_04(record):
    """Evaluate early-payment discount capture for control WP-0307-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_early_payment_discount_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-04", "metric": "supplier_early_payment_discount_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-04", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-04", "metric": "supplier_early_payment_discount_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-04", "metric": "supplier_early_payment_discount_capture_pct", "label": "early-payment discount capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "early-payment discount capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_finished_goods_cover_days_05(record):
    """Evaluate supplier finished-goods cover for control WP-0307-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_finished_goods_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-05", "metric": "supplier_finished_goods_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-05", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-05", "metric": "supplier_finished_goods_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-05", "metric": "supplier_finished_goods_cover_days", "label": "supplier finished-goods cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier finished-goods cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_migration_rehearsal_age_days_06(record):
    """Evaluate supplier migration rehearsal age for control WP-0307-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_migration_rehearsal_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-06", "metric": "supplier_migration_rehearsal_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-06", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-06", "metric": "supplier_migration_rehearsal_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-06", "metric": "supplier_migration_rehearsal_age_days", "label": "supplier migration rehearsal age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier migration rehearsal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_exit_signoff_pct_07(record):
    """Evaluate supplier exit signoff for control WP-0307-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-07", "metric": "supplier_exit_signoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-07", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-07", "metric": "supplier_exit_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-07", "metric": "supplier_exit_signoff_pct", "label": "supplier exit signoff",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier exit signoff exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_labor_hours_08(record):
    """Evaluate labor hours for control WP-0307-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-08", "metric": "labor_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-08", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-08", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-08", "metric": "labor_hours", "label": "labor hours",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "labor hours falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_worker_load_pct_09(record):
    """Evaluate worker load for control WP-0307-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_load_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-09", "metric": "worker_load_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-09", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-09", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-09", "metric": "worker_load_pct", "label": "worker load",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "worker load must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_backup_age_hours_10(record):
    """Evaluate backup age for control WP-0307-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-10", "metric": "backup_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-10", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-10", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-10", "metric": "backup_age_hours", "label": "backup age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backup age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_carrier_claim_rate_pct_11(record):
    """Evaluate carrier claim rate for control WP-0307-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_claim_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-11", "metric": "carrier_claim_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-11", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-11", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-11", "metric": "carrier_claim_rate_pct", "label": "carrier claim rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "carrier claim rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_yard_dwell_hours_12(record):
    """Evaluate yard dwell for control WP-0307-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-12", "metric": "yard_dwell_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-12", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-12", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-12", "metric": "yard_dwell_hours", "label": "yard dwell",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "yard dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_dashboard_load_ms_13(record):
    """Evaluate dashboard load time for control WP-0307-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dashboard_load_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-13", "metric": "dashboard_load_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-13", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-13", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-13", "metric": "dashboard_load_ms", "label": "dashboard load time",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dashboard load time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_batch_release_age_minutes_14(record):
    """Evaluate batch release age for control WP-0307-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-14", "metric": "batch_release_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-14", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-14", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-14", "metric": "batch_release_age_minutes", "label": "batch release age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "batch release age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_high_value_cage_open_minutes_15(record):
    """Evaluate high-value cage open time for control WP-0307-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_cage_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-15", "metric": "high_value_cage_open_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-15", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-15", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-15", "metric": "high_value_cage_open_minutes", "label": "high-value cage open time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "high-value cage open time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_compressor_runtime_hours_16(record):
    """Evaluate compressor runtime for control WP-0307-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("compressor_runtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-16", "metric": "compressor_runtime_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-16", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-16", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-16", "metric": "compressor_runtime_hours", "label": "compressor runtime",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "compressor runtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_authentication_scan_pct_17(record):
    """Evaluate authentication scan rate for control WP-0307-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("authentication_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-17", "metric": "authentication_scan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-17", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-17", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-17", "metric": "authentication_scan_pct", "label": "authentication scan rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "authentication scan rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_contractor_induction_pct_18(record):
    """Evaluate contractor induction completion for control WP-0307-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contractor_induction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-18", "metric": "contractor_induction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-18", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-18", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-18", "metric": "contractor_induction_pct", "label": "contractor induction completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "contractor induction completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_plc_alarm_count_19(record):
    """Evaluate PLC alarms for control WP-0307-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("plc_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-19", "metric": "plc_alarm_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-19", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-19", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-19", "metric": "plc_alarm_count", "label": "PLC alarms",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "PLC alarms exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_change_approval_pct_20(record):
    """Evaluate change approval completeness for control WP-0307-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-20", "metric": "change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-20", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-20", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-20", "metric": "change_approval_pct", "label": "change approval completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "change approval completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_data_export_age_hours_21(record):
    """Evaluate data export age for control WP-0307-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_export_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-21", "metric": "data_export_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-21", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-21", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-21", "metric": "data_export_age_hours", "label": "data export age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data export age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_harmonized_code_gap_count_22(record):
    """Evaluate harmonized-code gaps for control WP-0307-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-22", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-22", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-22", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-22", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "harmonized-code gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_asn_receipt_match_pct_23(record):
    """Evaluate ASN receipt match for control WP-0307-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-23", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-23", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-23", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-23", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "ASN receipt match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_customer_delivery_rating_24(record):
    """Evaluate customer delivery rating for control WP-0307-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0307-24", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0307-24", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0307-24", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0307-24", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "customer delivery rating falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_mfa_coverage_pct_01, assess_supplier_breach_notification_minutes_02, assess_supplier_waiver_expiry_days_03, assess_supplier_early_payment_discount_capture_pct_04, assess_supplier_finished_goods_cover_days_05, assess_supplier_migration_rehearsal_age_days_06, assess_supplier_exit_signoff_pct_07, assess_labor_hours_08, assess_worker_load_pct_09, assess_backup_age_hours_10, assess_carrier_claim_rate_pct_11, assess_yard_dwell_hours_12, assess_dashboard_load_ms_13, assess_batch_release_age_minutes_14, assess_high_value_cage_open_minutes_15, assess_compressor_runtime_hours_16, assess_authentication_scan_pct_17, assess_contractor_induction_pct_18, assess_plc_alarm_count_19, assess_change_approval_pct_20, assess_data_export_age_hours_21, assess_harmonized_code_gap_count_22, assess_asn_receipt_match_pct_23, assess_customer_delivery_rating_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

