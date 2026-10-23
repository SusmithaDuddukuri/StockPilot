"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_material_change_notice_days_01(record):
    """Evaluate supplier material-change notice for control WP-0107-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-01", "metric": "supplier_material_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-01", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-01", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-01", "metric": "supplier_material_change_notice_days", "label": "supplier material-change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier material-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_reach_compliance_pct_02(record):
    """Evaluate supplier REACH compliance for control WP-0107-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reach_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-02", "metric": "supplier_reach_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-02", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-02", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-02", "metric": "supplier_reach_compliance_pct", "label": "supplier REACH compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier REACH compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_country_of_risk_score_03(record):
    """Evaluate supplier country-of-risk score for control WP-0107-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_of_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-03", "metric": "supplier_country_of_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-03", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-03", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-03", "metric": "supplier_country_of_risk_score", "label": "supplier country-of-risk score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier country-of-risk score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_fuel_storage_hours_04(record):
    """Evaluate supplier fuel storage for control WP-0107-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fuel_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-04", "metric": "supplier_fuel_storage_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-04", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-04", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-04", "metric": "supplier_fuel_storage_hours", "label": "supplier fuel storage",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier fuel storage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_data_access_review_age_days_05(record):
    """Evaluate supplier data-access review age for control WP-0107-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-05", "metric": "supplier_data_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-05", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-05", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-05", "metric": "supplier_data_access_review_age_days", "label": "supplier data-access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_rollback_readiness_pct_06(record):
    """Evaluate supplier rollback readiness for control WP-0107-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rollback_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-06", "metric": "supplier_rollback_readiness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-06", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-06", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-06", "metric": "supplier_rollback_readiness_pct", "label": "supplier rollback readiness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier rollback readiness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_identity_federation_pct_07(record):
    """Evaluate supplier identity federation for control WP-0107-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_identity_federation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-07", "metric": "supplier_identity_federation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-07", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-07", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-07", "metric": "supplier_identity_federation_pct", "label": "supplier identity federation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier identity federation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_retention_exception_count_08(record):
    """Evaluate supplier retention exceptions for control WP-0107-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-08", "metric": "supplier_retention_exception_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-08", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-08", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-08", "metric": "supplier_retention_exception_count", "label": "supplier retention exceptions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier retention exceptions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_policy_exception_age_days_09(record):
    """Evaluate supplier policy exception age for control WP-0107-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-09", "metric": "supplier_policy_exception_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-09", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-09", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-09", "metric": "supplier_policy_exception_age_days", "label": "supplier policy exception age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier policy exception age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_late_payment_fee_cost_10(record):
    """Evaluate late-payment fee cost for control WP-0107-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_late_payment_fee_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-10", "metric": "supplier_late_payment_fee_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-10", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-10", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-10", "metric": "supplier_late_payment_fee_cost", "label": "late-payment fee cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "late-payment fee cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_raw_material_cover_days_11(record):
    """Evaluate supplier raw-material cover for control WP-0107-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-11", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-11", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-11", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-11", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier raw-material cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_cutover_readiness_pct_12(record):
    """Evaluate supplier cutover readiness for control WP-0107-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-12", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-12", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-12", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-12", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier cutover readiness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_quantity_13(record):
    """Evaluate on-hand quantity for control WP-0107-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quantity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-13", "metric": "quantity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-13", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-13", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-13", "metric": "quantity", "label": "on-hand quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "on-hand quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_overtime_hours_14(record):
    """Evaluate overtime hours for control WP-0107-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-14", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-14", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-14", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-14", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "overtime hours must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_break_compliance_pct_15(record):
    """Evaluate break compliance for control WP-0107-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-15", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-15", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-15", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-15", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "break compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_restore_test_age_days_16(record):
    """Evaluate restore test age for control WP-0107-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-16", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-16", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-16", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-16", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "restore test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_claim_age_days_17(record):
    """Evaluate claim age for control WP-0107-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-17", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-17", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-17", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-17", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "claim age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_trailer_seal_age_hours_18(record):
    """Evaluate trailer seal age for control WP-0107-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-18", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-18", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-18", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-18", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trailer seal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_accessibility_score_19(record):
    """Evaluate accessibility score for control WP-0107-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-19", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-19", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-19", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-19", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "accessibility score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_conveyor_jam_count_20(record):
    """Evaluate conveyor jams for control WP-0107-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_jam_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-20", "metric": "conveyor_jam_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-20", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-20", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-20", "metric": "conveyor_jam_count", "label": "conveyor jams",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "conveyor jams falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_seal_audit_gap_count_21(record):
    """Evaluate seal audit gaps for control WP-0107-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-21", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-21", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-21", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-21", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seal audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_cold_room_door_open_minutes_22(record):
    """Evaluate cold-room door open time for control WP-0107-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-22", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-22", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-22", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-22", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cold-room door open time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_serial_activation_match_pct_23(record):
    """Evaluate serial activation match for control WP-0107-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-23", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-23", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-23", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-23", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "serial activation match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_site_induction_age_days_24(record):
    """Evaluate site induction age for control WP-0107-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0107-24", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0107-24", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0107-24", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0107-24", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "site induction age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_material_change_notice_days_01, assess_supplier_reach_compliance_pct_02, assess_supplier_country_of_risk_score_03, assess_supplier_fuel_storage_hours_04, assess_supplier_data_access_review_age_days_05, assess_supplier_rollback_readiness_pct_06, assess_supplier_identity_federation_pct_07, assess_supplier_retention_exception_count_08, assess_supplier_policy_exception_age_days_09, assess_supplier_late_payment_fee_cost_10, assess_supplier_raw_material_cover_days_11, assess_supplier_cutover_readiness_pct_12, assess_quantity_13, assess_overtime_hours_14, assess_break_compliance_pct_15, assess_restore_test_age_days_16, assess_claim_age_days_17, assess_trailer_seal_age_hours_18, assess_accessibility_score_19, assess_conveyor_jam_count_20, assess_seal_audit_gap_count_21, assess_cold_room_door_open_minutes_22, assess_serial_activation_match_pct_23, assess_site_induction_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

