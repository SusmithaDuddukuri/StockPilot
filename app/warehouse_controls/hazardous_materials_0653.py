"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_automation_manual_override_count_01(record):
    """Evaluate manual overrides for control WP-0653-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-01", "metric": "automation_manual_override_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-01", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-01", "metric": "automation_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-01", "metric": "automation_manual_override_count", "label": "manual overrides",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "manual overrides exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_clock_drift_seconds_02(record):
    """Evaluate clock drift for control WP-0653-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("clock_drift_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-02", "metric": "clock_drift_seconds",
            "status": "insufficient_data",
            "severity": "high", "unit": "seconds",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-02", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-02", "metric": "clock_drift_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-02", "metric": "clock_drift_seconds", "label": "clock drift",
        "status": "breach", "severity": "high", "unit": "seconds",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "clock drift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_lost_device_count_03(record):
    """Evaluate lost devices for control WP-0653-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lost_device_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-03", "metric": "lost_device_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "devices",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-03", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-03", "metric": "lost_device_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-03", "metric": "lost_device_count", "label": "lost devices",
        "status": "breach", "severity": "critical", "unit": "devices",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lost devices must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_receipt_duplicate_count_04(record):
    """Evaluate duplicate receipts for control WP-0653-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receipt_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-04", "metric": "receipt_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "receipts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-04", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-04", "metric": "receipt_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-04", "metric": "receipt_duplicate_count", "label": "duplicate receipts",
        "status": "breach", "severity": "low", "unit": "receipts",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate receipts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_replenishment_success_pct_05(record):
    """Evaluate replenishment success for control WP-0653-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-05", "metric": "replenishment_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-05", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-05", "metric": "replenishment_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-05", "metric": "replenishment_success_pct", "label": "replenishment success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "replenishment success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_payment_reconciliation_age_hours_06(record):
    """Evaluate payment reconciliation age for control WP-0653-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-06", "metric": "payment_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-06", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-06", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-06", "metric": "payment_reconciliation_age_hours", "label": "payment reconciliation age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "payment reconciliation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_trailer_location_age_minutes_07(record):
    """Evaluate trailer location age for control WP-0653-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_location_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-07", "metric": "trailer_location_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-07", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-07", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-07", "metric": "trailer_location_age_minutes", "label": "trailer location age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trailer location age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_damage_cost_monthly_08(record):
    """Evaluate monthly damage cost for control WP-0653-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_cost_monthly")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-08", "metric": "damage_cost_monthly",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-08", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-08", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-08", "metric": "damage_cost_monthly", "label": "monthly damage cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "monthly damage cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_short_ship_pct_09(record):
    """Evaluate supplier short-ship rate for control WP-0653-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_short_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-09", "metric": "supplier_short_ship_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-09", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-09", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-09", "metric": "supplier_short_ship_pct", "label": "supplier short-ship rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier short-ship rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_asn_timeliness_pct_10(record):
    """Evaluate supplier ASN timeliness for control WP-0653-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-10", "metric": "supplier_asn_timeliness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-10", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-10", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-10", "metric": "supplier_asn_timeliness_pct", "label": "supplier ASN timeliness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier ASN timeliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_demand_signal_age_hours_11(record):
    """Evaluate supplier demand signal age for control WP-0653-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_demand_signal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-11", "metric": "supplier_demand_signal_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-11", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-11", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-11", "metric": "supplier_demand_signal_age_hours", "label": "supplier demand signal age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier demand signal age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_business_owner_gap_count_12(record):
    """Evaluate supplier business-owner gaps for control WP-0653-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-12", "metric": "supplier_business_owner_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-12", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-12", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-12", "metric": "supplier_business_owner_gap_count", "label": "supplier business-owner gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier business-owner gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_recall_response_minutes_13(record):
    """Evaluate supplier recall response time for control WP-0653-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recall_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-13", "metric": "supplier_recall_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-13", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-13", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-13", "metric": "supplier_recall_response_minutes", "label": "supplier recall response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "supplier recall response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_seismic_risk_score_14(record):
    """Evaluate supplier seismic risk for control WP-0653-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seismic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-14", "metric": "supplier_seismic_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-14", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-14", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-14", "metric": "supplier_seismic_risk_score", "label": "supplier seismic risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "supplier seismic risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_tooling_transfer_days_15(record):
    """Evaluate supplier tooling transfer time for control WP-0653-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-15", "metric": "supplier_tooling_transfer_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-15", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-15", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-15", "metric": "supplier_tooling_transfer_days", "label": "supplier tooling transfer time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tooling transfer time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_certification_scope_gap_count_16(record):
    """Evaluate supplier certification scope gaps for control WP-0653-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_scope_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-16", "metric": "supplier_certification_scope_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-16", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-16", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-16", "metric": "supplier_certification_scope_gap_count", "label": "supplier certification scope gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier certification scope gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_gift_register_gap_count_17(record):
    """Evaluate supplier gift-register gaps for control WP-0653-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gift_register_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-17", "metric": "supplier_gift_register_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-17", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-17", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-17", "metric": "supplier_gift_register_gap_count", "label": "supplier gift-register gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier gift-register gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_bcp_contact_age_days_18(record):
    """Evaluate supplier BCP contact age for control WP-0653-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-18", "metric": "supplier_bcp_contact_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-18", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-18", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-18", "metric": "supplier_bcp_contact_age_days", "label": "supplier BCP contact age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier BCP contact age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_automation_coverage_pct_19(record):
    """Evaluate supplier automation coverage for control WP-0653-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_automation_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-19", "metric": "supplier_automation_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-19", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-19", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-19", "metric": "supplier_automation_coverage_pct", "label": "supplier automation coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier automation coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_human_review_queue_age_hours_20(record):
    """Evaluate supplier human review queue age for control WP-0653-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_review_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-20", "metric": "supplier_human_review_queue_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-20", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-20", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-20", "metric": "supplier_human_review_queue_age_hours", "label": "supplier human review queue age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier human review queue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_failover_test_age_days_21(record):
    """Evaluate supplier failover test age for control WP-0653-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_failover_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-21", "metric": "supplier_failover_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-21", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-21", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-21", "metric": "supplier_failover_test_age_days", "label": "supplier failover test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier failover test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_subprocessor_notice_pct_22(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0653-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-22", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-22", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-22", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-22", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier subprocessor notice compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_kri_breach_count_23(record):
    """Evaluate supplier KRI breaches for control WP-0653-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-23", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-23", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-23", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-23", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier KRI breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_po_after_invoice_count_24(record):
    """Evaluate PO-after-invoice events for control WP-0653-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0653-24", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0653-24", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0653-24", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0653-24", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "PO-after-invoice events must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_automation_manual_override_count_01, assess_clock_drift_seconds_02, assess_lost_device_count_03, assess_receipt_duplicate_count_04, assess_replenishment_success_pct_05, assess_payment_reconciliation_age_hours_06, assess_trailer_location_age_minutes_07, assess_damage_cost_monthly_08, assess_supplier_short_ship_pct_09, assess_supplier_asn_timeliness_pct_10, assess_supplier_demand_signal_age_hours_11, assess_supplier_business_owner_gap_count_12, assess_supplier_recall_response_minutes_13, assess_supplier_seismic_risk_score_14, assess_supplier_tooling_transfer_days_15, assess_supplier_certification_scope_gap_count_16, assess_supplier_gift_register_gap_count_17, assess_supplier_bcp_contact_age_days_18, assess_supplier_automation_coverage_pct_19, assess_supplier_human_review_queue_age_hours_20, assess_supplier_failover_test_age_days_21, assess_supplier_subprocessor_notice_pct_22, assess_supplier_kri_breach_count_23, assess_supplier_po_after_invoice_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

