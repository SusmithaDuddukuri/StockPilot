"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_vendor_model_license_days_left_01(record):
    """Evaluate supplier model-license validity for control WP-0684-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_model_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-01", "metric": "supplier_vendor_model_license_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-01", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-01", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-01", "metric": "supplier_vendor_model_license_days_left", "label": "supplier model-license validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier model-license validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_observability_score_02(record):
    """Evaluate supplier observability score for control WP-0684-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-02", "metric": "supplier_observability_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-02", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-02", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-02", "metric": "supplier_observability_score", "label": "supplier observability score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier observability score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_container_scan_pct_03(record):
    """Evaluate supplier container scan coverage for control WP-0684-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_container_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-03", "metric": "supplier_container_scan_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-03", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-03", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-03", "metric": "supplier_container_scan_pct", "label": "supplier container scan coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier container scan coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_exception_approval_age_hours_04(record):
    """Evaluate supplier exception approval age for control WP-0684-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-04", "metric": "supplier_exception_approval_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-04", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-04", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-04", "metric": "supplier_exception_approval_age_hours", "label": "supplier exception approval age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier exception approval age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_duplicate_bank_signal_05(record):
    """Evaluate supplier duplicate-bank signal for control WP-0684-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_bank_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-05", "metric": "supplier_duplicate_bank_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-05", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-05", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-05", "metric": "supplier_duplicate_bank_signal", "label": "supplier duplicate-bank signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "supplier duplicate-bank signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_schedule_exception_age_hours_06(record):
    """Evaluate schedule exception age for control WP-0684-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-06", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-06", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-06", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-06", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "schedule exception age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_edi_mapping_age_days_07(record):
    """Evaluate supplier EDI mapping age for control WP-0684-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-07", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-07", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-07", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-07", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier EDI mapping age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_monitoring_handover_pct_08(record):
    """Evaluate supplier monitoring handover for control WP-0684-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-08", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-08", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-08", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-08", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier monitoring handover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_shipment_age_hours_09(record):
    """Evaluate shipment age for control WP-0684-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-09", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-09", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-09", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-09", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "shipment age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_battery_pct_10(record):
    """Evaluate equipment battery for control WP-0684-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-10", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-10", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-10", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-10", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "equipment battery must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_serial_capture_pct_11(record):
    """Evaluate serial capture for control WP-0684-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-11", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-11", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-11", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-11", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "serial capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_expedite_cost_12(record):
    """Evaluate expedite cost for control WP-0684-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-12", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-12", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-12", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-12", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "expedite cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_tire_pressure_variance_pct_13(record):
    """Evaluate tire pressure variance for control WP-0684-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-13", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-13", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-13", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-13", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "tire pressure variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_endpoint_patch_age_days_14(record):
    """Evaluate endpoint patch age for control WP-0684-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-14", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-14", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-14", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-14", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "endpoint patch age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_task_reopen_pct_15(record):
    """Evaluate task reopen rate for control WP-0684-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("task_reopen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-15", "metric": "task_reopen_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-15", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-15", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-15", "metric": "task_reopen_pct", "label": "task reopen rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "task reopen rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_eyewash_test_age_days_16(record):
    """Evaluate eyewash test age for control WP-0684-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-16", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-16", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-16", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-16", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "eyewash test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_return_authorization_age_hours_17(record):
    """Evaluate return authorization age for control WP-0684-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-17", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-17", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-17", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-17", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "return authorization age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_quality_hold_age_days_18(record):
    """Evaluate quality hold age for control WP-0684-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-18", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-18", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-18", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-18", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality hold age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_battery_charge_pct_19(record):
    """Evaluate battery charge for control WP-0684-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-19", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-19", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-19", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-19", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "battery charge must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_first_aid_response_minutes_20(record):
    """Evaluate first aid response time for control WP-0684-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-20", "metric": "first_aid_response_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-20", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-20", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-20", "metric": "first_aid_response_minutes", "label": "first aid response time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "first aid response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_ups_runtime_minutes_21(record):
    """Evaluate UPS runtime for control WP-0684-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ups_runtime_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-21", "metric": "ups_runtime_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-21", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-21", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-21", "metric": "ups_runtime_minutes", "label": "UPS runtime",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "UPS runtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_role_review_age_days_22(record):
    """Evaluate role review age for control WP-0684-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-22", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-22", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-22", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-22", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "role review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_dimensioning_error_pct_23(record):
    """Evaluate dimensioning error for control WP-0684-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-23", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-23", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-23", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-23", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dimensioning error must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_blind_count_compliance_pct_24(record):
    """Evaluate blind count compliance for control WP-0684-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0684-24", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0684-24", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0684-24", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0684-24", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "blind count compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_vendor_model_license_days_left_01, assess_supplier_observability_score_02, assess_supplier_container_scan_pct_03, assess_supplier_exception_approval_age_hours_04, assess_supplier_duplicate_bank_signal_05, assess_supplier_schedule_exception_age_hours_06, assess_supplier_edi_mapping_age_days_07, assess_supplier_monitoring_handover_pct_08, assess_shipment_age_hours_09, assess_battery_pct_10, assess_serial_capture_pct_11, assess_expedite_cost_12, assess_tire_pressure_variance_pct_13, assess_endpoint_patch_age_days_14, assess_task_reopen_pct_15, assess_eyewash_test_age_days_16, assess_return_authorization_age_hours_17, assess_quality_hold_age_days_18, assess_battery_charge_pct_19, assess_first_aid_response_minutes_20, assess_ups_runtime_minutes_21, assess_role_review_age_days_22, assess_dimensioning_error_pct_23, assess_blind_count_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

