"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_workflow_bypass_count_01(record):
    """Evaluate supplier workflow bypasses for control WP-0247-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_workflow_bypass_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-01", "metric": "supplier_workflow_bypass_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-01", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-01", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-01", "metric": "supplier_workflow_bypass_count", "label": "supplier workflow bypasses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier workflow bypasses must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_minimum_commitment_variance_pct_02(record):
    """Evaluate minimum commitment variance for control WP-0247-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-02", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-02", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-02", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-02", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum commitment variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_pack_accuracy_pct_03(record):
    """Evaluate supplier pack accuracy for control WP-0247-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-03", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-03", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-03", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-03", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier pack accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_open_invoice_transfer_pct_04(record):
    """Evaluate open-invoice transfer completeness for control WP-0247-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_invoice_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-04", "metric": "supplier_open_invoice_transfer_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-04", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-04", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-04", "metric": "supplier_open_invoice_transfer_pct", "label": "open-invoice transfer completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "open-invoice transfer completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_unit_cost_05(record):
    """Evaluate unit cost for control WP-0247-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-05", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-05", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-05", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-05", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "unit cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_scan_compliance_pct_06(record):
    """Evaluate scan compliance for control WP-0247-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-06", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-06", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-06", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-06", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scan compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_seasonality_index_07(record):
    """Evaluate seasonality index for control WP-0247-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-07", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-07", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-07", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-07", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "seasonality index exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_reconciliation_delta_08(record):
    """Evaluate reconciliation delta for control WP-0247-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-08", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-08", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-08", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-08", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "reconciliation delta falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_recycling_rate_pct_09(record):
    """Evaluate recycling rate for control WP-0247-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-09", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-09", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-09", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-09", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recycling rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_expiry_capture_pct_10(record):
    """Evaluate expiry capture rate for control WP-0247-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-10", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-10", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-10", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-10", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "expiry capture rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_api_quota_pct_11(record):
    """Evaluate API quota utilization for control WP-0247-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-11", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-11", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-11", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-11", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "API quota utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_fragile_handling_compliance_pct_12(record):
    """Evaluate fragile handling compliance for control WP-0247-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fragile_handling_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-12", "metric": "fragile_handling_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-12", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-12", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-12", "metric": "fragile_handling_compliance_pct", "label": "fragile handling compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "fragile handling compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_fraud_review_age_hours_13(record):
    """Evaluate fraud review age for control WP-0247-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-13", "metric": "fraud_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-13", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-13", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-13", "metric": "fraud_review_age_hours", "label": "fraud review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fraud review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_thermal_pack_condition_score_14(record):
    """Evaluate thermal pack condition for control WP-0247-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("thermal_pack_condition_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-14", "metric": "thermal_pack_condition_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-14", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-14", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-14", "metric": "thermal_pack_condition_score", "label": "thermal pack condition",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "thermal pack condition must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_spare_parts_fill_pct_15(record):
    """Evaluate spare-parts fill rate for control WP-0247-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_parts_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-15", "metric": "spare_parts_fill_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-15", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-15", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-15", "metric": "spare_parts_fill_pct", "label": "spare-parts fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "spare-parts fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_aisle_width_cm_16(record):
    """Evaluate aisle width for control WP-0247-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_width_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-16", "metric": "aisle_width_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-16", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-16", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-16", "metric": "aisle_width_cm", "label": "aisle width",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "aisle width falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_amr_route_block_count_17(record):
    """Evaluate AMR route blocks for control WP-0247-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_route_block_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-17", "metric": "amr_route_block_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-17", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-17", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-17", "metric": "amr_route_block_count", "label": "AMR route blocks",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "AMR route blocks must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_log_retention_days_18(record):
    """Evaluate log retention for control WP-0247-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-18", "metric": "log_retention_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-18", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-18", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-18", "metric": "log_retention_days", "label": "log retention",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "log retention must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_device_compliance_pct_19(record):
    """Evaluate device compliance for control WP-0247-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-19", "metric": "device_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-19", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-19", "metric": "device_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-19", "metric": "device_compliance_pct", "label": "device compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "device compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_invoice_duplicate_count_20(record):
    """Evaluate duplicate invoices for control WP-0247-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-20", "metric": "invoice_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "invoices",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-20", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-20", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-20", "metric": "invoice_duplicate_count", "label": "duplicate invoices",
        "status": "breach", "severity": "high", "unit": "invoices",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "duplicate invoices falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_putaway_travel_meters_21(record):
    """Evaluate putaway travel for control WP-0247-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_travel_meters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-21", "metric": "putaway_travel_meters",
            "status": "insufficient_data",
            "severity": "critical", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-21", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-21", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-21", "metric": "putaway_travel_meters", "label": "putaway travel",
        "status": "breach", "severity": "critical", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway travel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_credit_review_age_days_22(record):
    """Evaluate credit review age for control WP-0247-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-22", "metric": "credit_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-22", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-22", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-22", "metric": "credit_review_age_days", "label": "credit review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "credit review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_yard_move_count_23(record):
    """Evaluate yard moves for control WP-0247-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_move_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-23", "metric": "yard_move_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "moves",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-23", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-23", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-23", "metric": "yard_move_count", "label": "yard moves",
        "status": "breach", "severity": "medium", "unit": "moves",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "yard moves exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_inventory_carrying_cost_pct_24(record):
    """Evaluate inventory carrying cost for control WP-0247-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0247-24", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0247-24", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0247-24", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0247-24", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "inventory carrying cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_workflow_bypass_count_01, assess_supplier_minimum_commitment_variance_pct_02, assess_supplier_pack_accuracy_pct_03, assess_supplier_open_invoice_transfer_pct_04, assess_unit_cost_05, assess_scan_compliance_pct_06, assess_seasonality_index_07, assess_reconciliation_delta_08, assess_recycling_rate_pct_09, assess_expiry_capture_pct_10, assess_api_quota_pct_11, assess_fragile_handling_compliance_pct_12, assess_fraud_review_age_hours_13, assess_thermal_pack_condition_score_14, assess_spare_parts_fill_pct_15, assess_aisle_width_cm_16, assess_amr_route_block_count_17, assess_log_retention_days_18, assess_device_compliance_pct_19, assess_invoice_duplicate_count_20, assess_putaway_travel_meters_21, assess_credit_review_age_days_22, assess_yard_move_count_23, assess_inventory_carrying_cost_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

