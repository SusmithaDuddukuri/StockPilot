"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_mean_time_to_repair_hours_01(record):
    """Evaluate mean time to repair for control WP-0639-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-01", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-01", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-01", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-01", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "mean time to repair must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_risk_score_02(record):
    """Evaluate supplier risk for control WP-0639-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-02", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-02", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-02", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-02", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_database_lock_wait_ms_03(record):
    """Evaluate database lock wait for control WP-0639-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_lock_wait_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-03", "metric": "database_lock_wait_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-03", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-03", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-03", "metric": "database_lock_wait_ms", "label": "database lock wait",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "database lock wait exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_min_order_qty_04(record):
    """Evaluate minimum order quantity for control WP-0639-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("min_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-04", "metric": "min_order_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-04", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-04", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-04", "metric": "min_order_qty", "label": "minimum order quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "minimum order quantity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_rest_period_hours_05(record):
    """Evaluate rest period for control WP-0639-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rest_period_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-05", "metric": "rest_period_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-05", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-05", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-05", "metric": "rest_period_hours", "label": "rest period",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "rest period must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_recycle_pickup_age_days_06(record):
    """Evaluate recycling pickup age for control WP-0639-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycle_pickup_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-06", "metric": "recycle_pickup_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-06", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-06", "metric": "recycle_pickup_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-06", "metric": "recycle_pickup_age_days", "label": "recycling pickup age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recycling pickup age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_secure_pack_compliance_pct_07(record):
    """Evaluate secure packaging compliance for control WP-0639-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secure_pack_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-07", "metric": "secure_pack_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-07", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-07", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-07", "metric": "secure_pack_compliance_pct", "label": "secure packaging compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "secure packaging compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_ventilation_check_age_days_08(record):
    """Evaluate ventilation check age for control WP-0639-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ventilation_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-08", "metric": "ventilation_check_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-08", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-08", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-08", "metric": "ventilation_check_age_days", "label": "ventilation check age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "ventilation check age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_equipment_certification_age_days_09(record):
    """Evaluate equipment certification age for control WP-0639-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_certification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-09", "metric": "equipment_certification_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-09", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-09", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-09", "metric": "equipment_certification_age_days", "label": "equipment certification age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "equipment certification age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_disaster_recovery_test_age_days_10(record):
    """Evaluate disaster recovery test age for control WP-0639-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disaster_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-10", "metric": "disaster_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-10", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-10", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-10", "metric": "disaster_recovery_test_age_days", "label": "disaster recovery test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "disaster recovery test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_pipeline_failure_count_11(record):
    """Evaluate pipeline failures for control WP-0639-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pipeline_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-11", "metric": "pipeline_failure_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-11", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-11", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-11", "metric": "pipeline_failure_count", "label": "pipeline failures",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "pipeline failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_packaging_master_gap_count_12(record):
    """Evaluate packaging master gaps for control WP-0639-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-12", "metric": "packaging_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-12", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-12", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-12", "metric": "packaging_master_gap_count", "label": "packaging master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "packaging master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_substitute_coverage_pct_13(record):
    """Evaluate substitute coverage for control WP-0639-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("substitute_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-13", "metric": "substitute_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-13", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-13", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-13", "metric": "substitute_coverage_pct", "label": "substitute coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "substitute coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_dispatch_cutoff_miss_count_14(record):
    """Evaluate dispatch cutoff misses for control WP-0639-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispatch_cutoff_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-14", "metric": "dispatch_cutoff_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-14", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-14", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-14", "metric": "dispatch_cutoff_miss_count", "label": "dispatch cutoff misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dispatch cutoff misses must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_claim_evidence_completeness_pct_15(record):
    """Evaluate claim evidence completeness for control WP-0639-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_evidence_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-15", "metric": "claim_evidence_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-15", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-15", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-15", "metric": "claim_evidence_completeness_pct", "label": "claim evidence completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "claim evidence completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_telematics_gap_minutes_16(record):
    """Evaluate telematics gap for control WP-0639-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-16", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-16", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-16", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-16", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "telematics gap falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_approval_queue_age_hours_17(record):
    """Evaluate approval queue age for control WP-0639-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-17", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-17", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-17", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-17", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "approval queue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_subtier_visibility_pct_18(record):
    """Evaluate supplier sub-tier visibility for control WP-0639-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-18", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-18", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-18", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-18", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-tier visibility must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_packaging_validation_age_days_19(record):
    """Evaluate supplier packaging validation age for control WP-0639-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-19", "metric": "supplier_packaging_validation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-19", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-19", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-19", "metric": "supplier_packaging_validation_age_days", "label": "supplier packaging validation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier packaging validation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_export_control_gap_count_20(record):
    """Evaluate supplier export-control gaps for control WP-0639-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-20", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-20", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-20", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-20", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier export-control gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_dependency_count_21(record):
    """Evaluate supplier dependencies for control WP-0639-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-21", "metric": "supplier_dependency_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-21", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-21", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-21", "metric": "supplier_dependency_count", "label": "supplier dependencies",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dependencies must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_aftermarket_support_score_22(record):
    """Evaluate supplier aftermarket support for control WP-0639-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_aftermarket_support_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-22", "metric": "supplier_aftermarket_support_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-22", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-22", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-22", "metric": "supplier_aftermarket_support_score", "label": "supplier aftermarket support",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier aftermarket support must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_service_recovery_score_23(record):
    """Evaluate supplier service recovery for control WP-0639-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-23", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-23", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-23", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-23", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier service recovery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_fai_completion_pct_24(record):
    """Evaluate supplier first-article inspection for control WP-0639-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fai_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0639-24", "metric": "supplier_fai_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0639-24", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0639-24", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0639-24", "metric": "supplier_fai_completion_pct", "label": "supplier first-article inspection",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier first-article inspection falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_mean_time_to_repair_hours_01, assess_supplier_risk_score_02, assess_database_lock_wait_ms_03, assess_min_order_qty_04, assess_rest_period_hours_05, assess_recycle_pickup_age_days_06, assess_secure_pack_compliance_pct_07, assess_ventilation_check_age_days_08, assess_equipment_certification_age_days_09, assess_disaster_recovery_test_age_days_10, assess_pipeline_failure_count_11, assess_packaging_master_gap_count_12, assess_substitute_coverage_pct_13, assess_dispatch_cutoff_miss_count_14, assess_claim_evidence_completeness_pct_15, assess_telematics_gap_minutes_16, assess_approval_queue_age_hours_17, assess_supplier_subtier_visibility_pct_18, assess_supplier_packaging_validation_age_days_19, assess_supplier_export_control_gap_count_20, assess_supplier_dependency_count_21, assess_supplier_aftermarket_support_score_22, assess_supplier_service_recovery_score_23, assess_supplier_fai_completion_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

