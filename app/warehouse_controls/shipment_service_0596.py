"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_inspection_cycle_minutes_01(record):
    """Evaluate inspection cycle time for control WP-0596-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_cycle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-01", "metric": "inspection_cycle_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-01", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-01", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-01", "metric": "inspection_cycle_minutes", "label": "inspection cycle time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "inspection cycle time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_order_amendment_count_02(record):
    """Evaluate order amendments for control WP-0596-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_amendment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-02", "metric": "order_amendment_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-02", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-02", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-02", "metric": "order_amendment_count", "label": "order amendments",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order amendments must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_intermodal_transfer_delay_hours_03(record):
    """Evaluate intermodal transfer delay for control WP-0596-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("intermodal_transfer_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-03", "metric": "intermodal_transfer_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-03", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-03", "metric": "intermodal_transfer_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-03", "metric": "intermodal_transfer_delay_hours", "label": "intermodal transfer delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "intermodal transfer delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_warehouse_cost_per_sq_m_04(record):
    """Evaluate warehouse cost per square meter for control WP-0596-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warehouse_cost_per_sq_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-04", "metric": "warehouse_cost_per_sq_m",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-04", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-04", "metric": "warehouse_cost_per_sq_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-04", "metric": "warehouse_cost_per_sq_m", "label": "warehouse cost per square meter",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "warehouse cost per square meter exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_data_exchange_pct_05(record):
    """Evaluate supplier data exchange compliance for control WP-0596-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_exchange_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-05", "metric": "supplier_data_exchange_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-05", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-05", "metric": "supplier_data_exchange_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-05", "metric": "supplier_data_exchange_pct", "label": "supplier data exchange compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier data exchange compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_backup_age_hours_06(record):
    """Evaluate supplier backup age for control WP-0596-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-06", "metric": "supplier_backup_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-06", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-06", "metric": "supplier_backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-06", "metric": "supplier_backup_age_hours", "label": "supplier backup age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier backup age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_safety_stock_days_07(record):
    """Evaluate supplier safety stock cover for control WP-0596-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-07", "metric": "supplier_safety_stock_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-07", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-07", "metric": "supplier_safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-07", "metric": "supplier_safety_stock_days", "label": "supplier safety stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier safety stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_cloud_region_gap_count_08(record):
    """Evaluate supplier cloud-region gaps for control WP-0596-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cloud_region_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-08", "metric": "supplier_cloud_region_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-08", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-08", "metric": "supplier_cloud_region_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-08", "metric": "supplier_cloud_region_gap_count", "label": "supplier cloud-region gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier cloud-region gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_transport_alternative_count_09(record):
    """Evaluate supplier transport alternatives for control WP-0596-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transport_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-09", "metric": "supplier_transport_alternative_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "routes",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-09", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-09", "metric": "supplier_transport_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-09", "metric": "supplier_transport_alternative_count", "label": "supplier transport alternatives",
        "status": "breach", "severity": "low", "unit": "routes",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier transport alternatives falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_adaptation_score_10(record):
    """Evaluate supplier climate adaptation for control WP-0596-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_adaptation_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-10", "metric": "supplier_adaptation_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-10", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-10", "metric": "supplier_adaptation_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-10", "metric": "supplier_adaptation_score", "label": "supplier climate adaptation",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier climate adaptation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_crisis_drill_age_days_11(record):
    """Evaluate supplier crisis drill age for control WP-0596-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-11", "metric": "supplier_crisis_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-11", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-11", "metric": "supplier_crisis_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-11", "metric": "supplier_crisis_drill_age_days", "label": "supplier crisis drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier crisis drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_audit_finding_age_days_12(record):
    """Evaluate supplier audit-finding age for control WP-0596-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_finding_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-12", "metric": "supplier_audit_finding_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-12", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-12", "metric": "supplier_audit_finding_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-12", "metric": "supplier_audit_finding_age_days", "label": "supplier audit-finding age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier audit-finding age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_diversity_score_13(record):
    """Evaluate supplier diversity score for control WP-0596-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_diversity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-13", "metric": "supplier_diversity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-13", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-13", "metric": "supplier_diversity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-13", "metric": "supplier_diversity_score", "label": "supplier diversity score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier diversity score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_disaster_exposure_score_14(record):
    """Evaluate supplier disaster exposure for control WP-0596-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disaster_exposure_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-14", "metric": "supplier_disaster_exposure_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-14", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-14", "metric": "supplier_disaster_exposure_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-14", "metric": "supplier_disaster_exposure_score", "label": "supplier disaster exposure",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disaster exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_quality_improvement_pct_15(record):
    """Evaluate supplier quality improvement for control WP-0596-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_quality_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-15", "metric": "supplier_quality_improvement_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-15", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-15", "metric": "supplier_quality_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-15", "metric": "supplier_quality_improvement_pct", "label": "supplier quality improvement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier quality improvement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_embedding_index_age_hours_16(record):
    """Evaluate supplier embedding index age for control WP-0596-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_embedding_index_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-16", "metric": "supplier_embedding_index_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-16", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-16", "metric": "supplier_embedding_index_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-16", "metric": "supplier_embedding_index_age_hours", "label": "supplier embedding index age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier embedding index age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_throughput_variance_pct_17(record):
    """Evaluate supplier throughput variance for control WP-0596-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_throughput_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-17", "metric": "supplier_throughput_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-17", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-17", "metric": "supplier_throughput_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-17", "metric": "supplier_throughput_variance_pct", "label": "supplier throughput variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier throughput variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_license_review_age_days_18(record):
    """Evaluate supplier license review age for control WP-0596-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-18", "metric": "supplier_license_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-18", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-18", "metric": "supplier_license_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-18", "metric": "supplier_license_review_age_days", "label": "supplier license review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier license review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_regulator_request_age_days_19(record):
    """Evaluate supplier regulator request age for control WP-0596-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_regulator_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-19", "metric": "supplier_regulator_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-19", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-19", "metric": "supplier_regulator_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-19", "metric": "supplier_regulator_request_age_days", "label": "supplier regulator request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier regulator request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_maverick_buy_pct_20(record):
    """Evaluate supplier maverick buying for control WP-0596-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_maverick_buy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-20", "metric": "supplier_maverick_buy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-20", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-20", "metric": "supplier_maverick_buy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-20", "metric": "supplier_maverick_buy_pct", "label": "supplier maverick buying",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier maverick buying exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_rework_pct_21(record):
    """Evaluate supplier rework rate for control WP-0596-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rework_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-21", "metric": "supplier_rework_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-21", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-21", "metric": "supplier_rework_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-21", "metric": "supplier_rework_pct", "label": "supplier rework rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier rework rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_business_review_age_days_22(record):
    """Evaluate business review age for control WP-0596-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-22", "metric": "supplier_business_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-22", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-22", "metric": "supplier_business_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-22", "metric": "supplier_business_review_age_days", "label": "business review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "business review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_contract_termination_age_days_23(record):
    """Evaluate supplier contract termination age for control WP-0596-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contract_termination_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-23", "metric": "supplier_contract_termination_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-23", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-23", "metric": "supplier_contract_termination_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-23", "metric": "supplier_contract_termination_age_days", "label": "supplier contract termination age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contract termination age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_fill_rate_pct_24(record):
    """Evaluate order fill rate for control WP-0596-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0596-24", "metric": "fill_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0596-24", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0596-24", "metric": "fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0596-24", "metric": "fill_rate_pct", "label": "order fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "order fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_inspection_cycle_minutes_01, assess_order_amendment_count_02, assess_intermodal_transfer_delay_hours_03, assess_warehouse_cost_per_sq_m_04, assess_supplier_data_exchange_pct_05, assess_supplier_backup_age_hours_06, assess_supplier_safety_stock_days_07, assess_supplier_cloud_region_gap_count_08, assess_supplier_transport_alternative_count_09, assess_supplier_adaptation_score_10, assess_supplier_crisis_drill_age_days_11, assess_supplier_audit_finding_age_days_12, assess_supplier_diversity_score_13, assess_supplier_disaster_exposure_score_14, assess_supplier_quality_improvement_pct_15, assess_supplier_embedding_index_age_hours_16, assess_supplier_throughput_variance_pct_17, assess_supplier_license_review_age_days_18, assess_supplier_regulator_request_age_days_19, assess_supplier_maverick_buy_pct_20, assess_supplier_rework_pct_21, assess_supplier_business_review_age_days_22, assess_supplier_contract_termination_age_days_23, assess_fill_rate_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

