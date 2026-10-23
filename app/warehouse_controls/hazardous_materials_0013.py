"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_heat_stress_score_01(record):
    """Evaluate heat stress for control WP-0013-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("heat_stress_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-01", "metric": "heat_stress_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-01", "metric": "heat_stress_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-01", "metric": "heat_stress_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-01", "metric": "heat_stress_score", "label": "heat stress",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "heat stress exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_restock_delay_hours_02(record):
    """Evaluate restock delay for control WP-0013-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restock_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-02", "metric": "restock_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-02", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-02", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-02", "metric": "restock_delay_hours", "label": "restock delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "restock delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_batch_release_approval_pct_03(record):
    """Evaluate batch release approval for control WP-0013-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-03", "metric": "batch_release_approval_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-03", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-03", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-03", "metric": "batch_release_approval_pct", "label": "batch release approval",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "batch release approval must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_e_waste_manifest_pct_04(record):
    """Evaluate e-waste manifest completeness for control WP-0013-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("e_waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-04", "metric": "e_waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-04", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-04", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-04", "metric": "e_waste_manifest_pct", "label": "e-waste manifest completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "e-waste manifest completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_risk_assessment_age_days_05(record):
    """Evaluate risk assessment age for control WP-0013-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("risk_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-05", "metric": "risk_assessment_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-05", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-05", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-05", "metric": "risk_assessment_age_days", "label": "risk assessment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "risk assessment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_lighting_lux_06(record):
    """Evaluate lighting level for control WP-0013-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lighting_lux")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-06", "metric": "lighting_lux",
            "status": "insufficient_data",
            "severity": "high", "unit": "lux",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-06", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-06", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-06", "metric": "lighting_lux", "label": "lighting level",
        "status": "breach", "severity": "high", "unit": "lux",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "lighting level falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_dependency_vulnerability_count_07(record):
    """Evaluate dependency vulnerabilities for control WP-0013-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dependency_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-07", "metric": "dependency_vulnerability_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-07", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-07", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-07", "metric": "dependency_vulnerability_count", "label": "dependency vulnerabilities",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dependency vulnerabilities must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_barcode_quality_score_08(record):
    """Evaluate barcode quality for control WP-0013-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("barcode_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-08", "metric": "barcode_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-08", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-08", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-08", "metric": "barcode_quality_score", "label": "barcode quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "barcode quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_inventory_writeoff_pct_09(record):
    """Evaluate inventory write-off rate for control WP-0013-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_writeoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-09", "metric": "inventory_writeoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-09", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-09", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-09", "metric": "inventory_writeoff_pct", "label": "inventory write-off rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "inventory write-off rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_pack_station_queue_10(record):
    """Evaluate pack-station queue for control WP-0013-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_station_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-10", "metric": "pack_station_queue",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-10", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-10", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-10", "metric": "pack_station_queue", "label": "pack-station queue",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "pack-station queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_trade_compliance_score_11(record):
    """Evaluate trade compliance score for control WP-0013-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trade_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-11", "metric": "trade_compliance_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-11", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-11", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-11", "metric": "trade_compliance_score", "label": "trade compliance score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trade compliance score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_preventable_accident_count_12(record):
    """Evaluate preventable accidents for control WP-0013-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventable_accident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-12", "metric": "preventable_accident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-12", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-12", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-12", "metric": "preventable_accident_count", "label": "preventable accidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "preventable accidents must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_equipment_cost_per_hour_13(record):
    """Evaluate equipment cost per hour for control WP-0013-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_cost_per_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-13", "metric": "equipment_cost_per_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-13", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-13", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-13", "metric": "equipment_cost_per_hour", "label": "equipment cost per hour",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "equipment cost per hour exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_insurance_days_left_14(record):
    """Evaluate supplier insurance validity for control WP-0013-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-14", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-14", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-14", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-14", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier insurance validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_8d_age_days_15(record):
    """Evaluate supplier 8D report age for control WP-0013-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-15", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-15", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-15", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-15", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier 8D report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_cost_breakdown_pct_16(record):
    """Evaluate supplier cost breakdown completeness for control WP-0013-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_breakdown_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-16", "metric": "supplier_cost_breakdown_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-16", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-16", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-16", "metric": "supplier_cost_breakdown_pct", "label": "supplier cost breakdown completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cost breakdown completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_test_evidence_pct_17(record):
    """Evaluate supplier test evidence completeness for control WP-0013-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_test_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-17", "metric": "supplier_test_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-17", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-17", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-17", "metric": "supplier_test_evidence_pct", "label": "supplier test evidence completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier test evidence completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_color_spec_match_pct_18(record):
    """Evaluate supplier color specification match for control WP-0013-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_color_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-18", "metric": "supplier_color_spec_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-18", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-18", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-18", "metric": "supplier_color_spec_match_pct", "label": "supplier color specification match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "supplier color specification match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dispatch_photo_pct_19(record):
    """Evaluate supplier dispatch photo completeness for control WP-0013-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-19", "metric": "supplier_dispatch_photo_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-19", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-19", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-19", "metric": "supplier_dispatch_photo_pct", "label": "supplier dispatch photo completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dispatch photo completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_subtier_change_notice_days_20(record):
    """Evaluate supplier sub-tier change notice for control WP-0013-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-20", "metric": "supplier_subtier_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-20", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-20", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-20", "metric": "supplier_subtier_change_notice_days", "label": "supplier sub-tier change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-tier change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_packaging_epr_pct_21(record):
    """Evaluate supplier packaging EPR compliance for control WP-0013-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_epr_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-21", "metric": "supplier_packaging_epr_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-21", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-21", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-21", "metric": "supplier_packaging_epr_pct", "label": "supplier packaging EPR compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "supplier packaging EPR compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_bank_change_review_age_hours_22(record):
    """Evaluate supplier bank-change review age for control WP-0013-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-22", "metric": "supplier_bank_change_review_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-22", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-22", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-22", "metric": "supplier_bank_change_review_age_hours", "label": "supplier bank-change review age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier bank-change review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_data_backup_success_pct_23(record):
    """Evaluate supplier data backup success for control WP-0013-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-23", "metric": "supplier_data_backup_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-23", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-23", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-23", "metric": "supplier_data_backup_success_pct", "label": "supplier data backup success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data backup success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_model_incident_count_24(record):
    """Evaluate supplier model incidents for control WP-0013-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0013-24", "metric": "supplier_model_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0013-24", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0013-24", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0013-24", "metric": "supplier_model_incident_count", "label": "supplier model incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model incidents must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_heat_stress_score_01, assess_restock_delay_hours_02, assess_batch_release_approval_pct_03, assess_e_waste_manifest_pct_04, assess_risk_assessment_age_days_05, assess_lighting_lux_06, assess_dependency_vulnerability_count_07, assess_barcode_quality_score_08, assess_inventory_writeoff_pct_09, assess_pack_station_queue_10, assess_trade_compliance_score_11, assess_preventable_accident_count_12, assess_equipment_cost_per_hour_13, assess_supplier_insurance_days_left_14, assess_supplier_8d_age_days_15, assess_supplier_cost_breakdown_pct_16, assess_supplier_test_evidence_pct_17, assess_supplier_color_spec_match_pct_18, assess_supplier_dispatch_photo_pct_19, assess_supplier_subtier_change_notice_days_20, assess_supplier_packaging_epr_pct_21, assess_supplier_bank_change_review_age_hours_22, assess_supplier_data_backup_success_pct_23, assess_supplier_model_incident_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

