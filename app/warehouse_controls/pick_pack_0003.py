"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_defect_count_01(record):
    """Evaluate supplier defects for control WP-0003-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-01", "metric": "supplier_defect_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-01", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-01", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-01", "metric": "supplier_defect_count", "label": "supplier defects",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier defects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_dock_to_stock_minutes_02(record):
    """Evaluate dock-to-stock time for control WP-0003-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_to_stock_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-02", "metric": "dock_to_stock_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-02", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-02", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-02", "metric": "dock_to_stock_minutes", "label": "dock-to-stock time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock-to-stock time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_near_miss_count_03(record):
    """Evaluate near misses for control WP-0003-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-03", "metric": "near_miss_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-03", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-03", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-03", "metric": "near_miss_count", "label": "near misses",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "near misses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_contract_days_left_04(record):
    """Evaluate contract validity for control WP-0003-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-04", "metric": "contract_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-04", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-04", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-04", "metric": "contract_days_left", "label": "contract validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "contract validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_backup_success_pct_05(record):
    """Evaluate backup success rate for control WP-0003-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-05", "metric": "backup_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-05", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-05", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-05", "metric": "backup_success_pct", "label": "backup success rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backup success rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_service_level_pct_06(record):
    """Evaluate service level for control WP-0003-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_level_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-06", "metric": "service_level_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-06", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-06", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-06", "metric": "service_level_pct", "label": "service level",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "service level must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_manual_handling_weight_kg_07(record):
    """Evaluate manual handling weight for control WP-0003-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manual_handling_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-07", "metric": "manual_handling_weight_kg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-07", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-07", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-07", "metric": "manual_handling_weight_kg", "label": "manual handling weight",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "manual handling weight exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_disposition_pending_count_08(record):
    """Evaluate pending dispositions for control WP-0003-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disposition_pending_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-08", "metric": "disposition_pending_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-08", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-08", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-08", "metric": "disposition_pending_count", "label": "pending dispositions",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "pending dispositions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_lot_expiry_capture_pct_09(record):
    """Evaluate lot expiry capture for control WP-0003-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-09", "metric": "lot_expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-09", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-09", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-09", "metric": "lot_expiry_capture_pct", "label": "lot expiry capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lot expiry capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_spill_response_minutes_10(record):
    """Evaluate spill response time for control WP-0003-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-10", "metric": "spill_response_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-10", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-10", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-10", "metric": "spill_response_minutes", "label": "spill response time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "spill response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_worker_feedback_age_days_11(record):
    """Evaluate worker feedback age for control WP-0003-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-11", "metric": "worker_feedback_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-11", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-11", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-11", "metric": "worker_feedback_age_days", "label": "worker feedback age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "worker feedback age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_evacuation_route_clearance_pct_12(record):
    """Evaluate evacuation route clearance for control WP-0003-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evacuation_route_clearance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-12", "metric": "evacuation_route_clearance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-12", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-12", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-12", "metric": "evacuation_route_clearance_pct", "label": "evacuation route clearance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "evacuation route clearance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_data_lineage_coverage_pct_13(record):
    """Evaluate data lineage coverage for control WP-0003-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_lineage_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-13", "metric": "data_lineage_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-13", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-13", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-13", "metric": "data_lineage_coverage_pct", "label": "data lineage coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data lineage coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_location_master_gap_count_14(record):
    """Evaluate location master gaps for control WP-0003-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("location_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-14", "metric": "location_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-14", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-14", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-14", "metric": "location_master_gap_count", "label": "location master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "location master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_slow_mover_age_days_15(record):
    """Evaluate slow-mover age for control WP-0003-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-15", "metric": "slow_mover_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-15", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-15", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-15", "metric": "slow_mover_age_days", "label": "slow-mover age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "slow-mover age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_manifest_close_age_minutes_16(record):
    """Evaluate manifest close age for control WP-0003-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manifest_close_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-16", "metric": "manifest_close_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-16", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-16", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-16", "metric": "manifest_close_age_minutes", "label": "manifest close age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "manifest close age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_export_control_review_age_hours_17(record):
    """Evaluate export-control review age for control WP-0003-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_control_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-17", "metric": "export_control_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-17", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-17", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-17", "metric": "export_control_review_age_hours", "label": "export-control review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "export-control review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_vehicle_registration_days_left_18(record):
    """Evaluate vehicle registration validity for control WP-0003-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-18", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-18", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-18", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-18", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle registration validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_project_milestone_delay_days_19(record):
    """Evaluate project milestone delay for control WP-0003-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-19", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-19", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-19", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-19", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "project milestone delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_capacity_review_age_days_20(record):
    """Evaluate supplier capacity review age for control WP-0003-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-20", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-20", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-20", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-20", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier capacity review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_process_audit_age_days_21(record):
    """Evaluate supplier process audit age for control WP-0003-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-21", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-21", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-21", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-21", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_tax_document_age_days_22(record):
    """Evaluate supplier tax document age for control WP-0003-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-22", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-22", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-22", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-22", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tax document age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_exit_plan_age_days_23(record):
    """Evaluate supplier exit-plan age for control WP-0003-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-23", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-23", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-23", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-23", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier exit-plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_recycling_label_pct_24(record):
    """Evaluate supplier recycling-label compliance for control WP-0003-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0003-24", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0003-24", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0003-24", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0003-24", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier recycling-label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_defect_count_01, assess_dock_to_stock_minutes_02, assess_near_miss_count_03, assess_contract_days_left_04, assess_backup_success_pct_05, assess_service_level_pct_06, assess_manual_handling_weight_kg_07, assess_disposition_pending_count_08, assess_lot_expiry_capture_pct_09, assess_spill_response_minutes_10, assess_worker_feedback_age_days_11, assess_evacuation_route_clearance_pct_12, assess_data_lineage_coverage_pct_13, assess_location_master_gap_count_14, assess_slow_mover_age_days_15, assess_manifest_close_age_minutes_16, assess_export_control_review_age_hours_17, assess_vehicle_registration_days_left_18, assess_project_milestone_delay_days_19, assess_supplier_capacity_review_age_days_20, assess_supplier_process_audit_age_days_21, assess_supplier_tax_document_age_days_22, assess_supplier_exit_plan_age_days_23, assess_supplier_recycling_label_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

