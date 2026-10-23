"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_preferred_status_review_age_days_01(record):
    """Evaluate preferred status review age for control WP-0441-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-01", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-01", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-01", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-01", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "preferred status review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_post_exit_data_transfer_count_02(record):
    """Evaluate post-exit data transfers for control WP-0441-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-02", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-02", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-02", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-02", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "post-exit data transfers falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_lot_age_days_03(record):
    """Evaluate lot age for control WP-0441-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-03", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-03", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-03", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-03", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lot age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_cold_chain_excursion_minutes_04(record):
    """Evaluate cold-chain excursion for control WP-0441-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-04", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-04", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-04", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-04", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cold-chain excursion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_smoke_alarm_signal_05(record):
    """Evaluate smoke alarm signal for control WP-0441-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-05", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-05", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-05", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-05", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "smoke alarm signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_label_reprint_count_06(record):
    """Evaluate label reprints for control WP-0441-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_reprint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-06", "metric": "label_reprint_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-06", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-06", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-06", "metric": "label_reprint_count", "label": "label reprints",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "label reprints falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_putaway_accuracy_pct_07(record):
    """Evaluate putaway accuracy for control WP-0441-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-07", "metric": "putaway_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-07", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-07", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-07", "metric": "putaway_accuracy_pct", "label": "putaway accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_dead_letter_count_08(record):
    """Evaluate dead-letter messages for control WP-0441-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_letter_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-08", "metric": "dead_letter_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "messages",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-08", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-08", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-08", "metric": "dead_letter_count", "label": "dead-letter messages",
        "status": "breach", "severity": "low", "unit": "messages",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dead-letter messages must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_each_pick_ratio_pct_09(record):
    """Evaluate each pick ratio for control WP-0441-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("each_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-09", "metric": "each_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-09", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-09", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-09", "metric": "each_pick_ratio_pct", "label": "each pick ratio",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "each pick ratio exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_camera_coverage_pct_10(record):
    """Evaluate camera coverage for control WP-0441-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-10", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-10", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-10", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-10", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "camera coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_energy_peak_kw_11(record):
    """Evaluate peak power demand for control WP-0441-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-11", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kW",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-11", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-11", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-11", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "critical", "unit": "kW",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "peak power demand must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_insurance_coverage_pct_12(record):
    """Evaluate insurance coverage for control WP-0441-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-12", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-12", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-12", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-12", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insurance coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_permit_to_work_gap_count_13(record):
    """Evaluate permit-to-work gaps for control WP-0441-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("permit_to_work_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-13", "metric": "permit_to_work_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-13", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-13", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-13", "metric": "permit_to_work_gap_count", "label": "permit-to-work gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "permit-to-work gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_unplanned_downtime_pct_14(record):
    """Evaluate unplanned downtime for control WP-0441-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unplanned_downtime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-14", "metric": "unplanned_downtime_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-14", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-14", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-14", "metric": "unplanned_downtime_pct", "label": "unplanned downtime",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "unplanned downtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_maintenance_window_overrun_minutes_15(record):
    """Evaluate maintenance window overrun for control WP-0441-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_window_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-15", "metric": "maintenance_window_overrun_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-15", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-15", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-15", "metric": "maintenance_window_overrun_minutes", "label": "maintenance window overrun",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "maintenance window overrun must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_referential_integrity_pct_16(record):
    """Evaluate referential integrity for control WP-0441-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("referential_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-16", "metric": "referential_integrity_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-16", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-16", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-16", "metric": "referential_integrity_pct", "label": "referential integrity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "referential integrity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_route_master_gap_count_17(record):
    """Evaluate route master gaps for control WP-0441-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-17", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-17", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-17", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-17", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "route master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_purchase_order_change_count_18(record):
    """Evaluate purchase order changes for control WP-0441-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-18", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-18", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-18", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-18", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "purchase order changes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_delivery_geofence_miss_count_19(record):
    """Evaluate delivery geofence misses for control WP-0441-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-19", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-19", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-19", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-19", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery geofence misses must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_fuel_surcharge_variance_pct_20(record):
    """Evaluate fuel surcharge variance for control WP-0441-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-20", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-20", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-20", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-20", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fuel surcharge variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_highway_restriction_match_count_21(record):
    """Evaluate highway restriction matches for control WP-0441-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-21", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-21", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-21", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-21", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "highway restriction matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_recovery_plan_age_days_22(record):
    """Evaluate supplier recovery plan age for control WP-0441-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-22", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-22", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-22", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-22", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "supplier recovery plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_energy_intensity_23(record):
    """Evaluate supplier energy intensity for control WP-0441-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-23", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-23", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-23", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-23", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy intensity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_route_risk_score_24(record):
    """Evaluate supplier route risk for control WP-0441-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0441-24", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0441-24", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0441-24", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0441-24", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier route risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_supplier_preferred_status_review_age_days_01, assess_supplier_post_exit_data_transfer_count_02, assess_lot_age_days_03, assess_cold_chain_excursion_minutes_04, assess_smoke_alarm_signal_05, assess_label_reprint_count_06, assess_putaway_accuracy_pct_07, assess_dead_letter_count_08, assess_each_pick_ratio_pct_09, assess_camera_coverage_pct_10, assess_energy_peak_kw_11, assess_insurance_coverage_pct_12, assess_permit_to_work_gap_count_13, assess_unplanned_downtime_pct_14, assess_maintenance_window_overrun_minutes_15, assess_referential_integrity_pct_16, assess_route_master_gap_count_17, assess_purchase_order_change_count_18, assess_delivery_geofence_miss_count_19, assess_fuel_surcharge_variance_pct_20, assess_highway_restriction_match_count_21, assess_supplier_recovery_plan_age_days_22, assess_supplier_energy_intensity_23, assess_supplier_route_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

