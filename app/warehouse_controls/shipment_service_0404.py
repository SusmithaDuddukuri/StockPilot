"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_barcode_quality_score_01(record):
    """Evaluate barcode quality for control WP-0404-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("barcode_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-01", "metric": "barcode_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-01", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-01", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-01", "metric": "barcode_quality_score", "label": "barcode quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "barcode quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_inventory_writeoff_pct_02(record):
    """Evaluate inventory write-off rate for control WP-0404-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_writeoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-02", "metric": "inventory_writeoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-02", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-02", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-02", "metric": "inventory_writeoff_pct", "label": "inventory write-off rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory write-off rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_pack_station_queue_03(record):
    """Evaluate pack-station queue for control WP-0404-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_station_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-03", "metric": "pack_station_queue",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-03", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-03", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-03", "metric": "pack_station_queue", "label": "pack-station queue",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pack-station queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_trade_compliance_score_04(record):
    """Evaluate trade compliance score for control WP-0404-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trade_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-04", "metric": "trade_compliance_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-04", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-04", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-04", "metric": "trade_compliance_score", "label": "trade compliance score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "trade compliance score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_preventable_accident_count_05(record):
    """Evaluate preventable accidents for control WP-0404-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventable_accident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-05", "metric": "preventable_accident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-05", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-05", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-05", "metric": "preventable_accident_count", "label": "preventable accidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "preventable accidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_equipment_cost_per_hour_06(record):
    """Evaluate equipment cost per hour for control WP-0404-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_cost_per_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-06", "metric": "equipment_cost_per_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-06", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-06", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-06", "metric": "equipment_cost_per_hour", "label": "equipment cost per hour",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "equipment cost per hour must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_insurance_days_left_07(record):
    """Evaluate supplier insurance validity for control WP-0404-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-07", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-07", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-07", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-07", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier insurance validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_8d_age_days_08(record):
    """Evaluate supplier 8D report age for control WP-0404-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-08", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-08", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-08", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-08", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier 8D report age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_cost_breakdown_pct_09(record):
    """Evaluate supplier cost breakdown completeness for control WP-0404-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_breakdown_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-09", "metric": "supplier_cost_breakdown_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-09", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-09", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-09", "metric": "supplier_cost_breakdown_pct", "label": "supplier cost breakdown completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier cost breakdown completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_test_evidence_pct_10(record):
    """Evaluate supplier test evidence completeness for control WP-0404-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_test_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-10", "metric": "supplier_test_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-10", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-10", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-10", "metric": "supplier_test_evidence_pct", "label": "supplier test evidence completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier test evidence completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_color_spec_match_pct_11(record):
    """Evaluate supplier color specification match for control WP-0404-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_color_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-11", "metric": "supplier_color_spec_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-11", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-11", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-11", "metric": "supplier_color_spec_match_pct", "label": "supplier color specification match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier color specification match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_dispatch_photo_pct_12(record):
    """Evaluate supplier dispatch photo completeness for control WP-0404-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-12", "metric": "supplier_dispatch_photo_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-12", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-12", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-12", "metric": "supplier_dispatch_photo_pct", "label": "supplier dispatch photo completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier dispatch photo completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_subtier_change_notice_days_13(record):
    """Evaluate supplier sub-tier change notice for control WP-0404-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-13", "metric": "supplier_subtier_change_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-13", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-13", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-13", "metric": "supplier_subtier_change_notice_days", "label": "supplier sub-tier change notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier sub-tier change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_packaging_epr_pct_14(record):
    """Evaluate supplier packaging EPR compliance for control WP-0404-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_epr_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-14", "metric": "supplier_packaging_epr_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-14", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-14", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-14", "metric": "supplier_packaging_epr_pct", "label": "supplier packaging EPR compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier packaging EPR compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_bank_change_review_age_hours_15(record):
    """Evaluate supplier bank-change review age for control WP-0404-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-15", "metric": "supplier_bank_change_review_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-15", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-15", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-15", "metric": "supplier_bank_change_review_age_hours", "label": "supplier bank-change review age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier bank-change review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_data_backup_success_pct_16(record):
    """Evaluate supplier data backup success for control WP-0404-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-16", "metric": "supplier_data_backup_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-16", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-16", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-16", "metric": "supplier_data_backup_success_pct", "label": "supplier data backup success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier data backup success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_model_incident_count_17(record):
    """Evaluate supplier model incidents for control WP-0404-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-17", "metric": "supplier_model_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-17", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-17", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-17", "metric": "supplier_model_incident_count", "label": "supplier model incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "supplier model incidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_api_contract_drift_count_18(record):
    """Evaluate supplier API contract drift for control WP-0404-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_contract_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-18", "metric": "supplier_api_contract_drift_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-18", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-18", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-18", "metric": "supplier_api_contract_drift_count", "label": "supplier API contract drift",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier API contract drift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_sso_success_pct_19(record):
    """Evaluate supplier SSO success for control WP-0404-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sso_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-19", "metric": "supplier_sso_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-19", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-19", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-19", "metric": "supplier_sso_success_pct", "label": "supplier SSO success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SSO success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_anonymization_score_20(record):
    """Evaluate supplier anonymization score for control WP-0404-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_anonymization_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-20", "metric": "supplier_anonymization_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-20", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-20", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-20", "metric": "supplier_anonymization_score", "label": "supplier anonymization score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier anonymization score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_framework_coverage_pct_21(record):
    """Evaluate supplier framework coverage for control WP-0404-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_framework_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-21", "metric": "supplier_framework_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-21", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-21", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-21", "metric": "supplier_framework_coverage_pct", "label": "supplier framework coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier framework coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_rebate_capture_pct_22(record):
    """Evaluate supplier rebate capture for control WP-0404-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-22", "metric": "supplier_rebate_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-22", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-22", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-22", "metric": "supplier_rebate_capture_pct", "label": "supplier rebate capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier rebate capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_cycle_count_age_days_23(record):
    """Evaluate supplier cycle-count age for control WP-0404-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-23", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-23", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-23", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-23", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cycle-count age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_data_migration_match_pct_24(record):
    """Evaluate supplier data migration match for control WP-0404-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0404-24", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0404-24", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0404-24", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0404-24", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier data migration match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_barcode_quality_score_01, assess_inventory_writeoff_pct_02, assess_pack_station_queue_03, assess_trade_compliance_score_04, assess_preventable_accident_count_05, assess_equipment_cost_per_hour_06, assess_supplier_insurance_days_left_07, assess_supplier_8d_age_days_08, assess_supplier_cost_breakdown_pct_09, assess_supplier_test_evidence_pct_10, assess_supplier_color_spec_match_pct_11, assess_supplier_dispatch_photo_pct_12, assess_supplier_subtier_change_notice_days_13, assess_supplier_packaging_epr_pct_14, assess_supplier_bank_change_review_age_hours_15, assess_supplier_data_backup_success_pct_16, assess_supplier_model_incident_count_17, assess_supplier_api_contract_drift_count_18, assess_supplier_sso_success_pct_19, assess_supplier_anonymization_score_20, assess_supplier_framework_coverage_pct_21, assess_supplier_rebate_capture_pct_22, assess_supplier_cycle_count_age_days_23, assess_supplier_data_migration_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

