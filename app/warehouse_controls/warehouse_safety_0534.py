"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_delivery_scan_gap_count_01(record):
    """Evaluate delivery scan gaps for control WP-0534-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_scan_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-01", "metric": "delivery_scan_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-01", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-01", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-01", "metric": "delivery_scan_gap_count", "label": "delivery scan gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "delivery scan gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_freight_payment_age_days_02(record):
    """Evaluate freight payment age for control WP-0534-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_payment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-02", "metric": "freight_payment_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-02", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-02", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-02", "metric": "freight_payment_age_days", "label": "freight payment age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "freight payment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_cargo_tamper_alert_count_03(record):
    """Evaluate cargo tamper alerts for control WP-0534-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cargo_tamper_alert_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-03", "metric": "cargo_tamper_alert_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-03", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-03", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-03", "metric": "cargo_tamper_alert_count", "label": "cargo tamper alerts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "cargo tamper alerts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_dispute_count_04(record):
    """Evaluate supplier disputes for control WP-0534-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-04", "metric": "supplier_dispute_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-04", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-04", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-04", "metric": "supplier_dispute_count", "label": "supplier disputes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disputes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_water_risk_score_05(record):
    """Evaluate supplier water risk for control WP-0534-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-05", "metric": "supplier_water_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-05", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-05", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-05", "metric": "supplier_water_risk_score", "label": "supplier water risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier water risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_mode_shift_pct_06(record):
    """Evaluate supplier mode shift for control WP-0534-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mode_shift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-06", "metric": "supplier_mode_shift_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-06", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-06", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-06", "metric": "supplier_mode_shift_pct", "label": "supplier mode shift",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier mode shift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_policy_ack_pct_07(record):
    """Evaluate supplier policy acknowledgement for control WP-0534-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-07", "metric": "supplier_policy_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-07", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-07", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-07", "metric": "supplier_policy_ack_pct", "label": "supplier policy acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier policy acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_insolvency_signal_score_08(record):
    """Evaluate supplier insolvency signal for control WP-0534-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insolvency_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-08", "metric": "supplier_insolvency_signal_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-08", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-08", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-08", "metric": "supplier_insolvency_signal_score", "label": "supplier insolvency signal",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier insolvency signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_material_recovery_pct_09(record):
    """Evaluate supplier material recovery for control WP-0534-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_recovery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-09", "metric": "supplier_material_recovery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-09", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-09", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-09", "metric": "supplier_material_recovery_pct", "label": "supplier material recovery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier material recovery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_capacity_visibility_pct_10(record):
    """Evaluate supplier capacity visibility for control WP-0534-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-10", "metric": "supplier_capacity_visibility_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-10", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-10", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-10", "metric": "supplier_capacity_visibility_pct", "label": "supplier capacity visibility",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier capacity visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_spc_compliance_pct_11(record):
    """Evaluate supplier SPC compliance for control WP-0534-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spc_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-11", "metric": "supplier_spc_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-11", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-11", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-11", "metric": "supplier_spc_compliance_pct", "label": "supplier SPC compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier SPC compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_occupational_exposure_gap_count_12(record):
    """Evaluate supplier occupational exposure gaps for control WP-0534-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_occupational_exposure_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-12", "metric": "supplier_occupational_exposure_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-12", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-12", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-12", "metric": "supplier_occupational_exposure_gap_count", "label": "supplier occupational exposure gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier occupational exposure gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_audited_financial_age_days_13(record):
    """Evaluate supplier audited-financial age for control WP-0534-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audited_financial_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-13", "metric": "supplier_audited_financial_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-13", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-13", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-13", "metric": "supplier_audited_financial_age_days", "label": "supplier audited-financial age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier audited-financial age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_change_control_pct_14(record):
    """Evaluate supplier change control for control WP-0534-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-14", "metric": "supplier_change_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-14", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-14", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-14", "metric": "supplier_change_control_pct", "label": "supplier change control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier change control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_pii_exposure_signal_15(record):
    """Evaluate supplier PII exposure signal for control WP-0534-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pii_exposure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-15", "metric": "supplier_pii_exposure_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-15", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-15", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-15", "metric": "supplier_pii_exposure_signal", "label": "supplier PII exposure signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier PII exposure signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_trace_coverage_pct_16(record):
    """Evaluate supplier trace coverage for control WP-0534-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-16", "metric": "supplier_trace_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-16", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-16", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-16", "metric": "supplier_trace_coverage_pct", "label": "supplier trace coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier trace coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_code_review_pct_17(record):
    """Evaluate supplier code review completeness for control WP-0534-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_code_review_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-17", "metric": "supplier_code_review_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-17", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-17", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-17", "metric": "supplier_code_review_pct", "label": "supplier code review completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier code review completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_offboarding_completion_pct_18(record):
    """Evaluate supplier offboarding completion for control WP-0534-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_offboarding_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-18", "metric": "supplier_offboarding_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-18", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-18", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-18", "metric": "supplier_offboarding_completion_pct", "label": "supplier offboarding completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier offboarding completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_purchase_split_signal_19(record):
    """Evaluate supplier purchase-splitting signal for control WP-0534-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_purchase_split_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-19", "metric": "supplier_purchase_split_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-19", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-19", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-19", "metric": "supplier_purchase_split_signal", "label": "supplier purchase-splitting signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier purchase-splitting signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_schedule_stability_pct_20(record):
    """Evaluate schedule stability for control WP-0534-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_stability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-20", "metric": "supplier_schedule_stability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-20", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-20", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-20", "metric": "supplier_schedule_stability_pct", "label": "schedule stability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "schedule stability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_pod_upload_age_hours_21(record):
    """Evaluate supplier POD upload age for control WP-0534-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pod_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-21", "metric": "supplier_pod_upload_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-21", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-21", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-21", "metric": "supplier_pod_upload_age_hours", "label": "supplier POD upload age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier POD upload age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_certificate_revocation_pct_22(record):
    """Evaluate supplier certificate revocation for control WP-0534-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-22", "metric": "supplier_certificate_revocation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-22", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-22", "metric": "supplier_certificate_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-22", "metric": "supplier_certificate_revocation_pct", "label": "supplier certificate revocation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "supplier certificate revocation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_pick_rate_23(record):
    """Evaluate picking rate for control WP-0534-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-23", "metric": "pick_rate",
            "status": "insufficient_data",
            "severity": "low", "unit": "lines/hour",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-23", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-23", "metric": "pick_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-23", "metric": "pick_rate", "label": "picking rate",
        "status": "breach", "severity": "low", "unit": "lines/hour",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "picking rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_bin_distance_m_24(record):
    """Evaluate bin travel distance for control WP-0534-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bin_distance_m")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0534-24", "metric": "bin_distance_m",
            "status": "insufficient_data",
            "severity": "medium", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0534-24", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0534-24", "metric": "bin_distance_m", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0534-24", "metric": "bin_distance_m", "label": "bin travel distance",
        "status": "breach", "severity": "medium", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "bin travel distance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_delivery_scan_gap_count_01, assess_freight_payment_age_days_02, assess_cargo_tamper_alert_count_03, assess_supplier_dispute_count_04, assess_supplier_water_risk_score_05, assess_supplier_mode_shift_pct_06, assess_supplier_policy_ack_pct_07, assess_supplier_insolvency_signal_score_08, assess_supplier_material_recovery_pct_09, assess_supplier_capacity_visibility_pct_10, assess_supplier_spc_compliance_pct_11, assess_supplier_occupational_exposure_gap_count_12, assess_supplier_audited_financial_age_days_13, assess_supplier_change_control_pct_14, assess_supplier_pii_exposure_signal_15, assess_supplier_trace_coverage_pct_16, assess_supplier_code_review_pct_17, assess_supplier_offboarding_completion_pct_18, assess_supplier_purchase_split_signal_19, assess_supplier_schedule_stability_pct_20, assess_supplier_pod_upload_age_hours_21, assess_supplier_certificate_revocation_pct_22, assess_pick_rate_23, assess_bin_distance_m_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

