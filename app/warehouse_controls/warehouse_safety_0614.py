"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_spc_compliance_pct_01(record):
    """Evaluate supplier SPC compliance for control WP-0614-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spc_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-01", "metric": "supplier_spc_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-01", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-01", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-01", "metric": "supplier_spc_compliance_pct", "label": "supplier SPC compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SPC compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_occupational_exposure_gap_count_02(record):
    """Evaluate supplier occupational exposure gaps for control WP-0614-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_occupational_exposure_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-02", "metric": "supplier_occupational_exposure_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-02", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-02", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-02", "metric": "supplier_occupational_exposure_gap_count", "label": "supplier occupational exposure gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier occupational exposure gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_audited_financial_age_days_03(record):
    """Evaluate supplier audited-financial age for control WP-0614-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audited_financial_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-03", "metric": "supplier_audited_financial_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-03", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-03", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-03", "metric": "supplier_audited_financial_age_days", "label": "supplier audited-financial age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier audited-financial age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_change_control_pct_04(record):
    """Evaluate supplier change control for control WP-0614-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-04", "metric": "supplier_change_control_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-04", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-04", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-04", "metric": "supplier_change_control_pct", "label": "supplier change control",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier change control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_pii_exposure_signal_05(record):
    """Evaluate supplier PII exposure signal for control WP-0614-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pii_exposure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-05", "metric": "supplier_pii_exposure_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-05", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-05", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-05", "metric": "supplier_pii_exposure_signal", "label": "supplier PII exposure signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier PII exposure signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_trace_coverage_pct_06(record):
    """Evaluate supplier trace coverage for control WP-0614-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-06", "metric": "supplier_trace_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-06", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-06", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-06", "metric": "supplier_trace_coverage_pct", "label": "supplier trace coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier trace coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_code_review_pct_07(record):
    """Evaluate supplier code review completeness for control WP-0614-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_code_review_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-07", "metric": "supplier_code_review_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-07", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-07", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-07", "metric": "supplier_code_review_pct", "label": "supplier code review completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "supplier code review completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_offboarding_completion_pct_08(record):
    """Evaluate supplier offboarding completion for control WP-0614-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_offboarding_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-08", "metric": "supplier_offboarding_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-08", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-08", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-08", "metric": "supplier_offboarding_completion_pct", "label": "supplier offboarding completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier offboarding completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_purchase_split_signal_09(record):
    """Evaluate supplier purchase-splitting signal for control WP-0614-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_purchase_split_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-09", "metric": "supplier_purchase_split_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-09", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-09", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-09", "metric": "supplier_purchase_split_signal", "label": "supplier purchase-splitting signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier purchase-splitting signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_schedule_stability_pct_10(record):
    """Evaluate schedule stability for control WP-0614-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_stability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-10", "metric": "supplier_schedule_stability_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-10", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-10", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-10", "metric": "supplier_schedule_stability_pct", "label": "schedule stability",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "schedule stability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_pod_upload_age_hours_11(record):
    """Evaluate supplier POD upload age for control WP-0614-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pod_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-11", "metric": "supplier_pod_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-11", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-11", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-11", "metric": "supplier_pod_upload_age_hours", "label": "supplier POD upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier POD upload age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_certificate_revocation_pct_12(record):
    """Evaluate supplier certificate revocation for control WP-0614-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-12", "metric": "supplier_certificate_revocation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-12", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-12", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-12", "metric": "supplier_certificate_revocation_pct", "label": "supplier certificate revocation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier certificate revocation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_pick_rate_13(record):
    """Evaluate picking rate for control WP-0614-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-13", "metric": "pick_rate",
            "status": "insufficient_data",
            "severity": "high", "unit": "lines/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-13", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-13", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-13", "metric": "pick_rate", "label": "picking rate",
        "status": "breach", "severity": "high", "unit": "lines/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "picking rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_bin_distance_m_14(record):
    """Evaluate bin travel distance for control WP-0614-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bin_distance_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-14", "metric": "bin_distance_m",
            "status": "insufficient_data",
            "severity": "critical", "unit": "meters",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-14", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-14", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-14", "metric": "bin_distance_m", "label": "bin travel distance",
        "status": "breach", "severity": "critical", "unit": "meters",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "bin travel distance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_cycle_count_age_days_15(record):
    """Evaluate cycle-count age for control WP-0614-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-15", "metric": "cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-15", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-15", "metric": "cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-15", "metric": "cycle_count_age_days", "label": "cycle-count age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "cycle-count age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_demand_spike_pct_16(record):
    """Evaluate demand spike for control WP-0614-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demand_spike_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-16", "metric": "demand_spike_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-16", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-16", "metric": "demand_spike_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-16", "metric": "demand_spike_pct", "label": "demand spike",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "demand spike must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_route_on_time_pct_17(record):
    """Evaluate route on-time rate for control WP-0614-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_on_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-17", "metric": "route_on_time_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-17", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-17", "metric": "route_on_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-17", "metric": "route_on_time_pct", "label": "route on-time rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route on-time rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_failed_login_count_18(record):
    """Evaluate failed logins for control WP-0614-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_login_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-18", "metric": "failed_login_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-18", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-18", "metric": "failed_login_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-18", "metric": "failed_login_count", "label": "failed logins",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "failed logins exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_absence_rate_pct_19(record):
    """Evaluate absence rate for control WP-0614-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("absence_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-19", "metric": "absence_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-19", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-19", "metric": "absence_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-19", "metric": "absence_rate_pct", "label": "absence rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "absence rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_emergency_light_test_age_days_20(record):
    """Evaluate emergency-light test age for control WP-0614-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_light_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-20", "metric": "emergency_light_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-20", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-20", "metric": "emergency_light_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-20", "metric": "emergency_light_test_age_days", "label": "emergency-light test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "emergency-light test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_signature_capture_pct_21(record):
    """Evaluate signature capture for control WP-0614-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("signature_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-21", "metric": "signature_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-21", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-21", "metric": "signature_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-21", "metric": "signature_capture_pct", "label": "signature capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "signature capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_chain_temperature_coverage_pct_22(record):
    """Evaluate temperature coverage for control WP-0614-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-22", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-22", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-22", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-22", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "temperature coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_replacement_stock_cover_days_23(record):
    """Evaluate replacement stock cover for control WP-0614-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-23", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-23", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-23", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-23", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "replacement stock cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_fall_protection_compliance_pct_24(record):
    """Evaluate fall protection compliance for control WP-0614-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0614-24", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0614-24", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0614-24", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0614-24", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fall protection compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_supplier_spc_compliance_pct_01, assess_supplier_occupational_exposure_gap_count_02, assess_supplier_audited_financial_age_days_03, assess_supplier_change_control_pct_04, assess_supplier_pii_exposure_signal_05, assess_supplier_trace_coverage_pct_06, assess_supplier_code_review_pct_07, assess_supplier_offboarding_completion_pct_08, assess_supplier_purchase_split_signal_09, assess_supplier_schedule_stability_pct_10, assess_supplier_pod_upload_age_hours_11, assess_supplier_certificate_revocation_pct_12, assess_pick_rate_13, assess_bin_distance_m_14, assess_cycle_count_age_days_15, assess_demand_spike_pct_16, assess_route_on_time_pct_17, assess_failed_login_count_18, assess_absence_rate_pct_19, assess_emergency_light_test_age_days_20, assess_signature_capture_pct_21, assess_chain_temperature_coverage_pct_22, assess_replacement_stock_cover_days_23, assess_fall_protection_compliance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

