"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_overtime_cost_pct_01(record):
    """Evaluate overtime cost share for control WP-0222-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-01", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-01", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-01", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-01", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "overtime cost share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_over_ship_pct_02(record):
    """Evaluate supplier over-ship rate for control WP-0222-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-02", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-02", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-02", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-02", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier over-ship rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_invoice_timeliness_pct_03(record):
    """Evaluate supplier invoice timeliness for control WP-0222-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-03", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-03", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-03", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-03", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier invoice timeliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_order_change_response_hours_04(record):
    """Evaluate supplier order-change response for control WP-0222-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-04", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-04", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-04", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-04", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier order-change response must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_sla_credit_age_days_05(record):
    """Evaluate supplier SLA-credit age for control WP-0222-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-05", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-05", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-05", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-05", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SLA-credit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_trace_query_minutes_06(record):
    """Evaluate supplier trace query time for control WP-0222-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-06", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-06", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-06", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-06", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier trace query time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_security_guard_coverage_pct_07(record):
    """Evaluate supplier guard coverage for control WP-0222-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-07", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-07", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-07", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-07", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier guard coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_mold_backup_pct_08(record):
    """Evaluate supplier mold backup coverage for control WP-0222-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-08", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-08", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-08", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-08", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier mold backup coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_certificate_verification_age_days_09(record):
    """Evaluate supplier certificate verification age for control WP-0222-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_verification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-09", "metric": "supplier_certificate_verification_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-09", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-09", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-09", "metric": "supplier_certificate_verification_age_days", "label": "supplier certificate verification age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier certificate verification age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_conflict_disclosure_pct_10(record):
    """Evaluate supplier conflict disclosure for control WP-0222-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_disclosure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-10", "metric": "supplier_conflict_disclosure_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-10", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-10", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-10", "metric": "supplier_conflict_disclosure_pct", "label": "supplier conflict disclosure",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier conflict disclosure exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_crisis_comms_test_age_days_11(record):
    """Evaluate supplier crisis communications test age for control WP-0222-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-11", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-11", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-11", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-11", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "supplier crisis communications test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_digital_twin_coverage_pct_12(record):
    """Evaluate supplier digital-twin coverage for control WP-0222-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_digital_twin_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-12", "metric": "supplier_digital_twin_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-12", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-12", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-12", "metric": "supplier_digital_twin_coverage_pct", "label": "supplier digital-twin coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier digital-twin coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_feedback_capture_pct_13(record):
    """Evaluate supplier feedback capture for control WP-0222-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-13", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-13", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-13", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-13", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier feedback capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_region_failover_minutes_14(record):
    """Evaluate supplier region failover time for control WP-0222-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-14", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-14", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-14", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-14", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier region failover time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_cross_border_transfer_pct_15(record):
    """Evaluate supplier cross-border transfer compliance for control WP-0222-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_border_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-15", "metric": "supplier_cross_border_transfer_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-15", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-15", "metric": "supplier_cross_border_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-15", "metric": "supplier_cross_border_transfer_pct", "label": "supplier cross-border transfer compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "supplier cross-border transfer compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_risk_appetite_variance_16(record):
    """Evaluate supplier risk appetite variance for control WP-0222-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_appetite_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-16", "metric": "supplier_risk_appetite_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-16", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-16", "metric": "supplier_risk_appetite_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-16", "metric": "supplier_risk_appetite_variance", "label": "supplier risk appetite variance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk appetite variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_invoice_without_receipt_count_17(record):
    """Evaluate invoice-without-receipt events for control WP-0222-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_without_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-17", "metric": "supplier_invoice_without_receipt_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-17", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-17", "metric": "supplier_invoice_without_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-17", "metric": "supplier_invoice_without_receipt_count", "label": "invoice-without-receipt events",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "invoice-without-receipt events must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_setup_time_minutes_18(record):
    """Evaluate supplier setup time for control WP-0222-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_setup_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-18", "metric": "supplier_setup_time_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-18", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-18", "metric": "supplier_setup_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-18", "metric": "supplier_setup_time_minutes", "label": "supplier setup time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier setup time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_performance_action_age_days_19(record):
    """Evaluate supplier performance action age for control WP-0222-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_performance_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-19", "metric": "supplier_performance_action_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-19", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-19", "metric": "supplier_performance_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-19", "metric": "supplier_performance_action_age_days", "label": "supplier performance action age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier performance action age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_exit_review_age_days_20(record):
    """Evaluate supplier exit review age for control WP-0222-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-20", "metric": "supplier_exit_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-20", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-20", "metric": "supplier_exit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-20", "metric": "supplier_exit_review_age_days", "label": "supplier exit review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exit review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_hazard_score_21(record):
    """Evaluate hazard score for control WP-0222-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-21", "metric": "hazard_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-21", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-21", "metric": "hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-21", "metric": "hazard_score", "label": "hazard score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "hazard score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_documentation_gap_count_22(record):
    """Evaluate documentation gaps for control WP-0222-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("documentation_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-22", "metric": "documentation_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-22", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-22", "metric": "documentation_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-22", "metric": "documentation_gap_count", "label": "documentation gaps",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "documentation gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_congestion_score_23(record):
    """Evaluate congestion score for control WP-0222-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-23", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-23", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-23", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-23", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "congestion score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_charger_queue_minutes_24(record):
    """Evaluate charger queue for control WP-0222-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0222-24", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0222-24", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0222-24", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0222-24", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "charger queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_overtime_cost_pct_01, assess_supplier_over_ship_pct_02, assess_supplier_invoice_timeliness_pct_03, assess_supplier_order_change_response_hours_04, assess_supplier_sla_credit_age_days_05, assess_supplier_trace_query_minutes_06, assess_supplier_security_guard_coverage_pct_07, assess_supplier_mold_backup_pct_08, assess_supplier_certificate_verification_age_days_09, assess_supplier_conflict_disclosure_pct_10, assess_supplier_crisis_comms_test_age_days_11, assess_supplier_digital_twin_coverage_pct_12, assess_supplier_feedback_capture_pct_13, assess_supplier_region_failover_minutes_14, assess_supplier_cross_border_transfer_pct_15, assess_supplier_risk_appetite_variance_16, assess_supplier_invoice_without_receipt_count_17, assess_supplier_setup_time_minutes_18, assess_supplier_performance_action_age_days_19, assess_supplier_exit_review_age_days_20, assess_hazard_score_21, assess_documentation_gap_count_22, assess_congestion_score_23, assess_charger_queue_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

