"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_vehicle_idle_minutes_01(record):
    """Evaluate vehicle idle time for control WP-0197-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_idle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-01", "metric": "vehicle_idle_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-01", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-01", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-01", "metric": "vehicle_idle_minutes", "label": "vehicle idle time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "vehicle idle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_access_violation_count_02(record):
    """Evaluate access violations for control WP-0197-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-02", "metric": "access_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-02", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-02", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-02", "metric": "access_violation_count", "label": "access violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "access violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_shift_coverage_pct_03(record):
    """Evaluate shift coverage for control WP-0197-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-03", "metric": "shift_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-03", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-03", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-03", "metric": "shift_coverage_pct", "label": "shift coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "shift coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_fire_drill_age_days_04(record):
    """Evaluate fire drill age for control WP-0197-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-04", "metric": "fire_drill_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-04", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-04", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-04", "metric": "fire_drill_age_days", "label": "fire drill age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fire drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_proof_photo_pct_05(record):
    """Evaluate proof photo completion for control WP-0197-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-05", "metric": "proof_photo_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-05", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-05", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-05", "metric": "proof_photo_pct", "label": "proof photo completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "proof photo completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_data_logger_download_age_hours_06(record):
    """Evaluate data logger download age for control WP-0197-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_logger_download_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-06", "metric": "data_logger_download_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-06", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-06", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-06", "metric": "data_logger_download_age_hours", "label": "data logger download age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "data logger download age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_customer_replacement_age_hours_07(record):
    """Evaluate replacement age for control WP-0197-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_replacement_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-07", "metric": "customer_replacement_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-07", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-07", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-07", "metric": "customer_replacement_age_hours", "label": "replacement age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replacement age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_dock_edge_protection_pct_08(record):
    """Evaluate dock edge protection for control WP-0197-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-08", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-08", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-08", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-08", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock edge protection must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_industrial_network_segmentation_pct_09(record):
    """Evaluate industrial network segmentation for control WP-0197-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-09", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-09", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-09", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-09", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "industrial network segmentation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_domain_expiry_days_10(record):
    """Evaluate domain validity for control WP-0197-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-10", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-10", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-10", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-10", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "domain validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_equipment_assignment_gap_count_11(record):
    """Evaluate equipment assignment gaps for control WP-0197-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-11", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-11", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-11", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-11", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "equipment assignment gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_movement_duplicate_count_12(record):
    """Evaluate duplicate movements for control WP-0197-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("movement_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-12", "metric": "movement_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "movements",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-12", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-12", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-12", "metric": "movement_duplicate_count", "label": "duplicate movements",
        "status": "breach", "severity": "low", "unit": "movements",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate movements must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_reserve_pick_access_pct_13(record):
    """Evaluate reserve-pick access for control WP-0197-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserve_pick_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-13", "metric": "reserve_pick_access_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-13", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-13", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-13", "metric": "reserve_pick_access_pct", "label": "reserve-pick access",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "reserve-pick access exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_dispute_resolution_days_14(record):
    """Evaluate dispute resolution time for control WP-0197-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_resolution_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-14", "metric": "dispute_resolution_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-14", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-14", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-14", "metric": "dispute_resolution_days", "label": "dispute resolution time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "dispute resolution time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_gate_checkout_minutes_15(record):
    """Evaluate gate check-out time for control WP-0197-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkout_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-15", "metric": "gate_checkout_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-15", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-15", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-15", "metric": "gate_checkout_minutes", "label": "gate check-out time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "gate check-out time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_agency_labor_pct_16(record):
    """Evaluate agency labor share for control WP-0197-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("agency_labor_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-16", "metric": "agency_labor_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-16", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-16", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-16", "metric": "agency_labor_pct", "label": "agency labor share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "agency labor share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_packaging_damage_pct_17(record):
    """Evaluate supplier packaging damage for control WP-0197-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-17", "metric": "supplier_packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-17", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-17", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-17", "metric": "supplier_packaging_damage_pct", "label": "supplier packaging damage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier packaging damage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_change_notice_days_18(record):
    """Evaluate supplier change notice for control WP-0197-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-18", "metric": "supplier_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-18", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-18", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-18", "metric": "supplier_change_notice_days", "label": "supplier change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "supplier change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_shipping_window_compliance_pct_19(record):
    """Evaluate supplier shipping-window compliance for control WP-0197-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_window_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-19", "metric": "supplier_shipping_window_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-19", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-19", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-19", "metric": "supplier_shipping_window_compliance_pct", "label": "supplier shipping-window compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier shipping-window compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_service_availability_pct_20(record):
    """Evaluate supplier service availability for control WP-0197-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-20", "metric": "supplier_service_availability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-20", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-20", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-20", "metric": "supplier_service_availability_pct", "label": "supplier service availability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier service availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_lot_data_completeness_pct_21(record):
    """Evaluate supplier lot-data completeness for control WP-0197-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lot_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-21", "metric": "supplier_lot_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-21", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-21", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-21", "metric": "supplier_lot_data_completeness_pct", "label": "supplier lot-data completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier lot-data completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_site_access_review_age_days_22(record):
    """Evaluate supplier site access review age for control WP-0197-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-22", "metric": "supplier_site_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-22", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-22", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-22", "metric": "supplier_site_access_review_age_days", "label": "supplier site access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "supplier site access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_critical_process_backup_pct_23(record):
    """Evaluate supplier critical-process backup for control WP-0197-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_process_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-23", "metric": "supplier_critical_process_backup_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-23", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-23", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-23", "metric": "supplier_critical_process_backup_pct", "label": "supplier critical-process backup",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier critical-process backup must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_regulatory_change_age_days_24(record):
    """Evaluate supplier regulatory-change age for control WP-0197-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulatory_change_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0197-24", "metric": "supplier_regulatory_change_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0197-24", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0197-24", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0197-24", "metric": "supplier_regulatory_change_age_days", "label": "supplier regulatory-change age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier regulatory-change age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_vehicle_idle_minutes_01, assess_access_violation_count_02, assess_shift_coverage_pct_03, assess_fire_drill_age_days_04, assess_proof_photo_pct_05, assess_data_logger_download_age_hours_06, assess_customer_replacement_age_hours_07, assess_dock_edge_protection_pct_08, assess_industrial_network_segmentation_pct_09, assess_domain_expiry_days_10, assess_equipment_assignment_gap_count_11, assess_movement_duplicate_count_12, assess_reserve_pick_access_pct_13, assess_dispute_resolution_days_14, assess_gate_checkout_minutes_15, assess_agency_labor_pct_16, assess_supplier_packaging_damage_pct_17, assess_supplier_change_notice_days_18, assess_supplier_shipping_window_compliance_pct_19, assess_supplier_service_availability_pct_20, assess_supplier_lot_data_completeness_pct_21, assess_supplier_site_access_review_age_days_22, assess_supplier_critical_process_backup_pct_23, assess_supplier_regulatory_change_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

