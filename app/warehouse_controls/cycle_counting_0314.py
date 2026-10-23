"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_dispatch_accuracy_pct_01(record):
    """Evaluate supplier dispatch accuracy for control WP-0314-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-01", "metric": "supplier_dispatch_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-01", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-01", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-01", "metric": "supplier_dispatch_accuracy_pct", "label": "supplier dispatch accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dispatch accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_inventory_transfer_match_pct_02(record):
    """Evaluate inventory transfer match for control WP-0314-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-02", "metric": "supplier_inventory_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-02", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-02", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-02", "metric": "supplier_inventory_transfer_match_pct", "label": "inventory transfer match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "inventory transfer match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_inventory_value_03(record):
    """Evaluate inventory value for control WP-0314-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-03", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-03", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-03", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-03", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "inventory value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_label_error_count_04(record):
    """Evaluate label errors for control WP-0314-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-04", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-04", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-04", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-04", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "label errors must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_concentration_pct_05(record):
    """Evaluate supplier concentration for control WP-0314-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-05", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-05", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-05", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-05", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier concentration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_invoice_match_pct_06(record):
    """Evaluate invoice match rate for control WP-0314-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-06", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-06", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-06", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-06", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "invoice match rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_energy_kwh_per_order_07(record):
    """Evaluate energy per order for control WP-0314-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-07", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "low", "unit": "kWh",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-07", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-07", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-07", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "low", "unit": "kWh",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "energy per order falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_batch_recall_trace_minutes_08(record):
    """Evaluate recall trace time for control WP-0314-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-08", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-08", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-08", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-08", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recall trace time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_data_retention_age_days_09(record):
    """Evaluate data retention age for control WP-0314-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-09", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-09", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-09", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-09", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data retention age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_hazmat_manifest_pct_10(record):
    """Evaluate hazmat manifest completion for control WP-0314-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-10", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-10", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-10", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-10", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "hazmat manifest completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_address_correction_count_11(record):
    """Evaluate address corrections for control WP-0314-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-11", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-11", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-11", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-11", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "address corrections falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_insulated_container_age_days_12(record):
    """Evaluate insulated container age for control WP-0314-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-12", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-12", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-12", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-12", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insulated container age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_technician_utilization_pct_13(record):
    """Evaluate technician utilization for control WP-0314-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-13", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-13", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-13", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-13", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "technician utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_egress_route_obstruction_count_14(record):
    """Evaluate egress route obstructions for control WP-0314-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-14", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-14", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-14", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-14", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "egress route obstructions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_charging_dwell_minutes_15(record):
    """Evaluate charging dwell for control WP-0314-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charging_dwell_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-15", "metric": "charging_dwell_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-15", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-15", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-15", "metric": "charging_dwell_minutes", "label": "charging dwell",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "charging dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_log_integrity_pct_16(record):
    """Evaluate log integrity for control WP-0314-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-16", "metric": "log_integrity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-16", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-16", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-16", "metric": "log_integrity_pct", "label": "log integrity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "log integrity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_remote_wipe_test_age_days_17(record):
    """Evaluate remote wipe test age for control WP-0314-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-17", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-17", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-17", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-17", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "remote wipe test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_shipment_duplicate_count_18(record):
    """Evaluate duplicate shipments for control WP-0314-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-18", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "shipments",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-18", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-18", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-18", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "critical", "unit": "shipments",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "duplicate shipments exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_replenishment_task_queue_19(record):
    """Evaluate replenishment task queue for control WP-0314-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-19", "metric": "replenishment_task_queue",
            "status": "insufficient_data",
            "severity": "low", "unit": "tasks",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-19", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-19", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-19", "metric": "replenishment_task_queue", "label": "replenishment task queue",
        "status": "breach", "severity": "low", "unit": "tasks",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "replenishment task queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_payment_capture_success_pct_20(record):
    """Evaluate payment capture success for control WP-0314-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_capture_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-20", "metric": "payment_capture_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-20", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-20", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-20", "metric": "payment_capture_success_pct", "label": "payment capture success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment capture success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_yard_spot_accuracy_pct_21(record):
    """Evaluate yard spot accuracy for control WP-0314-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_spot_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-21", "metric": "yard_spot_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-21", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-21", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-21", "metric": "yard_spot_accuracy_pct", "label": "yard spot accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "yard spot accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_shrinkage_rate_pct_22(record):
    """Evaluate shrinkage rate for control WP-0314-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shrinkage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-22", "metric": "shrinkage_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-22", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-22", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-22", "metric": "shrinkage_rate_pct", "label": "shrinkage rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "shrinkage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_fill_rate_pct_23(record):
    """Evaluate supplier fill rate for control WP-0314-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-23", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-23", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-23", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-23", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier fill rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_edi_success_pct_24(record):
    """Evaluate supplier EDI success for control WP-0314-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0314-24", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0314-24", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0314-24", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0314-24", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier EDI success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_dispatch_accuracy_pct_01, assess_supplier_inventory_transfer_match_pct_02, assess_inventory_value_03, assess_label_error_count_04, assess_supplier_concentration_pct_05, assess_invoice_match_pct_06, assess_energy_kwh_per_order_07, assess_batch_recall_trace_minutes_08, assess_data_retention_age_days_09, assess_hazmat_manifest_pct_10, assess_address_correction_count_11, assess_insulated_container_age_days_12, assess_technician_utilization_pct_13, assess_egress_route_obstruction_count_14, assess_charging_dwell_minutes_15, assess_log_integrity_pct_16, assess_remote_wipe_test_age_days_17, assess_shipment_duplicate_count_18, assess_replenishment_task_queue_19, assess_payment_capture_success_pct_20, assess_yard_spot_accuracy_pct_21, assess_shrinkage_rate_pct_22, assess_supplier_fill_rate_pct_23, assess_supplier_edi_success_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

