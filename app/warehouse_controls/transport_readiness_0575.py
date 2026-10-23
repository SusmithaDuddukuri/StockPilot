"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_demand_spike_pct_01(record):
    """Evaluate demand spike for control WP-0575-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demand_spike_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-01", "metric": "demand_spike_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-01", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-01", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-01", "metric": "demand_spike_pct", "label": "demand spike",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "demand spike must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_route_on_time_pct_02(record):
    """Evaluate route on-time rate for control WP-0575-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_on_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-02", "metric": "route_on_time_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-02", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-02", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-02", "metric": "route_on_time_pct", "label": "route on-time rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route on-time rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_failed_login_count_03(record):
    """Evaluate failed logins for control WP-0575-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_login_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-03", "metric": "failed_login_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-03", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-03", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-03", "metric": "failed_login_count", "label": "failed logins",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "failed logins exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_absence_rate_pct_04(record):
    """Evaluate absence rate for control WP-0575-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("absence_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-04", "metric": "absence_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-04", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-04", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-04", "metric": "absence_rate_pct", "label": "absence rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "absence rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_emergency_light_test_age_days_05(record):
    """Evaluate emergency-light test age for control WP-0575-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_light_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-05", "metric": "emergency_light_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-05", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-05", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-05", "metric": "emergency_light_test_age_days", "label": "emergency-light test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "emergency-light test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_signature_capture_pct_06(record):
    """Evaluate signature capture for control WP-0575-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("signature_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-06", "metric": "signature_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-06", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-06", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-06", "metric": "signature_capture_pct", "label": "signature capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "signature capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_chain_temperature_coverage_pct_07(record):
    """Evaluate temperature coverage for control WP-0575-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-07", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-07", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-07", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-07", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "temperature coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_replacement_stock_cover_days_08(record):
    """Evaluate replacement stock cover for control WP-0575-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-08", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-08", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-08", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-08", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "replacement stock cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_fall_protection_compliance_pct_09(record):
    """Evaluate fall protection compliance for control WP-0575-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-09", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-09", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-09", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-09", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fall protection compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_control_room_access_gap_count_10(record):
    """Evaluate control-room access gaps for control WP-0575-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-10", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-10", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-10", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-10", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "control-room access gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_dns_failure_count_11(record):
    """Evaluate DNS failures for control WP-0575-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-11", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-11", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-11", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-11", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "DNS failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_calibration_due_count_12(record):
    """Evaluate calibration due for control WP-0575-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("calibration_due_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-12", "metric": "calibration_due_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-12", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-12", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-12", "metric": "calibration_due_count", "label": "calibration due",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "calibration due falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_inventory_snapshot_age_minutes_13(record):
    """Evaluate inventory snapshot age for control WP-0575-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_snapshot_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-13", "metric": "inventory_snapshot_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-13", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-13", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-13", "metric": "inventory_snapshot_age_minutes", "label": "inventory snapshot age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory snapshot age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_slotting_recommendation_accept_pct_14(record):
    """Evaluate slotting acceptance for control WP-0575-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_recommendation_accept_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-14", "metric": "slotting_recommendation_accept_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-14", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-14", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-14", "metric": "slotting_recommendation_accept_pct", "label": "slotting acceptance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slotting acceptance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_tax_document_completeness_pct_15(record):
    """Evaluate tax document completeness for control WP-0575-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_document_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-15", "metric": "tax_document_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-15", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-15", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-15", "metric": "tax_document_completeness_pct", "label": "tax document completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "tax document completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_driver_checkin_compliance_pct_16(record):
    """Evaluate driver check-in compliance for control WP-0575-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-16", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-16", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-16", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-16", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "driver check-in compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_labor_productivity_index_17(record):
    """Evaluate labor productivity for control WP-0575-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-17", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-17", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-17", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-17", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "labor productivity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_label_compliance_pct_18(record):
    """Evaluate supplier label compliance for control WP-0575-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-18", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-18", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-18", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-18", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier label compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_obsolescence_notice_days_19(record):
    """Evaluate supplier obsolescence notice for control WP-0575-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-19", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-19", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-19", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-19", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier obsolescence notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_delivery_slot_compliance_pct_20(record):
    """Evaluate supplier delivery-slot compliance for control WP-0575-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-20", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-20", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-20", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-20", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier delivery-slot compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_support_ack_minutes_21(record):
    """Evaluate supplier support acknowledgement for control WP-0575-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-21", "metric": "supplier_support_ack_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-21", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-21", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-21", "metric": "supplier_support_ack_minutes", "label": "supplier support acknowledgement",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier support acknowledgement must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_serial_data_completeness_pct_22(record):
    """Evaluate supplier serial-data completeness for control WP-0575-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-22", "metric": "supplier_serial_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-22", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-22", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-22", "metric": "supplier_serial_data_completeness_pct", "label": "supplier serial-data completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier serial-data completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_personnel_screening_pct_23(record):
    """Evaluate supplier personnel screening for control WP-0575-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-23", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-23", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-23", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-23", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier personnel screening exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_knowledge_transfer_pct_24(record):
    """Evaluate supplier knowledge transfer for control WP-0575-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0575-24", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0575-24", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0575-24", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0575-24", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier knowledge transfer falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_demand_spike_pct_01, assess_route_on_time_pct_02, assess_failed_login_count_03, assess_absence_rate_pct_04, assess_emergency_light_test_age_days_05, assess_signature_capture_pct_06, assess_chain_temperature_coverage_pct_07, assess_replacement_stock_cover_days_08, assess_fall_protection_compliance_pct_09, assess_control_room_access_gap_count_10, assess_dns_failure_count_11, assess_calibration_due_count_12, assess_inventory_snapshot_age_minutes_13, assess_slotting_recommendation_accept_pct_14, assess_tax_document_completeness_pct_15, assess_driver_checkin_compliance_pct_16, assess_labor_productivity_index_17, assess_supplier_label_compliance_pct_18, assess_supplier_obsolescence_notice_days_19, assess_supplier_delivery_slot_compliance_pct_20, assess_supplier_support_ack_minutes_21, assess_supplier_serial_data_completeness_pct_22, assess_supplier_personnel_screening_pct_23, assess_supplier_knowledge_transfer_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

