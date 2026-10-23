"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_gate_checkout_minutes_01(record):
    """Evaluate gate check-out time for control WP-0600-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkout_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-01", "metric": "gate_checkout_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-01", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-01", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-01", "metric": "gate_checkout_minutes", "label": "gate check-out time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "gate check-out time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_agency_labor_pct_02(record):
    """Evaluate agency labor share for control WP-0600-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("agency_labor_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-02", "metric": "agency_labor_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-02", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-02", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-02", "metric": "agency_labor_pct", "label": "agency labor share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "agency labor share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_packaging_damage_pct_03(record):
    """Evaluate supplier packaging damage for control WP-0600-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-03", "metric": "supplier_packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-03", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-03", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-03", "metric": "supplier_packaging_damage_pct", "label": "supplier packaging damage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging damage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_change_notice_days_04(record):
    """Evaluate supplier change notice for control WP-0600-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-04", "metric": "supplier_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-04", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-04", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-04", "metric": "supplier_change_notice_days", "label": "supplier change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_shipping_window_compliance_pct_05(record):
    """Evaluate supplier shipping-window compliance for control WP-0600-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_window_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-05", "metric": "supplier_shipping_window_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-05", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-05", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-05", "metric": "supplier_shipping_window_compliance_pct", "label": "supplier shipping-window compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "supplier shipping-window compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_service_availability_pct_06(record):
    """Evaluate supplier service availability for control WP-0600-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-06", "metric": "supplier_service_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-06", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-06", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-06", "metric": "supplier_service_availability_pct", "label": "supplier service availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier service availability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_lot_data_completeness_pct_07(record):
    """Evaluate supplier lot-data completeness for control WP-0600-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lot_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-07", "metric": "supplier_lot_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-07", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-07", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-07", "metric": "supplier_lot_data_completeness_pct", "label": "supplier lot-data completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier lot-data completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_site_access_review_age_days_08(record):
    """Evaluate supplier site access review age for control WP-0600-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-08", "metric": "supplier_site_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-08", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-08", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-08", "metric": "supplier_site_access_review_age_days", "label": "supplier site access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "supplier site access review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_critical_process_backup_pct_09(record):
    """Evaluate supplier critical-process backup for control WP-0600-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_process_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-09", "metric": "supplier_critical_process_backup_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-09", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-09", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-09", "metric": "supplier_critical_process_backup_pct", "label": "supplier critical-process backup",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier critical-process backup falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_regulatory_change_age_days_10(record):
    """Evaluate supplier regulatory-change age for control WP-0600-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulatory_change_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-10", "metric": "supplier_regulatory_change_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-10", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-10", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-10", "metric": "supplier_regulatory_change_age_days", "label": "supplier regulatory-change age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier regulatory-change age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_tax_transparency_score_11(record):
    """Evaluate supplier tax transparency for control WP-0600-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_transparency_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-11", "metric": "supplier_tax_transparency_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-11", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-11", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-11", "metric": "supplier_tax_transparency_score", "label": "supplier tax transparency",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tax transparency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_alternate_logistics_pct_12(record):
    """Evaluate supplier alternate logistics coverage for control WP-0600-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_logistics_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-12", "metric": "supplier_alternate_logistics_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-12", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-12", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-12", "metric": "supplier_alternate_logistics_pct", "label": "supplier alternate logistics coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "supplier alternate logistics coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_predictive_maintenance_pct_13(record):
    """Evaluate supplier predictive maintenance for control WP-0600-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_predictive_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-13", "metric": "supplier_predictive_maintenance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-13", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-13", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-13", "metric": "supplier_predictive_maintenance_pct", "label": "supplier predictive maintenance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier predictive maintenance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_label_quality_score_14(record):
    """Evaluate supplier label quality for control WP-0600-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-14", "metric": "supplier_label_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-14", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-14", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-14", "metric": "supplier_label_quality_score", "label": "supplier label quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_multi_region_coverage_pct_15(record):
    """Evaluate supplier multi-region coverage for control WP-0600-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_multi_region_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-15", "metric": "supplier_multi_region_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-15", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-15", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-15", "metric": "supplier_multi_region_coverage_pct", "label": "supplier multi-region coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier multi-region coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_privacy_impact_age_days_16(record):
    """Evaluate supplier privacy impact assessment age for control WP-0600-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_impact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-16", "metric": "supplier_privacy_impact_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-16", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-16", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-16", "metric": "supplier_privacy_impact_age_days", "label": "supplier privacy impact assessment age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "supplier privacy impact assessment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_residual_risk_score_17(record):
    """Evaluate supplier residual risk for control WP-0600-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_residual_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-17", "metric": "supplier_residual_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-17", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-17", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-17", "metric": "supplier_residual_risk_score", "label": "supplier residual risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier residual risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_duplicate_invoice_signal_18(record):
    """Evaluate duplicate-invoice signal for control WP-0600-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_invoice_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-18", "metric": "supplier_duplicate_invoice_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-18", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-18", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-18", "metric": "supplier_duplicate_invoice_signal", "label": "duplicate-invoice signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate-invoice signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_batch_cycle_hours_19(record):
    """Evaluate supplier batch cycle for control WP-0600-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_batch_cycle_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-19", "metric": "supplier_batch_cycle_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-19", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-19", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-19", "metric": "supplier_batch_cycle_hours", "label": "supplier batch cycle",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier batch cycle must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_award_expiry_days_20(record):
    """Evaluate supplier award validity for control WP-0600-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_award_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-20", "metric": "supplier_award_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-20", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-20", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-20", "metric": "supplier_award_expiry_days", "label": "supplier award validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "supplier award validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_post_exit_access_count_21(record):
    """Evaluate post-exit access events for control WP-0600-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-21", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-21", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-21", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-21", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "post-exit access events falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_expiry_days_22(record):
    """Evaluate days to expiry for control WP-0600-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-22", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-22", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-22", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-22", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "days to expiry must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_customs_hold_hours_23(record):
    """Evaluate customs hold for control WP-0600-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-23", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-23", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-23", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-23", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customs hold must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_water_leak_signal_24(record):
    """Evaluate water leak signal for control WP-0600-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0600-24", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0600-24", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0600-24", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0600-24", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "water leak signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_gate_checkout_minutes_01, assess_agency_labor_pct_02, assess_supplier_packaging_damage_pct_03, assess_supplier_change_notice_days_04, assess_supplier_shipping_window_compliance_pct_05, assess_supplier_service_availability_pct_06, assess_supplier_lot_data_completeness_pct_07, assess_supplier_site_access_review_age_days_08, assess_supplier_critical_process_backup_pct_09, assess_supplier_regulatory_change_age_days_10, assess_supplier_tax_transparency_score_11, assess_supplier_alternate_logistics_pct_12, assess_supplier_predictive_maintenance_pct_13, assess_supplier_label_quality_score_14, assess_supplier_multi_region_coverage_pct_15, assess_supplier_privacy_impact_age_days_16, assess_supplier_residual_risk_score_17, assess_supplier_duplicate_invoice_signal_18, assess_supplier_batch_cycle_hours_19, assess_supplier_award_expiry_days_20, assess_supplier_post_exit_access_count_21, assess_expiry_days_22, assess_customs_hold_hours_23, assess_water_leak_signal_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

