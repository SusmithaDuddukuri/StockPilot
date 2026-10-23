"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_runbook_test_age_days_01(record):
    """Evaluate runbook test age for control WP-0338-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("runbook_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-01", "metric": "runbook_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-01", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-01", "metric": "runbook_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-01", "metric": "runbook_test_age_days", "label": "runbook test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "runbook test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_warehouse_sync_age_minutes_02(record):
    """Evaluate warehouse sync age for control WP-0338-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_sync_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-02", "metric": "warehouse_sync_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-02", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-02", "metric": "warehouse_sync_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-02", "metric": "warehouse_sync_age_minutes", "label": "warehouse sync age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "warehouse sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_recall_notification_pct_03(record):
    """Evaluate recall notification completion for control WP-0338-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-03", "metric": "recall_notification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-03", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-03", "metric": "recall_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-03", "metric": "recall_notification_pct", "label": "recall notification completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "recall notification completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_receiving_queue_orders_04(record):
    """Evaluate receiving queue for control WP-0338-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_queue_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-04", "metric": "receiving_queue_orders",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-04", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-04", "metric": "receiving_queue_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-04", "metric": "receiving_queue_orders", "label": "receiving queue",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receiving queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_customer_retention_pct_05(record):
    """Evaluate customer retention for control WP-0338-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-05", "metric": "customer_retention_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-05", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-05", "metric": "customer_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-05", "metric": "customer_retention_pct", "label": "customer retention",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_railcar_dwell_hours_06(record):
    """Evaluate railcar dwell for control WP-0338-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("railcar_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-06", "metric": "railcar_dwell_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-06", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-06", "metric": "railcar_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-06", "metric": "railcar_dwell_hours", "label": "railcar dwell",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "railcar dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_cost_per_line_07(record):
    """Evaluate cost per line for control WP-0338-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_line")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-07", "metric": "cost_per_line",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-07", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-07", "metric": "cost_per_line", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-07", "metric": "cost_per_line", "label": "cost per line",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "cost per line falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_labor_audit_gap_count_08(record):
    """Evaluate supplier labor audit gaps for control WP-0338-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-08", "metric": "supplier_labor_audit_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-08", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-08", "metric": "supplier_labor_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-08", "metric": "supplier_labor_audit_gap_count", "label": "supplier labor audit gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier labor audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_cyber_maturity_score_09(record):
    """Evaluate supplier cyber maturity for control WP-0338-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cyber_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-09", "metric": "supplier_cyber_maturity_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-09", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-09", "metric": "supplier_cyber_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-09", "metric": "supplier_cyber_maturity_score", "label": "supplier cyber maturity",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cyber maturity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_alternate_source_test_age_days_10(record):
    """Evaluate alternate-source test age for control WP-0338-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_source_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-10", "metric": "supplier_alternate_source_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-10", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-10", "metric": "supplier_alternate_source_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-10", "metric": "supplier_alternate_source_test_age_days", "label": "alternate-source test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "alternate-source test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_incident_notification_minutes_11(record):
    """Evaluate supplier incident notification time for control WP-0338-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_incident_notification_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-11", "metric": "supplier_incident_notification_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-11", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-11", "metric": "supplier_incident_notification_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-11", "metric": "supplier_incident_notification_minutes", "label": "supplier incident notification time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier incident notification time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_energy_security_score_12(record):
    """Evaluate supplier energy security for control WP-0338-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-12", "metric": "supplier_energy_security_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-12", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-12", "metric": "supplier_energy_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-12", "metric": "supplier_energy_security_score", "label": "supplier energy security",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy security must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_renewable_energy_pct_13(record):
    """Evaluate supplier renewable energy share for control WP-0338-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_renewable_energy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-13", "metric": "supplier_renewable_energy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-13", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-13", "metric": "supplier_renewable_energy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-13", "metric": "supplier_renewable_energy_pct", "label": "supplier renewable energy share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier renewable energy share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_escalation_compliance_pct_14(record):
    """Evaluate supplier escalation compliance for control WP-0338-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-14", "metric": "supplier_escalation_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-14", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-14", "metric": "supplier_escalation_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-14", "metric": "supplier_escalation_compliance_pct", "label": "supplier escalation compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "supplier escalation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_repeat_defect_count_15(record):
    """Evaluate supplier repeat defects for control WP-0338-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repeat_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-15", "metric": "supplier_repeat_defect_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-15", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-15", "metric": "supplier_repeat_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-15", "metric": "supplier_repeat_defect_count", "label": "supplier repeat defects",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier repeat defects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_forced_labor_screen_pct_16(record):
    """Evaluate supplier forced-labor screening for control WP-0338-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forced_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-16", "metric": "supplier_forced_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-16", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-16", "metric": "supplier_forced_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-16", "metric": "supplier_forced_labor_screen_pct", "label": "supplier forced-labor screening",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier forced-labor screening must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_layoff_signal_17(record):
    """Evaluate supplier layoff signal for control WP-0338-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_layoff_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-17", "metric": "supplier_layoff_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-17", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-17", "metric": "supplier_layoff_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-17", "metric": "supplier_layoff_signal", "label": "supplier layoff signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier layoff signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_productivity_improvement_pct_18(record):
    """Evaluate supplier productivity improvement for control WP-0338-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_productivity_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-18", "metric": "supplier_productivity_improvement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-18", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-18", "metric": "supplier_productivity_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-18", "metric": "supplier_productivity_improvement_pct", "label": "supplier productivity improvement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier productivity improvement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_model_retraining_age_days_19(record):
    """Evaluate supplier model retraining age for control WP-0338-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_retraining_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-19", "metric": "supplier_model_retraining_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-19", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-19", "metric": "supplier_model_retraining_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-19", "metric": "supplier_model_retraining_age_days", "label": "supplier model retraining age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier model retraining age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_latency_p95_ms_20(record):
    """Evaluate supplier p95 latency for control WP-0338-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p95_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-20", "metric": "supplier_latency_p95_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-20", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-20", "metric": "supplier_latency_p95_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-20", "metric": "supplier_latency_p95_ms", "label": "supplier p95 latency",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier p95 latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_release_attestation_pct_21(record):
    """Evaluate supplier release attestation for control WP-0338-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_attestation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-21", "metric": "supplier_release_attestation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-21", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-21", "metric": "supplier_release_attestation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-21", "metric": "supplier_release_attestation_pct", "label": "supplier release attestation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier release attestation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_audit_response_days_22(record):
    """Evaluate supplier audit response time for control WP-0338-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_response_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-22", "metric": "supplier_audit_response_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-22", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-22", "metric": "supplier_audit_response_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-22", "metric": "supplier_audit_response_days", "label": "supplier audit response time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier audit response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_emergency_order_pct_23(record):
    """Evaluate supplier emergency order rate for control WP-0338-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emergency_order_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-23", "metric": "supplier_emergency_order_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-23", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-23", "metric": "supplier_emergency_order_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-23", "metric": "supplier_emergency_order_pct", "label": "supplier emergency order rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier emergency order rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_production_yield_pct_24(record):
    """Evaluate supplier production yield for control WP-0338-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_production_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0338-24", "metric": "supplier_production_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0338-24", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0338-24", "metric": "supplier_production_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0338-24", "metric": "supplier_production_yield_pct", "label": "supplier production yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier production yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_runbook_test_age_days_01, assess_warehouse_sync_age_minutes_02, assess_recall_notification_pct_03, assess_receiving_queue_orders_04, assess_customer_retention_pct_05, assess_railcar_dwell_hours_06, assess_cost_per_line_07, assess_supplier_labor_audit_gap_count_08, assess_supplier_cyber_maturity_score_09, assess_supplier_alternate_source_test_age_days_10, assess_supplier_incident_notification_minutes_11, assess_supplier_energy_security_score_12, assess_supplier_renewable_energy_pct_13, assess_supplier_escalation_compliance_pct_14, assess_supplier_repeat_defect_count_15, assess_supplier_forced_labor_screen_pct_16, assess_supplier_layoff_signal_17, assess_supplier_productivity_improvement_pct_18, assess_supplier_model_retraining_age_days_19, assess_supplier_latency_p95_ms_20, assess_supplier_release_attestation_pct_21, assess_supplier_audit_response_days_22, assess_supplier_emergency_order_pct_23, assess_supplier_production_yield_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

