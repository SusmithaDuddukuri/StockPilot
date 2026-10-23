"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_concentration_risk_score_01(record):
    """Evaluate supplier concentration risk for control WP-0356-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-01", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-01", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-01", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-01", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier concentration risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_repairability_score_02(record):
    """Evaluate supplier repairability for control WP-0356-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repairability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-02", "metric": "supplier_repairability_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-02", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-02", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-02", "metric": "supplier_repairability_score", "label": "supplier repairability",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier repairability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_customer_complaint_rate_pct_03(record):
    """Evaluate supplier customer complaint rate for control WP-0356-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_complaint_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-03", "metric": "supplier_customer_complaint_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-03", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-03", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-03", "metric": "supplier_customer_complaint_rate_pct", "label": "supplier customer complaint rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer complaint rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_control_plan_age_days_04(record):
    """Evaluate supplier control-plan age for control WP-0356-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-04", "metric": "supplier_control_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-04", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-04", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-04", "metric": "supplier_control_plan_age_days", "label": "supplier control-plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier control-plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_evacuation_drill_age_days_05(record):
    """Evaluate supplier evacuation drill age for control WP-0356-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evacuation_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-05", "metric": "supplier_evacuation_drill_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-05", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-05", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-05", "metric": "supplier_evacuation_drill_age_days", "label": "supplier evacuation drill age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier evacuation drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_cash_runway_days_06(record):
    """Evaluate supplier cash runway for control WP-0356-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cash_runway_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-06", "metric": "supplier_cash_runway_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-06", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-06", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-06", "metric": "supplier_cash_runway_days", "label": "supplier cash runway",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cash runway must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_document_control_pct_07(record):
    """Evaluate supplier document control for control WP-0356-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-07", "metric": "supplier_document_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-07", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-07", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-07", "metric": "supplier_document_control_pct", "label": "supplier document control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier document control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_model_card_age_days_08(record):
    """Evaluate supplier model-card age for control WP-0356-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_card_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-08", "metric": "supplier_model_card_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-08", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-08", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-08", "metric": "supplier_model_card_age_days", "label": "supplier model-card age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier model-card age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_ordering_violation_count_09(record):
    """Evaluate supplier ordering violations for control WP-0356-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ordering_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-09", "metric": "supplier_ordering_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-09", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-09", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-09", "metric": "supplier_ordering_violation_count", "label": "supplier ordering violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier ordering violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_vulnerability_sla_breach_count_10(record):
    """Evaluate supplier vulnerability SLA breaches for control WP-0356-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-10", "metric": "supplier_vulnerability_sla_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-10", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-10", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-10", "metric": "supplier_vulnerability_sla_breach_count", "label": "supplier vulnerability SLA breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vulnerability SLA breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_media_encryption_pct_11(record):
    """Evaluate supplier media encryption for control WP-0356-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_media_encryption_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-11", "metric": "supplier_media_encryption_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-11", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-11", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-11", "metric": "supplier_media_encryption_pct", "label": "supplier media encryption",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier media encryption must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_conflict_check_pct_12(record):
    """Evaluate supplier conflict checks for control WP-0356-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_check_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-12", "metric": "supplier_conflict_check_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-12", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-12", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-12", "metric": "supplier_conflict_check_pct", "label": "supplier conflict checks",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier conflict checks exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_order_freeze_violation_count_13(record):
    """Evaluate order-freeze violations for control WP-0356-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_freeze_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-13", "metric": "supplier_order_freeze_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-13", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-13", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-13", "metric": "supplier_order_freeze_violation_count", "label": "order-freeze violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "order-freeze violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_tracking_upload_pct_14(record):
    """Evaluate supplier tracking upload for control WP-0356-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tracking_upload_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-14", "metric": "supplier_tracking_upload_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-14", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-14", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-14", "metric": "supplier_tracking_upload_pct", "label": "supplier tracking upload",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tracking upload must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_access_revocation_pct_15(record):
    """Evaluate supplier access revocation for control WP-0356-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-15", "metric": "supplier_access_revocation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-15", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-15", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-15", "metric": "supplier_access_revocation_pct", "label": "supplier access revocation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access revocation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_occupied_units_16(record):
    """Evaluate occupied capacity for control WP-0356-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("occupied_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-16", "metric": "occupied_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-16", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-16", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-16", "metric": "occupied_units", "label": "occupied capacity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "occupied capacity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_queue_depth_17(record):
    """Evaluate queue depth for control WP-0356-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-17", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "low", "unit": "jobs",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-17", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-17", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-17", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "low", "unit": "jobs",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "queue depth falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_obsolete_stock_value_18(record):
    """Evaluate obsolete stock value for control WP-0356-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-18", "metric": "obsolete_stock_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-18", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-18", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-18", "metric": "obsolete_stock_value", "label": "obsolete stock value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "obsolete stock value must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_budget_variance_pct_19(record):
    """Evaluate budget variance for control WP-0356-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-19", "metric": "budget_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-19", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-19", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-19", "metric": "budget_variance_pct", "label": "budget variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "budget variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_emissions_kg_per_order_20(record):
    """Evaluate emissions per order for control WP-0356-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emissions_kg_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-20", "metric": "emissions_kg_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-20", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-20", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-20", "metric": "emissions_kg_per_order", "label": "emissions per order",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "emissions per order exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_privacy_request_age_days_21(record):
    """Evaluate privacy request age for control WP-0356-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-21", "metric": "privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-21", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-21", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-21", "metric": "privacy_request_age_days", "label": "privacy request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "privacy request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_training_completion_pct_22(record):
    """Evaluate training completion for control WP-0356-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-22", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-22", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-22", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-22", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "training completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_ppe_compliance_pct_23(record):
    """Evaluate PPE compliance for control WP-0356-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-23", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-23", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-23", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-23", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "PPE compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_failed_delivery_rate_pct_24(record):
    """Evaluate failed delivery rate for control WP-0356-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0356-24", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0356-24", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0356-24", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0356-24", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "failed delivery rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_concentration_risk_score_01, assess_supplier_repairability_score_02, assess_supplier_customer_complaint_rate_pct_03, assess_supplier_control_plan_age_days_04, assess_supplier_evacuation_drill_age_days_05, assess_supplier_cash_runway_days_06, assess_supplier_document_control_pct_07, assess_supplier_model_card_age_days_08, assess_supplier_ordering_violation_count_09, assess_supplier_vulnerability_sla_breach_count_10, assess_supplier_media_encryption_pct_11, assess_supplier_conflict_check_pct_12, assess_supplier_order_freeze_violation_count_13, assess_supplier_tracking_upload_pct_14, assess_supplier_access_revocation_pct_15, assess_occupied_units_16, assess_queue_depth_17, assess_obsolete_stock_value_18, assess_budget_variance_pct_19, assess_emissions_kg_per_order_20, assess_privacy_request_age_days_21, assess_training_completion_pct_22, assess_ppe_compliance_pct_23, assess_failed_delivery_rate_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

