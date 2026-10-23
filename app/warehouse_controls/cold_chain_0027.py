"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_receiving_queue_orders_01(record):
    """Evaluate receiving queue for control WP-0027-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-01", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-01", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-01", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-01", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receiving queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_customer_retention_pct_02(record):
    """Evaluate customer retention for control WP-0027-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-02", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-02", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-02", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-02", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_railcar_dwell_hours_03(record):
    """Evaluate railcar dwell for control WP-0027-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-03", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-03", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-03", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-03", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "railcar dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_cost_per_line_04(record):
    """Evaluate cost per line for control WP-0027-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-04", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-04", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-04", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-04", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "cost per line falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_labor_audit_gap_count_05(record):
    """Evaluate supplier labor audit gaps for control WP-0027-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-05", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-05", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-05", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-05", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier labor audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_cyber_maturity_score_06(record):
    """Evaluate supplier cyber maturity for control WP-0027-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-06", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-06", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-06", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-06", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cyber maturity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_alternate_source_test_age_days_07(record):
    """Evaluate alternate-source test age for control WP-0027-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-07", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-07", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-07", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-07", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "alternate-source test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_incident_notification_minutes_08(record):
    """Evaluate supplier incident notification time for control WP-0027-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-08", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-08", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-08", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-08", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier incident notification time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_energy_security_score_09(record):
    """Evaluate supplier energy security for control WP-0027-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-09", "metric": "supplier_energy_security_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-09", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-09", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-09", "metric": "supplier_energy_security_score", "label": "supplier energy security",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy security must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_renewable_energy_pct_10(record):
    """Evaluate supplier renewable energy share for control WP-0027-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_renewable_energy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-10", "metric": "supplier_renewable_energy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-10", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-10", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-10", "metric": "supplier_renewable_energy_pct", "label": "supplier renewable energy share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier renewable energy share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_escalation_compliance_pct_11(record):
    """Evaluate supplier escalation compliance for control WP-0027-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-11", "metric": "supplier_escalation_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-11", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-11", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-11", "metric": "supplier_escalation_compliance_pct", "label": "supplier escalation compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier escalation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_repeat_defect_count_12(record):
    """Evaluate supplier repeat defects for control WP-0027-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repeat_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-12", "metric": "supplier_repeat_defect_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-12", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-12", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-12", "metric": "supplier_repeat_defect_count", "label": "supplier repeat defects",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier repeat defects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_forced_labor_screen_pct_13(record):
    """Evaluate supplier forced-labor screening for control WP-0027-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forced_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-13", "metric": "supplier_forced_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-13", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-13", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-13", "metric": "supplier_forced_labor_screen_pct", "label": "supplier forced-labor screening",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier forced-labor screening must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_layoff_signal_14(record):
    """Evaluate supplier layoff signal for control WP-0027-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_layoff_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-14", "metric": "supplier_layoff_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-14", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-14", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-14", "metric": "supplier_layoff_signal", "label": "supplier layoff signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier layoff signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_productivity_improvement_pct_15(record):
    """Evaluate supplier productivity improvement for control WP-0027-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_productivity_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-15", "metric": "supplier_productivity_improvement_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-15", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-15", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-15", "metric": "supplier_productivity_improvement_pct", "label": "supplier productivity improvement",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier productivity improvement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_model_retraining_age_days_16(record):
    """Evaluate supplier model retraining age for control WP-0027-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_retraining_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-16", "metric": "supplier_model_retraining_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-16", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-16", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-16", "metric": "supplier_model_retraining_age_days", "label": "supplier model retraining age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier model retraining age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_latency_p95_ms_17(record):
    """Evaluate supplier p95 latency for control WP-0027-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p95_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-17", "metric": "supplier_latency_p95_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-17", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-17", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-17", "metric": "supplier_latency_p95_ms", "label": "supplier p95 latency",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier p95 latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_release_attestation_pct_18(record):
    """Evaluate supplier release attestation for control WP-0027-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_attestation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-18", "metric": "supplier_release_attestation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-18", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-18", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-18", "metric": "supplier_release_attestation_pct", "label": "supplier release attestation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier release attestation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_audit_response_days_19(record):
    """Evaluate supplier audit response time for control WP-0027-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_response_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-19", "metric": "supplier_audit_response_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-19", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-19", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-19", "metric": "supplier_audit_response_days", "label": "supplier audit response time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier audit response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_emergency_order_pct_20(record):
    """Evaluate supplier emergency order rate for control WP-0027-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_order_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-20", "metric": "supplier_emergency_order_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-20", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-20", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-20", "metric": "supplier_emergency_order_pct", "label": "supplier emergency order rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "supplier emergency order rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_production_yield_pct_21(record):
    """Evaluate supplier production yield for control WP-0027-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_production_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-21", "metric": "supplier_production_yield_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-21", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-21", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-21", "metric": "supplier_production_yield_pct", "label": "supplier production yield",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier production yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_escalation_quality_score_22(record):
    """Evaluate supplier escalation quality for control WP-0027-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-22", "metric": "supplier_escalation_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-22", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-22", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-22", "metric": "supplier_escalation_quality_score", "label": "supplier escalation quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier escalation quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_regulator_notice_pct_23(record):
    """Evaluate supplier regulator notice completion for control WP-0027-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-23", "metric": "supplier_regulator_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-23", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-23", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-23", "metric": "supplier_regulator_notice_pct", "label": "supplier regulator notice completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier regulator notice completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_accuracy_pct_24(record):
    """Evaluate inventory accuracy for control WP-0027-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0027-24", "metric": "accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0027-24", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0027-24", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0027-24", "metric": "accuracy_pct", "label": "inventory accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "inventory accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
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

