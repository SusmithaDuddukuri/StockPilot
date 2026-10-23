"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_schedule_exception_age_hours_01(record):
    """Evaluate schedule exception age for control WP-0186-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-01", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-01", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-01", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-01", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schedule exception age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_edi_mapping_age_days_02(record):
    """Evaluate supplier EDI mapping age for control WP-0186-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-02", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-02", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-02", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-02", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier EDI mapping age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_monitoring_handover_pct_03(record):
    """Evaluate supplier monitoring handover for control WP-0186-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-03", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-03", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-03", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-03", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "supplier monitoring handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_shipment_age_hours_04(record):
    """Evaluate shipment age for control WP-0186-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-04", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-04", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-04", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-04", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "shipment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_battery_pct_05(record):
    """Evaluate equipment battery for control WP-0186-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-05", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-05", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-05", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-05", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment battery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_serial_capture_pct_06(record):
    """Evaluate serial capture for control WP-0186-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-06", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-06", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-06", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-06", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "serial capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_expedite_cost_07(record):
    """Evaluate expedite cost for control WP-0186-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-07", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-07", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-07", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-07", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "expedite cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_tire_pressure_variance_pct_08(record):
    """Evaluate tire pressure variance for control WP-0186-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-08", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-08", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-08", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-08", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tire pressure variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_endpoint_patch_age_days_09(record):
    """Evaluate endpoint patch age for control WP-0186-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-09", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-09", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-09", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-09", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "endpoint patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_task_reopen_pct_10(record):
    """Evaluate task reopen rate for control WP-0186-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("task_reopen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-10", "metric": "task_reopen_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-10", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-10", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-10", "metric": "task_reopen_pct", "label": "task reopen rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "task reopen rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_eyewash_test_age_days_11(record):
    """Evaluate eyewash test age for control WP-0186-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-11", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-11", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-11", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-11", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "eyewash test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_return_authorization_age_hours_12(record):
    """Evaluate return authorization age for control WP-0186-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-12", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-12", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-12", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-12", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "return authorization age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_quality_hold_age_days_13(record):
    """Evaluate quality hold age for control WP-0186-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-13", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-13", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-13", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-13", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quality hold age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_battery_charge_pct_14(record):
    """Evaluate battery charge for control WP-0186-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-14", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-14", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-14", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-14", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "battery charge exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_first_aid_response_minutes_15(record):
    """Evaluate first aid response time for control WP-0186-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-15", "metric": "first_aid_response_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-15", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-15", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-15", "metric": "first_aid_response_minutes", "label": "first aid response time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "first aid response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_ups_runtime_minutes_16(record):
    """Evaluate UPS runtime for control WP-0186-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ups_runtime_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-16", "metric": "ups_runtime_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-16", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-16", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-16", "metric": "ups_runtime_minutes", "label": "UPS runtime",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "UPS runtime must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_role_review_age_days_17(record):
    """Evaluate role review age for control WP-0186-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-17", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-17", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-17", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-17", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "role review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_dimensioning_error_pct_18(record):
    """Evaluate dimensioning error for control WP-0186-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-18", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-18", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-18", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-18", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "dimensioning error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_blind_count_compliance_pct_19(record):
    """Evaluate blind count compliance for control WP-0186-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-19", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-19", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-19", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-19", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "blind count compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_pick_short_count_20(record):
    """Evaluate pick shorts for control WP-0186-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-20", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-20", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-20", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-20", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "medium", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick shorts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_broker_response_hours_21(record):
    """Evaluate broker response time for control WP-0186-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-21", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-21", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-21", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-21", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "broker response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_route_emissions_variance_pct_22(record):
    """Evaluate route emissions variance for control WP-0186-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-22", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-22", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-22", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-22", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "route emissions variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_lines_per_labor_hour_23(record):
    """Evaluate lines per labor hour for control WP-0186-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-23", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "lines/hour",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-23", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-23", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-23", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "low", "unit": "lines/hour",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "lines per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_corrective_action_age_days_24(record):
    """Evaluate supplier corrective-action age for control WP-0186-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0186-24", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0186-24", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0186-24", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0186-24", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier corrective-action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_schedule_exception_age_hours_01, assess_supplier_edi_mapping_age_days_02, assess_supplier_monitoring_handover_pct_03, assess_shipment_age_hours_04, assess_battery_pct_05, assess_serial_capture_pct_06, assess_expedite_cost_07, assess_tire_pressure_variance_pct_08, assess_endpoint_patch_age_days_09, assess_task_reopen_pct_10, assess_eyewash_test_age_days_11, assess_return_authorization_age_hours_12, assess_quality_hold_age_days_13, assess_battery_charge_pct_14, assess_first_aid_response_minutes_15, assess_ups_runtime_minutes_16, assess_role_review_age_days_17, assess_dimensioning_error_pct_18, assess_blind_count_compliance_pct_19, assess_pick_short_count_20, assess_broker_response_hours_21, assess_route_emissions_variance_pct_22, assess_lines_per_labor_hour_23, assess_supplier_corrective_action_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

