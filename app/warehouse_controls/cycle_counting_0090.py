"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_purchase_order_ack_age_hours_01(record):
    """Evaluate purchase-order acknowledgement age for control WP-0090-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_ack_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-01", "metric": "purchase_order_ack_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-01", "metric": "purchase_order_ack_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-01", "metric": "purchase_order_ack_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-01", "metric": "purchase_order_ack_age_hours", "label": "purchase-order acknowledgement age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "purchase-order acknowledgement age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_route_stop_overrun_minutes_02(record):
    """Evaluate route stop overrun for control WP-0090-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_stop_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-02", "metric": "route_stop_overrun_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-02", "metric": "route_stop_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-02", "metric": "route_stop_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-02", "metric": "route_stop_overrun_minutes", "label": "route stop overrun",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "route stop overrun exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_accessorial_charge_count_03(record):
    """Evaluate accessorial charges for control WP-0090-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessorial_charge_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-03", "metric": "accessorial_charge_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-03", "metric": "accessorial_charge_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-03", "metric": "accessorial_charge_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-03", "metric": "accessorial_charge_count", "label": "accessorial charges",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "accessorial charges falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_toll_reconciliation_pct_04(record):
    """Evaluate toll reconciliation for control WP-0090-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("toll_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-04", "metric": "toll_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-04", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-04", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-04", "metric": "toll_reconciliation_pct", "label": "toll reconciliation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "toll reconciliation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_continuity_score_05(record):
    """Evaluate supplier continuity score for control WP-0090-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-05", "metric": "supplier_continuity_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-05", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-05", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-05", "metric": "supplier_continuity_score", "label": "supplier continuity score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier continuity score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_waste_rate_pct_06(record):
    """Evaluate supplier waste rate for control WP-0090-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waste_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-06", "metric": "supplier_waste_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-06", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-06", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-06", "metric": "supplier_waste_rate_pct", "label": "supplier waste rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "supplier waste rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_port_dependency_pct_07(record):
    """Evaluate supplier port dependency for control WP-0090-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-07", "metric": "supplier_port_dependency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-07", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-07", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-07", "metric": "supplier_port_dependency_pct", "label": "supplier port dependency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "supplier port dependency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_data_retention_gap_count_08(record):
    """Evaluate supplier data-retention gaps for control WP-0090-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_retention_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-08", "metric": "supplier_data_retention_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-08", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-08", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-08", "metric": "supplier_data_retention_gap_count", "label": "supplier data-retention gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-retention gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_working_capital_score_09(record):
    """Evaluate supplier working-capital score for control WP-0090-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_capital_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-09", "metric": "supplier_working_capital_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-09", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-09", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-09", "metric": "supplier_working_capital_score", "label": "supplier working-capital score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier working-capital score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_end_of_life_plan_pct_10(record):
    """Evaluate supplier end-of-life plan completeness for control WP-0090-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_end_of_life_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-10", "metric": "supplier_end_of_life_plan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-10", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-10", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-10", "metric": "supplier_end_of_life_plan_pct", "label": "supplier end-of-life plan completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "supplier end-of-life plan completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_event_visibility_pct_11(record):
    """Evaluate supplier event visibility for control WP-0090-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-11", "metric": "supplier_event_visibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-11", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-11", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-11", "metric": "supplier_event_visibility_pct", "label": "supplier event visibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier event visibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_measurement_calibration_pct_12(record):
    """Evaluate supplier measurement calibration for control WP-0090-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_calibration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-12", "metric": "supplier_measurement_calibration_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-12", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-12", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-12", "metric": "supplier_measurement_calibration_pct", "label": "supplier measurement calibration",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier measurement calibration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_labor_compliance_score_13(record):
    """Evaluate supplier labor compliance for control WP-0090-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-13", "metric": "supplier_labor_compliance_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-13", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-13", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-13", "metric": "supplier_labor_compliance_score", "label": "supplier labor compliance",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier labor compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_bankruptcy_signal_14(record):
    """Evaluate supplier bankruptcy signal for control WP-0090-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bankruptcy_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-14", "metric": "supplier_bankruptcy_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-14", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-14", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-14", "metric": "supplier_bankruptcy_signal", "label": "supplier bankruptcy signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "supplier bankruptcy signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_management_review_age_days_15(record):
    """Evaluate supplier management review age for control WP-0090-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_management_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-15", "metric": "supplier_management_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-15", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-15", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-15", "metric": "supplier_management_review_age_days", "label": "supplier management review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier management review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_ai_redteam_age_days_16(record):
    """Evaluate supplier AI red-team age for control WP-0090-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_redteam_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-16", "metric": "supplier_ai_redteam_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-16", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-16", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-16", "metric": "supplier_ai_redteam_age_days", "label": "supplier AI red-team age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier AI red-team age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_log_redaction_pct_17(record):
    """Evaluate supplier log redaction for control WP-0090-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_log_redaction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-17", "metric": "supplier_log_redaction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-17", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-17", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-17", "metric": "supplier_log_redaction_pct", "label": "supplier log redaction",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier log redaction must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_dynamic_analysis_age_days_18(record):
    """Evaluate supplier dynamic analysis age for control WP-0090-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dynamic_analysis_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-18", "metric": "supplier_dynamic_analysis_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-18", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-18", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-18", "metric": "supplier_dynamic_analysis_age_days", "label": "supplier dynamic analysis age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "supplier dynamic analysis age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_access_certification_pct_19(record):
    """Evaluate supplier access certification for control WP-0090-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_certification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-19", "metric": "supplier_access_certification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-19", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-19", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-19", "metric": "supplier_access_certification_pct", "label": "supplier access certification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "supplier access certification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_round_sum_signal_20(record):
    """Evaluate supplier round-sum signal for control WP-0090-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_round_sum_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-20", "metric": "supplier_round_sum_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-20", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-20", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-20", "metric": "supplier_round_sum_signal", "label": "supplier round-sum signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier round-sum signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_schedule_ack_pct_21(record):
    """Evaluate schedule acknowledgement for control WP-0090-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-21", "metric": "supplier_schedule_ack_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-21", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-21", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-21", "metric": "supplier_schedule_ack_pct", "label": "schedule acknowledgement",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schedule acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_asn_upload_age_hours_22(record):
    """Evaluate supplier ASN upload age for control WP-0090-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-22", "metric": "supplier_asn_upload_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-22", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-22", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-22", "metric": "supplier_asn_upload_age_hours", "label": "supplier ASN upload age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier ASN upload age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_endpoint_cutover_pct_23(record):
    """Evaluate supplier endpoint cutover for control WP-0090-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_endpoint_cutover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-23", "metric": "supplier_endpoint_cutover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-23", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-23", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-23", "metric": "supplier_endpoint_cutover_pct", "label": "supplier endpoint cutover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier endpoint cutover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_order_age_hours_24(record):
    """Evaluate order age for control WP-0090-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0090-24", "metric": "order_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0090-24", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0090-24", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0090-24", "metric": "order_age_hours", "label": "order age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_purchase_order_ack_age_hours_01, assess_route_stop_overrun_minutes_02, assess_accessorial_charge_count_03, assess_toll_reconciliation_pct_04, assess_supplier_continuity_score_05, assess_supplier_waste_rate_pct_06, assess_supplier_port_dependency_pct_07, assess_supplier_data_retention_gap_count_08, assess_supplier_working_capital_score_09, assess_supplier_end_of_life_plan_pct_10, assess_supplier_event_visibility_pct_11, assess_supplier_measurement_calibration_pct_12, assess_supplier_labor_compliance_score_13, assess_supplier_bankruptcy_signal_14, assess_supplier_management_review_age_days_15, assess_supplier_ai_redteam_age_days_16, assess_supplier_log_redaction_pct_17, assess_supplier_dynamic_analysis_age_days_18, assess_supplier_access_certification_pct_19, assess_supplier_round_sum_signal_20, assess_supplier_schedule_ack_pct_21, assess_supplier_asn_upload_age_hours_22, assess_supplier_endpoint_cutover_pct_23, assess_order_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

