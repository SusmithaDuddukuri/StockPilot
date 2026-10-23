"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_contact_tree_age_days_01(record):
    """Evaluate supplier contact-tree age for control WP-0043-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_tree_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-01", "metric": "supplier_contact_tree_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-01", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-01", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-01", "metric": "supplier_contact_tree_age_days", "label": "supplier contact-tree age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier contact-tree age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_customer_escape_count_02(record):
    """Evaluate supplier customer escapes for control WP-0043-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-02", "metric": "supplier_customer_escape_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-02", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-02", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-02", "metric": "supplier_customer_escape_count", "label": "supplier customer escapes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer escapes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_union_rights_policy_pct_03(record):
    """Evaluate supplier worker-rights policy for control WP-0043-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_union_rights_policy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-03", "metric": "supplier_union_rights_policy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-03", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-03", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-03", "metric": "supplier_union_rights_policy_pct", "label": "supplier worker-rights policy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier worker-rights policy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_site_closure_signal_04(record):
    """Evaluate supplier site-closure signal for control WP-0043-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_closure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-04", "metric": "supplier_site_closure_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-04", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-04", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-04", "metric": "supplier_site_closure_signal", "label": "supplier site-closure signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "supplier site-closure signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_lead_time_reduction_pct_05(record):
    """Evaluate supplier lead-time reduction for control WP-0043-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-05", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-05", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-05", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-05", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier lead-time reduction must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_feature_store_lag_minutes_06(record):
    """Evaluate supplier feature-store lag for control WP-0043-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-06", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-06", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-06", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-06", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier feature-store lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_latency_p99_ms_07(record):
    """Evaluate supplier p99 latency for control WP-0043-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p99_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-07", "metric": "supplier_latency_p99_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-07", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-07", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-07", "metric": "supplier_latency_p99_ms", "label": "supplier p99 latency",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "supplier p99 latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_open_source_notice_pct_08(record):
    """Evaluate supplier open-source notice completeness for control WP-0043-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_source_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-08", "metric": "supplier_open_source_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-08", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-08", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-08", "metric": "supplier_open_source_notice_pct", "label": "supplier open-source notice completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "supplier open-source notice completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_remediation_validation_pct_09(record):
    """Evaluate supplier remediation validation for control WP-0043-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_remediation_validation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-09", "metric": "supplier_remediation_validation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-09", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-09", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-09", "metric": "supplier_remediation_validation_pct", "label": "supplier remediation validation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier remediation validation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_off_contract_spend_pct_10(record):
    """Evaluate supplier off-contract spend for control WP-0043-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_off_contract_spend_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-10", "metric": "supplier_off_contract_spend_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-10", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-10", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-10", "metric": "supplier_off_contract_spend_pct", "label": "supplier off-contract spend",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier off-contract spend must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_first_pass_yield_pct_11(record):
    """Evaluate supplier first-pass yield for control WP-0043-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_first_pass_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-11", "metric": "supplier_first_pass_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-11", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-11", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-11", "metric": "supplier_first_pass_yield_pct", "label": "supplier first-pass yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier first-pass yield exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_joint_planning_age_days_12(record):
    """Evaluate joint planning age for control WP-0043-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joint_planning_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-12", "metric": "supplier_joint_planning_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-12", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-12", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-12", "metric": "supplier_joint_planning_age_days", "label": "joint planning age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "joint planning age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_partner_notice_pct_13(record):
    """Evaluate supplier partner notice completion for control WP-0043-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_partner_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-13", "metric": "supplier_partner_notice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-13", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-13", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-13", "metric": "supplier_partner_notice_pct", "label": "supplier partner notice completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier partner notice completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_forecast_error_pct_14(record):
    """Evaluate forecast error for control WP-0043-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-14", "metric": "forecast_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-14", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-14", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-14", "metric": "forecast_error_pct", "label": "forecast error",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forecast error must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_quality_score_15(record):
    """Evaluate quality score for control WP-0043-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-15", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-15", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-15", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-15", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "quality score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_carrier_exception_count_16(record):
    """Evaluate carrier exceptions for control WP-0043-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-16", "metric": "carrier_exception_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-16", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-16", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-16", "metric": "carrier_exception_count", "label": "carrier exceptions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "carrier exceptions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_ergonomic_risk_score_17(record):
    """Evaluate ergonomic risk for control WP-0043-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-17", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-17", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-17", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-17", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ergonomic risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_insurance_days_left_18(record):
    """Evaluate insurance validity for control WP-0043-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-18", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-18", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-18", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-18", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insurance validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_incident_resolution_hours_19(record):
    """Evaluate incident resolution for control WP-0043-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-19", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-19", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-19", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-19", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "incident resolution exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_forecast_wape_pct_20(record):
    """Evaluate forecast WAPE for control WP-0043-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_wape_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-20", "metric": "forecast_wape_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-20", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-20", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-20", "metric": "forecast_wape_pct", "label": "forecast WAPE",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "forecast WAPE falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_lift_assist_usage_pct_21(record):
    """Evaluate lift-assist usage for control WP-0043-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lift_assist_usage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-21", "metric": "lift_assist_usage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-21", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-21", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-21", "metric": "lift_assist_usage_pct", "label": "lift-assist usage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lift-assist usage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_recovery_case_age_days_22(record):
    """Evaluate recovery case age for control WP-0043-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_case_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-22", "metric": "recovery_case_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-22", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-22", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-22", "metric": "recovery_case_age_days", "label": "recovery case age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recovery case age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_traceability_query_minutes_23(record):
    """Evaluate traceability query time for control WP-0043-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("traceability_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-23", "metric": "traceability_query_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-23", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-23", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-23", "metric": "traceability_query_minutes", "label": "traceability query time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "traceability query time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_lithium_battery_label_pct_24(record):
    """Evaluate lithium battery label compliance for control WP-0043-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lithium_battery_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0043-24", "metric": "lithium_battery_label_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0043-24", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0043-24", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0043-24", "metric": "lithium_battery_label_pct", "label": "lithium battery label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "lithium battery label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_contact_tree_age_days_01, assess_supplier_customer_escape_count_02, assess_supplier_union_rights_policy_pct_03, assess_supplier_site_closure_signal_04, assess_supplier_lead_time_reduction_pct_05, assess_supplier_feature_store_lag_minutes_06, assess_supplier_latency_p99_ms_07, assess_supplier_open_source_notice_pct_08, assess_supplier_remediation_validation_pct_09, assess_supplier_off_contract_spend_pct_10, assess_supplier_first_pass_yield_pct_11, assess_supplier_joint_planning_age_days_12, assess_supplier_partner_notice_pct_13, assess_forecast_error_pct_14, assess_quality_score_15, assess_carrier_exception_count_16, assess_ergonomic_risk_score_17, assess_insurance_days_left_18, assess_incident_resolution_hours_19, assess_forecast_wape_pct_20, assess_lift_assist_usage_pct_21, assess_recovery_case_age_days_22, assess_traceability_query_minutes_23, assess_lithium_battery_label_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

