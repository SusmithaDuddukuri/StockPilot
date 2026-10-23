"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_tax_rate_variance_pct_01(record):
    """Evaluate supplier tax-rate variance for control WP-0628-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-01", "metric": "supplier_tax_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-01", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-01", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-01", "metric": "supplier_tax_rate_variance_pct", "label": "supplier tax-rate variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier tax-rate variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_queue_time_hours_02(record):
    """Evaluate supplier queue time for control WP-0628-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_queue_time_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-02", "metric": "supplier_queue_time_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-02", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-02", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-02", "metric": "supplier_queue_time_hours", "label": "supplier queue time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier queue time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_preferred_status_review_age_days_03(record):
    """Evaluate preferred status review age for control WP-0628-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-03", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-03", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-03", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-03", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "preferred status review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_post_exit_data_transfer_count_04(record):
    """Evaluate post-exit data transfers for control WP-0628-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-04", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-04", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-04", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-04", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "post-exit data transfers exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_lot_age_days_05(record):
    """Evaluate lot age for control WP-0628-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-05", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-05", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-05", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-05", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "lot age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_cold_chain_excursion_minutes_06(record):
    """Evaluate cold-chain excursion for control WP-0628-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-06", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-06", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-06", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-06", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold-chain excursion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_smoke_alarm_signal_07(record):
    """Evaluate smoke alarm signal for control WP-0628-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-07", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-07", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-07", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-07", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "smoke alarm signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_label_reprint_count_08(record):
    """Evaluate label reprints for control WP-0628-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_reprint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-08", "metric": "label_reprint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-08", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-08", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-08", "metric": "label_reprint_count", "label": "label reprints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "label reprints exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_putaway_accuracy_pct_09(record):
    """Evaluate putaway accuracy for control WP-0628-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-09", "metric": "putaway_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-09", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-09", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-09", "metric": "putaway_accuracy_pct", "label": "putaway accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "putaway accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_dead_letter_count_10(record):
    """Evaluate dead-letter messages for control WP-0628-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_letter_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-10", "metric": "dead_letter_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "messages",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-10", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-10", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-10", "metric": "dead_letter_count", "label": "dead-letter messages",
        "status": "breach", "severity": "medium", "unit": "messages",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dead-letter messages must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_each_pick_ratio_pct_11(record):
    """Evaluate each pick ratio for control WP-0628-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("each_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-11", "metric": "each_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-11", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-11", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-11", "metric": "each_pick_ratio_pct", "label": "each pick ratio",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "each pick ratio must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_camera_coverage_pct_12(record):
    """Evaluate camera coverage for control WP-0628-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-12", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-12", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-12", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-12", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "camera coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_energy_peak_kw_13(record):
    """Evaluate peak power demand for control WP-0628-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-13", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "low", "unit": "kW",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-13", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-13", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-13", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "low", "unit": "kW",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "peak power demand falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_insurance_coverage_pct_14(record):
    """Evaluate insurance coverage for control WP-0628-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-14", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-14", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-14", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-14", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insurance coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_permit_to_work_gap_count_15(record):
    """Evaluate permit-to-work gaps for control WP-0628-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("permit_to_work_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-15", "metric": "permit_to_work_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-15", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-15", "metric": "permit_to_work_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-15", "metric": "permit_to_work_gap_count", "label": "permit-to-work gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "permit-to-work gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_unplanned_downtime_pct_16(record):
    """Evaluate unplanned downtime for control WP-0628-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unplanned_downtime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-16", "metric": "unplanned_downtime_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-16", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-16", "metric": "unplanned_downtime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-16", "metric": "unplanned_downtime_pct", "label": "unplanned downtime",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "unplanned downtime exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_maintenance_window_overrun_minutes_17(record):
    """Evaluate maintenance window overrun for control WP-0628-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_window_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-17", "metric": "maintenance_window_overrun_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-17", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-17", "metric": "maintenance_window_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-17", "metric": "maintenance_window_overrun_minutes", "label": "maintenance window overrun",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "maintenance window overrun falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_referential_integrity_pct_18(record):
    """Evaluate referential integrity for control WP-0628-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("referential_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-18", "metric": "referential_integrity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-18", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-18", "metric": "referential_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-18", "metric": "referential_integrity_pct", "label": "referential integrity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "referential integrity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_route_master_gap_count_19(record):
    """Evaluate route master gaps for control WP-0628-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-19", "metric": "route_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-19", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-19", "metric": "route_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-19", "metric": "route_master_gap_count", "label": "route master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_purchase_order_change_count_20(record):
    """Evaluate purchase order changes for control WP-0628-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-20", "metric": "purchase_order_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-20", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-20", "metric": "purchase_order_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-20", "metric": "purchase_order_change_count", "label": "purchase order changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "purchase order changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_delivery_geofence_miss_count_21(record):
    """Evaluate delivery geofence misses for control WP-0628-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_geofence_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-21", "metric": "delivery_geofence_miss_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-21", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-21", "metric": "delivery_geofence_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-21", "metric": "delivery_geofence_miss_count", "label": "delivery geofence misses",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "delivery geofence misses falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_fuel_surcharge_variance_pct_22(record):
    """Evaluate fuel surcharge variance for control WP-0628-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_surcharge_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-22", "metric": "fuel_surcharge_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-22", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-22", "metric": "fuel_surcharge_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-22", "metric": "fuel_surcharge_variance_pct", "label": "fuel surcharge variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fuel surcharge variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_highway_restriction_match_count_23(record):
    """Evaluate highway restriction matches for control WP-0628-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("highway_restriction_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-23", "metric": "highway_restriction_match_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-23", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-23", "metric": "highway_restriction_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-23", "metric": "highway_restriction_match_count", "label": "highway restriction matches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "highway restriction matches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_recovery_plan_age_days_24(record):
    """Evaluate supplier recovery plan age for control WP-0628-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0628-24", "metric": "supplier_recovery_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0628-24", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0628-24", "metric": "supplier_recovery_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0628-24", "metric": "supplier_recovery_plan_age_days", "label": "supplier recovery plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier recovery plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_tax_rate_variance_pct_01, assess_supplier_queue_time_hours_02, assess_supplier_preferred_status_review_age_days_03, assess_supplier_post_exit_data_transfer_count_04, assess_lot_age_days_05, assess_cold_chain_excursion_minutes_06, assess_smoke_alarm_signal_07, assess_label_reprint_count_08, assess_putaway_accuracy_pct_09, assess_dead_letter_count_10, assess_each_pick_ratio_pct_11, assess_camera_coverage_pct_12, assess_energy_peak_kw_13, assess_insurance_coverage_pct_14, assess_permit_to_work_gap_count_15, assess_unplanned_downtime_pct_16, assess_maintenance_window_overrun_minutes_17, assess_referential_integrity_pct_18, assess_route_master_gap_count_19, assess_purchase_order_change_count_20, assess_delivery_geofence_miss_count_21, assess_fuel_surcharge_variance_pct_22, assess_highway_restriction_match_count_23, assess_supplier_recovery_plan_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

