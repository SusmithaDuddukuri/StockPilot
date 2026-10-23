"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_catalog_compliance_pct_01(record):
    """Evaluate supplier catalog compliance for control WP-0058-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_catalog_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-01", "metric": "supplier_catalog_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-01", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-01", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-01", "metric": "supplier_catalog_compliance_pct", "label": "supplier catalog compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier catalog compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_scrap_pct_02(record):
    """Evaluate supplier scrap rate for control WP-0058-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scrap_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-02", "metric": "supplier_scrap_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-02", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-02", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-02", "metric": "supplier_scrap_pct", "label": "supplier scrap rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier scrap rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_scorecard_dispute_age_days_03(record):
    """Evaluate scorecard dispute age for control WP-0058-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-03", "metric": "supplier_scorecard_dispute_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-03", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-03", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-03", "metric": "supplier_scorecard_dispute_age_days", "label": "scorecard dispute age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "scorecard dispute age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_final_invoice_age_days_04(record):
    """Evaluate supplier final invoice age for control WP-0058-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-04", "metric": "supplier_final_invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-04", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-04", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-04", "metric": "supplier_final_invoice_age_days", "label": "supplier final invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier final invoice age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_otif_pct_05(record):
    """Evaluate supplier OTIF for control WP-0058-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_otif_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-05", "metric": "supplier_otif_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-05", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-05", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-05", "metric": "supplier_otif_pct", "label": "supplier OTIF",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier OTIF must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_pallet_overhang_cm_06(record):
    """Evaluate pallet overhang for control WP-0058-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_overhang_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-06", "metric": "pallet_overhang_cm",
            "status": "insufficient_data",
            "severity": "critical", "unit": "cm",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-06", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-06", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-06", "metric": "pallet_overhang_cm", "label": "pallet overhang",
        "status": "breach", "severity": "critical", "unit": "cm",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "pallet overhang exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_putaway_age_hours_07(record):
    """Evaluate putaway age for control WP-0058-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-07", "metric": "putaway_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-07", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-07", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-07", "metric": "putaway_age_hours", "label": "putaway age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "putaway age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_incident_rate_pct_08(record):
    """Evaluate incident rate for control WP-0058-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-08", "metric": "incident_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-08", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-08", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-08", "metric": "incident_rate_pct", "label": "incident rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "incident rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_audit_age_days_09(record):
    """Evaluate supplier audit age for control WP-0058-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-09", "metric": "supplier_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-09", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-09", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-09", "metric": "supplier_audit_age_days", "label": "supplier audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier audit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_restore_success_pct_10(record):
    """Evaluate restore success rate for control WP-0058-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-10", "metric": "restore_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-10", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-10", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-10", "metric": "restore_success_pct", "label": "restore success rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "restore success rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_safety_stock_days_11(record):
    """Evaluate safety stock cover for control WP-0058-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-11", "metric": "safety_stock_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-11", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-11", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-11", "metric": "safety_stock_days", "label": "safety stock cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "safety stock cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_fatigue_score_12(record):
    """Evaluate fatigue score for control WP-0058-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fatigue_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-12", "metric": "fatigue_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-12", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-12", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-12", "metric": "fatigue_score", "label": "fatigue score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fatigue score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_scrap_approval_age_hours_13(record):
    """Evaluate scrap approval age for control WP-0058-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scrap_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-13", "metric": "scrap_approval_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-13", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-13", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-13", "metric": "scrap_approval_age_hours", "label": "scrap approval age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scrap approval age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_serial_audit_match_pct_14(record):
    """Evaluate serial audit match for control WP-0058-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_audit_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-14", "metric": "serial_audit_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-14", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-14", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-14", "metric": "serial_audit_match_pct", "label": "serial audit match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "serial audit match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_hazmat_segregation_pct_15(record):
    """Evaluate hazmat segregation compliance for control WP-0058-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_segregation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-15", "metric": "hazmat_segregation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-15", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-15", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-15", "metric": "hazmat_segregation_pct", "label": "hazmat segregation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "hazmat segregation compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_training_assessment_pct_16(record):
    """Evaluate training assessment score for control WP-0058-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_assessment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-16", "metric": "training_assessment_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-16", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-16", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-16", "metric": "training_assessment_pct", "label": "training assessment score",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "training assessment score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_assembly_point_signage_pct_17(record):
    """Evaluate assembly point signage for control WP-0058-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("assembly_point_signage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-17", "metric": "assembly_point_signage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-17", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-17", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-17", "metric": "assembly_point_signage_pct", "label": "assembly point signage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "assembly point signage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_schema_drift_count_18(record):
    """Evaluate schema drift events for control WP-0058-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("schema_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-18", "metric": "schema_drift_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-18", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-18", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-18", "metric": "schema_drift_count", "label": "schema drift events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "schema drift events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_sku_master_gap_count_19(record):
    """Evaluate SKU master gaps for control WP-0058-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sku_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-19", "metric": "sku_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-19", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-19", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-19", "metric": "sku_master_gap_count", "label": "SKU master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "SKU master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_dead_stock_value_20(record):
    """Evaluate dead stock value for control WP-0058-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-20", "metric": "dead_stock_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-20", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-20", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-20", "metric": "dead_stock_value", "label": "dead stock value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dead stock value must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_label_purchase_cost_21(record):
    """Evaluate label purchase cost for control WP-0058-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_purchase_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-21", "metric": "label_purchase_cost",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-21", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-21", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-21", "metric": "label_purchase_cost", "label": "label purchase cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "label purchase cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_country_risk_score_22(record):
    """Evaluate country risk score for control WP-0058-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-22", "metric": "country_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-22", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-22", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-22", "metric": "country_risk_score", "label": "country risk score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "country risk score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_vehicle_insurance_days_left_23(record):
    """Evaluate vehicle insurance validity for control WP-0058-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-23", "metric": "vehicle_insurance_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-23", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-23", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-23", "metric": "vehicle_insurance_days_left", "label": "vehicle insurance validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "vehicle insurance validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_vendor_invoice_age_days_24(record):
    """Evaluate vendor invoice age for control WP-0058-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vendor_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0058-24", "metric": "vendor_invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0058-24", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0058-24", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0058-24", "metric": "vendor_invoice_age_days", "label": "vendor invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vendor invoice age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_catalog_compliance_pct_01, assess_supplier_scrap_pct_02, assess_supplier_scorecard_dispute_age_days_03, assess_supplier_final_invoice_age_days_04, assess_supplier_otif_pct_05, assess_pallet_overhang_cm_06, assess_putaway_age_hours_07, assess_incident_rate_pct_08, assess_supplier_audit_age_days_09, assess_restore_success_pct_10, assess_safety_stock_days_11, assess_fatigue_score_12, assess_scrap_approval_age_hours_13, assess_serial_audit_match_pct_14, assess_hazmat_segregation_pct_15, assess_training_assessment_pct_16, assess_assembly_point_signage_pct_17, assess_schema_drift_count_18, assess_sku_master_gap_count_19, assess_dead_stock_value_20, assess_label_purchase_cost_21, assess_country_risk_score_22, assess_vehicle_insurance_days_left_23, assess_vendor_invoice_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

