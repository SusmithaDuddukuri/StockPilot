"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_linehaul_departure_delay_minutes_01(record):
    """Evaluate linehaul departure delay for control WP-0344-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("linehaul_departure_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-01", "metric": "linehaul_departure_delay_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-01", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-01", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-01", "metric": "linehaul_departure_delay_minutes", "label": "linehaul departure delay",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "linehaul departure delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_carrier_invoice_match_pct_02(record):
    """Evaluate carrier invoice match for control WP-0344-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-02", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-02", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-02", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-02", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_geofence_breach_count_03(record):
    """Evaluate geofence breaches for control WP-0344-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("geofence_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-03", "metric": "geofence_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-03", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-03", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-03", "metric": "geofence_breach_count", "label": "geofence breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "geofence breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_contract_renewal_days_left_04(record):
    """Evaluate contract renewal validity for control WP-0344-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_renewal_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-04", "metric": "contract_renewal_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-04", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-04", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-04", "metric": "contract_renewal_days_left", "label": "contract renewal validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "contract renewal validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_material_traceability_pct_05(record):
    """Evaluate supplier material traceability for control WP-0344-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-05", "metric": "supplier_material_traceability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-05", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-05", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-05", "metric": "supplier_material_traceability_pct", "label": "supplier material traceability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier material traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_label_validation_age_days_06(record):
    """Evaluate supplier label validation age for control WP-0344-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-06", "metric": "supplier_label_validation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-06", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-06", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-06", "metric": "supplier_label_validation_age_days", "label": "supplier label validation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label validation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_sanctions_screen_age_days_07(record):
    """Evaluate supplier sanctions-screen age for control WP-0344-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_screen_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-07", "metric": "supplier_sanctions_screen_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-07", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-07", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-07", "metric": "supplier_sanctions_screen_age_days", "label": "supplier sanctions-screen age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sanctions-screen age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_concentration_risk_score_08(record):
    """Evaluate supplier concentration risk for control WP-0344-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-08", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-08", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-08", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-08", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier concentration risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_repairability_score_09(record):
    """Evaluate supplier repairability for control WP-0344-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repairability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-09", "metric": "supplier_repairability_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-09", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-09", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-09", "metric": "supplier_repairability_score", "label": "supplier repairability",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier repairability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_customer_complaint_rate_pct_10(record):
    """Evaluate supplier customer complaint rate for control WP-0344-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_complaint_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-10", "metric": "supplier_customer_complaint_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-10", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-10", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-10", "metric": "supplier_customer_complaint_rate_pct", "label": "supplier customer complaint rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer complaint rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_control_plan_age_days_11(record):
    """Evaluate supplier control-plan age for control WP-0344-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-11", "metric": "supplier_control_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-11", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-11", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-11", "metric": "supplier_control_plan_age_days", "label": "supplier control-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control-plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_evacuation_drill_age_days_12(record):
    """Evaluate supplier evacuation drill age for control WP-0344-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evacuation_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-12", "metric": "supplier_evacuation_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-12", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-12", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-12", "metric": "supplier_evacuation_drill_age_days", "label": "supplier evacuation drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "supplier evacuation drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_cash_runway_days_13(record):
    """Evaluate supplier cash runway for control WP-0344-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cash_runway_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-13", "metric": "supplier_cash_runway_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-13", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-13", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-13", "metric": "supplier_cash_runway_days", "label": "supplier cash runway",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier cash runway falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_document_control_pct_14(record):
    """Evaluate supplier document control for control WP-0344-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-14", "metric": "supplier_document_control_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-14", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-14", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-14", "metric": "supplier_document_control_pct", "label": "supplier document control",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier document control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_model_card_age_days_15(record):
    """Evaluate supplier model-card age for control WP-0344-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_card_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-15", "metric": "supplier_model_card_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-15", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-15", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-15", "metric": "supplier_model_card_age_days", "label": "supplier model-card age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model-card age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_ordering_violation_count_16(record):
    """Evaluate supplier ordering violations for control WP-0344-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ordering_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-16", "metric": "supplier_ordering_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-16", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-16", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-16", "metric": "supplier_ordering_violation_count", "label": "supplier ordering violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "supplier ordering violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_vulnerability_sla_breach_count_17(record):
    """Evaluate supplier vulnerability SLA breaches for control WP-0344-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-17", "metric": "supplier_vulnerability_sla_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-17", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-17", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-17", "metric": "supplier_vulnerability_sla_breach_count", "label": "supplier vulnerability SLA breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier vulnerability SLA breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_media_encryption_pct_18(record):
    """Evaluate supplier media encryption for control WP-0344-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_media_encryption_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-18", "metric": "supplier_media_encryption_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-18", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-18", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-18", "metric": "supplier_media_encryption_pct", "label": "supplier media encryption",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier media encryption must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_conflict_check_pct_19(record):
    """Evaluate supplier conflict checks for control WP-0344-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_check_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-19", "metric": "supplier_conflict_check_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-19", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-19", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-19", "metric": "supplier_conflict_check_pct", "label": "supplier conflict checks",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier conflict checks must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_order_freeze_violation_count_20(record):
    """Evaluate order-freeze violations for control WP-0344-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_freeze_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-20", "metric": "supplier_order_freeze_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-20", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-20", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-20", "metric": "supplier_order_freeze_violation_count", "label": "order-freeze violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "order-freeze violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_tracking_upload_pct_21(record):
    """Evaluate supplier tracking upload for control WP-0344-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tracking_upload_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-21", "metric": "supplier_tracking_upload_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-21", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-21", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-21", "metric": "supplier_tracking_upload_pct", "label": "supplier tracking upload",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier tracking upload falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_access_revocation_pct_22(record):
    """Evaluate supplier access revocation for control WP-0344-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-22", "metric": "supplier_access_revocation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-22", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-22", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-22", "metric": "supplier_access_revocation_pct", "label": "supplier access revocation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access revocation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_occupied_units_23(record):
    """Evaluate occupied capacity for control WP-0344-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("occupied_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-23", "metric": "occupied_units",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-23", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-23", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-23", "metric": "occupied_units", "label": "occupied capacity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "occupied capacity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_queue_depth_24(record):
    """Evaluate queue depth for control WP-0344-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0344-24", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "critical", "unit": "jobs",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0344-24", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0344-24", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0344-24", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "critical", "unit": "jobs",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "queue depth exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_linehaul_departure_delay_minutes_01, assess_carrier_invoice_match_pct_02, assess_geofence_breach_count_03, assess_contract_renewal_days_left_04, assess_supplier_material_traceability_pct_05, assess_supplier_label_validation_age_days_06, assess_supplier_sanctions_screen_age_days_07, assess_supplier_concentration_risk_score_08, assess_supplier_repairability_score_09, assess_supplier_customer_complaint_rate_pct_10, assess_supplier_control_plan_age_days_11, assess_supplier_evacuation_drill_age_days_12, assess_supplier_cash_runway_days_13, assess_supplier_document_control_pct_14, assess_supplier_model_card_age_days_15, assess_supplier_ordering_violation_count_16, assess_supplier_vulnerability_sla_breach_count_17, assess_supplier_media_encryption_pct_18, assess_supplier_conflict_check_pct_19, assess_supplier_order_freeze_violation_count_20, assess_supplier_tracking_upload_pct_21, assess_supplier_access_revocation_pct_22, assess_occupied_units_23, assess_queue_depth_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

