"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_compute_budget_variance_pct_01(record):
    """Evaluate supplier compute budget variance for control WP-0241-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-01", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-01", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-01", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-01", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier compute budget variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_alert_ack_minutes_02(record):
    """Evaluate supplier alert acknowledgement for control WP-0241-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-02", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-02", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-02", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-02", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier alert acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_artifact_signature_pct_03(record):
    """Evaluate supplier artifact signature coverage for control WP-0241-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_artifact_signature_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-03", "metric": "supplier_artifact_signature_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-03", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-03", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-03", "metric": "supplier_artifact_signature_pct", "label": "supplier artifact signature coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier artifact signature coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_risk_acceptance_age_days_04(record):
    """Evaluate supplier risk acceptance age for control WP-0241-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_acceptance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-04", "metric": "supplier_risk_acceptance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-04", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-04", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-04", "metric": "supplier_risk_acceptance_age_days", "label": "supplier risk acceptance age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk acceptance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_related_party_match_count_05(record):
    """Evaluate supplier related-party matches for control WP-0241-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_related_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-05", "metric": "supplier_related_party_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-05", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-05", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-05", "metric": "supplier_related_party_match_count", "label": "supplier related-party matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "supplier related-party matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_material_availability_pct_06(record):
    """Evaluate supplier material availability for control WP-0241-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-06", "metric": "supplier_material_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-06", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-06", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-06", "metric": "supplier_material_availability_pct", "label": "supplier material availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier material availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_portal_login_age_days_07(record):
    """Evaluate supplier portal login age for control WP-0241-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_portal_login_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-07", "metric": "supplier_portal_login_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-07", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-07", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-07", "metric": "supplier_portal_login_age_days", "label": "supplier portal login age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier portal login age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_runbook_handover_pct_08(record):
    """Evaluate supplier runbook handover for control WP-0241-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-08", "metric": "supplier_runbook_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-08", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-08", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-08", "metric": "supplier_runbook_handover_pct", "label": "supplier runbook handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier runbook handover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_delivery_days_09(record):
    """Evaluate delivery duration for control WP-0241-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-09", "metric": "delivery_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-09", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-09", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-09", "metric": "delivery_days", "label": "delivery duration",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "delivery duration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_network_latency_ms_10(record):
    """Evaluate network latency for control WP-0241-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("network_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-10", "metric": "network_latency_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-10", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-10", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-10", "metric": "network_latency_ms", "label": "network latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "network latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_customer_complaint_count_11(record):
    """Evaluate customer complaints for control WP-0241-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_complaint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-11", "metric": "customer_complaint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-11", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-11", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-11", "metric": "customer_complaint_count", "label": "customer complaints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer complaints must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_response_hours_12(record):
    """Evaluate supplier response time for control WP-0241-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-12", "metric": "supplier_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-12", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-12", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-12", "metric": "supplier_response_hours", "label": "supplier response time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_load_balance_score_13(record):
    """Evaluate load balance for control WP-0241-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("load_balance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-13", "metric": "load_balance_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-13", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-13", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-13", "metric": "load_balance_score", "label": "load balance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "load balance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_critical_vulnerability_count_14(record):
    """Evaluate critical vulnerabilities for control WP-0241-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("critical_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-14", "metric": "critical_vulnerability_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-14", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-14", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-14", "metric": "critical_vulnerability_count", "label": "critical vulnerabilities",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "critical vulnerabilities falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_customer_wait_minutes_15(record):
    """Evaluate customer wait time for control WP-0241-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-15", "metric": "customer_wait_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-15", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-15", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-15", "metric": "customer_wait_minutes", "label": "customer wait time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer wait time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_noise_exposure_db_16(record):
    """Evaluate noise exposure for control WP-0241-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("noise_exposure_db")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-16", "metric": "noise_exposure_db",
            "status": "insufficient_data",
            "severity": "low", "unit": "dB",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-16", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-16", "metric": "noise_exposure_db", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-16", "metric": "noise_exposure_db", "label": "noise exposure",
        "status": "breach", "severity": "low", "unit": "dB",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "noise exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_inspection_queue_age_hours_17(record):
    """Evaluate inspection queue age for control WP-0241-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-17", "metric": "inspection_queue_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-17", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-17", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-17", "metric": "inspection_queue_age_hours", "label": "inspection queue age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "inspection queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_inspection_sample_pct_18(record):
    """Evaluate inspection sample rate for control WP-0241-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_sample_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-18", "metric": "inspection_sample_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-18", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-18", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-18", "metric": "inspection_sample_pct", "label": "inspection sample rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "inspection sample rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_battery_cycle_count_19(record):
    """Evaluate battery cycle count for control WP-0241-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_cycle_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-19", "metric": "battery_cycle_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "cycles",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-19", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-19", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-19", "metric": "battery_cycle_count", "label": "battery cycle count",
        "status": "breach", "severity": "critical", "unit": "cycles",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery cycle count must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_incident_report_age_hours_20(record):
    """Evaluate incident report age for control WP-0241-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_report_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-20", "metric": "incident_report_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-20", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-20", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-20", "metric": "incident_report_age_hours", "label": "incident report age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident report age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_power_quality_score_21(record):
    """Evaluate power quality for control WP-0241-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("power_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-21", "metric": "power_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-21", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-21", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-21", "metric": "power_quality_score", "label": "power quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "power quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_least_privilege_score_22(record):
    """Evaluate least privilege score for control WP-0241-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("least_privilege_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-22", "metric": "least_privilege_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-22", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-22", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-22", "metric": "least_privilege_score", "label": "least privilege score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "least privilege score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_scale_zero_drift_23(record):
    """Evaluate scale zero drift for control WP-0241-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_zero_drift")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-23", "metric": "scale_zero_drift",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-23", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-23", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-23", "metric": "scale_zero_drift", "label": "scale zero drift",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scale zero drift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_variance_approval_age_hours_24(record):
    """Evaluate variance approval age for control WP-0241-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("variance_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0241-24", "metric": "variance_approval_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0241-24", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0241-24", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0241-24", "metric": "variance_approval_age_hours", "label": "variance approval age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "variance approval age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_compute_budget_variance_pct_01, assess_supplier_alert_ack_minutes_02, assess_supplier_artifact_signature_pct_03, assess_supplier_risk_acceptance_age_days_04, assess_supplier_related_party_match_count_05, assess_supplier_material_availability_pct_06, assess_supplier_portal_login_age_days_07, assess_supplier_runbook_handover_pct_08, assess_delivery_days_09, assess_network_latency_ms_10, assess_customer_complaint_count_11, assess_supplier_response_hours_12, assess_load_balance_score_13, assess_critical_vulnerability_count_14, assess_customer_wait_minutes_15, assess_noise_exposure_db_16, assess_inspection_queue_age_hours_17, assess_inspection_sample_pct_18, assess_battery_cycle_count_19, assess_incident_report_age_hours_20, assess_power_quality_score_21, assess_least_privilege_score_22, assess_scale_zero_drift_23, assess_variance_approval_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

