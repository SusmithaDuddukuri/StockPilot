"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_asn_timeliness_pct_01(record):
    """Evaluate supplier ASN timeliness for control WP-0478-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-01", "metric": "supplier_asn_timeliness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-01", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-01", "metric": "supplier_asn_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-01", "metric": "supplier_asn_timeliness_pct", "label": "supplier ASN timeliness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ASN timeliness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_demand_signal_age_hours_02(record):
    """Evaluate supplier demand signal age for control WP-0478-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_demand_signal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-02", "metric": "supplier_demand_signal_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-02", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-02", "metric": "supplier_demand_signal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-02", "metric": "supplier_demand_signal_age_hours", "label": "supplier demand signal age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier demand signal age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_business_owner_gap_count_03(record):
    """Evaluate supplier business-owner gaps for control WP-0478-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_business_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-03", "metric": "supplier_business_owner_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-03", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-03", "metric": "supplier_business_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-03", "metric": "supplier_business_owner_gap_count", "label": "supplier business-owner gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier business-owner gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_recall_response_minutes_04(record):
    """Evaluate supplier recall response time for control WP-0478-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recall_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-04", "metric": "supplier_recall_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-04", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-04", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-04", "metric": "supplier_recall_response_minutes", "label": "supplier recall response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recall response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_seismic_risk_score_05(record):
    """Evaluate supplier seismic risk for control WP-0478-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seismic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-05", "metric": "supplier_seismic_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-05", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-05", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-05", "metric": "supplier_seismic_risk_score", "label": "supplier seismic risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier seismic risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_tooling_transfer_days_06(record):
    """Evaluate supplier tooling transfer time for control WP-0478-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-06", "metric": "supplier_tooling_transfer_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-06", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-06", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-06", "metric": "supplier_tooling_transfer_days", "label": "supplier tooling transfer time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier tooling transfer time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_certification_scope_gap_count_07(record):
    """Evaluate supplier certification scope gaps for control WP-0478-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_scope_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-07", "metric": "supplier_certification_scope_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-07", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-07", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-07", "metric": "supplier_certification_scope_gap_count", "label": "supplier certification scope gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "supplier certification scope gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_gift_register_gap_count_08(record):
    """Evaluate supplier gift-register gaps for control WP-0478-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gift_register_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-08", "metric": "supplier_gift_register_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-08", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-08", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-08", "metric": "supplier_gift_register_gap_count", "label": "supplier gift-register gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier gift-register gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_bcp_contact_age_days_09(record):
    """Evaluate supplier BCP contact age for control WP-0478-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-09", "metric": "supplier_bcp_contact_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-09", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-09", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-09", "metric": "supplier_bcp_contact_age_days", "label": "supplier BCP contact age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier BCP contact age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_automation_coverage_pct_10(record):
    """Evaluate supplier automation coverage for control WP-0478-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_automation_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-10", "metric": "supplier_automation_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-10", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-10", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-10", "metric": "supplier_automation_coverage_pct", "label": "supplier automation coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "supplier automation coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_human_review_queue_age_hours_11(record):
    """Evaluate supplier human review queue age for control WP-0478-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_review_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-11", "metric": "supplier_human_review_queue_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-11", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-11", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-11", "metric": "supplier_human_review_queue_age_hours", "label": "supplier human review queue age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier human review queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_failover_test_age_days_12(record):
    """Evaluate supplier failover test age for control WP-0478-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_failover_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-12", "metric": "supplier_failover_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-12", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-12", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-12", "metric": "supplier_failover_test_age_days", "label": "supplier failover test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier failover test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_subprocessor_notice_pct_13(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0478-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-13", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-13", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-13", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-13", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier subprocessor notice compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_kri_breach_count_14(record):
    """Evaluate supplier KRI breaches for control WP-0478-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-14", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-14", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-14", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-14", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier KRI breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_po_after_invoice_count_15(record):
    """Evaluate PO-after-invoice events for control WP-0478-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-15", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-15", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-15", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-15", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "PO-after-invoice events falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_tool_changeover_minutes_16(record):
    """Evaluate supplier tool changeover for control WP-0478-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tool_changeover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-16", "metric": "supplier_tool_changeover_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-16", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-16", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-16", "metric": "supplier_tool_changeover_minutes", "label": "supplier tool changeover",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tool changeover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_reporting_lag_hours_17(record):
    """Evaluate supplier reporting lag for control WP-0478-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reporting_lag_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-17", "metric": "supplier_reporting_lag_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-17", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-17", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-17", "metric": "supplier_reporting_lag_hours", "label": "supplier reporting lag",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier reporting lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_retention_exception_resolution_pct_18(record):
    """Evaluate supplier retention exception resolution for control WP-0478-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-18", "metric": "supplier_retention_exception_resolution_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-18", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-18", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-18", "metric": "supplier_retention_exception_resolution_pct", "label": "supplier retention exception resolution",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier retention exception resolution exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_weight_kg_19(record):
    """Evaluate handling weight for control WP-0478-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-19", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-19", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-19", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-19", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "handling weight falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_seal_mismatch_count_20(record):
    """Evaluate seal mismatches for control WP-0478-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-20", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-20", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-20", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-20", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seal mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_pick_path_efficiency_pct_21(record):
    """Evaluate pick path efficiency for control WP-0478-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-21", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-21", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-21", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-21", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick path efficiency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_mean_time_between_failures_hours_22(record):
    """Evaluate mean time between failures for control WP-0478-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-22", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-22", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-22", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-22", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "mean time between failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_payment_term_days_23(record):
    """Evaluate payment terms for control WP-0478-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-23", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-23", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-23", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-23", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "payment terms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_database_connection_pct_24(record):
    """Evaluate database connection utilization for control WP-0478-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0478-24", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0478-24", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0478-24", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0478-24", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "database connection utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_supplier_asn_timeliness_pct_01, assess_supplier_demand_signal_age_hours_02, assess_supplier_business_owner_gap_count_03, assess_supplier_recall_response_minutes_04, assess_supplier_seismic_risk_score_05, assess_supplier_tooling_transfer_days_06, assess_supplier_certification_scope_gap_count_07, assess_supplier_gift_register_gap_count_08, assess_supplier_bcp_contact_age_days_09, assess_supplier_automation_coverage_pct_10, assess_supplier_human_review_queue_age_hours_11, assess_supplier_failover_test_age_days_12, assess_supplier_subprocessor_notice_pct_13, assess_supplier_kri_breach_count_14, assess_supplier_po_after_invoice_count_15, assess_supplier_tool_changeover_minutes_16, assess_supplier_reporting_lag_hours_17, assess_supplier_retention_exception_resolution_pct_18, assess_weight_kg_19, assess_seal_mismatch_count_20, assess_pick_path_efficiency_pct_21, assess_mean_time_between_failures_hours_22, assess_payment_term_days_23, assess_database_connection_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

