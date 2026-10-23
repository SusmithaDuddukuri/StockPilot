"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_route_master_gap_count_01(record):
    """Evaluate route master gaps for control WP-0278-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-01", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-01", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-01", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-01", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_purchase_order_change_count_02(record):
    """Evaluate purchase order changes for control WP-0278-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-02", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-02", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-02", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-02", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "purchase order changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_delivery_geofence_miss_count_03(record):
    """Evaluate delivery geofence misses for control WP-0278-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-03", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-03", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-03", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-03", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "delivery geofence misses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_fuel_surcharge_variance_pct_04(record):
    """Evaluate fuel surcharge variance for control WP-0278-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-04", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-04", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-04", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-04", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fuel surcharge variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_highway_restriction_match_count_05(record):
    """Evaluate highway restriction matches for control WP-0278-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-05", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-05", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-05", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-05", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "highway restriction matches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_recovery_plan_age_days_06(record):
    """Evaluate supplier recovery plan age for control WP-0278-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-06", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-06", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-06", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-06", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier recovery plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_energy_intensity_07(record):
    """Evaluate supplier energy intensity for control WP-0278-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-07", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-07", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-07", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-07", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier energy intensity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_route_risk_score_08(record):
    """Evaluate supplier route risk for control WP-0278-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-08", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-08", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-08", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-08", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier route risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_training_record_pct_09(record):
    """Evaluate supplier training-record completeness for control WP-0278-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-09", "metric": "supplier_training_record_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-09", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-09", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-09", "metric": "supplier_training_record_pct", "label": "supplier training-record completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier training-record completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_payment_delay_days_10(record):
    """Evaluate supplier payment delay for control WP-0278-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-10", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-10", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-10", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-10", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier payment delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_takeback_compliance_pct_11(record):
    """Evaluate supplier take-back compliance for control WP-0278-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-11", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-11", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-11", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-11", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "supplier take-back compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_inventory_visibility_pct_12(record):
    """Evaluate supplier inventory visibility for control WP-0278-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-12", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-12", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-12", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-12", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier inventory visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_capability_study_age_days_13(record):
    """Evaluate supplier capability-study age for control WP-0278-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-13", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-13", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-13", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-13", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capability-study age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_worker_grievance_age_days_14(record):
    """Evaluate supplier worker grievance age for control WP-0278-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-14", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-14", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-14", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-14", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier worker grievance age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_credit_rating_score_15(record):
    """Evaluate supplier credit rating for control WP-0278-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-15", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-15", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-15", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-15", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "supplier credit rating falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_internal_audit_age_days_16(record):
    """Evaluate supplier internal audit age for control WP-0278-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_internal_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-16", "metric": "supplier_internal_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-16", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-16", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-16", "metric": "supplier_internal_audit_age_days", "label": "supplier internal audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier internal audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_prompt_injection_test_age_days_17(record):
    """Evaluate supplier prompt-injection test age for control WP-0278-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prompt_injection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-17", "metric": "supplier_prompt_injection_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-17", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-17", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-17", "metric": "supplier_prompt_injection_test_age_days", "label": "supplier prompt-injection test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier prompt-injection test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_correlation_id_missing_pct_18(record):
    """Evaluate supplier correlation ID missing for control WP-0278-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_correlation_id_missing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-18", "metric": "supplier_correlation_id_missing_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-18", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-18", "metric": "supplier_correlation_id_missing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-18", "metric": "supplier_correlation_id_missing_pct", "label": "supplier correlation ID missing",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier correlation ID missing exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_static_analysis_pct_19(record):
    """Evaluate supplier static analysis coverage for control WP-0278-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_static_analysis_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-19", "metric": "supplier_static_analysis_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-19", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-19", "metric": "supplier_static_analysis_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-19", "metric": "supplier_static_analysis_pct", "label": "supplier static analysis coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier static analysis coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_joiner_mover_leaver_age_hours_20(record):
    """Evaluate supplier JML processing time for control WP-0278-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joiner_mover_leaver_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-20", "metric": "supplier_joiner_mover_leaver_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-20", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-20", "metric": "supplier_joiner_mover_leaver_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-20", "metric": "supplier_joiner_mover_leaver_age_hours", "label": "supplier JML processing time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier JML processing time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_unusual_price_signal_21(record):
    """Evaluate supplier unusual-price signal for control WP-0278-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_unusual_price_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-21", "metric": "supplier_unusual_price_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-21", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-21", "metric": "supplier_unusual_price_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-21", "metric": "supplier_unusual_price_signal", "label": "supplier unusual-price signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier unusual-price signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_delivery_window_change_count_22(record):
    """Evaluate delivery-window changes for control WP-0278-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_window_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-22", "metric": "supplier_delivery_window_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-22", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-22", "metric": "supplier_delivery_window_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-22", "metric": "supplier_delivery_window_change_count", "label": "delivery-window changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "delivery-window changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_invoice_upload_age_hours_23(record):
    """Evaluate supplier invoice upload age for control WP-0278-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-23", "metric": "supplier_invoice_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-23", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-23", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-23", "metric": "supplier_invoice_upload_age_hours", "label": "supplier invoice upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier invoice upload age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_dns_cutover_age_hours_24(record):
    """Evaluate supplier DNS cutover age for control WP-0278-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dns_cutover_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0278-24", "metric": "supplier_dns_cutover_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0278-24", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0278-24", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0278-24", "metric": "supplier_dns_cutover_age_hours", "label": "supplier DNS cutover age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier DNS cutover age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_route_master_gap_count_01, assess_purchase_order_change_count_02, assess_delivery_geofence_miss_count_03, assess_fuel_surcharge_variance_pct_04, assess_highway_restriction_match_count_05, assess_supplier_recovery_plan_age_days_06, assess_supplier_energy_intensity_07, assess_supplier_route_risk_score_08, assess_supplier_training_record_pct_09, assess_supplier_payment_delay_days_10, assess_supplier_takeback_compliance_pct_11, assess_supplier_inventory_visibility_pct_12, assess_supplier_capability_study_age_days_13, assess_supplier_worker_grievance_age_days_14, assess_supplier_credit_rating_score_15, assess_supplier_internal_audit_age_days_16, assess_supplier_prompt_injection_test_age_days_17, assess_supplier_correlation_id_missing_pct_18, assess_supplier_static_analysis_pct_19, assess_supplier_joiner_mover_leaver_age_hours_20, assess_supplier_unusual_price_signal_21, assess_supplier_delivery_window_change_count_22, assess_supplier_invoice_upload_age_hours_23, assess_supplier_dns_cutover_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

