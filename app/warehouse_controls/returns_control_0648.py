"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_coolant_remaining_pct_01(record):
    """Evaluate coolant remaining for control WP-0648-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-01", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-01", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-01", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-01", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "coolant remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_open_box_age_days_02(record):
    """Evaluate open-box age for control WP-0648-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-02", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-02", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-02", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-02", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-box age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_racking_inspection_age_days_03(record):
    """Evaluate racking inspection age for control WP-0648-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("racking_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-03", "metric": "racking_inspection_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-03", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-03", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-03", "metric": "racking_inspection_age_days", "label": "racking inspection age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "racking inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_robot_cycle_time_seconds_04(record):
    """Evaluate robot cycle time for control WP-0648-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_cycle_time_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-04", "metric": "robot_cycle_time_seconds",
            "status": "insufficient_data",
            "severity": "critical", "unit": "seconds",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-04", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-04", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-04", "metric": "robot_cycle_time_seconds", "label": "robot cycle time",
        "status": "breach", "severity": "critical", "unit": "seconds",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "robot cycle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_on_call_ack_minutes_05(record):
    """Evaluate on-call acknowledgement for control WP-0648-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("on_call_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-05", "metric": "on_call_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-05", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-05", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-05", "metric": "on_call_ack_minutes", "label": "on-call acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "on-call acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_mobile_app_crash_pct_06(record):
    """Evaluate mobile app crash rate for control WP-0648-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_app_crash_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-06", "metric": "mobile_app_crash_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-06", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-06", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-06", "metric": "mobile_app_crash_pct", "label": "mobile app crash rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "mobile app crash rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_customer_contact_valid_pct_07(record):
    """Evaluate customer contact validity for control WP-0648-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-07", "metric": "customer_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-07", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-07", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-07", "metric": "customer_contact_valid_pct", "label": "customer contact validity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer contact validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_quality_hold_pct_08(record):
    """Evaluate quality hold share for control WP-0648-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-08", "metric": "quality_hold_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-08", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-08", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-08", "metric": "quality_hold_pct", "label": "quality hold share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "quality hold share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_order_cancellation_pct_09(record):
    """Evaluate order cancellation rate for control WP-0648-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_cancellation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-09", "metric": "order_cancellation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-09", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-09", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-09", "metric": "order_cancellation_pct", "label": "order cancellation rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "order cancellation rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_port_dwell_days_10(record):
    """Evaluate port dwell for control WP-0648-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("port_dwell_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-10", "metric": "port_dwell_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-10", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-10", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-10", "metric": "port_dwell_days", "label": "port dwell",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "port dwell must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_labor_cost_per_unit_11(record):
    """Evaluate labor cost per unit for control WP-0648-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_cost_per_unit")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-11", "metric": "labor_cost_per_unit",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-11", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-11", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-11", "metric": "labor_cost_per_unit", "label": "labor cost per unit",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor cost per unit must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_ethics_report_age_days_12(record):
    """Evaluate supplier ethics report age for control WP-0648-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_report_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-12", "metric": "supplier_ethics_report_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-12", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-12", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-12", "metric": "supplier_ethics_report_age_days", "label": "supplier ethics report age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "supplier ethics report age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_patch_age_days_13(record):
    """Evaluate supplier patch age for control WP-0648-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-13", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-13", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-13", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-13", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier patch age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_recovery_lead_days_14(record):
    """Evaluate supplier recovery lead time for control WP-0648-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-14", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-14", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-14", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-14", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery lead time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_subprocessor_count_15(record):
    """Evaluate supplier sub-processors for control WP-0648-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-15", "metric": "supplier_subprocessor_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "entities",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-15", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-15", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-15", "metric": "supplier_subprocessor_count", "label": "supplier sub-processors",
        "status": "breach", "severity": "high", "unit": "entities",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-processors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_water_continuity_score_16(record):
    """Evaluate supplier water continuity for control WP-0648-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-16", "metric": "supplier_water_continuity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-16", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-16", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-16", "metric": "supplier_water_continuity_score", "label": "supplier water continuity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier water continuity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_climate_plan_age_days_17(record):
    """Evaluate supplier climate-plan age for control WP-0648-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_climate_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-17", "metric": "supplier_climate_plan_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-17", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-17", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-17", "metric": "supplier_climate_plan_age_days", "label": "supplier climate-plan age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier climate-plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_contact_tree_age_days_18(record):
    """Evaluate supplier contact-tree age for control WP-0648-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_tree_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-18", "metric": "supplier_contact_tree_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-18", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-18", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-18", "metric": "supplier_contact_tree_age_days", "label": "supplier contact-tree age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier contact-tree age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_customer_escape_count_19(record):
    """Evaluate supplier customer escapes for control WP-0648-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-19", "metric": "supplier_customer_escape_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-19", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-19", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-19", "metric": "supplier_customer_escape_count", "label": "supplier customer escapes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer escapes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_union_rights_policy_pct_20(record):
    """Evaluate supplier worker-rights policy for control WP-0648-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_union_rights_policy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-20", "metric": "supplier_union_rights_policy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-20", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-20", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-20", "metric": "supplier_union_rights_policy_pct", "label": "supplier worker-rights policy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier worker-rights policy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_site_closure_signal_21(record):
    """Evaluate supplier site-closure signal for control WP-0648-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_closure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-21", "metric": "supplier_site_closure_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-21", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-21", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-21", "metric": "supplier_site_closure_signal", "label": "supplier site-closure signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier site-closure signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_lead_time_reduction_pct_22(record):
    """Evaluate supplier lead-time reduction for control WP-0648-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-22", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-22", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-22", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-22", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier lead-time reduction must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_feature_store_lag_minutes_23(record):
    """Evaluate supplier feature-store lag for control WP-0648-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-23", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-23", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-23", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-23", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier feature-store lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_latency_p99_ms_24(record):
    """Evaluate supplier p99 latency for control WP-0648-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p99_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0648-24", "metric": "supplier_latency_p99_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0648-24", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0648-24", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0648-24", "metric": "supplier_latency_p99_ms", "label": "supplier p99 latency",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier p99 latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_coolant_remaining_pct_01, assess_open_box_age_days_02, assess_racking_inspection_age_days_03, assess_robot_cycle_time_seconds_04, assess_on_call_ack_minutes_05, assess_mobile_app_crash_pct_06, assess_customer_contact_valid_pct_07, assess_quality_hold_pct_08, assess_order_cancellation_pct_09, assess_port_dwell_days_10, assess_labor_cost_per_unit_11, assess_supplier_ethics_report_age_days_12, assess_supplier_patch_age_days_13, assess_supplier_recovery_lead_days_14, assess_supplier_subprocessor_count_15, assess_supplier_water_continuity_score_16, assess_supplier_climate_plan_age_days_17, assess_supplier_contact_tree_age_days_18, assess_supplier_customer_escape_count_19, assess_supplier_union_rights_policy_pct_20, assess_supplier_site_closure_signal_21, assess_supplier_lead_time_reduction_pct_22, assess_supplier_feature_store_lag_minutes_23, assess_supplier_latency_p99_ms_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

