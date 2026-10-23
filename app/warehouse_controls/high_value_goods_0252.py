"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_certificate_revocation_pct_01(record):
    """Evaluate supplier certificate revocation for control WP-0252-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-01", "metric": "supplier_certificate_revocation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-01", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-01", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-01", "metric": "supplier_certificate_revocation_pct", "label": "supplier certificate revocation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier certificate revocation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_pick_rate_02(record):
    """Evaluate picking rate for control WP-0252-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-02", "metric": "pick_rate",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-02", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-02", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-02", "metric": "pick_rate", "label": "picking rate",
        "status": "breach", "severity": "medium", "unit": "lines/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "picking rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_bin_distance_m_03(record):
    """Evaluate bin travel distance for control WP-0252-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bin_distance_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-03", "metric": "bin_distance_m",
            "status": "insufficient_data",
            "severity": "high", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-03", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-03", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-03", "metric": "bin_distance_m", "label": "bin travel distance",
        "status": "breach", "severity": "high", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "bin travel distance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_cycle_count_age_days_04(record):
    """Evaluate cycle-count age for control WP-0252-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-04", "metric": "cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-04", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-04", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-04", "metric": "cycle_count_age_days", "label": "cycle-count age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "cycle-count age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_demand_spike_pct_05(record):
    """Evaluate demand spike for control WP-0252-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demand_spike_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-05", "metric": "demand_spike_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-05", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-05", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-05", "metric": "demand_spike_pct", "label": "demand spike",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "demand spike falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_route_on_time_pct_06(record):
    """Evaluate route on-time rate for control WP-0252-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_on_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-06", "metric": "route_on_time_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-06", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-06", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-06", "metric": "route_on_time_pct", "label": "route on-time rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "route on-time rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_failed_login_count_07(record):
    """Evaluate failed logins for control WP-0252-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_login_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-07", "metric": "failed_login_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-07", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-07", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-07", "metric": "failed_login_count", "label": "failed logins",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "failed logins must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_absence_rate_pct_08(record):
    """Evaluate absence rate for control WP-0252-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("absence_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-08", "metric": "absence_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-08", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-08", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-08", "metric": "absence_rate_pct", "label": "absence rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "absence rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_emergency_light_test_age_days_09(record):
    """Evaluate emergency-light test age for control WP-0252-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_light_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-09", "metric": "emergency_light_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-09", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-09", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-09", "metric": "emergency_light_test_age_days", "label": "emergency-light test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "emergency-light test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_signature_capture_pct_10(record):
    """Evaluate signature capture for control WP-0252-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("signature_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-10", "metric": "signature_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-10", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-10", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-10", "metric": "signature_capture_pct", "label": "signature capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "signature capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_chain_temperature_coverage_pct_11(record):
    """Evaluate temperature coverage for control WP-0252-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-11", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-11", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-11", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-11", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "temperature coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_replacement_stock_cover_days_12(record):
    """Evaluate replacement stock cover for control WP-0252-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-12", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-12", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-12", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-12", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "replacement stock cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_fall_protection_compliance_pct_13(record):
    """Evaluate fall protection compliance for control WP-0252-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-13", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-13", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-13", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-13", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "fall protection compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_control_room_access_gap_count_14(record):
    """Evaluate control-room access gaps for control WP-0252-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-14", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-14", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-14", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-14", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "control-room access gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_dns_failure_count_15(record):
    """Evaluate DNS failures for control WP-0252-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-15", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-15", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-15", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-15", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "DNS failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_calibration_due_count_16(record):
    """Evaluate calibration due for control WP-0252-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("calibration_due_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-16", "metric": "calibration_due_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-16", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-16", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-16", "metric": "calibration_due_count", "label": "calibration due",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "calibration due exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_inventory_snapshot_age_minutes_17(record):
    """Evaluate inventory snapshot age for control WP-0252-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_snapshot_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-17", "metric": "inventory_snapshot_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-17", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-17", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-17", "metric": "inventory_snapshot_age_minutes", "label": "inventory snapshot age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "inventory snapshot age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_slotting_recommendation_accept_pct_18(record):
    """Evaluate slotting acceptance for control WP-0252-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_recommendation_accept_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-18", "metric": "slotting_recommendation_accept_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-18", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-18", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-18", "metric": "slotting_recommendation_accept_pct", "label": "slotting acceptance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "slotting acceptance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_tax_document_completeness_pct_19(record):
    """Evaluate tax document completeness for control WP-0252-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_document_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-19", "metric": "tax_document_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-19", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-19", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-19", "metric": "tax_document_completeness_pct", "label": "tax document completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "tax document completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_driver_checkin_compliance_pct_20(record):
    """Evaluate driver check-in compliance for control WP-0252-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-20", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-20", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-20", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-20", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "driver check-in compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_labor_productivity_index_21(record):
    """Evaluate labor productivity for control WP-0252-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-21", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-21", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-21", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-21", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "labor productivity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_label_compliance_pct_22(record):
    """Evaluate supplier label compliance for control WP-0252-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-22", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-22", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-22", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-22", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_obsolescence_notice_days_23(record):
    """Evaluate supplier obsolescence notice for control WP-0252-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-23", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-23", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-23", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-23", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier obsolescence notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_delivery_slot_compliance_pct_24(record):
    """Evaluate supplier delivery-slot compliance for control WP-0252-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0252-24", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0252-24", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0252-24", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0252-24", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier delivery-slot compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_certificate_revocation_pct_01, assess_pick_rate_02, assess_bin_distance_m_03, assess_cycle_count_age_days_04, assess_demand_spike_pct_05, assess_route_on_time_pct_06, assess_failed_login_count_07, assess_absence_rate_pct_08, assess_emergency_light_test_age_days_09, assess_signature_capture_pct_10, assess_chain_temperature_coverage_pct_11, assess_replacement_stock_cover_days_12, assess_fall_protection_compliance_pct_13, assess_control_room_access_gap_count_14, assess_dns_failure_count_15, assess_calibration_due_count_16, assess_inventory_snapshot_age_minutes_17, assess_slotting_recommendation_accept_pct_18, assess_tax_document_completeness_pct_19, assess_driver_checkin_compliance_pct_20, assess_labor_productivity_index_21, assess_supplier_label_compliance_pct_22, assess_supplier_obsolescence_notice_days_23, assess_supplier_delivery_slot_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

