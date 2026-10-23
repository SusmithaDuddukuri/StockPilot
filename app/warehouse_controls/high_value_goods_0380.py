"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_lead_days_01(record):
    """Evaluate supplier lead time for control WP-0380-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-01", "metric": "lead_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-01", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-01", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-01", "metric": "lead_days", "label": "supplier lead time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "supplier lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_carbon_kg_02(record):
    """Evaluate carbon estimate for control WP-0380-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carbon_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-02", "metric": "carbon_kg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-02", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-02", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-02", "metric": "carbon_kg", "label": "carbon estimate",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carbon estimate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_forecast_confidence_pct_03(record):
    """Evaluate forecast confidence for control WP-0380-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-03", "metric": "forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-03", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-03", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-03", "metric": "forecast_confidence_pct", "label": "forecast confidence",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forecast confidence must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_orphan_receipt_count_04(record):
    """Evaluate orphan receipts for control WP-0380-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-04", "metric": "orphan_receipt_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-04", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-04", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-04", "metric": "orphan_receipt_count", "label": "orphan receipts",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "orphan receipts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_recovery_value_pct_05(record):
    """Evaluate recovery value for control WP-0380-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_value_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-05", "metric": "recovery_value_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-05", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-05", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-05", "metric": "recovery_value_pct", "label": "recovery value",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "recovery value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_serial_mismatch_count_06(record):
    """Evaluate serial mismatches for control WP-0380-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-06", "metric": "serial_mismatch_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-06", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-06", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-06", "metric": "serial_mismatch_count", "label": "serial mismatches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_integration_failure_count_07(record):
    """Evaluate integration failures for control WP-0380-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("integration_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-07", "metric": "integration_failure_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-07", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-07", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-07", "metric": "integration_failure_count", "label": "integration failures",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "integration failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_carton_fill_pct_08(record):
    """Evaluate carton fill for control WP-0380-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carton_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-08", "metric": "carton_fill_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-08", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-08", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-08", "metric": "carton_fill_pct", "label": "carton fill",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "carton fill exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_dispute_age_days_09(record):
    """Evaluate dispute age for control WP-0380-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-09", "metric": "dispute_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-09", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-09", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-09", "metric": "dispute_age_days", "label": "dispute age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "dispute age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_reefer_fuel_remaining_pct_10(record):
    """Evaluate reefer fuel remaining for control WP-0380-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_fuel_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-10", "metric": "reefer_fuel_remaining_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-10", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-10", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-10", "metric": "reefer_fuel_remaining_pct", "label": "reefer fuel remaining",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reefer fuel remaining must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_refurbishment_yield_pct_11(record):
    """Evaluate refurbishment yield for control WP-0380-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refurbishment_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-11", "metric": "refurbishment_yield_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-11", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-11", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-11", "metric": "refurbishment_yield_pct", "label": "refurbishment yield",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "refurbishment yield must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_rack_load_variance_pct_12(record):
    """Evaluate rack load variance for control WP-0380-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rack_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-12", "metric": "rack_load_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-12", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-12", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-12", "metric": "rack_load_variance_pct", "label": "rack load variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "rack load variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_robot_pick_success_pct_13(record):
    """Evaluate robot pick success for control WP-0380-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_pick_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-13", "metric": "robot_pick_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-13", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-13", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-13", "metric": "robot_pick_success_pct", "label": "robot pick success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "robot pick success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_alert_noise_pct_14(record):
    """Evaluate alert noise rate for control WP-0380-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alert_noise_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-14", "metric": "alert_noise_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-14", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-14", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-14", "metric": "alert_noise_pct", "label": "alert noise rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "alert noise rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_scanner_firmware_age_days_15(record):
    """Evaluate scanner firmware age for control WP-0380-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_firmware_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-15", "metric": "scanner_firmware_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-15", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-15", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-15", "metric": "scanner_firmware_age_days", "label": "scanner firmware age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scanner firmware age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_contact_valid_pct_16(record):
    """Evaluate supplier contact validity for control WP-0380-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-16", "metric": "supplier_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-16", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-16", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-16", "metric": "supplier_contact_valid_pct", "label": "supplier contact validity",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "supplier contact validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_inspection_cycle_minutes_17(record):
    """Evaluate inspection cycle time for control WP-0380-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_cycle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-17", "metric": "inspection_cycle_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-17", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-17", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-17", "metric": "inspection_cycle_minutes", "label": "inspection cycle time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "inspection cycle time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_order_amendment_count_18(record):
    """Evaluate order amendments for control WP-0380-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_amendment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-18", "metric": "order_amendment_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-18", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-18", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-18", "metric": "order_amendment_count", "label": "order amendments",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order amendments must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_intermodal_transfer_delay_hours_19(record):
    """Evaluate intermodal transfer delay for control WP-0380-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("intermodal_transfer_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-19", "metric": "intermodal_transfer_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-19", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-19", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-19", "metric": "intermodal_transfer_delay_hours", "label": "intermodal transfer delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "intermodal transfer delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_warehouse_cost_per_sq_m_20(record):
    """Evaluate warehouse cost per square meter for control WP-0380-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_cost_per_sq_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-20", "metric": "warehouse_cost_per_sq_m",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-20", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-20", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-20", "metric": "warehouse_cost_per_sq_m", "label": "warehouse cost per square meter",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "warehouse cost per square meter exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_data_exchange_pct_21(record):
    """Evaluate supplier data exchange compliance for control WP-0380-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_exchange_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-21", "metric": "supplier_data_exchange_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-21", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-21", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-21", "metric": "supplier_data_exchange_pct", "label": "supplier data exchange compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier data exchange compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_backup_age_hours_22(record):
    """Evaluate supplier backup age for control WP-0380-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-22", "metric": "supplier_backup_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-22", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-22", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-22", "metric": "supplier_backup_age_hours", "label": "supplier backup age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier backup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_safety_stock_days_23(record):
    """Evaluate supplier safety stock cover for control WP-0380-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-23", "metric": "supplier_safety_stock_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-23", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-23", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-23", "metric": "supplier_safety_stock_days", "label": "supplier safety stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier safety stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_cloud_region_gap_count_24(record):
    """Evaluate supplier cloud-region gaps for control WP-0380-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cloud_region_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0380-24", "metric": "supplier_cloud_region_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0380-24", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0380-24", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0380-24", "metric": "supplier_cloud_region_gap_count", "label": "supplier cloud-region gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier cloud-region gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_lead_days_01, assess_carbon_kg_02, assess_forecast_confidence_pct_03, assess_orphan_receipt_count_04, assess_recovery_value_pct_05, assess_serial_mismatch_count_06, assess_integration_failure_count_07, assess_carton_fill_pct_08, assess_dispute_age_days_09, assess_reefer_fuel_remaining_pct_10, assess_refurbishment_yield_pct_11, assess_rack_load_variance_pct_12, assess_robot_pick_success_pct_13, assess_alert_noise_pct_14, assess_scanner_firmware_age_days_15, assess_supplier_contact_valid_pct_16, assess_inspection_cycle_minutes_17, assess_order_amendment_count_18, assess_intermodal_transfer_delay_hours_19, assess_warehouse_cost_per_sq_m_20, assess_supplier_data_exchange_pct_21, assess_supplier_backup_age_hours_22, assess_supplier_safety_stock_days_23, assess_supplier_cloud_region_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

