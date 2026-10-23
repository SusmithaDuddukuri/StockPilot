"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_order_cancellation_pct_01(record):
    """Evaluate order cancellation rate for control WP-0218-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_cancellation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-01", "metric": "order_cancellation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-01", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-01", "metric": "order_cancellation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-01", "metric": "order_cancellation_pct", "label": "order cancellation rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order cancellation rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_port_dwell_days_02(record):
    """Evaluate port dwell for control WP-0218-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("port_dwell_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-02", "metric": "port_dwell_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-02", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-02", "metric": "port_dwell_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-02", "metric": "port_dwell_days", "label": "port dwell",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "port dwell exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_labor_cost_per_unit_03(record):
    """Evaluate labor cost per unit for control WP-0218-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_cost_per_unit")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-03", "metric": "labor_cost_per_unit",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-03", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-03", "metric": "labor_cost_per_unit", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-03", "metric": "labor_cost_per_unit", "label": "labor cost per unit",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "labor cost per unit falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_ethics_report_age_days_04(record):
    """Evaluate supplier ethics report age for control WP-0218-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_report_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-04", "metric": "supplier_ethics_report_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-04", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-04", "metric": "supplier_ethics_report_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-04", "metric": "supplier_ethics_report_age_days", "label": "supplier ethics report age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ethics report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_patch_age_days_05(record):
    """Evaluate supplier patch age for control WP-0218-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-05", "metric": "supplier_patch_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-05", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-05", "metric": "supplier_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-05", "metric": "supplier_patch_age_days", "label": "supplier patch age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_recovery_lead_days_06(record):
    """Evaluate supplier recovery lead time for control WP-0218-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-06", "metric": "supplier_recovery_lead_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-06", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-06", "metric": "supplier_recovery_lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-06", "metric": "supplier_recovery_lead_days", "label": "supplier recovery lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier recovery lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_subprocessor_count_07(record):
    """Evaluate supplier sub-processors for control WP-0218-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-07", "metric": "supplier_subprocessor_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "entities",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-07", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-07", "metric": "supplier_subprocessor_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-07", "metric": "supplier_subprocessor_count", "label": "supplier sub-processors",
        "status": "breach", "severity": "low", "unit": "entities",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "supplier sub-processors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_water_continuity_score_08(record):
    """Evaluate supplier water continuity for control WP-0218-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-08", "metric": "supplier_water_continuity_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-08", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-08", "metric": "supplier_water_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-08", "metric": "supplier_water_continuity_score", "label": "supplier water continuity",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water continuity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_climate_plan_age_days_09(record):
    """Evaluate supplier climate-plan age for control WP-0218-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_climate_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-09", "metric": "supplier_climate_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-09", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-09", "metric": "supplier_climate_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-09", "metric": "supplier_climate_plan_age_days", "label": "supplier climate-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier climate-plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_contact_tree_age_days_10(record):
    """Evaluate supplier contact-tree age for control WP-0218-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_tree_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-10", "metric": "supplier_contact_tree_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-10", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-10", "metric": "supplier_contact_tree_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-10", "metric": "supplier_contact_tree_age_days", "label": "supplier contact-tree age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier contact-tree age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_customer_escape_count_11(record):
    """Evaluate supplier customer escapes for control WP-0218-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_escape_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-11", "metric": "supplier_customer_escape_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-11", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-11", "metric": "supplier_customer_escape_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-11", "metric": "supplier_customer_escape_count", "label": "supplier customer escapes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier customer escapes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_union_rights_policy_pct_12(record):
    """Evaluate supplier worker-rights policy for control WP-0218-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_union_rights_policy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-12", "metric": "supplier_union_rights_policy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-12", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-12", "metric": "supplier_union_rights_policy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-12", "metric": "supplier_union_rights_policy_pct", "label": "supplier worker-rights policy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier worker-rights policy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_site_closure_signal_13(record):
    """Evaluate supplier site-closure signal for control WP-0218-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_closure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-13", "metric": "supplier_site_closure_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-13", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-13", "metric": "supplier_site_closure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-13", "metric": "supplier_site_closure_signal", "label": "supplier site-closure signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier site-closure signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_lead_time_reduction_pct_14(record):
    """Evaluate supplier lead-time reduction for control WP-0218-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lead_time_reduction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-14", "metric": "supplier_lead_time_reduction_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-14", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-14", "metric": "supplier_lead_time_reduction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-14", "metric": "supplier_lead_time_reduction_pct", "label": "supplier lead-time reduction",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "supplier lead-time reduction exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_feature_store_lag_minutes_15(record):
    """Evaluate supplier feature-store lag for control WP-0218-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_store_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-15", "metric": "supplier_feature_store_lag_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-15", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-15", "metric": "supplier_feature_store_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-15", "metric": "supplier_feature_store_lag_minutes", "label": "supplier feature-store lag",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier feature-store lag falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_latency_p99_ms_16(record):
    """Evaluate supplier p99 latency for control WP-0218-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_latency_p99_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-16", "metric": "supplier_latency_p99_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-16", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-16", "metric": "supplier_latency_p99_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-16", "metric": "supplier_latency_p99_ms", "label": "supplier p99 latency",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier p99 latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_open_source_notice_pct_17(record):
    """Evaluate supplier open-source notice completeness for control WP-0218-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_source_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-17", "metric": "supplier_open_source_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-17", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-17", "metric": "supplier_open_source_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-17", "metric": "supplier_open_source_notice_pct", "label": "supplier open-source notice completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier open-source notice completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_remediation_validation_pct_18(record):
    """Evaluate supplier remediation validation for control WP-0218-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_remediation_validation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-18", "metric": "supplier_remediation_validation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-18", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-18", "metric": "supplier_remediation_validation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-18", "metric": "supplier_remediation_validation_pct", "label": "supplier remediation validation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier remediation validation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_off_contract_spend_pct_19(record):
    """Evaluate supplier off-contract spend for control WP-0218-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_off_contract_spend_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-19", "metric": "supplier_off_contract_spend_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-19", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-19", "metric": "supplier_off_contract_spend_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-19", "metric": "supplier_off_contract_spend_pct", "label": "supplier off-contract spend",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier off-contract spend falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_first_pass_yield_pct_20(record):
    """Evaluate supplier first-pass yield for control WP-0218-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_first_pass_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-20", "metric": "supplier_first_pass_yield_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-20", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-20", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-20", "metric": "supplier_first_pass_yield_pct", "label": "supplier first-pass yield",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier first-pass yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_joint_planning_age_days_21(record):
    """Evaluate joint planning age for control WP-0218-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joint_planning_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-21", "metric": "supplier_joint_planning_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-21", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-21", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-21", "metric": "supplier_joint_planning_age_days", "label": "joint planning age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "joint planning age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_partner_notice_pct_22(record):
    """Evaluate supplier partner notice completion for control WP-0218-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_partner_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-22", "metric": "supplier_partner_notice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-22", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-22", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-22", "metric": "supplier_partner_notice_pct", "label": "supplier partner notice completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier partner notice completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_forecast_error_pct_23(record):
    """Evaluate forecast error for control WP-0218-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-23", "metric": "forecast_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-23", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-23", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-23", "metric": "forecast_error_pct", "label": "forecast error",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "forecast error falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_quality_score_24(record):
    """Evaluate quality score for control WP-0218-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0218-24", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0218-24", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0218-24", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0218-24", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_order_cancellation_pct_01, assess_port_dwell_days_02, assess_labor_cost_per_unit_03, assess_supplier_ethics_report_age_days_04, assess_supplier_patch_age_days_05, assess_supplier_recovery_lead_days_06, assess_supplier_subprocessor_count_07, assess_supplier_water_continuity_score_08, assess_supplier_climate_plan_age_days_09, assess_supplier_contact_tree_age_days_10, assess_supplier_customer_escape_count_11, assess_supplier_union_rights_policy_pct_12, assess_supplier_site_closure_signal_13, assess_supplier_lead_time_reduction_pct_14, assess_supplier_feature_store_lag_minutes_15, assess_supplier_latency_p99_ms_16, assess_supplier_open_source_notice_pct_17, assess_supplier_remediation_validation_pct_18, assess_supplier_off_contract_spend_pct_19, assess_supplier_first_pass_yield_pct_20, assess_supplier_joint_planning_age_days_21, assess_supplier_partner_notice_pct_22, assess_forecast_error_pct_23, assess_quality_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

