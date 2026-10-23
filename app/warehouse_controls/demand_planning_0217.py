"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_pack_station_queue_01(record):
    """Evaluate pack-station queue for control WP-0217-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_station_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-01", "metric": "pack_station_queue",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-01", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-01", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-01", "metric": "pack_station_queue", "label": "pack-station queue",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "pack-station queue exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_trade_compliance_score_02(record):
    """Evaluate trade compliance score for control WP-0217-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trade_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-02", "metric": "trade_compliance_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-02", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-02", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-02", "metric": "trade_compliance_score", "label": "trade compliance score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "trade compliance score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_preventable_accident_count_03(record):
    """Evaluate preventable accidents for control WP-0217-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventable_accident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-03", "metric": "preventable_accident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-03", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-03", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-03", "metric": "preventable_accident_count", "label": "preventable accidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "preventable accidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_equipment_cost_per_hour_04(record):
    """Evaluate equipment cost per hour for control WP-0217-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_cost_per_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-04", "metric": "equipment_cost_per_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-04", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-04", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-04", "metric": "equipment_cost_per_hour", "label": "equipment cost per hour",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment cost per hour must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_insurance_days_left_05(record):
    """Evaluate supplier insurance validity for control WP-0217-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-05", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-05", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-05", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-05", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier insurance validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_8d_age_days_06(record):
    """Evaluate supplier 8D report age for control WP-0217-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-06", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-06", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-06", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-06", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier 8D report age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_cost_breakdown_pct_07(record):
    """Evaluate supplier cost breakdown completeness for control WP-0217-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_breakdown_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-07", "metric": "supplier_cost_breakdown_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-07", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-07", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-07", "metric": "supplier_cost_breakdown_pct", "label": "supplier cost breakdown completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cost breakdown completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_test_evidence_pct_08(record):
    """Evaluate supplier test evidence completeness for control WP-0217-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_test_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-08", "metric": "supplier_test_evidence_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-08", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-08", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-08", "metric": "supplier_test_evidence_pct", "label": "supplier test evidence completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier test evidence completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_color_spec_match_pct_09(record):
    """Evaluate supplier color specification match for control WP-0217-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_color_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-09", "metric": "supplier_color_spec_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-09", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-09", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-09", "metric": "supplier_color_spec_match_pct", "label": "supplier color specification match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier color specification match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_dispatch_photo_pct_10(record):
    """Evaluate supplier dispatch photo completeness for control WP-0217-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-10", "metric": "supplier_dispatch_photo_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-10", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-10", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-10", "metric": "supplier_dispatch_photo_pct", "label": "supplier dispatch photo completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier dispatch photo completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_subtier_change_notice_days_11(record):
    """Evaluate supplier sub-tier change notice for control WP-0217-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-11", "metric": "supplier_subtier_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-11", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-11", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-11", "metric": "supplier_subtier_change_notice_days", "label": "supplier sub-tier change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sub-tier change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_packaging_epr_pct_12(record):
    """Evaluate supplier packaging EPR compliance for control WP-0217-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_epr_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-12", "metric": "supplier_packaging_epr_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-12", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-12", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-12", "metric": "supplier_packaging_epr_pct", "label": "supplier packaging EPR compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier packaging EPR compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_bank_change_review_age_hours_13(record):
    """Evaluate supplier bank-change review age for control WP-0217-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-13", "metric": "supplier_bank_change_review_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-13", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-13", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-13", "metric": "supplier_bank_change_review_age_hours", "label": "supplier bank-change review age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier bank-change review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_data_backup_success_pct_14(record):
    """Evaluate supplier data backup success for control WP-0217-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-14", "metric": "supplier_data_backup_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-14", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-14", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-14", "metric": "supplier_data_backup_success_pct", "label": "supplier data backup success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier data backup success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_model_incident_count_15(record):
    """Evaluate supplier model incidents for control WP-0217-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-15", "metric": "supplier_model_incident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-15", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-15", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-15", "metric": "supplier_model_incident_count", "label": "supplier model incidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model incidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_api_contract_drift_count_16(record):
    """Evaluate supplier API contract drift for control WP-0217-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_contract_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-16", "metric": "supplier_api_contract_drift_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-16", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-16", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-16", "metric": "supplier_api_contract_drift_count", "label": "supplier API contract drift",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier API contract drift must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_sso_success_pct_17(record):
    """Evaluate supplier SSO success for control WP-0217-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sso_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-17", "metric": "supplier_sso_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-17", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-17", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-17", "metric": "supplier_sso_success_pct", "label": "supplier SSO success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier SSO success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_anonymization_score_18(record):
    """Evaluate supplier anonymization score for control WP-0217-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_anonymization_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-18", "metric": "supplier_anonymization_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-18", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-18", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-18", "metric": "supplier_anonymization_score", "label": "supplier anonymization score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier anonymization score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_framework_coverage_pct_19(record):
    """Evaluate supplier framework coverage for control WP-0217-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_framework_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-19", "metric": "supplier_framework_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-19", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-19", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-19", "metric": "supplier_framework_coverage_pct", "label": "supplier framework coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier framework coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_rebate_capture_pct_20(record):
    """Evaluate supplier rebate capture for control WP-0217-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-20", "metric": "supplier_rebate_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-20", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-20", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-20", "metric": "supplier_rebate_capture_pct", "label": "supplier rebate capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier rebate capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_cycle_count_age_days_21(record):
    """Evaluate supplier cycle-count age for control WP-0217-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-21", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-21", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-21", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-21", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier cycle-count age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_data_migration_match_pct_22(record):
    """Evaluate supplier data migration match for control WP-0217-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-22", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-22", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-22", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-22", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier data migration match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_reserved_qty_23(record):
    """Evaluate reserved quantity for control WP-0217-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-23", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-23", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-23", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-23", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reserved quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_truck_fill_pct_24(record):
    """Evaluate truck fill rate for control WP-0217-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0217-24", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0217-24", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0217-24", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0217-24", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "truck fill rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_pack_station_queue_01, assess_trade_compliance_score_02, assess_preventable_accident_count_03, assess_equipment_cost_per_hour_04, assess_supplier_insurance_days_left_05, assess_supplier_8d_age_days_06, assess_supplier_cost_breakdown_pct_07, assess_supplier_test_evidence_pct_08, assess_supplier_color_spec_match_pct_09, assess_supplier_dispatch_photo_pct_10, assess_supplier_subtier_change_notice_days_11, assess_supplier_packaging_epr_pct_12, assess_supplier_bank_change_review_age_hours_13, assess_supplier_data_backup_success_pct_14, assess_supplier_model_incident_count_15, assess_supplier_api_contract_drift_count_16, assess_supplier_sso_success_pct_17, assess_supplier_anonymization_score_18, assess_supplier_framework_coverage_pct_19, assess_supplier_rebate_capture_pct_20, assess_supplier_cycle_count_age_days_21, assess_supplier_data_migration_match_pct_22, assess_reserved_qty_23, assess_truck_fill_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

