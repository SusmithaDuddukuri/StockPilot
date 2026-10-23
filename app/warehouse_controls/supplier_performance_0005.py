"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_slotting_score_01(record):
    """Evaluate slotting score for control WP-0005-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-01", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-01", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-01", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-01", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "slotting score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_mean_time_to_repair_hours_02(record):
    """Evaluate mean time to repair for control WP-0005-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-02", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-02", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-02", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-02", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "mean time to repair falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_risk_score_03(record):
    """Evaluate supplier risk for control WP-0005-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-03", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-03", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-03", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-03", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_database_lock_wait_ms_04(record):
    """Evaluate database lock wait for control WP-0005-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_lock_wait_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-04", "metric": "database_lock_wait_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-04", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-04", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-04", "metric": "database_lock_wait_ms", "label": "database lock wait",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "database lock wait must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_min_order_qty_05(record):
    """Evaluate minimum order quantity for control WP-0005-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("min_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-05", "metric": "min_order_qty",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-05", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-05", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-05", "metric": "min_order_qty", "label": "minimum order quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "minimum order quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_rest_period_hours_06(record):
    """Evaluate rest period for control WP-0005-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rest_period_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-06", "metric": "rest_period_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-06", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-06", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-06", "metric": "rest_period_hours", "label": "rest period",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "rest period falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_recycle_pickup_age_days_07(record):
    """Evaluate recycling pickup age for control WP-0005-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycle_pickup_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-07", "metric": "recycle_pickup_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-07", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-07", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-07", "metric": "recycle_pickup_age_days", "label": "recycling pickup age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recycling pickup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_secure_pack_compliance_pct_08(record):
    """Evaluate secure packaging compliance for control WP-0005-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secure_pack_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-08", "metric": "secure_pack_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-08", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-08", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-08", "metric": "secure_pack_compliance_pct", "label": "secure packaging compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "secure packaging compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_ventilation_check_age_days_09(record):
    """Evaluate ventilation check age for control WP-0005-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ventilation_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-09", "metric": "ventilation_check_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-09", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-09", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-09", "metric": "ventilation_check_age_days", "label": "ventilation check age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "ventilation check age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_equipment_certification_age_days_10(record):
    """Evaluate equipment certification age for control WP-0005-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_certification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-10", "metric": "equipment_certification_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-10", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-10", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-10", "metric": "equipment_certification_age_days", "label": "equipment certification age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "equipment certification age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_disaster_recovery_test_age_days_11(record):
    """Evaluate disaster recovery test age for control WP-0005-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disaster_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-11", "metric": "disaster_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-11", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-11", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-11", "metric": "disaster_recovery_test_age_days", "label": "disaster recovery test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "disaster recovery test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_pipeline_failure_count_12(record):
    """Evaluate pipeline failures for control WP-0005-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pipeline_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-12", "metric": "pipeline_failure_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-12", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-12", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-12", "metric": "pipeline_failure_count", "label": "pipeline failures",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pipeline failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_packaging_master_gap_count_13(record):
    """Evaluate packaging master gaps for control WP-0005-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-13", "metric": "packaging_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-13", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-13", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-13", "metric": "packaging_master_gap_count", "label": "packaging master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "packaging master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_substitute_coverage_pct_14(record):
    """Evaluate substitute coverage for control WP-0005-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("substitute_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-14", "metric": "substitute_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-14", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-14", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-14", "metric": "substitute_coverage_pct", "label": "substitute coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "substitute coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_dispatch_cutoff_miss_count_15(record):
    """Evaluate dispatch cutoff misses for control WP-0005-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispatch_cutoff_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-15", "metric": "dispatch_cutoff_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-15", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-15", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-15", "metric": "dispatch_cutoff_miss_count", "label": "dispatch cutoff misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dispatch cutoff misses must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_claim_evidence_completeness_pct_16(record):
    """Evaluate claim evidence completeness for control WP-0005-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_evidence_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-16", "metric": "claim_evidence_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-16", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-16", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-16", "metric": "claim_evidence_completeness_pct", "label": "claim evidence completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "claim evidence completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_telematics_gap_minutes_17(record):
    """Evaluate telematics gap for control WP-0005-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-17", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-17", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-17", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-17", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "telematics gap exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_approval_queue_age_hours_18(record):
    """Evaluate approval queue age for control WP-0005-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-18", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-18", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-18", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-18", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "approval queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_subtier_visibility_pct_19(record):
    """Evaluate supplier sub-tier visibility for control WP-0005-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-19", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-19", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-19", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-19", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sub-tier visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_packaging_validation_age_days_20(record):
    """Evaluate supplier packaging validation age for control WP-0005-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-20", "metric": "supplier_packaging_validation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-20", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-20", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-20", "metric": "supplier_packaging_validation_age_days", "label": "supplier packaging validation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging validation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_export_control_gap_count_21(record):
    """Evaluate supplier export-control gaps for control WP-0005-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-21", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-21", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-21", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-21", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier export-control gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_dependency_count_22(record):
    """Evaluate supplier dependencies for control WP-0005-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-22", "metric": "supplier_dependency_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-22", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-22", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-22", "metric": "supplier_dependency_count", "label": "supplier dependencies",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier dependencies falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_aftermarket_support_score_23(record):
    """Evaluate supplier aftermarket support for control WP-0005-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_aftermarket_support_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-23", "metric": "supplier_aftermarket_support_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-23", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-23", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-23", "metric": "supplier_aftermarket_support_score", "label": "supplier aftermarket support",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier aftermarket support must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_service_recovery_score_24(record):
    """Evaluate supplier service recovery for control WP-0005-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0005-24", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0005-24", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0005-24", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0005-24", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier service recovery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_slotting_score_01, assess_mean_time_to_repair_hours_02, assess_supplier_risk_score_03, assess_database_lock_wait_ms_04, assess_min_order_qty_05, assess_rest_period_hours_06, assess_recycle_pickup_age_days_07, assess_secure_pack_compliance_pct_08, assess_ventilation_check_age_days_09, assess_equipment_certification_age_days_10, assess_disaster_recovery_test_age_days_11, assess_pipeline_failure_count_12, assess_packaging_master_gap_count_13, assess_substitute_coverage_pct_14, assess_dispatch_cutoff_miss_count_15, assess_claim_evidence_completeness_pct_16, assess_telematics_gap_minutes_17, assess_approval_queue_age_hours_18, assess_supplier_subtier_visibility_pct_19, assess_supplier_packaging_validation_age_days_20, assess_supplier_export_control_gap_count_21, assess_supplier_dependency_count_22, assess_supplier_aftermarket_support_score_23, assess_supplier_service_recovery_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

