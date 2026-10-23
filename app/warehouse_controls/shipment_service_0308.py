"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_subject_access_age_days_01(record):
    """Evaluate supplier subject-access request age for control WP-0308-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subject_access_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-01", "metric": "supplier_subject_access_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-01", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-01", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-01", "metric": "supplier_subject_access_age_days", "label": "supplier subject-access request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier subject-access request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_control_exception_count_02(record):
    """Evaluate supplier control exceptions for control WP-0308-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-02", "metric": "supplier_control_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-02", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-02", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-02", "metric": "supplier_control_exception_count", "label": "supplier control exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier control exceptions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_payment_term_variance_days_03(record):
    """Evaluate supplier payment-term variance for control WP-0308-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_term_variance_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-03", "metric": "supplier_payment_term_variance_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-03", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-03", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-03", "metric": "supplier_payment_term_variance_days", "label": "supplier payment-term variance",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment-term variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_wip_age_days_04(record):
    """Evaluate supplier WIP age for control WP-0308-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wip_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-04", "metric": "supplier_wip_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-04", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-04", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-04", "metric": "supplier_wip_age_days", "label": "supplier WIP age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier WIP age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_transition_plan_pct_05(record):
    """Evaluate supplier transition plan completeness for control WP-0308-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-05", "metric": "supplier_transition_plan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-05", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-05", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-05", "metric": "supplier_transition_plan_pct", "label": "supplier transition plan completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier transition plan completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_exit_evidence_pct_06(record):
    """Evaluate supplier exit evidence completeness for control WP-0308-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-06", "metric": "supplier_exit_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-06", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-06", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-06", "metric": "supplier_exit_evidence_pct", "label": "supplier exit evidence completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exit evidence completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_backlog_orders_07(record):
    """Evaluate order backlog for control WP-0308-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backlog_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-07", "metric": "backlog_orders",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-07", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-07", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-07", "metric": "backlog_orders", "label": "order backlog",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order backlog must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_equipment_downtime_hours_08(record):
    """Evaluate equipment downtime for control WP-0308-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_downtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-08", "metric": "equipment_downtime_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-08", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-08", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-08", "metric": "equipment_downtime_hours", "label": "equipment downtime",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "equipment downtime exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_access_review_age_days_09(record):
    """Evaluate access review age for control WP-0308-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-09", "metric": "access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-09", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-09", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-09", "metric": "access_review_age_days", "label": "access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_humidity_sensor_gap_minutes_10(record):
    """Evaluate humidity data gap for control WP-0308-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-10", "metric": "humidity_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-10", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-10", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-10", "metric": "humidity_sensor_gap_minutes", "label": "humidity data gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "humidity data gap must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_dock_appointment_delay_minutes_11(record):
    """Evaluate dock appointment delay for control WP-0308-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_appointment_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-11", "metric": "dock_appointment_delay_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-11", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-11", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-11", "metric": "dock_appointment_delay_minutes", "label": "dock appointment delay",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock appointment delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_report_freshness_minutes_12(record):
    """Evaluate report freshness for control WP-0308-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_freshness_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-12", "metric": "report_freshness_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-12", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-12", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-12", "metric": "report_freshness_minutes", "label": "report freshness",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "report freshness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_wave_completion_pct_13(record):
    """Evaluate wave completion for control WP-0308-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("wave_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-13", "metric": "wave_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-13", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-13", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-13", "metric": "wave_completion_pct", "label": "wave completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "wave completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_door_forced_open_count_14(record):
    """Evaluate forced doors for control WP-0308-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-14", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-14", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-14", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-14", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forced doors must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_refrigerant_leak_signal_15(record):
    """Evaluate refrigerant leak signal for control WP-0308-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-15", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-15", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-15", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-15", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "refrigerant leak signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_counterfeit_signal_score_16(record):
    """Evaluate counterfeit signal score for control WP-0308-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("counterfeit_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-16", "metric": "counterfeit_signal_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-16", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-16", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-16", "metric": "counterfeit_signal_score", "label": "counterfeit signal score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "counterfeit signal score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_confined_space_permit_pct_17(record):
    """Evaluate confined-space permit compliance for control WP-0308-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("confined_space_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-17", "metric": "confined_space_permit_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-17", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-17", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-17", "metric": "confined_space_permit_pct", "label": "confined-space permit compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "confined-space permit compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_sensor_fault_count_18(record):
    """Evaluate sensor faults for control WP-0308-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_fault_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-18", "metric": "sensor_fault_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-18", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-18", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-18", "metric": "sensor_fault_count", "label": "sensor faults",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sensor faults must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_deployment_failure_pct_19(record):
    """Evaluate deployment failure rate for control WP-0308-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deployment_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-19", "metric": "deployment_failure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-19", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-19", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-19", "metric": "deployment_failure_pct", "label": "deployment failure rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "deployment failure rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_deletion_request_age_days_20(record):
    """Evaluate deletion request age for control WP-0308-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deletion_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-20", "metric": "deletion_request_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-20", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-20", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-20", "metric": "deletion_request_age_days", "label": "deletion request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "deletion request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_country_of_origin_gap_count_21(record):
    """Evaluate country-of-origin gaps for control WP-0308-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_of_origin_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-21", "metric": "country_of_origin_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-21", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-21", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-21", "metric": "country_of_origin_gap_count", "label": "country-of-origin gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "country-of-origin gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_asn_accuracy_pct_22(record):
    """Evaluate supplier ASN accuracy for control WP-0308-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-22", "metric": "supplier_asn_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-22", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-22", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-22", "metric": "supplier_asn_accuracy_pct", "label": "supplier ASN accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ASN accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_delivery_window_success_pct_23(record):
    """Evaluate delivery-window success for control WP-0308-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_window_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-23", "metric": "delivery_window_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-23", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-23", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-23", "metric": "delivery_window_success_pct", "label": "delivery-window success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "delivery-window success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_detention_charge_hours_24(record):
    """Evaluate detention charge hours for control WP-0308-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("detention_charge_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0308-24", "metric": "detention_charge_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0308-24", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0308-24", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0308-24", "metric": "detention_charge_hours", "label": "detention charge hours",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "detention charge hours exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_subject_access_age_days_01, assess_supplier_control_exception_count_02, assess_supplier_payment_term_variance_days_03, assess_supplier_wip_age_days_04, assess_supplier_transition_plan_pct_05, assess_supplier_exit_evidence_pct_06, assess_backlog_orders_07, assess_equipment_downtime_hours_08, assess_access_review_age_days_09, assess_humidity_sensor_gap_minutes_10, assess_dock_appointment_delay_minutes_11, assess_report_freshness_minutes_12, assess_wave_completion_pct_13, assess_door_forced_open_count_14, assess_refrigerant_leak_signal_15, assess_counterfeit_signal_score_16, assess_confined_space_permit_pct_17, assess_sensor_fault_count_18, assess_deployment_failure_pct_19, assess_deletion_request_age_days_20, assess_country_of_origin_gap_count_21, assess_supplier_asn_accuracy_pct_22, assess_delivery_window_success_pct_23, assess_detention_charge_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

