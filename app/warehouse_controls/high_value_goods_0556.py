"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_delivery_improvement_pct_01(record):
    """Evaluate supplier delivery improvement for control WP-0556-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-01", "metric": "supplier_delivery_improvement_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-01", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-01", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-01", "metric": "supplier_delivery_improvement_pct", "label": "supplier delivery improvement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier delivery improvement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_vector_recall_pct_02(record):
    """Evaluate supplier vector recall for control WP-0556-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vector_recall_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-02", "metric": "supplier_vector_recall_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-02", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-02", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-02", "metric": "supplier_vector_recall_pct", "label": "supplier vector recall",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vector recall must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_capacity_forecast_confidence_pct_03(record):
    """Evaluate supplier capacity forecast confidence for control WP-0556-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-03", "metric": "supplier_capacity_forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-03", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-03", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-03", "metric": "supplier_capacity_forecast_confidence_pct", "label": "supplier capacity forecast confidence",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity forecast confidence must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_ip_claim_count_04(record):
    """Evaluate supplier IP claims for control WP-0556-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ip_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-04", "metric": "supplier_ip_claim_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-04", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-04", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-04", "metric": "supplier_ip_claim_count", "label": "supplier IP claims",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier IP claims exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_policy_review_age_days_05(record):
    """Evaluate supplier policy review age for control WP-0556-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-05", "metric": "supplier_policy_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-05", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-05", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-05", "metric": "supplier_policy_review_age_days", "label": "supplier policy review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier policy review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_catalog_compliance_pct_06(record):
    """Evaluate supplier catalog compliance for control WP-0556-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_catalog_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-06", "metric": "supplier_catalog_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-06", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-06", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-06", "metric": "supplier_catalog_compliance_pct", "label": "supplier catalog compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier catalog compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_scrap_pct_07(record):
    """Evaluate supplier scrap rate for control WP-0556-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scrap_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-07", "metric": "supplier_scrap_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-07", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-07", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-07", "metric": "supplier_scrap_pct", "label": "supplier scrap rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier scrap rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_scorecard_dispute_age_days_08(record):
    """Evaluate scorecard dispute age for control WP-0556-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-08", "metric": "supplier_scorecard_dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-08", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-08", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-08", "metric": "supplier_scorecard_dispute_age_days", "label": "scorecard dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "scorecard dispute age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_final_invoice_age_days_09(record):
    """Evaluate supplier final invoice age for control WP-0556-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-09", "metric": "supplier_final_invoice_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-09", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-09", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-09", "metric": "supplier_final_invoice_age_days", "label": "supplier final invoice age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier final invoice age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_otif_pct_10(record):
    """Evaluate supplier OTIF for control WP-0556-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_otif_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-10", "metric": "supplier_otif_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-10", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-10", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-10", "metric": "supplier_otif_pct", "label": "supplier OTIF",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier OTIF must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_pallet_overhang_cm_11(record):
    """Evaluate pallet overhang for control WP-0556-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_overhang_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-11", "metric": "pallet_overhang_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-11", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-11", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-11", "metric": "pallet_overhang_cm", "label": "pallet overhang",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pallet overhang must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_putaway_age_hours_12(record):
    """Evaluate putaway age for control WP-0556-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-12", "metric": "putaway_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-12", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-12", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-12", "metric": "putaway_age_hours", "label": "putaway age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "putaway age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_incident_rate_pct_13(record):
    """Evaluate incident rate for control WP-0556-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-13", "metric": "incident_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-13", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-13", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-13", "metric": "incident_rate_pct", "label": "incident rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "incident rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_audit_age_days_14(record):
    """Evaluate supplier audit age for control WP-0556-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-14", "metric": "supplier_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-14", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-14", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-14", "metric": "supplier_audit_age_days", "label": "supplier audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_restore_success_pct_15(record):
    """Evaluate restore success rate for control WP-0556-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-15", "metric": "restore_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-15", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-15", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-15", "metric": "restore_success_pct", "label": "restore success rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restore success rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_safety_stock_days_16(record):
    """Evaluate safety stock cover for control WP-0556-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-16", "metric": "safety_stock_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-16", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-16", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-16", "metric": "safety_stock_days", "label": "safety stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "safety stock cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_fatigue_score_17(record):
    """Evaluate fatigue score for control WP-0556-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fatigue_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-17", "metric": "fatigue_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-17", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-17", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-17", "metric": "fatigue_score", "label": "fatigue score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "fatigue score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_scrap_approval_age_hours_18(record):
    """Evaluate scrap approval age for control WP-0556-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scrap_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-18", "metric": "scrap_approval_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-18", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-18", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-18", "metric": "scrap_approval_age_hours", "label": "scrap approval age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scrap approval age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_serial_audit_match_pct_19(record):
    """Evaluate serial audit match for control WP-0556-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_audit_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-19", "metric": "serial_audit_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-19", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-19", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-19", "metric": "serial_audit_match_pct", "label": "serial audit match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "serial audit match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_hazmat_segregation_pct_20(record):
    """Evaluate hazmat segregation compliance for control WP-0556-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_segregation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-20", "metric": "hazmat_segregation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-20", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-20", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-20", "metric": "hazmat_segregation_pct", "label": "hazmat segregation compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "hazmat segregation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_training_assessment_pct_21(record):
    """Evaluate training assessment score for control WP-0556-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_assessment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-21", "metric": "training_assessment_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-21", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-21", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-21", "metric": "training_assessment_pct", "label": "training assessment score",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "training assessment score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_assembly_point_signage_pct_22(record):
    """Evaluate assembly point signage for control WP-0556-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("assembly_point_signage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-22", "metric": "assembly_point_signage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-22", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-22", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-22", "metric": "assembly_point_signage_pct", "label": "assembly point signage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "assembly point signage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_schema_drift_count_23(record):
    """Evaluate schema drift events for control WP-0556-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("schema_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-23", "metric": "schema_drift_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-23", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-23", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-23", "metric": "schema_drift_count", "label": "schema drift events",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schema drift events must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_sku_master_gap_count_24(record):
    """Evaluate SKU master gaps for control WP-0556-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sku_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0556-24", "metric": "sku_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0556-24", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0556-24", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0556-24", "metric": "sku_master_gap_count", "label": "SKU master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "SKU master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_delivery_improvement_pct_01, assess_supplier_vector_recall_pct_02, assess_supplier_capacity_forecast_confidence_pct_03, assess_supplier_ip_claim_count_04, assess_supplier_policy_review_age_days_05, assess_supplier_catalog_compliance_pct_06, assess_supplier_scrap_pct_07, assess_supplier_scorecard_dispute_age_days_08, assess_supplier_final_invoice_age_days_09, assess_supplier_otif_pct_10, assess_pallet_overhang_cm_11, assess_putaway_age_hours_12, assess_incident_rate_pct_13, assess_supplier_audit_age_days_14, assess_restore_success_pct_15, assess_safety_stock_days_16, assess_fatigue_score_17, assess_scrap_approval_age_hours_18, assess_serial_audit_match_pct_19, assess_hazmat_segregation_pct_20, assess_training_assessment_pct_21, assess_assembly_point_signage_pct_22, assess_schema_drift_count_23, assess_sku_master_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

