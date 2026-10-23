"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_batch_cycle_hours_01(record):
    """Evaluate supplier batch cycle for control WP-0250-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_batch_cycle_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-01", "metric": "supplier_batch_cycle_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-01", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-01", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-01", "metric": "supplier_batch_cycle_hours", "label": "supplier batch cycle",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier batch cycle must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_award_expiry_days_02(record):
    """Evaluate supplier award validity for control WP-0250-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_award_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-02", "metric": "supplier_award_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-02", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-02", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-02", "metric": "supplier_award_expiry_days", "label": "supplier award validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier award validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_post_exit_access_count_03(record):
    """Evaluate post-exit access events for control WP-0250-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-03", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-03", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-03", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-03", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "post-exit access events falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_expiry_days_04(record):
    """Evaluate days to expiry for control WP-0250-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-04", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-04", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-04", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-04", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "days to expiry must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_customs_hold_hours_05(record):
    """Evaluate customs hold for control WP-0250-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-05", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-05", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-05", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-05", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customs hold must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_water_leak_signal_06(record):
    """Evaluate water leak signal for control WP-0250-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-06", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-06", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-06", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-06", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "water leak signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_scanner_disconnect_count_07(record):
    """Evaluate scanner disconnects for control WP-0250-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_disconnect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-07", "metric": "scanner_disconnect_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-07", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-07", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-07", "metric": "scanner_disconnect_count", "label": "scanner disconnects",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "scanner disconnects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_receiving_accuracy_pct_08(record):
    """Evaluate receiving accuracy for control WP-0250-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-08", "metric": "receiving_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-08", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-08", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-08", "metric": "receiving_accuracy_pct", "label": "receiving accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receiving accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_queue_retry_pct_09(record):
    """Evaluate queue retry rate for control WP-0250-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_retry_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-09", "metric": "queue_retry_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-09", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-09", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-09", "metric": "queue_retry_pct", "label": "queue retry rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "queue retry rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_case_pick_ratio_pct_10(record):
    """Evaluate case pick ratio for control WP-0250-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("case_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-10", "metric": "case_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-10", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-10", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-10", "metric": "case_pick_ratio_pct", "label": "case pick ratio",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "case pick ratio exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_visitor_badge_gap_count_11(record):
    """Evaluate visitor badge gaps for control WP-0250-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("visitor_badge_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-11", "metric": "visitor_badge_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-11", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-11", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-11", "metric": "visitor_badge_gap_count", "label": "visitor badge gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "visitor badge gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_water_consumption_liters_12(record):
    """Evaluate water consumption for control WP-0250-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_consumption_liters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-12", "metric": "water_consumption_liters",
            "status": "insufficient_data",
            "severity": "medium", "unit": "liters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-12", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-12", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-12", "metric": "water_consumption_liters", "label": "water consumption",
        "status": "breach", "severity": "medium", "unit": "liters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "water consumption must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_vault_access_review_age_days_13(record):
    """Evaluate vault access review age for control WP-0250-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vault_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-13", "metric": "vault_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-13", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-13", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-13", "metric": "vault_access_review_age_days", "label": "vault access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vault access review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_sds_access_pct_14(record):
    """Evaluate SDS access completeness for control WP-0250-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sds_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-14", "metric": "sds_access_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-14", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-14", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-14", "metric": "sds_access_pct", "label": "SDS access completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "SDS access completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_planned_maintenance_pct_15(record):
    """Evaluate planned maintenance share for control WP-0250-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("planned_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-15", "metric": "planned_maintenance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-15", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-15", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-15", "metric": "planned_maintenance_pct", "label": "planned maintenance share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "planned maintenance share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_service_availability_pct_16(record):
    """Evaluate service availability for control WP-0250-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-16", "metric": "service_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-16", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-16", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-16", "metric": "service_availability_pct", "label": "service availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "service availability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_record_uniqueness_pct_17(record):
    """Evaluate record uniqueness for control WP-0250-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_uniqueness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-17", "metric": "record_uniqueness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-17", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-17", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-17", "metric": "record_uniqueness_pct", "label": "record uniqueness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "record uniqueness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_carrier_master_gap_count_18(record):
    """Evaluate carrier master gaps for control WP-0250-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-18", "metric": "carrier_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-18", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-18", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-18", "metric": "carrier_master_gap_count", "label": "carrier master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "carrier master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_sourcing_switch_cost_19(record):
    """Evaluate sourcing switch cost for control WP-0250-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sourcing_switch_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-19", "metric": "sourcing_switch_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-19", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-19", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-19", "metric": "sourcing_switch_cost", "label": "sourcing switch cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "sourcing switch cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_delivery_scan_gap_count_20(record):
    """Evaluate delivery scan gaps for control WP-0250-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_scan_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-20", "metric": "delivery_scan_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-20", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-20", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-20", "metric": "delivery_scan_gap_count", "label": "delivery scan gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery scan gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_freight_payment_age_days_21(record):
    """Evaluate freight payment age for control WP-0250-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_payment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-21", "metric": "freight_payment_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-21", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-21", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-21", "metric": "freight_payment_age_days", "label": "freight payment age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "freight payment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_cargo_tamper_alert_count_22(record):
    """Evaluate cargo tamper alerts for control WP-0250-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cargo_tamper_alert_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-22", "metric": "cargo_tamper_alert_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-22", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-22", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-22", "metric": "cargo_tamper_alert_count", "label": "cargo tamper alerts",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "cargo tamper alerts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_dispute_count_23(record):
    """Evaluate supplier disputes for control WP-0250-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-23", "metric": "supplier_dispute_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-23", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-23", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-23", "metric": "supplier_dispute_count", "label": "supplier disputes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier disputes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_water_risk_score_24(record):
    """Evaluate supplier water risk for control WP-0250-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0250-24", "metric": "supplier_water_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0250-24", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0250-24", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0250-24", "metric": "supplier_water_risk_score", "label": "supplier water risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_batch_cycle_hours_01, assess_supplier_award_expiry_days_02, assess_supplier_post_exit_access_count_03, assess_expiry_days_04, assess_customs_hold_hours_05, assess_water_leak_signal_06, assess_scanner_disconnect_count_07, assess_receiving_accuracy_pct_08, assess_queue_retry_pct_09, assess_case_pick_ratio_pct_10, assess_visitor_badge_gap_count_11, assess_water_consumption_liters_12, assess_vault_access_review_age_days_13, assess_sds_access_pct_14, assess_planned_maintenance_pct_15, assess_service_availability_pct_16, assess_record_uniqueness_pct_17, assess_carrier_master_gap_count_18, assess_sourcing_switch_cost_19, assess_delivery_scan_gap_count_20, assess_freight_payment_age_days_21, assess_cargo_tamper_alert_count_22, assess_supplier_dispute_count_23, assess_supplier_water_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

