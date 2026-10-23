"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_worker_feedback_age_days_01(record):
    """Evaluate worker feedback age for control WP-0462-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-01", "metric": "worker_feedback_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-01", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-01", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-01", "metric": "worker_feedback_age_days", "label": "worker feedback age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "worker feedback age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_evacuation_route_clearance_pct_02(record):
    """Evaluate evacuation route clearance for control WP-0462-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evacuation_route_clearance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-02", "metric": "evacuation_route_clearance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-02", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-02", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-02", "metric": "evacuation_route_clearance_pct", "label": "evacuation route clearance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "evacuation route clearance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_data_lineage_coverage_pct_03(record):
    """Evaluate data lineage coverage for control WP-0462-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_lineage_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-03", "metric": "data_lineage_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-03", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-03", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-03", "metric": "data_lineage_coverage_pct", "label": "data lineage coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "data lineage coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_location_master_gap_count_04(record):
    """Evaluate location master gaps for control WP-0462-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("location_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-04", "metric": "location_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-04", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-04", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-04", "metric": "location_master_gap_count", "label": "location master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "location master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_slow_mover_age_days_05(record):
    """Evaluate slow-mover age for control WP-0462-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-05", "metric": "slow_mover_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-05", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-05", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-05", "metric": "slow_mover_age_days", "label": "slow-mover age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slow-mover age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_manifest_close_age_minutes_06(record):
    """Evaluate manifest close age for control WP-0462-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manifest_close_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-06", "metric": "manifest_close_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-06", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-06", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-06", "metric": "manifest_close_age_minutes", "label": "manifest close age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "manifest close age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_export_control_review_age_hours_07(record):
    """Evaluate export-control review age for control WP-0462-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_control_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-07", "metric": "export_control_review_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-07", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-07", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-07", "metric": "export_control_review_age_hours", "label": "export-control review age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "export-control review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_vehicle_registration_days_left_08(record):
    """Evaluate vehicle registration validity for control WP-0462-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-08", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-08", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-08", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-08", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle registration validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_project_milestone_delay_days_09(record):
    """Evaluate project milestone delay for control WP-0462-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-09", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-09", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-09", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-09", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "project milestone delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_capacity_review_age_days_10(record):
    """Evaluate supplier capacity review age for control WP-0462-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-10", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-10", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-10", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-10", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier capacity review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_process_audit_age_days_11(record):
    """Evaluate supplier process audit age for control WP-0462-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-11", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-11", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-11", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-11", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier process audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_tax_document_age_days_12(record):
    """Evaluate supplier tax document age for control WP-0462-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-12", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-12", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-12", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-12", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tax document age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_exit_plan_age_days_13(record):
    """Evaluate supplier exit-plan age for control WP-0462-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-13", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-13", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-13", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-13", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit-plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_recycling_label_pct_14(record):
    """Evaluate supplier recycling-label compliance for control WP-0462-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-14", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-14", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-14", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-14", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "supplier recycling-label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_route_monitoring_pct_15(record):
    """Evaluate supplier route monitoring for control WP-0462-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-15", "metric": "supplier_route_monitoring_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-15", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-15", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-15", "metric": "supplier_route_monitoring_pct", "label": "supplier route monitoring",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier route monitoring falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_deviation_age_days_16(record):
    """Evaluate supplier deviation age for control WP-0462-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deviation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-16", "metric": "supplier_deviation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-16", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-16", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-16", "metric": "supplier_deviation_age_days", "label": "supplier deviation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier deviation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_hazmat_training_pct_17(record):
    """Evaluate supplier hazmat training for control WP-0462-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_hazmat_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-17", "metric": "supplier_hazmat_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-17", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-17", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-17", "metric": "supplier_hazmat_training_pct", "label": "supplier hazmat training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier hazmat training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_payment_exception_age_days_18(record):
    """Evaluate supplier payment exception age for control WP-0462-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-18", "metric": "supplier_payment_exception_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-18", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-18", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-18", "metric": "supplier_payment_exception_age_days", "label": "supplier payment exception age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier payment exception age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_cross_training_pct_19(record):
    """Evaluate supplier cross-training for control WP-0462-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-19", "metric": "supplier_cross_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-19", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-19", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-19", "metric": "supplier_cross_training_pct", "label": "supplier cross-training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "supplier cross-training falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_model_availability_pct_20(record):
    """Evaluate supplier model availability for control WP-0462-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-20", "metric": "supplier_model_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-20", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-20", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-20", "metric": "supplier_model_availability_pct", "label": "supplier model availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model availability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_event_schema_age_days_21(record):
    """Evaluate supplier event-schema age for control WP-0462-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_schema_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-21", "metric": "supplier_event_schema_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-21", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-21", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-21", "metric": "supplier_event_schema_age_days", "label": "supplier event-schema age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier event-schema age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_admin_session_age_minutes_22(record):
    """Evaluate supplier admin session age for control WP-0462-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_admin_session_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-22", "metric": "supplier_admin_session_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-22", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-22", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-22", "metric": "supplier_admin_session_age_minutes", "label": "supplier admin session age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier admin session age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_confidentiality_breach_count_23(record):
    """Evaluate supplier confidentiality breaches for control WP-0462-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_confidentiality_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-23", "metric": "supplier_confidentiality_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-23", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-23", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-23", "metric": "supplier_confidentiality_breach_count", "label": "supplier confidentiality breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier confidentiality breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_record_signoff_pct_24(record):
    """Evaluate supplier record signoff for control WP-0462-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0462-24", "metric": "supplier_record_signoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0462-24", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0462-24", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0462-24", "metric": "supplier_record_signoff_pct", "label": "supplier record signoff",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier record signoff must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_worker_feedback_age_days_01, assess_evacuation_route_clearance_pct_02, assess_data_lineage_coverage_pct_03, assess_location_master_gap_count_04, assess_slow_mover_age_days_05, assess_manifest_close_age_minutes_06, assess_export_control_review_age_hours_07, assess_vehicle_registration_days_left_08, assess_project_milestone_delay_days_09, assess_supplier_capacity_review_age_days_10, assess_supplier_process_audit_age_days_11, assess_supplier_tax_document_age_days_12, assess_supplier_exit_plan_age_days_13, assess_supplier_recycling_label_pct_14, assess_supplier_route_monitoring_pct_15, assess_supplier_deviation_age_days_16, assess_supplier_hazmat_training_pct_17, assess_supplier_payment_exception_age_days_18, assess_supplier_cross_training_pct_19, assess_supplier_model_availability_pct_20, assess_supplier_event_schema_age_days_21, assess_supplier_admin_session_age_minutes_22, assess_supplier_confidentiality_breach_count_23, assess_supplier_record_signoff_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

