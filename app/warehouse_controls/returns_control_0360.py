"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_key_person_dependency_pct_01(record):
    """Evaluate supplier key-person dependency for control WP-0360-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_person_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-01", "metric": "supplier_key_person_dependency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-01", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-01", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-01", "metric": "supplier_key_person_dependency_pct", "label": "supplier key-person dependency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier key-person dependency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_material_restriction_gap_count_02(record):
    """Evaluate supplier material restriction gaps for control WP-0360-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_restriction_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-02", "metric": "supplier_material_restriction_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-02", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-02", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-02", "metric": "supplier_material_restriction_gap_count", "label": "supplier material restriction gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier material restriction gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_ownership_review_age_days_03(record):
    """Evaluate supplier ownership review age for control WP-0360-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ownership_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-03", "metric": "supplier_ownership_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-03", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-03", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-03", "metric": "supplier_ownership_review_age_days", "label": "supplier ownership review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ownership review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_tooling_spare_pct_04(record):
    """Evaluate supplier spare tooling coverage for control WP-0360-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-04", "metric": "supplier_tooling_spare_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-04", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-04", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-04", "metric": "supplier_tooling_spare_pct", "label": "supplier spare tooling coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier spare tooling coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_ai_governance_score_05(record):
    """Evaluate supplier AI governance for control WP-0360-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_governance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-05", "metric": "supplier_ai_governance_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-05", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-05", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-05", "metric": "supplier_ai_governance_score", "label": "supplier AI governance",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier AI governance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_ab_test_age_days_06(record):
    """Evaluate supplier A/B test age for control WP-0360-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ab_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-06", "metric": "supplier_ab_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-06", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-06", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-06", "metric": "supplier_ab_test_age_days", "label": "supplier A/B test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier A/B test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_encryption_key_age_days_07(record):
    """Evaluate supplier encryption-key age for control WP-0360-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_key_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-07", "metric": "supplier_encryption_key_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-07", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-07", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-07", "metric": "supplier_encryption_key_age_days", "label": "supplier encryption-key age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier encryption-key age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_consent_withdrawal_age_hours_08(record):
    """Evaluate supplier consent withdrawal age for control WP-0360-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_consent_withdrawal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-08", "metric": "supplier_consent_withdrawal_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-08", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-08", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-08", "metric": "supplier_consent_withdrawal_age_hours", "label": "supplier consent withdrawal age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "supplier consent withdrawal age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_action_overdue_count_09(record):
    """Evaluate supplier overdue actions for control WP-0360-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_overdue_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-09", "metric": "supplier_action_overdue_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-09", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-09", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-09", "metric": "supplier_action_overdue_count", "label": "supplier overdue actions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier overdue actions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_fx_variance_pct_10(record):
    """Evaluate supplier FX variance for control WP-0360-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fx_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-10", "metric": "supplier_fx_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-10", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-10", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-10", "metric": "supplier_fx_variance_pct", "label": "supplier FX variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier FX variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_work_in_process_units_11(record):
    """Evaluate supplier WIP units for control WP-0360-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_in_process_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-11", "metric": "supplier_work_in_process_units",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-11", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-11", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-11", "metric": "supplier_work_in_process_units", "label": "supplier WIP units",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier WIP units must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_exit_criteria_gap_count_12(record):
    """Evaluate supplier exit-criteria gaps for control WP-0360-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_criteria_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-12", "metric": "supplier_exit_criteria_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-12", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-12", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-12", "metric": "supplier_exit_criteria_gap_count", "label": "supplier exit-criteria gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier exit-criteria gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_post_exit_billing_count_13(record):
    """Evaluate post-exit billing events for control WP-0360-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_billing_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-13", "metric": "supplier_post_exit_billing_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-13", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-13", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-13", "metric": "supplier_post_exit_billing_count", "label": "post-exit billing events",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "post-exit billing events falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_count_variance_14(record):
    """Evaluate cycle-count variance for control WP-0360-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("count_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-14", "metric": "count_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-14", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-14", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-14", "metric": "count_variance", "label": "cycle-count variance",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cycle-count variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_battery_health_pct_15(record):
    """Evaluate battery health for control WP-0360-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_health_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-15", "metric": "battery_health_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-15", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-15", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-15", "metric": "battery_health_pct", "label": "battery health",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "battery health must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_security_incident_count_16(record):
    """Evaluate security incidents for control WP-0360-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-16", "metric": "security_incident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-16", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-16", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-16", "metric": "security_incident_count", "label": "security incidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "security incidents exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_temperature_sensor_gap_minutes_17(record):
    """Evaluate sensor data gap for control WP-0360-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-17", "metric": "temperature_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-17", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-17", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-17", "metric": "temperature_sensor_gap_minutes", "label": "sensor data gap",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "sensor data gap falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_staging_age_minutes_18(record):
    """Evaluate staging age for control WP-0360-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("staging_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-18", "metric": "staging_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-18", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-18", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-18", "metric": "staging_age_minutes", "label": "staging age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "staging age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_event_lag_seconds_19(record):
    """Evaluate event processing lag for control WP-0360-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("event_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-19", "metric": "event_lag_seconds",
            "status": "insufficient_data",
            "severity": "high", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-19", "metric": "event_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-19", "metric": "event_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-19", "metric": "event_lag_seconds", "label": "event processing lag",
        "status": "breach", "severity": "high", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "event processing lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_pallet_pick_ratio_pct_20(record):
    """Evaluate pallet pick ratio for control WP-0360-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-20", "metric": "pallet_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-20", "metric": "pallet_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-20", "metric": "pallet_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-20", "metric": "pallet_pick_ratio_pct", "label": "pallet pick ratio",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "pallet pick ratio exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_perimeter_alarm_count_21(record):
    """Evaluate perimeter alarms for control WP-0360-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("perimeter_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-21", "metric": "perimeter_alarm_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-21", "metric": "perimeter_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-21", "metric": "perimeter_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-21", "metric": "perimeter_alarm_count", "label": "perimeter alarms",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "perimeter alarms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_renewable_energy_pct_22(record):
    """Evaluate renewable energy share for control WP-0360-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("renewable_energy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-22", "metric": "renewable_energy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-22", "metric": "renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-22", "metric": "renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-22", "metric": "renewable_energy_pct", "label": "renewable energy share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "renewable energy share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_high_value_claim_age_days_23(record):
    """Evaluate high-value claim age for control WP-0360-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-23", "metric": "high_value_claim_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-23", "metric": "high_value_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-23", "metric": "high_value_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-23", "metric": "high_value_claim_age_days", "label": "high-value claim age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "high-value claim age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_lockout_tagout_compliance_pct_24(record):
    """Evaluate lockout/tagout compliance for control WP-0360-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lockout_tagout_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0360-24", "metric": "lockout_tagout_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0360-24", "metric": "lockout_tagout_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0360-24", "metric": "lockout_tagout_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0360-24", "metric": "lockout_tagout_compliance_pct", "label": "lockout/tagout compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "lockout/tagout compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_key_person_dependency_pct_01, assess_supplier_material_restriction_gap_count_02, assess_supplier_ownership_review_age_days_03, assess_supplier_tooling_spare_pct_04, assess_supplier_ai_governance_score_05, assess_supplier_ab_test_age_days_06, assess_supplier_encryption_key_age_days_07, assess_supplier_consent_withdrawal_age_hours_08, assess_supplier_action_overdue_count_09, assess_supplier_fx_variance_pct_10, assess_supplier_work_in_process_units_11, assess_supplier_exit_criteria_gap_count_12, assess_supplier_post_exit_billing_count_13, assess_count_variance_14, assess_battery_health_pct_15, assess_security_incident_count_16, assess_temperature_sensor_gap_minutes_17, assess_staging_age_minutes_18, assess_event_lag_seconds_19, assess_pallet_pick_ratio_pct_20, assess_perimeter_alarm_count_21, assess_renewable_energy_pct_22, assess_high_value_claim_age_days_23, assess_lockout_tagout_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

