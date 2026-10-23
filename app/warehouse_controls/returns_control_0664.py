"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_roadside_assistance_age_days_01(record):
    """Evaluate roadside assistance review age for control WP-0664-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("roadside_assistance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-01", "metric": "roadside_assistance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-01", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-01", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-01", "metric": "roadside_assistance_age_days", "label": "roadside assistance review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "roadside assistance review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_purchase_requisition_age_hours_02(record):
    """Evaluate purchase requisition age for control WP-0664-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_requisition_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-02", "metric": "purchase_requisition_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-02", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-02", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-02", "metric": "purchase_requisition_age_hours", "label": "purchase requisition age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "purchase requisition age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_single_site_pct_03(record):
    """Evaluate supplier single-site dependency for control WP-0664-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_single_site_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-03", "metric": "supplier_single_site_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-03", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-03", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-03", "metric": "supplier_single_site_pct", "label": "supplier single-site dependency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier single-site dependency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_measurement_system_score_04(record):
    """Evaluate supplier measurement system score for control WP-0664-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_system_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-04", "metric": "supplier_measurement_system_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-04", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-04", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-04", "metric": "supplier_measurement_system_score", "label": "supplier measurement system score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier measurement system score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_origin_document_pct_05(record):
    """Evaluate supplier origin-document completeness for control WP-0664-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_origin_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-05", "metric": "supplier_origin_document_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-05", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-05", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-05", "metric": "supplier_origin_document_pct", "label": "supplier origin-document completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier origin-document completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_transition_readiness_pct_06(record):
    """Evaluate supplier transition readiness for control WP-0664-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-06", "metric": "supplier_transition_readiness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-06", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-06", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-06", "metric": "supplier_transition_readiness_pct", "label": "supplier transition readiness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transition readiness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_serial_warranty_match_pct_07(record):
    """Evaluate supplier serial/warranty match for control WP-0664-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_warranty_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-07", "metric": "supplier_serial_warranty_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-07", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-07", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-07", "metric": "supplier_serial_warranty_match_pct", "label": "supplier serial/warranty match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier serial/warranty match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_claim_settlement_days_08(record):
    """Evaluate supplier claim settlement time for control WP-0664-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_settlement_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-08", "metric": "supplier_claim_settlement_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-08", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-08", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-08", "metric": "supplier_claim_settlement_days", "label": "supplier claim settlement time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "supplier claim settlement time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_ppap_approval_pct_09(record):
    """Evaluate supplier PPAP approval for control WP-0664-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppap_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-09", "metric": "supplier_ppap_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-09", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-09", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-09", "metric": "supplier_ppap_approval_pct", "label": "supplier PPAP approval",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier PPAP approval falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_spill_response_drill_age_days_10(record):
    """Evaluate supplier spill drill age for control WP-0664-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spill_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-10", "metric": "supplier_spill_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-10", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-10", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-10", "metric": "supplier_spill_response_drill_age_days", "label": "supplier spill drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier spill drill age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_ar_days_11(record):
    """Evaluate supplier accounts-receivable days for control WP-0664-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ar_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-11", "metric": "supplier_ar_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-11", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-11", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-11", "metric": "supplier_ar_days", "label": "supplier accounts-receivable days",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier accounts-receivable days must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_training_refresh_days_12(record):
    """Evaluate supplier training refresh interval for control WP-0664-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_refresh_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-12", "metric": "supplier_training_refresh_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-12", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-12", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-12", "metric": "supplier_training_refresh_days", "label": "supplier training refresh interval",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "supplier training refresh interval exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_human_override_pct_13(record):
    """Evaluate supplier human override rate for control WP-0664-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_override_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-13", "metric": "supplier_human_override_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-13", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-13", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-13", "metric": "supplier_human_override_pct", "label": "supplier human override rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier human override rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_idempotency_violation_count_14(record):
    """Evaluate supplier idempotency violations for control WP-0664-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_idempotency_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-14", "metric": "supplier_idempotency_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-14", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-14", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-14", "metric": "supplier_idempotency_violation_count", "label": "supplier idempotency violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier idempotency violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_threat_model_age_days_15(record):
    """Evaluate supplier threat-model age for control WP-0664-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_threat_model_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-15", "metric": "supplier_threat_model_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-15", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-15", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-15", "metric": "supplier_threat_model_age_days", "label": "supplier threat-model age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier threat-model age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_screen_lock_pct_16(record):
    """Evaluate supplier screen-lock compliance for control WP-0664-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_screen_lock_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-16", "metric": "supplier_screen_lock_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-16", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-16", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-16", "metric": "supplier_screen_lock_pct", "label": "supplier screen-lock compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier screen-lock compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_manual_override_count_17(record):
    """Evaluate supplier manual overrides for control WP-0664-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-17", "metric": "supplier_manual_override_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-17", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-17", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-17", "metric": "supplier_manual_override_count", "label": "supplier manual overrides",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "supplier manual overrides falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_forecast_commitment_accuracy_pct_18(record):
    """Evaluate forecast commitment accuracy for control WP-0664-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_commitment_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-18", "metric": "supplier_forecast_commitment_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-18", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-18", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-18", "metric": "supplier_forecast_commitment_accuracy_pct", "label": "forecast commitment accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast commitment accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_dispatch_accuracy_pct_19(record):
    """Evaluate supplier dispatch accuracy for control WP-0664-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-19", "metric": "supplier_dispatch_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-19", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-19", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-19", "metric": "supplier_dispatch_accuracy_pct", "label": "supplier dispatch accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dispatch accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_inventory_transfer_match_pct_20(record):
    """Evaluate inventory transfer match for control WP-0664-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-20", "metric": "supplier_inventory_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-20", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-20", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-20", "metric": "supplier_inventory_transfer_match_pct", "label": "inventory transfer match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "inventory transfer match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_inventory_value_21(record):
    """Evaluate inventory value for control WP-0664-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-21", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-21", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-21", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-21", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "inventory value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_label_error_count_22(record):
    """Evaluate label errors for control WP-0664-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-22", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-22", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-22", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-22", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "label errors must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_concentration_pct_23(record):
    """Evaluate supplier concentration for control WP-0664-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-23", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-23", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-23", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-23", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier concentration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_invoice_match_pct_24(record):
    """Evaluate invoice match rate for control WP-0664-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0664-24", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0664-24", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0664-24", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0664-24", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "invoice match rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_roadside_assistance_age_days_01, assess_purchase_requisition_age_hours_02, assess_supplier_single_site_pct_03, assess_supplier_measurement_system_score_04, assess_supplier_origin_document_pct_05, assess_supplier_transition_readiness_pct_06, assess_supplier_serial_warranty_match_pct_07, assess_supplier_claim_settlement_days_08, assess_supplier_ppap_approval_pct_09, assess_supplier_spill_response_drill_age_days_10, assess_supplier_ar_days_11, assess_supplier_training_refresh_days_12, assess_supplier_human_override_pct_13, assess_supplier_idempotency_violation_count_14, assess_supplier_threat_model_age_days_15, assess_supplier_screen_lock_pct_16, assess_supplier_manual_override_count_17, assess_supplier_forecast_commitment_accuracy_pct_18, assess_supplier_dispatch_accuracy_pct_19, assess_supplier_inventory_transfer_match_pct_20, assess_inventory_value_21, assess_label_error_count_22, assess_supplier_concentration_pct_23, assess_invoice_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

