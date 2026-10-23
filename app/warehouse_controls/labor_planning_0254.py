"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_shipment_age_hours_01(record):
    """Evaluate shipment age for control WP-0254-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-01", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-01", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-01", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-01", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "shipment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_battery_pct_02(record):
    """Evaluate equipment battery for control WP-0254-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-02", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-02", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-02", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-02", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "equipment battery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_serial_capture_pct_03(record):
    """Evaluate serial capture for control WP-0254-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-03", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-03", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-03", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-03", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "serial capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_expedite_cost_04(record):
    """Evaluate expedite cost for control WP-0254-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-04", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-04", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-04", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-04", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "expedite cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_tire_pressure_variance_pct_05(record):
    """Evaluate tire pressure variance for control WP-0254-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-05", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-05", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-05", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-05", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "tire pressure variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_endpoint_patch_age_days_06(record):
    """Evaluate endpoint patch age for control WP-0254-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-06", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-06", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-06", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-06", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "endpoint patch age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_task_reopen_pct_07(record):
    """Evaluate task reopen rate for control WP-0254-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("task_reopen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-07", "metric": "task_reopen_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-07", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-07", "metric": "task_reopen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-07", "metric": "task_reopen_pct", "label": "task reopen rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "task reopen rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_eyewash_test_age_days_08(record):
    """Evaluate eyewash test age for control WP-0254-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("eyewash_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-08", "metric": "eyewash_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-08", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-08", "metric": "eyewash_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-08", "metric": "eyewash_test_age_days", "label": "eyewash test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "eyewash test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_return_authorization_age_hours_09(record):
    """Evaluate return authorization age for control WP-0254-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_authorization_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-09", "metric": "return_authorization_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-09", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-09", "metric": "return_authorization_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-09", "metric": "return_authorization_age_hours", "label": "return authorization age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "return authorization age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_quality_hold_age_days_10(record):
    """Evaluate quality hold age for control WP-0254-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-10", "metric": "quality_hold_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-10", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-10", "metric": "quality_hold_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-10", "metric": "quality_hold_age_days", "label": "quality hold age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "quality hold age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_battery_charge_pct_11(record):
    """Evaluate battery charge for control WP-0254-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_charge_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-11", "metric": "battery_charge_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-11", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-11", "metric": "battery_charge_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-11", "metric": "battery_charge_pct", "label": "battery charge",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "battery charge falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_first_aid_response_minutes_12(record):
    """Evaluate first aid response time for control WP-0254-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-12", "metric": "first_aid_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-12", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-12", "metric": "first_aid_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-12", "metric": "first_aid_response_minutes", "label": "first aid response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "first aid response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_ups_runtime_minutes_13(record):
    """Evaluate UPS runtime for control WP-0254-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ups_runtime_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-13", "metric": "ups_runtime_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-13", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-13", "metric": "ups_runtime_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-13", "metric": "ups_runtime_minutes", "label": "UPS runtime",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "UPS runtime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_role_review_age_days_14(record):
    """Evaluate role review age for control WP-0254-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("role_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-14", "metric": "role_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-14", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-14", "metric": "role_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-14", "metric": "role_review_age_days", "label": "role review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "role review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_dimensioning_error_pct_15(record):
    """Evaluate dimensioning error for control WP-0254-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dimensioning_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-15", "metric": "dimensioning_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-15", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-15", "metric": "dimensioning_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-15", "metric": "dimensioning_error_pct", "label": "dimensioning error",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "dimensioning error falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_blind_count_compliance_pct_16(record):
    """Evaluate blind count compliance for control WP-0254-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("blind_count_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-16", "metric": "blind_count_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-16", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-16", "metric": "blind_count_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-16", "metric": "blind_count_compliance_pct", "label": "blind count compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "blind count compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_pick_short_count_17(record):
    """Evaluate pick shorts for control WP-0254-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_short_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-17", "metric": "pick_short_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-17", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-17", "metric": "pick_short_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-17", "metric": "pick_short_count", "label": "pick shorts",
        "status": "breach", "severity": "high", "unit": "lines",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick shorts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_broker_response_hours_18(record):
    """Evaluate broker response time for control WP-0254-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("broker_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-18", "metric": "broker_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-18", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-18", "metric": "broker_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-18", "metric": "broker_response_hours", "label": "broker response time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "broker response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_route_emissions_variance_pct_19(record):
    """Evaluate route emissions variance for control WP-0254-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_emissions_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-19", "metric": "route_emissions_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-19", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-19", "metric": "route_emissions_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-19", "metric": "route_emissions_variance_pct", "label": "route emissions variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "route emissions variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_lines_per_labor_hour_20(record):
    """Evaluate lines per labor hour for control WP-0254-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lines_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-20", "metric": "lines_per_labor_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-20", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-20", "metric": "lines_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-20", "metric": "lines_per_labor_hour", "label": "lines per labor hour",
        "status": "breach", "severity": "medium", "unit": "lines/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lines per labor hour must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_corrective_action_age_days_21(record):
    """Evaluate supplier corrective-action age for control WP-0254-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-21", "metric": "supplier_corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-21", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-21", "metric": "supplier_corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-21", "metric": "supplier_corrective_action_age_days", "label": "supplier corrective-action age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier corrective-action age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_quality_escape_count_22(record):
    """Evaluate supplier quality escapes for control WP-0254-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-22", "metric": "supplier_quality_escape_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-22", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-22", "metric": "supplier_quality_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-22", "metric": "supplier_quality_escape_count", "label": "supplier quality escapes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier quality escapes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_payment_dispute_age_days_23(record):
    """Evaluate supplier payment dispute age for control WP-0254-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-23", "metric": "supplier_payment_dispute_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-23", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-23", "metric": "supplier_payment_dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-23", "metric": "supplier_payment_dispute_age_days", "label": "supplier payment dispute age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier payment dispute age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_problem_record_age_days_24(record):
    """Evaluate supplier problem-record age for control WP-0254-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_problem_record_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0254-24", "metric": "supplier_problem_record_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0254-24", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0254-24", "metric": "supplier_problem_record_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0254-24", "metric": "supplier_problem_record_age_days", "label": "supplier problem-record age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier problem-record age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_shipment_age_hours_01, assess_battery_pct_02, assess_serial_capture_pct_03, assess_expedite_cost_04, assess_tire_pressure_variance_pct_05, assess_endpoint_patch_age_days_06, assess_task_reopen_pct_07, assess_eyewash_test_age_days_08, assess_return_authorization_age_hours_09, assess_quality_hold_age_days_10, assess_battery_charge_pct_11, assess_first_aid_response_minutes_12, assess_ups_runtime_minutes_13, assess_role_review_age_days_14, assess_dimensioning_error_pct_15, assess_blind_count_compliance_pct_16, assess_pick_short_count_17, assess_broker_response_hours_18, assess_route_emissions_variance_pct_19, assess_lines_per_labor_hour_20, assess_supplier_corrective_action_age_days_21, assess_supplier_quality_escape_count_22, assess_supplier_payment_dispute_age_days_23, assess_supplier_problem_record_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

