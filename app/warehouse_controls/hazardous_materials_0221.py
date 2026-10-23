"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_telematics_gap_minutes_01(record):
    """Evaluate telematics gap for control WP-0221-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("telematics_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-01", "metric": "telematics_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-01", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-01", "metric": "telematics_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-01", "metric": "telematics_gap_minutes", "label": "telematics gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "telematics gap exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_approval_queue_age_hours_02(record):
    """Evaluate approval queue age for control WP-0221-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("approval_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-02", "metric": "approval_queue_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-02", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-02", "metric": "approval_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-02", "metric": "approval_queue_age_hours", "label": "approval queue age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "approval queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_subtier_visibility_pct_03(record):
    """Evaluate supplier sub-tier visibility for control WP-0221-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-03", "metric": "supplier_subtier_visibility_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-03", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-03", "metric": "supplier_subtier_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-03", "metric": "supplier_subtier_visibility_pct", "label": "supplier sub-tier visibility",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sub-tier visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_packaging_validation_age_days_04(record):
    """Evaluate supplier packaging validation age for control WP-0221-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-04", "metric": "supplier_packaging_validation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-04", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-04", "metric": "supplier_packaging_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-04", "metric": "supplier_packaging_validation_age_days", "label": "supplier packaging validation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging validation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_export_control_gap_count_05(record):
    """Evaluate supplier export-control gaps for control WP-0221-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_export_control_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-05", "metric": "supplier_export_control_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-05", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-05", "metric": "supplier_export_control_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-05", "metric": "supplier_export_control_gap_count", "label": "supplier export-control gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier export-control gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dependency_count_06(record):
    """Evaluate supplier dependencies for control WP-0221-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-06", "metric": "supplier_dependency_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-06", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-06", "metric": "supplier_dependency_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-06", "metric": "supplier_dependency_count", "label": "supplier dependencies",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "supplier dependencies falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_aftermarket_support_score_07(record):
    """Evaluate supplier aftermarket support for control WP-0221-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_aftermarket_support_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-07", "metric": "supplier_aftermarket_support_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-07", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-07", "metric": "supplier_aftermarket_support_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-07", "metric": "supplier_aftermarket_support_score", "label": "supplier aftermarket support",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier aftermarket support must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_service_recovery_score_08(record):
    """Evaluate supplier service recovery for control WP-0221-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-08", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-08", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-08", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-08", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier service recovery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_fai_completion_pct_09(record):
    """Evaluate supplier first-article inspection for control WP-0221-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fai_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-09", "metric": "supplier_fai_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-09", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-09", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-09", "metric": "supplier_fai_completion_pct", "label": "supplier first-article inspection",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier first-article inspection exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_fire_response_drill_age_days_10(record):
    """Evaluate supplier fire drill age for control WP-0221-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-10", "metric": "supplier_fire_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-10", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-10", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-10", "metric": "supplier_fire_response_drill_age_days", "label": "supplier fire drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "supplier fire drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_ap_days_11(record):
    """Evaluate supplier accounts-payable days for control WP-0221-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ap_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-11", "metric": "supplier_ap_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-11", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-11", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-11", "metric": "supplier_ap_days", "label": "supplier accounts-payable days",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier accounts-payable days must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_knowledge_base_age_days_12(record):
    """Evaluate supplier knowledge-base age for control WP-0221-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_base_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-12", "metric": "supplier_knowledge_base_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-12", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-12", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-12", "metric": "supplier_knowledge_base_age_days", "label": "supplier knowledge-base age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier knowledge-base age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_bias_audit_age_days_13(record):
    """Evaluate supplier bias-audit age for control WP-0221-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bias_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-13", "metric": "supplier_bias_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-13", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-13", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-13", "metric": "supplier_bias_audit_age_days", "label": "supplier bias-audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier bias-audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_duplicate_event_pct_14(record):
    """Evaluate supplier duplicate event rate for control WP-0221-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_event_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-14", "metric": "supplier_duplicate_event_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-14", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-14", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-14", "metric": "supplier_duplicate_event_pct", "label": "supplier duplicate event rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier duplicate event rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_pen_test_age_days_15(record):
    """Evaluate supplier penetration-test age for control WP-0221-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pen_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-15", "metric": "supplier_pen_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-15", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-15", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-15", "metric": "supplier_pen_test_age_days", "label": "supplier penetration-test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier penetration-test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_secure_disposal_pct_16(record):
    """Evaluate supplier secure disposal for control WP-0221-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_disposal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-16", "metric": "supplier_secure_disposal_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-16", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-16", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-16", "metric": "supplier_secure_disposal_pct", "label": "supplier secure disposal",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier secure disposal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_segregation_duty_pct_17(record):
    """Evaluate supplier segregation of duties for control WP-0221-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_segregation_duty_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-17", "metric": "supplier_segregation_duty_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-17", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-17", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-17", "metric": "supplier_segregation_duty_pct", "label": "supplier segregation of duties",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier segregation of duties exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_capacity_allocation_pct_18(record):
    """Evaluate supplier capacity allocation for control WP-0221-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_allocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-18", "metric": "supplier_capacity_allocation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-18", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-18", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-18", "metric": "supplier_capacity_allocation_pct", "label": "supplier capacity allocation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier capacity allocation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_carrier_handoff_pct_19(record):
    """Evaluate supplier carrier handoff for control WP-0221-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carrier_handoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-19", "metric": "supplier_carrier_handoff_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-19", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-19", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-19", "metric": "supplier_carrier_handoff_pct", "label": "supplier carrier handoff",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier carrier handoff must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_asset_transfer_match_pct_20(record):
    """Evaluate asset transfer match for control WP-0221-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-20", "metric": "supplier_asset_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-20", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-20", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-20", "metric": "supplier_asset_transfer_match_pct", "label": "asset transfer match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "asset transfer match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_capacity_units_21(record):
    """Evaluate storage capacity for control WP-0221-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capacity_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-21", "metric": "capacity_units",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-21", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-21", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-21", "metric": "capacity_units", "label": "storage capacity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "storage capacity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_mis_pick_count_22(record):
    """Evaluate mis-picks for control WP-0221-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mis_pick_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-22", "metric": "mis_pick_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-22", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-22", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-22", "metric": "mis_pick_count", "label": "mis-picks",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "mis-picks falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_single_source_sku_count_23(record):
    """Evaluate single-source SKUs for control WP-0221-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("single_source_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-23", "metric": "single_source_sku_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-23", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-23", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-23", "metric": "single_source_sku_count", "label": "single-source SKUs",
        "status": "breach", "severity": "critical", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "single-source SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_cost_variance_pct_24(record):
    """Evaluate cost variance for control WP-0221-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0221-24", "metric": "cost_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0221-24", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0221-24", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0221-24", "metric": "cost_variance_pct", "label": "cost variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cost variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_telematics_gap_minutes_01, assess_approval_queue_age_hours_02, assess_supplier_subtier_visibility_pct_03, assess_supplier_packaging_validation_age_days_04, assess_supplier_export_control_gap_count_05, assess_supplier_dependency_count_06, assess_supplier_aftermarket_support_score_07, assess_supplier_service_recovery_score_08, assess_supplier_fai_completion_pct_09, assess_supplier_fire_response_drill_age_days_10, assess_supplier_ap_days_11, assess_supplier_knowledge_base_age_days_12, assess_supplier_bias_audit_age_days_13, assess_supplier_duplicate_event_pct_14, assess_supplier_pen_test_age_days_15, assess_supplier_secure_disposal_pct_16, assess_supplier_segregation_duty_pct_17, assess_supplier_capacity_allocation_pct_18, assess_supplier_carrier_handoff_pct_19, assess_supplier_asset_transfer_match_pct_20, assess_capacity_units_21, assess_mis_pick_count_22, assess_single_source_sku_count_23, assess_cost_variance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

