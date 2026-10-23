"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_privacy_incident_count_01(record):
    """Evaluate supplier privacy incidents for control WP-0351-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-01", "metric": "supplier_privacy_incident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-01", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-01", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-01", "metric": "supplier_privacy_incident_count", "label": "supplier privacy incidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy incidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_action_plan_completion_pct_02(record):
    """Evaluate supplier action-plan completion for control WP-0351-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-02", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-02", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-02", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-02", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier action-plan completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_vulnerability_remediation_days_03(record):
    """Evaluate supplier vulnerability remediation time for control WP-0351-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_remediation_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-03", "metric": "supplier_vulnerability_remediation_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-03", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-03", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-03", "metric": "supplier_vulnerability_remediation_days", "label": "supplier vulnerability remediation time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier vulnerability remediation time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_labor_availability_pct_04(record):
    """Evaluate supplier labor availability for control WP-0351-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-04", "metric": "supplier_labor_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-04", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-04", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-04", "metric": "supplier_labor_availability_pct", "label": "supplier labor availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "supplier labor availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_emission_audit_age_days_05(record):
    """Evaluate supplier emissions audit age for control WP-0351-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emission_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-05", "metric": "supplier_emission_audit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-05", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-05", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-05", "metric": "supplier_emission_audit_age_days", "label": "supplier emissions audit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier emissions audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_exception_latency_minutes_06(record):
    """Evaluate supplier exception latency for control WP-0351-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-06", "metric": "supplier_exception_latency_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-06", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-06", "metric": "supplier_exception_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-06", "metric": "supplier_exception_latency_minutes", "label": "supplier exception latency",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exception latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_corrective_action_effectiveness_pct_07(record):
    """Evaluate supplier corrective-action effectiveness for control WP-0351-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_corrective_action_effectiveness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-07", "metric": "supplier_corrective_action_effectiveness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-07", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-07", "metric": "supplier_corrective_action_effectiveness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-07", "metric": "supplier_corrective_action_effectiveness_pct", "label": "supplier corrective-action effectiveness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "supplier corrective-action effectiveness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_child_labor_screen_pct_08(record):
    """Evaluate supplier child-labor screening for control WP-0351-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_child_labor_screen_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-08", "metric": "supplier_child_labor_screen_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-08", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-08", "metric": "supplier_child_labor_screen_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-08", "metric": "supplier_child_labor_screen_pct", "label": "supplier child-labor screening",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "supplier child-labor screening falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_capacity_drop_pct_09(record):
    """Evaluate supplier capacity drop for control WP-0351-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-09", "metric": "supplier_capacity_drop_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-09", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-09", "metric": "supplier_capacity_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-09", "metric": "supplier_capacity_drop_pct", "label": "supplier capacity drop",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity drop must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_cost_reduction_pct_10(record):
    """Evaluate supplier cost reduction for control WP-0351-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-10", "metric": "supplier_cost_reduction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-10", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-10", "metric": "supplier_cost_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-10", "metric": "supplier_cost_reduction_pct", "label": "supplier cost reduction",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cost reduction must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_carbon_per_inference_11(record):
    """Evaluate supplier carbon per inference for control WP-0351-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carbon_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-11", "metric": "supplier_carbon_per_inference",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-11", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-11", "metric": "supplier_carbon_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-11", "metric": "supplier_carbon_per_inference", "label": "supplier carbon per inference",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "supplier carbon per inference exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_error_budget_remaining_pct_12(record):
    """Evaluate supplier error budget remaining for control WP-0351-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_error_budget_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-12", "metric": "supplier_error_budget_remaining_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-12", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-12", "metric": "supplier_error_budget_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-12", "metric": "supplier_error_budget_remaining_pct", "label": "supplier error budget remaining",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier error budget remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_reproducible_build_pct_13(record):
    """Evaluate supplier reproducible build rate for control WP-0351-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reproducible_build_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-13", "metric": "supplier_reproducible_build_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-13", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-13", "metric": "supplier_reproducible_build_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-13", "metric": "supplier_reproducible_build_pct", "label": "supplier reproducible build rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier reproducible build rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_evidence_freshness_days_14(record):
    """Evaluate supplier evidence freshness for control WP-0351-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_freshness_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-14", "metric": "supplier_evidence_freshness_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-14", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-14", "metric": "supplier_evidence_freshness_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-14", "metric": "supplier_evidence_freshness_days", "label": "supplier evidence freshness",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier evidence freshness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_bank_change_count_15(record):
    """Evaluate supplier bank changes for control WP-0351-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-15", "metric": "supplier_bank_change_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-15", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-15", "metric": "supplier_bank_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-15", "metric": "supplier_bank_change_count", "label": "supplier bank changes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier bank changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_subtier_shortage_count_16(record):
    """Evaluate supplier sub-tier shortages for control WP-0351-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-16", "metric": "supplier_subtier_shortage_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-16", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-16", "metric": "supplier_subtier_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-16", "metric": "supplier_subtier_shortage_count", "label": "supplier sub-tier shortages",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier sub-tier shortages falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_issue_transparency_pct_17(record):
    """Evaluate supplier issue transparency for control WP-0351-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_issue_transparency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-17", "metric": "supplier_issue_transparency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-17", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-17", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-17", "metric": "supplier_issue_transparency_pct", "label": "supplier issue transparency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier issue transparency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_customer_notice_pct_18(record):
    """Evaluate supplier customer notice completion for control WP-0351-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-18", "metric": "supplier_customer_notice_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-18", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-18", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-18", "metric": "supplier_customer_notice_pct", "label": "supplier customer notice completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer notice completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_return_rate_pct_19(record):
    """Evaluate return rate for control WP-0351-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-19", "metric": "return_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-19", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-19", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-19", "metric": "return_rate_pct", "label": "return rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "return rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_payment_hold_count_20(record):
    """Evaluate payment holds for control WP-0351-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_hold_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-20", "metric": "payment_hold_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-20", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-20", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-20", "metric": "payment_hold_count", "label": "payment holds",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "payment holds falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_order_split_count_21(record):
    """Evaluate order splits for control WP-0351-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_split_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-21", "metric": "order_split_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-21", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-21", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-21", "metric": "order_split_count", "label": "order splits",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order splits must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_packaging_compliance_pct_22(record):
    """Evaluate packaging compliance for control WP-0351-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-22", "metric": "packaging_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-22", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-22", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-22", "metric": "packaging_compliance_pct", "label": "packaging compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "packaging compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_export_license_days_left_23(record):
    """Evaluate export license validity for control WP-0351-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-23", "metric": "export_license_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-23", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-23", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-23", "metric": "export_license_days_left", "label": "export license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "export license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_phishing_report_delay_minutes_24(record):
    """Evaluate phishing report delay for control WP-0351-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("phishing_report_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0351-24", "metric": "phishing_report_delay_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0351-24", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0351-24", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0351-24", "metric": "phishing_report_delay_minutes", "label": "phishing report delay",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "phishing report delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_privacy_incident_count_01, assess_supplier_action_plan_completion_pct_02, assess_supplier_vulnerability_remediation_days_03, assess_supplier_labor_availability_pct_04, assess_supplier_emission_audit_age_days_05, assess_supplier_exception_latency_minutes_06, assess_supplier_corrective_action_effectiveness_pct_07, assess_supplier_child_labor_screen_pct_08, assess_supplier_capacity_drop_pct_09, assess_supplier_cost_reduction_pct_10, assess_supplier_carbon_per_inference_11, assess_supplier_error_budget_remaining_pct_12, assess_supplier_reproducible_build_pct_13, assess_supplier_evidence_freshness_days_14, assess_supplier_bank_change_count_15, assess_supplier_subtier_shortage_count_16, assess_supplier_issue_transparency_pct_17, assess_supplier_customer_notice_pct_18, assess_return_rate_pct_19, assess_payment_hold_count_20, assess_order_split_count_21, assess_packaging_compliance_pct_22, assess_export_license_days_left_23, assess_phishing_report_delay_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

