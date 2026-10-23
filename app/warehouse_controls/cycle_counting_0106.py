"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_data_latency_minutes_01(record):
    """Evaluate supplier data latency for control WP-0106-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-01", "metric": "supplier_data_latency_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-01", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-01", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-01", "metric": "supplier_data_latency_minutes", "label": "supplier data latency",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_nonconformance_age_days_02(record):
    """Evaluate supplier nonconformance age for control WP-0106-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_nonconformance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-02", "metric": "supplier_nonconformance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-02", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-02", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-02", "metric": "supplier_nonconformance_age_days", "label": "supplier nonconformance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier nonconformance age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_working_hours_violation_count_03(record):
    """Evaluate supplier working-hours violations for control WP-0106-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_hours_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-03", "metric": "supplier_working_hours_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-03", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-03", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-03", "metric": "supplier_working_hours_violation_count", "label": "supplier working-hours violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier working-hours violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_going_concern_signal_04(record):
    """Evaluate supplier going-concern signal for control WP-0106-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_going_concern_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-04", "metric": "supplier_going_concern_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-04", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-04", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-04", "metric": "supplier_going_concern_signal", "label": "supplier going-concern signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier going-concern signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_kpi_review_age_days_05(record):
    """Evaluate supplier KPI review age for control WP-0106-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-05", "metric": "supplier_kpi_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-05", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-05", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-05", "metric": "supplier_kpi_review_age_days", "label": "supplier KPI review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KPI review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_vendor_model_license_days_left_06(record):
    """Evaluate supplier model-license validity for control WP-0106-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_model_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-06", "metric": "supplier_vendor_model_license_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-06", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-06", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-06", "metric": "supplier_vendor_model_license_days_left", "label": "supplier model-license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier model-license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_observability_score_07(record):
    """Evaluate supplier observability score for control WP-0106-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-07", "metric": "supplier_observability_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-07", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-07", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-07", "metric": "supplier_observability_score", "label": "supplier observability score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier observability score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_container_scan_pct_08(record):
    """Evaluate supplier container scan coverage for control WP-0106-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_container_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-08", "metric": "supplier_container_scan_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-08", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-08", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-08", "metric": "supplier_container_scan_pct", "label": "supplier container scan coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier container scan coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_exception_approval_age_hours_09(record):
    """Evaluate supplier exception approval age for control WP-0106-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-09", "metric": "supplier_exception_approval_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-09", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-09", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-09", "metric": "supplier_exception_approval_age_hours", "label": "supplier exception approval age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exception approval age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_duplicate_bank_signal_10(record):
    """Evaluate supplier duplicate-bank signal for control WP-0106-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_bank_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-10", "metric": "supplier_duplicate_bank_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-10", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-10", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-10", "metric": "supplier_duplicate_bank_signal", "label": "supplier duplicate-bank signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier duplicate-bank signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_schedule_exception_age_hours_11(record):
    """Evaluate schedule exception age for control WP-0106-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-11", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-11", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-11", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-11", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "schedule exception age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_edi_mapping_age_days_12(record):
    """Evaluate supplier EDI mapping age for control WP-0106-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-12", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-12", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-12", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-12", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier EDI mapping age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_monitoring_handover_pct_13(record):
    """Evaluate supplier monitoring handover for control WP-0106-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-13", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-13", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-13", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-13", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier monitoring handover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_shipment_age_hours_14(record):
    """Evaluate shipment age for control WP-0106-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-14", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-14", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-14", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-14", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "shipment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_battery_pct_15(record):
    """Evaluate equipment battery for control WP-0106-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-15", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-15", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-15", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-15", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "equipment battery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_serial_capture_pct_16(record):
    """Evaluate serial capture for control WP-0106-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-16", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-16", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-16", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-16", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_expedite_cost_17(record):
    """Evaluate expedite cost for control WP-0106-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-17", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-17", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-17", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-17", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "expedite cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_tire_pressure_variance_pct_18(record):
    """Evaluate tire pressure variance for control WP-0106-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-18", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-18", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-18", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-18", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "tire pressure variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_endpoint_patch_age_days_19(record):
    """Evaluate endpoint patch age for control WP-0106-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-19", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-19", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-19", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-19", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "endpoint patch age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_task_reopen_pct_20(record):
    """Evaluate task reopen rate for control WP-0106-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("task_reopen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-20", "metric": "task_reopen_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-20", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-20", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-20", "metric": "task_reopen_pct", "label": "task reopen rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "task reopen rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_eyewash_test_age_days_21(record):
    """Evaluate eyewash test age for control WP-0106-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-21", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-21", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-21", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-21", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "eyewash test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_return_authorization_age_hours_22(record):
    """Evaluate return authorization age for control WP-0106-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-22", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-22", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-22", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-22", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "return authorization age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_quality_hold_age_days_23(record):
    """Evaluate quality hold age for control WP-0106-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-23", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-23", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-23", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-23", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "quality hold age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_battery_charge_pct_24(record):
    """Evaluate battery charge for control WP-0106-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0106-24", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0106-24", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0106-24", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0106-24", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery charge must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_data_latency_minutes_01, assess_supplier_nonconformance_age_days_02, assess_supplier_working_hours_violation_count_03, assess_supplier_going_concern_signal_04, assess_supplier_kpi_review_age_days_05, assess_supplier_vendor_model_license_days_left_06, assess_supplier_observability_score_07, assess_supplier_container_scan_pct_08, assess_supplier_exception_approval_age_hours_09, assess_supplier_duplicate_bank_signal_10, assess_supplier_schedule_exception_age_hours_11, assess_supplier_edi_mapping_age_days_12, assess_supplier_monitoring_handover_pct_13, assess_shipment_age_hours_14, assess_battery_pct_15, assess_serial_capture_pct_16, assess_expedite_cost_17, assess_tire_pressure_variance_pct_18, assess_endpoint_patch_age_days_19, assess_task_reopen_pct_20, assess_eyewash_test_age_days_21, assess_return_authorization_age_hours_22, assess_quality_hold_age_days_23, assess_battery_charge_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

