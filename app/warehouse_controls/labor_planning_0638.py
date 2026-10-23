"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_reconciliation_delta_01(record):
    """Evaluate reconciliation delta for control WP-0638-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-01", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-01", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-01", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-01", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reconciliation delta must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_recycling_rate_pct_02(record):
    """Evaluate recycling rate for control WP-0638-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-02", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-02", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-02", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-02", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "recycling rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_expiry_capture_pct_03(record):
    """Evaluate expiry capture rate for control WP-0638-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-03", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-03", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-03", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-03", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "expiry capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_api_quota_pct_04(record):
    """Evaluate API quota utilization for control WP-0638-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-04", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-04", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-04", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-04", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "API quota utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_fragile_handling_compliance_pct_05(record):
    """Evaluate fragile handling compliance for control WP-0638-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fragile_handling_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-05", "metric": "fragile_handling_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-05", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-05", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-05", "metric": "fragile_handling_compliance_pct", "label": "fragile handling compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fragile handling compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_fraud_review_age_hours_06(record):
    """Evaluate fraud review age for control WP-0638-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-06", "metric": "fraud_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-06", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-06", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-06", "metric": "fraud_review_age_hours", "label": "fraud review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "fraud review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_thermal_pack_condition_score_07(record):
    """Evaluate thermal pack condition for control WP-0638-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("thermal_pack_condition_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-07", "metric": "thermal_pack_condition_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-07", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-07", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-07", "metric": "thermal_pack_condition_score", "label": "thermal pack condition",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "thermal pack condition falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_spare_parts_fill_pct_08(record):
    """Evaluate spare-parts fill rate for control WP-0638-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_parts_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-08", "metric": "spare_parts_fill_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-08", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-08", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-08", "metric": "spare_parts_fill_pct", "label": "spare-parts fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "spare-parts fill rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_aisle_width_cm_09(record):
    """Evaluate aisle width for control WP-0638-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_width_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-09", "metric": "aisle_width_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-09", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-09", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-09", "metric": "aisle_width_cm", "label": "aisle width",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "aisle width must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_amr_route_block_count_10(record):
    """Evaluate AMR route blocks for control WP-0638-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_route_block_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-10", "metric": "amr_route_block_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-10", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-10", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-10", "metric": "amr_route_block_count", "label": "AMR route blocks",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "AMR route blocks exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_log_retention_days_11(record):
    """Evaluate log retention for control WP-0638-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-11", "metric": "log_retention_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-11", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-11", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-11", "metric": "log_retention_days", "label": "log retention",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "log retention falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_device_compliance_pct_12(record):
    """Evaluate device compliance for control WP-0638-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-12", "metric": "device_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-12", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-12", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-12", "metric": "device_compliance_pct", "label": "device compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "device compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_invoice_duplicate_count_13(record):
    """Evaluate duplicate invoices for control WP-0638-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-13", "metric": "invoice_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "invoices",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-13", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-13", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-13", "metric": "invoice_duplicate_count", "label": "duplicate invoices",
        "status": "breach", "severity": "high", "unit": "invoices",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate invoices must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_putaway_travel_meters_14(record):
    """Evaluate putaway travel for control WP-0638-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_travel_meters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-14", "metric": "putaway_travel_meters",
            "status": "insufficient_data",
            "severity": "critical", "unit": "meters",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-14", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-14", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-14", "metric": "putaway_travel_meters", "label": "putaway travel",
        "status": "breach", "severity": "critical", "unit": "meters",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "putaway travel exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_credit_review_age_days_15(record):
    """Evaluate credit review age for control WP-0638-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-15", "metric": "credit_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-15", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-15", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-15", "metric": "credit_review_age_days", "label": "credit review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "credit review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_yard_move_count_16(record):
    """Evaluate yard moves for control WP-0638-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_move_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-16", "metric": "yard_move_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "moves",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-16", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-16", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-16", "metric": "yard_move_count", "label": "yard moves",
        "status": "breach", "severity": "medium", "unit": "moves",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "yard moves must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_inventory_carrying_cost_pct_17(record):
    """Evaluate inventory carrying cost for control WP-0638-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-17", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-17", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-17", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-17", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory carrying cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_commit_accuracy_pct_18(record):
    """Evaluate supplier commit accuracy for control WP-0638-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_commit_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-18", "metric": "supplier_commit_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-18", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-18", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-18", "metric": "supplier_commit_accuracy_pct", "label": "supplier commit accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier commit accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_api_error_pct_19(record):
    """Evaluate supplier API error rate for control WP-0638-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-19", "metric": "supplier_api_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-19", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-19", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-19", "metric": "supplier_api_error_pct", "label": "supplier API error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier API error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_capacity_reservation_pct_20(record):
    """Evaluate supplier capacity reservation for control WP-0638-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_reservation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-20", "metric": "supplier_capacity_reservation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-20", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-20", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-20", "metric": "supplier_capacity_reservation_pct", "label": "supplier capacity reservation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity reservation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_key_rotation_age_days_21(record):
    """Evaluate supplier key-rotation age for control WP-0638-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-21", "metric": "supplier_key_rotation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-21", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-21", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-21", "metric": "supplier_key_rotation_age_days", "label": "supplier key-rotation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier key-rotation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_substitute_qualification_days_22(record):
    """Evaluate substitute qualification time for control WP-0638-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_qualification_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-22", "metric": "supplier_substitute_qualification_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-22", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-22", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-22", "metric": "supplier_substitute_qualification_days", "label": "substitute qualification time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "substitute qualification time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_site_flood_risk_score_23(record):
    """Evaluate supplier site flood risk for control WP-0638-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_flood_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-23", "metric": "supplier_site_flood_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-23", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-23", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-23", "metric": "supplier_site_flood_risk_score", "label": "supplier site flood risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "supplier site flood risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_alternate_site_count_24(record):
    """Evaluate supplier alternate sites for control WP-0638-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_site_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0638-24", "metric": "supplier_alternate_site_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "sites",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0638-24", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0638-24", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0638-24", "metric": "supplier_alternate_site_count", "label": "supplier alternate sites",
        "status": "breach", "severity": "medium", "unit": "sites",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier alternate sites must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_reconciliation_delta_01, assess_recycling_rate_pct_02, assess_expiry_capture_pct_03, assess_api_quota_pct_04, assess_fragile_handling_compliance_pct_05, assess_fraud_review_age_hours_06, assess_thermal_pack_condition_score_07, assess_spare_parts_fill_pct_08, assess_aisle_width_cm_09, assess_amr_route_block_count_10, assess_log_retention_days_11, assess_device_compliance_pct_12, assess_invoice_duplicate_count_13, assess_putaway_travel_meters_14, assess_credit_review_age_days_15, assess_yard_move_count_16, assess_inventory_carrying_cost_pct_17, assess_supplier_commit_accuracy_pct_18, assess_supplier_api_error_pct_19, assess_supplier_capacity_reservation_pct_20, assess_supplier_key_rotation_age_days_21, assess_supplier_substitute_qualification_days_22, assess_supplier_site_flood_risk_score_23, assess_supplier_alternate_site_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

