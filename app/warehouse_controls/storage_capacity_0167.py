"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_recall_response_minutes_01(record):
    """Evaluate supplier recall response time for control WP-0167-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recall_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-01", "metric": "supplier_recall_response_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-01", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-01", "metric": "supplier_recall_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-01", "metric": "supplier_recall_response_minutes", "label": "supplier recall response time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recall response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_seismic_risk_score_02(record):
    """Evaluate supplier seismic risk for control WP-0167-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seismic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-02", "metric": "supplier_seismic_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-02", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-02", "metric": "supplier_seismic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-02", "metric": "supplier_seismic_risk_score", "label": "supplier seismic risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier seismic risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_tooling_transfer_days_03(record):
    """Evaluate supplier tooling transfer time for control WP-0167-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-03", "metric": "supplier_tooling_transfer_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-03", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-03", "metric": "supplier_tooling_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-03", "metric": "supplier_tooling_transfer_days", "label": "supplier tooling transfer time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier tooling transfer time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_certification_scope_gap_count_04(record):
    """Evaluate supplier certification scope gaps for control WP-0167-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_scope_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-04", "metric": "supplier_certification_scope_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-04", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-04", "metric": "supplier_certification_scope_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-04", "metric": "supplier_certification_scope_gap_count", "label": "supplier certification scope gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "supplier certification scope gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_gift_register_gap_count_05(record):
    """Evaluate supplier gift-register gaps for control WP-0167-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gift_register_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-05", "metric": "supplier_gift_register_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-05", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-05", "metric": "supplier_gift_register_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-05", "metric": "supplier_gift_register_gap_count", "label": "supplier gift-register gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier gift-register gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_bcp_contact_age_days_06(record):
    """Evaluate supplier BCP contact age for control WP-0167-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_contact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-06", "metric": "supplier_bcp_contact_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-06", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-06", "metric": "supplier_bcp_contact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-06", "metric": "supplier_bcp_contact_age_days", "label": "supplier BCP contact age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier BCP contact age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_automation_coverage_pct_07(record):
    """Evaluate supplier automation coverage for control WP-0167-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_automation_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-07", "metric": "supplier_automation_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-07", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-07", "metric": "supplier_automation_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-07", "metric": "supplier_automation_coverage_pct", "label": "supplier automation coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier automation coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_human_review_queue_age_hours_08(record):
    """Evaluate supplier human review queue age for control WP-0167-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_review_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-08", "metric": "supplier_human_review_queue_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-08", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-08", "metric": "supplier_human_review_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-08", "metric": "supplier_human_review_queue_age_hours", "label": "supplier human review queue age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier human review queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_failover_test_age_days_09(record):
    """Evaluate supplier failover test age for control WP-0167-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_failover_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-09", "metric": "supplier_failover_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-09", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-09", "metric": "supplier_failover_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-09", "metric": "supplier_failover_test_age_days", "label": "supplier failover test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier failover test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_subprocessor_notice_pct_10(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0167-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-10", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-10", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-10", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-10", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier subprocessor notice compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_kri_breach_count_11(record):
    """Evaluate supplier KRI breaches for control WP-0167-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-11", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-11", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-11", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-11", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier KRI breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_po_after_invoice_count_12(record):
    """Evaluate PO-after-invoice events for control WP-0167-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-12", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-12", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-12", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-12", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "PO-after-invoice events falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_tool_changeover_minutes_13(record):
    """Evaluate supplier tool changeover for control WP-0167-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tool_changeover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-13", "metric": "supplier_tool_changeover_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-13", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-13", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-13", "metric": "supplier_tool_changeover_minutes", "label": "supplier tool changeover",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tool changeover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_reporting_lag_hours_14(record):
    """Evaluate supplier reporting lag for control WP-0167-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reporting_lag_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-14", "metric": "supplier_reporting_lag_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-14", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-14", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-14", "metric": "supplier_reporting_lag_hours", "label": "supplier reporting lag",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier reporting lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_retention_exception_resolution_pct_15(record):
    """Evaluate supplier retention exception resolution for control WP-0167-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-15", "metric": "supplier_retention_exception_resolution_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-15", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-15", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-15", "metric": "supplier_retention_exception_resolution_pct", "label": "supplier retention exception resolution",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier retention exception resolution exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_weight_kg_16(record):
    """Evaluate handling weight for control WP-0167-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-16", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-16", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-16", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-16", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "handling weight falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_seal_mismatch_count_17(record):
    """Evaluate seal mismatches for control WP-0167-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-17", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-17", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-17", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-17", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seal mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_pick_path_efficiency_pct_18(record):
    """Evaluate pick path efficiency for control WP-0167-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-18", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-18", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-18", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-18", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick path efficiency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_mean_time_between_failures_hours_19(record):
    """Evaluate mean time between failures for control WP-0167-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-19", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-19", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-19", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-19", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "mean time between failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_payment_term_days_20(record):
    """Evaluate payment terms for control WP-0167-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-20", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-20", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-20", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-20", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "payment terms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_database_connection_pct_21(record):
    """Evaluate database connection utilization for control WP-0167-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-21", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-21", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-21", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-21", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "database connection utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_moq_violation_count_22(record):
    """Evaluate minimum order quantity violations for control WP-0167-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("moq_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-22", "metric": "moq_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-22", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-22", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-22", "metric": "moq_violation_count", "label": "minimum order quantity violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum order quantity violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_shift_length_hours_23(record):
    """Evaluate shift length for control WP-0167-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_length_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-23", "metric": "shift_length_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-23", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-23", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-23", "metric": "shift_length_hours", "label": "shift length",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "shift length exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_waste_manifest_pct_24(record):
    """Evaluate waste manifest completion for control WP-0167-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0167-24", "metric": "waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0167-24", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0167-24", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0167-24", "metric": "waste_manifest_pct", "label": "waste manifest completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "waste manifest completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_recall_response_minutes_01, assess_supplier_seismic_risk_score_02, assess_supplier_tooling_transfer_days_03, assess_supplier_certification_scope_gap_count_04, assess_supplier_gift_register_gap_count_05, assess_supplier_bcp_contact_age_days_06, assess_supplier_automation_coverage_pct_07, assess_supplier_human_review_queue_age_hours_08, assess_supplier_failover_test_age_days_09, assess_supplier_subprocessor_notice_pct_10, assess_supplier_kri_breach_count_11, assess_supplier_po_after_invoice_count_12, assess_supplier_tool_changeover_minutes_13, assess_supplier_reporting_lag_hours_14, assess_supplier_retention_exception_resolution_pct_15, assess_weight_kg_16, assess_seal_mismatch_count_17, assess_pick_path_efficiency_pct_18, assess_mean_time_between_failures_hours_19, assess_payment_term_days_20, assess_database_connection_pct_21, assess_moq_violation_count_22, assess_shift_length_hours_23, assess_waste_manifest_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

