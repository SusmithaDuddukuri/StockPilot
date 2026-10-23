"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_receiving_queue_orders_01(record):
    """Evaluate receiving queue for control WP-0406-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-01", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-01", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-01", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-01", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "receiving queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_customer_retention_pct_02(record):
    """Evaluate customer retention for control WP-0406-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-02", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-02", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-02", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-02", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "customer retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_railcar_dwell_hours_03(record):
    """Evaluate railcar dwell for control WP-0406-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-03", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-03", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-03", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-03", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "railcar dwell falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_cost_per_line_04(record):
    """Evaluate cost per line for control WP-0406-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-04", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-04", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-04", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-04", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cost per line must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_labor_audit_gap_count_05(record):
    """Evaluate supplier labor audit gaps for control WP-0406-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-05", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-05", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-05", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-05", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier labor audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_cyber_maturity_score_06(record):
    """Evaluate supplier cyber maturity for control WP-0406-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-06", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-06", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-06", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-06", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier cyber maturity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_alternate_source_test_age_days_07(record):
    """Evaluate alternate-source test age for control WP-0406-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-07", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-07", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-07", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-07", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "alternate-source test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_incident_notification_minutes_08(record):
    """Evaluate supplier incident notification time for control WP-0406-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-08", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-08", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-08", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-08", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier incident notification time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_energy_security_score_09(record):
    """Evaluate supplier energy security for control WP-0406-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-09", "metric": "supplier_energy_security_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-09", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-09", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-09", "metric": "supplier_energy_security_score", "label": "supplier energy security",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier energy security must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_renewable_energy_pct_10(record):
    """Evaluate supplier renewable energy share for control WP-0406-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_renewable_energy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-10", "metric": "supplier_renewable_energy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-10", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-10", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-10", "metric": "supplier_renewable_energy_pct", "label": "supplier renewable energy share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier renewable energy share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_escalation_compliance_pct_11(record):
    """Evaluate supplier escalation compliance for control WP-0406-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-11", "metric": "supplier_escalation_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-11", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-11", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-11", "metric": "supplier_escalation_compliance_pct", "label": "supplier escalation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier escalation compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_repeat_defect_count_12(record):
    """Evaluate supplier repeat defects for control WP-0406-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repeat_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-12", "metric": "supplier_repeat_defect_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-12", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-12", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-12", "metric": "supplier_repeat_defect_count", "label": "supplier repeat defects",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier repeat defects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_forced_labor_screen_pct_13(record):
    """Evaluate supplier forced-labor screening for control WP-0406-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forced_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-13", "metric": "supplier_forced_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-13", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-13", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-13", "metric": "supplier_forced_labor_screen_pct", "label": "supplier forced-labor screening",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier forced-labor screening must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_layoff_signal_14(record):
    """Evaluate supplier layoff signal for control WP-0406-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_layoff_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-14", "metric": "supplier_layoff_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-14", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-14", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-14", "metric": "supplier_layoff_signal", "label": "supplier layoff signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier layoff signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_productivity_improvement_pct_15(record):
    """Evaluate supplier productivity improvement for control WP-0406-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_productivity_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-15", "metric": "supplier_productivity_improvement_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-15", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-15", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-15", "metric": "supplier_productivity_improvement_pct", "label": "supplier productivity improvement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "supplier productivity improvement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_model_retraining_age_days_16(record):
    """Evaluate supplier model retraining age for control WP-0406-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_retraining_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-16", "metric": "supplier_model_retraining_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-16", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-16", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-16", "metric": "supplier_model_retraining_age_days", "label": "supplier model retraining age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model retraining age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_latency_p95_ms_17(record):
    """Evaluate supplier p95 latency for control WP-0406-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p95_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-17", "metric": "supplier_latency_p95_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-17", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-17", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-17", "metric": "supplier_latency_p95_ms", "label": "supplier p95 latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier p95 latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_release_attestation_pct_18(record):
    """Evaluate supplier release attestation for control WP-0406-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_attestation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-18", "metric": "supplier_release_attestation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-18", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-18", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-18", "metric": "supplier_release_attestation_pct", "label": "supplier release attestation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier release attestation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_audit_response_days_19(record):
    """Evaluate supplier audit response time for control WP-0406-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_response_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-19", "metric": "supplier_audit_response_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-19", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-19", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-19", "metric": "supplier_audit_response_days", "label": "supplier audit response time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "supplier audit response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_emergency_order_pct_20(record):
    """Evaluate supplier emergency order rate for control WP-0406-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_order_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-20", "metric": "supplier_emergency_order_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-20", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-20", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-20", "metric": "supplier_emergency_order_pct", "label": "supplier emergency order rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier emergency order rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_production_yield_pct_21(record):
    """Evaluate supplier production yield for control WP-0406-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_production_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-21", "metric": "supplier_production_yield_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-21", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-21", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-21", "metric": "supplier_production_yield_pct", "label": "supplier production yield",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier production yield must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_escalation_quality_score_22(record):
    """Evaluate supplier escalation quality for control WP-0406-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-22", "metric": "supplier_escalation_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-22", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-22", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-22", "metric": "supplier_escalation_quality_score", "label": "supplier escalation quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier escalation quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_regulator_notice_pct_23(record):
    """Evaluate supplier regulator notice completion for control WP-0406-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-23", "metric": "supplier_regulator_notice_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-23", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-23", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-23", "metric": "supplier_regulator_notice_pct", "label": "supplier regulator notice completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier regulator notice completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_accuracy_pct_24(record):
    """Evaluate inventory accuracy for control WP-0406-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0406-24", "metric": "accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0406-24", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0406-24", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0406-24", "metric": "accuracy_pct", "label": "inventory accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_receiving_queue_orders_01, assess_customer_retention_pct_02, assess_railcar_dwell_hours_03, assess_cost_per_line_04, assess_supplier_labor_audit_gap_count_05, assess_supplier_cyber_maturity_score_06, assess_supplier_alternate_source_test_age_days_07, assess_supplier_incident_notification_minutes_08, assess_supplier_energy_security_score_09, assess_supplier_renewable_energy_pct_10, assess_supplier_escalation_compliance_pct_11, assess_supplier_repeat_defect_count_12, assess_supplier_forced_labor_screen_pct_13, assess_supplier_layoff_signal_14, assess_supplier_productivity_improvement_pct_15, assess_supplier_model_retraining_age_days_16, assess_supplier_latency_p95_ms_17, assess_supplier_release_attestation_pct_18, assess_supplier_audit_response_days_19, assess_supplier_emergency_order_pct_20, assess_supplier_production_yield_pct_21, assess_supplier_escalation_quality_score_22, assess_supplier_regulator_notice_pct_23, assess_accuracy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

