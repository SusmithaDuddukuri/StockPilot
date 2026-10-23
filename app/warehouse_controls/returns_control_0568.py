"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_transaction_replay_pct_01(record):
    """Evaluate supplier transaction replay for control WP-0568-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transaction_replay_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-01", "metric": "supplier_transaction_replay_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-01", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-01", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-01", "metric": "supplier_transaction_replay_pct", "label": "supplier transaction replay",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier transaction replay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_reorder_level_02(record):
    """Evaluate reorder point for control WP-0568-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reorder_level")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-02", "metric": "reorder_level",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-02", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-02", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-02", "metric": "reorder_level", "label": "reorder point",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reorder point must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_fuel_cost_per_km_03(record):
    """Evaluate transport cost per km for control WP-0568-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_cost_per_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-03", "metric": "fuel_cost_per_km",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-03", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-03", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-03", "metric": "fuel_cost_per_km", "label": "transport cost per km",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "transport cost per km must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_address_quality_score_04(record):
    """Evaluate address quality for control WP-0568-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-04", "metric": "address_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-04", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-04", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-04", "metric": "address_quality_score", "label": "address quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "address quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_negative_stock_count_05(record):
    """Evaluate negative stock records for control WP-0568-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("negative_stock_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-05", "metric": "negative_stock_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-05", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-05", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-05", "metric": "negative_stock_count", "label": "negative stock records",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "negative stock records falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_reverse_logistics_cost_06(record):
    """Evaluate reverse logistics cost for control WP-0568-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reverse_logistics_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-06", "metric": "reverse_logistics_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-06", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-06", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-06", "metric": "reverse_logistics_cost", "label": "reverse logistics cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reverse logistics cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_weighbridge_variance_pct_07(record):
    """Evaluate weighbridge variance for control WP-0568-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighbridge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-07", "metric": "weighbridge_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-07", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-07", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-07", "metric": "weighbridge_variance_pct", "label": "weighbridge variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "weighbridge variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_offline_sync_age_hours_08(record):
    """Evaluate offline sync age for control WP-0568-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("offline_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-08", "metric": "offline_sync_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-08", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-08", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-08", "metric": "offline_sync_age_hours", "label": "offline sync age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "offline sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_weight_capture_pct_09(record):
    """Evaluate weight capture rate for control WP-0568-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-09", "metric": "weight_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-09", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-09", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-09", "metric": "weight_capture_pct", "label": "weight capture rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "weight capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_evidence_attachment_pct_10(record):
    """Evaluate evidence attachment completeness for control WP-0568-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evidence_attachment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-10", "metric": "evidence_attachment_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-10", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-10", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-10", "metric": "evidence_attachment_pct", "label": "evidence attachment completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "evidence attachment completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_coolant_remaining_pct_11(record):
    """Evaluate coolant remaining for control WP-0568-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-11", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-11", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-11", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-11", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "coolant remaining must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_open_box_age_days_12(record):
    """Evaluate open-box age for control WP-0568-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-12", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-12", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-12", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-12", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "open-box age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_racking_inspection_age_days_13(record):
    """Evaluate racking inspection age for control WP-0568-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("racking_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-13", "metric": "racking_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-13", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-13", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-13", "metric": "racking_inspection_age_days", "label": "racking inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "racking inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_robot_cycle_time_seconds_14(record):
    """Evaluate robot cycle time for control WP-0568-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_cycle_time_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-14", "metric": "robot_cycle_time_seconds",
            "status": "insufficient_data",
            "severity": "medium", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-14", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-14", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-14", "metric": "robot_cycle_time_seconds", "label": "robot cycle time",
        "status": "breach", "severity": "medium", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "robot cycle time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_on_call_ack_minutes_15(record):
    """Evaluate on-call acknowledgement for control WP-0568-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("on_call_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-15", "metric": "on_call_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-15", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-15", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-15", "metric": "on_call_ack_minutes", "label": "on-call acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "on-call acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_mobile_app_crash_pct_16(record):
    """Evaluate mobile app crash rate for control WP-0568-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_app_crash_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-16", "metric": "mobile_app_crash_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-16", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-16", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-16", "metric": "mobile_app_crash_pct", "label": "mobile app crash rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "mobile app crash rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_customer_contact_valid_pct_17(record):
    """Evaluate customer contact validity for control WP-0568-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-17", "metric": "customer_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-17", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-17", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-17", "metric": "customer_contact_valid_pct", "label": "customer contact validity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "customer contact validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_quality_hold_pct_18(record):
    """Evaluate quality hold share for control WP-0568-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-18", "metric": "quality_hold_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-18", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-18", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-18", "metric": "quality_hold_pct", "label": "quality hold share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality hold share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_order_cancellation_pct_19(record):
    """Evaluate order cancellation rate for control WP-0568-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_cancellation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-19", "metric": "order_cancellation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-19", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-19", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-19", "metric": "order_cancellation_pct", "label": "order cancellation rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order cancellation rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_port_dwell_days_20(record):
    """Evaluate port dwell for control WP-0568-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("port_dwell_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-20", "metric": "port_dwell_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-20", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-20", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-20", "metric": "port_dwell_days", "label": "port dwell",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "port dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_labor_cost_per_unit_21(record):
    """Evaluate labor cost per unit for control WP-0568-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_cost_per_unit")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-21", "metric": "labor_cost_per_unit",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-21", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-21", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-21", "metric": "labor_cost_per_unit", "label": "labor cost per unit",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "labor cost per unit falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_ethics_report_age_days_22(record):
    """Evaluate supplier ethics report age for control WP-0568-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_report_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-22", "metric": "supplier_ethics_report_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-22", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-22", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-22", "metric": "supplier_ethics_report_age_days", "label": "supplier ethics report age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ethics report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_patch_age_days_23(record):
    """Evaluate supplier patch age for control WP-0568-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-23", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-23", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-23", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-23", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_recovery_lead_days_24(record):
    """Evaluate supplier recovery lead time for control WP-0568-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0568-24", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0568-24", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0568-24", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0568-24", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier recovery lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_transaction_replay_pct_01, assess_reorder_level_02, assess_fuel_cost_per_km_03, assess_address_quality_score_04, assess_negative_stock_count_05, assess_reverse_logistics_cost_06, assess_weighbridge_variance_pct_07, assess_offline_sync_age_hours_08, assess_weight_capture_pct_09, assess_evidence_attachment_pct_10, assess_coolant_remaining_pct_11, assess_open_box_age_days_12, assess_racking_inspection_age_days_13, assess_robot_cycle_time_seconds_14, assess_on_call_ack_minutes_15, assess_mobile_app_crash_pct_16, assess_customer_contact_valid_pct_17, assess_quality_hold_pct_18, assess_order_cancellation_pct_19, assess_port_dwell_days_20, assess_labor_cost_per_unit_21, assess_supplier_ethics_report_age_days_22, assess_supplier_patch_age_days_23, assess_supplier_recovery_lead_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

