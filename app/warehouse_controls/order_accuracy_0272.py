"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_sprinkler_obstruction_count_01(record):
    """Evaluate sprinkler obstructions for control WP-0272-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-01", "metric": "sprinkler_obstruction_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-01", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-01", "metric": "sprinkler_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-01", "metric": "sprinkler_obstruction_count", "label": "sprinkler obstructions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "sprinkler obstructions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_amr_battery_pct_02(record):
    """Evaluate AMR battery for control WP-0272-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("amr_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-02", "metric": "amr_battery_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-02", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-02", "metric": "amr_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-02", "metric": "amr_battery_pct", "label": "AMR battery",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "AMR battery must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_monitoring_coverage_pct_03(record):
    """Evaluate monitoring coverage for control WP-0272-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("monitoring_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-03", "metric": "monitoring_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-03", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-03", "metric": "monitoring_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-03", "metric": "monitoring_coverage_pct", "label": "monitoring coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "monitoring coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_device_enrollment_pct_04(record):
    """Evaluate device enrollment for control WP-0272-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("device_enrollment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-04", "metric": "device_enrollment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-04", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-04", "metric": "device_enrollment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-04", "metric": "device_enrollment_pct", "label": "device enrollment",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "device enrollment exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_order_line_duplicate_count_05(record):
    """Evaluate duplicate order lines for control WP-0272-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_line_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-05", "metric": "order_line_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "lines",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-05", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-05", "metric": "order_line_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-05", "metric": "order_line_duplicate_count", "label": "duplicate order lines",
        "status": "breach", "severity": "low", "unit": "lines",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "duplicate order lines falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_putaway_task_queue_06(record):
    """Evaluate putaway task queue for control WP-0272-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-06", "metric": "putaway_task_queue",
            "status": "insufficient_data",
            "severity": "medium", "unit": "tasks",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-06", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-06", "metric": "putaway_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-06", "metric": "putaway_task_queue", "label": "putaway task queue",
        "status": "breach", "severity": "medium", "unit": "tasks",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway task queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_credit_hold_age_hours_07(record):
    """Evaluate credit hold age for control WP-0272-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_hold_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-07", "metric": "credit_hold_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-07", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-07", "metric": "credit_hold_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-07", "metric": "credit_hold_age_hours", "label": "credit hold age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "credit hold age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_crossdock_miss_count_08(record):
    """Evaluate cross-dock misses for control WP-0272-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_miss_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-08", "metric": "crossdock_miss_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-08", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-08", "metric": "crossdock_miss_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-08", "metric": "crossdock_miss_count", "label": "cross-dock misses",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "cross-dock misses exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_space_cost_per_pallet_09(record):
    """Evaluate space cost per pallet for control WP-0272-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("space_cost_per_pallet")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-09", "metric": "space_cost_per_pallet",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-09", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-09", "metric": "space_cost_per_pallet", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-09", "metric": "space_cost_per_pallet", "label": "space cost per pallet",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "space cost per pallet falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_order_ack_pct_10(record):
    """Evaluate supplier order acknowledgement for control WP-0272-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-10", "metric": "supplier_order_ack_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-10", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-10", "metric": "supplier_order_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-10", "metric": "supplier_order_ack_pct", "label": "supplier order acknowledgement",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier order acknowledgement must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_recovery_test_age_days_11(record):
    """Evaluate supplier recovery test age for control WP-0272-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-11", "metric": "supplier_recovery_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-11", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-11", "metric": "supplier_recovery_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-11", "metric": "supplier_recovery_test_age_days", "label": "supplier recovery test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_buffer_inventory_units_12(record):
    """Evaluate supplier buffer inventory for control WP-0272-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_buffer_inventory_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-12", "metric": "supplier_buffer_inventory_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-12", "metric": "supplier_buffer_inventory_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-12", "metric": "supplier_buffer_inventory_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-12", "metric": "supplier_buffer_inventory_units", "label": "supplier buffer inventory",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier buffer inventory exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_encryption_compliance_pct_13(record):
    """Evaluate supplier encryption compliance for control WP-0272-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-13", "metric": "supplier_encryption_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-13", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-13", "metric": "supplier_encryption_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-13", "metric": "supplier_encryption_compliance_pct", "label": "supplier encryption compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier encryption compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_port_alternative_count_14(record):
    """Evaluate supplier port alternatives for control WP-0272-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_alternative_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-14", "metric": "supplier_port_alternative_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ports",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-14", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-14", "metric": "supplier_port_alternative_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-14", "metric": "supplier_port_alternative_count", "label": "supplier port alternatives",
        "status": "breach", "severity": "medium", "unit": "ports",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier port alternatives must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_natural_hazard_score_15(record):
    """Evaluate supplier natural-hazard exposure for control WP-0272-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_natural_hazard_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-15", "metric": "supplier_natural_hazard_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-15", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-15", "metric": "supplier_natural_hazard_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-15", "metric": "supplier_natural_hazard_score", "label": "supplier natural-hazard exposure",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier natural-hazard exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_recovery_contact_pct_16(record):
    """Evaluate supplier recovery contact completeness for control WP-0272-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_contact_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-16", "metric": "supplier_recovery_contact_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-16", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-16", "metric": "supplier_recovery_contact_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-16", "metric": "supplier_recovery_contact_pct", "label": "supplier recovery contact completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier recovery contact completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_major_finding_count_17(record):
    """Evaluate supplier major findings for control WP-0272-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_major_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-17", "metric": "supplier_major_finding_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-17", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-17", "metric": "supplier_major_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-17", "metric": "supplier_major_finding_count", "label": "supplier major findings",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier major findings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_community_impact_score_18(record):
    """Evaluate supplier community impact for control WP-0272-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_community_impact_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-18", "metric": "supplier_community_impact_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-18", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-18", "metric": "supplier_community_impact_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-18", "metric": "supplier_community_impact_score", "label": "supplier community impact",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier community impact must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_recovery_capacity_pct_19(record):
    """Evaluate supplier recovery capacity for control WP-0272-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-19", "metric": "supplier_recovery_capacity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-19", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-19", "metric": "supplier_recovery_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-19", "metric": "supplier_recovery_capacity_pct", "label": "supplier recovery capacity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery capacity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_delivery_improvement_pct_20(record):
    """Evaluate supplier delivery improvement for control WP-0272-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_improvement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-20", "metric": "supplier_delivery_improvement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-20", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-20", "metric": "supplier_delivery_improvement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-20", "metric": "supplier_delivery_improvement_pct", "label": "supplier delivery improvement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier delivery improvement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_vector_recall_pct_21(record):
    """Evaluate supplier vector recall for control WP-0272-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vector_recall_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-21", "metric": "supplier_vector_recall_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-21", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-21", "metric": "supplier_vector_recall_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-21", "metric": "supplier_vector_recall_pct", "label": "supplier vector recall",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "supplier vector recall falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_capacity_forecast_confidence_pct_22(record):
    """Evaluate supplier capacity forecast confidence for control WP-0272-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-22", "metric": "supplier_capacity_forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-22", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-22", "metric": "supplier_capacity_forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-22", "metric": "supplier_capacity_forecast_confidence_pct", "label": "supplier capacity forecast confidence",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity forecast confidence must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_ip_claim_count_23(record):
    """Evaluate supplier IP claims for control WP-0272-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ip_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-23", "metric": "supplier_ip_claim_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-23", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-23", "metric": "supplier_ip_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-23", "metric": "supplier_ip_claim_count", "label": "supplier IP claims",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier IP claims must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_policy_review_age_days_24(record):
    """Evaluate supplier policy review age for control WP-0272-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0272-24", "metric": "supplier_policy_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0272-24", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0272-24", "metric": "supplier_policy_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0272-24", "metric": "supplier_policy_review_age_days", "label": "supplier policy review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier policy review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_sprinkler_obstruction_count_01, assess_amr_battery_pct_02, assess_monitoring_coverage_pct_03, assess_device_enrollment_pct_04, assess_order_line_duplicate_count_05, assess_putaway_task_queue_06, assess_credit_hold_age_hours_07, assess_crossdock_miss_count_08, assess_space_cost_per_pallet_09, assess_supplier_order_ack_pct_10, assess_supplier_recovery_test_age_days_11, assess_supplier_buffer_inventory_units_12, assess_supplier_encryption_compliance_pct_13, assess_supplier_port_alternative_count_14, assess_supplier_natural_hazard_score_15, assess_supplier_recovery_contact_pct_16, assess_supplier_major_finding_count_17, assess_supplier_community_impact_score_18, assess_supplier_recovery_capacity_pct_19, assess_supplier_delivery_improvement_pct_20, assess_supplier_vector_recall_pct_21, assess_supplier_capacity_forecast_confidence_pct_22, assess_supplier_ip_claim_count_23, assess_supplier_policy_review_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

