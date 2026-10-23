"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_cost_per_order_01(record):
    """Evaluate cost per order for control WP-0538-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-01", "metric": "cost_per_order",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-01", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-01", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-01", "metric": "cost_per_order", "label": "cost per order",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cost per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_emissions_intensity_02(record):
    """Evaluate supplier emissions intensity for control WP-0538-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emissions_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-02", "metric": "supplier_emissions_intensity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-02", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-02", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-02", "metric": "supplier_emissions_intensity", "label": "supplier emissions intensity",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier emissions intensity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_privacy_incident_count_03(record):
    """Evaluate supplier privacy incidents for control WP-0538-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-03", "metric": "supplier_privacy_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-03", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-03", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-03", "metric": "supplier_privacy_incident_count", "label": "supplier privacy incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier privacy incidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_action_plan_completion_pct_04(record):
    """Evaluate supplier action-plan completion for control WP-0538-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-04", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-04", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-04", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-04", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier action-plan completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_vulnerability_remediation_days_05(record):
    """Evaluate supplier vulnerability remediation time for control WP-0538-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_remediation_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-05", "metric": "supplier_vulnerability_remediation_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-05", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-05", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-05", "metric": "supplier_vulnerability_remediation_days", "label": "supplier vulnerability remediation time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier vulnerability remediation time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_labor_availability_pct_06(record):
    """Evaluate supplier labor availability for control WP-0538-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-06", "metric": "supplier_labor_availability_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-06", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-06", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-06", "metric": "supplier_labor_availability_pct", "label": "supplier labor availability",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier labor availability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_emission_audit_age_days_07(record):
    """Evaluate supplier emissions audit age for control WP-0538-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emission_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-07", "metric": "supplier_emission_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-07", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-07", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-07", "metric": "supplier_emission_audit_age_days", "label": "supplier emissions audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier emissions audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_exception_latency_minutes_08(record):
    """Evaluate supplier exception latency for control WP-0538-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-08", "metric": "supplier_exception_latency_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-08", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-08", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-08", "metric": "supplier_exception_latency_minutes", "label": "supplier exception latency",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exception latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_corrective_action_effectiveness_pct_09(record):
    """Evaluate supplier corrective-action effectiveness for control WP-0538-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_effectiveness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-09", "metric": "supplier_corrective_action_effectiveness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-09", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-09", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-09", "metric": "supplier_corrective_action_effectiveness_pct", "label": "supplier corrective-action effectiveness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier corrective-action effectiveness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_child_labor_screen_pct_10(record):
    """Evaluate supplier child-labor screening for control WP-0538-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_child_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-10", "metric": "supplier_child_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-10", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-10", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-10", "metric": "supplier_child_labor_screen_pct", "label": "supplier child-labor screening",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "supplier child-labor screening exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_capacity_drop_pct_11(record):
    """Evaluate supplier capacity drop for control WP-0538-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-11", "metric": "supplier_capacity_drop_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-11", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-11", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-11", "metric": "supplier_capacity_drop_pct", "label": "supplier capacity drop",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier capacity drop falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_cost_reduction_pct_12(record):
    """Evaluate supplier cost reduction for control WP-0538-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-12", "metric": "supplier_cost_reduction_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-12", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-12", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-12", "metric": "supplier_cost_reduction_pct", "label": "supplier cost reduction",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cost reduction must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_carbon_per_inference_13(record):
    """Evaluate supplier carbon per inference for control WP-0538-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carbon_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-13", "metric": "supplier_carbon_per_inference",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-13", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-13", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-13", "metric": "supplier_carbon_per_inference", "label": "supplier carbon per inference",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier carbon per inference must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_error_budget_remaining_pct_14(record):
    """Evaluate supplier error budget remaining for control WP-0538-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_error_budget_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-14", "metric": "supplier_error_budget_remaining_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-14", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-14", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-14", "metric": "supplier_error_budget_remaining_pct", "label": "supplier error budget remaining",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier error budget remaining exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_reproducible_build_pct_15(record):
    """Evaluate supplier reproducible build rate for control WP-0538-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reproducible_build_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-15", "metric": "supplier_reproducible_build_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-15", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-15", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-15", "metric": "supplier_reproducible_build_pct", "label": "supplier reproducible build rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier reproducible build rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_evidence_freshness_days_16(record):
    """Evaluate supplier evidence freshness for control WP-0538-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_freshness_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-16", "metric": "supplier_evidence_freshness_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-16", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-16", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-16", "metric": "supplier_evidence_freshness_days", "label": "supplier evidence freshness",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier evidence freshness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_bank_change_count_17(record):
    """Evaluate supplier bank changes for control WP-0538-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-17", "metric": "supplier_bank_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-17", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-17", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-17", "metric": "supplier_bank_change_count", "label": "supplier bank changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier bank changes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_subtier_shortage_count_18(record):
    """Evaluate supplier sub-tier shortages for control WP-0538-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-18", "metric": "supplier_subtier_shortage_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-18", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-18", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-18", "metric": "supplier_subtier_shortage_count", "label": "supplier sub-tier shortages",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier sub-tier shortages exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_issue_transparency_pct_19(record):
    """Evaluate supplier issue transparency for control WP-0538-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_issue_transparency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-19", "metric": "supplier_issue_transparency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-19", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-19", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-19", "metric": "supplier_issue_transparency_pct", "label": "supplier issue transparency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier issue transparency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_customer_notice_pct_20(record):
    """Evaluate supplier customer notice completion for control WP-0538-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-20", "metric": "supplier_customer_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-20", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-20", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-20", "metric": "supplier_customer_notice_pct", "label": "supplier customer notice completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer notice completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_return_rate_pct_21(record):
    """Evaluate return rate for control WP-0538-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-21", "metric": "return_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-21", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-21", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-21", "metric": "return_rate_pct", "label": "return rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "return rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_payment_hold_count_22(record):
    """Evaluate payment holds for control WP-0538-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_hold_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-22", "metric": "payment_hold_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-22", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-22", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-22", "metric": "payment_hold_count", "label": "payment holds",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "payment holds exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_order_split_count_23(record):
    """Evaluate order splits for control WP-0538-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_split_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-23", "metric": "order_split_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-23", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-23", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-23", "metric": "order_split_count", "label": "order splits",
        "status": "breach", "severity": "low", "unit": "orders",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "order splits falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_packaging_compliance_pct_24(record):
    """Evaluate packaging compliance for control WP-0538-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0538-24", "metric": "packaging_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0538-24", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0538-24", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0538-24", "metric": "packaging_compliance_pct", "label": "packaging compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "packaging compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_cost_per_order_01, assess_supplier_emissions_intensity_02, assess_supplier_privacy_incident_count_03, assess_supplier_action_plan_completion_pct_04, assess_supplier_vulnerability_remediation_days_05, assess_supplier_labor_availability_pct_06, assess_supplier_emission_audit_age_days_07, assess_supplier_exception_latency_minutes_08, assess_supplier_corrective_action_effectiveness_pct_09, assess_supplier_child_labor_screen_pct_10, assess_supplier_capacity_drop_pct_11, assess_supplier_cost_reduction_pct_12, assess_supplier_carbon_per_inference_13, assess_supplier_error_budget_remaining_pct_14, assess_supplier_reproducible_build_pct_15, assess_supplier_evidence_freshness_days_16, assess_supplier_bank_change_count_17, assess_supplier_subtier_shortage_count_18, assess_supplier_issue_transparency_pct_19, assess_supplier_customer_notice_pct_20, assess_return_rate_pct_21, assess_payment_hold_count_22, assess_order_split_count_23, assess_packaging_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

