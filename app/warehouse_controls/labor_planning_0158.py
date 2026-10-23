"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_toll_reconciliation_pct_01(record):
    """Evaluate toll reconciliation for control WP-0158-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("toll_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-01", "metric": "toll_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-01", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-01", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-01", "metric": "toll_reconciliation_pct", "label": "toll reconciliation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "toll reconciliation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_continuity_score_02(record):
    """Evaluate supplier continuity score for control WP-0158-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-02", "metric": "supplier_continuity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-02", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-02", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-02", "metric": "supplier_continuity_score", "label": "supplier continuity score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier continuity score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_waste_rate_pct_03(record):
    """Evaluate supplier waste rate for control WP-0158-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waste_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-03", "metric": "supplier_waste_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-03", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-03", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-03", "metric": "supplier_waste_rate_pct", "label": "supplier waste rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier waste rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_port_dependency_pct_04(record):
    """Evaluate supplier port dependency for control WP-0158-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-04", "metric": "supplier_port_dependency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-04", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-04", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-04", "metric": "supplier_port_dependency_pct", "label": "supplier port dependency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier port dependency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_data_retention_gap_count_05(record):
    """Evaluate supplier data-retention gaps for control WP-0158-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_retention_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-05", "metric": "supplier_data_retention_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-05", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-05", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-05", "metric": "supplier_data_retention_gap_count", "label": "supplier data-retention gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data-retention gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_working_capital_score_06(record):
    """Evaluate supplier working-capital score for control WP-0158-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_capital_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-06", "metric": "supplier_working_capital_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-06", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-06", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-06", "metric": "supplier_working_capital_score", "label": "supplier working-capital score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier working-capital score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_end_of_life_plan_pct_07(record):
    """Evaluate supplier end-of-life plan completeness for control WP-0158-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_end_of_life_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-07", "metric": "supplier_end_of_life_plan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-07", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-07", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-07", "metric": "supplier_end_of_life_plan_pct", "label": "supplier end-of-life plan completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier end-of-life plan completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_event_visibility_pct_08(record):
    """Evaluate supplier event visibility for control WP-0158-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-08", "metric": "supplier_event_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-08", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-08", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-08", "metric": "supplier_event_visibility_pct", "label": "supplier event visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier event visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_measurement_calibration_pct_09(record):
    """Evaluate supplier measurement calibration for control WP-0158-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_calibration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-09", "metric": "supplier_measurement_calibration_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-09", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-09", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-09", "metric": "supplier_measurement_calibration_pct", "label": "supplier measurement calibration",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier measurement calibration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_labor_compliance_score_10(record):
    """Evaluate supplier labor compliance for control WP-0158-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-10", "metric": "supplier_labor_compliance_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-10", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-10", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-10", "metric": "supplier_labor_compliance_score", "label": "supplier labor compliance",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier labor compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_bankruptcy_signal_11(record):
    """Evaluate supplier bankruptcy signal for control WP-0158-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bankruptcy_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-11", "metric": "supplier_bankruptcy_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-11", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-11", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-11", "metric": "supplier_bankruptcy_signal", "label": "supplier bankruptcy signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "supplier bankruptcy signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_management_review_age_days_12(record):
    """Evaluate supplier management review age for control WP-0158-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_management_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-12", "metric": "supplier_management_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-12", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-12", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-12", "metric": "supplier_management_review_age_days", "label": "supplier management review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier management review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_ai_redteam_age_days_13(record):
    """Evaluate supplier AI red-team age for control WP-0158-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_redteam_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-13", "metric": "supplier_ai_redteam_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-13", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-13", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-13", "metric": "supplier_ai_redteam_age_days", "label": "supplier AI red-team age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier AI red-team age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_log_redaction_pct_14(record):
    """Evaluate supplier log redaction for control WP-0158-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_log_redaction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-14", "metric": "supplier_log_redaction_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-14", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-14", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-14", "metric": "supplier_log_redaction_pct", "label": "supplier log redaction",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "supplier log redaction exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_dynamic_analysis_age_days_15(record):
    """Evaluate supplier dynamic analysis age for control WP-0158-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dynamic_analysis_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-15", "metric": "supplier_dynamic_analysis_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-15", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-15", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-15", "metric": "supplier_dynamic_analysis_age_days", "label": "supplier dynamic analysis age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier dynamic analysis age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_access_certification_pct_16(record):
    """Evaluate supplier access certification for control WP-0158-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_certification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-16", "metric": "supplier_access_certification_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-16", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-16", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-16", "metric": "supplier_access_certification_pct", "label": "supplier access certification",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access certification must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_round_sum_signal_17(record):
    """Evaluate supplier round-sum signal for control WP-0158-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_round_sum_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-17", "metric": "supplier_round_sum_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-17", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-17", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-17", "metric": "supplier_round_sum_signal", "label": "supplier round-sum signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier round-sum signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_schedule_ack_pct_18(record):
    """Evaluate schedule acknowledgement for control WP-0158-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-18", "metric": "supplier_schedule_ack_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-18", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-18", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-18", "metric": "supplier_schedule_ack_pct", "label": "schedule acknowledgement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "schedule acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_asn_upload_age_hours_19(record):
    """Evaluate supplier ASN upload age for control WP-0158-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-19", "metric": "supplier_asn_upload_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-19", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-19", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-19", "metric": "supplier_asn_upload_age_hours", "label": "supplier ASN upload age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier ASN upload age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_endpoint_cutover_pct_20(record):
    """Evaluate supplier endpoint cutover for control WP-0158-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_endpoint_cutover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-20", "metric": "supplier_endpoint_cutover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-20", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-20", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-20", "metric": "supplier_endpoint_cutover_pct", "label": "supplier endpoint cutover",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier endpoint cutover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_order_age_hours_21(record):
    """Evaluate order age for control WP-0158-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-21", "metric": "order_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-21", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-21", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-21", "metric": "order_age_hours", "label": "order age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_training_expiry_days_22(record):
    """Evaluate training validity for control WP-0158-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-22", "metric": "training_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-22", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-22", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-22", "metric": "training_expiry_days", "label": "training validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "training validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_lot_traceability_pct_23(record):
    """Evaluate lot traceability for control WP-0158-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-23", "metric": "lot_traceability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-23", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-23", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-23", "metric": "lot_traceability_pct", "label": "lot traceability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "lot traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_backorder_units_24(record):
    """Evaluate backordered units for control WP-0158-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backorder_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0158-24", "metric": "backorder_units",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0158-24", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0158-24", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0158-24", "metric": "backorder_units", "label": "backordered units",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backordered units must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_toll_reconciliation_pct_01, assess_supplier_continuity_score_02, assess_supplier_waste_rate_pct_03, assess_supplier_port_dependency_pct_04, assess_supplier_data_retention_gap_count_05, assess_supplier_working_capital_score_06, assess_supplier_end_of_life_plan_pct_07, assess_supplier_event_visibility_pct_08, assess_supplier_measurement_calibration_pct_09, assess_supplier_labor_compliance_score_10, assess_supplier_bankruptcy_signal_11, assess_supplier_management_review_age_days_12, assess_supplier_ai_redteam_age_days_13, assess_supplier_log_redaction_pct_14, assess_supplier_dynamic_analysis_age_days_15, assess_supplier_access_certification_pct_16, assess_supplier_round_sum_signal_17, assess_supplier_schedule_ack_pct_18, assess_supplier_asn_upload_age_hours_19, assess_supplier_endpoint_cutover_pct_20, assess_order_age_hours_21, assess_training_expiry_days_22, assess_lot_traceability_pct_23, assess_backorder_units_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

