"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_inventory_value_01(record):
    """Evaluate inventory value for control WP-0127-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-01", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-01", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-01", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-01", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory value must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_label_error_count_02(record):
    """Evaluate label errors for control WP-0127-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-02", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-02", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-02", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-02", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "label errors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_concentration_pct_03(record):
    """Evaluate supplier concentration for control WP-0127-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-03", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-03", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-03", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-03", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier concentration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_invoice_match_pct_04(record):
    """Evaluate invoice match rate for control WP-0127-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-04", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-04", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-04", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-04", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "invoice match rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_energy_kwh_per_order_05(record):
    """Evaluate energy per order for control WP-0127-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-05", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-05", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-05", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-05", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "critical", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "energy per order must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_batch_recall_trace_minutes_06(record):
    """Evaluate recall trace time for control WP-0127-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-06", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-06", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-06", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-06", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recall trace time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_data_retention_age_days_07(record):
    """Evaluate data retention age for control WP-0127-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-07", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-07", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-07", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-07", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "data retention age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_hazmat_manifest_pct_08(record):
    """Evaluate hazmat manifest completion for control WP-0127-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-08", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-08", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-08", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-08", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "hazmat manifest completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_address_correction_count_09(record):
    """Evaluate address corrections for control WP-0127-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-09", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-09", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-09", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-09", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "address corrections must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_insulated_container_age_days_10(record):
    """Evaluate insulated container age for control WP-0127-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-10", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-10", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-10", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-10", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insulated container age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_technician_utilization_pct_11(record):
    """Evaluate technician utilization for control WP-0127-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-11", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-11", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-11", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-11", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "technician utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_egress_route_obstruction_count_12(record):
    """Evaluate egress route obstructions for control WP-0127-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-12", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-12", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-12", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-12", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "egress route obstructions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_charging_dwell_minutes_13(record):
    """Evaluate charging dwell for control WP-0127-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charging_dwell_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-13", "metric": "charging_dwell_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-13", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-13", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-13", "metric": "charging_dwell_minutes", "label": "charging dwell",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "charging dwell must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_log_integrity_pct_14(record):
    """Evaluate log integrity for control WP-0127-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-14", "metric": "log_integrity_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-14", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-14", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-14", "metric": "log_integrity_pct", "label": "log integrity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "log integrity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_remote_wipe_test_age_days_15(record):
    """Evaluate remote wipe test age for control WP-0127-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-15", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-15", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-15", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-15", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "remote wipe test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_shipment_duplicate_count_16(record):
    """Evaluate duplicate shipments for control WP-0127-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-16", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "shipments",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-16", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-16", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-16", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "high", "unit": "shipments",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "duplicate shipments falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_replenishment_task_queue_17(record):
    """Evaluate replenishment task queue for control WP-0127-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-17", "metric": "replenishment_task_queue",
            "status": "insufficient_data",
            "severity": "critical", "unit": "tasks",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-17", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-17", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-17", "metric": "replenishment_task_queue", "label": "replenishment task queue",
        "status": "breach", "severity": "critical", "unit": "tasks",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replenishment task queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_payment_capture_success_pct_18(record):
    """Evaluate payment capture success for control WP-0127-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_capture_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-18", "metric": "payment_capture_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-18", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-18", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-18", "metric": "payment_capture_success_pct", "label": "payment capture success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "payment capture success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_yard_spot_accuracy_pct_19(record):
    """Evaluate yard spot accuracy for control WP-0127-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_spot_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-19", "metric": "yard_spot_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-19", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-19", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-19", "metric": "yard_spot_accuracy_pct", "label": "yard spot accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "yard spot accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_shrinkage_rate_pct_20(record):
    """Evaluate shrinkage rate for control WP-0127-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shrinkage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-20", "metric": "shrinkage_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-20", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-20", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-20", "metric": "shrinkage_rate_pct", "label": "shrinkage rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "shrinkage rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_fill_rate_pct_21(record):
    """Evaluate supplier fill rate for control WP-0127-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-21", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-21", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-21", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-21", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier fill rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_edi_success_pct_22(record):
    """Evaluate supplier EDI success for control WP-0127-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-22", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-22", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-22", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-22", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier EDI success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_forecast_sharing_pct_23(record):
    """Evaluate supplier forecast sharing for control WP-0127-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_sharing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-23", "metric": "supplier_forecast_sharing_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-23", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-23", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-23", "metric": "supplier_forecast_sharing_pct", "label": "supplier forecast sharing",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier forecast sharing exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_audit_log_retention_days_24(record):
    """Evaluate supplier audit-log retention for control WP-0127-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0127-24", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0127-24", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0127-24", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0127-24", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier audit-log retention falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_inventory_value_01, assess_label_error_count_02, assess_supplier_concentration_pct_03, assess_invoice_match_pct_04, assess_energy_kwh_per_order_05, assess_batch_recall_trace_minutes_06, assess_data_retention_age_days_07, assess_hazmat_manifest_pct_08, assess_address_correction_count_09, assess_insulated_container_age_days_10, assess_technician_utilization_pct_11, assess_egress_route_obstruction_count_12, assess_charging_dwell_minutes_13, assess_log_integrity_pct_14, assess_remote_wipe_test_age_days_15, assess_shipment_duplicate_count_16, assess_replenishment_task_queue_17, assess_payment_capture_success_pct_18, assess_yard_spot_accuracy_pct_19, assess_shrinkage_rate_pct_20, assess_supplier_fill_rate_pct_21, assess_supplier_edi_success_pct_22, assess_supplier_forecast_sharing_pct_23, assess_supplier_audit_log_retention_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

