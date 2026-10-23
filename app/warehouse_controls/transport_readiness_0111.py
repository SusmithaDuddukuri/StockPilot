"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_credit_limit_utilization_pct_01(record):
    """Evaluate supplier credit limit utilization for control WP-0111-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_limit_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-01", "metric": "supplier_credit_limit_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-01", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-01", "metric": "supplier_credit_limit_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-01", "metric": "supplier_credit_limit_utilization_pct", "label": "supplier credit limit utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier credit limit utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_skill_matrix_age_days_02(record):
    """Evaluate supplier skill-matrix age for control WP-0111-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_skill_matrix_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-02", "metric": "supplier_skill_matrix_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-02", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-02", "metric": "supplier_skill_matrix_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-02", "metric": "supplier_skill_matrix_age_days", "label": "supplier skill-matrix age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier skill-matrix age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_explainability_compliance_pct_03(record):
    """Evaluate supplier explainability compliance for control WP-0111-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_explainability_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-03", "metric": "supplier_explainability_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-03", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-03", "metric": "supplier_explainability_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-03", "metric": "supplier_explainability_compliance_pct", "label": "supplier explainability compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier explainability compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_event_replay_test_age_days_04(record):
    """Evaluate supplier event replay test age for control WP-0111-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_replay_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-04", "metric": "supplier_event_replay_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-04", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-04", "metric": "supplier_event_replay_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-04", "metric": "supplier_event_replay_test_age_days", "label": "supplier event replay test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier event replay test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_security_event_review_age_hours_05(record):
    """Evaluate supplier security-event review age for control WP-0111-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_event_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-05", "metric": "supplier_security_event_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-05", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-05", "metric": "supplier_security_event_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-05", "metric": "supplier_security_event_review_age_hours", "label": "supplier security-event review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier security-event review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_clean_desk_pct_06(record):
    """Evaluate supplier clean-desk compliance for control WP-0111-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clean_desk_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-06", "metric": "supplier_clean_desk_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-06", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-06", "metric": "supplier_clean_desk_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-06", "metric": "supplier_clean_desk_pct", "label": "supplier clean-desk compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier clean-desk compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_workflow_bypass_count_07(record):
    """Evaluate supplier workflow bypasses for control WP-0111-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_workflow_bypass_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-07", "metric": "supplier_workflow_bypass_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-07", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-07", "metric": "supplier_workflow_bypass_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-07", "metric": "supplier_workflow_bypass_count", "label": "supplier workflow bypasses",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier workflow bypasses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_minimum_commitment_variance_pct_08(record):
    """Evaluate minimum commitment variance for control WP-0111-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minimum_commitment_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-08", "metric": "supplier_minimum_commitment_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-08", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-08", "metric": "supplier_minimum_commitment_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-08", "metric": "supplier_minimum_commitment_variance_pct", "label": "minimum commitment variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "minimum commitment variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_pack_accuracy_pct_09(record):
    """Evaluate supplier pack accuracy for control WP-0111-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pack_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-09", "metric": "supplier_pack_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-09", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-09", "metric": "supplier_pack_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-09", "metric": "supplier_pack_accuracy_pct", "label": "supplier pack accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier pack accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_open_invoice_transfer_pct_10(record):
    """Evaluate open-invoice transfer completeness for control WP-0111-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_invoice_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-10", "metric": "supplier_open_invoice_transfer_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-10", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-10", "metric": "supplier_open_invoice_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-10", "metric": "supplier_open_invoice_transfer_pct", "label": "open-invoice transfer completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "open-invoice transfer completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_unit_cost_11(record):
    """Evaluate unit cost for control WP-0111-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unit_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-11", "metric": "unit_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-11", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-11", "metric": "unit_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-11", "metric": "unit_cost", "label": "unit cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "unit cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_scan_compliance_pct_12(record):
    """Evaluate scan compliance for control WP-0111-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scan_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-12", "metric": "scan_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-12", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-12", "metric": "scan_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-12", "metric": "scan_compliance_pct", "label": "scan compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "scan compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_seasonality_index_13(record):
    """Evaluate seasonality index for control WP-0111-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seasonality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-13", "metric": "seasonality_index",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-13", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-13", "metric": "seasonality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-13", "metric": "seasonality_index", "label": "seasonality index",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seasonality index must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_reconciliation_delta_14(record):
    """Evaluate reconciliation delta for control WP-0111-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reconciliation_delta")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-14", "metric": "reconciliation_delta",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-14", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-14", "metric": "reconciliation_delta", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-14", "metric": "reconciliation_delta", "label": "reconciliation delta",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reconciliation delta must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_recycling_rate_pct_15(record):
    """Evaluate recycling rate for control WP-0111-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recycling_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-15", "metric": "recycling_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-15", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-15", "metric": "recycling_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-15", "metric": "recycling_rate_pct", "label": "recycling rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "recycling rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_expiry_capture_pct_16(record):
    """Evaluate expiry capture rate for control WP-0111-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-16", "metric": "expiry_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-16", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-16", "metric": "expiry_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-16", "metric": "expiry_capture_pct", "label": "expiry capture rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "expiry capture rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_api_quota_pct_17(record):
    """Evaluate API quota utilization for control WP-0111-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_quota_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-17", "metric": "api_quota_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-17", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-17", "metric": "api_quota_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-17", "metric": "api_quota_pct", "label": "API quota utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "API quota utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_fragile_handling_compliance_pct_18(record):
    """Evaluate fragile handling compliance for control WP-0111-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fragile_handling_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-18", "metric": "fragile_handling_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-18", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-18", "metric": "fragile_handling_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-18", "metric": "fragile_handling_compliance_pct", "label": "fragile handling compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fragile handling compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_fraud_review_age_hours_19(record):
    """Evaluate fraud review age for control WP-0111-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-19", "metric": "fraud_review_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-19", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-19", "metric": "fraud_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-19", "metric": "fraud_review_age_hours", "label": "fraud review age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "fraud review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_thermal_pack_condition_score_20(record):
    """Evaluate thermal pack condition for control WP-0111-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("thermal_pack_condition_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-20", "metric": "thermal_pack_condition_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-20", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-20", "metric": "thermal_pack_condition_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-20", "metric": "thermal_pack_condition_score", "label": "thermal pack condition",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "thermal pack condition falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_spare_parts_fill_pct_21(record):
    """Evaluate spare-parts fill rate for control WP-0111-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_parts_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-21", "metric": "spare_parts_fill_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-21", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-21", "metric": "spare_parts_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-21", "metric": "spare_parts_fill_pct", "label": "spare-parts fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "spare-parts fill rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_aisle_width_cm_22(record):
    """Evaluate aisle width for control WP-0111-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_width_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-22", "metric": "aisle_width_cm",
            "status": "insufficient_data",
            "severity": "low", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-22", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-22", "metric": "aisle_width_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-22", "metric": "aisle_width_cm", "label": "aisle width",
        "status": "breach", "severity": "low", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "aisle width must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_amr_route_block_count_23(record):
    """Evaluate AMR route blocks for control WP-0111-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_route_block_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-23", "metric": "amr_route_block_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-23", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-23", "metric": "amr_route_block_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-23", "metric": "amr_route_block_count", "label": "AMR route blocks",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "AMR route blocks exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_log_retention_days_24(record):
    """Evaluate log retention for control WP-0111-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0111-24", "metric": "log_retention_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0111-24", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0111-24", "metric": "log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0111-24", "metric": "log_retention_days", "label": "log retention",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "log retention falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_credit_limit_utilization_pct_01, assess_supplier_skill_matrix_age_days_02, assess_supplier_explainability_compliance_pct_03, assess_supplier_event_replay_test_age_days_04, assess_supplier_security_event_review_age_hours_05, assess_supplier_clean_desk_pct_06, assess_supplier_workflow_bypass_count_07, assess_supplier_minimum_commitment_variance_pct_08, assess_supplier_pack_accuracy_pct_09, assess_supplier_open_invoice_transfer_pct_10, assess_unit_cost_11, assess_scan_compliance_pct_12, assess_seasonality_index_13, assess_reconciliation_delta_14, assess_recycling_rate_pct_15, assess_expiry_capture_pct_16, assess_api_quota_pct_17, assess_fragile_handling_compliance_pct_18, assess_fraud_review_age_hours_19, assess_thermal_pack_condition_score_20, assess_spare_parts_fill_pct_21, assess_aisle_width_cm_22, assess_amr_route_block_count_23, assess_log_retention_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

