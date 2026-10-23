"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_dead_letter_count_01(record):
    """Evaluate dead-letter messages for control WP-0453-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_letter_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-01", "metric": "dead_letter_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "messages",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-01", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-01", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-01", "metric": "dead_letter_count", "label": "dead-letter messages",
        "status": "breach", "severity": "medium", "unit": "messages",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "dead-letter messages exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_each_pick_ratio_pct_02(record):
    """Evaluate each pick ratio for control WP-0453-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("each_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-02", "metric": "each_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-02", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-02", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-02", "metric": "each_pick_ratio_pct", "label": "each pick ratio",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "each pick ratio falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_camera_coverage_pct_03(record):
    """Evaluate camera coverage for control WP-0453-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-03", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-03", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-03", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-03", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "camera coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_energy_peak_kw_04(record):
    """Evaluate peak power demand for control WP-0453-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-04", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "low", "unit": "kW",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-04", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-04", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-04", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "low", "unit": "kW",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "peak power demand must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_insurance_coverage_pct_05(record):
    """Evaluate insurance coverage for control WP-0453-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-05", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-05", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-05", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-05", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "insurance coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_permit_to_work_gap_count_06(record):
    """Evaluate permit-to-work gaps for control WP-0453-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("permit_to_work_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-06", "metric": "permit_to_work_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-06", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-06", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-06", "metric": "permit_to_work_gap_count", "label": "permit-to-work gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "permit-to-work gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_unplanned_downtime_pct_07(record):
    """Evaluate unplanned downtime for control WP-0453-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unplanned_downtime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-07", "metric": "unplanned_downtime_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-07", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-07", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-07", "metric": "unplanned_downtime_pct", "label": "unplanned downtime",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "unplanned downtime must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_maintenance_window_overrun_minutes_08(record):
    """Evaluate maintenance window overrun for control WP-0453-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_window_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-08", "metric": "maintenance_window_overrun_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-08", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-08", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-08", "metric": "maintenance_window_overrun_minutes", "label": "maintenance window overrun",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "maintenance window overrun must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_referential_integrity_pct_09(record):
    """Evaluate referential integrity for control WP-0453-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("referential_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-09", "metric": "referential_integrity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-09", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-09", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-09", "metric": "referential_integrity_pct", "label": "referential integrity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "referential integrity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_route_master_gap_count_10(record):
    """Evaluate route master gaps for control WP-0453-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-10", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-10", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-10", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-10", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "route master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_purchase_order_change_count_11(record):
    """Evaluate purchase order changes for control WP-0453-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-11", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-11", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-11", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-11", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "purchase order changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_delivery_geofence_miss_count_12(record):
    """Evaluate delivery geofence misses for control WP-0453-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-12", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-12", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-12", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-12", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "delivery geofence misses must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_fuel_surcharge_variance_pct_13(record):
    """Evaluate fuel surcharge variance for control WP-0453-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-13", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-13", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-13", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-13", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "fuel surcharge variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_highway_restriction_match_count_14(record):
    """Evaluate highway restriction matches for control WP-0453-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-14", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-14", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-14", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-14", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "highway restriction matches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_recovery_plan_age_days_15(record):
    """Evaluate supplier recovery plan age for control WP-0453-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-15", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-15", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-15", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-15", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery plan age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_energy_intensity_16(record):
    """Evaluate supplier energy intensity for control WP-0453-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-16", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-16", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-16", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-16", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier energy intensity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_route_risk_score_17(record):
    """Evaluate supplier route risk for control WP-0453-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-17", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-17", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-17", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-17", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier route risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_training_record_pct_18(record):
    """Evaluate supplier training-record completeness for control WP-0453-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-18", "metric": "supplier_training_record_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-18", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-18", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-18", "metric": "supplier_training_record_pct", "label": "supplier training-record completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier training-record completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_payment_delay_days_19(record):
    """Evaluate supplier payment delay for control WP-0453-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-19", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-19", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-19", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-19", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_takeback_compliance_pct_20(record):
    """Evaluate supplier take-back compliance for control WP-0453-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-20", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-20", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-20", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-20", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier take-back compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_inventory_visibility_pct_21(record):
    """Evaluate supplier inventory visibility for control WP-0453-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-21", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-21", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-21", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-21", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "supplier inventory visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_capability_study_age_days_22(record):
    """Evaluate supplier capability-study age for control WP-0453-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-22", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-22", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-22", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-22", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier capability-study age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_worker_grievance_age_days_23(record):
    """Evaluate supplier worker grievance age for control WP-0453-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-23", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-23", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-23", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-23", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier worker grievance age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_credit_rating_score_24(record):
    """Evaluate supplier credit rating for control WP-0453-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0453-24", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0453-24", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0453-24", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0453-24", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit rating must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_dead_letter_count_01, assess_each_pick_ratio_pct_02, assess_camera_coverage_pct_03, assess_energy_peak_kw_04, assess_insurance_coverage_pct_05, assess_permit_to_work_gap_count_06, assess_unplanned_downtime_pct_07, assess_maintenance_window_overrun_minutes_08, assess_referential_integrity_pct_09, assess_route_master_gap_count_10, assess_purchase_order_change_count_11, assess_delivery_geofence_miss_count_12, assess_fuel_surcharge_variance_pct_13, assess_highway_restriction_match_count_14, assess_supplier_recovery_plan_age_days_15, assess_supplier_energy_intensity_16, assess_supplier_route_risk_score_17, assess_supplier_training_record_pct_18, assess_supplier_payment_delay_days_19, assess_supplier_takeback_compliance_pct_20, assess_supplier_inventory_visibility_pct_21, assess_supplier_capability_study_age_days_22, assess_supplier_worker_grievance_age_days_23, assess_supplier_credit_rating_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

