"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_restock_delay_hours_01(record):
    """Evaluate restock delay for control WP-0647-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restock_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-01", "metric": "restock_delay_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-01", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-01", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-01", "metric": "restock_delay_hours", "label": "restock delay",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restock delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_batch_release_approval_pct_02(record):
    """Evaluate batch release approval for control WP-0647-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-02", "metric": "batch_release_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-02", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-02", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-02", "metric": "batch_release_approval_pct", "label": "batch release approval",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "batch release approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_e_waste_manifest_pct_03(record):
    """Evaluate e-waste manifest completeness for control WP-0647-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("e_waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-03", "metric": "e_waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-03", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-03", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-03", "metric": "e_waste_manifest_pct", "label": "e-waste manifest completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "e-waste manifest completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_risk_assessment_age_days_04(record):
    """Evaluate risk assessment age for control WP-0647-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("risk_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-04", "metric": "risk_assessment_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-04", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-04", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-04", "metric": "risk_assessment_age_days", "label": "risk assessment age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "risk assessment age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_lighting_lux_05(record):
    """Evaluate lighting level for control WP-0647-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lighting_lux")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-05", "metric": "lighting_lux",
            "status": "insufficient_data",
            "severity": "critical", "unit": "lux",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-05", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-05", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-05", "metric": "lighting_lux", "label": "lighting level",
        "status": "breach", "severity": "critical", "unit": "lux",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lighting level must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_dependency_vulnerability_count_06(record):
    """Evaluate dependency vulnerabilities for control WP-0647-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dependency_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-06", "metric": "dependency_vulnerability_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-06", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-06", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-06", "metric": "dependency_vulnerability_count", "label": "dependency vulnerabilities",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dependency vulnerabilities must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_barcode_quality_score_07(record):
    """Evaluate barcode quality for control WP-0647-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("barcode_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-07", "metric": "barcode_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-07", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-07", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-07", "metric": "barcode_quality_score", "label": "barcode quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "barcode quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_inventory_writeoff_pct_08(record):
    """Evaluate inventory write-off rate for control WP-0647-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_writeoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-08", "metric": "inventory_writeoff_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-08", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-08", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-08", "metric": "inventory_writeoff_pct", "label": "inventory write-off rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "inventory write-off rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_pack_station_queue_09(record):
    """Evaluate pack-station queue for control WP-0647-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_station_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-09", "metric": "pack_station_queue",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-09", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-09", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-09", "metric": "pack_station_queue", "label": "pack-station queue",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pack-station queue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_trade_compliance_score_10(record):
    """Evaluate trade compliance score for control WP-0647-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trade_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-10", "metric": "trade_compliance_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-10", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-10", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-10", "metric": "trade_compliance_score", "label": "trade compliance score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trade compliance score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_preventable_accident_count_11(record):
    """Evaluate preventable accidents for control WP-0647-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventable_accident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-11", "metric": "preventable_accident_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-11", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-11", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-11", "metric": "preventable_accident_count", "label": "preventable accidents",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "preventable accidents exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_equipment_cost_per_hour_12(record):
    """Evaluate equipment cost per hour for control WP-0647-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_cost_per_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-12", "metric": "equipment_cost_per_hour",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-12", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-12", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-12", "metric": "equipment_cost_per_hour", "label": "equipment cost per hour",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "equipment cost per hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_insurance_days_left_13(record):
    """Evaluate supplier insurance validity for control WP-0647-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-13", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-13", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-13", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-13", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier insurance validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_8d_age_days_14(record):
    """Evaluate supplier 8D report age for control WP-0647-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-14", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-14", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-14", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-14", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier 8D report age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_cost_breakdown_pct_15(record):
    """Evaluate supplier cost breakdown completeness for control WP-0647-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_breakdown_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-15", "metric": "supplier_cost_breakdown_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-15", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-15", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-15", "metric": "supplier_cost_breakdown_pct", "label": "supplier cost breakdown completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier cost breakdown completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_test_evidence_pct_16(record):
    """Evaluate supplier test evidence completeness for control WP-0647-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_test_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-16", "metric": "supplier_test_evidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-16", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-16", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-16", "metric": "supplier_test_evidence_pct", "label": "supplier test evidence completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier test evidence completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_color_spec_match_pct_17(record):
    """Evaluate supplier color specification match for control WP-0647-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_color_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-17", "metric": "supplier_color_spec_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-17", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-17", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-17", "metric": "supplier_color_spec_match_pct", "label": "supplier color specification match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier color specification match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_dispatch_photo_pct_18(record):
    """Evaluate supplier dispatch photo completeness for control WP-0647-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-18", "metric": "supplier_dispatch_photo_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-18", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-18", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-18", "metric": "supplier_dispatch_photo_pct", "label": "supplier dispatch photo completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dispatch photo completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_subtier_change_notice_days_19(record):
    """Evaluate supplier sub-tier change notice for control WP-0647-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-19", "metric": "supplier_subtier_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-19", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-19", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-19", "metric": "supplier_subtier_change_notice_days", "label": "supplier sub-tier change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier sub-tier change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_packaging_epr_pct_20(record):
    """Evaluate supplier packaging EPR compliance for control WP-0647-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_epr_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-20", "metric": "supplier_packaging_epr_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-20", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-20", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-20", "metric": "supplier_packaging_epr_pct", "label": "supplier packaging EPR compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier packaging EPR compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_bank_change_review_age_hours_21(record):
    """Evaluate supplier bank-change review age for control WP-0647-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-21", "metric": "supplier_bank_change_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-21", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-21", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-21", "metric": "supplier_bank_change_review_age_hours", "label": "supplier bank-change review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier bank-change review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_data_backup_success_pct_22(record):
    """Evaluate supplier data backup success for control WP-0647-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-22", "metric": "supplier_data_backup_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-22", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-22", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-22", "metric": "supplier_data_backup_success_pct", "label": "supplier data backup success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data backup success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_model_incident_count_23(record):
    """Evaluate supplier model incidents for control WP-0647-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-23", "metric": "supplier_model_incident_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-23", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-23", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-23", "metric": "supplier_model_incident_count", "label": "supplier model incidents",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier model incidents exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_api_contract_drift_count_24(record):
    """Evaluate supplier API contract drift for control WP-0647-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_contract_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0647-24", "metric": "supplier_api_contract_drift_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0647-24", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0647-24", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0647-24", "metric": "supplier_api_contract_drift_count", "label": "supplier API contract drift",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier API contract drift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_restock_delay_hours_01, assess_batch_release_approval_pct_02, assess_e_waste_manifest_pct_03, assess_risk_assessment_age_days_04, assess_lighting_lux_05, assess_dependency_vulnerability_count_06, assess_barcode_quality_score_07, assess_inventory_writeoff_pct_08, assess_pack_station_queue_09, assess_trade_compliance_score_10, assess_preventable_accident_count_11, assess_equipment_cost_per_hour_12, assess_supplier_insurance_days_left_13, assess_supplier_8d_age_days_14, assess_supplier_cost_breakdown_pct_15, assess_supplier_test_evidence_pct_16, assess_supplier_color_spec_match_pct_17, assess_supplier_dispatch_photo_pct_18, assess_supplier_subtier_change_notice_days_19, assess_supplier_packaging_epr_pct_20, assess_supplier_bank_change_review_age_hours_21, assess_supplier_data_backup_success_pct_22, assess_supplier_model_incident_count_23, assess_supplier_api_contract_drift_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

