"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_payment_reconciliation_age_hours_01(record):
    """Evaluate payment reconciliation age for control WP-0155-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-01", "metric": "payment_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-01", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-01", "metric": "payment_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-01", "metric": "payment_reconciliation_age_hours", "label": "payment reconciliation age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment reconciliation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_trailer_location_age_minutes_02(record):
    """Evaluate trailer location age for control WP-0155-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_location_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-02", "metric": "trailer_location_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-02", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-02", "metric": "trailer_location_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-02", "metric": "trailer_location_age_minutes", "label": "trailer location age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trailer location age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_damage_cost_monthly_03(record):
    """Evaluate monthly damage cost for control WP-0155-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_cost_monthly")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-03", "metric": "damage_cost_monthly",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-03", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-03", "metric": "damage_cost_monthly", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-03", "metric": "damage_cost_monthly", "label": "monthly damage cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "monthly damage cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_short_ship_pct_04(record):
    """Evaluate supplier short-ship rate for control WP-0155-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_short_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-04", "metric": "supplier_short_ship_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-04", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-04", "metric": "supplier_short_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-04", "metric": "supplier_short_ship_pct", "label": "supplier short-ship rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier short-ship rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_asn_timeliness_pct_05(record):
    """Evaluate supplier ASN timeliness for control WP-0155-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-05", "metric": "supplier_asn_timeliness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-05", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-05", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-05", "metric": "supplier_asn_timeliness_pct", "label": "supplier ASN timeliness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ASN timeliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_demand_signal_age_hours_06(record):
    """Evaluate supplier demand signal age for control WP-0155-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_demand_signal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-06", "metric": "supplier_demand_signal_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-06", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-06", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-06", "metric": "supplier_demand_signal_age_hours", "label": "supplier demand signal age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier demand signal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_business_owner_gap_count_07(record):
    """Evaluate supplier business-owner gaps for control WP-0155-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-07", "metric": "supplier_business_owner_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-07", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-07", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-07", "metric": "supplier_business_owner_gap_count", "label": "supplier business-owner gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier business-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_recall_response_minutes_08(record):
    """Evaluate supplier recall response time for control WP-0155-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recall_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-08", "metric": "supplier_recall_response_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-08", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-08", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-08", "metric": "supplier_recall_response_minutes", "label": "supplier recall response time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier recall response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_seismic_risk_score_09(record):
    """Evaluate supplier seismic risk for control WP-0155-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seismic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-09", "metric": "supplier_seismic_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-09", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-09", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-09", "metric": "supplier_seismic_risk_score", "label": "supplier seismic risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier seismic risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tooling_transfer_days_10(record):
    """Evaluate supplier tooling transfer time for control WP-0155-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-10", "metric": "supplier_tooling_transfer_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-10", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-10", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-10", "metric": "supplier_tooling_transfer_days", "label": "supplier tooling transfer time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tooling transfer time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_certification_scope_gap_count_11(record):
    """Evaluate supplier certification scope gaps for control WP-0155-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_scope_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-11", "metric": "supplier_certification_scope_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-11", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-11", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-11", "metric": "supplier_certification_scope_gap_count", "label": "supplier certification scope gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier certification scope gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_gift_register_gap_count_12(record):
    """Evaluate supplier gift-register gaps for control WP-0155-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gift_register_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-12", "metric": "supplier_gift_register_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-12", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-12", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-12", "metric": "supplier_gift_register_gap_count", "label": "supplier gift-register gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier gift-register gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_bcp_contact_age_days_13(record):
    """Evaluate supplier BCP contact age for control WP-0155-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-13", "metric": "supplier_bcp_contact_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-13", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-13", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-13", "metric": "supplier_bcp_contact_age_days", "label": "supplier BCP contact age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier BCP contact age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_automation_coverage_pct_14(record):
    """Evaluate supplier automation coverage for control WP-0155-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_automation_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-14", "metric": "supplier_automation_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-14", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-14", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-14", "metric": "supplier_automation_coverage_pct", "label": "supplier automation coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier automation coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_human_review_queue_age_hours_15(record):
    """Evaluate supplier human review queue age for control WP-0155-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_review_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-15", "metric": "supplier_human_review_queue_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-15", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-15", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-15", "metric": "supplier_human_review_queue_age_hours", "label": "supplier human review queue age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "supplier human review queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_failover_test_age_days_16(record):
    """Evaluate supplier failover test age for control WP-0155-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_failover_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-16", "metric": "supplier_failover_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-16", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-16", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-16", "metric": "supplier_failover_test_age_days", "label": "supplier failover test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier failover test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_subprocessor_notice_pct_17(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0155-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-17", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-17", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-17", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-17", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier subprocessor notice compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_kri_breach_count_18(record):
    """Evaluate supplier KRI breaches for control WP-0155-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-18", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-18", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-18", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-18", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KRI breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_po_after_invoice_count_19(record):
    """Evaluate PO-after-invoice events for control WP-0155-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-19", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-19", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-19", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-19", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "PO-after-invoice events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tool_changeover_minutes_20(record):
    """Evaluate supplier tool changeover for control WP-0155-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tool_changeover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-20", "metric": "supplier_tool_changeover_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-20", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-20", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-20", "metric": "supplier_tool_changeover_minutes", "label": "supplier tool changeover",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "supplier tool changeover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_reporting_lag_hours_21(record):
    """Evaluate supplier reporting lag for control WP-0155-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reporting_lag_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-21", "metric": "supplier_reporting_lag_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-21", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-21", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-21", "metric": "supplier_reporting_lag_hours", "label": "supplier reporting lag",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier reporting lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_retention_exception_resolution_pct_22(record):
    """Evaluate supplier retention exception resolution for control WP-0155-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-22", "metric": "supplier_retention_exception_resolution_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-22", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-22", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-22", "metric": "supplier_retention_exception_resolution_pct", "label": "supplier retention exception resolution",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier retention exception resolution must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_weight_kg_23(record):
    """Evaluate handling weight for control WP-0155-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-23", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-23", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-23", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-23", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "handling weight exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_seal_mismatch_count_24(record):
    """Evaluate seal mismatches for control WP-0155-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0155-24", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0155-24", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0155-24", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0155-24", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "seal mismatches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_payment_reconciliation_age_hours_01, assess_trailer_location_age_minutes_02, assess_damage_cost_monthly_03, assess_supplier_short_ship_pct_04, assess_supplier_asn_timeliness_pct_05, assess_supplier_demand_signal_age_hours_06, assess_supplier_business_owner_gap_count_07, assess_supplier_recall_response_minutes_08, assess_supplier_seismic_risk_score_09, assess_supplier_tooling_transfer_days_10, assess_supplier_certification_scope_gap_count_11, assess_supplier_gift_register_gap_count_12, assess_supplier_bcp_contact_age_days_13, assess_supplier_automation_coverage_pct_14, assess_supplier_human_review_queue_age_hours_15, assess_supplier_failover_test_age_days_16, assess_supplier_subprocessor_notice_pct_17, assess_supplier_kri_breach_count_18, assess_supplier_po_after_invoice_count_19, assess_supplier_tool_changeover_minutes_20, assess_supplier_reporting_lag_hours_21, assess_supplier_retention_exception_resolution_pct_22, assess_weight_kg_23, assess_seal_mismatch_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

