"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_high_value_claim_age_days_01(record):
    """Evaluate high-value claim age for control WP-0333-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-01", "metric": "high_value_claim_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-01", "metric": "high_value_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-01", "metric": "high_value_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-01", "metric": "high_value_claim_age_days", "label": "high-value claim age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "high-value claim age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_lockout_tagout_compliance_pct_02(record):
    """Evaluate lockout/tagout compliance for control WP-0333-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lockout_tagout_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-02", "metric": "lockout_tagout_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-02", "metric": "lockout_tagout_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-02", "metric": "lockout_tagout_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-02", "metric": "lockout_tagout_compliance_pct", "label": "lockout/tagout compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "lockout/tagout compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_preventive_maintenance_overdue_count_03(record):
    """Evaluate overdue preventive maintenance for control WP-0333-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventive_maintenance_overdue_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-03", "metric": "preventive_maintenance_overdue_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "jobs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-03", "metric": "preventive_maintenance_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-03", "metric": "preventive_maintenance_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-03", "metric": "preventive_maintenance_overdue_count", "label": "overdue preventive maintenance",
        "status": "breach", "severity": "critical", "unit": "jobs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "overdue preventive maintenance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_release_rollback_count_04(record):
    """Evaluate release rollbacks for control WP-0333-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("release_rollback_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-04", "metric": "release_rollback_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-04", "metric": "release_rollback_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-04", "metric": "release_rollback_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-04", "metric": "release_rollback_count", "label": "release rollbacks",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "release rollbacks must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_retention_policy_gap_count_05(record):
    """Evaluate retention policy gaps for control WP-0333-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("retention_policy_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-05", "metric": "retention_policy_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-05", "metric": "retention_policy_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-05", "metric": "retention_policy_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-05", "metric": "retention_policy_gap_count", "label": "retention policy gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "retention policy gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_tax_code_gap_count_06(record):
    """Evaluate tax-code gaps for control WP-0333-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-06", "metric": "tax_code_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-06", "metric": "tax_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-06", "metric": "tax_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-06", "metric": "tax_code_gap_count", "label": "tax-code gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "tax-code gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_purchase_order_ack_age_hours_07(record):
    """Evaluate purchase-order acknowledgement age for control WP-0333-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_order_ack_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-07", "metric": "purchase_order_ack_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-07", "metric": "purchase_order_ack_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-07", "metric": "purchase_order_ack_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-07", "metric": "purchase_order_ack_age_hours", "label": "purchase-order acknowledgement age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "purchase-order acknowledgement age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_route_stop_overrun_minutes_08(record):
    """Evaluate route stop overrun for control WP-0333-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_stop_overrun_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-08", "metric": "route_stop_overrun_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-08", "metric": "route_stop_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-08", "metric": "route_stop_overrun_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-08", "metric": "route_stop_overrun_minutes", "label": "route stop overrun",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route stop overrun must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_accessorial_charge_count_09(record):
    """Evaluate accessorial charges for control WP-0333-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessorial_charge_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-09", "metric": "accessorial_charge_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-09", "metric": "accessorial_charge_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-09", "metric": "accessorial_charge_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-09", "metric": "accessorial_charge_count", "label": "accessorial charges",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "accessorial charges exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_toll_reconciliation_pct_10(record):
    """Evaluate toll reconciliation for control WP-0333-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("toll_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-10", "metric": "toll_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-10", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-10", "metric": "toll_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-10", "metric": "toll_reconciliation_pct", "label": "toll reconciliation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "toll reconciliation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_continuity_score_11(record):
    """Evaluate supplier continuity score for control WP-0333-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-11", "metric": "supplier_continuity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-11", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-11", "metric": "supplier_continuity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-11", "metric": "supplier_continuity_score", "label": "supplier continuity score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier continuity score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_waste_rate_pct_12(record):
    """Evaluate supplier waste rate for control WP-0333-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waste_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-12", "metric": "supplier_waste_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-12", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-12", "metric": "supplier_waste_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-12", "metric": "supplier_waste_rate_pct", "label": "supplier waste rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier waste rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_port_dependency_pct_13(record):
    """Evaluate supplier port dependency for control WP-0333-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-13", "metric": "supplier_port_dependency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-13", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-13", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-13", "metric": "supplier_port_dependency_pct", "label": "supplier port dependency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier port dependency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_data_retention_gap_count_14(record):
    """Evaluate supplier data-retention gaps for control WP-0333-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_retention_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-14", "metric": "supplier_data_retention_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-14", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-14", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-14", "metric": "supplier_data_retention_gap_count", "label": "supplier data-retention gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier data-retention gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_working_capital_score_15(record):
    """Evaluate supplier working-capital score for control WP-0333-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_capital_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-15", "metric": "supplier_working_capital_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-15", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-15", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-15", "metric": "supplier_working_capital_score", "label": "supplier working-capital score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier working-capital score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_end_of_life_plan_pct_16(record):
    """Evaluate supplier end-of-life plan completeness for control WP-0333-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_end_of_life_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-16", "metric": "supplier_end_of_life_plan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-16", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-16", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-16", "metric": "supplier_end_of_life_plan_pct", "label": "supplier end-of-life plan completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier end-of-life plan completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_event_visibility_pct_17(record):
    """Evaluate supplier event visibility for control WP-0333-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-17", "metric": "supplier_event_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-17", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-17", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-17", "metric": "supplier_event_visibility_pct", "label": "supplier event visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "supplier event visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_measurement_calibration_pct_18(record):
    """Evaluate supplier measurement calibration for control WP-0333-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_calibration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-18", "metric": "supplier_measurement_calibration_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-18", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-18", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-18", "metric": "supplier_measurement_calibration_pct", "label": "supplier measurement calibration",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier measurement calibration falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_labor_compliance_score_19(record):
    """Evaluate supplier labor compliance for control WP-0333-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-19", "metric": "supplier_labor_compliance_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-19", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-19", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-19", "metric": "supplier_labor_compliance_score", "label": "supplier labor compliance",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier labor compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_bankruptcy_signal_20(record):
    """Evaluate supplier bankruptcy signal for control WP-0333-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bankruptcy_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-20", "metric": "supplier_bankruptcy_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-20", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-20", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-20", "metric": "supplier_bankruptcy_signal", "label": "supplier bankruptcy signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier bankruptcy signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_management_review_age_days_21(record):
    """Evaluate supplier management review age for control WP-0333-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_management_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-21", "metric": "supplier_management_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-21", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-21", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-21", "metric": "supplier_management_review_age_days", "label": "supplier management review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier management review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_ai_redteam_age_days_22(record):
    """Evaluate supplier AI red-team age for control WP-0333-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_redteam_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-22", "metric": "supplier_ai_redteam_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-22", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-22", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-22", "metric": "supplier_ai_redteam_age_days", "label": "supplier AI red-team age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier AI red-team age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_log_redaction_pct_23(record):
    """Evaluate supplier log redaction for control WP-0333-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_log_redaction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-23", "metric": "supplier_log_redaction_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-23", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-23", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-23", "metric": "supplier_log_redaction_pct", "label": "supplier log redaction",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier log redaction must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dynamic_analysis_age_days_24(record):
    """Evaluate supplier dynamic analysis age for control WP-0333-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dynamic_analysis_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0333-24", "metric": "supplier_dynamic_analysis_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0333-24", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0333-24", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0333-24", "metric": "supplier_dynamic_analysis_age_days", "label": "supplier dynamic analysis age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dynamic analysis age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_high_value_claim_age_days_01, assess_lockout_tagout_compliance_pct_02, assess_preventive_maintenance_overdue_count_03, assess_release_rollback_count_04, assess_retention_policy_gap_count_05, assess_tax_code_gap_count_06, assess_purchase_order_ack_age_hours_07, assess_route_stop_overrun_minutes_08, assess_accessorial_charge_count_09, assess_toll_reconciliation_pct_10, assess_supplier_continuity_score_11, assess_supplier_waste_rate_pct_12, assess_supplier_port_dependency_pct_13, assess_supplier_data_retention_gap_count_14, assess_supplier_working_capital_score_15, assess_supplier_end_of_life_plan_pct_16, assess_supplier_event_visibility_pct_17, assess_supplier_measurement_calibration_pct_18, assess_supplier_labor_compliance_score_19, assess_supplier_bankruptcy_signal_20, assess_supplier_management_review_age_days_21, assess_supplier_ai_redteam_age_days_22, assess_supplier_log_redaction_pct_23, assess_supplier_dynamic_analysis_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

