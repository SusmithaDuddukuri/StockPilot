"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_schema_compatibility_pct_01(record):
    """Evaluate supplier schema compatibility for control WP-0432-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schema_compatibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-01", "metric": "supplier_schema_compatibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-01", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-01", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-01", "metric": "supplier_schema_compatibility_pct", "label": "supplier schema compatibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier schema compatibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_account_deprovision_age_hours_02(record):
    """Evaluate supplier account deprovision age for control WP-0432-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_account_deprovision_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-02", "metric": "supplier_account_deprovision_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-02", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-02", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-02", "metric": "supplier_account_deprovision_age_hours", "label": "supplier account deprovision age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier account deprovision age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_data_minimization_pct_03(record):
    """Evaluate supplier data minimization for control WP-0432-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_minimization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-03", "metric": "supplier_data_minimization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-03", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-03", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-03", "metric": "supplier_data_minimization_pct", "label": "supplier data minimization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data minimization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_attestation_age_days_04(record):
    """Evaluate supplier attestation age for control WP-0432-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-04", "metric": "supplier_attestation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-04", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-04", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-04", "metric": "supplier_attestation_age_days", "label": "supplier attestation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier attestation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_rebate_claim_age_days_05(record):
    """Evaluate supplier rebate claim age for control WP-0432-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-05", "metric": "supplier_rebate_claim_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-05", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-05", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-05", "metric": "supplier_rebate_claim_age_days", "label": "supplier rebate claim age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "supplier rebate claim age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_warehouse_capacity_pct_06(record):
    """Evaluate supplier warehouse capacity for control WP-0432-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warehouse_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-06", "metric": "supplier_warehouse_capacity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-06", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-06", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-06", "metric": "supplier_warehouse_capacity_pct", "label": "supplier warehouse capacity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier warehouse capacity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_transaction_replay_pct_07(record):
    """Evaluate supplier transaction replay for control WP-0432-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transaction_replay_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-07", "metric": "supplier_transaction_replay_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-07", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-07", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-07", "metric": "supplier_transaction_replay_pct", "label": "supplier transaction replay",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier transaction replay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_reorder_level_08(record):
    """Evaluate reorder point for control WP-0432-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reorder_level")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-08", "metric": "reorder_level",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-08", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-08", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-08", "metric": "reorder_level", "label": "reorder point",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "reorder point exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_fuel_cost_per_km_09(record):
    """Evaluate transport cost per km for control WP-0432-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_cost_per_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-09", "metric": "fuel_cost_per_km",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-09", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-09", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-09", "metric": "fuel_cost_per_km", "label": "transport cost per km",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "transport cost per km falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_address_quality_score_10(record):
    """Evaluate address quality for control WP-0432-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-10", "metric": "address_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-10", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-10", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-10", "metric": "address_quality_score", "label": "address quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "address quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_negative_stock_count_11(record):
    """Evaluate negative stock records for control WP-0432-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("negative_stock_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-11", "metric": "negative_stock_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-11", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-11", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-11", "metric": "negative_stock_count", "label": "negative stock records",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "negative stock records must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_reverse_logistics_cost_12(record):
    """Evaluate reverse logistics cost for control WP-0432-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reverse_logistics_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-12", "metric": "reverse_logistics_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-12", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-12", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-12", "metric": "reverse_logistics_cost", "label": "reverse logistics cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "reverse logistics cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_weighbridge_variance_pct_13(record):
    """Evaluate weighbridge variance for control WP-0432-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighbridge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-13", "metric": "weighbridge_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-13", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-13", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-13", "metric": "weighbridge_variance_pct", "label": "weighbridge variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "weighbridge variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_offline_sync_age_hours_14(record):
    """Evaluate offline sync age for control WP-0432-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("offline_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-14", "metric": "offline_sync_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-14", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-14", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-14", "metric": "offline_sync_age_hours", "label": "offline sync age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "offline sync age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_weight_capture_pct_15(record):
    """Evaluate weight capture rate for control WP-0432-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-15", "metric": "weight_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-15", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-15", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-15", "metric": "weight_capture_pct", "label": "weight capture rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "weight capture rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_evidence_attachment_pct_16(record):
    """Evaluate evidence attachment completeness for control WP-0432-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evidence_attachment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-16", "metric": "evidence_attachment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-16", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-16", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-16", "metric": "evidence_attachment_pct", "label": "evidence attachment completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "evidence attachment completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_coolant_remaining_pct_17(record):
    """Evaluate coolant remaining for control WP-0432-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-17", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-17", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-17", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-17", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "coolant remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_open_box_age_days_18(record):
    """Evaluate open-box age for control WP-0432-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-18", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-18", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-18", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-18", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-box age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_racking_inspection_age_days_19(record):
    """Evaluate racking inspection age for control WP-0432-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("racking_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-19", "metric": "racking_inspection_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-19", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-19", "metric": "racking_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-19", "metric": "racking_inspection_age_days", "label": "racking inspection age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "racking inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_robot_cycle_time_seconds_20(record):
    """Evaluate robot cycle time for control WP-0432-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_cycle_time_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-20", "metric": "robot_cycle_time_seconds",
            "status": "insufficient_data",
            "severity": "critical", "unit": "seconds",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-20", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-20", "metric": "robot_cycle_time_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-20", "metric": "robot_cycle_time_seconds", "label": "robot cycle time",
        "status": "breach", "severity": "critical", "unit": "seconds",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "robot cycle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_on_call_ack_minutes_21(record):
    """Evaluate on-call acknowledgement for control WP-0432-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("on_call_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-21", "metric": "on_call_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-21", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-21", "metric": "on_call_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-21", "metric": "on_call_ack_minutes", "label": "on-call acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "on-call acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_mobile_app_crash_pct_22(record):
    """Evaluate mobile app crash rate for control WP-0432-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mobile_app_crash_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-22", "metric": "mobile_app_crash_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-22", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-22", "metric": "mobile_app_crash_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-22", "metric": "mobile_app_crash_pct", "label": "mobile app crash rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "mobile app crash rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_customer_contact_valid_pct_23(record):
    """Evaluate customer contact validity for control WP-0432-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-23", "metric": "customer_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-23", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-23", "metric": "customer_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-23", "metric": "customer_contact_valid_pct", "label": "customer contact validity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer contact validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_quality_hold_pct_24(record):
    """Evaluate quality hold share for control WP-0432-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_hold_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0432-24", "metric": "quality_hold_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0432-24", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0432-24", "metric": "quality_hold_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0432-24", "metric": "quality_hold_pct", "label": "quality hold share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "quality hold share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_schema_compatibility_pct_01, assess_supplier_account_deprovision_age_hours_02, assess_supplier_data_minimization_pct_03, assess_supplier_attestation_age_days_04, assess_supplier_rebate_claim_age_days_05, assess_supplier_warehouse_capacity_pct_06, assess_supplier_transaction_replay_pct_07, assess_reorder_level_08, assess_fuel_cost_per_km_09, assess_address_quality_score_10, assess_negative_stock_count_11, assess_reverse_logistics_cost_12, assess_weighbridge_variance_pct_13, assess_offline_sync_age_hours_14, assess_weight_capture_pct_15, assess_evidence_attachment_pct_16, assess_coolant_remaining_pct_17, assess_open_box_age_days_18, assess_racking_inspection_age_days_19, assess_robot_cycle_time_seconds_20, assess_on_call_ack_minutes_21, assess_mobile_app_crash_pct_22, assess_customer_contact_valid_pct_23, assess_quality_hold_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

