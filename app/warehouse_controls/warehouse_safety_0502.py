"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_minimum_commitment_variance_pct_01(record):
    """Evaluate minimum commitment variance for control WP-0502-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-01", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-01", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-01", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-01", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum commitment variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_pack_accuracy_pct_02(record):
    """Evaluate supplier pack accuracy for control WP-0502-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-02", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-02", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-02", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-02", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier pack accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_open_invoice_transfer_pct_03(record):
    """Evaluate open-invoice transfer completeness for control WP-0502-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_invoice_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-03", "metric": "supplier_open_invoice_transfer_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-03", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-03", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-03", "metric": "supplier_open_invoice_transfer_pct", "label": "open-invoice transfer completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "open-invoice transfer completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_unit_cost_04(record):
    """Evaluate unit cost for control WP-0502-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-04", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-04", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-04", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-04", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "unit cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_scan_compliance_pct_05(record):
    """Evaluate scan compliance for control WP-0502-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-05", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-05", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-05", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-05", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scan compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_seasonality_index_06(record):
    """Evaluate seasonality index for control WP-0502-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-06", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-06", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-06", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-06", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "seasonality index exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_reconciliation_delta_07(record):
    """Evaluate reconciliation delta for control WP-0502-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-07", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-07", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-07", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-07", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "reconciliation delta falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_recycling_rate_pct_08(record):
    """Evaluate recycling rate for control WP-0502-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-08", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-08", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-08", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-08", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recycling rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_expiry_capture_pct_09(record):
    """Evaluate expiry capture rate for control WP-0502-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-09", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-09", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-09", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-09", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "expiry capture rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_api_quota_pct_10(record):
    """Evaluate API quota utilization for control WP-0502-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-10", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-10", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-10", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-10", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "API quota utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_fragile_handling_compliance_pct_11(record):
    """Evaluate fragile handling compliance for control WP-0502-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fragile_handling_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-11", "metric": "fragile_handling_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-11", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-11", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-11", "metric": "fragile_handling_compliance_pct", "label": "fragile handling compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "fragile handling compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_fraud_review_age_hours_12(record):
    """Evaluate fraud review age for control WP-0502-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-12", "metric": "fraud_review_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-12", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-12", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-12", "metric": "fraud_review_age_hours", "label": "fraud review age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fraud review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_thermal_pack_condition_score_13(record):
    """Evaluate thermal pack condition for control WP-0502-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("thermal_pack_condition_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-13", "metric": "thermal_pack_condition_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-13", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-13", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-13", "metric": "thermal_pack_condition_score", "label": "thermal pack condition",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "thermal pack condition must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_spare_parts_fill_pct_14(record):
    """Evaluate spare-parts fill rate for control WP-0502-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_parts_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-14", "metric": "spare_parts_fill_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-14", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-14", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-14", "metric": "spare_parts_fill_pct", "label": "spare-parts fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "spare-parts fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_aisle_width_cm_15(record):
    """Evaluate aisle width for control WP-0502-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_width_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-15", "metric": "aisle_width_cm",
            "status": "insufficient_data",
            "severity": "low", "unit": "cm",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-15", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-15", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-15", "metric": "aisle_width_cm", "label": "aisle width",
        "status": "breach", "severity": "low", "unit": "cm",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "aisle width falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_amr_route_block_count_16(record):
    """Evaluate AMR route blocks for control WP-0502-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_route_block_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-16", "metric": "amr_route_block_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-16", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-16", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-16", "metric": "amr_route_block_count", "label": "AMR route blocks",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "AMR route blocks must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_log_retention_days_17(record):
    """Evaluate log retention for control WP-0502-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-17", "metric": "log_retention_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-17", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-17", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-17", "metric": "log_retention_days", "label": "log retention",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "log retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_device_compliance_pct_18(record):
    """Evaluate device compliance for control WP-0502-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-18", "metric": "device_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-18", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-18", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-18", "metric": "device_compliance_pct", "label": "device compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "device compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_invoice_duplicate_count_19(record):
    """Evaluate duplicate invoices for control WP-0502-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-19", "metric": "invoice_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "invoices",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-19", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-19", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-19", "metric": "invoice_duplicate_count", "label": "duplicate invoices",
        "status": "breach", "severity": "low", "unit": "invoices",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "duplicate invoices falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_putaway_travel_meters_20(record):
    """Evaluate putaway travel for control WP-0502-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_travel_meters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-20", "metric": "putaway_travel_meters",
            "status": "insufficient_data",
            "severity": "medium", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-20", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-20", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-20", "metric": "putaway_travel_meters", "label": "putaway travel",
        "status": "breach", "severity": "medium", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway travel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_credit_review_age_days_21(record):
    """Evaluate credit review age for control WP-0502-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-21", "metric": "credit_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-21", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-21", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-21", "metric": "credit_review_age_days", "label": "credit review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "credit review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_yard_move_count_22(record):
    """Evaluate yard moves for control WP-0502-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_move_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-22", "metric": "yard_move_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "moves",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-22", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-22", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-22", "metric": "yard_move_count", "label": "yard moves",
        "status": "breach", "severity": "critical", "unit": "moves",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "yard moves exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_inventory_carrying_cost_pct_23(record):
    """Evaluate inventory carrying cost for control WP-0502-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-23", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-23", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-23", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-23", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "inventory carrying cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_commit_accuracy_pct_24(record):
    """Evaluate supplier commit accuracy for control WP-0502-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_commit_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0502-24", "metric": "supplier_commit_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0502-24", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0502-24", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0502-24", "metric": "supplier_commit_accuracy_pct", "label": "supplier commit accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier commit accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_supplier_minimum_commitment_variance_pct_01, assess_supplier_pack_accuracy_pct_02, assess_supplier_open_invoice_transfer_pct_03, assess_unit_cost_04, assess_scan_compliance_pct_05, assess_seasonality_index_06, assess_reconciliation_delta_07, assess_recycling_rate_pct_08, assess_expiry_capture_pct_09, assess_api_quota_pct_10, assess_fragile_handling_compliance_pct_11, assess_fraud_review_age_hours_12, assess_thermal_pack_condition_score_13, assess_spare_parts_fill_pct_14, assess_aisle_width_cm_15, assess_amr_route_block_count_16, assess_log_retention_days_17, assess_device_compliance_pct_18, assess_invoice_duplicate_count_19, assess_putaway_travel_meters_20, assess_credit_review_age_days_21, assess_yard_move_count_22, assess_inventory_carrying_cost_pct_23, assess_supplier_commit_accuracy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

