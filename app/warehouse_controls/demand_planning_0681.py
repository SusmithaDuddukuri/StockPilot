"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_crisis_comms_test_age_days_01(record):
    """Evaluate supplier crisis communications test age for control WP-0681-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-01", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-01", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-01", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-01", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier crisis communications test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_digital_twin_coverage_pct_02(record):
    """Evaluate supplier digital-twin coverage for control WP-0681-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_digital_twin_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-02", "metric": "supplier_digital_twin_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-02", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-02", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-02", "metric": "supplier_digital_twin_coverage_pct", "label": "supplier digital-twin coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "supplier digital-twin coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_feedback_capture_pct_03(record):
    """Evaluate supplier feedback capture for control WP-0681-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-03", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-03", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-03", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-03", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier feedback capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_region_failover_minutes_04(record):
    """Evaluate supplier region failover time for control WP-0681-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-04", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-04", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-04", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-04", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier region failover time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_cross_border_transfer_pct_05(record):
    """Evaluate supplier cross-border transfer compliance for control WP-0681-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_border_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-05", "metric": "supplier_cross_border_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-05", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-05", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-05", "metric": "supplier_cross_border_transfer_pct", "label": "supplier cross-border transfer compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier cross-border transfer compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_risk_appetite_variance_06(record):
    """Evaluate supplier risk appetite variance for control WP-0681-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_appetite_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-06", "metric": "supplier_risk_appetite_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-06", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-06", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-06", "metric": "supplier_risk_appetite_variance", "label": "supplier risk appetite variance",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "supplier risk appetite variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_invoice_without_receipt_count_07(record):
    """Evaluate invoice-without-receipt events for control WP-0681-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_without_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-07", "metric": "supplier_invoice_without_receipt_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-07", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-07", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-07", "metric": "supplier_invoice_without_receipt_count", "label": "invoice-without-receipt events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice-without-receipt events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_setup_time_minutes_08(record):
    """Evaluate supplier setup time for control WP-0681-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_setup_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-08", "metric": "supplier_setup_time_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-08", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-08", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-08", "metric": "supplier_setup_time_minutes", "label": "supplier setup time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier setup time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_performance_action_age_days_09(record):
    """Evaluate supplier performance action age for control WP-0681-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_performance_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-09", "metric": "supplier_performance_action_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-09", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-09", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-09", "metric": "supplier_performance_action_age_days", "label": "supplier performance action age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier performance action age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_exit_review_age_days_10(record):
    """Evaluate supplier exit review age for control WP-0681-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-10", "metric": "supplier_exit_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-10", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-10", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-10", "metric": "supplier_exit_review_age_days", "label": "supplier exit review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier exit review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_hazard_score_11(record):
    """Evaluate hazard score for control WP-0681-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-11", "metric": "hazard_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-11", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-11", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-11", "metric": "hazard_score", "label": "hazard score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "hazard score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_documentation_gap_count_12(record):
    """Evaluate documentation gaps for control WP-0681-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("documentation_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-12", "metric": "documentation_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-12", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-12", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-12", "metric": "documentation_gap_count", "label": "documentation gaps",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "documentation gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_congestion_score_13(record):
    """Evaluate congestion score for control WP-0681-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-13", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-13", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-13", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-13", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "congestion score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_charger_queue_minutes_14(record):
    """Evaluate charger queue for control WP-0681-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-14", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-14", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-14", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-14", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "charger queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_invoice_age_days_15(record):
    """Evaluate invoice age for control WP-0681-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-15", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-15", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-15", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-15", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_cache_hit_pct_16(record):
    """Evaluate cache hit rate for control WP-0681-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-16", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-16", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-16", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-16", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cache hit rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_pack_size_variance_17(record):
    """Evaluate pack-size variance for control WP-0681-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_size_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-17", "metric": "pack_size_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-17", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-17", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-17", "metric": "pack_size_variance", "label": "pack-size variance",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "pack-size variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_handover_ack_pct_18(record):
    """Evaluate handover acknowledgement for control WP-0681-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-18", "metric": "handover_ack_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-18", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-18", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-18", "metric": "handover_ack_pct", "label": "handover acknowledgement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "handover acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_environmental_incident_count_19(record):
    """Evaluate environmental incidents for control WP-0681-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("environmental_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-19", "metric": "environmental_incident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-19", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-19", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-19", "metric": "environmental_incident_count", "label": "environmental incidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "environmental incidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_dual_control_compliance_pct_20(record):
    """Evaluate dual control compliance for control WP-0681-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dual_control_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-20", "metric": "dual_control_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-20", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-20", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-20", "metric": "dual_control_compliance_pct", "label": "dual control compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dual control compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_chemical_inventory_reconcile_pct_21(record):
    """Evaluate chemical inventory reconciliation for control WP-0681-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chemical_inventory_reconcile_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-21", "metric": "chemical_inventory_reconcile_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-21", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-21", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-21", "metric": "chemical_inventory_reconcile_pct", "label": "chemical inventory reconciliation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "chemical inventory reconciliation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_spare_part_stockout_count_22(record):
    """Evaluate spare part stockouts for control WP-0681-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_part_stockout_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-22", "metric": "spare_part_stockout_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-22", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-22", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-22", "metric": "spare_part_stockout_count", "label": "spare part stockouts",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "spare part stockouts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_recovery_point_minutes_23(record):
    """Evaluate recovery point for control WP-0681-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_point_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-23", "metric": "recovery_point_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-23", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-23", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-23", "metric": "recovery_point_minutes", "label": "recovery point",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recovery point must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_record_completeness_pct_24(record):
    """Evaluate record completeness for control WP-0681-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0681-24", "metric": "record_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0681-24", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0681-24", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0681-24", "metric": "record_completeness_pct", "label": "record completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "record completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_supplier_crisis_comms_test_age_days_01, assess_supplier_digital_twin_coverage_pct_02, assess_supplier_feedback_capture_pct_03, assess_supplier_region_failover_minutes_04, assess_supplier_cross_border_transfer_pct_05, assess_supplier_risk_appetite_variance_06, assess_supplier_invoice_without_receipt_count_07, assess_supplier_setup_time_minutes_08, assess_supplier_performance_action_age_days_09, assess_supplier_exit_review_age_days_10, assess_hazard_score_11, assess_documentation_gap_count_12, assess_congestion_score_13, assess_charger_queue_minutes_14, assess_invoice_age_days_15, assess_cache_hit_pct_16, assess_pack_size_variance_17, assess_handover_ack_pct_18, assess_environmental_incident_count_19, assess_dual_control_compliance_pct_20, assess_chemical_inventory_reconcile_pct_21, assess_spare_part_stockout_count_22, assess_recovery_point_minutes_23, assess_record_completeness_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

