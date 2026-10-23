"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_human_override_pct_01(record):
    """Evaluate supplier human override rate for control WP-0557-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_override_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-01", "metric": "supplier_human_override_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-01", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-01", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-01", "metric": "supplier_human_override_pct", "label": "supplier human override rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier human override rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_idempotency_violation_count_02(record):
    """Evaluate supplier idempotency violations for control WP-0557-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_idempotency_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-02", "metric": "supplier_idempotency_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-02", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-02", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-02", "metric": "supplier_idempotency_violation_count", "label": "supplier idempotency violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier idempotency violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_threat_model_age_days_03(record):
    """Evaluate supplier threat-model age for control WP-0557-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_threat_model_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-03", "metric": "supplier_threat_model_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-03", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-03", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-03", "metric": "supplier_threat_model_age_days", "label": "supplier threat-model age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier threat-model age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_screen_lock_pct_04(record):
    """Evaluate supplier screen-lock compliance for control WP-0557-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_screen_lock_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-04", "metric": "supplier_screen_lock_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-04", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-04", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-04", "metric": "supplier_screen_lock_pct", "label": "supplier screen-lock compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier screen-lock compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_manual_override_count_05(record):
    """Evaluate supplier manual overrides for control WP-0557-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-05", "metric": "supplier_manual_override_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-05", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-05", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-05", "metric": "supplier_manual_override_count", "label": "supplier manual overrides",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier manual overrides exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_forecast_commitment_accuracy_pct_06(record):
    """Evaluate forecast commitment accuracy for control WP-0557-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_commitment_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-06", "metric": "supplier_forecast_commitment_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-06", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-06", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-06", "metric": "supplier_forecast_commitment_accuracy_pct", "label": "forecast commitment accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "forecast commitment accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dispatch_accuracy_pct_07(record):
    """Evaluate supplier dispatch accuracy for control WP-0557-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-07", "metric": "supplier_dispatch_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-07", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-07", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-07", "metric": "supplier_dispatch_accuracy_pct", "label": "supplier dispatch accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dispatch accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_inventory_transfer_match_pct_08(record):
    """Evaluate inventory transfer match for control WP-0557-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-08", "metric": "supplier_inventory_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-08", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-08", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-08", "metric": "supplier_inventory_transfer_match_pct", "label": "inventory transfer match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory transfer match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_inventory_value_09(record):
    """Evaluate inventory value for control WP-0557-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-09", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-09", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-09", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-09", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "inventory value exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_label_error_count_10(record):
    """Evaluate label errors for control WP-0557-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-10", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-10", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-10", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-10", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "label errors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_concentration_pct_11(record):
    """Evaluate supplier concentration for control WP-0557-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-11", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-11", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-11", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-11", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier concentration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_invoice_match_pct_12(record):
    """Evaluate invoice match rate for control WP-0557-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-12", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-12", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-12", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-12", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "invoice match rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_energy_kwh_per_order_13(record):
    """Evaluate energy per order for control WP-0557-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-13", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kWh",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-13", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-13", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-13", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "medium", "unit": "kWh",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "energy per order exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_batch_recall_trace_minutes_14(record):
    """Evaluate recall trace time for control WP-0557-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-14", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-14", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-14", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-14", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "recall trace time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_data_retention_age_days_15(record):
    """Evaluate data retention age for control WP-0557-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-15", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-15", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-15", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-15", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data retention age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_hazmat_manifest_pct_16(record):
    """Evaluate hazmat manifest completion for control WP-0557-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-16", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-16", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-16", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-16", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "hazmat manifest completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_address_correction_count_17(record):
    """Evaluate address corrections for control WP-0557-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-17", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-17", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-17", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-17", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "address corrections exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_insulated_container_age_days_18(record):
    """Evaluate insulated container age for control WP-0557-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-18", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-18", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-18", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-18", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "insulated container age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_technician_utilization_pct_19(record):
    """Evaluate technician utilization for control WP-0557-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-19", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-19", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-19", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-19", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "technician utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_egress_route_obstruction_count_20(record):
    """Evaluate egress route obstructions for control WP-0557-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-20", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-20", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-20", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-20", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "egress route obstructions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_charging_dwell_minutes_21(record):
    """Evaluate charging dwell for control WP-0557-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charging_dwell_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-21", "metric": "charging_dwell_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-21", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-21", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-21", "metric": "charging_dwell_minutes", "label": "charging dwell",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "charging dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_log_integrity_pct_22(record):
    """Evaluate log integrity for control WP-0557-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-22", "metric": "log_integrity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-22", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-22", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-22", "metric": "log_integrity_pct", "label": "log integrity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "log integrity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_remote_wipe_test_age_days_23(record):
    """Evaluate remote wipe test age for control WP-0557-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-23", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-23", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-23", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-23", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "remote wipe test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_shipment_duplicate_count_24(record):
    """Evaluate duplicate shipments for control WP-0557-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0557-24", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "shipments",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0557-24", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0557-24", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0557-24", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "low", "unit": "shipments",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate shipments must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_human_override_pct_01, assess_supplier_idempotency_violation_count_02, assess_supplier_threat_model_age_days_03, assess_supplier_screen_lock_pct_04, assess_supplier_manual_override_count_05, assess_supplier_forecast_commitment_accuracy_pct_06, assess_supplier_dispatch_accuracy_pct_07, assess_supplier_inventory_transfer_match_pct_08, assess_inventory_value_09, assess_label_error_count_10, assess_supplier_concentration_pct_11, assess_invoice_match_pct_12, assess_energy_kwh_per_order_13, assess_batch_recall_trace_minutes_14, assess_data_retention_age_days_15, assess_hazmat_manifest_pct_16, assess_address_correction_count_17, assess_insulated_container_age_days_18, assess_technician_utilization_pct_19, assess_egress_route_obstruction_count_20, assess_charging_dwell_minutes_21, assess_log_integrity_pct_22, assess_remote_wipe_test_age_days_23, assess_shipment_duplicate_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

