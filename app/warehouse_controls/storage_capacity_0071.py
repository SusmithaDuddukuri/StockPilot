"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_contract_days_left_01(record):
    """Evaluate contract validity for control WP-0071-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-01", "metric": "contract_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-01", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-01", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-01", "metric": "contract_days_left", "label": "contract validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "contract validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_backup_success_pct_02(record):
    """Evaluate backup success rate for control WP-0071-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-02", "metric": "backup_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-02", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-02", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-02", "metric": "backup_success_pct", "label": "backup success rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backup success rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_service_level_pct_03(record):
    """Evaluate service level for control WP-0071-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_level_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-03", "metric": "service_level_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-03", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-03", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-03", "metric": "service_level_pct", "label": "service level",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "service level exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_manual_handling_weight_kg_04(record):
    """Evaluate manual handling weight for control WP-0071-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manual_handling_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-04", "metric": "manual_handling_weight_kg",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-04", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-04", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-04", "metric": "manual_handling_weight_kg", "label": "manual handling weight",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "manual handling weight falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_disposition_pending_count_05(record):
    """Evaluate pending dispositions for control WP-0071-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disposition_pending_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-05", "metric": "disposition_pending_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-05", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-05", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-05", "metric": "disposition_pending_count", "label": "pending dispositions",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pending dispositions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_lot_expiry_capture_pct_06(record):
    """Evaluate lot expiry capture for control WP-0071-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-06", "metric": "lot_expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-06", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-06", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-06", "metric": "lot_expiry_capture_pct", "label": "lot expiry capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lot expiry capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_spill_response_minutes_07(record):
    """Evaluate spill response time for control WP-0071-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-07", "metric": "spill_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-07", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-07", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-07", "metric": "spill_response_minutes", "label": "spill response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "spill response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_worker_feedback_age_days_08(record):
    """Evaluate worker feedback age for control WP-0071-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-08", "metric": "worker_feedback_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-08", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-08", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-08", "metric": "worker_feedback_age_days", "label": "worker feedback age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "worker feedback age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_evacuation_route_clearance_pct_09(record):
    """Evaluate evacuation route clearance for control WP-0071-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evacuation_route_clearance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-09", "metric": "evacuation_route_clearance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-09", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-09", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-09", "metric": "evacuation_route_clearance_pct", "label": "evacuation route clearance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "evacuation route clearance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_data_lineage_coverage_pct_10(record):
    """Evaluate data lineage coverage for control WP-0071-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_lineage_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-10", "metric": "data_lineage_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-10", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-10", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-10", "metric": "data_lineage_coverage_pct", "label": "data lineage coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data lineage coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_location_master_gap_count_11(record):
    """Evaluate location master gaps for control WP-0071-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("location_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-11", "metric": "location_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-11", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-11", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-11", "metric": "location_master_gap_count", "label": "location master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "location master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_slow_mover_age_days_12(record):
    """Evaluate slow-mover age for control WP-0071-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-12", "metric": "slow_mover_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-12", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-12", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-12", "metric": "slow_mover_age_days", "label": "slow-mover age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "slow-mover age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_manifest_close_age_minutes_13(record):
    """Evaluate manifest close age for control WP-0071-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manifest_close_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-13", "metric": "manifest_close_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-13", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-13", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-13", "metric": "manifest_close_age_minutes", "label": "manifest close age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "manifest close age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_export_control_review_age_hours_14(record):
    """Evaluate export-control review age for control WP-0071-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_control_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-14", "metric": "export_control_review_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-14", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-14", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-14", "metric": "export_control_review_age_hours", "label": "export-control review age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "export-control review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_vehicle_registration_days_left_15(record):
    """Evaluate vehicle registration validity for control WP-0071-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-15", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-15", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-15", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-15", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "vehicle registration validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_project_milestone_delay_days_16(record):
    """Evaluate project milestone delay for control WP-0071-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-16", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-16", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-16", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-16", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "project milestone delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_capacity_review_age_days_17(record):
    """Evaluate supplier capacity review age for control WP-0071-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-17", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-17", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-17", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-17", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_process_audit_age_days_18(record):
    """Evaluate supplier process audit age for control WP-0071-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-18", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-18", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-18", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-18", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process audit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_tax_document_age_days_19(record):
    """Evaluate supplier tax document age for control WP-0071-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-19", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-19", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-19", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-19", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "supplier tax document age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_exit_plan_age_days_20(record):
    """Evaluate supplier exit-plan age for control WP-0071-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-20", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-20", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-20", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-20", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier exit-plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_recycling_label_pct_21(record):
    """Evaluate supplier recycling-label compliance for control WP-0071-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-21", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-21", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-21", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-21", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recycling-label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_route_monitoring_pct_22(record):
    """Evaluate supplier route monitoring for control WP-0071-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-22", "metric": "supplier_route_monitoring_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-22", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-22", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-22", "metric": "supplier_route_monitoring_pct", "label": "supplier route monitoring",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier route monitoring must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_deviation_age_days_23(record):
    """Evaluate supplier deviation age for control WP-0071-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deviation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-23", "metric": "supplier_deviation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-23", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-23", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-23", "metric": "supplier_deviation_age_days", "label": "supplier deviation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier deviation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_hazmat_training_pct_24(record):
    """Evaluate supplier hazmat training for control WP-0071-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_hazmat_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0071-24", "metric": "supplier_hazmat_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0071-24", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0071-24", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0071-24", "metric": "supplier_hazmat_training_pct", "label": "supplier hazmat training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier hazmat training falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_contract_days_left_01, assess_backup_success_pct_02, assess_service_level_pct_03, assess_manual_handling_weight_kg_04, assess_disposition_pending_count_05, assess_lot_expiry_capture_pct_06, assess_spill_response_minutes_07, assess_worker_feedback_age_days_08, assess_evacuation_route_clearance_pct_09, assess_data_lineage_coverage_pct_10, assess_location_master_gap_count_11, assess_slow_mover_age_days_12, assess_manifest_close_age_minutes_13, assess_export_control_review_age_hours_14, assess_vehicle_registration_days_left_15, assess_project_milestone_delay_days_16, assess_supplier_capacity_review_age_days_17, assess_supplier_process_audit_age_days_18, assess_supplier_tax_document_age_days_19, assess_supplier_exit_plan_age_days_20, assess_supplier_recycling_label_pct_21, assess_supplier_route_monitoring_pct_22, assess_supplier_deviation_age_days_23, assess_supplier_hazmat_training_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

