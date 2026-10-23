"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_secure_pack_compliance_pct_01(record):
    """Evaluate secure packaging compliance for control WP-0396-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secure_pack_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-01", "metric": "secure_pack_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-01", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-01", "metric": "secure_pack_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-01", "metric": "secure_pack_compliance_pct", "label": "secure packaging compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "secure packaging compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_ventilation_check_age_days_02(record):
    """Evaluate ventilation check age for control WP-0396-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ventilation_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-02", "metric": "ventilation_check_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-02", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-02", "metric": "ventilation_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-02", "metric": "ventilation_check_age_days", "label": "ventilation check age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ventilation check age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_equipment_certification_age_days_03(record):
    """Evaluate equipment certification age for control WP-0396-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_certification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-03", "metric": "equipment_certification_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-03", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-03", "metric": "equipment_certification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-03", "metric": "equipment_certification_age_days", "label": "equipment certification age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment certification age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_disaster_recovery_test_age_days_04(record):
    """Evaluate disaster recovery test age for control WP-0396-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disaster_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-04", "metric": "disaster_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-04", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-04", "metric": "disaster_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-04", "metric": "disaster_recovery_test_age_days", "label": "disaster recovery test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "disaster recovery test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_pipeline_failure_count_05(record):
    """Evaluate pipeline failures for control WP-0396-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pipeline_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-05", "metric": "pipeline_failure_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-05", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-05", "metric": "pipeline_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-05", "metric": "pipeline_failure_count", "label": "pipeline failures",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "pipeline failures falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_packaging_master_gap_count_06(record):
    """Evaluate packaging master gaps for control WP-0396-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-06", "metric": "packaging_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-06", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-06", "metric": "packaging_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-06", "metric": "packaging_master_gap_count", "label": "packaging master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "packaging master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_substitute_coverage_pct_07(record):
    """Evaluate substitute coverage for control WP-0396-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("substitute_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-07", "metric": "substitute_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-07", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-07", "metric": "substitute_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-07", "metric": "substitute_coverage_pct", "label": "substitute coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "substitute coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_dispatch_cutoff_miss_count_08(record):
    """Evaluate dispatch cutoff misses for control WP-0396-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispatch_cutoff_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-08", "metric": "dispatch_cutoff_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-08", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-08", "metric": "dispatch_cutoff_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-08", "metric": "dispatch_cutoff_miss_count", "label": "dispatch cutoff misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "dispatch cutoff misses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_claim_evidence_completeness_pct_09(record):
    """Evaluate claim evidence completeness for control WP-0396-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_evidence_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-09", "metric": "claim_evidence_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-09", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-09", "metric": "claim_evidence_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-09", "metric": "claim_evidence_completeness_pct", "label": "claim evidence completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "claim evidence completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_telematics_gap_minutes_10(record):
    """Evaluate telematics gap for control WP-0396-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-10", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-10", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-10", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-10", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "telematics gap must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_approval_queue_age_hours_11(record):
    """Evaluate approval queue age for control WP-0396-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-11", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-11", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-11", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-11", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "approval queue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_subtier_visibility_pct_12(record):
    """Evaluate supplier sub-tier visibility for control WP-0396-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-12", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-12", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-12", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-12", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier sub-tier visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_packaging_validation_age_days_13(record):
    """Evaluate supplier packaging validation age for control WP-0396-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-13", "metric": "supplier_packaging_validation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-13", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-13", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-13", "metric": "supplier_packaging_validation_age_days", "label": "supplier packaging validation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier packaging validation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_export_control_gap_count_14(record):
    """Evaluate supplier export-control gaps for control WP-0396-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-14", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-14", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-14", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-14", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier export-control gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_dependency_count_15(record):
    """Evaluate supplier dependencies for control WP-0396-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-15", "metric": "supplier_dependency_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-15", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-15", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-15", "metric": "supplier_dependency_count", "label": "supplier dependencies",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dependencies must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_aftermarket_support_score_16(record):
    """Evaluate supplier aftermarket support for control WP-0396-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_aftermarket_support_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-16", "metric": "supplier_aftermarket_support_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-16", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-16", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-16", "metric": "supplier_aftermarket_support_score", "label": "supplier aftermarket support",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier aftermarket support exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_service_recovery_score_17(record):
    """Evaluate supplier service recovery for control WP-0396-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-17", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-17", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-17", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-17", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier service recovery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_fai_completion_pct_18(record):
    """Evaluate supplier first-article inspection for control WP-0396-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fai_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-18", "metric": "supplier_fai_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-18", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-18", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-18", "metric": "supplier_fai_completion_pct", "label": "supplier first-article inspection",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier first-article inspection must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_fire_response_drill_age_days_19(record):
    """Evaluate supplier fire drill age for control WP-0396-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-19", "metric": "supplier_fire_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-19", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-19", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-19", "metric": "supplier_fire_response_drill_age_days", "label": "supplier fire drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier fire drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_ap_days_20(record):
    """Evaluate supplier accounts-payable days for control WP-0396-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ap_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-20", "metric": "supplier_ap_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-20", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-20", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-20", "metric": "supplier_ap_days", "label": "supplier accounts-payable days",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier accounts-payable days exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_knowledge_base_age_days_21(record):
    """Evaluate supplier knowledge-base age for control WP-0396-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_base_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-21", "metric": "supplier_knowledge_base_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-21", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-21", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-21", "metric": "supplier_knowledge_base_age_days", "label": "supplier knowledge-base age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier knowledge-base age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_bias_audit_age_days_22(record):
    """Evaluate supplier bias-audit age for control WP-0396-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bias_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-22", "metric": "supplier_bias_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-22", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-22", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-22", "metric": "supplier_bias_audit_age_days", "label": "supplier bias-audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier bias-audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_duplicate_event_pct_23(record):
    """Evaluate supplier duplicate event rate for control WP-0396-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_event_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-23", "metric": "supplier_duplicate_event_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-23", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-23", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-23", "metric": "supplier_duplicate_event_pct", "label": "supplier duplicate event rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier duplicate event rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_pen_test_age_days_24(record):
    """Evaluate supplier penetration-test age for control WP-0396-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pen_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0396-24", "metric": "supplier_pen_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0396-24", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0396-24", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0396-24", "metric": "supplier_pen_test_age_days", "label": "supplier penetration-test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier penetration-test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_secure_pack_compliance_pct_01, assess_ventilation_check_age_days_02, assess_equipment_certification_age_days_03, assess_disaster_recovery_test_age_days_04, assess_pipeline_failure_count_05, assess_packaging_master_gap_count_06, assess_substitute_coverage_pct_07, assess_dispatch_cutoff_miss_count_08, assess_claim_evidence_completeness_pct_09, assess_telematics_gap_minutes_10, assess_approval_queue_age_hours_11, assess_supplier_subtier_visibility_pct_12, assess_supplier_packaging_validation_age_days_13, assess_supplier_export_control_gap_count_14, assess_supplier_dependency_count_15, assess_supplier_aftermarket_support_score_16, assess_supplier_service_recovery_score_17, assess_supplier_fai_completion_pct_18, assess_supplier_fire_response_drill_age_days_19, assess_supplier_ap_days_20, assess_supplier_knowledge_base_age_days_21, assess_supplier_bias_audit_age_days_22, assess_supplier_duplicate_event_pct_23, assess_supplier_pen_test_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

