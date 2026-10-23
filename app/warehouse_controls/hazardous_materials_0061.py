"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_delivery_confirmation_pct_01(record):
    """Evaluate supplier delivery confirmation for control WP-0061-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_confirmation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-01", "metric": "supplier_delivery_confirmation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-01", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-01", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-01", "metric": "supplier_delivery_confirmation_pct", "label": "supplier delivery confirmation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier delivery confirmation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_data_wipe_verification_pct_02(record):
    """Evaluate supplier data-wipe verification for control WP-0061-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_wipe_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-02", "metric": "supplier_data_wipe_verification_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-02", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-02", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-02", "metric": "supplier_data_wipe_verification_pct", "label": "supplier data-wipe verification",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier data-wipe verification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_utilization_pct_03(record):
    """Evaluate capacity utilization for control WP-0061-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-03", "metric": "utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-03", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-03", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-03", "metric": "utilization_pct", "label": "capacity utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "capacity utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_replenishment_age_hours_04(record):
    """Evaluate replenishment age for control WP-0061-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-04", "metric": "replenishment_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-04", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-04", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-04", "metric": "replenishment_age_hours", "label": "replenishment age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replenishment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_slow_mover_pct_05(record):
    """Evaluate slow-moving inventory for control WP-0061-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-05", "metric": "slow_mover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-05", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-05", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-05", "metric": "slow_mover_pct", "label": "slow-moving inventory",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "slow-moving inventory exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_purchase_price_variance_pct_06(record):
    """Evaluate purchase price variance for control WP-0061-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_price_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-06", "metric": "purchase_price_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-06", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-06", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-06", "metric": "purchase_price_variance_pct", "label": "purchase price variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "purchase price variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_vehicle_idle_minutes_07(record):
    """Evaluate vehicle idle time for control WP-0061-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_idle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-07", "metric": "vehicle_idle_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-07", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-07", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-07", "metric": "vehicle_idle_minutes", "label": "vehicle idle time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle idle time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_access_violation_count_08(record):
    """Evaluate access violations for control WP-0061-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-08", "metric": "access_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-08", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-08", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-08", "metric": "access_violation_count", "label": "access violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "access violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_shift_coverage_pct_09(record):
    """Evaluate shift coverage for control WP-0061-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-09", "metric": "shift_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-09", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-09", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-09", "metric": "shift_coverage_pct", "label": "shift coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "shift coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_fire_drill_age_days_10(record):
    """Evaluate fire drill age for control WP-0061-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-10", "metric": "fire_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-10", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-10", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-10", "metric": "fire_drill_age_days", "label": "fire drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "fire drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_proof_photo_pct_11(record):
    """Evaluate proof photo completion for control WP-0061-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-11", "metric": "proof_photo_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-11", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-11", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-11", "metric": "proof_photo_pct", "label": "proof photo completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "proof photo completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_data_logger_download_age_hours_12(record):
    """Evaluate data logger download age for control WP-0061-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_logger_download_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-12", "metric": "data_logger_download_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-12", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-12", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-12", "metric": "data_logger_download_age_hours", "label": "data logger download age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data logger download age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_customer_replacement_age_hours_13(record):
    """Evaluate replacement age for control WP-0061-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_replacement_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-13", "metric": "customer_replacement_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-13", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-13", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-13", "metric": "customer_replacement_age_hours", "label": "replacement age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "replacement age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_dock_edge_protection_pct_14(record):
    """Evaluate dock edge protection for control WP-0061-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-14", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-14", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-14", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-14", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "dock edge protection falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_industrial_network_segmentation_pct_15(record):
    """Evaluate industrial network segmentation for control WP-0061-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-15", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-15", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-15", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-15", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "industrial network segmentation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_domain_expiry_days_16(record):
    """Evaluate domain validity for control WP-0061-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-16", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-16", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-16", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-16", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "domain validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_equipment_assignment_gap_count_17(record):
    """Evaluate equipment assignment gaps for control WP-0061-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-17", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-17", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-17", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-17", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "equipment assignment gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_movement_duplicate_count_18(record):
    """Evaluate duplicate movements for control WP-0061-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("movement_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-18", "metric": "movement_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "movements",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-18", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-18", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-18", "metric": "movement_duplicate_count", "label": "duplicate movements",
        "status": "breach", "severity": "high", "unit": "movements",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "duplicate movements falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_reserve_pick_access_pct_19(record):
    """Evaluate reserve-pick access for control WP-0061-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserve_pick_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-19", "metric": "reserve_pick_access_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-19", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-19", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-19", "metric": "reserve_pick_access_pct", "label": "reserve-pick access",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reserve-pick access must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_dispute_resolution_days_20(record):
    """Evaluate dispute resolution time for control WP-0061-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_resolution_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-20", "metric": "dispute_resolution_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-20", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-20", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-20", "metric": "dispute_resolution_days", "label": "dispute resolution time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dispute resolution time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_gate_checkout_minutes_21(record):
    """Evaluate gate check-out time for control WP-0061-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkout_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-21", "metric": "gate_checkout_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-21", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-21", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-21", "metric": "gate_checkout_minutes", "label": "gate check-out time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "gate check-out time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_agency_labor_pct_22(record):
    """Evaluate agency labor share for control WP-0061-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("agency_labor_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-22", "metric": "agency_labor_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-22", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-22", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-22", "metric": "agency_labor_pct", "label": "agency labor share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "agency labor share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_packaging_damage_pct_23(record):
    """Evaluate supplier packaging damage for control WP-0061-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-23", "metric": "supplier_packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-23", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-23", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-23", "metric": "supplier_packaging_damage_pct", "label": "supplier packaging damage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier packaging damage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_change_notice_days_24(record):
    """Evaluate supplier change notice for control WP-0061-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0061-24", "metric": "supplier_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0061-24", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0061-24", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0061-24", "metric": "supplier_change_notice_days", "label": "supplier change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_delivery_confirmation_pct_01, assess_supplier_data_wipe_verification_pct_02, assess_utilization_pct_03, assess_replenishment_age_hours_04, assess_slow_mover_pct_05, assess_purchase_price_variance_pct_06, assess_vehicle_idle_minutes_07, assess_access_violation_count_08, assess_shift_coverage_pct_09, assess_fire_drill_age_days_10, assess_proof_photo_pct_11, assess_data_logger_download_age_hours_12, assess_customer_replacement_age_hours_13, assess_dock_edge_protection_pct_14, assess_industrial_network_segmentation_pct_15, assess_domain_expiry_days_16, assess_equipment_assignment_gap_count_17, assess_movement_duplicate_count_18, assess_reserve_pick_access_pct_19, assess_dispute_resolution_days_20, assess_gate_checkout_minutes_21, assess_agency_labor_pct_22, assess_supplier_packaging_damage_pct_23, assess_supplier_change_notice_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

