"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_container_scan_pct_01(record):
    """Evaluate supplier container scan coverage for control WP-0497-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_container_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-01", "metric": "supplier_container_scan_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-01", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-01", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-01", "metric": "supplier_container_scan_pct", "label": "supplier container scan coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier container scan coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_exception_approval_age_hours_02(record):
    """Evaluate supplier exception approval age for control WP-0497-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-02", "metric": "supplier_exception_approval_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-02", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-02", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-02", "metric": "supplier_exception_approval_age_hours", "label": "supplier exception approval age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier exception approval age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_duplicate_bank_signal_03(record):
    """Evaluate supplier duplicate-bank signal for control WP-0497-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_bank_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-03", "metric": "supplier_duplicate_bank_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-03", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-03", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-03", "metric": "supplier_duplicate_bank_signal", "label": "supplier duplicate-bank signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier duplicate-bank signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_schedule_exception_age_hours_04(record):
    """Evaluate schedule exception age for control WP-0497-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-04", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-04", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-04", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-04", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schedule exception age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_edi_mapping_age_days_05(record):
    """Evaluate supplier EDI mapping age for control WP-0497-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-05", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-05", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-05", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-05", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier EDI mapping age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_monitoring_handover_pct_06(record):
    """Evaluate supplier monitoring handover for control WP-0497-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-06", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-06", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-06", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-06", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier monitoring handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_shipment_age_hours_07(record):
    """Evaluate shipment age for control WP-0497-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-07", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-07", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-07", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-07", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "shipment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_battery_pct_08(record):
    """Evaluate equipment battery for control WP-0497-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-08", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-08", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-08", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-08", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment battery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_serial_capture_pct_09(record):
    """Evaluate serial capture for control WP-0497-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-09", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-09", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-09", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-09", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "serial capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_expedite_cost_10(record):
    """Evaluate expedite cost for control WP-0497-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-10", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-10", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-10", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-10", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "expedite cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_tire_pressure_variance_pct_11(record):
    """Evaluate tire pressure variance for control WP-0497-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-11", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-11", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-11", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-11", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tire pressure variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_endpoint_patch_age_days_12(record):
    """Evaluate endpoint patch age for control WP-0497-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-12", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-12", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-12", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-12", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "endpoint patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_task_reopen_pct_13(record):
    """Evaluate task reopen rate for control WP-0497-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("task_reopen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-13", "metric": "task_reopen_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-13", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-13", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-13", "metric": "task_reopen_pct", "label": "task reopen rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "task reopen rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_eyewash_test_age_days_14(record):
    """Evaluate eyewash test age for control WP-0497-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-14", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-14", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-14", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-14", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "eyewash test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_return_authorization_age_hours_15(record):
    """Evaluate return authorization age for control WP-0497-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-15", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-15", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-15", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-15", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "return authorization age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_quality_hold_age_days_16(record):
    """Evaluate quality hold age for control WP-0497-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-16", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-16", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-16", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-16", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quality hold age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_battery_charge_pct_17(record):
    """Evaluate battery charge for control WP-0497-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-17", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-17", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-17", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-17", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "battery charge exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_first_aid_response_minutes_18(record):
    """Evaluate first aid response time for control WP-0497-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-18", "metric": "first_aid_response_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-18", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-18", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-18", "metric": "first_aid_response_minutes", "label": "first aid response time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "first aid response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_ups_runtime_minutes_19(record):
    """Evaluate UPS runtime for control WP-0497-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ups_runtime_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-19", "metric": "ups_runtime_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-19", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-19", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-19", "metric": "ups_runtime_minutes", "label": "UPS runtime",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "UPS runtime must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_role_review_age_days_20(record):
    """Evaluate role review age for control WP-0497-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-20", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-20", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-20", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-20", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "role review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_dimensioning_error_pct_21(record):
    """Evaluate dimensioning error for control WP-0497-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-21", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-21", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-21", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-21", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "dimensioning error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_blind_count_compliance_pct_22(record):
    """Evaluate blind count compliance for control WP-0497-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-22", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-22", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-22", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-22", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "blind count compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_pick_short_count_23(record):
    """Evaluate pick shorts for control WP-0497-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-23", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-23", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-23", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-23", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "critical", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick shorts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_broker_response_hours_24(record):
    """Evaluate broker response time for control WP-0497-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0497-24", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0497-24", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0497-24", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0497-24", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "broker response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_container_scan_pct_01, assess_supplier_exception_approval_age_hours_02, assess_supplier_duplicate_bank_signal_03, assess_supplier_schedule_exception_age_hours_04, assess_supplier_edi_mapping_age_days_05, assess_supplier_monitoring_handover_pct_06, assess_shipment_age_hours_07, assess_battery_pct_08, assess_serial_capture_pct_09, assess_expedite_cost_10, assess_tire_pressure_variance_pct_11, assess_endpoint_patch_age_days_12, assess_task_reopen_pct_13, assess_eyewash_test_age_days_14, assess_return_authorization_age_hours_15, assess_quality_hold_age_days_16, assess_battery_charge_pct_17, assess_first_aid_response_minutes_18, assess_ups_runtime_minutes_19, assess_role_review_age_days_20, assess_dimensioning_error_pct_21, assess_blind_count_compliance_pct_22, assess_pick_short_count_23, assess_broker_response_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

