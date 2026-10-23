"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_capacity_allocation_pct_01(record):
    """Evaluate supplier capacity allocation for control WP-0692-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_allocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-01", "metric": "supplier_capacity_allocation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-01", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-01", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-01", "metric": "supplier_capacity_allocation_pct", "label": "supplier capacity allocation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier capacity allocation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_carrier_handoff_pct_02(record):
    """Evaluate supplier carrier handoff for control WP-0692-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carrier_handoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-02", "metric": "supplier_carrier_handoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-02", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-02", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-02", "metric": "supplier_carrier_handoff_pct", "label": "supplier carrier handoff",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier carrier handoff must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_asset_transfer_match_pct_03(record):
    """Evaluate asset transfer match for control WP-0692-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-03", "metric": "supplier_asset_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-03", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-03", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-03", "metric": "supplier_asset_transfer_match_pct", "label": "asset transfer match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "asset transfer match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_capacity_units_04(record):
    """Evaluate storage capacity for control WP-0692-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capacity_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-04", "metric": "capacity_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-04", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-04", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-04", "metric": "capacity_units", "label": "storage capacity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "storage capacity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_mis_pick_count_05(record):
    """Evaluate mis-picks for control WP-0692-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mis_pick_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-05", "metric": "mis_pick_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-05", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-05", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-05", "metric": "mis_pick_count", "label": "mis-picks",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "mis-picks falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_single_source_sku_count_06(record):
    """Evaluate single-source SKUs for control WP-0692-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("single_source_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-06", "metric": "single_source_sku_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-06", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-06", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-06", "metric": "single_source_sku_count", "label": "single-source SKUs",
        "status": "breach", "severity": "medium", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "single-source SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_cost_variance_pct_07(record):
    """Evaluate cost variance for control WP-0692-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-07", "metric": "cost_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-07", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-07", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-07", "metric": "cost_variance_pct", "label": "cost variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cost variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_water_liters_per_order_08(record):
    """Evaluate water per order for control WP-0692-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_liters_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-08", "metric": "water_liters_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "liters",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-08", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-08", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-08", "metric": "water_liters_per_order", "label": "water per order",
        "status": "breach", "severity": "critical", "unit": "liters",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "water per order exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_regulatory_document_age_days_09(record):
    """Evaluate regulatory document age for control WP-0692-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("regulatory_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-09", "metric": "regulatory_document_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-09", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-09", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-09", "metric": "regulatory_document_age_days", "label": "regulatory document age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "regulatory document age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_consent_record_pct_10(record):
    """Evaluate consent records completeness for control WP-0692-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("consent_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-10", "metric": "consent_record_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-10", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-10", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-10", "metric": "consent_record_pct", "label": "consent records completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "consent records completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_spill_kit_check_age_days_11(record):
    """Evaluate spill-kit check age for control WP-0692-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-11", "metric": "spill_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-11", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-11", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-11", "metric": "spill_kit_check_age_days", "label": "spill-kit check age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "spill-kit check age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_delivery_attempts_12(record):
    """Evaluate delivery attempts for control WP-0692-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_attempts")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-12", "metric": "delivery_attempts",
            "status": "insufficient_data",
            "severity": "critical", "unit": "attempts",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-12", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-12", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-12", "metric": "delivery_attempts", "label": "delivery attempts",
        "status": "breach", "severity": "critical", "unit": "attempts",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "delivery attempts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_sensor_battery_pct_13(record):
    """Evaluate sensor battery for control WP-0692-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-13", "metric": "sensor_battery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-13", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-13", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-13", "metric": "sensor_battery_pct", "label": "sensor battery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "sensor battery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_repair_first_time_fix_pct_14(record):
    """Evaluate first-time fix rate for control WP-0692-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_first_time_fix_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-14", "metric": "repair_first_time_fix_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-14", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-14", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-14", "metric": "repair_first_time_fix_pct", "label": "first-time fix rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "first-time fix rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_dock_plate_inspection_age_days_15(record):
    """Evaluate dock plate inspection age for control WP-0692-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_plate_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-15", "metric": "dock_plate_inspection_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-15", "metric": "dock_plate_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-15", "metric": "dock_plate_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-15", "metric": "dock_plate_inspection_age_days", "label": "dock plate inspection age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock plate inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_automation_manual_override_count_16(record):
    """Evaluate manual overrides for control WP-0692-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-16", "metric": "automation_manual_override_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-16", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-16", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-16", "metric": "automation_manual_override_count", "label": "manual overrides",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "manual overrides exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_clock_drift_seconds_17(record):
    """Evaluate clock drift for control WP-0692-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("clock_drift_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-17", "metric": "clock_drift_seconds",
            "status": "insufficient_data",
            "severity": "low", "unit": "seconds",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-17", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-17", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-17", "metric": "clock_drift_seconds", "label": "clock drift",
        "status": "breach", "severity": "low", "unit": "seconds",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "clock drift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_lost_device_count_18(record):
    """Evaluate lost devices for control WP-0692-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lost_device_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-18", "metric": "lost_device_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "devices",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-18", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-18", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-18", "metric": "lost_device_count", "label": "lost devices",
        "status": "breach", "severity": "medium", "unit": "devices",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lost devices must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_receipt_duplicate_count_19(record):
    """Evaluate duplicate receipts for control WP-0692-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receipt_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-19", "metric": "receipt_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "receipts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-19", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-19", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-19", "metric": "receipt_duplicate_count", "label": "duplicate receipts",
        "status": "breach", "severity": "high", "unit": "receipts",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate receipts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_replenishment_success_pct_20(record):
    """Evaluate replenishment success for control WP-0692-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-20", "metric": "replenishment_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-20", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-20", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-20", "metric": "replenishment_success_pct", "label": "replenishment success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "replenishment success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_payment_reconciliation_age_hours_21(record):
    """Evaluate payment reconciliation age for control WP-0692-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-21", "metric": "payment_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-21", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-21", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-21", "metric": "payment_reconciliation_age_hours", "label": "payment reconciliation age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "payment reconciliation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_trailer_location_age_minutes_22(record):
    """Evaluate trailer location age for control WP-0692-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_location_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-22", "metric": "trailer_location_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-22", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-22", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-22", "metric": "trailer_location_age_minutes", "label": "trailer location age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trailer location age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_damage_cost_monthly_23(record):
    """Evaluate monthly damage cost for control WP-0692-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_cost_monthly")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-23", "metric": "damage_cost_monthly",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-23", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-23", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-23", "metric": "damage_cost_monthly", "label": "monthly damage cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "monthly damage cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_short_ship_pct_24(record):
    """Evaluate supplier short-ship rate for control WP-0692-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_short_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0692-24", "metric": "supplier_short_ship_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0692-24", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0692-24", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0692-24", "metric": "supplier_short_ship_pct", "label": "supplier short-ship rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier short-ship rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_capacity_allocation_pct_01, assess_supplier_carrier_handoff_pct_02, assess_supplier_asset_transfer_match_pct_03, assess_capacity_units_04, assess_mis_pick_count_05, assess_single_source_sku_count_06, assess_cost_variance_pct_07, assess_water_liters_per_order_08, assess_regulatory_document_age_days_09, assess_consent_record_pct_10, assess_spill_kit_check_age_days_11, assess_delivery_attempts_12, assess_sensor_battery_pct_13, assess_repair_first_time_fix_pct_14, assess_dock_plate_inspection_age_days_15, assess_automation_manual_override_count_16, assess_clock_drift_seconds_17, assess_lost_device_count_18, assess_receipt_duplicate_count_19, assess_replenishment_success_pct_20, assess_payment_reconciliation_age_hours_21, assess_trailer_location_age_minutes_22, assess_damage_cost_monthly_23, assess_supplier_short_ship_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

