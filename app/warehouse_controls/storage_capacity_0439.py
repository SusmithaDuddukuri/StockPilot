"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_schedule_stability_pct_01(record):
    """Evaluate schedule stability for control WP-0439-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_stability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-01", "metric": "supplier_schedule_stability_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-01", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-01", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-01", "metric": "supplier_schedule_stability_pct", "label": "schedule stability",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "schedule stability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_pod_upload_age_hours_02(record):
    """Evaluate supplier POD upload age for control WP-0439-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pod_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-02", "metric": "supplier_pod_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-02", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-02", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-02", "metric": "supplier_pod_upload_age_hours", "label": "supplier POD upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier POD upload age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_certificate_revocation_pct_03(record):
    """Evaluate supplier certificate revocation for control WP-0439-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-03", "metric": "supplier_certificate_revocation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-03", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-03", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-03", "metric": "supplier_certificate_revocation_pct", "label": "supplier certificate revocation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier certificate revocation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_pick_rate_04(record):
    """Evaluate picking rate for control WP-0439-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-04", "metric": "pick_rate",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines/hour",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-04", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-04", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-04", "metric": "pick_rate", "label": "picking rate",
        "status": "breach", "severity": "high", "unit": "lines/hour",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "picking rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_bin_distance_m_05(record):
    """Evaluate bin travel distance for control WP-0439-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bin_distance_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-05", "metric": "bin_distance_m",
            "status": "insufficient_data",
            "severity": "critical", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-05", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-05", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-05", "metric": "bin_distance_m", "label": "bin travel distance",
        "status": "breach", "severity": "critical", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "bin travel distance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_cycle_count_age_days_06(record):
    """Evaluate cycle-count age for control WP-0439-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-06", "metric": "cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-06", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-06", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-06", "metric": "cycle_count_age_days", "label": "cycle-count age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cycle-count age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_demand_spike_pct_07(record):
    """Evaluate demand spike for control WP-0439-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demand_spike_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-07", "metric": "demand_spike_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-07", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-07", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-07", "metric": "demand_spike_pct", "label": "demand spike",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "demand spike exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_route_on_time_pct_08(record):
    """Evaluate route on-time rate for control WP-0439-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_on_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-08", "metric": "route_on_time_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-08", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-08", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-08", "metric": "route_on_time_pct", "label": "route on-time rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "route on-time rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_failed_login_count_09(record):
    """Evaluate failed logins for control WP-0439-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_login_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-09", "metric": "failed_login_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-09", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-09", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-09", "metric": "failed_login_count", "label": "failed logins",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "failed logins must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_absence_rate_pct_10(record):
    """Evaluate absence rate for control WP-0439-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("absence_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-10", "metric": "absence_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-10", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-10", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-10", "metric": "absence_rate_pct", "label": "absence rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "absence rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_emergency_light_test_age_days_11(record):
    """Evaluate emergency-light test age for control WP-0439-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_light_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-11", "metric": "emergency_light_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-11", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-11", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-11", "metric": "emergency_light_test_age_days", "label": "emergency-light test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "emergency-light test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_signature_capture_pct_12(record):
    """Evaluate signature capture for control WP-0439-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("signature_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-12", "metric": "signature_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-12", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-12", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-12", "metric": "signature_capture_pct", "label": "signature capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "signature capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_chain_temperature_coverage_pct_13(record):
    """Evaluate temperature coverage for control WP-0439-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-13", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-13", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-13", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-13", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "temperature coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_replacement_stock_cover_days_14(record):
    """Evaluate replacement stock cover for control WP-0439-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-14", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-14", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-14", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-14", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replacement stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_fall_protection_compliance_pct_15(record):
    """Evaluate fall protection compliance for control WP-0439-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-15", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-15", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-15", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-15", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "fall protection compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_control_room_access_gap_count_16(record):
    """Evaluate control-room access gaps for control WP-0439-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-16", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-16", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-16", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-16", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "control-room access gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_dns_failure_count_17(record):
    """Evaluate DNS failures for control WP-0439-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-17", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-17", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-17", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-17", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "DNS failures must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_calibration_due_count_18(record):
    """Evaluate calibration due for control WP-0439-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("calibration_due_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-18", "metric": "calibration_due_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-18", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-18", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-18", "metric": "calibration_due_count", "label": "calibration due",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "calibration due must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_inventory_snapshot_age_minutes_19(record):
    """Evaluate inventory snapshot age for control WP-0439-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_snapshot_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-19", "metric": "inventory_snapshot_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-19", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-19", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-19", "metric": "inventory_snapshot_age_minutes", "label": "inventory snapshot age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "inventory snapshot age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_slotting_recommendation_accept_pct_20(record):
    """Evaluate slotting acceptance for control WP-0439-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_recommendation_accept_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-20", "metric": "slotting_recommendation_accept_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-20", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-20", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-20", "metric": "slotting_recommendation_accept_pct", "label": "slotting acceptance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "slotting acceptance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_tax_document_completeness_pct_21(record):
    """Evaluate tax document completeness for control WP-0439-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_document_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-21", "metric": "tax_document_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-21", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-21", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-21", "metric": "tax_document_completeness_pct", "label": "tax document completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tax document completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_driver_checkin_compliance_pct_22(record):
    """Evaluate driver check-in compliance for control WP-0439-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-22", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-22", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-22", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-22", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "driver check-in compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_labor_productivity_index_23(record):
    """Evaluate labor productivity for control WP-0439-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-23", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-23", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-23", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-23", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "labor productivity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_label_compliance_pct_24(record):
    """Evaluate supplier label compliance for control WP-0439-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0439-24", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0439-24", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0439-24", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0439-24", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_schedule_stability_pct_01, assess_supplier_pod_upload_age_hours_02, assess_supplier_certificate_revocation_pct_03, assess_pick_rate_04, assess_bin_distance_m_05, assess_cycle_count_age_days_06, assess_demand_spike_pct_07, assess_route_on_time_pct_08, assess_failed_login_count_09, assess_absence_rate_pct_10, assess_emergency_light_test_age_days_11, assess_signature_capture_pct_12, assess_chain_temperature_coverage_pct_13, assess_replacement_stock_cover_days_14, assess_fall_protection_compliance_pct_15, assess_control_room_access_gap_count_16, assess_dns_failure_count_17, assess_calibration_due_count_18, assess_inventory_snapshot_age_minutes_19, assess_slotting_recommendation_accept_pct_20, assess_tax_document_completeness_pct_21, assess_driver_checkin_compliance_pct_22, assess_labor_productivity_index_23, assess_supplier_label_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

