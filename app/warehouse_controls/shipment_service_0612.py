"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_service_recovery_score_01(record):
    """Evaluate supplier service recovery for control WP-0612-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_recovery_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-01", "metric": "supplier_service_recovery_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-01", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-01", "metric": "supplier_service_recovery_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-01", "metric": "supplier_service_recovery_score", "label": "supplier service recovery",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier service recovery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_fai_completion_pct_02(record):
    """Evaluate supplier first-article inspection for control WP-0612-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fai_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-02", "metric": "supplier_fai_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-02", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-02", "metric": "supplier_fai_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-02", "metric": "supplier_fai_completion_pct", "label": "supplier first-article inspection",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier first-article inspection must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_fire_response_drill_age_days_03(record):
    """Evaluate supplier fire drill age for control WP-0612-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-03", "metric": "supplier_fire_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-03", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-03", "metric": "supplier_fire_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-03", "metric": "supplier_fire_response_drill_age_days", "label": "supplier fire drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier fire drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_ap_days_04(record):
    """Evaluate supplier accounts-payable days for control WP-0612-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ap_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-04", "metric": "supplier_ap_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-04", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-04", "metric": "supplier_ap_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-04", "metric": "supplier_ap_days", "label": "supplier accounts-payable days",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier accounts-payable days exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_knowledge_base_age_days_05(record):
    """Evaluate supplier knowledge-base age for control WP-0612-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_base_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-05", "metric": "supplier_knowledge_base_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-05", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-05", "metric": "supplier_knowledge_base_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-05", "metric": "supplier_knowledge_base_age_days", "label": "supplier knowledge-base age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "supplier knowledge-base age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_bias_audit_age_days_06(record):
    """Evaluate supplier bias-audit age for control WP-0612-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bias_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-06", "metric": "supplier_bias_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-06", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-06", "metric": "supplier_bias_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-06", "metric": "supplier_bias_audit_age_days", "label": "supplier bias-audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier bias-audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_duplicate_event_pct_07(record):
    """Evaluate supplier duplicate event rate for control WP-0612-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_event_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-07", "metric": "supplier_duplicate_event_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-07", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-07", "metric": "supplier_duplicate_event_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-07", "metric": "supplier_duplicate_event_pct", "label": "supplier duplicate event rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier duplicate event rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_pen_test_age_days_08(record):
    """Evaluate supplier penetration-test age for control WP-0612-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pen_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-08", "metric": "supplier_pen_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-08", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-08", "metric": "supplier_pen_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-08", "metric": "supplier_pen_test_age_days", "label": "supplier penetration-test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier penetration-test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_secure_disposal_pct_09(record):
    """Evaluate supplier secure disposal for control WP-0612-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_disposal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-09", "metric": "supplier_secure_disposal_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-09", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-09", "metric": "supplier_secure_disposal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-09", "metric": "supplier_secure_disposal_pct", "label": "supplier secure disposal",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier secure disposal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_segregation_duty_pct_10(record):
    """Evaluate supplier segregation of duties for control WP-0612-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_segregation_duty_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-10", "metric": "supplier_segregation_duty_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-10", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-10", "metric": "supplier_segregation_duty_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-10", "metric": "supplier_segregation_duty_pct", "label": "supplier segregation of duties",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier segregation of duties must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_capacity_allocation_pct_11(record):
    """Evaluate supplier capacity allocation for control WP-0612-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_allocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-11", "metric": "supplier_capacity_allocation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-11", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-11", "metric": "supplier_capacity_allocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-11", "metric": "supplier_capacity_allocation_pct", "label": "supplier capacity allocation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity allocation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_carrier_handoff_pct_12(record):
    """Evaluate supplier carrier handoff for control WP-0612-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_carrier_handoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-12", "metric": "supplier_carrier_handoff_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-12", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-12", "metric": "supplier_carrier_handoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-12", "metric": "supplier_carrier_handoff_pct", "label": "supplier carrier handoff",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier carrier handoff exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_asset_transfer_match_pct_13(record):
    """Evaluate asset transfer match for control WP-0612-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-13", "metric": "supplier_asset_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-13", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-13", "metric": "supplier_asset_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-13", "metric": "supplier_asset_transfer_match_pct", "label": "asset transfer match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "asset transfer match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_capacity_units_14(record):
    """Evaluate storage capacity for control WP-0612-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capacity_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-14", "metric": "capacity_units",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-14", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-14", "metric": "capacity_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-14", "metric": "capacity_units", "label": "storage capacity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage capacity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_mis_pick_count_15(record):
    """Evaluate mis-picks for control WP-0612-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mis_pick_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-15", "metric": "mis_pick_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-15", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-15", "metric": "mis_pick_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-15", "metric": "mis_pick_count", "label": "mis-picks",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "mis-picks must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_single_source_sku_count_16(record):
    """Evaluate single-source SKUs for control WP-0612-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("single_source_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-16", "metric": "single_source_sku_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "SKUs",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-16", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-16", "metric": "single_source_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-16", "metric": "single_source_sku_count", "label": "single-source SKUs",
        "status": "breach", "severity": "critical", "unit": "SKUs",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "single-source SKUs exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_cost_variance_pct_17(record):
    """Evaluate cost variance for control WP-0612-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-17", "metric": "cost_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-17", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-17", "metric": "cost_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-17", "metric": "cost_variance_pct", "label": "cost variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "cost variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_water_liters_per_order_18(record):
    """Evaluate water per order for control WP-0612-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_liters_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-18", "metric": "water_liters_per_order",
            "status": "insufficient_data",
            "severity": "medium", "unit": "liters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-18", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-18", "metric": "water_liters_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-18", "metric": "water_liters_per_order", "label": "water per order",
        "status": "breach", "severity": "medium", "unit": "liters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "water per order must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_regulatory_document_age_days_19(record):
    """Evaluate regulatory document age for control WP-0612-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("regulatory_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-19", "metric": "regulatory_document_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-19", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-19", "metric": "regulatory_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-19", "metric": "regulatory_document_age_days", "label": "regulatory document age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "regulatory document age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_consent_record_pct_20(record):
    """Evaluate consent records completeness for control WP-0612-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("consent_record_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-20", "metric": "consent_record_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-20", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-20", "metric": "consent_record_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-20", "metric": "consent_record_pct", "label": "consent records completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "consent records completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_spill_kit_check_age_days_21(record):
    """Evaluate spill-kit check age for control WP-0612-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spill_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-21", "metric": "spill_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-21", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-21", "metric": "spill_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-21", "metric": "spill_kit_check_age_days", "label": "spill-kit check age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "spill-kit check age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_delivery_attempts_22(record):
    """Evaluate delivery attempts for control WP-0612-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_attempts")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-22", "metric": "delivery_attempts",
            "status": "insufficient_data",
            "severity": "medium", "unit": "attempts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-22", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-22", "metric": "delivery_attempts", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-22", "metric": "delivery_attempts", "label": "delivery attempts",
        "status": "breach", "severity": "medium", "unit": "attempts",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery attempts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_sensor_battery_pct_23(record):
    """Evaluate sensor battery for control WP-0612-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-23", "metric": "sensor_battery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-23", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-23", "metric": "sensor_battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-23", "metric": "sensor_battery_pct", "label": "sensor battery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sensor battery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_repair_first_time_fix_pct_24(record):
    """Evaluate first-time fix rate for control WP-0612-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_first_time_fix_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0612-24", "metric": "repair_first_time_fix_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0612-24", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0612-24", "metric": "repair_first_time_fix_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0612-24", "metric": "repair_first_time_fix_pct", "label": "first-time fix rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "first-time fix rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_service_recovery_score_01, assess_supplier_fai_completion_pct_02, assess_supplier_fire_response_drill_age_days_03, assess_supplier_ap_days_04, assess_supplier_knowledge_base_age_days_05, assess_supplier_bias_audit_age_days_06, assess_supplier_duplicate_event_pct_07, assess_supplier_pen_test_age_days_08, assess_supplier_secure_disposal_pct_09, assess_supplier_segregation_duty_pct_10, assess_supplier_capacity_allocation_pct_11, assess_supplier_carrier_handoff_pct_12, assess_supplier_asset_transfer_match_pct_13, assess_capacity_units_14, assess_mis_pick_count_15, assess_single_source_sku_count_16, assess_cost_variance_pct_17, assess_water_liters_per_order_18, assess_regulatory_document_age_days_19, assess_consent_record_pct_20, assess_spill_kit_check_age_days_21, assess_delivery_attempts_22, assess_sensor_battery_pct_23, assess_repair_first_time_fix_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

