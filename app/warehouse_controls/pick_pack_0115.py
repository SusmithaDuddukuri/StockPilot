"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_feedback_capture_pct_01(record):
    """Evaluate supplier feedback capture for control WP-0115-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-01", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-01", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-01", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-01", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier feedback capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_region_failover_minutes_02(record):
    """Evaluate supplier region failover time for control WP-0115-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-02", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-02", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-02", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-02", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier region failover time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_cross_border_transfer_pct_03(record):
    """Evaluate supplier cross-border transfer compliance for control WP-0115-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_border_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-03", "metric": "supplier_cross_border_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-03", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-03", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-03", "metric": "supplier_cross_border_transfer_pct", "label": "supplier cross-border transfer compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier cross-border transfer compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_risk_appetite_variance_04(record):
    """Evaluate supplier risk appetite variance for control WP-0115-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_appetite_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-04", "metric": "supplier_risk_appetite_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-04", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-04", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-04", "metric": "supplier_risk_appetite_variance", "label": "supplier risk appetite variance",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "supplier risk appetite variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_invoice_without_receipt_count_05(record):
    """Evaluate invoice-without-receipt events for control WP-0115-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_without_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-05", "metric": "supplier_invoice_without_receipt_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-05", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-05", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-05", "metric": "supplier_invoice_without_receipt_count", "label": "invoice-without-receipt events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice-without-receipt events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_setup_time_minutes_06(record):
    """Evaluate supplier setup time for control WP-0115-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_setup_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-06", "metric": "supplier_setup_time_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-06", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-06", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-06", "metric": "supplier_setup_time_minutes", "label": "supplier setup time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier setup time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_performance_action_age_days_07(record):
    """Evaluate supplier performance action age for control WP-0115-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_performance_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-07", "metric": "supplier_performance_action_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-07", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-07", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-07", "metric": "supplier_performance_action_age_days", "label": "supplier performance action age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier performance action age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_exit_review_age_days_08(record):
    """Evaluate supplier exit review age for control WP-0115-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-08", "metric": "supplier_exit_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-08", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-08", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-08", "metric": "supplier_exit_review_age_days", "label": "supplier exit review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier exit review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_hazard_score_09(record):
    """Evaluate hazard score for control WP-0115-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-09", "metric": "hazard_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-09", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-09", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-09", "metric": "hazard_score", "label": "hazard score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "hazard score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_documentation_gap_count_10(record):
    """Evaluate documentation gaps for control WP-0115-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("documentation_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-10", "metric": "documentation_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-10", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-10", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-10", "metric": "documentation_gap_count", "label": "documentation gaps",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "documentation gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_congestion_score_11(record):
    """Evaluate congestion score for control WP-0115-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-11", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-11", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-11", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-11", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "congestion score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_charger_queue_minutes_12(record):
    """Evaluate charger queue for control WP-0115-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-12", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-12", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-12", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-12", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "charger queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_invoice_age_days_13(record):
    """Evaluate invoice age for control WP-0115-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-13", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-13", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-13", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-13", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_cache_hit_pct_14(record):
    """Evaluate cache hit rate for control WP-0115-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-14", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-14", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-14", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-14", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cache hit rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_pack_size_variance_15(record):
    """Evaluate pack-size variance for control WP-0115-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_size_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-15", "metric": "pack_size_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-15", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-15", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-15", "metric": "pack_size_variance", "label": "pack-size variance",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "pack-size variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_handover_ack_pct_16(record):
    """Evaluate handover acknowledgement for control WP-0115-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-16", "metric": "handover_ack_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-16", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-16", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-16", "metric": "handover_ack_pct", "label": "handover acknowledgement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "handover acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_environmental_incident_count_17(record):
    """Evaluate environmental incidents for control WP-0115-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("environmental_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-17", "metric": "environmental_incident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-17", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-17", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-17", "metric": "environmental_incident_count", "label": "environmental incidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "environmental incidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_dual_control_compliance_pct_18(record):
    """Evaluate dual control compliance for control WP-0115-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dual_control_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-18", "metric": "dual_control_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-18", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-18", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-18", "metric": "dual_control_compliance_pct", "label": "dual control compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dual control compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_chemical_inventory_reconcile_pct_19(record):
    """Evaluate chemical inventory reconciliation for control WP-0115-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chemical_inventory_reconcile_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-19", "metric": "chemical_inventory_reconcile_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-19", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-19", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-19", "metric": "chemical_inventory_reconcile_pct", "label": "chemical inventory reconciliation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "chemical inventory reconciliation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_spare_part_stockout_count_20(record):
    """Evaluate spare part stockouts for control WP-0115-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_part_stockout_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-20", "metric": "spare_part_stockout_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-20", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-20", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-20", "metric": "spare_part_stockout_count", "label": "spare part stockouts",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "spare part stockouts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_recovery_point_minutes_21(record):
    """Evaluate recovery point for control WP-0115-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_point_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-21", "metric": "recovery_point_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-21", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-21", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-21", "metric": "recovery_point_minutes", "label": "recovery point",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recovery point must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_record_completeness_pct_22(record):
    """Evaluate record completeness for control WP-0115-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-22", "metric": "record_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-22", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-22", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-22", "metric": "record_completeness_pct", "label": "record completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "record completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_customer_master_gap_count_23(record):
    """Evaluate customer master gaps for control WP-0115-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-23", "metric": "customer_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-23", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-23", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-23", "metric": "customer_master_gap_count", "label": "customer master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "customer master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_backup_days_24(record):
    """Evaluate backup supplier lead time for control WP-0115-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0115-24", "metric": "supplier_backup_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0115-24", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0115-24", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0115-24", "metric": "supplier_backup_days", "label": "backup supplier lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "backup supplier lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_feedback_capture_pct_01, assess_supplier_region_failover_minutes_02, assess_supplier_cross_border_transfer_pct_03, assess_supplier_risk_appetite_variance_04, assess_supplier_invoice_without_receipt_count_05, assess_supplier_setup_time_minutes_06, assess_supplier_performance_action_age_days_07, assess_supplier_exit_review_age_days_08, assess_hazard_score_09, assess_documentation_gap_count_10, assess_congestion_score_11, assess_charger_queue_minutes_12, assess_invoice_age_days_13, assess_cache_hit_pct_14, assess_pack_size_variance_15, assess_handover_ack_pct_16, assess_environmental_incident_count_17, assess_dual_control_compliance_pct_18, assess_chemical_inventory_reconcile_pct_19, assess_spare_part_stockout_count_20, assess_recovery_point_minutes_21, assess_record_completeness_pct_22, assess_customer_master_gap_count_23, assess_supplier_backup_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

