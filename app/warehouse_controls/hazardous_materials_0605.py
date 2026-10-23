"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_ppm_defects_01(record):
    """Evaluate supplier PPM defects for control WP-0605-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppm_defects")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-01", "metric": "supplier_ppm_defects",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ppm",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-01", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-01", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-01", "metric": "supplier_ppm_defects", "label": "supplier PPM defects",
        "status": "breach", "severity": "medium", "unit": "ppm",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier PPM defects exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_credit_note_age_days_02(record):
    """Evaluate supplier credit-note age for control WP-0605-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-02", "metric": "supplier_credit_note_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-02", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-02", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-02", "metric": "supplier_credit_note_age_days", "label": "supplier credit-note age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier credit-note age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_release_notice_days_03(record):
    """Evaluate supplier release notice for control WP-0605-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-03", "metric": "supplier_release_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-03", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-03", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-03", "metric": "supplier_release_notice_days", "label": "supplier release notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier release notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dimension_spec_match_pct_04(record):
    """Evaluate supplier dimension specification match for control WP-0605-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dimension_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-04", "metric": "supplier_dimension_spec_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-04", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-04", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-04", "metric": "supplier_dimension_spec_match_pct", "label": "supplier dimension specification match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dimension specification match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_seal_control_pct_05(record):
    """Evaluate supplier seal control for control WP-0605-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seal_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-05", "metric": "supplier_seal_control_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-05", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-05", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-05", "metric": "supplier_seal_control_pct", "label": "supplier seal control",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier seal control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_material_change_notice_days_06(record):
    """Evaluate supplier material-change notice for control WP-0605-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-06", "metric": "supplier_material_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-06", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-06", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-06", "metric": "supplier_material_change_notice_days", "label": "supplier material-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier material-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_reach_compliance_pct_07(record):
    """Evaluate supplier REACH compliance for control WP-0605-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reach_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-07", "metric": "supplier_reach_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-07", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-07", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-07", "metric": "supplier_reach_compliance_pct", "label": "supplier REACH compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier REACH compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_country_of_risk_score_08(record):
    """Evaluate supplier country-of-risk score for control WP-0605-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_of_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-08", "metric": "supplier_country_of_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-08", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-08", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-08", "metric": "supplier_country_of_risk_score", "label": "supplier country-of-risk score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier country-of-risk score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_fuel_storage_hours_09(record):
    """Evaluate supplier fuel storage for control WP-0605-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fuel_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-09", "metric": "supplier_fuel_storage_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-09", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-09", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-09", "metric": "supplier_fuel_storage_hours", "label": "supplier fuel storage",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier fuel storage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_data_access_review_age_days_10(record):
    """Evaluate supplier data-access review age for control WP-0605-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-10", "metric": "supplier_data_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-10", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-10", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-10", "metric": "supplier_data_access_review_age_days", "label": "supplier data-access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "supplier data-access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_rollback_readiness_pct_11(record):
    """Evaluate supplier rollback readiness for control WP-0605-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rollback_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-11", "metric": "supplier_rollback_readiness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-11", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-11", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-11", "metric": "supplier_rollback_readiness_pct", "label": "supplier rollback readiness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier rollback readiness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_identity_federation_pct_12(record):
    """Evaluate supplier identity federation for control WP-0605-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_identity_federation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-12", "metric": "supplier_identity_federation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-12", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-12", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-12", "metric": "supplier_identity_federation_pct", "label": "supplier identity federation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier identity federation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_retention_exception_count_13(record):
    """Evaluate supplier retention exceptions for control WP-0605-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-13", "metric": "supplier_retention_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-13", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-13", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-13", "metric": "supplier_retention_exception_count", "label": "supplier retention exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier retention exceptions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_policy_exception_age_days_14(record):
    """Evaluate supplier policy exception age for control WP-0605-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-14", "metric": "supplier_policy_exception_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-14", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-14", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-14", "metric": "supplier_policy_exception_age_days", "label": "supplier policy exception age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier policy exception age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_late_payment_fee_cost_15(record):
    """Evaluate late-payment fee cost for control WP-0605-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_late_payment_fee_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-15", "metric": "supplier_late_payment_fee_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-15", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-15", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-15", "metric": "supplier_late_payment_fee_cost", "label": "late-payment fee cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "late-payment fee cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_raw_material_cover_days_16(record):
    """Evaluate supplier raw-material cover for control WP-0605-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-16", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-16", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-16", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-16", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier raw-material cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_cutover_readiness_pct_17(record):
    """Evaluate supplier cutover readiness for control WP-0605-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-17", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-17", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-17", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-17", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier cutover readiness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_quantity_18(record):
    """Evaluate on-hand quantity for control WP-0605-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quantity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-18", "metric": "quantity",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-18", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-18", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-18", "metric": "quantity", "label": "on-hand quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "on-hand quantity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_overtime_hours_19(record):
    """Evaluate overtime hours for control WP-0605-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-19", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-19", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-19", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-19", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "overtime hours must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_break_compliance_pct_20(record):
    """Evaluate break compliance for control WP-0605-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-20", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-20", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-20", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-20", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "break compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_restore_test_age_days_21(record):
    """Evaluate restore test age for control WP-0605-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-21", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-21", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-21", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-21", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "restore test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_claim_age_days_22(record):
    """Evaluate claim age for control WP-0605-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-22", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-22", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-22", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-22", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "claim age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_trailer_seal_age_hours_23(record):
    """Evaluate trailer seal age for control WP-0605-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-23", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-23", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-23", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-23", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trailer seal age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_accessibility_score_24(record):
    """Evaluate accessibility score for control WP-0605-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0605-24", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0605-24", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0605-24", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0605-24", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "accessibility score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_ppm_defects_01, assess_supplier_credit_note_age_days_02, assess_supplier_release_notice_days_03, assess_supplier_dimension_spec_match_pct_04, assess_supplier_seal_control_pct_05, assess_supplier_material_change_notice_days_06, assess_supplier_reach_compliance_pct_07, assess_supplier_country_of_risk_score_08, assess_supplier_fuel_storage_hours_09, assess_supplier_data_access_review_age_days_10, assess_supplier_rollback_readiness_pct_11, assess_supplier_identity_federation_pct_12, assess_supplier_retention_exception_count_13, assess_supplier_policy_exception_age_days_14, assess_supplier_late_payment_fee_cost_15, assess_supplier_raw_material_cover_days_16, assess_supplier_cutover_readiness_pct_17, assess_quantity_18, assess_overtime_hours_19, assess_break_compliance_pct_20, assess_restore_test_age_days_21, assess_claim_age_days_22, assess_trailer_seal_age_hours_23, assess_accessibility_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

