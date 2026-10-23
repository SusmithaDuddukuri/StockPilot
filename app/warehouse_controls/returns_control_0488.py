"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_major_finding_count_01(record):
    """Evaluate supplier major findings for control WP-0488-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_major_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-01", "metric": "supplier_major_finding_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-01", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-01", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-01", "metric": "supplier_major_finding_count", "label": "supplier major findings",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier major findings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_community_impact_score_02(record):
    """Evaluate supplier community impact for control WP-0488-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_community_impact_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-02", "metric": "supplier_community_impact_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-02", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-02", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-02", "metric": "supplier_community_impact_score", "label": "supplier community impact",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier community impact must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_recovery_capacity_pct_03(record):
    """Evaluate supplier recovery capacity for control WP-0488-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-03", "metric": "supplier_recovery_capacity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-03", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-03", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-03", "metric": "supplier_recovery_capacity_pct", "label": "supplier recovery capacity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery capacity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_delivery_improvement_pct_04(record):
    """Evaluate supplier delivery improvement for control WP-0488-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-04", "metric": "supplier_delivery_improvement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-04", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-04", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-04", "metric": "supplier_delivery_improvement_pct", "label": "supplier delivery improvement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier delivery improvement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_vector_recall_pct_05(record):
    """Evaluate supplier vector recall for control WP-0488-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vector_recall_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-05", "metric": "supplier_vector_recall_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-05", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-05", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-05", "metric": "supplier_vector_recall_pct", "label": "supplier vector recall",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier vector recall falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_capacity_forecast_confidence_pct_06(record):
    """Evaluate supplier capacity forecast confidence for control WP-0488-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-06", "metric": "supplier_capacity_forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-06", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-06", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-06", "metric": "supplier_capacity_forecast_confidence_pct", "label": "supplier capacity forecast confidence",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity forecast confidence must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_ip_claim_count_07(record):
    """Evaluate supplier IP claims for control WP-0488-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ip_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-07", "metric": "supplier_ip_claim_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-07", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-07", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-07", "metric": "supplier_ip_claim_count", "label": "supplier IP claims",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier IP claims must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_policy_review_age_days_08(record):
    """Evaluate supplier policy review age for control WP-0488-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-08", "metric": "supplier_policy_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-08", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-08", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-08", "metric": "supplier_policy_review_age_days", "label": "supplier policy review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier policy review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_catalog_compliance_pct_09(record):
    """Evaluate supplier catalog compliance for control WP-0488-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_catalog_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-09", "metric": "supplier_catalog_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-09", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-09", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-09", "metric": "supplier_catalog_compliance_pct", "label": "supplier catalog compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier catalog compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_scrap_pct_10(record):
    """Evaluate supplier scrap rate for control WP-0488-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scrap_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-10", "metric": "supplier_scrap_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-10", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-10", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-10", "metric": "supplier_scrap_pct", "label": "supplier scrap rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier scrap rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_scorecard_dispute_age_days_11(record):
    """Evaluate scorecard dispute age for control WP-0488-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-11", "metric": "supplier_scorecard_dispute_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-11", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-11", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-11", "metric": "supplier_scorecard_dispute_age_days", "label": "scorecard dispute age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scorecard dispute age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_final_invoice_age_days_12(record):
    """Evaluate supplier final invoice age for control WP-0488-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-12", "metric": "supplier_final_invoice_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-12", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-12", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-12", "metric": "supplier_final_invoice_age_days", "label": "supplier final invoice age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier final invoice age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_otif_pct_13(record):
    """Evaluate supplier OTIF for control WP-0488-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_otif_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-13", "metric": "supplier_otif_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-13", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-13", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-13", "metric": "supplier_otif_pct", "label": "supplier OTIF",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier OTIF falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_pallet_overhang_cm_14(record):
    """Evaluate pallet overhang for control WP-0488-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_overhang_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-14", "metric": "pallet_overhang_cm",
            "status": "insufficient_data",
            "severity": "medium", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-14", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-14", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-14", "metric": "pallet_overhang_cm", "label": "pallet overhang",
        "status": "breach", "severity": "medium", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pallet overhang must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_putaway_age_hours_15(record):
    """Evaluate putaway age for control WP-0488-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-15", "metric": "putaway_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-15", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-15", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-15", "metric": "putaway_age_hours", "label": "putaway age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "putaway age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_incident_rate_pct_16(record):
    """Evaluate incident rate for control WP-0488-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-16", "metric": "incident_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-16", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-16", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-16", "metric": "incident_rate_pct", "label": "incident rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "incident rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_audit_age_days_17(record):
    """Evaluate supplier audit age for control WP-0488-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-17", "metric": "supplier_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-17", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-17", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-17", "metric": "supplier_audit_age_days", "label": "supplier audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_restore_success_pct_18(record):
    """Evaluate restore success rate for control WP-0488-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-18", "metric": "restore_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-18", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-18", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-18", "metric": "restore_success_pct", "label": "restore success rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restore success rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_safety_stock_days_19(record):
    """Evaluate safety stock cover for control WP-0488-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-19", "metric": "safety_stock_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-19", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-19", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-19", "metric": "safety_stock_days", "label": "safety stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "safety stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_fatigue_score_20(record):
    """Evaluate fatigue score for control WP-0488-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fatigue_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-20", "metric": "fatigue_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-20", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-20", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-20", "metric": "fatigue_score", "label": "fatigue score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "fatigue score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_scrap_approval_age_hours_21(record):
    """Evaluate scrap approval age for control WP-0488-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scrap_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-21", "metric": "scrap_approval_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-21", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-21", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-21", "metric": "scrap_approval_age_hours", "label": "scrap approval age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "scrap approval age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_serial_audit_match_pct_22(record):
    """Evaluate serial audit match for control WP-0488-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_audit_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-22", "metric": "serial_audit_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-22", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-22", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-22", "metric": "serial_audit_match_pct", "label": "serial audit match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial audit match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_hazmat_segregation_pct_23(record):
    """Evaluate hazmat segregation compliance for control WP-0488-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_segregation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-23", "metric": "hazmat_segregation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-23", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-23", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-23", "metric": "hazmat_segregation_pct", "label": "hazmat segregation compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "hazmat segregation compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_training_assessment_pct_24(record):
    """Evaluate training assessment score for control WP-0488-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_assessment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0488-24", "metric": "training_assessment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0488-24", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0488-24", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0488-24", "metric": "training_assessment_pct", "label": "training assessment score",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "training assessment score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_major_finding_count_01, assess_supplier_community_impact_score_02, assess_supplier_recovery_capacity_pct_03, assess_supplier_delivery_improvement_pct_04, assess_supplier_vector_recall_pct_05, assess_supplier_capacity_forecast_confidence_pct_06, assess_supplier_ip_claim_count_07, assess_supplier_policy_review_age_days_08, assess_supplier_catalog_compliance_pct_09, assess_supplier_scrap_pct_10, assess_supplier_scorecard_dispute_age_days_11, assess_supplier_final_invoice_age_days_12, assess_supplier_otif_pct_13, assess_pallet_overhang_cm_14, assess_putaway_age_hours_15, assess_incident_rate_pct_16, assess_supplier_audit_age_days_17, assess_restore_success_pct_18, assess_safety_stock_days_19, assess_fatigue_score_20, assess_scrap_approval_age_hours_21, assess_serial_audit_match_pct_22, assess_hazmat_segregation_pct_23, assess_training_assessment_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

