"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_lead_time_reduction_pct_01(record):
    """Evaluate supplier lead-time reduction for control WP-0366-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-01", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-01", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-01", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-01", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier lead-time reduction must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_feature_store_lag_minutes_02(record):
    """Evaluate supplier feature-store lag for control WP-0366-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-02", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-02", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-02", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-02", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier feature-store lag exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_latency_p99_ms_03(record):
    """Evaluate supplier p99 latency for control WP-0366-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p99_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-03", "metric": "supplier_latency_p99_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-03", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-03", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-03", "metric": "supplier_latency_p99_ms", "label": "supplier p99 latency",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier p99 latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_open_source_notice_pct_04(record):
    """Evaluate supplier open-source notice completeness for control WP-0366-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_source_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-04", "metric": "supplier_open_source_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-04", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-04", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-04", "metric": "supplier_open_source_notice_pct", "label": "supplier open-source notice completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier open-source notice completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_remediation_validation_pct_05(record):
    """Evaluate supplier remediation validation for control WP-0366-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_remediation_validation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-05", "metric": "supplier_remediation_validation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-05", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-05", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-05", "metric": "supplier_remediation_validation_pct", "label": "supplier remediation validation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier remediation validation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_off_contract_spend_pct_06(record):
    """Evaluate supplier off-contract spend for control WP-0366-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_off_contract_spend_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-06", "metric": "supplier_off_contract_spend_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-06", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-06", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-06", "metric": "supplier_off_contract_spend_pct", "label": "supplier off-contract spend",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier off-contract spend exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_first_pass_yield_pct_07(record):
    """Evaluate supplier first-pass yield for control WP-0366-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_first_pass_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-07", "metric": "supplier_first_pass_yield_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-07", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-07", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-07", "metric": "supplier_first_pass_yield_pct", "label": "supplier first-pass yield",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "supplier first-pass yield falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_joint_planning_age_days_08(record):
    """Evaluate joint planning age for control WP-0366-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joint_planning_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-08", "metric": "supplier_joint_planning_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-08", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-08", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-08", "metric": "supplier_joint_planning_age_days", "label": "joint planning age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "joint planning age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_partner_notice_pct_09(record):
    """Evaluate supplier partner notice completion for control WP-0366-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_partner_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-09", "metric": "supplier_partner_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-09", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-09", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-09", "metric": "supplier_partner_notice_pct", "label": "supplier partner notice completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier partner notice completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_forecast_error_pct_10(record):
    """Evaluate forecast error for control WP-0366-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-10", "metric": "forecast_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-10", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-10", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-10", "metric": "forecast_error_pct", "label": "forecast error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "forecast error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_quality_score_11(record):
    """Evaluate quality score for control WP-0366-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-11", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-11", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-11", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-11", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "quality score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_carrier_exception_count_12(record):
    """Evaluate carrier exceptions for control WP-0366-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-12", "metric": "carrier_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-12", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-12", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-12", "metric": "carrier_exception_count", "label": "carrier exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier exceptions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_ergonomic_risk_score_13(record):
    """Evaluate ergonomic risk for control WP-0366-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-13", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-13", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-13", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-13", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "ergonomic risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_insurance_days_left_14(record):
    """Evaluate insurance validity for control WP-0366-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-14", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-14", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-14", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-14", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "insurance validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_incident_resolution_hours_15(record):
    """Evaluate incident resolution for control WP-0366-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-15", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-15", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-15", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-15", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "incident resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_forecast_wape_pct_16(record):
    """Evaluate forecast WAPE for control WP-0366-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_wape_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-16", "metric": "forecast_wape_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-16", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-16", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-16", "metric": "forecast_wape_pct", "label": "forecast WAPE",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast WAPE must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_lift_assist_usage_pct_17(record):
    """Evaluate lift-assist usage for control WP-0366-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lift_assist_usage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-17", "metric": "lift_assist_usage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-17", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-17", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-17", "metric": "lift_assist_usage_pct", "label": "lift-assist usage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lift-assist usage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_recovery_case_age_days_18(record):
    """Evaluate recovery case age for control WP-0366-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_case_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-18", "metric": "recovery_case_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-18", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-18", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-18", "metric": "recovery_case_age_days", "label": "recovery case age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "recovery case age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_traceability_query_minutes_19(record):
    """Evaluate traceability query time for control WP-0366-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("traceability_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-19", "metric": "traceability_query_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-19", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-19", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-19", "metric": "traceability_query_minutes", "label": "traceability query time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "traceability query time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_lithium_battery_label_pct_20(record):
    """Evaluate lithium battery label compliance for control WP-0366-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lithium_battery_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-20", "metric": "lithium_battery_label_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-20", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-20", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-20", "metric": "lithium_battery_label_pct", "label": "lithium battery label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lithium battery label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_near_miss_close_rate_pct_21(record):
    """Evaluate near-miss close rate for control WP-0366-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_close_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-21", "metric": "near_miss_close_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-21", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-21", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-21", "metric": "near_miss_close_rate_pct", "label": "near-miss close rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "near-miss close rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_public_address_test_age_days_22(record):
    """Evaluate public-address test age for control WP-0366-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("public_address_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-22", "metric": "public_address_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-22", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-22", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-22", "metric": "public_address_test_age_days", "label": "public-address test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "public-address test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_license_compliance_pct_23(record):
    """Evaluate license compliance for control WP-0366-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-23", "metric": "license_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-23", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-23", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-23", "metric": "license_compliance_pct", "label": "license compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "license compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_rfid_collision_count_24(record):
    """Evaluate RFID collisions for control WP-0366-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_collision_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0366-24", "metric": "rfid_collision_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0366-24", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0366-24", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0366-24", "metric": "rfid_collision_count", "label": "RFID collisions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "RFID collisions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_supplier_lead_time_reduction_pct_01, assess_supplier_feature_store_lag_minutes_02, assess_supplier_latency_p99_ms_03, assess_supplier_open_source_notice_pct_04, assess_supplier_remediation_validation_pct_05, assess_supplier_off_contract_spend_pct_06, assess_supplier_first_pass_yield_pct_07, assess_supplier_joint_planning_age_days_08, assess_supplier_partner_notice_pct_09, assess_forecast_error_pct_10, assess_quality_score_11, assess_carrier_exception_count_12, assess_ergonomic_risk_score_13, assess_insurance_days_left_14, assess_incident_resolution_hours_15, assess_forecast_wape_pct_16, assess_lift_assist_usage_pct_17, assess_recovery_case_age_days_18, assess_traceability_query_minutes_19, assess_lithium_battery_label_pct_20, assess_near_miss_close_rate_pct_21, assess_public_address_test_age_days_22, assess_license_compliance_pct_23, assess_rfid_collision_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

