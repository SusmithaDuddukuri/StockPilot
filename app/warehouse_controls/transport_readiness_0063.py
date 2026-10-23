"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_post_exit_access_count_01(record):
    """Evaluate post-exit access events for control WP-0063-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-01", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-01", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-01", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-01", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "post-exit access events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_expiry_days_02(record):
    """Evaluate days to expiry for control WP-0063-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-02", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-02", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-02", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-02", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "days to expiry must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_customs_hold_hours_03(record):
    """Evaluate customs hold for control WP-0063-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-03", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-03", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-03", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-03", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "customs hold exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_water_leak_signal_04(record):
    """Evaluate water leak signal for control WP-0063-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-04", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-04", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-04", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-04", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "water leak signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_scanner_disconnect_count_05(record):
    """Evaluate scanner disconnects for control WP-0063-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_disconnect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-05", "metric": "scanner_disconnect_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-05", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-05", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-05", "metric": "scanner_disconnect_count", "label": "scanner disconnects",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner disconnects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_receiving_accuracy_pct_06(record):
    """Evaluate receiving accuracy for control WP-0063-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-06", "metric": "receiving_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-06", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-06", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-06", "metric": "receiving_accuracy_pct", "label": "receiving accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "receiving accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_queue_retry_pct_07(record):
    """Evaluate queue retry rate for control WP-0063-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_retry_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-07", "metric": "queue_retry_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-07", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-07", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-07", "metric": "queue_retry_pct", "label": "queue retry rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "queue retry rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_case_pick_ratio_pct_08(record):
    """Evaluate case pick ratio for control WP-0063-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("case_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-08", "metric": "case_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-08", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-08", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-08", "metric": "case_pick_ratio_pct", "label": "case pick ratio",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "case pick ratio falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_visitor_badge_gap_count_09(record):
    """Evaluate visitor badge gaps for control WP-0063-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("visitor_badge_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-09", "metric": "visitor_badge_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-09", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-09", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-09", "metric": "visitor_badge_gap_count", "label": "visitor badge gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "visitor badge gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_water_consumption_liters_10(record):
    """Evaluate water consumption for control WP-0063-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_consumption_liters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-10", "metric": "water_consumption_liters",
            "status": "insufficient_data",
            "severity": "low", "unit": "liters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-10", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-10", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-10", "metric": "water_consumption_liters", "label": "water consumption",
        "status": "breach", "severity": "low", "unit": "liters",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "water consumption must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_vault_access_review_age_days_11(record):
    """Evaluate vault access review age for control WP-0063-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vault_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-11", "metric": "vault_access_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-11", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-11", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-11", "metric": "vault_access_review_age_days", "label": "vault access review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "vault access review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_sds_access_pct_12(record):
    """Evaluate SDS access completeness for control WP-0063-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sds_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-12", "metric": "sds_access_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-12", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-12", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-12", "metric": "sds_access_pct", "label": "SDS access completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "SDS access completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_planned_maintenance_pct_13(record):
    """Evaluate planned maintenance share for control WP-0063-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("planned_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-13", "metric": "planned_maintenance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-13", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-13", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-13", "metric": "planned_maintenance_pct", "label": "planned maintenance share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "planned maintenance share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_service_availability_pct_14(record):
    """Evaluate service availability for control WP-0063-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-14", "metric": "service_availability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-14", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-14", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-14", "metric": "service_availability_pct", "label": "service availability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "service availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_record_uniqueness_pct_15(record):
    """Evaluate record uniqueness for control WP-0063-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_uniqueness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-15", "metric": "record_uniqueness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-15", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-15", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-15", "metric": "record_uniqueness_pct", "label": "record uniqueness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "record uniqueness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_carrier_master_gap_count_16(record):
    """Evaluate carrier master gaps for control WP-0063-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-16", "metric": "carrier_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-16", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-16", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-16", "metric": "carrier_master_gap_count", "label": "carrier master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "carrier master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_sourcing_switch_cost_17(record):
    """Evaluate sourcing switch cost for control WP-0063-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sourcing_switch_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-17", "metric": "sourcing_switch_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-17", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-17", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-17", "metric": "sourcing_switch_cost", "label": "sourcing switch cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sourcing switch cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_delivery_scan_gap_count_18(record):
    """Evaluate delivery scan gaps for control WP-0063-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_scan_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-18", "metric": "delivery_scan_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-18", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-18", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-18", "metric": "delivery_scan_gap_count", "label": "delivery scan gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "delivery scan gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_freight_payment_age_days_19(record):
    """Evaluate freight payment age for control WP-0063-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_payment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-19", "metric": "freight_payment_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-19", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-19", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-19", "metric": "freight_payment_age_days", "label": "freight payment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "freight payment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_cargo_tamper_alert_count_20(record):
    """Evaluate cargo tamper alerts for control WP-0063-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cargo_tamper_alert_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-20", "metric": "cargo_tamper_alert_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-20", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-20", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-20", "metric": "cargo_tamper_alert_count", "label": "cargo tamper alerts",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "cargo tamper alerts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_dispute_count_21(record):
    """Evaluate supplier disputes for control WP-0063-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-21", "metric": "supplier_dispute_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-21", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-21", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-21", "metric": "supplier_dispute_count", "label": "supplier disputes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disputes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_water_risk_score_22(record):
    """Evaluate supplier water risk for control WP-0063-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-22", "metric": "supplier_water_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-22", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-22", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-22", "metric": "supplier_water_risk_score", "label": "supplier water risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier water risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_mode_shift_pct_23(record):
    """Evaluate supplier mode shift for control WP-0063-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mode_shift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-23", "metric": "supplier_mode_shift_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-23", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-23", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-23", "metric": "supplier_mode_shift_pct", "label": "supplier mode shift",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier mode shift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_policy_ack_pct_24(record):
    """Evaluate supplier policy acknowledgement for control WP-0063-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0063-24", "metric": "supplier_policy_ack_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0063-24", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0063-24", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0063-24", "metric": "supplier_policy_ack_pct", "label": "supplier policy acknowledgement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier policy acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_post_exit_access_count_01, assess_expiry_days_02, assess_customs_hold_hours_03, assess_water_leak_signal_04, assess_scanner_disconnect_count_05, assess_receiving_accuracy_pct_06, assess_queue_retry_pct_07, assess_case_pick_ratio_pct_08, assess_visitor_badge_gap_count_09, assess_water_consumption_liters_10, assess_vault_access_review_age_days_11, assess_sds_access_pct_12, assess_planned_maintenance_pct_13, assess_service_availability_pct_14, assess_record_uniqueness_pct_15, assess_carrier_master_gap_count_16, assess_sourcing_switch_cost_17, assess_delivery_scan_gap_count_18, assess_freight_payment_age_days_19, assess_cargo_tamper_alert_count_20, assess_supplier_dispute_count_21, assess_supplier_water_risk_score_22, assess_supplier_mode_shift_pct_23, assess_supplier_policy_ack_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

