"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_single_source_sku_count_01(record):
    """Evaluate single-source SKUs for control WP-0194-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("single_source_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-01", "metric": "single_source_sku_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-01", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-01", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-01", "metric": "single_source_sku_count", "label": "single-source SKUs",
        "status": "breach", "severity": "high", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "single-source SKUs must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_cost_variance_pct_02(record):
    """Evaluate cost variance for control WP-0194-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-02", "metric": "cost_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-02", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-02", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-02", "metric": "cost_variance_pct", "label": "cost variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "cost variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_water_liters_per_order_03(record):
    """Evaluate water per order for control WP-0194-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_liters_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-03", "metric": "water_liters_per_order",
            "status": "insufficient_data",
            "severity": "low", "unit": "liters",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-03", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-03", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-03", "metric": "water_liters_per_order", "label": "water per order",
        "status": "breach", "severity": "low", "unit": "liters",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "water per order falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_regulatory_document_age_days_04(record):
    """Evaluate regulatory document age for control WP-0194-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("regulatory_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-04", "metric": "regulatory_document_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-04", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-04", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-04", "metric": "regulatory_document_age_days", "label": "regulatory document age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "regulatory document age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_consent_record_pct_05(record):
    """Evaluate consent records completeness for control WP-0194-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("consent_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-05", "metric": "consent_record_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-05", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-05", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-05", "metric": "consent_record_pct", "label": "consent records completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "consent records completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_spill_kit_check_age_days_06(record):
    """Evaluate spill-kit check age for control WP-0194-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-06", "metric": "spill_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-06", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-06", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-06", "metric": "spill_kit_check_age_days", "label": "spill-kit check age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "spill-kit check age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_delivery_attempts_07(record):
    """Evaluate delivery attempts for control WP-0194-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_attempts")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-07", "metric": "delivery_attempts",
            "status": "insufficient_data",
            "severity": "low", "unit": "attempts",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-07", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-07", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-07", "metric": "delivery_attempts", "label": "delivery attempts",
        "status": "breach", "severity": "low", "unit": "attempts",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "delivery attempts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_sensor_battery_pct_08(record):
    """Evaluate sensor battery for control WP-0194-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-08", "metric": "sensor_battery_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-08", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-08", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-08", "metric": "sensor_battery_pct", "label": "sensor battery",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sensor battery must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_repair_first_time_fix_pct_09(record):
    """Evaluate first-time fix rate for control WP-0194-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_first_time_fix_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-09", "metric": "repair_first_time_fix_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-09", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-09", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-09", "metric": "repair_first_time_fix_pct", "label": "first-time fix rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "first-time fix rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_dock_plate_inspection_age_days_10(record):
    """Evaluate dock plate inspection age for control WP-0194-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_plate_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-10", "metric": "dock_plate_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-10", "metric": "dock_plate_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-10", "metric": "dock_plate_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-10", "metric": "dock_plate_inspection_age_days", "label": "dock plate inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "dock plate inspection age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_automation_manual_override_count_11(record):
    """Evaluate manual overrides for control WP-0194-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-11", "metric": "automation_manual_override_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-11", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-11", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-11", "metric": "automation_manual_override_count", "label": "manual overrides",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "manual overrides falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_clock_drift_seconds_12(record):
    """Evaluate clock drift for control WP-0194-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("clock_drift_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-12", "metric": "clock_drift_seconds",
            "status": "insufficient_data",
            "severity": "medium", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-12", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-12", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-12", "metric": "clock_drift_seconds", "label": "clock drift",
        "status": "breach", "severity": "medium", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "clock drift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_lost_device_count_13(record):
    """Evaluate lost devices for control WP-0194-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lost_device_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-13", "metric": "lost_device_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "devices",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-13", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-13", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-13", "metric": "lost_device_count", "label": "lost devices",
        "status": "breach", "severity": "high", "unit": "devices",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lost devices must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_receipt_duplicate_count_14(record):
    """Evaluate duplicate receipts for control WP-0194-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receipt_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-14", "metric": "receipt_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "receipts",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-14", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-14", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-14", "metric": "receipt_duplicate_count", "label": "duplicate receipts",
        "status": "breach", "severity": "critical", "unit": "receipts",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "duplicate receipts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_replenishment_success_pct_15(record):
    """Evaluate replenishment success for control WP-0194-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-15", "metric": "replenishment_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-15", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-15", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-15", "metric": "replenishment_success_pct", "label": "replenishment success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "replenishment success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_payment_reconciliation_age_hours_16(record):
    """Evaluate payment reconciliation age for control WP-0194-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-16", "metric": "payment_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-16", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-16", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-16", "metric": "payment_reconciliation_age_hours", "label": "payment reconciliation age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment reconciliation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_trailer_location_age_minutes_17(record):
    """Evaluate trailer location age for control WP-0194-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_location_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-17", "metric": "trailer_location_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-17", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-17", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-17", "metric": "trailer_location_age_minutes", "label": "trailer location age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trailer location age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_damage_cost_monthly_18(record):
    """Evaluate monthly damage cost for control WP-0194-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_cost_monthly")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-18", "metric": "damage_cost_monthly",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-18", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-18", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-18", "metric": "damage_cost_monthly", "label": "monthly damage cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "monthly damage cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_short_ship_pct_19(record):
    """Evaluate supplier short-ship rate for control WP-0194-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_short_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-19", "metric": "supplier_short_ship_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-19", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-19", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-19", "metric": "supplier_short_ship_pct", "label": "supplier short-ship rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier short-ship rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_asn_timeliness_pct_20(record):
    """Evaluate supplier ASN timeliness for control WP-0194-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-20", "metric": "supplier_asn_timeliness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-20", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-20", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-20", "metric": "supplier_asn_timeliness_pct", "label": "supplier ASN timeliness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ASN timeliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_demand_signal_age_hours_21(record):
    """Evaluate supplier demand signal age for control WP-0194-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_demand_signal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-21", "metric": "supplier_demand_signal_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-21", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-21", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-21", "metric": "supplier_demand_signal_age_hours", "label": "supplier demand signal age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier demand signal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_business_owner_gap_count_22(record):
    """Evaluate supplier business-owner gaps for control WP-0194-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-22", "metric": "supplier_business_owner_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-22", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-22", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-22", "metric": "supplier_business_owner_gap_count", "label": "supplier business-owner gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier business-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_recall_response_minutes_23(record):
    """Evaluate supplier recall response time for control WP-0194-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recall_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-23", "metric": "supplier_recall_response_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-23", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-23", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-23", "metric": "supplier_recall_response_minutes", "label": "supplier recall response time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier recall response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_seismic_risk_score_24(record):
    """Evaluate supplier seismic risk for control WP-0194-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seismic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0194-24", "metric": "supplier_seismic_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0194-24", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0194-24", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0194-24", "metric": "supplier_seismic_risk_score", "label": "supplier seismic risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier seismic risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_single_source_sku_count_01, assess_cost_variance_pct_02, assess_water_liters_per_order_03, assess_regulatory_document_age_days_04, assess_consent_record_pct_05, assess_spill_kit_check_age_days_06, assess_delivery_attempts_07, assess_sensor_battery_pct_08, assess_repair_first_time_fix_pct_09, assess_dock_plate_inspection_age_days_10, assess_automation_manual_override_count_11, assess_clock_drift_seconds_12, assess_lost_device_count_13, assess_receipt_duplicate_count_14, assess_replenishment_success_pct_15, assess_payment_reconciliation_age_hours_16, assess_trailer_location_age_minutes_17, assess_damage_cost_monthly_18, assess_supplier_short_ship_pct_19, assess_supplier_asn_timeliness_pct_20, assess_supplier_demand_signal_age_hours_21, assess_supplier_business_owner_gap_count_22, assess_supplier_recall_response_minutes_23, assess_supplier_seismic_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

