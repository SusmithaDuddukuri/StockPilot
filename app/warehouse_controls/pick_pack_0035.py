"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_invoice_timeliness_pct_01(record):
    """Evaluate supplier invoice timeliness for control WP-0035-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-01", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-01", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-01", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-01", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice timeliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_order_change_response_hours_02(record):
    """Evaluate supplier order-change response for control WP-0035-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-02", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-02", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-02", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-02", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier order-change response must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_sla_credit_age_days_03(record):
    """Evaluate supplier SLA-credit age for control WP-0035-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-03", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-03", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-03", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-03", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "supplier SLA-credit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_trace_query_minutes_04(record):
    """Evaluate supplier trace query time for control WP-0035-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-04", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-04", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-04", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-04", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "supplier trace query time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_security_guard_coverage_pct_05(record):
    """Evaluate supplier guard coverage for control WP-0035-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-05", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-05", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-05", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-05", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier guard coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_mold_backup_pct_06(record):
    """Evaluate supplier mold backup coverage for control WP-0035-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-06", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-06", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-06", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-06", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier mold backup coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_certificate_verification_age_days_07(record):
    """Evaluate supplier certificate verification age for control WP-0035-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_verification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-07", "metric": "supplier_certificate_verification_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-07", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-07", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-07", "metric": "supplier_certificate_verification_age_days", "label": "supplier certificate verification age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier certificate verification age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_conflict_disclosure_pct_08(record):
    """Evaluate supplier conflict disclosure for control WP-0035-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_disclosure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-08", "metric": "supplier_conflict_disclosure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-08", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-08", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-08", "metric": "supplier_conflict_disclosure_pct", "label": "supplier conflict disclosure",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier conflict disclosure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_crisis_comms_test_age_days_09(record):
    """Evaluate supplier crisis communications test age for control WP-0035-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-09", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-09", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-09", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-09", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier crisis communications test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_digital_twin_coverage_pct_10(record):
    """Evaluate supplier digital-twin coverage for control WP-0035-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_digital_twin_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-10", "metric": "supplier_digital_twin_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-10", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-10", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-10", "metric": "supplier_digital_twin_coverage_pct", "label": "supplier digital-twin coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier digital-twin coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_feedback_capture_pct_11(record):
    """Evaluate supplier feedback capture for control WP-0035-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-11", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-11", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-11", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-11", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier feedback capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_region_failover_minutes_12(record):
    """Evaluate supplier region failover time for control WP-0035-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-12", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-12", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-12", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-12", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier region failover time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_cross_border_transfer_pct_13(record):
    """Evaluate supplier cross-border transfer compliance for control WP-0035-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_border_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-13", "metric": "supplier_cross_border_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-13", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-13", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-13", "metric": "supplier_cross_border_transfer_pct", "label": "supplier cross-border transfer compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cross-border transfer compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_risk_appetite_variance_14(record):
    """Evaluate supplier risk appetite variance for control WP-0035-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_appetite_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-14", "metric": "supplier_risk_appetite_variance",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-14", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-14", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-14", "metric": "supplier_risk_appetite_variance", "label": "supplier risk appetite variance",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk appetite variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_invoice_without_receipt_count_15(record):
    """Evaluate invoice-without-receipt events for control WP-0035-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_without_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-15", "metric": "supplier_invoice_without_receipt_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-15", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-15", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-15", "metric": "supplier_invoice_without_receipt_count", "label": "invoice-without-receipt events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "invoice-without-receipt events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_setup_time_minutes_16(record):
    """Evaluate supplier setup time for control WP-0035-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_setup_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-16", "metric": "supplier_setup_time_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-16", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-16", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-16", "metric": "supplier_setup_time_minutes", "label": "supplier setup time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier setup time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_performance_action_age_days_17(record):
    """Evaluate supplier performance action age for control WP-0035-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_performance_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-17", "metric": "supplier_performance_action_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-17", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-17", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-17", "metric": "supplier_performance_action_age_days", "label": "supplier performance action age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier performance action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_exit_review_age_days_18(record):
    """Evaluate supplier exit review age for control WP-0035-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-18", "metric": "supplier_exit_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-18", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-18", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-18", "metric": "supplier_exit_review_age_days", "label": "supplier exit review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_hazard_score_19(record):
    """Evaluate hazard score for control WP-0035-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-19", "metric": "hazard_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-19", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-19", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-19", "metric": "hazard_score", "label": "hazard score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "hazard score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_documentation_gap_count_20(record):
    """Evaluate documentation gaps for control WP-0035-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("documentation_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-20", "metric": "documentation_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-20", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-20", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-20", "metric": "documentation_gap_count", "label": "documentation gaps",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "documentation gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_congestion_score_21(record):
    """Evaluate congestion score for control WP-0035-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-21", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-21", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-21", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-21", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "congestion score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_charger_queue_minutes_22(record):
    """Evaluate charger queue for control WP-0035-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-22", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-22", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-22", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-22", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "charger queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_invoice_age_days_23(record):
    """Evaluate invoice age for control WP-0035-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-23", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-23", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-23", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-23", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "invoice age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_cache_hit_pct_24(record):
    """Evaluate cache hit rate for control WP-0035-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0035-24", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0035-24", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0035-24", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0035-24", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "cache hit rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_invoice_timeliness_pct_01, assess_supplier_order_change_response_hours_02, assess_supplier_sla_credit_age_days_03, assess_supplier_trace_query_minutes_04, assess_supplier_security_guard_coverage_pct_05, assess_supplier_mold_backup_pct_06, assess_supplier_certificate_verification_age_days_07, assess_supplier_conflict_disclosure_pct_08, assess_supplier_crisis_comms_test_age_days_09, assess_supplier_digital_twin_coverage_pct_10, assess_supplier_feedback_capture_pct_11, assess_supplier_region_failover_minutes_12, assess_supplier_cross_border_transfer_pct_13, assess_supplier_risk_appetite_variance_14, assess_supplier_invoice_without_receipt_count_15, assess_supplier_setup_time_minutes_16, assess_supplier_performance_action_age_days_17, assess_supplier_exit_review_age_days_18, assess_hazard_score_19, assess_documentation_gap_count_20, assess_congestion_score_21, assess_charger_queue_minutes_22, assess_invoice_age_days_23, assess_cache_hit_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

