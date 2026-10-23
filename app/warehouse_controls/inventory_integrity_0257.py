"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_address_quality_score_01(record):
    """Evaluate address quality for control WP-0257-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-01", "metric": "address_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-01", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-01", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-01", "metric": "address_quality_score", "label": "address quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "address quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_negative_stock_count_02(record):
    """Evaluate negative stock records for control WP-0257-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("negative_stock_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-02", "metric": "negative_stock_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-02", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-02", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-02", "metric": "negative_stock_count", "label": "negative stock records",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "negative stock records falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_reverse_logistics_cost_03(record):
    """Evaluate reverse logistics cost for control WP-0257-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reverse_logistics_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-03", "metric": "reverse_logistics_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-03", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-03", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-03", "metric": "reverse_logistics_cost", "label": "reverse logistics cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reverse logistics cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_weighbridge_variance_pct_04(record):
    """Evaluate weighbridge variance for control WP-0257-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighbridge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-04", "metric": "weighbridge_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-04", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-04", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-04", "metric": "weighbridge_variance_pct", "label": "weighbridge variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "weighbridge variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_offline_sync_age_hours_05(record):
    """Evaluate offline sync age for control WP-0257-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("offline_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-05", "metric": "offline_sync_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-05", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-05", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-05", "metric": "offline_sync_age_hours", "label": "offline sync age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "offline sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_weight_capture_pct_06(record):
    """Evaluate weight capture rate for control WP-0257-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-06", "metric": "weight_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-06", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-06", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-06", "metric": "weight_capture_pct", "label": "weight capture rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "weight capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_evidence_attachment_pct_07(record):
    """Evaluate evidence attachment completeness for control WP-0257-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evidence_attachment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-07", "metric": "evidence_attachment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-07", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-07", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-07", "metric": "evidence_attachment_pct", "label": "evidence attachment completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "evidence attachment completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_coolant_remaining_pct_08(record):
    """Evaluate coolant remaining for control WP-0257-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-08", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-08", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-08", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-08", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "coolant remaining must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_open_box_age_days_09(record):
    """Evaluate open-box age for control WP-0257-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-09", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-09", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-09", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-09", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "open-box age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_racking_inspection_age_days_10(record):
    """Evaluate racking inspection age for control WP-0257-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("racking_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-10", "metric": "racking_inspection_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-10", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-10", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-10", "metric": "racking_inspection_age_days", "label": "racking inspection age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "racking inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_robot_cycle_time_seconds_11(record):
    """Evaluate robot cycle time for control WP-0257-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_cycle_time_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-11", "metric": "robot_cycle_time_seconds",
            "status": "insufficient_data",
            "severity": "critical", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-11", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-11", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-11", "metric": "robot_cycle_time_seconds", "label": "robot cycle time",
        "status": "breach", "severity": "critical", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "robot cycle time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_on_call_ack_minutes_12(record):
    """Evaluate on-call acknowledgement for control WP-0257-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("on_call_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-12", "metric": "on_call_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-12", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-12", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-12", "metric": "on_call_ack_minutes", "label": "on-call acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "on-call acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_mobile_app_crash_pct_13(record):
    """Evaluate mobile app crash rate for control WP-0257-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_app_crash_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-13", "metric": "mobile_app_crash_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-13", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-13", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-13", "metric": "mobile_app_crash_pct", "label": "mobile app crash rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "mobile app crash rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_customer_contact_valid_pct_14(record):
    """Evaluate customer contact validity for control WP-0257-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-14", "metric": "customer_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-14", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-14", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-14", "metric": "customer_contact_valid_pct", "label": "customer contact validity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "customer contact validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_quality_hold_pct_15(record):
    """Evaluate quality hold share for control WP-0257-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-15", "metric": "quality_hold_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-15", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-15", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-15", "metric": "quality_hold_pct", "label": "quality hold share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality hold share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_order_cancellation_pct_16(record):
    """Evaluate order cancellation rate for control WP-0257-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_cancellation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-16", "metric": "order_cancellation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-16", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-16", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-16", "metric": "order_cancellation_pct", "label": "order cancellation rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order cancellation rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_port_dwell_days_17(record):
    """Evaluate port dwell for control WP-0257-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("port_dwell_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-17", "metric": "port_dwell_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-17", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-17", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-17", "metric": "port_dwell_days", "label": "port dwell",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "port dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_labor_cost_per_unit_18(record):
    """Evaluate labor cost per unit for control WP-0257-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_cost_per_unit")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-18", "metric": "labor_cost_per_unit",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-18", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-18", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-18", "metric": "labor_cost_per_unit", "label": "labor cost per unit",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "labor cost per unit falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_ethics_report_age_days_19(record):
    """Evaluate supplier ethics report age for control WP-0257-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_report_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-19", "metric": "supplier_ethics_report_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-19", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-19", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-19", "metric": "supplier_ethics_report_age_days", "label": "supplier ethics report age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ethics report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_patch_age_days_20(record):
    """Evaluate supplier patch age for control WP-0257-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-20", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-20", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-20", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-20", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_recovery_lead_days_21(record):
    """Evaluate supplier recovery lead time for control WP-0257-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-21", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-21", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-21", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-21", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier recovery lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_subprocessor_count_22(record):
    """Evaluate supplier sub-processors for control WP-0257-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-22", "metric": "supplier_subprocessor_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "entities",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-22", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-22", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-22", "metric": "supplier_subprocessor_count", "label": "supplier sub-processors",
        "status": "breach", "severity": "high", "unit": "entities",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "supplier sub-processors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_water_continuity_score_23(record):
    """Evaluate supplier water continuity for control WP-0257-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-23", "metric": "supplier_water_continuity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-23", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-23", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-23", "metric": "supplier_water_continuity_score", "label": "supplier water continuity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water continuity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_climate_plan_age_days_24(record):
    """Evaluate supplier climate-plan age for control WP-0257-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_climate_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0257-24", "metric": "supplier_climate_plan_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0257-24", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0257-24", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0257-24", "metric": "supplier_climate_plan_age_days", "label": "supplier climate-plan age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier climate-plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_address_quality_score_01, assess_negative_stock_count_02, assess_reverse_logistics_cost_03, assess_weighbridge_variance_pct_04, assess_offline_sync_age_hours_05, assess_weight_capture_pct_06, assess_evidence_attachment_pct_07, assess_coolant_remaining_pct_08, assess_open_box_age_days_09, assess_racking_inspection_age_days_10, assess_robot_cycle_time_seconds_11, assess_on_call_ack_minutes_12, assess_mobile_app_crash_pct_13, assess_customer_contact_valid_pct_14, assess_quality_hold_pct_15, assess_order_cancellation_pct_16, assess_port_dwell_days_17, assess_labor_cost_per_unit_18, assess_supplier_ethics_report_age_days_19, assess_supplier_patch_age_days_20, assess_supplier_recovery_lead_days_21, assess_supplier_subprocessor_count_22, assess_supplier_water_continuity_score_23, assess_supplier_climate_plan_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

