"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_volume_commitment_pct_01(record):
    """Evaluate supplier volume commitment for control WP-0312-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_volume_commitment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-01", "metric": "supplier_volume_commitment_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-01", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-01", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-01", "metric": "supplier_volume_commitment_pct", "label": "supplier volume commitment",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier volume commitment falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_shipping_accuracy_pct_02(record):
    """Evaluate supplier shipping accuracy for control WP-0312-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-02", "metric": "supplier_shipping_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-02", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-02", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-02", "metric": "supplier_shipping_accuracy_pct", "label": "supplier shipping accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier shipping accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_open_order_transfer_pct_03(record):
    """Evaluate open-order transfer completeness for control WP-0312-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_order_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-03", "metric": "supplier_open_order_transfer_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-03", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-03", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-03", "metric": "supplier_open_order_transfer_pct", "label": "open-order transfer completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "open-order transfer completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_lead_days_04(record):
    """Evaluate supplier lead time for control WP-0312-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-04", "metric": "lead_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-04", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-04", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-04", "metric": "lead_days", "label": "supplier lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_carbon_kg_05(record):
    """Evaluate carbon estimate for control WP-0312-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carbon_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-05", "metric": "carbon_kg",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-05", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-05", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-05", "metric": "carbon_kg", "label": "carbon estimate",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "carbon estimate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_forecast_confidence_pct_06(record):
    """Evaluate forecast confidence for control WP-0312-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-06", "metric": "forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-06", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-06", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-06", "metric": "forecast_confidence_pct", "label": "forecast confidence",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast confidence must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_orphan_receipt_count_07(record):
    """Evaluate orphan receipts for control WP-0312-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-07", "metric": "orphan_receipt_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-07", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-07", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-07", "metric": "orphan_receipt_count", "label": "orphan receipts",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "orphan receipts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_recovery_value_pct_08(record):
    """Evaluate recovery value for control WP-0312-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_value_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-08", "metric": "recovery_value_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-08", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-08", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-08", "metric": "recovery_value_pct", "label": "recovery value",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "recovery value exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_serial_mismatch_count_09(record):
    """Evaluate serial mismatches for control WP-0312-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-09", "metric": "serial_mismatch_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-09", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-09", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-09", "metric": "serial_mismatch_count", "label": "serial mismatches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "serial mismatches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_integration_failure_count_10(record):
    """Evaluate integration failures for control WP-0312-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("integration_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-10", "metric": "integration_failure_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-10", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-10", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-10", "metric": "integration_failure_count", "label": "integration failures",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "integration failures must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_carton_fill_pct_11(record):
    """Evaluate carton fill for control WP-0312-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carton_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-11", "metric": "carton_fill_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-11", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-11", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-11", "metric": "carton_fill_pct", "label": "carton fill",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carton fill must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_dispute_age_days_12(record):
    """Evaluate dispute age for control WP-0312-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-12", "metric": "dispute_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-12", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-12", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-12", "metric": "dispute_age_days", "label": "dispute age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "dispute age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_reefer_fuel_remaining_pct_13(record):
    """Evaluate reefer fuel remaining for control WP-0312-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_fuel_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-13", "metric": "reefer_fuel_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-13", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-13", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-13", "metric": "reefer_fuel_remaining_pct", "label": "reefer fuel remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "reefer fuel remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_refurbishment_yield_pct_14(record):
    """Evaluate refurbishment yield for control WP-0312-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refurbishment_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-14", "metric": "refurbishment_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-14", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-14", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-14", "metric": "refurbishment_yield_pct", "label": "refurbishment yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refurbishment yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_rack_load_variance_pct_15(record):
    """Evaluate rack load variance for control WP-0312-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rack_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-15", "metric": "rack_load_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-15", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-15", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-15", "metric": "rack_load_variance_pct", "label": "rack load variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "rack load variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_robot_pick_success_pct_16(record):
    """Evaluate robot pick success for control WP-0312-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_pick_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-16", "metric": "robot_pick_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-16", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-16", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-16", "metric": "robot_pick_success_pct", "label": "robot pick success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "robot pick success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_alert_noise_pct_17(record):
    """Evaluate alert noise rate for control WP-0312-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alert_noise_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-17", "metric": "alert_noise_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-17", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-17", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-17", "metric": "alert_noise_pct", "label": "alert noise rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "alert noise rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_scanner_firmware_age_days_18(record):
    """Evaluate scanner firmware age for control WP-0312-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_firmware_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-18", "metric": "scanner_firmware_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-18", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-18", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-18", "metric": "scanner_firmware_age_days", "label": "scanner firmware age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner firmware age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_contact_valid_pct_19(record):
    """Evaluate supplier contact validity for control WP-0312-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-19", "metric": "supplier_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-19", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-19", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-19", "metric": "supplier_contact_valid_pct", "label": "supplier contact validity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contact validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_inspection_cycle_minutes_20(record):
    """Evaluate inspection cycle time for control WP-0312-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_cycle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-20", "metric": "inspection_cycle_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-20", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-20", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-20", "metric": "inspection_cycle_minutes", "label": "inspection cycle time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "inspection cycle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_order_amendment_count_21(record):
    """Evaluate order amendments for control WP-0312-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_amendment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-21", "metric": "order_amendment_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-21", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-21", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-21", "metric": "order_amendment_count", "label": "order amendments",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "order amendments falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_intermodal_transfer_delay_hours_22(record):
    """Evaluate intermodal transfer delay for control WP-0312-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("intermodal_transfer_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-22", "metric": "intermodal_transfer_delay_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-22", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-22", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-22", "metric": "intermodal_transfer_delay_hours", "label": "intermodal transfer delay",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "intermodal transfer delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_warehouse_cost_per_sq_m_23(record):
    """Evaluate warehouse cost per square meter for control WP-0312-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_cost_per_sq_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-23", "metric": "warehouse_cost_per_sq_m",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-23", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-23", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-23", "metric": "warehouse_cost_per_sq_m", "label": "warehouse cost per square meter",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "warehouse cost per square meter must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_data_exchange_pct_24(record):
    """Evaluate supplier data exchange compliance for control WP-0312-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_exchange_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0312-24", "metric": "supplier_data_exchange_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0312-24", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0312-24", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0312-24", "metric": "supplier_data_exchange_pct", "label": "supplier data exchange compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier data exchange compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_volume_commitment_pct_01, assess_supplier_shipping_accuracy_pct_02, assess_supplier_open_order_transfer_pct_03, assess_lead_days_04, assess_carbon_kg_05, assess_forecast_confidence_pct_06, assess_orphan_receipt_count_07, assess_recovery_value_pct_08, assess_serial_mismatch_count_09, assess_integration_failure_count_10, assess_carton_fill_pct_11, assess_dispute_age_days_12, assess_reefer_fuel_remaining_pct_13, assess_refurbishment_yield_pct_14, assess_rack_load_variance_pct_15, assess_robot_pick_success_pct_16, assess_alert_noise_pct_17, assess_scanner_firmware_age_days_18, assess_supplier_contact_valid_pct_19, assess_inspection_cycle_minutes_20, assess_order_amendment_count_21, assess_intermodal_transfer_delay_hours_22, assess_warehouse_cost_per_sq_m_23, assess_supplier_data_exchange_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

