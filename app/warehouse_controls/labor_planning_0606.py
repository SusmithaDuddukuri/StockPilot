"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_action_plan_completion_pct_01(record):
    """Evaluate supplier action-plan completion for control WP-0606-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-01", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-01", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-01", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-01", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier action-plan completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_vulnerability_remediation_days_02(record):
    """Evaluate supplier vulnerability remediation time for control WP-0606-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_remediation_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-02", "metric": "supplier_vulnerability_remediation_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-02", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-02", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-02", "metric": "supplier_vulnerability_remediation_days", "label": "supplier vulnerability remediation time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier vulnerability remediation time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_labor_availability_pct_03(record):
    """Evaluate supplier labor availability for control WP-0606-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-03", "metric": "supplier_labor_availability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-03", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-03", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-03", "metric": "supplier_labor_availability_pct", "label": "supplier labor availability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier labor availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_emission_audit_age_days_04(record):
    """Evaluate supplier emissions audit age for control WP-0606-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emission_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-04", "metric": "supplier_emission_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-04", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-04", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-04", "metric": "supplier_emission_audit_age_days", "label": "supplier emissions audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier emissions audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_exception_latency_minutes_05(record):
    """Evaluate supplier exception latency for control WP-0606-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-05", "metric": "supplier_exception_latency_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-05", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-05", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-05", "metric": "supplier_exception_latency_minutes", "label": "supplier exception latency",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exception latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_corrective_action_effectiveness_pct_06(record):
    """Evaluate supplier corrective-action effectiveness for control WP-0606-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_effectiveness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-06", "metric": "supplier_corrective_action_effectiveness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-06", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-06", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-06", "metric": "supplier_corrective_action_effectiveness_pct", "label": "supplier corrective-action effectiveness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier corrective-action effectiveness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_child_labor_screen_pct_07(record):
    """Evaluate supplier child-labor screening for control WP-0606-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_child_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-07", "metric": "supplier_child_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-07", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-07", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-07", "metric": "supplier_child_labor_screen_pct", "label": "supplier child-labor screening",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier child-labor screening falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_capacity_drop_pct_08(record):
    """Evaluate supplier capacity drop for control WP-0606-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-08", "metric": "supplier_capacity_drop_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-08", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-08", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-08", "metric": "supplier_capacity_drop_pct", "label": "supplier capacity drop",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity drop must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_cost_reduction_pct_09(record):
    """Evaluate supplier cost reduction for control WP-0606-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-09", "metric": "supplier_cost_reduction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-09", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-09", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-09", "metric": "supplier_cost_reduction_pct", "label": "supplier cost reduction",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cost reduction must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_carbon_per_inference_10(record):
    """Evaluate supplier carbon per inference for control WP-0606-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carbon_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-10", "metric": "supplier_carbon_per_inference",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-10", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-10", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-10", "metric": "supplier_carbon_per_inference", "label": "supplier carbon per inference",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier carbon per inference exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_error_budget_remaining_pct_11(record):
    """Evaluate supplier error budget remaining for control WP-0606-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_error_budget_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-11", "metric": "supplier_error_budget_remaining_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-11", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-11", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-11", "metric": "supplier_error_budget_remaining_pct", "label": "supplier error budget remaining",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier error budget remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_reproducible_build_pct_12(record):
    """Evaluate supplier reproducible build rate for control WP-0606-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reproducible_build_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-12", "metric": "supplier_reproducible_build_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-12", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-12", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-12", "metric": "supplier_reproducible_build_pct", "label": "supplier reproducible build rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier reproducible build rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_evidence_freshness_days_13(record):
    """Evaluate supplier evidence freshness for control WP-0606-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_freshness_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-13", "metric": "supplier_evidence_freshness_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-13", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-13", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-13", "metric": "supplier_evidence_freshness_days", "label": "supplier evidence freshness",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier evidence freshness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_bank_change_count_14(record):
    """Evaluate supplier bank changes for control WP-0606-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-14", "metric": "supplier_bank_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-14", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-14", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-14", "metric": "supplier_bank_change_count", "label": "supplier bank changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier bank changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_subtier_shortage_count_15(record):
    """Evaluate supplier sub-tier shortages for control WP-0606-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-15", "metric": "supplier_subtier_shortage_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-15", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-15", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-15", "metric": "supplier_subtier_shortage_count", "label": "supplier sub-tier shortages",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier sub-tier shortages falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_issue_transparency_pct_16(record):
    """Evaluate supplier issue transparency for control WP-0606-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_issue_transparency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-16", "metric": "supplier_issue_transparency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-16", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-16", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-16", "metric": "supplier_issue_transparency_pct", "label": "supplier issue transparency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier issue transparency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_customer_notice_pct_17(record):
    """Evaluate supplier customer notice completion for control WP-0606-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-17", "metric": "supplier_customer_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-17", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-17", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-17", "metric": "supplier_customer_notice_pct", "label": "supplier customer notice completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer notice completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_return_rate_pct_18(record):
    """Evaluate return rate for control WP-0606-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-18", "metric": "return_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-18", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-18", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-18", "metric": "return_rate_pct", "label": "return rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "return rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_payment_hold_count_19(record):
    """Evaluate payment holds for control WP-0606-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_hold_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-19", "metric": "payment_hold_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-19", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-19", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-19", "metric": "payment_hold_count", "label": "payment holds",
        "status": "breach", "severity": "low", "unit": "orders",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "payment holds falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_order_split_count_20(record):
    """Evaluate order splits for control WP-0606-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_split_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-20", "metric": "order_split_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-20", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-20", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-20", "metric": "order_split_count", "label": "order splits",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order splits must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_packaging_compliance_pct_21(record):
    """Evaluate packaging compliance for control WP-0606-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-21", "metric": "packaging_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-21", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-21", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-21", "metric": "packaging_compliance_pct", "label": "packaging compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "packaging compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_export_license_days_left_22(record):
    """Evaluate export license validity for control WP-0606-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-22", "metric": "export_license_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-22", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-22", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-22", "metric": "export_license_days_left", "label": "export license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "export license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_phishing_report_delay_minutes_23(record):
    """Evaluate phishing report delay for control WP-0606-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("phishing_report_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-23", "metric": "phishing_report_delay_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-23", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-23", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-23", "metric": "phishing_report_delay_minutes", "label": "phishing report delay",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "phishing report delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_quote_age_hours_24(record):
    """Evaluate quote age for control WP-0606-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quote_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0606-24", "metric": "quote_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0606-24", "metric": "quote_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0606-24", "metric": "quote_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0606-24", "metric": "quote_age_hours", "label": "quote age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quote age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_supplier_action_plan_completion_pct_01, assess_supplier_vulnerability_remediation_days_02, assess_supplier_labor_availability_pct_03, assess_supplier_emission_audit_age_days_04, assess_supplier_exception_latency_minutes_05, assess_supplier_corrective_action_effectiveness_pct_06, assess_supplier_child_labor_screen_pct_07, assess_supplier_capacity_drop_pct_08, assess_supplier_cost_reduction_pct_09, assess_supplier_carbon_per_inference_10, assess_supplier_error_budget_remaining_pct_11, assess_supplier_reproducible_build_pct_12, assess_supplier_evidence_freshness_days_13, assess_supplier_bank_change_count_14, assess_supplier_subtier_shortage_count_15, assess_supplier_issue_transparency_pct_16, assess_supplier_customer_notice_pct_17, assess_return_rate_pct_18, assess_payment_hold_count_19, assess_order_split_count_20, assess_packaging_compliance_pct_21, assess_export_license_days_left_22, assess_phishing_report_delay_minutes_23, assess_quote_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

