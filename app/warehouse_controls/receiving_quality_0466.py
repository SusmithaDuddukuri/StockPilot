"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_record_uniqueness_pct_01(record):
    """Evaluate record uniqueness for control WP-0466-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_uniqueness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-01", "metric": "record_uniqueness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-01", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-01", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-01", "metric": "record_uniqueness_pct", "label": "record uniqueness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "record uniqueness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_carrier_master_gap_count_02(record):
    """Evaluate carrier master gaps for control WP-0466-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-02", "metric": "carrier_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-02", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-02", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-02", "metric": "carrier_master_gap_count", "label": "carrier master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "carrier master gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_sourcing_switch_cost_03(record):
    """Evaluate sourcing switch cost for control WP-0466-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sourcing_switch_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-03", "metric": "sourcing_switch_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-03", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-03", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-03", "metric": "sourcing_switch_cost", "label": "sourcing switch cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "sourcing switch cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_delivery_scan_gap_count_04(record):
    """Evaluate delivery scan gaps for control WP-0466-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_scan_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-04", "metric": "delivery_scan_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-04", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-04", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-04", "metric": "delivery_scan_gap_count", "label": "delivery scan gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery scan gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_freight_payment_age_days_05(record):
    """Evaluate freight payment age for control WP-0466-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_payment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-05", "metric": "freight_payment_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-05", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-05", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-05", "metric": "freight_payment_age_days", "label": "freight payment age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "freight payment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_cargo_tamper_alert_count_06(record):
    """Evaluate cargo tamper alerts for control WP-0466-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cargo_tamper_alert_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-06", "metric": "cargo_tamper_alert_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-06", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-06", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-06", "metric": "cargo_tamper_alert_count", "label": "cargo tamper alerts",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "cargo tamper alerts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_dispute_count_07(record):
    """Evaluate supplier disputes for control WP-0466-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-07", "metric": "supplier_dispute_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-07", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-07", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-07", "metric": "supplier_dispute_count", "label": "supplier disputes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier disputes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_water_risk_score_08(record):
    """Evaluate supplier water risk for control WP-0466-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-08", "metric": "supplier_water_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-08", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-08", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-08", "metric": "supplier_water_risk_score", "label": "supplier water risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier water risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_mode_shift_pct_09(record):
    """Evaluate supplier mode shift for control WP-0466-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mode_shift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-09", "metric": "supplier_mode_shift_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-09", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-09", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-09", "metric": "supplier_mode_shift_pct", "label": "supplier mode shift",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier mode shift must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_policy_ack_pct_10(record):
    """Evaluate supplier policy acknowledgement for control WP-0466-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-10", "metric": "supplier_policy_ack_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-10", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-10", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-10", "metric": "supplier_policy_ack_pct", "label": "supplier policy acknowledgement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier policy acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_insolvency_signal_score_11(record):
    """Evaluate supplier insolvency signal for control WP-0466-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insolvency_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-11", "metric": "supplier_insolvency_signal_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-11", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-11", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-11", "metric": "supplier_insolvency_signal_score", "label": "supplier insolvency signal",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier insolvency signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_material_recovery_pct_12(record):
    """Evaluate supplier material recovery for control WP-0466-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_recovery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-12", "metric": "supplier_material_recovery_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-12", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-12", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-12", "metric": "supplier_material_recovery_pct", "label": "supplier material recovery",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier material recovery must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_capacity_visibility_pct_13(record):
    """Evaluate supplier capacity visibility for control WP-0466-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-13", "metric": "supplier_capacity_visibility_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-13", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-13", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-13", "metric": "supplier_capacity_visibility_pct", "label": "supplier capacity visibility",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity visibility must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_spc_compliance_pct_14(record):
    """Evaluate supplier SPC compliance for control WP-0466-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spc_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-14", "metric": "supplier_spc_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-14", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-14", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-14", "metric": "supplier_spc_compliance_pct", "label": "supplier SPC compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier SPC compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_occupational_exposure_gap_count_15(record):
    """Evaluate supplier occupational exposure gaps for control WP-0466-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_occupational_exposure_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-15", "metric": "supplier_occupational_exposure_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-15", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-15", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-15", "metric": "supplier_occupational_exposure_gap_count", "label": "supplier occupational exposure gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier occupational exposure gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_audited_financial_age_days_16(record):
    """Evaluate supplier audited-financial age for control WP-0466-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audited_financial_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-16", "metric": "supplier_audited_financial_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-16", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-16", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-16", "metric": "supplier_audited_financial_age_days", "label": "supplier audited-financial age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audited-financial age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_change_control_pct_17(record):
    """Evaluate supplier change control for control WP-0466-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-17", "metric": "supplier_change_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-17", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-17", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-17", "metric": "supplier_change_control_pct", "label": "supplier change control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier change control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_pii_exposure_signal_18(record):
    """Evaluate supplier PII exposure signal for control WP-0466-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pii_exposure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-18", "metric": "supplier_pii_exposure_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-18", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-18", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-18", "metric": "supplier_pii_exposure_signal", "label": "supplier PII exposure signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier PII exposure signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_trace_coverage_pct_19(record):
    """Evaluate supplier trace coverage for control WP-0466-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-19", "metric": "supplier_trace_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-19", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-19", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-19", "metric": "supplier_trace_coverage_pct", "label": "supplier trace coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier trace coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_code_review_pct_20(record):
    """Evaluate supplier code review completeness for control WP-0466-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_code_review_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-20", "metric": "supplier_code_review_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-20", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-20", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-20", "metric": "supplier_code_review_pct", "label": "supplier code review completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier code review completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_offboarding_completion_pct_21(record):
    """Evaluate supplier offboarding completion for control WP-0466-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_offboarding_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-21", "metric": "supplier_offboarding_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-21", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-21", "metric": "supplier_offboarding_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-21", "metric": "supplier_offboarding_completion_pct", "label": "supplier offboarding completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier offboarding completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_purchase_split_signal_22(record):
    """Evaluate supplier purchase-splitting signal for control WP-0466-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_purchase_split_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-22", "metric": "supplier_purchase_split_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-22", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-22", "metric": "supplier_purchase_split_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-22", "metric": "supplier_purchase_split_signal", "label": "supplier purchase-splitting signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier purchase-splitting signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_schedule_stability_pct_23(record):
    """Evaluate schedule stability for control WP-0466-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_stability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-23", "metric": "supplier_schedule_stability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-23", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-23", "metric": "supplier_schedule_stability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-23", "metric": "supplier_schedule_stability_pct", "label": "schedule stability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "schedule stability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_pod_upload_age_hours_24(record):
    """Evaluate supplier POD upload age for control WP-0466-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pod_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0466-24", "metric": "supplier_pod_upload_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0466-24", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0466-24", "metric": "supplier_pod_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0466-24", "metric": "supplier_pod_upload_age_hours", "label": "supplier POD upload age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier POD upload age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_record_uniqueness_pct_01, assess_carrier_master_gap_count_02, assess_sourcing_switch_cost_03, assess_delivery_scan_gap_count_04, assess_freight_payment_age_days_05, assess_cargo_tamper_alert_count_06, assess_supplier_dispute_count_07, assess_supplier_water_risk_score_08, assess_supplier_mode_shift_pct_09, assess_supplier_policy_ack_pct_10, assess_supplier_insolvency_signal_score_11, assess_supplier_material_recovery_pct_12, assess_supplier_capacity_visibility_pct_13, assess_supplier_spc_compliance_pct_14, assess_supplier_occupational_exposure_gap_count_15, assess_supplier_audited_financial_age_days_16, assess_supplier_change_control_pct_17, assess_supplier_pii_exposure_signal_18, assess_supplier_trace_coverage_pct_19, assess_supplier_code_review_pct_20, assess_supplier_offboarding_completion_pct_21, assess_supplier_purchase_split_signal_22, assess_supplier_schedule_stability_pct_23, assess_supplier_pod_upload_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

