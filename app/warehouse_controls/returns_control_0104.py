"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_sds_accuracy_pct_01(record):
    """Evaluate supplier SDS accuracy for control WP-0104-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-01", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-01", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-01", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-01", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier SDS accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_cargo_security_score_02(record):
    """Evaluate supplier cargo security for control WP-0104-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-02", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-02", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-02", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-02", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cargo security must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_work_instruction_age_days_03(record):
    """Evaluate supplier work-instruction age for control WP-0104-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_instruction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-03", "metric": "supplier_work_instruction_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-03", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-03", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-03", "metric": "supplier_work_instruction_age_days", "label": "supplier work-instruction age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier work-instruction age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_conflict_mineral_pct_04(record):
    """Evaluate supplier conflict-mineral reporting for control WP-0104-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_mineral_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-04", "metric": "supplier_conflict_mineral_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-04", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-04", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-04", "metric": "supplier_conflict_mineral_pct", "label": "supplier conflict-mineral reporting",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier conflict-mineral reporting exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_sanctions_update_age_hours_05(record):
    """Evaluate supplier sanctions update age for control WP-0104-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_update_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-05", "metric": "supplier_sanctions_update_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-05", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-05", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-05", "metric": "supplier_sanctions_update_age_hours", "label": "supplier sanctions update age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "supplier sanctions update age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_backup_power_pct_06(record):
    """Evaluate supplier backup power coverage for control WP-0104-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_power_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-06", "metric": "supplier_backup_power_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-06", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-06", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-06", "metric": "supplier_backup_power_pct", "label": "supplier backup power coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier backup power coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_model_monitoring_pct_07(record):
    """Evaluate supplier model monitoring for control WP-0104-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-07", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-07", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-07", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-07", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model monitoring must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_feature_flag_age_days_08(record):
    """Evaluate supplier feature flag age for control WP-0104-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-08", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-08", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-08", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-08", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier feature flag age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_access_token_age_hours_09(record):
    """Evaluate supplier access-token age for control WP-0104-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_token_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-09", "metric": "supplier_access_token_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-09", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-09", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-09", "metric": "supplier_access_token_age_hours", "label": "supplier access-token age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier access-token age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_subject_access_age_days_10(record):
    """Evaluate supplier subject-access request age for control WP-0104-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subject_access_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-10", "metric": "supplier_subject_access_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-10", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-10", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-10", "metric": "supplier_subject_access_age_days", "label": "supplier subject-access request age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier subject-access request age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_control_exception_count_11(record):
    """Evaluate supplier control exceptions for control WP-0104-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-11", "metric": "supplier_control_exception_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-11", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-11", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-11", "metric": "supplier_control_exception_count", "label": "supplier control exceptions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control exceptions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_payment_term_variance_days_12(record):
    """Evaluate supplier payment-term variance for control WP-0104-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_term_variance_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-12", "metric": "supplier_payment_term_variance_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-12", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-12", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-12", "metric": "supplier_payment_term_variance_days", "label": "supplier payment-term variance",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier payment-term variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_wip_age_days_13(record):
    """Evaluate supplier WIP age for control WP-0104-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wip_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-13", "metric": "supplier_wip_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-13", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-13", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-13", "metric": "supplier_wip_age_days", "label": "supplier WIP age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier WIP age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_transition_plan_pct_14(record):
    """Evaluate supplier transition plan completeness for control WP-0104-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-14", "metric": "supplier_transition_plan_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-14", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-14", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-14", "metric": "supplier_transition_plan_pct", "label": "supplier transition plan completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transition plan completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_exit_evidence_pct_15(record):
    """Evaluate supplier exit evidence completeness for control WP-0104-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-15", "metric": "supplier_exit_evidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-15", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-15", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-15", "metric": "supplier_exit_evidence_pct", "label": "supplier exit evidence completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit evidence completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_backlog_orders_16(record):
    """Evaluate order backlog for control WP-0104-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backlog_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-16", "metric": "backlog_orders",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-16", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-16", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-16", "metric": "backlog_orders", "label": "order backlog",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "order backlog exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_equipment_downtime_hours_17(record):
    """Evaluate equipment downtime for control WP-0104-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_downtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-17", "metric": "equipment_downtime_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-17", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-17", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-17", "metric": "equipment_downtime_hours", "label": "equipment downtime",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "equipment downtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_access_review_age_days_18(record):
    """Evaluate access review age for control WP-0104-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-18", "metric": "access_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-18", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-18", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-18", "metric": "access_review_age_days", "label": "access review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_humidity_sensor_gap_minutes_19(record):
    """Evaluate humidity data gap for control WP-0104-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-19", "metric": "humidity_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-19", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-19", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-19", "metric": "humidity_sensor_gap_minutes", "label": "humidity data gap",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "humidity data gap must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_dock_appointment_delay_minutes_20(record):
    """Evaluate dock appointment delay for control WP-0104-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_appointment_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-20", "metric": "dock_appointment_delay_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-20", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-20", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-20", "metric": "dock_appointment_delay_minutes", "label": "dock appointment delay",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "dock appointment delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_report_freshness_minutes_21(record):
    """Evaluate report freshness for control WP-0104-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_freshness_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-21", "metric": "report_freshness_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-21", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-21", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-21", "metric": "report_freshness_minutes", "label": "report freshness",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "report freshness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_wave_completion_pct_22(record):
    """Evaluate wave completion for control WP-0104-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("wave_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-22", "metric": "wave_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-22", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-22", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-22", "metric": "wave_completion_pct", "label": "wave completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "wave completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_door_forced_open_count_23(record):
    """Evaluate forced doors for control WP-0104-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-23", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-23", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-23", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-23", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forced doors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_refrigerant_leak_signal_24(record):
    """Evaluate refrigerant leak signal for control WP-0104-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0104-24", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0104-24", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0104-24", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0104-24", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "refrigerant leak signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_sds_accuracy_pct_01, assess_supplier_cargo_security_score_02, assess_supplier_work_instruction_age_days_03, assess_supplier_conflict_mineral_pct_04, assess_supplier_sanctions_update_age_hours_05, assess_supplier_backup_power_pct_06, assess_supplier_model_monitoring_pct_07, assess_supplier_feature_flag_age_days_08, assess_supplier_access_token_age_hours_09, assess_supplier_subject_access_age_days_10, assess_supplier_control_exception_count_11, assess_supplier_payment_term_variance_days_12, assess_supplier_wip_age_days_13, assess_supplier_transition_plan_pct_14, assess_supplier_exit_evidence_pct_15, assess_backlog_orders_16, assess_equipment_downtime_hours_17, assess_access_review_age_days_18, assess_humidity_sensor_gap_minutes_19, assess_dock_appointment_delay_minutes_20, assess_report_freshness_minutes_21, assess_wave_completion_pct_22, assess_door_forced_open_count_23, assess_refrigerant_leak_signal_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

