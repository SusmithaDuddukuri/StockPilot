"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_encryption_compliance_pct_01(record):
    """Evaluate supplier encryption compliance for control WP-0165-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-01", "metric": "supplier_encryption_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-01", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-01", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-01", "metric": "supplier_encryption_compliance_pct", "label": "supplier encryption compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier encryption compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_port_alternative_count_02(record):
    """Evaluate supplier port alternatives for control WP-0165-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-02", "metric": "supplier_port_alternative_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "ports",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-02", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-02", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-02", "metric": "supplier_port_alternative_count", "label": "supplier port alternatives",
        "status": "breach", "severity": "high", "unit": "ports",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier port alternatives falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_natural_hazard_score_03(record):
    """Evaluate supplier natural-hazard exposure for control WP-0165-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_natural_hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-03", "metric": "supplier_natural_hazard_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-03", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-03", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-03", "metric": "supplier_natural_hazard_score", "label": "supplier natural-hazard exposure",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier natural-hazard exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_recovery_contact_pct_04(record):
    """Evaluate supplier recovery contact completeness for control WP-0165-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_contact_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-04", "metric": "supplier_recovery_contact_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-04", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-04", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-04", "metric": "supplier_recovery_contact_pct", "label": "supplier recovery contact completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery contact completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_major_finding_count_05(record):
    """Evaluate supplier major findings for control WP-0165-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_major_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-05", "metric": "supplier_major_finding_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-05", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-05", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-05", "metric": "supplier_major_finding_count", "label": "supplier major findings",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier major findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_community_impact_score_06(record):
    """Evaluate supplier community impact for control WP-0165-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_community_impact_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-06", "metric": "supplier_community_impact_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-06", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-06", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-06", "metric": "supplier_community_impact_score", "label": "supplier community impact",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier community impact falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_recovery_capacity_pct_07(record):
    """Evaluate supplier recovery capacity for control WP-0165-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-07", "metric": "supplier_recovery_capacity_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-07", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-07", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-07", "metric": "supplier_recovery_capacity_pct", "label": "supplier recovery capacity",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery capacity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_delivery_improvement_pct_08(record):
    """Evaluate supplier delivery improvement for control WP-0165-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-08", "metric": "supplier_delivery_improvement_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-08", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-08", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-08", "metric": "supplier_delivery_improvement_pct", "label": "supplier delivery improvement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier delivery improvement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_vector_recall_pct_09(record):
    """Evaluate supplier vector recall for control WP-0165-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vector_recall_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-09", "metric": "supplier_vector_recall_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-09", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-09", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-09", "metric": "supplier_vector_recall_pct", "label": "supplier vector recall",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier vector recall exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_capacity_forecast_confidence_pct_10(record):
    """Evaluate supplier capacity forecast confidence for control WP-0165-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-10", "metric": "supplier_capacity_forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-10", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-10", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-10", "metric": "supplier_capacity_forecast_confidence_pct", "label": "supplier capacity forecast confidence",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier capacity forecast confidence falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_ip_claim_count_11(record):
    """Evaluate supplier IP claims for control WP-0165-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ip_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-11", "metric": "supplier_ip_claim_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-11", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-11", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-11", "metric": "supplier_ip_claim_count", "label": "supplier IP claims",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier IP claims must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_policy_review_age_days_12(record):
    """Evaluate supplier policy review age for control WP-0165-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-12", "metric": "supplier_policy_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-12", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-12", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-12", "metric": "supplier_policy_review_age_days", "label": "supplier policy review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier policy review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_catalog_compliance_pct_13(record):
    """Evaluate supplier catalog compliance for control WP-0165-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_catalog_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-13", "metric": "supplier_catalog_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-13", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-13", "metric": "supplier_catalog_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-13", "metric": "supplier_catalog_compliance_pct", "label": "supplier catalog compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier catalog compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_scrap_pct_14(record):
    """Evaluate supplier scrap rate for control WP-0165-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scrap_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-14", "metric": "supplier_scrap_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-14", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-14", "metric": "supplier_scrap_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-14", "metric": "supplier_scrap_pct", "label": "supplier scrap rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier scrap rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_scorecard_dispute_age_days_15(record):
    """Evaluate scorecard dispute age for control WP-0165-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-15", "metric": "supplier_scorecard_dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-15", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-15", "metric": "supplier_scorecard_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-15", "metric": "supplier_scorecard_dispute_age_days", "label": "scorecard dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scorecard dispute age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_final_invoice_age_days_16(record):
    """Evaluate supplier final invoice age for control WP-0165-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-16", "metric": "supplier_final_invoice_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-16", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-16", "metric": "supplier_final_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-16", "metric": "supplier_final_invoice_age_days", "label": "supplier final invoice age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier final invoice age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_otif_pct_17(record):
    """Evaluate supplier OTIF for control WP-0165-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_otif_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-17", "metric": "supplier_otif_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-17", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-17", "metric": "supplier_otif_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-17", "metric": "supplier_otif_pct", "label": "supplier OTIF",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier OTIF exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_pallet_overhang_cm_18(record):
    """Evaluate pallet overhang for control WP-0165-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_overhang_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-18", "metric": "pallet_overhang_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-18", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-18", "metric": "pallet_overhang_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-18", "metric": "pallet_overhang_cm", "label": "pallet overhang",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "pallet overhang falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_putaway_age_hours_19(record):
    """Evaluate putaway age for control WP-0165-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-19", "metric": "putaway_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-19", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-19", "metric": "putaway_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-19", "metric": "putaway_age_hours", "label": "putaway age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_incident_rate_pct_20(record):
    """Evaluate incident rate for control WP-0165-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-20", "metric": "incident_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-20", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-20", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-20", "metric": "incident_rate_pct", "label": "incident rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_audit_age_days_21(record):
    """Evaluate supplier audit age for control WP-0165-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-21", "metric": "supplier_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-21", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-21", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-21", "metric": "supplier_audit_age_days", "label": "supplier audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_restore_success_pct_22(record):
    """Evaluate restore success rate for control WP-0165-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-22", "metric": "restore_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-22", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-22", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-22", "metric": "restore_success_pct", "label": "restore success rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "restore success rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_safety_stock_days_23(record):
    """Evaluate safety stock cover for control WP-0165-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-23", "metric": "safety_stock_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-23", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-23", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-23", "metric": "safety_stock_days", "label": "safety stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "safety stock cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_fatigue_score_24(record):
    """Evaluate fatigue score for control WP-0165-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fatigue_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0165-24", "metric": "fatigue_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0165-24", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0165-24", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0165-24", "metric": "fatigue_score", "label": "fatigue score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fatigue score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_supplier_encryption_compliance_pct_01, assess_supplier_port_alternative_count_02, assess_supplier_natural_hazard_score_03, assess_supplier_recovery_contact_pct_04, assess_supplier_major_finding_count_05, assess_supplier_community_impact_score_06, assess_supplier_recovery_capacity_pct_07, assess_supplier_delivery_improvement_pct_08, assess_supplier_vector_recall_pct_09, assess_supplier_capacity_forecast_confidence_pct_10, assess_supplier_ip_claim_count_11, assess_supplier_policy_review_age_days_12, assess_supplier_catalog_compliance_pct_13, assess_supplier_scrap_pct_14, assess_supplier_scorecard_dispute_age_days_15, assess_supplier_final_invoice_age_days_16, assess_supplier_otif_pct_17, assess_pallet_overhang_cm_18, assess_putaway_age_hours_19, assess_incident_rate_pct_20, assess_supplier_audit_age_days_21, assess_restore_success_pct_22, assess_safety_stock_days_23, assess_fatigue_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

