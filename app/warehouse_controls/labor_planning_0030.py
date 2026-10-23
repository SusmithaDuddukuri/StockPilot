"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_intermodal_transfer_delay_hours_01(record):
    """Evaluate intermodal transfer delay for control WP-0030-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("intermodal_transfer_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-01", "metric": "intermodal_transfer_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-01", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-01", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-01", "metric": "intermodal_transfer_delay_hours", "label": "intermodal transfer delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "intermodal transfer delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_warehouse_cost_per_sq_m_02(record):
    """Evaluate warehouse cost per square meter for control WP-0030-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_cost_per_sq_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-02", "metric": "warehouse_cost_per_sq_m",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-02", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-02", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-02", "metric": "warehouse_cost_per_sq_m", "label": "warehouse cost per square meter",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "warehouse cost per square meter exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_data_exchange_pct_03(record):
    """Evaluate supplier data exchange compliance for control WP-0030-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_exchange_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-03", "metric": "supplier_data_exchange_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-03", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-03", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-03", "metric": "supplier_data_exchange_pct", "label": "supplier data exchange compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier data exchange compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_backup_age_hours_04(record):
    """Evaluate supplier backup age for control WP-0030-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-04", "metric": "supplier_backup_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-04", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-04", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-04", "metric": "supplier_backup_age_hours", "label": "supplier backup age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier backup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_safety_stock_days_05(record):
    """Evaluate supplier safety stock cover for control WP-0030-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-05", "metric": "supplier_safety_stock_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-05", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-05", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-05", "metric": "supplier_safety_stock_days", "label": "supplier safety stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier safety stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_cloud_region_gap_count_06(record):
    """Evaluate supplier cloud-region gaps for control WP-0030-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cloud_region_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-06", "metric": "supplier_cloud_region_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-06", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-06", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-06", "metric": "supplier_cloud_region_gap_count", "label": "supplier cloud-region gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier cloud-region gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_transport_alternative_count_07(record):
    """Evaluate supplier transport alternatives for control WP-0030-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transport_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-07", "metric": "supplier_transport_alternative_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "routes",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-07", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-07", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-07", "metric": "supplier_transport_alternative_count", "label": "supplier transport alternatives",
        "status": "breach", "severity": "low", "unit": "routes",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier transport alternatives falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_adaptation_score_08(record):
    """Evaluate supplier climate adaptation for control WP-0030-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adaptation_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-08", "metric": "supplier_adaptation_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-08", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-08", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-08", "metric": "supplier_adaptation_score", "label": "supplier climate adaptation",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier climate adaptation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_crisis_drill_age_days_09(record):
    """Evaluate supplier crisis drill age for control WP-0030-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-09", "metric": "supplier_crisis_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-09", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-09", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-09", "metric": "supplier_crisis_drill_age_days", "label": "supplier crisis drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier crisis drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_audit_finding_age_days_10(record):
    """Evaluate supplier audit-finding age for control WP-0030-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_finding_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-10", "metric": "supplier_audit_finding_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-10", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-10", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-10", "metric": "supplier_audit_finding_age_days", "label": "supplier audit-finding age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier audit-finding age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_diversity_score_11(record):
    """Evaluate supplier diversity score for control WP-0030-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_diversity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-11", "metric": "supplier_diversity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-11", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-11", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-11", "metric": "supplier_diversity_score", "label": "supplier diversity score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "supplier diversity score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_disaster_exposure_score_12(record):
    """Evaluate supplier disaster exposure for control WP-0030-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disaster_exposure_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-12", "metric": "supplier_disaster_exposure_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-12", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-12", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-12", "metric": "supplier_disaster_exposure_score", "label": "supplier disaster exposure",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disaster exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_quality_improvement_pct_13(record):
    """Evaluate supplier quality improvement for control WP-0030-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-13", "metric": "supplier_quality_improvement_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-13", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-13", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-13", "metric": "supplier_quality_improvement_pct", "label": "supplier quality improvement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier quality improvement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_embedding_index_age_hours_14(record):
    """Evaluate supplier embedding index age for control WP-0030-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_embedding_index_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-14", "metric": "supplier_embedding_index_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-14", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-14", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-14", "metric": "supplier_embedding_index_age_hours", "label": "supplier embedding index age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "supplier embedding index age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_throughput_variance_pct_15(record):
    """Evaluate supplier throughput variance for control WP-0030-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_throughput_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-15", "metric": "supplier_throughput_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-15", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-15", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-15", "metric": "supplier_throughput_variance_pct", "label": "supplier throughput variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier throughput variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_license_review_age_days_16(record):
    """Evaluate supplier license review age for control WP-0030-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-16", "metric": "supplier_license_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-16", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-16", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-16", "metric": "supplier_license_review_age_days", "label": "supplier license review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier license review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_regulator_request_age_days_17(record):
    """Evaluate supplier regulator request age for control WP-0030-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-17", "metric": "supplier_regulator_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-17", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-17", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-17", "metric": "supplier_regulator_request_age_days", "label": "supplier regulator request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier regulator request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_maverick_buy_pct_18(record):
    """Evaluate supplier maverick buying for control WP-0030-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_maverick_buy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-18", "metric": "supplier_maverick_buy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-18", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-18", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-18", "metric": "supplier_maverick_buy_pct", "label": "supplier maverick buying",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "supplier maverick buying exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_rework_pct_19(record):
    """Evaluate supplier rework rate for control WP-0030-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rework_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-19", "metric": "supplier_rework_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-19", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-19", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-19", "metric": "supplier_rework_pct", "label": "supplier rework rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "supplier rework rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_business_review_age_days_20(record):
    """Evaluate business review age for control WP-0030-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-20", "metric": "supplier_business_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-20", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-20", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-20", "metric": "supplier_business_review_age_days", "label": "business review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "business review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_contract_termination_age_days_21(record):
    """Evaluate supplier contract termination age for control WP-0030-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contract_termination_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-21", "metric": "supplier_contract_termination_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-21", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-21", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-21", "metric": "supplier_contract_termination_age_days", "label": "supplier contract termination age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contract termination age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_fill_rate_pct_22(record):
    """Evaluate order fill rate for control WP-0030-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-22", "metric": "fill_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-22", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-22", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-22", "metric": "fill_rate_pct", "label": "order fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "order fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_defect_count_23(record):
    """Evaluate supplier defects for control WP-0030-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_defect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-23", "metric": "supplier_defect_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-23", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-23", "metric": "supplier_defect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-23", "metric": "supplier_defect_count", "label": "supplier defects",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "supplier defects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_dock_to_stock_minutes_24(record):
    """Evaluate dock-to-stock time for control WP-0030-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_to_stock_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0030-24", "metric": "dock_to_stock_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0030-24", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0030-24", "metric": "dock_to_stock_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0030-24", "metric": "dock_to_stock_minutes", "label": "dock-to-stock time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dock-to-stock time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_intermodal_transfer_delay_hours_01, assess_warehouse_cost_per_sq_m_02, assess_supplier_data_exchange_pct_03, assess_supplier_backup_age_hours_04, assess_supplier_safety_stock_days_05, assess_supplier_cloud_region_gap_count_06, assess_supplier_transport_alternative_count_07, assess_supplier_adaptation_score_08, assess_supplier_crisis_drill_age_days_09, assess_supplier_audit_finding_age_days_10, assess_supplier_diversity_score_11, assess_supplier_disaster_exposure_score_12, assess_supplier_quality_improvement_pct_13, assess_supplier_embedding_index_age_hours_14, assess_supplier_throughput_variance_pct_15, assess_supplier_license_review_age_days_16, assess_supplier_regulator_request_age_days_17, assess_supplier_maverick_buy_pct_18, assess_supplier_rework_pct_19, assess_supplier_business_review_age_days_20, assess_supplier_contract_termination_age_days_21, assess_fill_rate_pct_22, assess_supplier_defect_count_23, assess_dock_to_stock_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

