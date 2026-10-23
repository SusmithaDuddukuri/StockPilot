"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_energy_kwh_per_order_01(record):
    """Evaluate energy per order for control WP-0450-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-01", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "high", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-01", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-01", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-01", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "high", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "energy per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_batch_recall_trace_minutes_02(record):
    """Evaluate recall trace time for control WP-0450-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-02", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-02", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-02", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-02", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "recall trace time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_data_retention_age_days_03(record):
    """Evaluate data retention age for control WP-0450-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-03", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-03", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-03", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-03", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "data retention age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_hazmat_manifest_pct_04(record):
    """Evaluate hazmat manifest completion for control WP-0450-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-04", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-04", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-04", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-04", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "hazmat manifest completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_address_correction_count_05(record):
    """Evaluate address corrections for control WP-0450-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-05", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-05", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-05", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-05", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "address corrections must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_insulated_container_age_days_06(record):
    """Evaluate insulated container age for control WP-0450-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-06", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-06", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-06", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-06", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "insulated container age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_technician_utilization_pct_07(record):
    """Evaluate technician utilization for control WP-0450-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-07", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-07", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-07", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-07", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "technician utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_egress_route_obstruction_count_08(record):
    """Evaluate egress route obstructions for control WP-0450-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-08", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-08", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-08", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-08", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "egress route obstructions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_charging_dwell_minutes_09(record):
    """Evaluate charging dwell for control WP-0450-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charging_dwell_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-09", "metric": "charging_dwell_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-09", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-09", "metric": "charging_dwell_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-09", "metric": "charging_dwell_minutes", "label": "charging dwell",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "charging dwell must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_log_integrity_pct_10(record):
    """Evaluate log integrity for control WP-0450-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-10", "metric": "log_integrity_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-10", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-10", "metric": "log_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-10", "metric": "log_integrity_pct", "label": "log integrity",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "log integrity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_remote_wipe_test_age_days_11(record):
    """Evaluate remote wipe test age for control WP-0450-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-11", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-11", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-11", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-11", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "remote wipe test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_shipment_duplicate_count_12(record):
    """Evaluate duplicate shipments for control WP-0450-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-12", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "shipments",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-12", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-12", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-12", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "medium", "unit": "shipments",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate shipments must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_replenishment_task_queue_13(record):
    """Evaluate replenishment task queue for control WP-0450-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-13", "metric": "replenishment_task_queue",
            "status": "insufficient_data",
            "severity": "high", "unit": "tasks",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-13", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-13", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-13", "metric": "replenishment_task_queue", "label": "replenishment task queue",
        "status": "breach", "severity": "high", "unit": "tasks",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replenishment task queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_payment_capture_success_pct_14(record):
    """Evaluate payment capture success for control WP-0450-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_capture_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-14", "metric": "payment_capture_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-14", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-14", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-14", "metric": "payment_capture_success_pct", "label": "payment capture success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "payment capture success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_yard_spot_accuracy_pct_15(record):
    """Evaluate yard spot accuracy for control WP-0450-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_spot_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-15", "metric": "yard_spot_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-15", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-15", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-15", "metric": "yard_spot_accuracy_pct", "label": "yard spot accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "yard spot accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_shrinkage_rate_pct_16(record):
    """Evaluate shrinkage rate for control WP-0450-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shrinkage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-16", "metric": "shrinkage_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-16", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-16", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-16", "metric": "shrinkage_rate_pct", "label": "shrinkage rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "shrinkage rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_fill_rate_pct_17(record):
    """Evaluate supplier fill rate for control WP-0450-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-17", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-17", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-17", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-17", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier fill rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_edi_success_pct_18(record):
    """Evaluate supplier EDI success for control WP-0450-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-18", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-18", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-18", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-18", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "supplier EDI success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_forecast_sharing_pct_19(record):
    """Evaluate supplier forecast sharing for control WP-0450-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_sharing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-19", "metric": "supplier_forecast_sharing_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-19", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-19", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-19", "metric": "supplier_forecast_sharing_pct", "label": "supplier forecast sharing",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "supplier forecast sharing falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_audit_log_retention_days_20(record):
    """Evaluate supplier audit-log retention for control WP-0450-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-20", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-20", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-20", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-20", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit-log retention must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_requalification_age_days_21(record):
    """Evaluate supplier requalification age for control WP-0450-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_requalification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-21", "metric": "supplier_requalification_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-21", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-21", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-21", "metric": "supplier_requalification_age_days", "label": "supplier requalification age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier requalification age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_fire_risk_score_22(record):
    """Evaluate supplier site fire risk for control WP-0450-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-22", "metric": "supplier_fire_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-22", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-22", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-22", "metric": "supplier_fire_risk_score", "label": "supplier site fire risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier site fire risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_capacity_transfer_days_23(record):
    """Evaluate supplier capacity transfer time for control WP-0450-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-23", "metric": "supplier_capacity_transfer_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-23", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-23", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-23", "metric": "supplier_capacity_transfer_days", "label": "supplier capacity transfer time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "supplier capacity transfer time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_observation_count_24(record):
    """Evaluate supplier observations for control WP-0450-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0450-24", "metric": "supplier_observation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0450-24", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0450-24", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0450-24", "metric": "supplier_observation_count", "label": "supplier observations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier observations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_energy_kwh_per_order_01, assess_batch_recall_trace_minutes_02, assess_data_retention_age_days_03, assess_hazmat_manifest_pct_04, assess_address_correction_count_05, assess_insulated_container_age_days_06, assess_technician_utilization_pct_07, assess_egress_route_obstruction_count_08, assess_charging_dwell_minutes_09, assess_log_integrity_pct_10, assess_remote_wipe_test_age_days_11, assess_shipment_duplicate_count_12, assess_replenishment_task_queue_13, assess_payment_capture_success_pct_14, assess_yard_spot_accuracy_pct_15, assess_shrinkage_rate_pct_16, assess_supplier_fill_rate_pct_17, assess_supplier_edi_success_pct_18, assess_supplier_forecast_sharing_pct_19, assess_supplier_audit_log_retention_days_20, assess_supplier_requalification_age_days_21, assess_supplier_fire_risk_score_22, assess_supplier_capacity_transfer_days_23, assess_supplier_observation_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

