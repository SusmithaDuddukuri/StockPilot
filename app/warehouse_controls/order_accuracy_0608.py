"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_cloud_region_gap_count_01(record):
    """Evaluate supplier cloud-region gaps for control WP-0608-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cloud_region_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-01", "metric": "supplier_cloud_region_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-01", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-01", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-01", "metric": "supplier_cloud_region_gap_count", "label": "supplier cloud-region gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier cloud-region gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_transport_alternative_count_02(record):
    """Evaluate supplier transport alternatives for control WP-0608-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transport_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-02", "metric": "supplier_transport_alternative_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "routes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-02", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-02", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-02", "metric": "supplier_transport_alternative_count", "label": "supplier transport alternatives",
        "status": "breach", "severity": "medium", "unit": "routes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transport alternatives must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_adaptation_score_03(record):
    """Evaluate supplier climate adaptation for control WP-0608-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adaptation_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-03", "metric": "supplier_adaptation_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-03", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-03", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-03", "metric": "supplier_adaptation_score", "label": "supplier climate adaptation",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier climate adaptation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_crisis_drill_age_days_04(record):
    """Evaluate supplier crisis drill age for control WP-0608-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-04", "metric": "supplier_crisis_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-04", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-04", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-04", "metric": "supplier_crisis_drill_age_days", "label": "supplier crisis drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier crisis drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_audit_finding_age_days_05(record):
    """Evaluate supplier audit-finding age for control WP-0608-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_finding_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-05", "metric": "supplier_audit_finding_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-05", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-05", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-05", "metric": "supplier_audit_finding_age_days", "label": "supplier audit-finding age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier audit-finding age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_diversity_score_06(record):
    """Evaluate supplier diversity score for control WP-0608-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_diversity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-06", "metric": "supplier_diversity_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-06", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-06", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-06", "metric": "supplier_diversity_score", "label": "supplier diversity score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier diversity score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_disaster_exposure_score_07(record):
    """Evaluate supplier disaster exposure for control WP-0608-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disaster_exposure_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-07", "metric": "supplier_disaster_exposure_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-07", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-07", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-07", "metric": "supplier_disaster_exposure_score", "label": "supplier disaster exposure",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier disaster exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_quality_improvement_pct_08(record):
    """Evaluate supplier quality improvement for control WP-0608-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-08", "metric": "supplier_quality_improvement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-08", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-08", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-08", "metric": "supplier_quality_improvement_pct", "label": "supplier quality improvement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "supplier quality improvement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_embedding_index_age_hours_09(record):
    """Evaluate supplier embedding index age for control WP-0608-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_embedding_index_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-09", "metric": "supplier_embedding_index_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-09", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-09", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-09", "metric": "supplier_embedding_index_age_hours", "label": "supplier embedding index age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier embedding index age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_throughput_variance_pct_10(record):
    """Evaluate supplier throughput variance for control WP-0608-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_throughput_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-10", "metric": "supplier_throughput_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-10", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-10", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-10", "metric": "supplier_throughput_variance_pct", "label": "supplier throughput variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier throughput variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_license_review_age_days_11(record):
    """Evaluate supplier license review age for control WP-0608-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-11", "metric": "supplier_license_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-11", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-11", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-11", "metric": "supplier_license_review_age_days", "label": "supplier license review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier license review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_regulator_request_age_days_12(record):
    """Evaluate supplier regulator request age for control WP-0608-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-12", "metric": "supplier_regulator_request_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-12", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-12", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-12", "metric": "supplier_regulator_request_age_days", "label": "supplier regulator request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "supplier regulator request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_maverick_buy_pct_13(record):
    """Evaluate supplier maverick buying for control WP-0608-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_maverick_buy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-13", "metric": "supplier_maverick_buy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-13", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-13", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-13", "metric": "supplier_maverick_buy_pct", "label": "supplier maverick buying",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "supplier maverick buying falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_rework_pct_14(record):
    """Evaluate supplier rework rate for control WP-0608-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rework_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-14", "metric": "supplier_rework_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-14", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-14", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-14", "metric": "supplier_rework_pct", "label": "supplier rework rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier rework rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_business_review_age_days_15(record):
    """Evaluate business review age for control WP-0608-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-15", "metric": "supplier_business_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-15", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-15", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-15", "metric": "supplier_business_review_age_days", "label": "business review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "business review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_contract_termination_age_days_16(record):
    """Evaluate supplier contract termination age for control WP-0608-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contract_termination_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-16", "metric": "supplier_contract_termination_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-16", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-16", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-16", "metric": "supplier_contract_termination_age_days", "label": "supplier contract termination age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier contract termination age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_fill_rate_pct_17(record):
    """Evaluate order fill rate for control WP-0608-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-17", "metric": "fill_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-17", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-17", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-17", "metric": "fill_rate_pct", "label": "order fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "order fill rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_defect_count_18(record):
    """Evaluate supplier defects for control WP-0608-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-18", "metric": "supplier_defect_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-18", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-18", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-18", "metric": "supplier_defect_count", "label": "supplier defects",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier defects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_dock_to_stock_minutes_19(record):
    """Evaluate dock-to-stock time for control WP-0608-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_to_stock_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-19", "metric": "dock_to_stock_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-19", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-19", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-19", "metric": "dock_to_stock_minutes", "label": "dock-to-stock time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock-to-stock time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_near_miss_count_20(record):
    """Evaluate near misses for control WP-0608-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-20", "metric": "near_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-20", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-20", "metric": "near_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-20", "metric": "near_miss_count", "label": "near misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "near misses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_contract_days_left_21(record):
    """Evaluate contract validity for control WP-0608-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-21", "metric": "contract_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-21", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-21", "metric": "contract_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-21", "metric": "contract_days_left", "label": "contract validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "contract validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_backup_success_pct_22(record):
    """Evaluate backup success rate for control WP-0608-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-22", "metric": "backup_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-22", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-22", "metric": "backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-22", "metric": "backup_success_pct", "label": "backup success rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backup success rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_service_level_pct_23(record):
    """Evaluate service level for control WP-0608-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_level_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-23", "metric": "service_level_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-23", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-23", "metric": "service_level_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-23", "metric": "service_level_pct", "label": "service level",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "service level must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_manual_handling_weight_kg_24(record):
    """Evaluate manual handling weight for control WP-0608-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("manual_handling_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0608-24", "metric": "manual_handling_weight_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0608-24", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0608-24", "metric": "manual_handling_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0608-24", "metric": "manual_handling_weight_kg", "label": "manual handling weight",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "manual handling weight exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_cloud_region_gap_count_01, assess_supplier_transport_alternative_count_02, assess_supplier_adaptation_score_03, assess_supplier_crisis_drill_age_days_04, assess_supplier_audit_finding_age_days_05, assess_supplier_diversity_score_06, assess_supplier_disaster_exposure_score_07, assess_supplier_quality_improvement_pct_08, assess_supplier_embedding_index_age_hours_09, assess_supplier_throughput_variance_pct_10, assess_supplier_license_review_age_days_11, assess_supplier_regulator_request_age_days_12, assess_supplier_maverick_buy_pct_13, assess_supplier_rework_pct_14, assess_supplier_business_review_age_days_15, assess_supplier_contract_termination_age_days_16, assess_fill_rate_pct_17, assess_supplier_defect_count_18, assess_dock_to_stock_minutes_19, assess_near_miss_count_20, assess_contract_days_left_21, assess_backup_success_pct_22, assess_service_level_pct_23, assess_manual_handling_weight_kg_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

