"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_certification_scope_gap_count_01(record):
    """Evaluate supplier certification scope gaps for control WP-0235-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_scope_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-01", "metric": "supplier_certification_scope_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-01", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-01", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-01", "metric": "supplier_certification_scope_gap_count", "label": "supplier certification scope gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier certification scope gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_gift_register_gap_count_02(record):
    """Evaluate supplier gift-register gaps for control WP-0235-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gift_register_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-02", "metric": "supplier_gift_register_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-02", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-02", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-02", "metric": "supplier_gift_register_gap_count", "label": "supplier gift-register gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier gift-register gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_bcp_contact_age_days_03(record):
    """Evaluate supplier BCP contact age for control WP-0235-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-03", "metric": "supplier_bcp_contact_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-03", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-03", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-03", "metric": "supplier_bcp_contact_age_days", "label": "supplier BCP contact age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier BCP contact age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_automation_coverage_pct_04(record):
    """Evaluate supplier automation coverage for control WP-0235-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_automation_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-04", "metric": "supplier_automation_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-04", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-04", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-04", "metric": "supplier_automation_coverage_pct", "label": "supplier automation coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier automation coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_human_review_queue_age_hours_05(record):
    """Evaluate supplier human review queue age for control WP-0235-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_review_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-05", "metric": "supplier_human_review_queue_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-05", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-05", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-05", "metric": "supplier_human_review_queue_age_hours", "label": "supplier human review queue age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier human review queue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_failover_test_age_days_06(record):
    """Evaluate supplier failover test age for control WP-0235-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_failover_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-06", "metric": "supplier_failover_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-06", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-06", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-06", "metric": "supplier_failover_test_age_days", "label": "supplier failover test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier failover test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_subprocessor_notice_pct_07(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0235-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-07", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-07", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-07", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-07", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier subprocessor notice compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_kri_breach_count_08(record):
    """Evaluate supplier KRI breaches for control WP-0235-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-08", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-08", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-08", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-08", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "supplier KRI breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_po_after_invoice_count_09(record):
    """Evaluate PO-after-invoice events for control WP-0235-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-09", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-09", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-09", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-09", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "PO-after-invoice events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tool_changeover_minutes_10(record):
    """Evaluate supplier tool changeover for control WP-0235-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tool_changeover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-10", "metric": "supplier_tool_changeover_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-10", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-10", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-10", "metric": "supplier_tool_changeover_minutes", "label": "supplier tool changeover",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tool changeover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_reporting_lag_hours_11(record):
    """Evaluate supplier reporting lag for control WP-0235-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reporting_lag_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-11", "metric": "supplier_reporting_lag_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-11", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-11", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-11", "metric": "supplier_reporting_lag_hours", "label": "supplier reporting lag",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier reporting lag exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_retention_exception_resolution_pct_12(record):
    """Evaluate supplier retention exception resolution for control WP-0235-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-12", "metric": "supplier_retention_exception_resolution_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-12", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-12", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-12", "metric": "supplier_retention_exception_resolution_pct", "label": "supplier retention exception resolution",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier retention exception resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_weight_kg_13(record):
    """Evaluate handling weight for control WP-0235-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-13", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-13", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-13", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-13", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "handling weight must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_seal_mismatch_count_14(record):
    """Evaluate seal mismatches for control WP-0235-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-14", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-14", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-14", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-14", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "seal mismatches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_pick_path_efficiency_pct_15(record):
    """Evaluate pick path efficiency for control WP-0235-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-15", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-15", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-15", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-15", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "pick path efficiency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_mean_time_between_failures_hours_16(record):
    """Evaluate mean time between failures for control WP-0235-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-16", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-16", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-16", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-16", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "mean time between failures falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_payment_term_days_17(record):
    """Evaluate payment terms for control WP-0235-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-17", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-17", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-17", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-17", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment terms must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_database_connection_pct_18(record):
    """Evaluate database connection utilization for control WP-0235-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-18", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-18", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-18", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-18", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "database connection utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_moq_violation_count_19(record):
    """Evaluate minimum order quantity violations for control WP-0235-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("moq_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-19", "metric": "moq_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-19", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-19", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-19", "metric": "moq_violation_count", "label": "minimum order quantity violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "minimum order quantity violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_shift_length_hours_20(record):
    """Evaluate shift length for control WP-0235-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_length_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-20", "metric": "shift_length_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-20", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-20", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-20", "metric": "shift_length_hours", "label": "shift length",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "shift length falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_waste_manifest_pct_21(record):
    """Evaluate waste manifest completion for control WP-0235-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-21", "metric": "waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-21", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-21", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-21", "metric": "waste_manifest_pct", "label": "waste manifest completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "waste manifest completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_tamper_evident_seal_pct_22(record):
    """Evaluate tamper-evident seal use for control WP-0235-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_evident_seal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-22", "metric": "tamper_evident_seal_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-22", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-22", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-22", "metric": "tamper_evident_seal_pct", "label": "tamper-evident seal use",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "tamper-evident seal use must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_gas_detector_test_age_days_23(record):
    """Evaluate gas detector test age for control WP-0235-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gas_detector_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-23", "metric": "gas_detector_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-23", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-23", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-23", "metric": "gas_detector_test_age_days", "label": "gas detector test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "gas detector test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_maintenance_backlog_count_24(record):
    """Evaluate maintenance backlog for control WP-0235-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_backlog_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0235-24", "metric": "maintenance_backlog_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "jobs",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0235-24", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0235-24", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0235-24", "metric": "maintenance_backlog_count", "label": "maintenance backlog",
        "status": "breach", "severity": "high", "unit": "jobs",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "maintenance backlog falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_certification_scope_gap_count_01, assess_supplier_gift_register_gap_count_02, assess_supplier_bcp_contact_age_days_03, assess_supplier_automation_coverage_pct_04, assess_supplier_human_review_queue_age_hours_05, assess_supplier_failover_test_age_days_06, assess_supplier_subprocessor_notice_pct_07, assess_supplier_kri_breach_count_08, assess_supplier_po_after_invoice_count_09, assess_supplier_tool_changeover_minutes_10, assess_supplier_reporting_lag_hours_11, assess_supplier_retention_exception_resolution_pct_12, assess_weight_kg_13, assess_seal_mismatch_count_14, assess_pick_path_efficiency_pct_15, assess_mean_time_between_failures_hours_16, assess_payment_term_days_17, assess_database_connection_pct_18, assess_moq_violation_count_19, assess_shift_length_hours_20, assess_waste_manifest_pct_21, assess_tamper_evident_seal_pct_22, assess_gas_detector_test_age_days_23, assess_maintenance_backlog_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

