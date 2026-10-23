"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_product_recall_match_pct_01(record):
    """Evaluate product recall match for control WP-0215-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_recall_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-01", "metric": "product_recall_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-01", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-01", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-01", "metric": "product_recall_match_pct", "label": "product recall match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product recall match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_unload_rate_pallets_hour_02(record):
    """Evaluate unload rate for control WP-0215-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unload_rate_pallets_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-02", "metric": "unload_rate_pallets_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "pallets/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-02", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-02", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-02", "metric": "unload_rate_pallets_hour", "label": "unload rate",
        "status": "breach", "severity": "low", "unit": "pallets/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unload rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_customer_refund_rate_pct_03(record):
    """Evaluate customer refund rate for control WP-0215-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_refund_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-03", "metric": "customer_refund_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-03", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-03", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-03", "metric": "customer_refund_rate_pct", "label": "customer refund rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "customer refund rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_empty_container_balance_04(record):
    """Evaluate empty container balance for control WP-0215-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_container_balance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-04", "metric": "empty_container_balance",
            "status": "insufficient_data",
            "severity": "high", "unit": "containers",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-04", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-04", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-04", "metric": "empty_container_balance", "label": "empty container balance",
        "status": "breach", "severity": "high", "unit": "containers",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "empty container balance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_cost_per_order_05(record):
    """Evaluate cost per order for control WP-0215-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-05", "metric": "cost_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-05", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-05", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-05", "metric": "cost_per_order", "label": "cost per order",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cost per order must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_emissions_intensity_06(record):
    """Evaluate supplier emissions intensity for control WP-0215-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emissions_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-06", "metric": "supplier_emissions_intensity",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-06", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-06", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-06", "metric": "supplier_emissions_intensity", "label": "supplier emissions intensity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier emissions intensity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_privacy_incident_count_07(record):
    """Evaluate supplier privacy incidents for control WP-0215-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-07", "metric": "supplier_privacy_incident_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-07", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-07", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-07", "metric": "supplier_privacy_incident_count", "label": "supplier privacy incidents",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier privacy incidents exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_action_plan_completion_pct_08(record):
    """Evaluate supplier action-plan completion for control WP-0215-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-08", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-08", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-08", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-08", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "supplier action-plan completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_vulnerability_remediation_days_09(record):
    """Evaluate supplier vulnerability remediation time for control WP-0215-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_remediation_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-09", "metric": "supplier_vulnerability_remediation_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-09", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-09", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-09", "metric": "supplier_vulnerability_remediation_days", "label": "supplier vulnerability remediation time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vulnerability remediation time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_labor_availability_pct_10(record):
    """Evaluate supplier labor availability for control WP-0215-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-10", "metric": "supplier_labor_availability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-10", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-10", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-10", "metric": "supplier_labor_availability_pct", "label": "supplier labor availability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier labor availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_emission_audit_age_days_11(record):
    """Evaluate supplier emissions audit age for control WP-0215-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emission_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-11", "metric": "supplier_emission_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-11", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-11", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-11", "metric": "supplier_emission_audit_age_days", "label": "supplier emissions audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier emissions audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_exception_latency_minutes_12(record):
    """Evaluate supplier exception latency for control WP-0215-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-12", "metric": "supplier_exception_latency_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-12", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-12", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-12", "metric": "supplier_exception_latency_minutes", "label": "supplier exception latency",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier exception latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_corrective_action_effectiveness_pct_13(record):
    """Evaluate supplier corrective-action effectiveness for control WP-0215-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_effectiveness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-13", "metric": "supplier_corrective_action_effectiveness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-13", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-13", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-13", "metric": "supplier_corrective_action_effectiveness_pct", "label": "supplier corrective-action effectiveness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier corrective-action effectiveness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_child_labor_screen_pct_14(record):
    """Evaluate supplier child-labor screening for control WP-0215-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_child_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-14", "metric": "supplier_child_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-14", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-14", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-14", "metric": "supplier_child_labor_screen_pct", "label": "supplier child-labor screening",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier child-labor screening must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_capacity_drop_pct_15(record):
    """Evaluate supplier capacity drop for control WP-0215-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-15", "metric": "supplier_capacity_drop_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-15", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-15", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-15", "metric": "supplier_capacity_drop_pct", "label": "supplier capacity drop",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier capacity drop exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_cost_reduction_pct_16(record):
    """Evaluate supplier cost reduction for control WP-0215-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-16", "metric": "supplier_cost_reduction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-16", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-16", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-16", "metric": "supplier_cost_reduction_pct", "label": "supplier cost reduction",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "supplier cost reduction falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_carbon_per_inference_17(record):
    """Evaluate supplier carbon per inference for control WP-0215-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carbon_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-17", "metric": "supplier_carbon_per_inference",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-17", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-17", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-17", "metric": "supplier_carbon_per_inference", "label": "supplier carbon per inference",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier carbon per inference must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_error_budget_remaining_pct_18(record):
    """Evaluate supplier error budget remaining for control WP-0215-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_error_budget_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-18", "metric": "supplier_error_budget_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-18", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-18", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-18", "metric": "supplier_error_budget_remaining_pct", "label": "supplier error budget remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier error budget remaining must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_reproducible_build_pct_19(record):
    """Evaluate supplier reproducible build rate for control WP-0215-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reproducible_build_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-19", "metric": "supplier_reproducible_build_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-19", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-19", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-19", "metric": "supplier_reproducible_build_pct", "label": "supplier reproducible build rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier reproducible build rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_evidence_freshness_days_20(record):
    """Evaluate supplier evidence freshness for control WP-0215-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_freshness_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-20", "metric": "supplier_evidence_freshness_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-20", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-20", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-20", "metric": "supplier_evidence_freshness_days", "label": "supplier evidence freshness",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier evidence freshness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_bank_change_count_21(record):
    """Evaluate supplier bank changes for control WP-0215-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-21", "metric": "supplier_bank_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-21", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-21", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-21", "metric": "supplier_bank_change_count", "label": "supplier bank changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier bank changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_subtier_shortage_count_22(record):
    """Evaluate supplier sub-tier shortages for control WP-0215-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-22", "metric": "supplier_subtier_shortage_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-22", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-22", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-22", "metric": "supplier_subtier_shortage_count", "label": "supplier sub-tier shortages",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-tier shortages must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_issue_transparency_pct_23(record):
    """Evaluate supplier issue transparency for control WP-0215-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_issue_transparency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-23", "metric": "supplier_issue_transparency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-23", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-23", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-23", "metric": "supplier_issue_transparency_pct", "label": "supplier issue transparency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier issue transparency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_customer_notice_pct_24(record):
    """Evaluate supplier customer notice completion for control WP-0215-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0215-24", "metric": "supplier_customer_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0215-24", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0215-24", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0215-24", "metric": "supplier_customer_notice_pct", "label": "supplier customer notice completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier customer notice completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_product_recall_match_pct_01, assess_unload_rate_pallets_hour_02, assess_customer_refund_rate_pct_03, assess_empty_container_balance_04, assess_cost_per_order_05, assess_supplier_emissions_intensity_06, assess_supplier_privacy_incident_count_07, assess_supplier_action_plan_completion_pct_08, assess_supplier_vulnerability_remediation_days_09, assess_supplier_labor_availability_pct_10, assess_supplier_emission_audit_age_days_11, assess_supplier_exception_latency_minutes_12, assess_supplier_corrective_action_effectiveness_pct_13, assess_supplier_child_labor_screen_pct_14, assess_supplier_capacity_drop_pct_15, assess_supplier_cost_reduction_pct_16, assess_supplier_carbon_per_inference_17, assess_supplier_error_budget_remaining_pct_18, assess_supplier_reproducible_build_pct_19, assess_supplier_evidence_freshness_days_20, assess_supplier_bank_change_count_21, assess_supplier_subtier_shortage_count_22, assess_supplier_issue_transparency_pct_23, assess_supplier_customer_notice_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

