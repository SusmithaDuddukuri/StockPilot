"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_archive_completion_pct_01(record):
    """Evaluate supplier archive completion for control WP-0316-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_archive_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-01", "metric": "supplier_archive_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-01", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-01", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-01", "metric": "supplier_archive_completion_pct", "label": "supplier archive completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier archive completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_humidity_pct_02(record):
    """Evaluate storage humidity for control WP-0316-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-02", "metric": "humidity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-02", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-02", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-02", "metric": "humidity_pct", "label": "storage humidity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage humidity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_fire_exit_clearance_cm_03(record):
    """Evaluate fire exit clearance for control WP-0316-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_exit_clearance_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-03", "metric": "fire_exit_clearance_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-03", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-03", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-03", "metric": "fire_exit_clearance_cm", "label": "fire exit clearance",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fire exit clearance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_slotting_score_04(record):
    """Evaluate slotting score for control WP-0316-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-04", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-04", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-04", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-04", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "slotting score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_mean_time_to_repair_hours_05(record):
    """Evaluate mean time to repair for control WP-0316-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-05", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-05", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-05", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-05", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "mean time to repair falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_risk_score_06(record):
    """Evaluate supplier risk for control WP-0316-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-06", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-06", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-06", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-06", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_database_lock_wait_ms_07(record):
    """Evaluate database lock wait for control WP-0316-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_lock_wait_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-07", "metric": "database_lock_wait_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-07", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-07", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-07", "metric": "database_lock_wait_ms", "label": "database lock wait",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "database lock wait must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_min_order_qty_08(record):
    """Evaluate minimum order quantity for control WP-0316-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("min_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-08", "metric": "min_order_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-08", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-08", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-08", "metric": "min_order_qty", "label": "minimum order quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "minimum order quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_rest_period_hours_09(record):
    """Evaluate rest period for control WP-0316-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rest_period_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-09", "metric": "rest_period_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-09", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-09", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-09", "metric": "rest_period_hours", "label": "rest period",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "rest period falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_recycle_pickup_age_days_10(record):
    """Evaluate recycling pickup age for control WP-0316-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycle_pickup_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-10", "metric": "recycle_pickup_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-10", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-10", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-10", "metric": "recycle_pickup_age_days", "label": "recycling pickup age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recycling pickup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_secure_pack_compliance_pct_11(record):
    """Evaluate secure packaging compliance for control WP-0316-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secure_pack_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-11", "metric": "secure_pack_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-11", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-11", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-11", "metric": "secure_pack_compliance_pct", "label": "secure packaging compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "secure packaging compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_ventilation_check_age_days_12(record):
    """Evaluate ventilation check age for control WP-0316-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ventilation_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-12", "metric": "ventilation_check_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-12", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-12", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-12", "metric": "ventilation_check_age_days", "label": "ventilation check age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "ventilation check age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_equipment_certification_age_days_13(record):
    """Evaluate equipment certification age for control WP-0316-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_certification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-13", "metric": "equipment_certification_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-13", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-13", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-13", "metric": "equipment_certification_age_days", "label": "equipment certification age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "equipment certification age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_disaster_recovery_test_age_days_14(record):
    """Evaluate disaster recovery test age for control WP-0316-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disaster_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-14", "metric": "disaster_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-14", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-14", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-14", "metric": "disaster_recovery_test_age_days", "label": "disaster recovery test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "disaster recovery test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_pipeline_failure_count_15(record):
    """Evaluate pipeline failures for control WP-0316-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pipeline_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-15", "metric": "pipeline_failure_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-15", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-15", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-15", "metric": "pipeline_failure_count", "label": "pipeline failures",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pipeline failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_packaging_master_gap_count_16(record):
    """Evaluate packaging master gaps for control WP-0316-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-16", "metric": "packaging_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-16", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-16", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-16", "metric": "packaging_master_gap_count", "label": "packaging master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "packaging master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_substitute_coverage_pct_17(record):
    """Evaluate substitute coverage for control WP-0316-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("substitute_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-17", "metric": "substitute_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-17", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-17", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-17", "metric": "substitute_coverage_pct", "label": "substitute coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "substitute coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_dispatch_cutoff_miss_count_18(record):
    """Evaluate dispatch cutoff misses for control WP-0316-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispatch_cutoff_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-18", "metric": "dispatch_cutoff_miss_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-18", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-18", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-18", "metric": "dispatch_cutoff_miss_count", "label": "dispatch cutoff misses",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dispatch cutoff misses must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_claim_evidence_completeness_pct_19(record):
    """Evaluate claim evidence completeness for control WP-0316-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_evidence_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-19", "metric": "claim_evidence_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-19", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-19", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-19", "metric": "claim_evidence_completeness_pct", "label": "claim evidence completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "claim evidence completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_telematics_gap_minutes_20(record):
    """Evaluate telematics gap for control WP-0316-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-20", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-20", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-20", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-20", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "telematics gap exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_approval_queue_age_hours_21(record):
    """Evaluate approval queue age for control WP-0316-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-21", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-21", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-21", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-21", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "approval queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_subtier_visibility_pct_22(record):
    """Evaluate supplier sub-tier visibility for control WP-0316-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-22", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-22", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-22", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-22", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sub-tier visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_packaging_validation_age_days_23(record):
    """Evaluate supplier packaging validation age for control WP-0316-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-23", "metric": "supplier_packaging_validation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-23", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-23", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-23", "metric": "supplier_packaging_validation_age_days", "label": "supplier packaging validation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging validation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_export_control_gap_count_24(record):
    """Evaluate supplier export-control gaps for control WP-0316-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0316-24", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0316-24", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0316-24", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0316-24", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier export-control gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_archive_completion_pct_01, assess_humidity_pct_02, assess_fire_exit_clearance_cm_03, assess_slotting_score_04, assess_mean_time_to_repair_hours_05, assess_supplier_risk_score_06, assess_database_lock_wait_ms_07, assess_min_order_qty_08, assess_rest_period_hours_09, assess_recycle_pickup_age_days_10, assess_secure_pack_compliance_pct_11, assess_ventilation_check_age_days_12, assess_equipment_certification_age_days_13, assess_disaster_recovery_test_age_days_14, assess_pipeline_failure_count_15, assess_packaging_master_gap_count_16, assess_substitute_coverage_pct_17, assess_dispatch_cutoff_miss_count_18, assess_claim_evidence_completeness_pct_19, assess_telematics_gap_minutes_20, assess_approval_queue_age_hours_21, assess_supplier_subtier_visibility_pct_22, assess_supplier_packaging_validation_age_days_23, assess_supplier_export_control_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

