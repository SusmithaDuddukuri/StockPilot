"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_patch_age_days_01(record):
    """Evaluate supplier patch age for control WP-0541-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-01", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-01", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-01", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-01", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier patch age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_recovery_lead_days_02(record):
    """Evaluate supplier recovery lead time for control WP-0541-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-02", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-02", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-02", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-02", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "supplier recovery lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_subprocessor_count_03(record):
    """Evaluate supplier sub-processors for control WP-0541-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-03", "metric": "supplier_subprocessor_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "entities",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-03", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-03", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-03", "metric": "supplier_subprocessor_count", "label": "supplier sub-processors",
        "status": "breach", "severity": "critical", "unit": "entities",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sub-processors must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_water_continuity_score_04(record):
    """Evaluate supplier water continuity for control WP-0541-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-04", "metric": "supplier_water_continuity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-04", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-04", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-04", "metric": "supplier_water_continuity_score", "label": "supplier water continuity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier water continuity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_climate_plan_age_days_05(record):
    """Evaluate supplier climate-plan age for control WP-0541-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_climate_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-05", "metric": "supplier_climate_plan_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-05", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-05", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-05", "metric": "supplier_climate_plan_age_days", "label": "supplier climate-plan age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier climate-plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_contact_tree_age_days_06(record):
    """Evaluate supplier contact-tree age for control WP-0541-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_tree_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-06", "metric": "supplier_contact_tree_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-06", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-06", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-06", "metric": "supplier_contact_tree_age_days", "label": "supplier contact-tree age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier contact-tree age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_customer_escape_count_07(record):
    """Evaluate supplier customer escapes for control WP-0541-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-07", "metric": "supplier_customer_escape_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-07", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-07", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-07", "metric": "supplier_customer_escape_count", "label": "supplier customer escapes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer escapes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_union_rights_policy_pct_08(record):
    """Evaluate supplier worker-rights policy for control WP-0541-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_union_rights_policy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-08", "metric": "supplier_union_rights_policy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-08", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-08", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-08", "metric": "supplier_union_rights_policy_pct", "label": "supplier worker-rights policy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier worker-rights policy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_site_closure_signal_09(record):
    """Evaluate supplier site-closure signal for control WP-0541-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_closure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-09", "metric": "supplier_site_closure_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-09", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-09", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-09", "metric": "supplier_site_closure_signal", "label": "supplier site-closure signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier site-closure signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_lead_time_reduction_pct_10(record):
    """Evaluate supplier lead-time reduction for control WP-0541-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-10", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-10", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-10", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-10", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier lead-time reduction falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_feature_store_lag_minutes_11(record):
    """Evaluate supplier feature-store lag for control WP-0541-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-11", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-11", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-11", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-11", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier feature-store lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_latency_p99_ms_12(record):
    """Evaluate supplier p99 latency for control WP-0541-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p99_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-12", "metric": "supplier_latency_p99_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-12", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-12", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-12", "metric": "supplier_latency_p99_ms", "label": "supplier p99 latency",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier p99 latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_open_source_notice_pct_13(record):
    """Evaluate supplier open-source notice completeness for control WP-0541-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_source_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-13", "metric": "supplier_open_source_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-13", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-13", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-13", "metric": "supplier_open_source_notice_pct", "label": "supplier open-source notice completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier open-source notice completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_remediation_validation_pct_14(record):
    """Evaluate supplier remediation validation for control WP-0541-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_remediation_validation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-14", "metric": "supplier_remediation_validation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-14", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-14", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-14", "metric": "supplier_remediation_validation_pct", "label": "supplier remediation validation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "supplier remediation validation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_off_contract_spend_pct_15(record):
    """Evaluate supplier off-contract spend for control WP-0541-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_off_contract_spend_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-15", "metric": "supplier_off_contract_spend_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-15", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-15", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-15", "metric": "supplier_off_contract_spend_pct", "label": "supplier off-contract spend",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier off-contract spend must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_first_pass_yield_pct_16(record):
    """Evaluate supplier first-pass yield for control WP-0541-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_first_pass_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-16", "metric": "supplier_first_pass_yield_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-16", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-16", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-16", "metric": "supplier_first_pass_yield_pct", "label": "supplier first-pass yield",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier first-pass yield must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_joint_planning_age_days_17(record):
    """Evaluate joint planning age for control WP-0541-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joint_planning_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-17", "metric": "supplier_joint_planning_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-17", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-17", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-17", "metric": "supplier_joint_planning_age_days", "label": "joint planning age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "joint planning age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_partner_notice_pct_18(record):
    """Evaluate supplier partner notice completion for control WP-0541-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_partner_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-18", "metric": "supplier_partner_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-18", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-18", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-18", "metric": "supplier_partner_notice_pct", "label": "supplier partner notice completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier partner notice completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_forecast_error_pct_19(record):
    """Evaluate forecast error for control WP-0541-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-19", "metric": "forecast_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-19", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-19", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-19", "metric": "forecast_error_pct", "label": "forecast error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast error must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_quality_score_20(record):
    """Evaluate quality score for control WP-0541-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-20", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-20", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-20", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-20", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quality score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_carrier_exception_count_21(record):
    """Evaluate carrier exceptions for control WP-0541-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-21", "metric": "carrier_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-21", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-21", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-21", "metric": "carrier_exception_count", "label": "carrier exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "carrier exceptions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_ergonomic_risk_score_22(record):
    """Evaluate ergonomic risk for control WP-0541-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-22", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-22", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-22", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-22", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "ergonomic risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_insurance_days_left_23(record):
    """Evaluate insurance validity for control WP-0541-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-23", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-23", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-23", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-23", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insurance validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_incident_resolution_hours_24(record):
    """Evaluate incident resolution for control WP-0541-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0541-24", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0541-24", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0541-24", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0541-24", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident resolution must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_patch_age_days_01, assess_supplier_recovery_lead_days_02, assess_supplier_subprocessor_count_03, assess_supplier_water_continuity_score_04, assess_supplier_climate_plan_age_days_05, assess_supplier_contact_tree_age_days_06, assess_supplier_customer_escape_count_07, assess_supplier_union_rights_policy_pct_08, assess_supplier_site_closure_signal_09, assess_supplier_lead_time_reduction_pct_10, assess_supplier_feature_store_lag_minutes_11, assess_supplier_latency_p99_ms_12, assess_supplier_open_source_notice_pct_13, assess_supplier_remediation_validation_pct_14, assess_supplier_off_contract_spend_pct_15, assess_supplier_first_pass_yield_pct_16, assess_supplier_joint_planning_age_days_17, assess_supplier_partner_notice_pct_18, assess_forecast_error_pct_19, assess_quality_score_20, assess_carrier_exception_count_21, assess_ergonomic_risk_score_22, assess_insurance_days_left_23, assess_incident_resolution_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

