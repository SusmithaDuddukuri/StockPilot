"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_sla_credit_age_days_01(record):
    """Evaluate supplier SLA-credit age for control WP-0545-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-01", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-01", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-01", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-01", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier SLA-credit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_trace_query_minutes_02(record):
    """Evaluate supplier trace query time for control WP-0545-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-02", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-02", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-02", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-02", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier trace query time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_security_guard_coverage_pct_03(record):
    """Evaluate supplier guard coverage for control WP-0545-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-03", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-03", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-03", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-03", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier guard coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_mold_backup_pct_04(record):
    """Evaluate supplier mold backup coverage for control WP-0545-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-04", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-04", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-04", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-04", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier mold backup coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_certificate_verification_age_days_05(record):
    """Evaluate supplier certificate verification age for control WP-0545-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_verification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-05", "metric": "supplier_certificate_verification_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-05", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-05", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-05", "metric": "supplier_certificate_verification_age_days", "label": "supplier certificate verification age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier certificate verification age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_conflict_disclosure_pct_06(record):
    """Evaluate supplier conflict disclosure for control WP-0545-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_disclosure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-06", "metric": "supplier_conflict_disclosure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-06", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-06", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-06", "metric": "supplier_conflict_disclosure_pct", "label": "supplier conflict disclosure",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier conflict disclosure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_crisis_comms_test_age_days_07(record):
    """Evaluate supplier crisis communications test age for control WP-0545-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-07", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-07", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-07", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-07", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier crisis communications test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_digital_twin_coverage_pct_08(record):
    """Evaluate supplier digital-twin coverage for control WP-0545-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_digital_twin_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-08", "metric": "supplier_digital_twin_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-08", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-08", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-08", "metric": "supplier_digital_twin_coverage_pct", "label": "supplier digital-twin coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier digital-twin coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_feedback_capture_pct_09(record):
    """Evaluate supplier feedback capture for control WP-0545-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-09", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-09", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-09", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-09", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "supplier feedback capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_region_failover_minutes_10(record):
    """Evaluate supplier region failover time for control WP-0545-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-10", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-10", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-10", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-10", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier region failover time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_cross_border_transfer_pct_11(record):
    """Evaluate supplier cross-border transfer compliance for control WP-0545-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_border_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-11", "metric": "supplier_cross_border_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-11", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-11", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-11", "metric": "supplier_cross_border_transfer_pct", "label": "supplier cross-border transfer compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cross-border transfer compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_risk_appetite_variance_12(record):
    """Evaluate supplier risk appetite variance for control WP-0545-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_appetite_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-12", "metric": "supplier_risk_appetite_variance",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-12", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-12", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-12", "metric": "supplier_risk_appetite_variance", "label": "supplier risk appetite variance",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk appetite variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_invoice_without_receipt_count_13(record):
    """Evaluate invoice-without-receipt events for control WP-0545-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_without_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-13", "metric": "supplier_invoice_without_receipt_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-13", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-13", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-13", "metric": "supplier_invoice_without_receipt_count", "label": "invoice-without-receipt events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "invoice-without-receipt events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_setup_time_minutes_14(record):
    """Evaluate supplier setup time for control WP-0545-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_setup_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-14", "metric": "supplier_setup_time_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-14", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-14", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-14", "metric": "supplier_setup_time_minutes", "label": "supplier setup time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier setup time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_performance_action_age_days_15(record):
    """Evaluate supplier performance action age for control WP-0545-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_performance_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-15", "metric": "supplier_performance_action_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-15", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-15", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-15", "metric": "supplier_performance_action_age_days", "label": "supplier performance action age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier performance action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_exit_review_age_days_16(record):
    """Evaluate supplier exit review age for control WP-0545-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-16", "metric": "supplier_exit_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-16", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-16", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-16", "metric": "supplier_exit_review_age_days", "label": "supplier exit review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_hazard_score_17(record):
    """Evaluate hazard score for control WP-0545-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-17", "metric": "hazard_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-17", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-17", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-17", "metric": "hazard_score", "label": "hazard score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "hazard score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_documentation_gap_count_18(record):
    """Evaluate documentation gaps for control WP-0545-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("documentation_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-18", "metric": "documentation_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-18", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-18", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-18", "metric": "documentation_gap_count", "label": "documentation gaps",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "documentation gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_congestion_score_19(record):
    """Evaluate congestion score for control WP-0545-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-19", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-19", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-19", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-19", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "congestion score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_charger_queue_minutes_20(record):
    """Evaluate charger queue for control WP-0545-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-20", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-20", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-20", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-20", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "charger queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_invoice_age_days_21(record):
    """Evaluate invoice age for control WP-0545-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-21", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-21", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-21", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-21", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "invoice age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_cache_hit_pct_22(record):
    """Evaluate cache hit rate for control WP-0545-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-22", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-22", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-22", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-22", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "cache hit rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_pack_size_variance_23(record):
    """Evaluate pack-size variance for control WP-0545-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_size_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-23", "metric": "pack_size_variance",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-23", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-23", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-23", "metric": "pack_size_variance", "label": "pack-size variance",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pack-size variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_handover_ack_pct_24(record):
    """Evaluate handover acknowledgement for control WP-0545-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0545-24", "metric": "handover_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0545-24", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0545-24", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0545-24", "metric": "handover_ack_pct", "label": "handover acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "handover acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_sla_credit_age_days_01, assess_supplier_trace_query_minutes_02, assess_supplier_security_guard_coverage_pct_03, assess_supplier_mold_backup_pct_04, assess_supplier_certificate_verification_age_days_05, assess_supplier_conflict_disclosure_pct_06, assess_supplier_crisis_comms_test_age_days_07, assess_supplier_digital_twin_coverage_pct_08, assess_supplier_feedback_capture_pct_09, assess_supplier_region_failover_minutes_10, assess_supplier_cross_border_transfer_pct_11, assess_supplier_risk_appetite_variance_12, assess_supplier_invoice_without_receipt_count_13, assess_supplier_setup_time_minutes_14, assess_supplier_performance_action_age_days_15, assess_supplier_exit_review_age_days_16, assess_hazard_score_17, assess_documentation_gap_count_18, assess_congestion_score_19, assess_charger_queue_minutes_20, assess_invoice_age_days_21, assess_cache_hit_pct_22, assess_pack_size_variance_23, assess_handover_ack_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

