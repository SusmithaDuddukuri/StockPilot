"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_machine_uptime_pct_01(record):
    """Evaluate supplier machine uptime for control WP-0503-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_machine_uptime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-01", "metric": "supplier_machine_uptime_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-01", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-01", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-01", "metric": "supplier_machine_uptime_pct", "label": "supplier machine uptime",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier machine uptime must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_metric_definition_gap_count_02(record):
    """Evaluate supplier metric-definition gaps for control WP-0503-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_metric_definition_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-02", "metric": "supplier_metric_definition_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-02", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-02", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-02", "metric": "supplier_metric_definition_gap_count", "label": "supplier metric-definition gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier metric-definition gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_archive_completion_pct_03(record):
    """Evaluate supplier archive completion for control WP-0503-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_archive_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-03", "metric": "supplier_archive_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-03", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-03", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-03", "metric": "supplier_archive_completion_pct", "label": "supplier archive completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier archive completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_humidity_pct_04(record):
    """Evaluate storage humidity for control WP-0503-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-04", "metric": "humidity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-04", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-04", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-04", "metric": "humidity_pct", "label": "storage humidity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "storage humidity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_fire_exit_clearance_cm_05(record):
    """Evaluate fire exit clearance for control WP-0503-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_exit_clearance_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-05", "metric": "fire_exit_clearance_cm",
            "status": "insufficient_data",
            "severity": "critical", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-05", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-05", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-05", "metric": "fire_exit_clearance_cm", "label": "fire exit clearance",
        "status": "breach", "severity": "critical", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fire exit clearance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_slotting_score_06(record):
    """Evaluate slotting score for control WP-0503-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-06", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-06", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-06", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-06", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slotting score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_mean_time_to_repair_hours_07(record):
    """Evaluate mean time to repair for control WP-0503-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-07", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-07", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-07", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-07", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "mean time to repair exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_risk_score_08(record):
    """Evaluate supplier risk for control WP-0503-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-08", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-08", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-08", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-08", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_database_lock_wait_ms_09(record):
    """Evaluate database lock wait for control WP-0503-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_lock_wait_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-09", "metric": "database_lock_wait_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-09", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-09", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-09", "metric": "database_lock_wait_ms", "label": "database lock wait",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "database lock wait must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_min_order_qty_10(record):
    """Evaluate minimum order quantity for control WP-0503-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("min_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-10", "metric": "min_order_qty",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-10", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-10", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-10", "metric": "min_order_qty", "label": "minimum order quantity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum order quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_rest_period_hours_11(record):
    """Evaluate rest period for control WP-0503-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rest_period_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-11", "metric": "rest_period_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-11", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-11", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-11", "metric": "rest_period_hours", "label": "rest period",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "rest period exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_recycle_pickup_age_days_12(record):
    """Evaluate recycling pickup age for control WP-0503-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycle_pickup_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-12", "metric": "recycle_pickup_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-12", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-12", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-12", "metric": "recycle_pickup_age_days", "label": "recycling pickup age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "recycling pickup age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_secure_pack_compliance_pct_13(record):
    """Evaluate secure packaging compliance for control WP-0503-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secure_pack_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-13", "metric": "secure_pack_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-13", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-13", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-13", "metric": "secure_pack_compliance_pct", "label": "secure packaging compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "secure packaging compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_ventilation_check_age_days_14(record):
    """Evaluate ventilation check age for control WP-0503-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ventilation_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-14", "metric": "ventilation_check_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-14", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-14", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-14", "metric": "ventilation_check_age_days", "label": "ventilation check age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "ventilation check age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_equipment_certification_age_days_15(record):
    """Evaluate equipment certification age for control WP-0503-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_certification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-15", "metric": "equipment_certification_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-15", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-15", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-15", "metric": "equipment_certification_age_days", "label": "equipment certification age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "equipment certification age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_disaster_recovery_test_age_days_16(record):
    """Evaluate disaster recovery test age for control WP-0503-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disaster_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-16", "metric": "disaster_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-16", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-16", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-16", "metric": "disaster_recovery_test_age_days", "label": "disaster recovery test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "disaster recovery test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_pipeline_failure_count_17(record):
    """Evaluate pipeline failures for control WP-0503-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pipeline_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-17", "metric": "pipeline_failure_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-17", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-17", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-17", "metric": "pipeline_failure_count", "label": "pipeline failures",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pipeline failures must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_packaging_master_gap_count_18(record):
    """Evaluate packaging master gaps for control WP-0503-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-18", "metric": "packaging_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-18", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-18", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-18", "metric": "packaging_master_gap_count", "label": "packaging master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "packaging master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_substitute_coverage_pct_19(record):
    """Evaluate substitute coverage for control WP-0503-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("substitute_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-19", "metric": "substitute_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-19", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-19", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-19", "metric": "substitute_coverage_pct", "label": "substitute coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "substitute coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_dispatch_cutoff_miss_count_20(record):
    """Evaluate dispatch cutoff misses for control WP-0503-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispatch_cutoff_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-20", "metric": "dispatch_cutoff_miss_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-20", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-20", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-20", "metric": "dispatch_cutoff_miss_count", "label": "dispatch cutoff misses",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "dispatch cutoff misses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_claim_evidence_completeness_pct_21(record):
    """Evaluate claim evidence completeness for control WP-0503-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_evidence_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-21", "metric": "claim_evidence_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-21", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-21", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-21", "metric": "claim_evidence_completeness_pct", "label": "claim evidence completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "claim evidence completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_telematics_gap_minutes_22(record):
    """Evaluate telematics gap for control WP-0503-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-22", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-22", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-22", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-22", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "telematics gap must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_approval_queue_age_hours_23(record):
    """Evaluate approval queue age for control WP-0503-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-23", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-23", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-23", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-23", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "approval queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_subtier_visibility_pct_24(record):
    """Evaluate supplier sub-tier visibility for control WP-0503-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0503-24", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0503-24", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0503-24", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0503-24", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier sub-tier visibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_machine_uptime_pct_01, assess_supplier_metric_definition_gap_count_02, assess_supplier_archive_completion_pct_03, assess_humidity_pct_04, assess_fire_exit_clearance_cm_05, assess_slotting_score_06, assess_mean_time_to_repair_hours_07, assess_supplier_risk_score_08, assess_database_lock_wait_ms_09, assess_min_order_qty_10, assess_rest_period_hours_11, assess_recycle_pickup_age_days_12, assess_secure_pack_compliance_pct_13, assess_ventilation_check_age_days_14, assess_equipment_certification_age_days_15, assess_disaster_recovery_test_age_days_16, assess_pipeline_failure_count_17, assess_packaging_master_gap_count_18, assess_substitute_coverage_pct_19, assess_dispatch_cutoff_miss_count_20, assess_claim_evidence_completeness_pct_21, assess_telematics_gap_minutes_22, assess_approval_queue_age_hours_23, assess_supplier_subtier_visibility_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

