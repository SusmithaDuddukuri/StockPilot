"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_runbook_handover_pct_01(record):
    """Evaluate supplier runbook handover for control WP-0632-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-01", "metric": "supplier_runbook_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-01", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-01", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-01", "metric": "supplier_runbook_handover_pct", "label": "supplier runbook handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier runbook handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_delivery_days_02(record):
    """Evaluate delivery duration for control WP-0632-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-02", "metric": "delivery_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-02", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-02", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-02", "metric": "delivery_days", "label": "delivery duration",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery duration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_network_latency_ms_03(record):
    """Evaluate network latency for control WP-0632-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("network_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-03", "metric": "network_latency_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-03", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-03", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-03", "metric": "network_latency_ms", "label": "network latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "network latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_customer_complaint_count_04(record):
    """Evaluate customer complaints for control WP-0632-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_complaint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-04", "metric": "customer_complaint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-04", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-04", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-04", "metric": "customer_complaint_count", "label": "customer complaints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "customer complaints exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_response_hours_05(record):
    """Evaluate supplier response time for control WP-0632-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-05", "metric": "supplier_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-05", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-05", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-05", "metric": "supplier_response_hours", "label": "supplier response time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_load_balance_score_06(record):
    """Evaluate load balance for control WP-0632-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("load_balance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-06", "metric": "load_balance_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-06", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-06", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-06", "metric": "load_balance_score", "label": "load balance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "load balance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_critical_vulnerability_count_07(record):
    """Evaluate critical vulnerabilities for control WP-0632-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("critical_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-07", "metric": "critical_vulnerability_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-07", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-07", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-07", "metric": "critical_vulnerability_count", "label": "critical vulnerabilities",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "critical vulnerabilities must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_customer_wait_minutes_08(record):
    """Evaluate customer wait time for control WP-0632-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-08", "metric": "customer_wait_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-08", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-08", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-08", "metric": "customer_wait_minutes", "label": "customer wait time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "customer wait time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_noise_exposure_db_09(record):
    """Evaluate noise exposure for control WP-0632-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("noise_exposure_db")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-09", "metric": "noise_exposure_db",
            "status": "insufficient_data",
            "severity": "low", "unit": "dB",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-09", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-09", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-09", "metric": "noise_exposure_db", "label": "noise exposure",
        "status": "breach", "severity": "low", "unit": "dB",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "noise exposure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_inspection_queue_age_hours_10(record):
    """Evaluate inspection queue age for control WP-0632-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-10", "metric": "inspection_queue_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-10", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-10", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-10", "metric": "inspection_queue_age_hours", "label": "inspection queue age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inspection queue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_inspection_sample_pct_11(record):
    """Evaluate inspection sample rate for control WP-0632-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_sample_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-11", "metric": "inspection_sample_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-11", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-11", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-11", "metric": "inspection_sample_pct", "label": "inspection sample rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inspection sample rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_battery_cycle_count_12(record):
    """Evaluate battery cycle count for control WP-0632-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_cycle_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-12", "metric": "battery_cycle_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "cycles",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-12", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-12", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-12", "metric": "battery_cycle_count", "label": "battery cycle count",
        "status": "breach", "severity": "critical", "unit": "cycles",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "battery cycle count exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_incident_report_age_hours_13(record):
    """Evaluate incident report age for control WP-0632-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_report_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-13", "metric": "incident_report_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-13", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-13", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-13", "metric": "incident_report_age_hours", "label": "incident report age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "incident report age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_power_quality_score_14(record):
    """Evaluate power quality for control WP-0632-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("power_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-14", "metric": "power_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-14", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-14", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-14", "metric": "power_quality_score", "label": "power quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "power quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_least_privilege_score_15(record):
    """Evaluate least privilege score for control WP-0632-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("least_privilege_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-15", "metric": "least_privilege_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-15", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-15", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-15", "metric": "least_privilege_score", "label": "least privilege score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "least privilege score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_scale_zero_drift_16(record):
    """Evaluate scale zero drift for control WP-0632-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_zero_drift")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-16", "metric": "scale_zero_drift",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-16", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-16", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-16", "metric": "scale_zero_drift", "label": "scale zero drift",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "scale zero drift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_variance_approval_age_hours_17(record):
    """Evaluate variance approval age for control WP-0632-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("variance_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-17", "metric": "variance_approval_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-17", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-17", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-17", "metric": "variance_approval_age_hours", "label": "variance approval age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "variance approval age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_pick_substitution_pct_18(record):
    """Evaluate pick substitution rate for control WP-0632-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_substitution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-18", "metric": "pick_substitution_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-18", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-18", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-18", "metric": "pick_substitution_pct", "label": "pick substitution rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick substitution rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_customs_exam_age_hours_19(record):
    """Evaluate customs exam age for control WP-0632-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_exam_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-19", "metric": "customs_exam_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-19", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-19", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-19", "metric": "customs_exam_age_hours", "label": "customs exam age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customs exam age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_fleet_utilization_pct_20(record):
    """Evaluate fleet utilization for control WP-0632-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fleet_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-20", "metric": "fleet_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-20", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-20", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-20", "metric": "fleet_utilization_pct", "label": "fleet utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "fleet utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_travel_time_pct_21(record):
    """Evaluate travel time share for control WP-0632-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("travel_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-21", "metric": "travel_time_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-21", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-21", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-21", "metric": "travel_time_pct", "label": "travel time share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "travel time share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_audit_score_22(record):
    """Evaluate supplier audit score for control WP-0632-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-22", "metric": "supplier_audit_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-22", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-22", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-22", "metric": "supplier_audit_score", "label": "supplier audit score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_ppm_defects_23(record):
    """Evaluate supplier PPM defects for control WP-0632-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppm_defects")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-23", "metric": "supplier_ppm_defects",
            "status": "insufficient_data",
            "severity": "high", "unit": "ppm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-23", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-23", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-23", "metric": "supplier_ppm_defects", "label": "supplier PPM defects",
        "status": "breach", "severity": "high", "unit": "ppm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier PPM defects must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_credit_note_age_days_24(record):
    """Evaluate supplier credit-note age for control WP-0632-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0632-24", "metric": "supplier_credit_note_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0632-24", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0632-24", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0632-24", "metric": "supplier_credit_note_age_days", "label": "supplier credit-note age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier credit-note age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_supplier_runbook_handover_pct_01, assess_delivery_days_02, assess_network_latency_ms_03, assess_customer_complaint_count_04, assess_supplier_response_hours_05, assess_load_balance_score_06, assess_critical_vulnerability_count_07, assess_customer_wait_minutes_08, assess_noise_exposure_db_09, assess_inspection_queue_age_hours_10, assess_inspection_sample_pct_11, assess_battery_cycle_count_12, assess_incident_report_age_hours_13, assess_power_quality_score_14, assess_least_privilege_score_15, assess_scale_zero_drift_16, assess_variance_approval_age_hours_17, assess_pick_substitution_pct_18, assess_customs_exam_age_hours_19, assess_fleet_utilization_pct_20, assess_travel_time_pct_21, assess_supplier_audit_score_22, assess_supplier_ppm_defects_23, assess_supplier_credit_note_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

