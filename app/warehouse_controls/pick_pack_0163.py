"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_alternate_source_test_age_days_01(record):
    """Evaluate alternate-source test age for control WP-0163-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-01", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-01", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-01", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-01", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "alternate-source test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_incident_notification_minutes_02(record):
    """Evaluate supplier incident notification time for control WP-0163-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-02", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-02", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-02", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-02", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier incident notification time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_energy_security_score_03(record):
    """Evaluate supplier energy security for control WP-0163-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-03", "metric": "supplier_energy_security_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-03", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-03", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-03", "metric": "supplier_energy_security_score", "label": "supplier energy security",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier energy security exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_renewable_energy_pct_04(record):
    """Evaluate supplier renewable energy share for control WP-0163-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_renewable_energy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-04", "metric": "supplier_renewable_energy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-04", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-04", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-04", "metric": "supplier_renewable_energy_pct", "label": "supplier renewable energy share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "supplier renewable energy share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_escalation_compliance_pct_05(record):
    """Evaluate supplier escalation compliance for control WP-0163-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-05", "metric": "supplier_escalation_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-05", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-05", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-05", "metric": "supplier_escalation_compliance_pct", "label": "supplier escalation compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier escalation compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_repeat_defect_count_06(record):
    """Evaluate supplier repeat defects for control WP-0163-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repeat_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-06", "metric": "supplier_repeat_defect_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-06", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-06", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-06", "metric": "supplier_repeat_defect_count", "label": "supplier repeat defects",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier repeat defects must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_forced_labor_screen_pct_07(record):
    """Evaluate supplier forced-labor screening for control WP-0163-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forced_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-07", "metric": "supplier_forced_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-07", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-07", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-07", "metric": "supplier_forced_labor_screen_pct", "label": "supplier forced-labor screening",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "supplier forced-labor screening exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_layoff_signal_08(record):
    """Evaluate supplier layoff signal for control WP-0163-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_layoff_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-08", "metric": "supplier_layoff_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-08", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-08", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-08", "metric": "supplier_layoff_signal", "label": "supplier layoff signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "supplier layoff signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_productivity_improvement_pct_09(record):
    """Evaluate supplier productivity improvement for control WP-0163-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_productivity_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-09", "metric": "supplier_productivity_improvement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-09", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-09", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-09", "metric": "supplier_productivity_improvement_pct", "label": "supplier productivity improvement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier productivity improvement must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_model_retraining_age_days_10(record):
    """Evaluate supplier model retraining age for control WP-0163-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_retraining_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-10", "metric": "supplier_model_retraining_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-10", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-10", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-10", "metric": "supplier_model_retraining_age_days", "label": "supplier model retraining age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model retraining age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_latency_p95_ms_11(record):
    """Evaluate supplier p95 latency for control WP-0163-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p95_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-11", "metric": "supplier_latency_p95_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-11", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-11", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-11", "metric": "supplier_latency_p95_ms", "label": "supplier p95 latency",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "supplier p95 latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_release_attestation_pct_12(record):
    """Evaluate supplier release attestation for control WP-0163-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_attestation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-12", "metric": "supplier_release_attestation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-12", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-12", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-12", "metric": "supplier_release_attestation_pct", "label": "supplier release attestation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier release attestation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_audit_response_days_13(record):
    """Evaluate supplier audit response time for control WP-0163-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_response_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-13", "metric": "supplier_audit_response_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-13", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-13", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-13", "metric": "supplier_audit_response_days", "label": "supplier audit response time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_emergency_order_pct_14(record):
    """Evaluate supplier emergency order rate for control WP-0163-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_order_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-14", "metric": "supplier_emergency_order_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-14", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-14", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-14", "metric": "supplier_emergency_order_pct", "label": "supplier emergency order rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier emergency order rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_production_yield_pct_15(record):
    """Evaluate supplier production yield for control WP-0163-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_production_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-15", "metric": "supplier_production_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-15", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-15", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-15", "metric": "supplier_production_yield_pct", "label": "supplier production yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier production yield exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_escalation_quality_score_16(record):
    """Evaluate supplier escalation quality for control WP-0163-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-16", "metric": "supplier_escalation_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-16", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-16", "metric": "supplier_escalation_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-16", "metric": "supplier_escalation_quality_score", "label": "supplier escalation quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier escalation quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_regulator_notice_pct_17(record):
    """Evaluate supplier regulator notice completion for control WP-0163-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-17", "metric": "supplier_regulator_notice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-17", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-17", "metric": "supplier_regulator_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-17", "metric": "supplier_regulator_notice_pct", "label": "supplier regulator notice completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier regulator notice completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_accuracy_pct_18(record):
    """Evaluate inventory accuracy for control WP-0163-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-18", "metric": "accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-18", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-18", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-18", "metric": "accuracy_pct", "label": "inventory accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_fraud_signal_score_19(record):
    """Evaluate fraud signal score for control WP-0163-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-19", "metric": "fraud_signal_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-19", "metric": "fraud_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-19", "metric": "fraud_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-19", "metric": "fraud_signal_score", "label": "fraud signal score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "fraud signal score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_partial_shipment_pct_20(record):
    """Evaluate partial shipment rate for control WP-0163-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("partial_shipment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-20", "metric": "partial_shipment_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-20", "metric": "partial_shipment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-20", "metric": "partial_shipment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-20", "metric": "partial_shipment_pct", "label": "partial shipment rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "partial shipment rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_pallet_stability_score_21(record):
    """Evaluate pallet stability for control WP-0163-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_stability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-21", "metric": "pallet_stability_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-21", "metric": "pallet_stability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-21", "metric": "pallet_stability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-21", "metric": "pallet_stability_score", "label": "pallet stability",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pallet stability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_restricted_item_count_22(record):
    """Evaluate restricted items for control WP-0163-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_item_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-22", "metric": "restricted_item_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-22", "metric": "restricted_item_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-22", "metric": "restricted_item_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-22", "metric": "restricted_item_count", "label": "restricted items",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restricted items must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_incident_ack_minutes_23(record):
    """Evaluate incident acknowledgement for control WP-0163-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-23", "metric": "incident_ack_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-23", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-23", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-23", "metric": "incident_ack_minutes", "label": "incident acknowledgement",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "incident acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_forecast_bias_pct_24(record):
    """Evaluate forecast bias for control WP-0163-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_bias_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0163-24", "metric": "forecast_bias_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0163-24", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0163-24", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0163-24", "metric": "forecast_bias_pct", "label": "forecast bias",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "forecast bias falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_alternate_source_test_age_days_01, assess_supplier_incident_notification_minutes_02, assess_supplier_energy_security_score_03, assess_supplier_renewable_energy_pct_04, assess_supplier_escalation_compliance_pct_05, assess_supplier_repeat_defect_count_06, assess_supplier_forced_labor_screen_pct_07, assess_supplier_layoff_signal_08, assess_supplier_productivity_improvement_pct_09, assess_supplier_model_retraining_age_days_10, assess_supplier_latency_p95_ms_11, assess_supplier_release_attestation_pct_12, assess_supplier_audit_response_days_13, assess_supplier_emergency_order_pct_14, assess_supplier_production_yield_pct_15, assess_supplier_escalation_quality_score_16, assess_supplier_regulator_notice_pct_17, assess_accuracy_pct_18, assess_fraud_signal_score_19, assess_partial_shipment_pct_20, assess_pallet_stability_score_21, assess_restricted_item_count_22, assess_incident_ack_minutes_23, assess_forecast_bias_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

