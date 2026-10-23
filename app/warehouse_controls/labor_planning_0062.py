"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_preferred_status_review_age_days_01(record):
    """Evaluate preferred status review age for control WP-0062-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-01", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-01", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-01", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-01", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "preferred status review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_post_exit_data_transfer_count_02(record):
    """Evaluate post-exit data transfers for control WP-0062-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-02", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-02", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-02", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-02", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "post-exit data transfers exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_lot_age_days_03(record):
    """Evaluate lot age for control WP-0062-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-03", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-03", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-03", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-03", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "lot age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_cold_chain_excursion_minutes_04(record):
    """Evaluate cold-chain excursion for control WP-0062-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-04", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-04", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-04", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-04", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold-chain excursion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_smoke_alarm_signal_05(record):
    """Evaluate smoke alarm signal for control WP-0062-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-05", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-05", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-05", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-05", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "smoke alarm signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_label_reprint_count_06(record):
    """Evaluate label reprints for control WP-0062-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_reprint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-06", "metric": "label_reprint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-06", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-06", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-06", "metric": "label_reprint_count", "label": "label reprints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "label reprints exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_putaway_accuracy_pct_07(record):
    """Evaluate putaway accuracy for control WP-0062-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-07", "metric": "putaway_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-07", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-07", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-07", "metric": "putaway_accuracy_pct", "label": "putaway accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "putaway accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_dead_letter_count_08(record):
    """Evaluate dead-letter messages for control WP-0062-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_letter_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-08", "metric": "dead_letter_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "messages",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-08", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-08", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-08", "metric": "dead_letter_count", "label": "dead-letter messages",
        "status": "breach", "severity": "medium", "unit": "messages",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dead-letter messages must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_each_pick_ratio_pct_09(record):
    """Evaluate each pick ratio for control WP-0062-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("each_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-09", "metric": "each_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-09", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-09", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-09", "metric": "each_pick_ratio_pct", "label": "each pick ratio",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "each pick ratio must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_camera_coverage_pct_10(record):
    """Evaluate camera coverage for control WP-0062-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-10", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-10", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-10", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-10", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "camera coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_energy_peak_kw_11(record):
    """Evaluate peak power demand for control WP-0062-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-11", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "low", "unit": "kW",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-11", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-11", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-11", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "low", "unit": "kW",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "peak power demand falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_insurance_coverage_pct_12(record):
    """Evaluate insurance coverage for control WP-0062-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-12", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-12", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-12", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-12", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insurance coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_permit_to_work_gap_count_13(record):
    """Evaluate permit-to-work gaps for control WP-0062-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("permit_to_work_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-13", "metric": "permit_to_work_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-13", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-13", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-13", "metric": "permit_to_work_gap_count", "label": "permit-to-work gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "permit-to-work gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_unplanned_downtime_pct_14(record):
    """Evaluate unplanned downtime for control WP-0062-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unplanned_downtime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-14", "metric": "unplanned_downtime_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-14", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-14", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-14", "metric": "unplanned_downtime_pct", "label": "unplanned downtime",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "unplanned downtime exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_maintenance_window_overrun_minutes_15(record):
    """Evaluate maintenance window overrun for control WP-0062-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_window_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-15", "metric": "maintenance_window_overrun_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-15", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-15", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-15", "metric": "maintenance_window_overrun_minutes", "label": "maintenance window overrun",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "maintenance window overrun falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_referential_integrity_pct_16(record):
    """Evaluate referential integrity for control WP-0062-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("referential_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-16", "metric": "referential_integrity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-16", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-16", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-16", "metric": "referential_integrity_pct", "label": "referential integrity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "referential integrity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_route_master_gap_count_17(record):
    """Evaluate route master gaps for control WP-0062-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-17", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-17", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-17", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-17", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_purchase_order_change_count_18(record):
    """Evaluate purchase order changes for control WP-0062-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-18", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-18", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-18", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-18", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "purchase order changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_delivery_geofence_miss_count_19(record):
    """Evaluate delivery geofence misses for control WP-0062-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-19", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-19", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-19", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-19", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "delivery geofence misses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_fuel_surcharge_variance_pct_20(record):
    """Evaluate fuel surcharge variance for control WP-0062-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-20", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-20", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-20", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-20", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fuel surcharge variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_highway_restriction_match_count_21(record):
    """Evaluate highway restriction matches for control WP-0062-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-21", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-21", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-21", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-21", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "highway restriction matches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_recovery_plan_age_days_22(record):
    """Evaluate supplier recovery plan age for control WP-0062-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-22", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-22", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-22", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-22", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier recovery plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_energy_intensity_23(record):
    """Evaluate supplier energy intensity for control WP-0062-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-23", "metric": "supplier_energy_intensity",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-23", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-23", "metric": "supplier_energy_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-23", "metric": "supplier_energy_intensity", "label": "supplier energy intensity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier energy intensity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_route_risk_score_24(record):
    """Evaluate supplier route risk for control WP-0062-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0062-24", "metric": "supplier_route_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0062-24", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0062-24", "metric": "supplier_route_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0062-24", "metric": "supplier_route_risk_score", "label": "supplier route risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier route risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
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

