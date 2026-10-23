"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_payment_delay_days_01(record):
    """Evaluate supplier payment delay for control WP-0103-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-01", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-01", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-01", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-01", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_takeback_compliance_pct_02(record):
    """Evaluate supplier take-back compliance for control WP-0103-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-02", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-02", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-02", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-02", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier take-back compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_inventory_visibility_pct_03(record):
    """Evaluate supplier inventory visibility for control WP-0103-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-03", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-03", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-03", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-03", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "supplier inventory visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_capability_study_age_days_04(record):
    """Evaluate supplier capability-study age for control WP-0103-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-04", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-04", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-04", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-04", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "supplier capability-study age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_worker_grievance_age_days_05(record):
    """Evaluate supplier worker grievance age for control WP-0103-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-05", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-05", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-05", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-05", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier worker grievance age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_credit_rating_score_06(record):
    """Evaluate supplier credit rating for control WP-0103-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-06", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-06", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-06", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-06", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit rating must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_internal_audit_age_days_07(record):
    """Evaluate supplier internal audit age for control WP-0103-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_internal_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-07", "metric": "supplier_internal_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-07", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-07", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-07", "metric": "supplier_internal_audit_age_days", "label": "supplier internal audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier internal audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_prompt_injection_test_age_days_08(record):
    """Evaluate supplier prompt-injection test age for control WP-0103-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prompt_injection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-08", "metric": "supplier_prompt_injection_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-08", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-08", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-08", "metric": "supplier_prompt_injection_test_age_days", "label": "supplier prompt-injection test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier prompt-injection test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_correlation_id_missing_pct_09(record):
    """Evaluate supplier correlation ID missing for control WP-0103-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_correlation_id_missing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-09", "metric": "supplier_correlation_id_missing_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-09", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-09", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-09", "metric": "supplier_correlation_id_missing_pct", "label": "supplier correlation ID missing",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier correlation ID missing must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_static_analysis_pct_10(record):
    """Evaluate supplier static analysis coverage for control WP-0103-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_static_analysis_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-10", "metric": "supplier_static_analysis_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-10", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-10", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-10", "metric": "supplier_static_analysis_pct", "label": "supplier static analysis coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier static analysis coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_joiner_mover_leaver_age_hours_11(record):
    """Evaluate supplier JML processing time for control WP-0103-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joiner_mover_leaver_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-11", "metric": "supplier_joiner_mover_leaver_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-11", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-11", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-11", "metric": "supplier_joiner_mover_leaver_age_hours", "label": "supplier JML processing time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier JML processing time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_unusual_price_signal_12(record):
    """Evaluate supplier unusual-price signal for control WP-0103-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_unusual_price_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-12", "metric": "supplier_unusual_price_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-12", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-12", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-12", "metric": "supplier_unusual_price_signal", "label": "supplier unusual-price signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "supplier unusual-price signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_delivery_window_change_count_13(record):
    """Evaluate delivery-window changes for control WP-0103-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_window_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-13", "metric": "supplier_delivery_window_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-13", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-13", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-13", "metric": "supplier_delivery_window_change_count", "label": "delivery-window changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery-window changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_invoice_upload_age_hours_14(record):
    """Evaluate supplier invoice upload age for control WP-0103-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-14", "metric": "supplier_invoice_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-14", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-14", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-14", "metric": "supplier_invoice_upload_age_hours", "label": "supplier invoice upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier invoice upload age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_dns_cutover_age_hours_15(record):
    """Evaluate supplier DNS cutover age for control WP-0103-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dns_cutover_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-15", "metric": "supplier_dns_cutover_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-15", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-15", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-15", "metric": "supplier_dns_cutover_age_hours", "label": "supplier DNS cutover age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier DNS cutover age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_pack_rate_16(record):
    """Evaluate packing rate for control WP-0103-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-16", "metric": "pack_rate",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders/hour",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-16", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-16", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-16", "metric": "pack_rate", "label": "packing rate",
        "status": "breach", "severity": "high", "unit": "orders/hour",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "packing rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_forklift_inspection_age_days_17(record):
    """Evaluate inspection age for control WP-0103-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-17", "metric": "forklift_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-17", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-17", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-17", "metric": "forklift_inspection_age_days", "label": "inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inspection age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_audit_gap_count_18(record):
    """Evaluate audit gaps for control WP-0103-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-18", "metric": "audit_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-18", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-18", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-18", "metric": "audit_gap_count", "label": "audit gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_stockout_hours_19(record):
    """Evaluate stockout duration for control WP-0103-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stockout_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-19", "metric": "stockout_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-19", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-19", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-19", "metric": "stockout_hours", "label": "stockout duration",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "stockout duration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_driver_hours_remaining_20(record):
    """Evaluate driver hours remaining for control WP-0103-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_hours_remaining")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-20", "metric": "driver_hours_remaining",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-20", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-20", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-20", "metric": "driver_hours_remaining", "label": "driver hours remaining",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "driver hours remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_privileged_account_count_21(record):
    """Evaluate privileged accounts for control WP-0103-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privileged_account_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-21", "metric": "privileged_account_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "accounts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-21", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-21", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-21", "metric": "privileged_account_count", "label": "privileged accounts",
        "status": "breach", "severity": "critical", "unit": "accounts",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "privileged accounts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_handover_gap_count_22(record):
    """Evaluate handover gaps for control WP-0103-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-22", "metric": "handover_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-22", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-22", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-22", "metric": "handover_gap_count", "label": "handover gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "handover gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_sprinkler_inspection_age_days_23(record):
    """Evaluate sprinkler inspection age for control WP-0103-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-23", "metric": "sprinkler_inspection_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-23", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-23", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-23", "metric": "sprinkler_inspection_age_days", "label": "sprinkler inspection age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "sprinkler inspection age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_recipient_match_pct_24(record):
    """Evaluate recipient match for control WP-0103-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recipient_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0103-24", "metric": "recipient_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0103-24", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0103-24", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0103-24", "metric": "recipient_match_pct", "label": "recipient match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "recipient match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_payment_delay_days_01, assess_supplier_takeback_compliance_pct_02, assess_supplier_inventory_visibility_pct_03, assess_supplier_capability_study_age_days_04, assess_supplier_worker_grievance_age_days_05, assess_supplier_credit_rating_score_06, assess_supplier_internal_audit_age_days_07, assess_supplier_prompt_injection_test_age_days_08, assess_supplier_correlation_id_missing_pct_09, assess_supplier_static_analysis_pct_10, assess_supplier_joiner_mover_leaver_age_hours_11, assess_supplier_unusual_price_signal_12, assess_supplier_delivery_window_change_count_13, assess_supplier_invoice_upload_age_hours_14, assess_supplier_dns_cutover_age_hours_15, assess_pack_rate_16, assess_forklift_inspection_age_days_17, assess_audit_gap_count_18, assess_stockout_hours_19, assess_driver_hours_remaining_20, assess_privileged_account_count_21, assess_handover_gap_count_22, assess_sprinkler_inspection_age_days_23, assess_recipient_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

