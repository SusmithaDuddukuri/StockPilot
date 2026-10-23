"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_evidence_attachment_pct_01(record):
    """Evaluate evidence attachment completeness for control WP-0393-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evidence_attachment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-01", "metric": "evidence_attachment_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-01", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-01", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-01", "metric": "evidence_attachment_pct", "label": "evidence attachment completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "evidence attachment completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_coolant_remaining_pct_02(record):
    """Evaluate coolant remaining for control WP-0393-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-02", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-02", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-02", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-02", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "coolant remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_open_box_age_days_03(record):
    """Evaluate open-box age for control WP-0393-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-03", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-03", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-03", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-03", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-box age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_racking_inspection_age_days_04(record):
    """Evaluate racking inspection age for control WP-0393-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("racking_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-04", "metric": "racking_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-04", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-04", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-04", "metric": "racking_inspection_age_days", "label": "racking inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "racking inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_robot_cycle_time_seconds_05(record):
    """Evaluate robot cycle time for control WP-0393-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_cycle_time_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-05", "metric": "robot_cycle_time_seconds",
            "status": "insufficient_data",
            "severity": "medium", "unit": "seconds",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-05", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-05", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-05", "metric": "robot_cycle_time_seconds", "label": "robot cycle time",
        "status": "breach", "severity": "medium", "unit": "seconds",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "robot cycle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_on_call_ack_minutes_06(record):
    """Evaluate on-call acknowledgement for control WP-0393-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("on_call_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-06", "metric": "on_call_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-06", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-06", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-06", "metric": "on_call_ack_minutes", "label": "on-call acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "on-call acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_mobile_app_crash_pct_07(record):
    """Evaluate mobile app crash rate for control WP-0393-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_app_crash_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-07", "metric": "mobile_app_crash_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-07", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-07", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-07", "metric": "mobile_app_crash_pct", "label": "mobile app crash rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "mobile app crash rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_customer_contact_valid_pct_08(record):
    """Evaluate customer contact validity for control WP-0393-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-08", "metric": "customer_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-08", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-08", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-08", "metric": "customer_contact_valid_pct", "label": "customer contact validity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer contact validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_quality_hold_pct_09(record):
    """Evaluate quality hold share for control WP-0393-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-09", "metric": "quality_hold_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-09", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-09", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-09", "metric": "quality_hold_pct", "label": "quality hold share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "quality hold share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_order_cancellation_pct_10(record):
    """Evaluate order cancellation rate for control WP-0393-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_cancellation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-10", "metric": "order_cancellation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-10", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-10", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-10", "metric": "order_cancellation_pct", "label": "order cancellation rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "order cancellation rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_port_dwell_days_11(record):
    """Evaluate port dwell for control WP-0393-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("port_dwell_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-11", "metric": "port_dwell_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-11", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-11", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-11", "metric": "port_dwell_days", "label": "port dwell",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "port dwell must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_labor_cost_per_unit_12(record):
    """Evaluate labor cost per unit for control WP-0393-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_cost_per_unit")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-12", "metric": "labor_cost_per_unit",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-12", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-12", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-12", "metric": "labor_cost_per_unit", "label": "labor cost per unit",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor cost per unit must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_ethics_report_age_days_13(record):
    """Evaluate supplier ethics report age for control WP-0393-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_report_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-13", "metric": "supplier_ethics_report_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-13", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-13", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-13", "metric": "supplier_ethics_report_age_days", "label": "supplier ethics report age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier ethics report age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_patch_age_days_14(record):
    """Evaluate supplier patch age for control WP-0393-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-14", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-14", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-14", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-14", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier patch age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_recovery_lead_days_15(record):
    """Evaluate supplier recovery lead time for control WP-0393-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-15", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-15", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-15", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-15", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery lead time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_subprocessor_count_16(record):
    """Evaluate supplier sub-processors for control WP-0393-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-16", "metric": "supplier_subprocessor_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "entities",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-16", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-16", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-16", "metric": "supplier_subprocessor_count", "label": "supplier sub-processors",
        "status": "breach", "severity": "low", "unit": "entities",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-processors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_water_continuity_score_17(record):
    """Evaluate supplier water continuity for control WP-0393-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-17", "metric": "supplier_water_continuity_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-17", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-17", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-17", "metric": "supplier_water_continuity_score", "label": "supplier water continuity",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier water continuity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_climate_plan_age_days_18(record):
    """Evaluate supplier climate-plan age for control WP-0393-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_climate_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-18", "metric": "supplier_climate_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-18", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-18", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-18", "metric": "supplier_climate_plan_age_days", "label": "supplier climate-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "supplier climate-plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_contact_tree_age_days_19(record):
    """Evaluate supplier contact-tree age for control WP-0393-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_tree_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-19", "metric": "supplier_contact_tree_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-19", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-19", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-19", "metric": "supplier_contact_tree_age_days", "label": "supplier contact-tree age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier contact-tree age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_customer_escape_count_20(record):
    """Evaluate supplier customer escapes for control WP-0393-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-20", "metric": "supplier_customer_escape_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-20", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-20", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-20", "metric": "supplier_customer_escape_count", "label": "supplier customer escapes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer escapes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_union_rights_policy_pct_21(record):
    """Evaluate supplier worker-rights policy for control WP-0393-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_union_rights_policy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-21", "metric": "supplier_union_rights_policy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-21", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-21", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-21", "metric": "supplier_union_rights_policy_pct", "label": "supplier worker-rights policy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "supplier worker-rights policy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_site_closure_signal_22(record):
    """Evaluate supplier site-closure signal for control WP-0393-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_closure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-22", "metric": "supplier_site_closure_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-22", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-22", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-22", "metric": "supplier_site_closure_signal", "label": "supplier site-closure signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier site-closure signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_lead_time_reduction_pct_23(record):
    """Evaluate supplier lead-time reduction for control WP-0393-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-23", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-23", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-23", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-23", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier lead-time reduction must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_feature_store_lag_minutes_24(record):
    """Evaluate supplier feature-store lag for control WP-0393-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0393-24", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0393-24", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0393-24", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0393-24", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier feature-store lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_evidence_attachment_pct_01, assess_coolant_remaining_pct_02, assess_open_box_age_days_03, assess_racking_inspection_age_days_04, assess_robot_cycle_time_seconds_05, assess_on_call_ack_minutes_06, assess_mobile_app_crash_pct_07, assess_customer_contact_valid_pct_08, assess_quality_hold_pct_09, assess_order_cancellation_pct_10, assess_port_dwell_days_11, assess_labor_cost_per_unit_12, assess_supplier_ethics_report_age_days_13, assess_supplier_patch_age_days_14, assess_supplier_recovery_lead_days_15, assess_supplier_subprocessor_count_16, assess_supplier_water_continuity_score_17, assess_supplier_climate_plan_age_days_18, assess_supplier_contact_tree_age_days_19, assess_supplier_customer_escape_count_20, assess_supplier_union_rights_policy_pct_21, assess_supplier_site_closure_signal_22, assess_supplier_lead_time_reduction_pct_23, assess_supplier_feature_store_lag_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

