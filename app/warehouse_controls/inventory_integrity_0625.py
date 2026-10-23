"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_screen_lock_pct_01(record):
    """Evaluate supplier screen-lock compliance for control WP-0625-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_screen_lock_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-01", "metric": "supplier_screen_lock_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-01", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-01", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-01", "metric": "supplier_screen_lock_pct", "label": "supplier screen-lock compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier screen-lock compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_manual_override_count_02(record):
    """Evaluate supplier manual overrides for control WP-0625-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-02", "metric": "supplier_manual_override_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-02", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-02", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-02", "metric": "supplier_manual_override_count", "label": "supplier manual overrides",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "supplier manual overrides falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_forecast_commitment_accuracy_pct_03(record):
    """Evaluate forecast commitment accuracy for control WP-0625-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_commitment_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-03", "metric": "supplier_forecast_commitment_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-03", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-03", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-03", "metric": "supplier_forecast_commitment_accuracy_pct", "label": "forecast commitment accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast commitment accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_dispatch_accuracy_pct_04(record):
    """Evaluate supplier dispatch accuracy for control WP-0625-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-04", "metric": "supplier_dispatch_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-04", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-04", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-04", "metric": "supplier_dispatch_accuracy_pct", "label": "supplier dispatch accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dispatch accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_inventory_transfer_match_pct_05(record):
    """Evaluate inventory transfer match for control WP-0625-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-05", "metric": "supplier_inventory_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-05", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-05", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-05", "metric": "supplier_inventory_transfer_match_pct", "label": "inventory transfer match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "inventory transfer match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_inventory_value_06(record):
    """Evaluate inventory value for control WP-0625-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-06", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-06", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-06", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-06", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "inventory value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_label_error_count_07(record):
    """Evaluate label errors for control WP-0625-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-07", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-07", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-07", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-07", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "label errors must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_concentration_pct_08(record):
    """Evaluate supplier concentration for control WP-0625-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-08", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-08", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-08", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-08", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier concentration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_invoice_match_pct_09(record):
    """Evaluate invoice match rate for control WP-0625-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-09", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-09", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-09", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-09", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "invoice match rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_energy_kwh_per_order_10(record):
    """Evaluate energy per order for control WP-0625-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-10", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "high", "unit": "kWh",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-10", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-10", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-10", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "high", "unit": "kWh",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "energy per order falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_batch_recall_trace_minutes_11(record):
    """Evaluate recall trace time for control WP-0625-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-11", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-11", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-11", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-11", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recall trace time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_data_retention_age_days_12(record):
    """Evaluate data retention age for control WP-0625-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-12", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-12", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-12", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-12", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data retention age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_hazmat_manifest_pct_13(record):
    """Evaluate hazmat manifest completion for control WP-0625-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-13", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-13", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-13", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-13", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "hazmat manifest completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_address_correction_count_14(record):
    """Evaluate address corrections for control WP-0625-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-14", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-14", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-14", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-14", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "address corrections falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_insulated_container_age_days_15(record):
    """Evaluate insulated container age for control WP-0625-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-15", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-15", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-15", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-15", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insulated container age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_technician_utilization_pct_16(record):
    """Evaluate technician utilization for control WP-0625-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-16", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-16", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-16", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-16", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "technician utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_egress_route_obstruction_count_17(record):
    """Evaluate egress route obstructions for control WP-0625-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-17", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-17", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-17", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-17", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "egress route obstructions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_charging_dwell_minutes_18(record):
    """Evaluate charging dwell for control WP-0625-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charging_dwell_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-18", "metric": "charging_dwell_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-18", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-18", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-18", "metric": "charging_dwell_minutes", "label": "charging dwell",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "charging dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_log_integrity_pct_19(record):
    """Evaluate log integrity for control WP-0625-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-19", "metric": "log_integrity_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-19", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-19", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-19", "metric": "log_integrity_pct", "label": "log integrity",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "log integrity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_remote_wipe_test_age_days_20(record):
    """Evaluate remote wipe test age for control WP-0625-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-20", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-20", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-20", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-20", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "remote wipe test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_shipment_duplicate_count_21(record):
    """Evaluate duplicate shipments for control WP-0625-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-21", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "shipments",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-21", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-21", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-21", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "medium", "unit": "shipments",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "duplicate shipments exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_replenishment_task_queue_22(record):
    """Evaluate replenishment task queue for control WP-0625-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-22", "metric": "replenishment_task_queue",
            "status": "insufficient_data",
            "severity": "high", "unit": "tasks",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-22", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-22", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-22", "metric": "replenishment_task_queue", "label": "replenishment task queue",
        "status": "breach", "severity": "high", "unit": "tasks",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "replenishment task queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_payment_capture_success_pct_23(record):
    """Evaluate payment capture success for control WP-0625-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_capture_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-23", "metric": "payment_capture_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-23", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-23", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-23", "metric": "payment_capture_success_pct", "label": "payment capture success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment capture success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_yard_spot_accuracy_pct_24(record):
    """Evaluate yard spot accuracy for control WP-0625-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_spot_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0625-24", "metric": "yard_spot_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0625-24", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0625-24", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0625-24", "metric": "yard_spot_accuracy_pct", "label": "yard spot accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "yard spot accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_screen_lock_pct_01, assess_supplier_manual_override_count_02, assess_supplier_forecast_commitment_accuracy_pct_03, assess_supplier_dispatch_accuracy_pct_04, assess_supplier_inventory_transfer_match_pct_05, assess_inventory_value_06, assess_label_error_count_07, assess_supplier_concentration_pct_08, assess_invoice_match_pct_09, assess_energy_kwh_per_order_10, assess_batch_recall_trace_minutes_11, assess_data_retention_age_days_12, assess_hazmat_manifest_pct_13, assess_address_correction_count_14, assess_insulated_container_age_days_15, assess_technician_utilization_pct_16, assess_egress_route_obstruction_count_17, assess_charging_dwell_minutes_18, assess_log_integrity_pct_19, assess_remote_wipe_test_age_days_20, assess_shipment_duplicate_count_21, assess_replenishment_task_queue_22, assess_payment_capture_success_pct_23, assess_yard_spot_accuracy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

