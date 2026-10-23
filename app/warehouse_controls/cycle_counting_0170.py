"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_critical_process_backup_pct_01(record):
    """Evaluate supplier critical-process backup for control WP-0170-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_process_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-01", "metric": "supplier_critical_process_backup_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-01", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-01", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-01", "metric": "supplier_critical_process_backup_pct", "label": "supplier critical-process backup",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier critical-process backup must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_regulatory_change_age_days_02(record):
    """Evaluate supplier regulatory-change age for control WP-0170-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulatory_change_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-02", "metric": "supplier_regulatory_change_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-02", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-02", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-02", "metric": "supplier_regulatory_change_age_days", "label": "supplier regulatory-change age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier regulatory-change age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_tax_transparency_score_03(record):
    """Evaluate supplier tax transparency for control WP-0170-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_transparency_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-03", "metric": "supplier_tax_transparency_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-03", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-03", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-03", "metric": "supplier_tax_transparency_score", "label": "supplier tax transparency",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "supplier tax transparency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_alternate_logistics_pct_04(record):
    """Evaluate supplier alternate logistics coverage for control WP-0170-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_logistics_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-04", "metric": "supplier_alternate_logistics_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-04", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-04", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-04", "metric": "supplier_alternate_logistics_pct", "label": "supplier alternate logistics coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier alternate logistics coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_predictive_maintenance_pct_05(record):
    """Evaluate supplier predictive maintenance for control WP-0170-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_predictive_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-05", "metric": "supplier_predictive_maintenance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-05", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-05", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-05", "metric": "supplier_predictive_maintenance_pct", "label": "supplier predictive maintenance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier predictive maintenance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_label_quality_score_06(record):
    """Evaluate supplier label quality for control WP-0170-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-06", "metric": "supplier_label_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-06", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-06", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-06", "metric": "supplier_label_quality_score", "label": "supplier label quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier label quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_multi_region_coverage_pct_07(record):
    """Evaluate supplier multi-region coverage for control WP-0170-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_multi_region_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-07", "metric": "supplier_multi_region_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-07", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-07", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-07", "metric": "supplier_multi_region_coverage_pct", "label": "supplier multi-region coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier multi-region coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_privacy_impact_age_days_08(record):
    """Evaluate supplier privacy impact assessment age for control WP-0170-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_impact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-08", "metric": "supplier_privacy_impact_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-08", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-08", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-08", "metric": "supplier_privacy_impact_age_days", "label": "supplier privacy impact assessment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy impact assessment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_residual_risk_score_09(record):
    """Evaluate supplier residual risk for control WP-0170-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_residual_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-09", "metric": "supplier_residual_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-09", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-09", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-09", "metric": "supplier_residual_risk_score", "label": "supplier residual risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier residual risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_duplicate_invoice_signal_10(record):
    """Evaluate duplicate-invoice signal for control WP-0170-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_invoice_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-10", "metric": "supplier_duplicate_invoice_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-10", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-10", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-10", "metric": "supplier_duplicate_invoice_signal", "label": "duplicate-invoice signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "duplicate-invoice signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_batch_cycle_hours_11(record):
    """Evaluate supplier batch cycle for control WP-0170-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_batch_cycle_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-11", "metric": "supplier_batch_cycle_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-11", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-11", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-11", "metric": "supplier_batch_cycle_hours", "label": "supplier batch cycle",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier batch cycle falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_award_expiry_days_12(record):
    """Evaluate supplier award validity for control WP-0170-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_award_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-12", "metric": "supplier_award_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-12", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-12", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-12", "metric": "supplier_award_expiry_days", "label": "supplier award validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier award validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_post_exit_access_count_13(record):
    """Evaluate post-exit access events for control WP-0170-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-13", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-13", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-13", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-13", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "post-exit access events must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_expiry_days_14(record):
    """Evaluate days to expiry for control WP-0170-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-14", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-14", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-14", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-14", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "days to expiry exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_customs_hold_hours_15(record):
    """Evaluate customs hold for control WP-0170-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-15", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-15", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-15", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-15", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "customs hold falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_water_leak_signal_16(record):
    """Evaluate water leak signal for control WP-0170-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-16", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-16", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-16", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-16", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "water leak signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_scanner_disconnect_count_17(record):
    """Evaluate scanner disconnects for control WP-0170-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_disconnect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-17", "metric": "scanner_disconnect_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-17", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-17", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-17", "metric": "scanner_disconnect_count", "label": "scanner disconnects",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scanner disconnects must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_receiving_accuracy_pct_18(record):
    """Evaluate receiving accuracy for control WP-0170-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-18", "metric": "receiving_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-18", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-18", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-18", "metric": "receiving_accuracy_pct", "label": "receiving accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "receiving accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_queue_retry_pct_19(record):
    """Evaluate queue retry rate for control WP-0170-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_retry_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-19", "metric": "queue_retry_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-19", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-19", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-19", "metric": "queue_retry_pct", "label": "queue retry rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "queue retry rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_case_pick_ratio_pct_20(record):
    """Evaluate case pick ratio for control WP-0170-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("case_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-20", "metric": "case_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-20", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-20", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-20", "metric": "case_pick_ratio_pct", "label": "case pick ratio",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "case pick ratio must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_visitor_badge_gap_count_21(record):
    """Evaluate visitor badge gaps for control WP-0170-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("visitor_badge_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-21", "metric": "visitor_badge_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-21", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-21", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-21", "metric": "visitor_badge_gap_count", "label": "visitor badge gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "visitor badge gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_water_consumption_liters_22(record):
    """Evaluate water consumption for control WP-0170-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_consumption_liters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-22", "metric": "water_consumption_liters",
            "status": "insufficient_data",
            "severity": "critical", "unit": "liters",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-22", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-22", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-22", "metric": "water_consumption_liters", "label": "water consumption",
        "status": "breach", "severity": "critical", "unit": "liters",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "water consumption exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_vault_access_review_age_days_23(record):
    """Evaluate vault access review age for control WP-0170-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vault_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-23", "metric": "vault_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-23", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-23", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-23", "metric": "vault_access_review_age_days", "label": "vault access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "vault access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_sds_access_pct_24(record):
    """Evaluate SDS access completeness for control WP-0170-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sds_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0170-24", "metric": "sds_access_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0170-24", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0170-24", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0170-24", "metric": "sds_access_pct", "label": "SDS access completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "SDS access completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_critical_process_backup_pct_01, assess_supplier_regulatory_change_age_days_02, assess_supplier_tax_transparency_score_03, assess_supplier_alternate_logistics_pct_04, assess_supplier_predictive_maintenance_pct_05, assess_supplier_label_quality_score_06, assess_supplier_multi_region_coverage_pct_07, assess_supplier_privacy_impact_age_days_08, assess_supplier_residual_risk_score_09, assess_supplier_duplicate_invoice_signal_10, assess_supplier_batch_cycle_hours_11, assess_supplier_award_expiry_days_12, assess_supplier_post_exit_access_count_13, assess_expiry_days_14, assess_customs_hold_hours_15, assess_water_leak_signal_16, assess_scanner_disconnect_count_17, assess_receiving_accuracy_pct_18, assess_queue_retry_pct_19, assess_case_pick_ratio_pct_20, assess_visitor_badge_gap_count_21, assess_water_consumption_liters_22, assess_vault_access_review_age_days_23, assess_sds_access_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

