"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_vault_access_review_age_days_01(record):
    """Evaluate vault access review age for control WP-0143-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vault_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-01", "metric": "vault_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-01", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-01", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-01", "metric": "vault_access_review_age_days", "label": "vault access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vault access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_sds_access_pct_02(record):
    """Evaluate SDS access completeness for control WP-0143-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sds_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-02", "metric": "sds_access_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-02", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-02", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-02", "metric": "sds_access_pct", "label": "SDS access completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "SDS access completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_planned_maintenance_pct_03(record):
    """Evaluate planned maintenance share for control WP-0143-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("planned_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-03", "metric": "planned_maintenance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-03", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-03", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-03", "metric": "planned_maintenance_pct", "label": "planned maintenance share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "planned maintenance share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_service_availability_pct_04(record):
    """Evaluate service availability for control WP-0143-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-04", "metric": "service_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-04", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-04", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-04", "metric": "service_availability_pct", "label": "service availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "service availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_record_uniqueness_pct_05(record):
    """Evaluate record uniqueness for control WP-0143-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_uniqueness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-05", "metric": "record_uniqueness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-05", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-05", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-05", "metric": "record_uniqueness_pct", "label": "record uniqueness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "record uniqueness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_carrier_master_gap_count_06(record):
    """Evaluate carrier master gaps for control WP-0143-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-06", "metric": "carrier_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-06", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-06", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-06", "metric": "carrier_master_gap_count", "label": "carrier master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carrier master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_sourcing_switch_cost_07(record):
    """Evaluate sourcing switch cost for control WP-0143-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sourcing_switch_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-07", "metric": "sourcing_switch_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-07", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-07", "metric": "sourcing_switch_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-07", "metric": "sourcing_switch_cost", "label": "sourcing switch cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "sourcing switch cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_delivery_scan_gap_count_08(record):
    """Evaluate delivery scan gaps for control WP-0143-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_scan_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-08", "metric": "delivery_scan_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-08", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-08", "metric": "delivery_scan_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-08", "metric": "delivery_scan_gap_count", "label": "delivery scan gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "delivery scan gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_freight_payment_age_days_09(record):
    """Evaluate freight payment age for control WP-0143-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_payment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-09", "metric": "freight_payment_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-09", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-09", "metric": "freight_payment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-09", "metric": "freight_payment_age_days", "label": "freight payment age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "freight payment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_cargo_tamper_alert_count_10(record):
    """Evaluate cargo tamper alerts for control WP-0143-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cargo_tamper_alert_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-10", "metric": "cargo_tamper_alert_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-10", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-10", "metric": "cargo_tamper_alert_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-10", "metric": "cargo_tamper_alert_count", "label": "cargo tamper alerts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cargo tamper alerts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_dispute_count_11(record):
    """Evaluate supplier disputes for control WP-0143-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-11", "metric": "supplier_dispute_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-11", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-11", "metric": "supplier_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-11", "metric": "supplier_dispute_count", "label": "supplier disputes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier disputes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_water_risk_score_12(record):
    """Evaluate supplier water risk for control WP-0143-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_water_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-12", "metric": "supplier_water_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-12", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-12", "metric": "supplier_water_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-12", "metric": "supplier_water_risk_score", "label": "supplier water risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier water risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_mode_shift_pct_13(record):
    """Evaluate supplier mode shift for control WP-0143-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mode_shift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-13", "metric": "supplier_mode_shift_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-13", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-13", "metric": "supplier_mode_shift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-13", "metric": "supplier_mode_shift_pct", "label": "supplier mode shift",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier mode shift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_policy_ack_pct_14(record):
    """Evaluate supplier policy acknowledgement for control WP-0143-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-14", "metric": "supplier_policy_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-14", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-14", "metric": "supplier_policy_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-14", "metric": "supplier_policy_ack_pct", "label": "supplier policy acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier policy acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_insolvency_signal_score_15(record):
    """Evaluate supplier insolvency signal for control WP-0143-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insolvency_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-15", "metric": "supplier_insolvency_signal_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-15", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-15", "metric": "supplier_insolvency_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-15", "metric": "supplier_insolvency_signal_score", "label": "supplier insolvency signal",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier insolvency signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_material_recovery_pct_16(record):
    """Evaluate supplier material recovery for control WP-0143-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_recovery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-16", "metric": "supplier_material_recovery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-16", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-16", "metric": "supplier_material_recovery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-16", "metric": "supplier_material_recovery_pct", "label": "supplier material recovery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier material recovery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_capacity_visibility_pct_17(record):
    """Evaluate supplier capacity visibility for control WP-0143-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-17", "metric": "supplier_capacity_visibility_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-17", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-17", "metric": "supplier_capacity_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-17", "metric": "supplier_capacity_visibility_pct", "label": "supplier capacity visibility",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_spc_compliance_pct_18(record):
    """Evaluate supplier SPC compliance for control WP-0143-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spc_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-18", "metric": "supplier_spc_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-18", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-18", "metric": "supplier_spc_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-18", "metric": "supplier_spc_compliance_pct", "label": "supplier SPC compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SPC compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_occupational_exposure_gap_count_19(record):
    """Evaluate supplier occupational exposure gaps for control WP-0143-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_occupational_exposure_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-19", "metric": "supplier_occupational_exposure_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-19", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-19", "metric": "supplier_occupational_exposure_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-19", "metric": "supplier_occupational_exposure_gap_count", "label": "supplier occupational exposure gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier occupational exposure gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_audited_financial_age_days_20(record):
    """Evaluate supplier audited-financial age for control WP-0143-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audited_financial_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-20", "metric": "supplier_audited_financial_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-20", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-20", "metric": "supplier_audited_financial_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-20", "metric": "supplier_audited_financial_age_days", "label": "supplier audited-financial age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier audited-financial age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_change_control_pct_21(record):
    """Evaluate supplier change control for control WP-0143-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-21", "metric": "supplier_change_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-21", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-21", "metric": "supplier_change_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-21", "metric": "supplier_change_control_pct", "label": "supplier change control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier change control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_pii_exposure_signal_22(record):
    """Evaluate supplier PII exposure signal for control WP-0143-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pii_exposure_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-22", "metric": "supplier_pii_exposure_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-22", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-22", "metric": "supplier_pii_exposure_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-22", "metric": "supplier_pii_exposure_signal", "label": "supplier PII exposure signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier PII exposure signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_trace_coverage_pct_23(record):
    """Evaluate supplier trace coverage for control WP-0143-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-23", "metric": "supplier_trace_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-23", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-23", "metric": "supplier_trace_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-23", "metric": "supplier_trace_coverage_pct", "label": "supplier trace coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "supplier trace coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_code_review_pct_24(record):
    """Evaluate supplier code review completeness for control WP-0143-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_code_review_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0143-24", "metric": "supplier_code_review_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0143-24", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0143-24", "metric": "supplier_code_review_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0143-24", "metric": "supplier_code_review_pct", "label": "supplier code review completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier code review completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_vault_access_review_age_days_01, assess_sds_access_pct_02, assess_planned_maintenance_pct_03, assess_service_availability_pct_04, assess_record_uniqueness_pct_05, assess_carrier_master_gap_count_06, assess_sourcing_switch_cost_07, assess_delivery_scan_gap_count_08, assess_freight_payment_age_days_09, assess_cargo_tamper_alert_count_10, assess_supplier_dispute_count_11, assess_supplier_water_risk_score_12, assess_supplier_mode_shift_pct_13, assess_supplier_policy_ack_pct_14, assess_supplier_insolvency_signal_score_15, assess_supplier_material_recovery_pct_16, assess_supplier_capacity_visibility_pct_17, assess_supplier_spc_compliance_pct_18, assess_supplier_occupational_exposure_gap_count_19, assess_supplier_audited_financial_age_days_20, assess_supplier_change_control_pct_21, assess_supplier_pii_exposure_signal_22, assess_supplier_trace_coverage_pct_23, assess_supplier_code_review_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

