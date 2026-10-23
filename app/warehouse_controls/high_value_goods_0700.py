"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_customer_complaint_count_01(record):
    """Evaluate customer complaints for control WP-0700-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_complaint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-01", "metric": "customer_complaint_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-01", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-01", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-01", "metric": "customer_complaint_count", "label": "customer complaints",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "customer complaints falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_response_hours_02(record):
    """Evaluate supplier response time for control WP-0700-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-02", "metric": "supplier_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-02", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-02", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-02", "metric": "supplier_response_hours", "label": "supplier response time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_load_balance_score_03(record):
    """Evaluate load balance for control WP-0700-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("load_balance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-03", "metric": "load_balance_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-03", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-03", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-03", "metric": "load_balance_score", "label": "load balance",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "load balance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_critical_vulnerability_count_04(record):
    """Evaluate critical vulnerabilities for control WP-0700-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("critical_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-04", "metric": "critical_vulnerability_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-04", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-04", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-04", "metric": "critical_vulnerability_count", "label": "critical vulnerabilities",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "critical vulnerabilities exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_customer_wait_minutes_05(record):
    """Evaluate customer wait time for control WP-0700-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-05", "metric": "customer_wait_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-05", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-05", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-05", "metric": "customer_wait_minutes", "label": "customer wait time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "customer wait time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_noise_exposure_db_06(record):
    """Evaluate noise exposure for control WP-0700-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("noise_exposure_db")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-06", "metric": "noise_exposure_db",
            "status": "insufficient_data",
            "severity": "medium", "unit": "dB",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-06", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-06", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-06", "metric": "noise_exposure_db", "label": "noise exposure",
        "status": "breach", "severity": "medium", "unit": "dB",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "noise exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_inspection_queue_age_hours_07(record):
    """Evaluate inspection queue age for control WP-0700-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-07", "metric": "inspection_queue_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-07", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-07", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-07", "metric": "inspection_queue_age_hours", "label": "inspection queue age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inspection queue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_inspection_sample_pct_08(record):
    """Evaluate inspection sample rate for control WP-0700-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_sample_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-08", "metric": "inspection_sample_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-08", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-08", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-08", "metric": "inspection_sample_pct", "label": "inspection sample rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "inspection sample rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_battery_cycle_count_09(record):
    """Evaluate battery cycle count for control WP-0700-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_cycle_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-09", "metric": "battery_cycle_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "cycles",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-09", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-09", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-09", "metric": "battery_cycle_count", "label": "battery cycle count",
        "status": "breach", "severity": "low", "unit": "cycles",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "battery cycle count falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_incident_report_age_hours_10(record):
    """Evaluate incident report age for control WP-0700-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_report_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-10", "metric": "incident_report_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-10", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-10", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-10", "metric": "incident_report_age_hours", "label": "incident report age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "incident report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_power_quality_score_11(record):
    """Evaluate power quality for control WP-0700-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("power_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-11", "metric": "power_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-11", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-11", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-11", "metric": "power_quality_score", "label": "power quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "power quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_least_privilege_score_12(record):
    """Evaluate least privilege score for control WP-0700-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("least_privilege_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-12", "metric": "least_privilege_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-12", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-12", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-12", "metric": "least_privilege_score", "label": "least privilege score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "least privilege score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_scale_zero_drift_13(record):
    """Evaluate scale zero drift for control WP-0700-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_zero_drift")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-13", "metric": "scale_zero_drift",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-13", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-13", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-13", "metric": "scale_zero_drift", "label": "scale zero drift",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "scale zero drift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_variance_approval_age_hours_14(record):
    """Evaluate variance approval age for control WP-0700-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("variance_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-14", "metric": "variance_approval_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-14", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-14", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-14", "metric": "variance_approval_age_hours", "label": "variance approval age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "variance approval age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_pick_substitution_pct_15(record):
    """Evaluate pick substitution rate for control WP-0700-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_substitution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-15", "metric": "pick_substitution_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-15", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-15", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-15", "metric": "pick_substitution_pct", "label": "pick substitution rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick substitution rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_customs_exam_age_hours_16(record):
    """Evaluate customs exam age for control WP-0700-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_exam_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-16", "metric": "customs_exam_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-16", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-16", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-16", "metric": "customs_exam_age_hours", "label": "customs exam age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "customs exam age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_fleet_utilization_pct_17(record):
    """Evaluate fleet utilization for control WP-0700-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fleet_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-17", "metric": "fleet_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-17", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-17", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-17", "metric": "fleet_utilization_pct", "label": "fleet utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "fleet utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_travel_time_pct_18(record):
    """Evaluate travel time share for control WP-0700-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("travel_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-18", "metric": "travel_time_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-18", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-18", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-18", "metric": "travel_time_pct", "label": "travel time share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "travel time share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_audit_score_19(record):
    """Evaluate supplier audit score for control WP-0700-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-19", "metric": "supplier_audit_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-19", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-19", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-19", "metric": "supplier_audit_score", "label": "supplier audit score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier audit score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_ppm_defects_20(record):
    """Evaluate supplier PPM defects for control WP-0700-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppm_defects")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-20", "metric": "supplier_ppm_defects",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ppm",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-20", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-20", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-20", "metric": "supplier_ppm_defects", "label": "supplier PPM defects",
        "status": "breach", "severity": "critical", "unit": "ppm",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier PPM defects exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_credit_note_age_days_21(record):
    """Evaluate supplier credit-note age for control WP-0700-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-21", "metric": "supplier_credit_note_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-21", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-21", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-21", "metric": "supplier_credit_note_age_days", "label": "supplier credit-note age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier credit-note age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_release_notice_days_22(record):
    """Evaluate supplier release notice for control WP-0700-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-22", "metric": "supplier_release_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-22", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-22", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-22", "metric": "supplier_release_notice_days", "label": "supplier release notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier release notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_dimension_spec_match_pct_23(record):
    """Evaluate supplier dimension specification match for control WP-0700-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dimension_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-23", "metric": "supplier_dimension_spec_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-23", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-23", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-23", "metric": "supplier_dimension_spec_match_pct", "label": "supplier dimension specification match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dimension specification match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_seal_control_pct_24(record):
    """Evaluate supplier seal control for control WP-0700-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seal_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0700-24", "metric": "supplier_seal_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0700-24", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0700-24", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0700-24", "metric": "supplier_seal_control_pct", "label": "supplier seal control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "supplier seal control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_customer_complaint_count_01, assess_supplier_response_hours_02, assess_load_balance_score_03, assess_critical_vulnerability_count_04, assess_customer_wait_minutes_05, assess_noise_exposure_db_06, assess_inspection_queue_age_hours_07, assess_inspection_sample_pct_08, assess_battery_cycle_count_09, assess_incident_report_age_hours_10, assess_power_quality_score_11, assess_least_privilege_score_12, assess_scale_zero_drift_13, assess_variance_approval_age_hours_14, assess_pick_substitution_pct_15, assess_customs_exam_age_hours_16, assess_fleet_utilization_pct_17, assess_travel_time_pct_18, assess_supplier_audit_score_19, assess_supplier_ppm_defects_20, assess_supplier_credit_note_age_days_21, assess_supplier_release_notice_days_22, assess_supplier_dimension_spec_match_pct_23, assess_supplier_seal_control_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

