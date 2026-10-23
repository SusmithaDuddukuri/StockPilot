"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_audited_financial_age_days_01(record):
    """Evaluate supplier audited-financial age for control WP-0427-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audited_financial_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-01", "metric": "supplier_audited_financial_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-01", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-01", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-01", "metric": "supplier_audited_financial_age_days", "label": "supplier audited-financial age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audited-financial age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_change_control_pct_02(record):
    """Evaluate supplier change control for control WP-0427-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-02", "metric": "supplier_change_control_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-02", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-02", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-02", "metric": "supplier_change_control_pct", "label": "supplier change control",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier change control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_pii_exposure_signal_03(record):
    """Evaluate supplier PII exposure signal for control WP-0427-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pii_exposure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-03", "metric": "supplier_pii_exposure_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-03", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-03", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-03", "metric": "supplier_pii_exposure_signal", "label": "supplier PII exposure signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier PII exposure signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_trace_coverage_pct_04(record):
    """Evaluate supplier trace coverage for control WP-0427-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-04", "metric": "supplier_trace_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-04", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-04", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-04", "metric": "supplier_trace_coverage_pct", "label": "supplier trace coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier trace coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_code_review_pct_05(record):
    """Evaluate supplier code review completeness for control WP-0427-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_code_review_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-05", "metric": "supplier_code_review_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-05", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-05", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-05", "metric": "supplier_code_review_pct", "label": "supplier code review completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier code review completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_offboarding_completion_pct_06(record):
    """Evaluate supplier offboarding completion for control WP-0427-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_offboarding_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-06", "metric": "supplier_offboarding_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-06", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-06", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-06", "metric": "supplier_offboarding_completion_pct", "label": "supplier offboarding completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier offboarding completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_purchase_split_signal_07(record):
    """Evaluate supplier purchase-splitting signal for control WP-0427-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_purchase_split_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-07", "metric": "supplier_purchase_split_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-07", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-07", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-07", "metric": "supplier_purchase_split_signal", "label": "supplier purchase-splitting signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier purchase-splitting signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_schedule_stability_pct_08(record):
    """Evaluate schedule stability for control WP-0427-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_stability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-08", "metric": "supplier_schedule_stability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-08", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-08", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-08", "metric": "supplier_schedule_stability_pct", "label": "schedule stability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "schedule stability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_pod_upload_age_hours_09(record):
    """Evaluate supplier POD upload age for control WP-0427-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pod_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-09", "metric": "supplier_pod_upload_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-09", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-09", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-09", "metric": "supplier_pod_upload_age_hours", "label": "supplier POD upload age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier POD upload age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_certificate_revocation_pct_10(record):
    """Evaluate supplier certificate revocation for control WP-0427-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-10", "metric": "supplier_certificate_revocation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-10", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-10", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-10", "metric": "supplier_certificate_revocation_pct", "label": "supplier certificate revocation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier certificate revocation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_pick_rate_11(record):
    """Evaluate picking rate for control WP-0427-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-11", "metric": "pick_rate",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lines/hour",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-11", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-11", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-11", "metric": "pick_rate", "label": "picking rate",
        "status": "breach", "severity": "medium", "unit": "lines/hour",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "picking rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_bin_distance_m_12(record):
    """Evaluate bin travel distance for control WP-0427-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bin_distance_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-12", "metric": "bin_distance_m",
            "status": "insufficient_data",
            "severity": "high", "unit": "meters",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-12", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-12", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-12", "metric": "bin_distance_m", "label": "bin travel distance",
        "status": "breach", "severity": "high", "unit": "meters",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "bin travel distance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_cycle_count_age_days_13(record):
    """Evaluate cycle-count age for control WP-0427-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-13", "metric": "cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-13", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-13", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-13", "metric": "cycle_count_age_days", "label": "cycle-count age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cycle-count age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_demand_spike_pct_14(record):
    """Evaluate demand spike for control WP-0427-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demand_spike_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-14", "metric": "demand_spike_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-14", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-14", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-14", "metric": "demand_spike_pct", "label": "demand spike",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "demand spike must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_route_on_time_pct_15(record):
    """Evaluate route on-time rate for control WP-0427-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_on_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-15", "metric": "route_on_time_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-15", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-15", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-15", "metric": "route_on_time_pct", "label": "route on-time rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "route on-time rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_failed_login_count_16(record):
    """Evaluate failed logins for control WP-0427-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_login_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-16", "metric": "failed_login_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-16", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-16", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-16", "metric": "failed_login_count", "label": "failed logins",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "failed logins falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_absence_rate_pct_17(record):
    """Evaluate absence rate for control WP-0427-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("absence_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-17", "metric": "absence_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-17", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-17", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-17", "metric": "absence_rate_pct", "label": "absence rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "absence rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_emergency_light_test_age_days_18(record):
    """Evaluate emergency-light test age for control WP-0427-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_light_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-18", "metric": "emergency_light_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-18", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-18", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-18", "metric": "emergency_light_test_age_days", "label": "emergency-light test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "emergency-light test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_signature_capture_pct_19(record):
    """Evaluate signature capture for control WP-0427-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("signature_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-19", "metric": "signature_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-19", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-19", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-19", "metric": "signature_capture_pct", "label": "signature capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "signature capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_chain_temperature_coverage_pct_20(record):
    """Evaluate temperature coverage for control WP-0427-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-20", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-20", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-20", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-20", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "temperature coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_replacement_stock_cover_days_21(record):
    """Evaluate replacement stock cover for control WP-0427-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-21", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-21", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-21", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-21", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replacement stock cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_fall_protection_compliance_pct_22(record):
    """Evaluate fall protection compliance for control WP-0427-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-22", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-22", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-22", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-22", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fall protection compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_control_room_access_gap_count_23(record):
    """Evaluate control-room access gaps for control WP-0427-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-23", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-23", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-23", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-23", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "control-room access gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_dns_failure_count_24(record):
    """Evaluate DNS failures for control WP-0427-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0427-24", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0427-24", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0427-24", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0427-24", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "DNS failures falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_audited_financial_age_days_01, assess_supplier_change_control_pct_02, assess_supplier_pii_exposure_signal_03, assess_supplier_trace_coverage_pct_04, assess_supplier_code_review_pct_05, assess_supplier_offboarding_completion_pct_06, assess_supplier_purchase_split_signal_07, assess_supplier_schedule_stability_pct_08, assess_supplier_pod_upload_age_hours_09, assess_supplier_certificate_revocation_pct_10, assess_pick_rate_11, assess_bin_distance_m_12, assess_cycle_count_age_days_13, assess_demand_spike_pct_14, assess_route_on_time_pct_15, assess_failed_login_count_16, assess_absence_rate_pct_17, assess_emergency_light_test_age_days_18, assess_signature_capture_pct_19, assess_chain_temperature_coverage_pct_20, assess_replacement_stock_cover_days_21, assess_fall_protection_compliance_pct_22, assess_control_room_access_gap_count_23, assess_dns_failure_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

