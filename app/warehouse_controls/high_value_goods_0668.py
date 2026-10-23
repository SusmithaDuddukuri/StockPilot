"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_change_notice_days_01(record):
    """Evaluate supplier change notice for control WP-0668-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-01", "metric": "supplier_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-01", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-01", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-01", "metric": "supplier_change_notice_days", "label": "supplier change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_shipping_window_compliance_pct_02(record):
    """Evaluate supplier shipping-window compliance for control WP-0668-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_window_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-02", "metric": "supplier_shipping_window_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-02", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-02", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-02", "metric": "supplier_shipping_window_compliance_pct", "label": "supplier shipping-window compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier shipping-window compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_service_availability_pct_03(record):
    """Evaluate supplier service availability for control WP-0668-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-03", "metric": "supplier_service_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-03", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-03", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-03", "metric": "supplier_service_availability_pct", "label": "supplier service availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier service availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_lot_data_completeness_pct_04(record):
    """Evaluate supplier lot-data completeness for control WP-0668-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lot_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-04", "metric": "supplier_lot_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-04", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-04", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-04", "metric": "supplier_lot_data_completeness_pct", "label": "supplier lot-data completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier lot-data completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_site_access_review_age_days_05(record):
    """Evaluate supplier site access review age for control WP-0668-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-05", "metric": "supplier_site_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-05", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-05", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-05", "metric": "supplier_site_access_review_age_days", "label": "supplier site access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier site access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_critical_process_backup_pct_06(record):
    """Evaluate supplier critical-process backup for control WP-0668-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_process_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-06", "metric": "supplier_critical_process_backup_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-06", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-06", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-06", "metric": "supplier_critical_process_backup_pct", "label": "supplier critical-process backup",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier critical-process backup must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_regulatory_change_age_days_07(record):
    """Evaluate supplier regulatory-change age for control WP-0668-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulatory_change_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-07", "metric": "supplier_regulatory_change_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-07", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-07", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-07", "metric": "supplier_regulatory_change_age_days", "label": "supplier regulatory-change age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier regulatory-change age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_tax_transparency_score_08(record):
    """Evaluate supplier tax transparency for control WP-0668-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_transparency_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-08", "metric": "supplier_tax_transparency_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-08", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-08", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-08", "metric": "supplier_tax_transparency_score", "label": "supplier tax transparency",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier tax transparency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_alternate_logistics_pct_09(record):
    """Evaluate supplier alternate logistics coverage for control WP-0668-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_logistics_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-09", "metric": "supplier_alternate_logistics_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-09", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-09", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-09", "metric": "supplier_alternate_logistics_pct", "label": "supplier alternate logistics coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier alternate logistics coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_predictive_maintenance_pct_10(record):
    """Evaluate supplier predictive maintenance for control WP-0668-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_predictive_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-10", "metric": "supplier_predictive_maintenance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-10", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-10", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-10", "metric": "supplier_predictive_maintenance_pct", "label": "supplier predictive maintenance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier predictive maintenance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_label_quality_score_11(record):
    """Evaluate supplier label quality for control WP-0668-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-11", "metric": "supplier_label_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-11", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-11", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-11", "metric": "supplier_label_quality_score", "label": "supplier label quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier label quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_multi_region_coverage_pct_12(record):
    """Evaluate supplier multi-region coverage for control WP-0668-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_multi_region_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-12", "metric": "supplier_multi_region_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-12", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-12", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-12", "metric": "supplier_multi_region_coverage_pct", "label": "supplier multi-region coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier multi-region coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_privacy_impact_age_days_13(record):
    """Evaluate supplier privacy impact assessment age for control WP-0668-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_impact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-13", "metric": "supplier_privacy_impact_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-13", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-13", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-13", "metric": "supplier_privacy_impact_age_days", "label": "supplier privacy impact assessment age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier privacy impact assessment age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_residual_risk_score_14(record):
    """Evaluate supplier residual risk for control WP-0668-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_residual_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-14", "metric": "supplier_residual_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-14", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-14", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-14", "metric": "supplier_residual_risk_score", "label": "supplier residual risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier residual risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_duplicate_invoice_signal_15(record):
    """Evaluate duplicate-invoice signal for control WP-0668-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_invoice_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-15", "metric": "supplier_duplicate_invoice_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-15", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-15", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-15", "metric": "supplier_duplicate_invoice_signal", "label": "duplicate-invoice signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate-invoice signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_batch_cycle_hours_16(record):
    """Evaluate supplier batch cycle for control WP-0668-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_batch_cycle_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-16", "metric": "supplier_batch_cycle_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-16", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-16", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-16", "metric": "supplier_batch_cycle_hours", "label": "supplier batch cycle",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier batch cycle exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_award_expiry_days_17(record):
    """Evaluate supplier award validity for control WP-0668-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_award_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-17", "metric": "supplier_award_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-17", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-17", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-17", "metric": "supplier_award_expiry_days", "label": "supplier award validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier award validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_post_exit_access_count_18(record):
    """Evaluate post-exit access events for control WP-0668-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-18", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-18", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-18", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-18", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "post-exit access events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_expiry_days_19(record):
    """Evaluate days to expiry for control WP-0668-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-19", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-19", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-19", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-19", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "days to expiry must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_customs_hold_hours_20(record):
    """Evaluate customs hold for control WP-0668-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-20", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-20", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-20", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-20", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "customs hold exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_water_leak_signal_21(record):
    """Evaluate water leak signal for control WP-0668-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-21", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-21", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-21", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-21", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "water leak signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_scanner_disconnect_count_22(record):
    """Evaluate scanner disconnects for control WP-0668-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_disconnect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-22", "metric": "scanner_disconnect_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-22", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-22", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-22", "metric": "scanner_disconnect_count", "label": "scanner disconnects",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner disconnects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_receiving_accuracy_pct_23(record):
    """Evaluate receiving accuracy for control WP-0668-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-23", "metric": "receiving_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-23", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-23", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-23", "metric": "receiving_accuracy_pct", "label": "receiving accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "receiving accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_queue_retry_pct_24(record):
    """Evaluate queue retry rate for control WP-0668-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_retry_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0668-24", "metric": "queue_retry_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0668-24", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0668-24", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0668-24", "metric": "queue_retry_pct", "label": "queue retry rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "queue retry rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_change_notice_days_01, assess_supplier_shipping_window_compliance_pct_02, assess_supplier_service_availability_pct_03, assess_supplier_lot_data_completeness_pct_04, assess_supplier_site_access_review_age_days_05, assess_supplier_critical_process_backup_pct_06, assess_supplier_regulatory_change_age_days_07, assess_supplier_tax_transparency_score_08, assess_supplier_alternate_logistics_pct_09, assess_supplier_predictive_maintenance_pct_10, assess_supplier_label_quality_score_11, assess_supplier_multi_region_coverage_pct_12, assess_supplier_privacy_impact_age_days_13, assess_supplier_residual_risk_score_14, assess_supplier_duplicate_invoice_signal_15, assess_supplier_batch_cycle_hours_16, assess_supplier_award_expiry_days_17, assess_supplier_post_exit_access_count_18, assess_expiry_days_19, assess_customs_hold_hours_20, assess_water_leak_signal_21, assess_scanner_disconnect_count_22, assess_receiving_accuracy_pct_23, assess_queue_retry_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

