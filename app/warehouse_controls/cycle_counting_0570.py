"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_unit_cost_01(record):
    """Evaluate unit cost for control WP-0570-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-01", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-01", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-01", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-01", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unit cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_scan_compliance_pct_02(record):
    """Evaluate scan compliance for control WP-0570-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-02", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-02", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-02", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-02", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "scan compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_seasonality_index_03(record):
    """Evaluate seasonality index for control WP-0570-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-03", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-03", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-03", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-03", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "seasonality index falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_reconciliation_delta_04(record):
    """Evaluate reconciliation delta for control WP-0570-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-04", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-04", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-04", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-04", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reconciliation delta must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_recycling_rate_pct_05(record):
    """Evaluate recycling rate for control WP-0570-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-05", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-05", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-05", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-05", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recycling rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_expiry_capture_pct_06(record):
    """Evaluate expiry capture rate for control WP-0570-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-06", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-06", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-06", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-06", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "expiry capture rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_api_quota_pct_07(record):
    """Evaluate API quota utilization for control WP-0570-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-07", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-07", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-07", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-07", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "API quota utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_fragile_handling_compliance_pct_08(record):
    """Evaluate fragile handling compliance for control WP-0570-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fragile_handling_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-08", "metric": "fragile_handling_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-08", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-08", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-08", "metric": "fragile_handling_compliance_pct", "label": "fragile handling compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fragile handling compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_fraud_review_age_hours_09(record):
    """Evaluate fraud review age for control WP-0570-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-09", "metric": "fraud_review_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-09", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-09", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-09", "metric": "fraud_review_age_hours", "label": "fraud review age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fraud review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_thermal_pack_condition_score_10(record):
    """Evaluate thermal pack condition for control WP-0570-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("thermal_pack_condition_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-10", "metric": "thermal_pack_condition_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-10", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-10", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-10", "metric": "thermal_pack_condition_score", "label": "thermal pack condition",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "thermal pack condition exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_spare_parts_fill_pct_11(record):
    """Evaluate spare-parts fill rate for control WP-0570-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_parts_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-11", "metric": "spare_parts_fill_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-11", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-11", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-11", "metric": "spare_parts_fill_pct", "label": "spare-parts fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "spare-parts fill rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_aisle_width_cm_12(record):
    """Evaluate aisle width for control WP-0570-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_width_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-12", "metric": "aisle_width_cm",
            "status": "insufficient_data",
            "severity": "medium", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-12", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-12", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-12", "metric": "aisle_width_cm", "label": "aisle width",
        "status": "breach", "severity": "medium", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "aisle width must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_amr_route_block_count_13(record):
    """Evaluate AMR route blocks for control WP-0570-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_route_block_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-13", "metric": "amr_route_block_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-13", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-13", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-13", "metric": "amr_route_block_count", "label": "AMR route blocks",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "AMR route blocks must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_log_retention_days_14(record):
    """Evaluate log retention for control WP-0570-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-14", "metric": "log_retention_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-14", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-14", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-14", "metric": "log_retention_days", "label": "log retention",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "log retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_device_compliance_pct_15(record):
    """Evaluate device compliance for control WP-0570-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-15", "metric": "device_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-15", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-15", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-15", "metric": "device_compliance_pct", "label": "device compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "device compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_invoice_duplicate_count_16(record):
    """Evaluate duplicate invoices for control WP-0570-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-16", "metric": "invoice_duplicate_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "invoices",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-16", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-16", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-16", "metric": "invoice_duplicate_count", "label": "duplicate invoices",
        "status": "breach", "severity": "medium", "unit": "invoices",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate invoices must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_putaway_travel_meters_17(record):
    """Evaluate putaway travel for control WP-0570-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_travel_meters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-17", "metric": "putaway_travel_meters",
            "status": "insufficient_data",
            "severity": "high", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-17", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-17", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-17", "metric": "putaway_travel_meters", "label": "putaway travel",
        "status": "breach", "severity": "high", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "putaway travel must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_credit_review_age_days_18(record):
    """Evaluate credit review age for control WP-0570-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-18", "metric": "credit_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-18", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-18", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-18", "metric": "credit_review_age_days", "label": "credit review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "credit review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_yard_move_count_19(record):
    """Evaluate yard moves for control WP-0570-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_move_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-19", "metric": "yard_move_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "moves",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-19", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-19", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-19", "metric": "yard_move_count", "label": "yard moves",
        "status": "breach", "severity": "low", "unit": "moves",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "yard moves falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_inventory_carrying_cost_pct_20(record):
    """Evaluate inventory carrying cost for control WP-0570-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-20", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-20", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-20", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-20", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory carrying cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_commit_accuracy_pct_21(record):
    """Evaluate supplier commit accuracy for control WP-0570-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_commit_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-21", "metric": "supplier_commit_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-21", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-21", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-21", "metric": "supplier_commit_accuracy_pct", "label": "supplier commit accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier commit accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_api_error_pct_22(record):
    """Evaluate supplier API error rate for control WP-0570-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-22", "metric": "supplier_api_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-22", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-22", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-22", "metric": "supplier_api_error_pct", "label": "supplier API error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "supplier API error rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_capacity_reservation_pct_23(record):
    """Evaluate supplier capacity reservation for control WP-0570-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_reservation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-23", "metric": "supplier_capacity_reservation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-23", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-23", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-23", "metric": "supplier_capacity_reservation_pct", "label": "supplier capacity reservation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier capacity reservation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_key_rotation_age_days_24(record):
    """Evaluate supplier key-rotation age for control WP-0570-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0570-24", "metric": "supplier_key_rotation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0570-24", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0570-24", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0570-24", "metric": "supplier_key_rotation_age_days", "label": "supplier key-rotation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier key-rotation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_unit_cost_01, assess_scan_compliance_pct_02, assess_seasonality_index_03, assess_reconciliation_delta_04, assess_recycling_rate_pct_05, assess_expiry_capture_pct_06, assess_api_quota_pct_07, assess_fragile_handling_compliance_pct_08, assess_fraud_review_age_hours_09, assess_thermal_pack_condition_score_10, assess_spare_parts_fill_pct_11, assess_aisle_width_cm_12, assess_amr_route_block_count_13, assess_log_retention_days_14, assess_device_compliance_pct_15, assess_invoice_duplicate_count_16, assess_putaway_travel_meters_17, assess_credit_review_age_days_18, assess_yard_move_count_19, assess_inventory_carrying_cost_pct_20, assess_supplier_commit_accuracy_pct_21, assess_supplier_api_error_pct_22, assess_supplier_capacity_reservation_pct_23, assess_supplier_key_rotation_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

