"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_model_monitoring_pct_01(record):
    """Evaluate supplier model monitoring for control WP-0240-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-01", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-01", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-01", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-01", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier model monitoring falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_feature_flag_age_days_02(record):
    """Evaluate supplier feature flag age for control WP-0240-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-02", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-02", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-02", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-02", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier feature flag age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_access_token_age_hours_03(record):
    """Evaluate supplier access-token age for control WP-0240-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_token_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-03", "metric": "supplier_access_token_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-03", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-03", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-03", "metric": "supplier_access_token_age_hours", "label": "supplier access-token age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access-token age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_subject_access_age_days_04(record):
    """Evaluate supplier subject-access request age for control WP-0240-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subject_access_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-04", "metric": "supplier_subject_access_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-04", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-04", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-04", "metric": "supplier_subject_access_age_days", "label": "supplier subject-access request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier subject-access request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_control_exception_count_05(record):
    """Evaluate supplier control exceptions for control WP-0240-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-05", "metric": "supplier_control_exception_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-05", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-05", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-05", "metric": "supplier_control_exception_count", "label": "supplier control exceptions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier control exceptions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_payment_term_variance_days_06(record):
    """Evaluate supplier payment-term variance for control WP-0240-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_term_variance_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-06", "metric": "supplier_payment_term_variance_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-06", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-06", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-06", "metric": "supplier_payment_term_variance_days", "label": "supplier payment-term variance",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment-term variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_wip_age_days_07(record):
    """Evaluate supplier WIP age for control WP-0240-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wip_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-07", "metric": "supplier_wip_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-07", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-07", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-07", "metric": "supplier_wip_age_days", "label": "supplier WIP age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier WIP age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_transition_plan_pct_08(record):
    """Evaluate supplier transition plan completeness for control WP-0240-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-08", "metric": "supplier_transition_plan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-08", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-08", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-08", "metric": "supplier_transition_plan_pct", "label": "supplier transition plan completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "supplier transition plan completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_exit_evidence_pct_09(record):
    """Evaluate supplier exit evidence completeness for control WP-0240-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-09", "metric": "supplier_exit_evidence_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-09", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-09", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-09", "metric": "supplier_exit_evidence_pct", "label": "supplier exit evidence completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier exit evidence completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_backlog_orders_10(record):
    """Evaluate order backlog for control WP-0240-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backlog_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-10", "metric": "backlog_orders",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-10", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-10", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-10", "metric": "backlog_orders", "label": "order backlog",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order backlog must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_equipment_downtime_hours_11(record):
    """Evaluate equipment downtime for control WP-0240-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_downtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-11", "metric": "equipment_downtime_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-11", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-11", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-11", "metric": "equipment_downtime_hours", "label": "equipment downtime",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment downtime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_access_review_age_days_12(record):
    """Evaluate access review age for control WP-0240-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-12", "metric": "access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-12", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-12", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-12", "metric": "access_review_age_days", "label": "access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "access review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_humidity_sensor_gap_minutes_13(record):
    """Evaluate humidity data gap for control WP-0240-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-13", "metric": "humidity_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-13", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-13", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-13", "metric": "humidity_sensor_gap_minutes", "label": "humidity data gap",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "humidity data gap falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_dock_appointment_delay_minutes_14(record):
    """Evaluate dock appointment delay for control WP-0240-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_appointment_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-14", "metric": "dock_appointment_delay_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-14", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-14", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-14", "metric": "dock_appointment_delay_minutes", "label": "dock appointment delay",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dock appointment delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_report_freshness_minutes_15(record):
    """Evaluate report freshness for control WP-0240-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_freshness_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-15", "metric": "report_freshness_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-15", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-15", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-15", "metric": "report_freshness_minutes", "label": "report freshness",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "report freshness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_wave_completion_pct_16(record):
    """Evaluate wave completion for control WP-0240-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("wave_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-16", "metric": "wave_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-16", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-16", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-16", "metric": "wave_completion_pct", "label": "wave completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "wave completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_door_forced_open_count_17(record):
    """Evaluate forced doors for control WP-0240-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-17", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-17", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-17", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-17", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "forced doors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_refrigerant_leak_signal_18(record):
    """Evaluate refrigerant leak signal for control WP-0240-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-18", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-18", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-18", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-18", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refrigerant leak signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_counterfeit_signal_score_19(record):
    """Evaluate counterfeit signal score for control WP-0240-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("counterfeit_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-19", "metric": "counterfeit_signal_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-19", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-19", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-19", "metric": "counterfeit_signal_score", "label": "counterfeit signal score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "counterfeit signal score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_confined_space_permit_pct_20(record):
    """Evaluate confined-space permit compliance for control WP-0240-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("confined_space_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-20", "metric": "confined_space_permit_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-20", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-20", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-20", "metric": "confined_space_permit_pct", "label": "confined-space permit compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "confined-space permit compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_sensor_fault_count_21(record):
    """Evaluate sensor faults for control WP-0240-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_fault_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-21", "metric": "sensor_fault_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-21", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-21", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-21", "metric": "sensor_fault_count", "label": "sensor faults",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "sensor faults falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_deployment_failure_pct_22(record):
    """Evaluate deployment failure rate for control WP-0240-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deployment_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-22", "metric": "deployment_failure_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-22", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-22", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-22", "metric": "deployment_failure_pct", "label": "deployment failure rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "deployment failure rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_deletion_request_age_days_23(record):
    """Evaluate deletion request age for control WP-0240-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deletion_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-23", "metric": "deletion_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-23", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-23", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-23", "metric": "deletion_request_age_days", "label": "deletion request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "deletion request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_country_of_origin_gap_count_24(record):
    """Evaluate country-of-origin gaps for control WP-0240-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_of_origin_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0240-24", "metric": "country_of_origin_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0240-24", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0240-24", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0240-24", "metric": "country_of_origin_gap_count", "label": "country-of-origin gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "country-of-origin gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_model_monitoring_pct_01, assess_supplier_feature_flag_age_days_02, assess_supplier_access_token_age_hours_03, assess_supplier_subject_access_age_days_04, assess_supplier_control_exception_count_05, assess_supplier_payment_term_variance_days_06, assess_supplier_wip_age_days_07, assess_supplier_transition_plan_pct_08, assess_supplier_exit_evidence_pct_09, assess_backlog_orders_10, assess_equipment_downtime_hours_11, assess_access_review_age_days_12, assess_humidity_sensor_gap_minutes_13, assess_dock_appointment_delay_minutes_14, assess_report_freshness_minutes_15, assess_wave_completion_pct_16, assess_door_forced_open_count_17, assess_refrigerant_leak_signal_18, assess_counterfeit_signal_score_19, assess_confined_space_permit_pct_20, assess_sensor_fault_count_21, assess_deployment_failure_pct_22, assess_deletion_request_age_days_23, assess_country_of_origin_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

