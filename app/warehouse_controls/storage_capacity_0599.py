"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_carrier_invoice_match_pct_01(record):
    """Evaluate carrier invoice match for control WP-0599-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-01", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-01", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-01", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-01", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_geofence_breach_count_02(record):
    """Evaluate geofence breaches for control WP-0599-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("geofence_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-02", "metric": "geofence_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-02", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-02", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-02", "metric": "geofence_breach_count", "label": "geofence breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "geofence breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_contract_renewal_days_left_03(record):
    """Evaluate contract renewal validity for control WP-0599-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_renewal_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-03", "metric": "contract_renewal_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-03", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-03", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-03", "metric": "contract_renewal_days_left", "label": "contract renewal validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "contract renewal validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_material_traceability_pct_04(record):
    """Evaluate supplier material traceability for control WP-0599-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-04", "metric": "supplier_material_traceability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-04", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-04", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-04", "metric": "supplier_material_traceability_pct", "label": "supplier material traceability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "supplier material traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_label_validation_age_days_05(record):
    """Evaluate supplier label validation age for control WP-0599-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-05", "metric": "supplier_label_validation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-05", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-05", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-05", "metric": "supplier_label_validation_age_days", "label": "supplier label validation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label validation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_sanctions_screen_age_days_06(record):
    """Evaluate supplier sanctions-screen age for control WP-0599-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_screen_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-06", "metric": "supplier_sanctions_screen_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-06", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-06", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-06", "metric": "supplier_sanctions_screen_age_days", "label": "supplier sanctions-screen age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sanctions-screen age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_concentration_risk_score_07(record):
    """Evaluate supplier concentration risk for control WP-0599-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-07", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-07", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-07", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-07", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier concentration risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_repairability_score_08(record):
    """Evaluate supplier repairability for control WP-0599-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repairability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-08", "metric": "supplier_repairability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-08", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-08", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-08", "metric": "supplier_repairability_score", "label": "supplier repairability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "supplier repairability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_customer_complaint_rate_pct_09(record):
    """Evaluate supplier customer complaint rate for control WP-0599-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_complaint_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-09", "metric": "supplier_customer_complaint_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-09", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-09", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-09", "metric": "supplier_customer_complaint_rate_pct", "label": "supplier customer complaint rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer complaint rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_control_plan_age_days_10(record):
    """Evaluate supplier control-plan age for control WP-0599-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-10", "metric": "supplier_control_plan_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-10", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-10", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-10", "metric": "supplier_control_plan_age_days", "label": "supplier control-plan age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control-plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_evacuation_drill_age_days_11(record):
    """Evaluate supplier evacuation drill age for control WP-0599-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evacuation_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-11", "metric": "supplier_evacuation_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-11", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-11", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-11", "metric": "supplier_evacuation_drill_age_days", "label": "supplier evacuation drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier evacuation drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_cash_runway_days_12(record):
    """Evaluate supplier cash runway for control WP-0599-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cash_runway_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-12", "metric": "supplier_cash_runway_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-12", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-12", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-12", "metric": "supplier_cash_runway_days", "label": "supplier cash runway",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier cash runway falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_document_control_pct_13(record):
    """Evaluate supplier document control for control WP-0599-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-13", "metric": "supplier_document_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-13", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-13", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-13", "metric": "supplier_document_control_pct", "label": "supplier document control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier document control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_model_card_age_days_14(record):
    """Evaluate supplier model-card age for control WP-0599-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_card_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-14", "metric": "supplier_model_card_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-14", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-14", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-14", "metric": "supplier_model_card_age_days", "label": "supplier model-card age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model-card age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_ordering_violation_count_15(record):
    """Evaluate supplier ordering violations for control WP-0599-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ordering_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-15", "metric": "supplier_ordering_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-15", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-15", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-15", "metric": "supplier_ordering_violation_count", "label": "supplier ordering violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier ordering violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_vulnerability_sla_breach_count_16(record):
    """Evaluate supplier vulnerability SLA breaches for control WP-0599-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-16", "metric": "supplier_vulnerability_sla_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-16", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-16", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-16", "metric": "supplier_vulnerability_sla_breach_count", "label": "supplier vulnerability SLA breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier vulnerability SLA breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_media_encryption_pct_17(record):
    """Evaluate supplier media encryption for control WP-0599-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_media_encryption_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-17", "metric": "supplier_media_encryption_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-17", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-17", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-17", "metric": "supplier_media_encryption_pct", "label": "supplier media encryption",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier media encryption must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_conflict_check_pct_18(record):
    """Evaluate supplier conflict checks for control WP-0599-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_check_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-18", "metric": "supplier_conflict_check_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-18", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-18", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-18", "metric": "supplier_conflict_check_pct", "label": "supplier conflict checks",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier conflict checks must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_order_freeze_violation_count_19(record):
    """Evaluate order-freeze violations for control WP-0599-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_freeze_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-19", "metric": "supplier_order_freeze_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-19", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-19", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-19", "metric": "supplier_order_freeze_violation_count", "label": "order-freeze violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "order-freeze violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_tracking_upload_pct_20(record):
    """Evaluate supplier tracking upload for control WP-0599-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tracking_upload_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-20", "metric": "supplier_tracking_upload_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-20", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-20", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-20", "metric": "supplier_tracking_upload_pct", "label": "supplier tracking upload",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier tracking upload falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_access_revocation_pct_21(record):
    """Evaluate supplier access revocation for control WP-0599-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-21", "metric": "supplier_access_revocation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-21", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-21", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-21", "metric": "supplier_access_revocation_pct", "label": "supplier access revocation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access revocation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_occupied_units_22(record):
    """Evaluate occupied capacity for control WP-0599-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("occupied_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-22", "metric": "occupied_units",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-22", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-22", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-22", "metric": "occupied_units", "label": "occupied capacity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "occupied capacity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_queue_depth_23(record):
    """Evaluate queue depth for control WP-0599-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-23", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "medium", "unit": "jobs",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-23", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-23", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-23", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "medium", "unit": "jobs",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "queue depth exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_obsolete_stock_value_24(record):
    """Evaluate obsolete stock value for control WP-0599-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0599-24", "metric": "obsolete_stock_value",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0599-24", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0599-24", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0599-24", "metric": "obsolete_stock_value", "label": "obsolete stock value",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "obsolete stock value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_carrier_invoice_match_pct_01, assess_geofence_breach_count_02, assess_contract_renewal_days_left_03, assess_supplier_material_traceability_pct_04, assess_supplier_label_validation_age_days_05, assess_supplier_sanctions_screen_age_days_06, assess_supplier_concentration_risk_score_07, assess_supplier_repairability_score_08, assess_supplier_customer_complaint_rate_pct_09, assess_supplier_control_plan_age_days_10, assess_supplier_evacuation_drill_age_days_11, assess_supplier_cash_runway_days_12, assess_supplier_document_control_pct_13, assess_supplier_model_card_age_days_14, assess_supplier_ordering_violation_count_15, assess_supplier_vulnerability_sla_breach_count_16, assess_supplier_media_encryption_pct_17, assess_supplier_conflict_check_pct_18, assess_supplier_order_freeze_violation_count_19, assess_supplier_tracking_upload_pct_20, assess_supplier_access_revocation_pct_21, assess_occupied_units_22, assess_queue_depth_23, assess_obsolete_stock_value_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

