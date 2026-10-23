"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_dock_edge_protection_pct_01(record):
    """Evaluate dock edge protection for control WP-0209-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-01", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-01", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-01", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-01", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "dock edge protection exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_industrial_network_segmentation_pct_02(record):
    """Evaluate industrial network segmentation for control WP-0209-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-02", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-02", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-02", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-02", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "industrial network segmentation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_domain_expiry_days_03(record):
    """Evaluate domain validity for control WP-0209-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-03", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-03", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-03", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-03", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "domain validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_equipment_assignment_gap_count_04(record):
    """Evaluate equipment assignment gaps for control WP-0209-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-04", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-04", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-04", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-04", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment assignment gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_movement_duplicate_count_05(record):
    """Evaluate duplicate movements for control WP-0209-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("movement_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-05", "metric": "movement_duplicate_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "movements",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-05", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-05", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-05", "metric": "movement_duplicate_count", "label": "duplicate movements",
        "status": "breach", "severity": "medium", "unit": "movements",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "duplicate movements exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_reserve_pick_access_pct_06(record):
    """Evaluate reserve-pick access for control WP-0209-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserve_pick_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-06", "metric": "reserve_pick_access_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-06", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-06", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-06", "metric": "reserve_pick_access_pct", "label": "reserve-pick access",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "reserve-pick access falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_dispute_resolution_days_07(record):
    """Evaluate dispute resolution time for control WP-0209-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_resolution_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-07", "metric": "dispute_resolution_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-07", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-07", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-07", "metric": "dispute_resolution_days", "label": "dispute resolution time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dispute resolution time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_gate_checkout_minutes_08(record):
    """Evaluate gate check-out time for control WP-0209-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkout_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-08", "metric": "gate_checkout_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-08", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-08", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-08", "metric": "gate_checkout_minutes", "label": "gate check-out time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "gate check-out time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_agency_labor_pct_09(record):
    """Evaluate agency labor share for control WP-0209-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("agency_labor_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-09", "metric": "agency_labor_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-09", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-09", "metric": "agency_labor_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-09", "metric": "agency_labor_pct", "label": "agency labor share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "agency labor share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_packaging_damage_pct_10(record):
    """Evaluate supplier packaging damage for control WP-0209-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-10", "metric": "supplier_packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-10", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-10", "metric": "supplier_packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-10", "metric": "supplier_packaging_damage_pct", "label": "supplier packaging damage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier packaging damage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_change_notice_days_11(record):
    """Evaluate supplier change notice for control WP-0209-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-11", "metric": "supplier_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-11", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-11", "metric": "supplier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-11", "metric": "supplier_change_notice_days", "label": "supplier change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_shipping_window_compliance_pct_12(record):
    """Evaluate supplier shipping-window compliance for control WP-0209-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_window_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-12", "metric": "supplier_shipping_window_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-12", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-12", "metric": "supplier_shipping_window_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-12", "metric": "supplier_shipping_window_compliance_pct", "label": "supplier shipping-window compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier shipping-window compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_service_availability_pct_13(record):
    """Evaluate supplier service availability for control WP-0209-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-13", "metric": "supplier_service_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-13", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-13", "metric": "supplier_service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-13", "metric": "supplier_service_availability_pct", "label": "supplier service availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier service availability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_lot_data_completeness_pct_14(record):
    """Evaluate supplier lot-data completeness for control WP-0209-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lot_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-14", "metric": "supplier_lot_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-14", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-14", "metric": "supplier_lot_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-14", "metric": "supplier_lot_data_completeness_pct", "label": "supplier lot-data completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier lot-data completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_site_access_review_age_days_15(record):
    """Evaluate supplier site access review age for control WP-0209-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-15", "metric": "supplier_site_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-15", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-15", "metric": "supplier_site_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-15", "metric": "supplier_site_access_review_age_days", "label": "supplier site access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier site access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_critical_process_backup_pct_16(record):
    """Evaluate supplier critical-process backup for control WP-0209-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_process_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-16", "metric": "supplier_critical_process_backup_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-16", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-16", "metric": "supplier_critical_process_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-16", "metric": "supplier_critical_process_backup_pct", "label": "supplier critical-process backup",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier critical-process backup must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_regulatory_change_age_days_17(record):
    """Evaluate supplier regulatory-change age for control WP-0209-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulatory_change_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-17", "metric": "supplier_regulatory_change_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-17", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-17", "metric": "supplier_regulatory_change_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-17", "metric": "supplier_regulatory_change_age_days", "label": "supplier regulatory-change age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier regulatory-change age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_tax_transparency_score_18(record):
    """Evaluate supplier tax transparency for control WP-0209-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_transparency_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-18", "metric": "supplier_tax_transparency_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-18", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-18", "metric": "supplier_tax_transparency_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-18", "metric": "supplier_tax_transparency_score", "label": "supplier tax transparency",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "supplier tax transparency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_alternate_logistics_pct_19(record):
    """Evaluate supplier alternate logistics coverage for control WP-0209-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_logistics_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-19", "metric": "supplier_alternate_logistics_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-19", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-19", "metric": "supplier_alternate_logistics_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-19", "metric": "supplier_alternate_logistics_pct", "label": "supplier alternate logistics coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier alternate logistics coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_predictive_maintenance_pct_20(record):
    """Evaluate supplier predictive maintenance for control WP-0209-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_predictive_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-20", "metric": "supplier_predictive_maintenance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-20", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-20", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-20", "metric": "supplier_predictive_maintenance_pct", "label": "supplier predictive maintenance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier predictive maintenance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_label_quality_score_21(record):
    """Evaluate supplier label quality for control WP-0209-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-21", "metric": "supplier_label_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-21", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-21", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-21", "metric": "supplier_label_quality_score", "label": "supplier label quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier label quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_multi_region_coverage_pct_22(record):
    """Evaluate supplier multi-region coverage for control WP-0209-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_multi_region_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-22", "metric": "supplier_multi_region_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-22", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-22", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-22", "metric": "supplier_multi_region_coverage_pct", "label": "supplier multi-region coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier multi-region coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_privacy_impact_age_days_23(record):
    """Evaluate supplier privacy impact assessment age for control WP-0209-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_impact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-23", "metric": "supplier_privacy_impact_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-23", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-23", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-23", "metric": "supplier_privacy_impact_age_days", "label": "supplier privacy impact assessment age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy impact assessment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_residual_risk_score_24(record):
    """Evaluate supplier residual risk for control WP-0209-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_residual_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0209-24", "metric": "supplier_residual_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0209-24", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0209-24", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0209-24", "metric": "supplier_residual_risk_score", "label": "supplier residual risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier residual risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_dock_edge_protection_pct_01, assess_industrial_network_segmentation_pct_02, assess_domain_expiry_days_03, assess_equipment_assignment_gap_count_04, assess_movement_duplicate_count_05, assess_reserve_pick_access_pct_06, assess_dispute_resolution_days_07, assess_gate_checkout_minutes_08, assess_agency_labor_pct_09, assess_supplier_packaging_damage_pct_10, assess_supplier_change_notice_days_11, assess_supplier_shipping_window_compliance_pct_12, assess_supplier_service_availability_pct_13, assess_supplier_lot_data_completeness_pct_14, assess_supplier_site_access_review_age_days_15, assess_supplier_critical_process_backup_pct_16, assess_supplier_regulatory_change_age_days_17, assess_supplier_tax_transparency_score_18, assess_supplier_alternate_logistics_pct_19, assess_supplier_predictive_maintenance_pct_20, assess_supplier_label_quality_score_21, assess_supplier_multi_region_coverage_pct_22, assess_supplier_privacy_impact_age_days_23, assess_supplier_residual_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

