"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_vehicle_cleanliness_pct_01(record):
    """Evaluate supplier vehicle cleanliness for control WP-0675-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vehicle_cleanliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-01", "metric": "supplier_vehicle_cleanliness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-01", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-01", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-01", "metric": "supplier_vehicle_cleanliness_pct", "label": "supplier vehicle cleanliness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vehicle cleanliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_product_change_approval_pct_02(record):
    """Evaluate supplier product-change approval for control WP-0675-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-02", "metric": "supplier_product_change_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-02", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-02", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-02", "metric": "supplier_product_change_approval_pct", "label": "supplier product-change approval",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier product-change approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_battery_regulatory_pct_03(record):
    """Evaluate supplier battery regulation compliance for control WP-0675-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_battery_regulatory_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-03", "metric": "supplier_battery_regulatory_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-03", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-03", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-03", "metric": "supplier_battery_regulatory_pct", "label": "supplier battery regulation compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier battery regulation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_invoice_bank_match_pct_04(record):
    """Evaluate supplier invoice-bank match for control WP-0675-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_bank_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-04", "metric": "supplier_invoice_bank_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-04", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-04", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-04", "metric": "supplier_invoice_bank_match_pct", "label": "supplier invoice-bank match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier invoice-bank match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_communication_redundancy_pct_05(record):
    """Evaluate supplier communications redundancy for control WP-0675-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_communication_redundancy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-05", "metric": "supplier_communication_redundancy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-05", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-05", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-05", "metric": "supplier_communication_redundancy_pct", "label": "supplier communications redundancy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier communications redundancy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_model_drift_pct_06(record):
    """Evaluate supplier model drift for control WP-0675-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_drift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-06", "metric": "supplier_model_drift_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-06", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-06", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-06", "metric": "supplier_model_drift_pct", "label": "supplier model drift",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model drift must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_schema_compatibility_pct_07(record):
    """Evaluate supplier schema compatibility for control WP-0675-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schema_compatibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-07", "metric": "supplier_schema_compatibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-07", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-07", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-07", "metric": "supplier_schema_compatibility_pct", "label": "supplier schema compatibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier schema compatibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_account_deprovision_age_hours_08(record):
    """Evaluate supplier account deprovision age for control WP-0675-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_account_deprovision_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-08", "metric": "supplier_account_deprovision_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-08", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-08", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-08", "metric": "supplier_account_deprovision_age_hours", "label": "supplier account deprovision age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier account deprovision age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_data_minimization_pct_09(record):
    """Evaluate supplier data minimization for control WP-0675-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_minimization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-09", "metric": "supplier_data_minimization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-09", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-09", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-09", "metric": "supplier_data_minimization_pct", "label": "supplier data minimization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data minimization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_attestation_age_days_10(record):
    """Evaluate supplier attestation age for control WP-0675-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-10", "metric": "supplier_attestation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-10", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-10", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-10", "metric": "supplier_attestation_age_days", "label": "supplier attestation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier attestation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_rebate_claim_age_days_11(record):
    """Evaluate supplier rebate claim age for control WP-0675-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-11", "metric": "supplier_rebate_claim_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-11", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-11", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-11", "metric": "supplier_rebate_claim_age_days", "label": "supplier rebate claim age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier rebate claim age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_warehouse_capacity_pct_12(record):
    """Evaluate supplier warehouse capacity for control WP-0675-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warehouse_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-12", "metric": "supplier_warehouse_capacity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-12", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-12", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-12", "metric": "supplier_warehouse_capacity_pct", "label": "supplier warehouse capacity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier warehouse capacity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_transaction_replay_pct_13(record):
    """Evaluate supplier transaction replay for control WP-0675-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transaction_replay_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-13", "metric": "supplier_transaction_replay_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-13", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-13", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-13", "metric": "supplier_transaction_replay_pct", "label": "supplier transaction replay",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transaction replay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_reorder_level_14(record):
    """Evaluate reorder point for control WP-0675-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reorder_level")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-14", "metric": "reorder_level",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-14", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-14", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-14", "metric": "reorder_level", "label": "reorder point",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reorder point must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_fuel_cost_per_km_15(record):
    """Evaluate transport cost per km for control WP-0675-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_cost_per_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-15", "metric": "fuel_cost_per_km",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-15", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-15", "metric": "fuel_cost_per_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-15", "metric": "fuel_cost_per_km", "label": "transport cost per km",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "transport cost per km exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_address_quality_score_16(record):
    """Evaluate address quality for control WP-0675-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-16", "metric": "address_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-16", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-16", "metric": "address_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-16", "metric": "address_quality_score", "label": "address quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "address quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_negative_stock_count_17(record):
    """Evaluate negative stock records for control WP-0675-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("negative_stock_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-17", "metric": "negative_stock_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-17", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-17", "metric": "negative_stock_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-17", "metric": "negative_stock_count", "label": "negative stock records",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "negative stock records must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_reverse_logistics_cost_18(record):
    """Evaluate reverse logistics cost for control WP-0675-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reverse_logistics_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-18", "metric": "reverse_logistics_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-18", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-18", "metric": "reverse_logistics_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-18", "metric": "reverse_logistics_cost", "label": "reverse logistics cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reverse logistics cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_weighbridge_variance_pct_19(record):
    """Evaluate weighbridge variance for control WP-0675-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighbridge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-19", "metric": "weighbridge_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-19", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-19", "metric": "weighbridge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-19", "metric": "weighbridge_variance_pct", "label": "weighbridge variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "weighbridge variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_offline_sync_age_hours_20(record):
    """Evaluate offline sync age for control WP-0675-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("offline_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-20", "metric": "offline_sync_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-20", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-20", "metric": "offline_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-20", "metric": "offline_sync_age_hours", "label": "offline sync age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "offline sync age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_weight_capture_pct_21(record):
    """Evaluate weight capture rate for control WP-0675-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-21", "metric": "weight_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-21", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-21", "metric": "weight_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-21", "metric": "weight_capture_pct", "label": "weight capture rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "weight capture rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_evidence_attachment_pct_22(record):
    """Evaluate evidence attachment completeness for control WP-0675-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("evidence_attachment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-22", "metric": "evidence_attachment_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-22", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-22", "metric": "evidence_attachment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-22", "metric": "evidence_attachment_pct", "label": "evidence attachment completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "evidence attachment completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_coolant_remaining_pct_23(record):
    """Evaluate coolant remaining for control WP-0675-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coolant_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-23", "metric": "coolant_remaining_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-23", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-23", "metric": "coolant_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-23", "metric": "coolant_remaining_pct", "label": "coolant remaining",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "coolant remaining exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_open_box_age_days_24(record):
    """Evaluate open-box age for control WP-0675-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("open_box_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0675-24", "metric": "open_box_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0675-24", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0675-24", "metric": "open_box_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0675-24", "metric": "open_box_age_days", "label": "open-box age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "open-box age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_vehicle_cleanliness_pct_01, assess_supplier_product_change_approval_pct_02, assess_supplier_battery_regulatory_pct_03, assess_supplier_invoice_bank_match_pct_04, assess_supplier_communication_redundancy_pct_05, assess_supplier_model_drift_pct_06, assess_supplier_schema_compatibility_pct_07, assess_supplier_account_deprovision_age_hours_08, assess_supplier_data_minimization_pct_09, assess_supplier_attestation_age_days_10, assess_supplier_rebate_claim_age_days_11, assess_supplier_warehouse_capacity_pct_12, assess_supplier_transaction_replay_pct_13, assess_reorder_level_14, assess_fuel_cost_per_km_15, assess_address_quality_score_16, assess_negative_stock_count_17, assess_reverse_logistics_cost_18, assess_weighbridge_variance_pct_19, assess_offline_sync_age_hours_20, assess_weight_capture_pct_21, assess_evidence_attachment_pct_22, assess_coolant_remaining_pct_23, assess_open_box_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

