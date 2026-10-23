"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_maverick_buy_pct_01(record):
    """Evaluate supplier maverick buying for control WP-0501-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_maverick_buy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-01", "metric": "supplier_maverick_buy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-01", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-01", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-01", "metric": "supplier_maverick_buy_pct", "label": "supplier maverick buying",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier maverick buying exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_rework_pct_02(record):
    """Evaluate supplier rework rate for control WP-0501-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rework_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-02", "metric": "supplier_rework_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-02", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-02", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-02", "metric": "supplier_rework_pct", "label": "supplier rework rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier rework rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_business_review_age_days_03(record):
    """Evaluate business review age for control WP-0501-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-03", "metric": "supplier_business_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-03", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-03", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-03", "metric": "supplier_business_review_age_days", "label": "business review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "business review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_contract_termination_age_days_04(record):
    """Evaluate supplier contract termination age for control WP-0501-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contract_termination_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-04", "metric": "supplier_contract_termination_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-04", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-04", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-04", "metric": "supplier_contract_termination_age_days", "label": "supplier contract termination age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contract termination age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_fill_rate_pct_05(record):
    """Evaluate order fill rate for control WP-0501-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-05", "metric": "fill_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-05", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-05", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-05", "metric": "fill_rate_pct", "label": "order fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "order fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_defect_count_06(record):
    """Evaluate supplier defects for control WP-0501-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-06", "metric": "supplier_defect_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-06", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-06", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-06", "metric": "supplier_defect_count", "label": "supplier defects",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier defects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_dock_to_stock_minutes_07(record):
    """Evaluate dock-to-stock time for control WP-0501-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_to_stock_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-07", "metric": "dock_to_stock_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-07", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-07", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-07", "metric": "dock_to_stock_minutes", "label": "dock-to-stock time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dock-to-stock time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_near_miss_count_08(record):
    """Evaluate near misses for control WP-0501-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-08", "metric": "near_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-08", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-08", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-08", "metric": "near_miss_count", "label": "near misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "near misses must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_contract_days_left_09(record):
    """Evaluate contract validity for control WP-0501-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-09", "metric": "contract_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-09", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-09", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-09", "metric": "contract_days_left", "label": "contract validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "contract validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_backup_success_pct_10(record):
    """Evaluate backup success rate for control WP-0501-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-10", "metric": "backup_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-10", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-10", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-10", "metric": "backup_success_pct", "label": "backup success rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "backup success rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_service_level_pct_11(record):
    """Evaluate service level for control WP-0501-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_level_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-11", "metric": "service_level_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-11", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-11", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-11", "metric": "service_level_pct", "label": "service level",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "service level must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_manual_handling_weight_kg_12(record):
    """Evaluate manual handling weight for control WP-0501-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manual_handling_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-12", "metric": "manual_handling_weight_kg",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-12", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-12", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-12", "metric": "manual_handling_weight_kg", "label": "manual handling weight",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "manual handling weight must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_disposition_pending_count_13(record):
    """Evaluate pending dispositions for control WP-0501-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("disposition_pending_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-13", "metric": "disposition_pending_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "items",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-13", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-13", "metric": "disposition_pending_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-13", "metric": "disposition_pending_count", "label": "pending dispositions",
        "status": "breach", "severity": "medium", "unit": "items",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "pending dispositions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_lot_expiry_capture_pct_14(record):
    """Evaluate lot expiry capture for control WP-0501-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-14", "metric": "lot_expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-14", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-14", "metric": "lot_expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-14", "metric": "lot_expiry_capture_pct", "label": "lot expiry capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "lot expiry capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_spill_response_minutes_15(record):
    """Evaluate spill response time for control WP-0501-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-15", "metric": "spill_response_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-15", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-15", "metric": "spill_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-15", "metric": "spill_response_minutes", "label": "spill response time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "spill response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_worker_feedback_age_days_16(record):
    """Evaluate worker feedback age for control WP-0501-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-16", "metric": "worker_feedback_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-16", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-16", "metric": "worker_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-16", "metric": "worker_feedback_age_days", "label": "worker feedback age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "worker feedback age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_evacuation_route_clearance_pct_17(record):
    """Evaluate evacuation route clearance for control WP-0501-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evacuation_route_clearance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-17", "metric": "evacuation_route_clearance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-17", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-17", "metric": "evacuation_route_clearance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-17", "metric": "evacuation_route_clearance_pct", "label": "evacuation route clearance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "evacuation route clearance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_data_lineage_coverage_pct_18(record):
    """Evaluate data lineage coverage for control WP-0501-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_lineage_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-18", "metric": "data_lineage_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-18", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-18", "metric": "data_lineage_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-18", "metric": "data_lineage_coverage_pct", "label": "data lineage coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "data lineage coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_location_master_gap_count_19(record):
    """Evaluate location master gaps for control WP-0501-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("location_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-19", "metric": "location_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-19", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-19", "metric": "location_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-19", "metric": "location_master_gap_count", "label": "location master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "location master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_slow_mover_age_days_20(record):
    """Evaluate slow-mover age for control WP-0501-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-20", "metric": "slow_mover_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-20", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-20", "metric": "slow_mover_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-20", "metric": "slow_mover_age_days", "label": "slow-mover age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slow-mover age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_manifest_close_age_minutes_21(record):
    """Evaluate manifest close age for control WP-0501-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manifest_close_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-21", "metric": "manifest_close_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-21", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-21", "metric": "manifest_close_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-21", "metric": "manifest_close_age_minutes", "label": "manifest close age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "manifest close age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_export_control_review_age_hours_22(record):
    """Evaluate export-control review age for control WP-0501-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_control_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-22", "metric": "export_control_review_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-22", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-22", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-22", "metric": "export_control_review_age_hours", "label": "export-control review age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "export-control review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_vehicle_registration_days_left_23(record):
    """Evaluate vehicle registration validity for control WP-0501-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-23", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-23", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-23", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-23", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle registration validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_project_milestone_delay_days_24(record):
    """Evaluate project milestone delay for control WP-0501-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0501-24", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0501-24", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0501-24", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0501-24", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "project milestone delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_supplier_maverick_buy_pct_01, assess_supplier_rework_pct_02, assess_supplier_business_review_age_days_03, assess_supplier_contract_termination_age_days_04, assess_fill_rate_pct_05, assess_supplier_defect_count_06, assess_dock_to_stock_minutes_07, assess_near_miss_count_08, assess_contract_days_left_09, assess_backup_success_pct_10, assess_service_level_pct_11, assess_manual_handling_weight_kg_12, assess_disposition_pending_count_13, assess_lot_expiry_capture_pct_14, assess_spill_response_minutes_15, assess_worker_feedback_age_days_16, assess_evacuation_route_clearance_pct_17, assess_data_lineage_coverage_pct_18, assess_location_master_gap_count_19, assess_slow_mover_age_days_20, assess_manifest_close_age_minutes_21, assess_export_control_review_age_hours_22, assess_vehicle_registration_days_left_23, assess_project_milestone_delay_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

