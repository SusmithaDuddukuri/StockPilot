"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_integration_failure_count_01(record):
    """Evaluate integration failures for control WP-0137-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("integration_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-01", "metric": "integration_failure_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-01", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-01", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-01", "metric": "integration_failure_count", "label": "integration failures",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "integration failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_carton_fill_pct_02(record):
    """Evaluate carton fill for control WP-0137-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carton_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-02", "metric": "carton_fill_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-02", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-02", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-02", "metric": "carton_fill_pct", "label": "carton fill",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "carton fill falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_dispute_age_days_03(record):
    """Evaluate dispute age for control WP-0137-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-03", "metric": "dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-03", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-03", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-03", "metric": "dispute_age_days", "label": "dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dispute age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_reefer_fuel_remaining_pct_04(record):
    """Evaluate reefer fuel remaining for control WP-0137-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_fuel_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-04", "metric": "reefer_fuel_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-04", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-04", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-04", "metric": "reefer_fuel_remaining_pct", "label": "reefer fuel remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reefer fuel remaining must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_refurbishment_yield_pct_05(record):
    """Evaluate refurbishment yield for control WP-0137-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refurbishment_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-05", "metric": "refurbishment_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-05", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-05", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-05", "metric": "refurbishment_yield_pct", "label": "refurbishment yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "refurbishment yield exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_rack_load_variance_pct_06(record):
    """Evaluate rack load variance for control WP-0137-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rack_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-06", "metric": "rack_load_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-06", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-06", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-06", "metric": "rack_load_variance_pct", "label": "rack load variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "rack load variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_robot_pick_success_pct_07(record):
    """Evaluate robot pick success for control WP-0137-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_pick_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-07", "metric": "robot_pick_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-07", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-07", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-07", "metric": "robot_pick_success_pct", "label": "robot pick success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "robot pick success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_alert_noise_pct_08(record):
    """Evaluate alert noise rate for control WP-0137-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alert_noise_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-08", "metric": "alert_noise_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-08", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-08", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-08", "metric": "alert_noise_pct", "label": "alert noise rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "alert noise rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_scanner_firmware_age_days_09(record):
    """Evaluate scanner firmware age for control WP-0137-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_firmware_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-09", "metric": "scanner_firmware_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-09", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-09", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-09", "metric": "scanner_firmware_age_days", "label": "scanner firmware age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "scanner firmware age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_contact_valid_pct_10(record):
    """Evaluate supplier contact validity for control WP-0137-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-10", "metric": "supplier_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-10", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-10", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-10", "metric": "supplier_contact_valid_pct", "label": "supplier contact validity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier contact validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_inspection_cycle_minutes_11(record):
    """Evaluate inspection cycle time for control WP-0137-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_cycle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-11", "metric": "inspection_cycle_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-11", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-11", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-11", "metric": "inspection_cycle_minutes", "label": "inspection cycle time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inspection cycle time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_order_amendment_count_12(record):
    """Evaluate order amendments for control WP-0137-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_amendment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-12", "metric": "order_amendment_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-12", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-12", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-12", "metric": "order_amendment_count", "label": "order amendments",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order amendments must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_intermodal_transfer_delay_hours_13(record):
    """Evaluate intermodal transfer delay for control WP-0137-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("intermodal_transfer_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-13", "metric": "intermodal_transfer_delay_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-13", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-13", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-13", "metric": "intermodal_transfer_delay_hours", "label": "intermodal transfer delay",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "intermodal transfer delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_warehouse_cost_per_sq_m_14(record):
    """Evaluate warehouse cost per square meter for control WP-0137-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_cost_per_sq_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-14", "metric": "warehouse_cost_per_sq_m",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-14", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-14", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-14", "metric": "warehouse_cost_per_sq_m", "label": "warehouse cost per square meter",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "warehouse cost per square meter falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_data_exchange_pct_15(record):
    """Evaluate supplier data exchange compliance for control WP-0137-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_exchange_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-15", "metric": "supplier_data_exchange_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-15", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-15", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-15", "metric": "supplier_data_exchange_pct", "label": "supplier data exchange compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data exchange compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_backup_age_hours_16(record):
    """Evaluate supplier backup age for control WP-0137-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-16", "metric": "supplier_backup_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-16", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-16", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-16", "metric": "supplier_backup_age_hours", "label": "supplier backup age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier backup age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_safety_stock_days_17(record):
    """Evaluate supplier safety stock cover for control WP-0137-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-17", "metric": "supplier_safety_stock_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-17", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-17", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-17", "metric": "supplier_safety_stock_days", "label": "supplier safety stock cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier safety stock cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_cloud_region_gap_count_18(record):
    """Evaluate supplier cloud-region gaps for control WP-0137-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cloud_region_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-18", "metric": "supplier_cloud_region_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-18", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-18", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-18", "metric": "supplier_cloud_region_gap_count", "label": "supplier cloud-region gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier cloud-region gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_transport_alternative_count_19(record):
    """Evaluate supplier transport alternatives for control WP-0137-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transport_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-19", "metric": "supplier_transport_alternative_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "routes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-19", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-19", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-19", "metric": "supplier_transport_alternative_count", "label": "supplier transport alternatives",
        "status": "breach", "severity": "critical", "unit": "routes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transport alternatives must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_adaptation_score_20(record):
    """Evaluate supplier climate adaptation for control WP-0137-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adaptation_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-20", "metric": "supplier_adaptation_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-20", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-20", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-20", "metric": "supplier_adaptation_score", "label": "supplier climate adaptation",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier climate adaptation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_crisis_drill_age_days_21(record):
    """Evaluate supplier crisis drill age for control WP-0137-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-21", "metric": "supplier_crisis_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-21", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-21", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-21", "metric": "supplier_crisis_drill_age_days", "label": "supplier crisis drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier crisis drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_audit_finding_age_days_22(record):
    """Evaluate supplier audit-finding age for control WP-0137-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_finding_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-22", "metric": "supplier_audit_finding_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-22", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-22", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-22", "metric": "supplier_audit_finding_age_days", "label": "supplier audit-finding age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier audit-finding age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_diversity_score_23(record):
    """Evaluate supplier diversity score for control WP-0137-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_diversity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-23", "metric": "supplier_diversity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-23", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-23", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-23", "metric": "supplier_diversity_score", "label": "supplier diversity score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier diversity score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_disaster_exposure_score_24(record):
    """Evaluate supplier disaster exposure for control WP-0137-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disaster_exposure_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0137-24", "metric": "supplier_disaster_exposure_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0137-24", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0137-24", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0137-24", "metric": "supplier_disaster_exposure_score", "label": "supplier disaster exposure",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier disaster exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_integration_failure_count_01, assess_carton_fill_pct_02, assess_dispute_age_days_03, assess_reefer_fuel_remaining_pct_04, assess_refurbishment_yield_pct_05, assess_rack_load_variance_pct_06, assess_robot_pick_success_pct_07, assess_alert_noise_pct_08, assess_scanner_firmware_age_days_09, assess_supplier_contact_valid_pct_10, assess_inspection_cycle_minutes_11, assess_order_amendment_count_12, assess_intermodal_transfer_delay_hours_13, assess_warehouse_cost_per_sq_m_14, assess_supplier_data_exchange_pct_15, assess_supplier_backup_age_hours_16, assess_supplier_safety_stock_days_17, assess_supplier_cloud_region_gap_count_18, assess_supplier_transport_alternative_count_19, assess_supplier_adaptation_score_20, assess_supplier_crisis_drill_age_days_21, assess_supplier_audit_finding_age_days_22, assess_supplier_diversity_score_23, assess_supplier_disaster_exposure_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

