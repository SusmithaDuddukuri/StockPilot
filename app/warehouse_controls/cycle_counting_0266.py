"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_camera_coverage_pct_01(record):
    """Evaluate camera coverage for control WP-0266-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-01", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-01", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-01", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-01", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "camera coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_energy_peak_kw_02(record):
    """Evaluate peak power demand for control WP-0266-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-02", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kW",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-02", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-02", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-02", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "critical", "unit": "kW",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "peak power demand exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_insurance_coverage_pct_03(record):
    """Evaluate insurance coverage for control WP-0266-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-03", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-03", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-03", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-03", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "insurance coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_permit_to_work_gap_count_04(record):
    """Evaluate permit-to-work gaps for control WP-0266-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("permit_to_work_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-04", "metric": "permit_to_work_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-04", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-04", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-04", "metric": "permit_to_work_gap_count", "label": "permit-to-work gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "permit-to-work gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_unplanned_downtime_pct_05(record):
    """Evaluate unplanned downtime for control WP-0266-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unplanned_downtime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-05", "metric": "unplanned_downtime_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-05", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-05", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-05", "metric": "unplanned_downtime_pct", "label": "unplanned downtime",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unplanned downtime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_maintenance_window_overrun_minutes_06(record):
    """Evaluate maintenance window overrun for control WP-0266-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_window_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-06", "metric": "maintenance_window_overrun_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-06", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-06", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-06", "metric": "maintenance_window_overrun_minutes", "label": "maintenance window overrun",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "maintenance window overrun exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_referential_integrity_pct_07(record):
    """Evaluate referential integrity for control WP-0266-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("referential_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-07", "metric": "referential_integrity_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-07", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-07", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-07", "metric": "referential_integrity_pct", "label": "referential integrity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "referential integrity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_route_master_gap_count_08(record):
    """Evaluate route master gaps for control WP-0266-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-08", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-08", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-08", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-08", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "route master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_purchase_order_change_count_09(record):
    """Evaluate purchase order changes for control WP-0266-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-09", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-09", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-09", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-09", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "purchase order changes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_delivery_geofence_miss_count_10(record):
    """Evaluate delivery geofence misses for control WP-0266-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-10", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-10", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-10", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-10", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "delivery geofence misses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_fuel_surcharge_variance_pct_11(record):
    """Evaluate fuel surcharge variance for control WP-0266-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-11", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-11", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-11", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-11", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "fuel surcharge variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_highway_restriction_match_count_12(record):
    """Evaluate highway restriction matches for control WP-0266-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-12", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-12", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-12", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-12", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "highway restriction matches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_recovery_plan_age_days_13(record):
    """Evaluate supplier recovery plan age for control WP-0266-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-13", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-13", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-13", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-13", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery plan age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_energy_intensity_14(record):
    """Evaluate supplier energy intensity for control WP-0266-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-14", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-14", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-14", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-14", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier energy intensity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_route_risk_score_15(record):
    """Evaluate supplier route risk for control WP-0266-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-15", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-15", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-15", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-15", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier route risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_training_record_pct_16(record):
    """Evaluate supplier training-record completeness for control WP-0266-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-16", "metric": "supplier_training_record_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-16", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-16", "metric": "supplier_training_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-16", "metric": "supplier_training_record_pct", "label": "supplier training-record completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training-record completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_payment_delay_days_17(record):
    """Evaluate supplier payment delay for control WP-0266-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-17", "metric": "supplier_payment_delay_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-17", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-17", "metric": "supplier_payment_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-17", "metric": "supplier_payment_delay_days", "label": "supplier payment delay",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_takeback_compliance_pct_18(record):
    """Evaluate supplier take-back compliance for control WP-0266-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_takeback_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-18", "metric": "supplier_takeback_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-18", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-18", "metric": "supplier_takeback_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-18", "metric": "supplier_takeback_compliance_pct", "label": "supplier take-back compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier take-back compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_inventory_visibility_pct_19(record):
    """Evaluate supplier inventory visibility for control WP-0266-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-19", "metric": "supplier_inventory_visibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-19", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-19", "metric": "supplier_inventory_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-19", "metric": "supplier_inventory_visibility_pct", "label": "supplier inventory visibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier inventory visibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_capability_study_age_days_20(record):
    """Evaluate supplier capability-study age for control WP-0266-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_study_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-20", "metric": "supplier_capability_study_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-20", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-20", "metric": "supplier_capability_study_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-20", "metric": "supplier_capability_study_age_days", "label": "supplier capability-study age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capability-study age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_worker_grievance_age_days_21(record):
    """Evaluate supplier worker grievance age for control WP-0266-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_grievance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-21", "metric": "supplier_worker_grievance_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-21", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-21", "metric": "supplier_worker_grievance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-21", "metric": "supplier_worker_grievance_age_days", "label": "supplier worker grievance age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier worker grievance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_credit_rating_score_22(record):
    """Evaluate supplier credit rating for control WP-0266-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_rating_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-22", "metric": "supplier_credit_rating_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-22", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-22", "metric": "supplier_credit_rating_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-22", "metric": "supplier_credit_rating_score", "label": "supplier credit rating",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier credit rating exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_internal_audit_age_days_23(record):
    """Evaluate supplier internal audit age for control WP-0266-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_internal_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-23", "metric": "supplier_internal_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-23", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-23", "metric": "supplier_internal_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-23", "metric": "supplier_internal_audit_age_days", "label": "supplier internal audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier internal audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_prompt_injection_test_age_days_24(record):
    """Evaluate supplier prompt-injection test age for control WP-0266-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prompt_injection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0266-24", "metric": "supplier_prompt_injection_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0266-24", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0266-24", "metric": "supplier_prompt_injection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0266-24", "metric": "supplier_prompt_injection_test_age_days", "label": "supplier prompt-injection test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier prompt-injection test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_camera_coverage_pct_01, assess_energy_peak_kw_02, assess_insurance_coverage_pct_03, assess_permit_to_work_gap_count_04, assess_unplanned_downtime_pct_05, assess_maintenance_window_overrun_minutes_06, assess_referential_integrity_pct_07, assess_route_master_gap_count_08, assess_purchase_order_change_count_09, assess_delivery_geofence_miss_count_10, assess_fuel_surcharge_variance_pct_11, assess_highway_restriction_match_count_12, assess_supplier_recovery_plan_age_days_13, assess_supplier_energy_intensity_14, assess_supplier_route_risk_score_15, assess_supplier_training_record_pct_16, assess_supplier_payment_delay_days_17, assess_supplier_takeback_compliance_pct_18, assess_supplier_inventory_visibility_pct_19, assess_supplier_capability_study_age_days_20, assess_supplier_worker_grievance_age_days_21, assess_supplier_credit_rating_score_22, assess_supplier_internal_audit_age_days_23, assess_supplier_prompt_injection_test_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

