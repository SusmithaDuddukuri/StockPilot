"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_export_control_gap_count_01(record):
    """Evaluate supplier export-control gaps for control WP-0544-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-01", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-01", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-01", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-01", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier export-control gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_dependency_count_02(record):
    """Evaluate supplier dependencies for control WP-0544-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-02", "metric": "supplier_dependency_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-02", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-02", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-02", "metric": "supplier_dependency_count", "label": "supplier dependencies",
        "status": "breach", "severity": "medium", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dependencies must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_aftermarket_support_score_03(record):
    """Evaluate supplier aftermarket support for control WP-0544-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_aftermarket_support_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-03", "metric": "supplier_aftermarket_support_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-03", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-03", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-03", "metric": "supplier_aftermarket_support_score", "label": "supplier aftermarket support",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier aftermarket support must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_service_recovery_score_04(record):
    """Evaluate supplier service recovery for control WP-0544-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-04", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-04", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-04", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-04", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier service recovery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_fai_completion_pct_05(record):
    """Evaluate supplier first-article inspection for control WP-0544-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fai_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-05", "metric": "supplier_fai_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-05", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-05", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-05", "metric": "supplier_fai_completion_pct", "label": "supplier first-article inspection",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier first-article inspection falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_fire_response_drill_age_days_06(record):
    """Evaluate supplier fire drill age for control WP-0544-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-06", "metric": "supplier_fire_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-06", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-06", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-06", "metric": "supplier_fire_response_drill_age_days", "label": "supplier fire drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier fire drill age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_ap_days_07(record):
    """Evaluate supplier accounts-payable days for control WP-0544-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ap_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-07", "metric": "supplier_ap_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-07", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-07", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-07", "metric": "supplier_ap_days", "label": "supplier accounts-payable days",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier accounts-payable days must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_knowledge_base_age_days_08(record):
    """Evaluate supplier knowledge-base age for control WP-0544-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_base_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-08", "metric": "supplier_knowledge_base_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-08", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-08", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-08", "metric": "supplier_knowledge_base_age_days", "label": "supplier knowledge-base age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier knowledge-base age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_bias_audit_age_days_09(record):
    """Evaluate supplier bias-audit age for control WP-0544-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bias_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-09", "metric": "supplier_bias_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-09", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-09", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-09", "metric": "supplier_bias_audit_age_days", "label": "supplier bias-audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier bias-audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_duplicate_event_pct_10(record):
    """Evaluate supplier duplicate event rate for control WP-0544-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_event_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-10", "metric": "supplier_duplicate_event_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-10", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-10", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-10", "metric": "supplier_duplicate_event_pct", "label": "supplier duplicate event rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier duplicate event rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_pen_test_age_days_11(record):
    """Evaluate supplier penetration-test age for control WP-0544-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pen_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-11", "metric": "supplier_pen_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-11", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-11", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-11", "metric": "supplier_pen_test_age_days", "label": "supplier penetration-test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier penetration-test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_secure_disposal_pct_12(record):
    """Evaluate supplier secure disposal for control WP-0544-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_disposal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-12", "metric": "supplier_secure_disposal_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-12", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-12", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-12", "metric": "supplier_secure_disposal_pct", "label": "supplier secure disposal",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier secure disposal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_segregation_duty_pct_13(record):
    """Evaluate supplier segregation of duties for control WP-0544-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_segregation_duty_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-13", "metric": "supplier_segregation_duty_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-13", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-13", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-13", "metric": "supplier_segregation_duty_pct", "label": "supplier segregation of duties",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier segregation of duties falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_capacity_allocation_pct_14(record):
    """Evaluate supplier capacity allocation for control WP-0544-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_allocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-14", "metric": "supplier_capacity_allocation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-14", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-14", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-14", "metric": "supplier_capacity_allocation_pct", "label": "supplier capacity allocation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity allocation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_carrier_handoff_pct_15(record):
    """Evaluate supplier carrier handoff for control WP-0544-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carrier_handoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-15", "metric": "supplier_carrier_handoff_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-15", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-15", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-15", "metric": "supplier_carrier_handoff_pct", "label": "supplier carrier handoff",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier carrier handoff must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_asset_transfer_match_pct_16(record):
    """Evaluate asset transfer match for control WP-0544-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-16", "metric": "supplier_asset_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-16", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-16", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-16", "metric": "supplier_asset_transfer_match_pct", "label": "asset transfer match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "asset transfer match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_capacity_units_17(record):
    """Evaluate storage capacity for control WP-0544-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capacity_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-17", "metric": "capacity_units",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-17", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-17", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-17", "metric": "capacity_units", "label": "storage capacity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "storage capacity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_mis_pick_count_18(record):
    """Evaluate mis-picks for control WP-0544-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mis_pick_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-18", "metric": "mis_pick_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-18", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-18", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-18", "metric": "mis_pick_count", "label": "mis-picks",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "mis-picks must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_single_source_sku_count_19(record):
    """Evaluate single-source SKUs for control WP-0544-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("single_source_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-19", "metric": "single_source_sku_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-19", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-19", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-19", "metric": "single_source_sku_count", "label": "single-source SKUs",
        "status": "breach", "severity": "high", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "single-source SKUs must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_cost_variance_pct_20(record):
    """Evaluate cost variance for control WP-0544-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-20", "metric": "cost_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-20", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-20", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-20", "metric": "cost_variance_pct", "label": "cost variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "cost variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_water_liters_per_order_21(record):
    """Evaluate water per order for control WP-0544-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_liters_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-21", "metric": "water_liters_per_order",
            "status": "insufficient_data",
            "severity": "low", "unit": "liters",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-21", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-21", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-21", "metric": "water_liters_per_order", "label": "water per order",
        "status": "breach", "severity": "low", "unit": "liters",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "water per order falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_regulatory_document_age_days_22(record):
    """Evaluate regulatory document age for control WP-0544-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("regulatory_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-22", "metric": "regulatory_document_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-22", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-22", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-22", "metric": "regulatory_document_age_days", "label": "regulatory document age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "regulatory document age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_consent_record_pct_23(record):
    """Evaluate consent records completeness for control WP-0544-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("consent_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-23", "metric": "consent_record_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-23", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-23", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-23", "metric": "consent_record_pct", "label": "consent records completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "consent records completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_spill_kit_check_age_days_24(record):
    """Evaluate spill-kit check age for control WP-0544-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0544-24", "metric": "spill_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0544-24", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0544-24", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0544-24", "metric": "spill_kit_check_age_days", "label": "spill-kit check age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "spill-kit check age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_export_control_gap_count_01, assess_supplier_dependency_count_02, assess_supplier_aftermarket_support_score_03, assess_supplier_service_recovery_score_04, assess_supplier_fai_completion_pct_05, assess_supplier_fire_response_drill_age_days_06, assess_supplier_ap_days_07, assess_supplier_knowledge_base_age_days_08, assess_supplier_bias_audit_age_days_09, assess_supplier_duplicate_event_pct_10, assess_supplier_pen_test_age_days_11, assess_supplier_secure_disposal_pct_12, assess_supplier_segregation_duty_pct_13, assess_supplier_capacity_allocation_pct_14, assess_supplier_carrier_handoff_pct_15, assess_supplier_asset_transfer_match_pct_16, assess_capacity_units_17, assess_mis_pick_count_18, assess_single_source_sku_count_19, assess_cost_variance_pct_20, assess_water_liters_per_order_21, assess_regulatory_document_age_days_22, assess_consent_record_pct_23, assess_spill_kit_check_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

