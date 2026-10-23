"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_insurance_days_left_01(record):
    """Evaluate supplier insurance validity for control WP-0540-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-01", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-01", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-01", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-01", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier insurance validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_8d_age_days_02(record):
    """Evaluate supplier 8D report age for control WP-0540-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-02", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-02", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-02", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-02", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier 8D report age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_cost_breakdown_pct_03(record):
    """Evaluate supplier cost breakdown completeness for control WP-0540-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_breakdown_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-03", "metric": "supplier_cost_breakdown_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-03", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-03", "metric": "supplier_cost_breakdown_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-03", "metric": "supplier_cost_breakdown_pct", "label": "supplier cost breakdown completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cost breakdown completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_test_evidence_pct_04(record):
    """Evaluate supplier test evidence completeness for control WP-0540-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_test_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-04", "metric": "supplier_test_evidence_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-04", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-04", "metric": "supplier_test_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-04", "metric": "supplier_test_evidence_pct", "label": "supplier test evidence completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier test evidence completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_color_spec_match_pct_05(record):
    """Evaluate supplier color specification match for control WP-0540-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_color_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-05", "metric": "supplier_color_spec_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-05", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-05", "metric": "supplier_color_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-05", "metric": "supplier_color_spec_match_pct", "label": "supplier color specification match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier color specification match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_dispatch_photo_pct_06(record):
    """Evaluate supplier dispatch photo completeness for control WP-0540-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-06", "metric": "supplier_dispatch_photo_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-06", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-06", "metric": "supplier_dispatch_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-06", "metric": "supplier_dispatch_photo_pct", "label": "supplier dispatch photo completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dispatch photo completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_subtier_change_notice_days_07(record):
    """Evaluate supplier sub-tier change notice for control WP-0540-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subtier_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-07", "metric": "supplier_subtier_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-07", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-07", "metric": "supplier_subtier_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-07", "metric": "supplier_subtier_change_notice_days", "label": "supplier sub-tier change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sub-tier change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_packaging_epr_pct_08(record):
    """Evaluate supplier packaging EPR compliance for control WP-0540-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_packaging_epr_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-08", "metric": "supplier_packaging_epr_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-08", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-08", "metric": "supplier_packaging_epr_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-08", "metric": "supplier_packaging_epr_pct", "label": "supplier packaging EPR compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "supplier packaging EPR compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_bank_change_review_age_hours_09(record):
    """Evaluate supplier bank-change review age for control WP-0540-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bank_change_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-09", "metric": "supplier_bank_change_review_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-09", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-09", "metric": "supplier_bank_change_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-09", "metric": "supplier_bank_change_review_age_hours", "label": "supplier bank-change review age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "supplier bank-change review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_data_backup_success_pct_10(record):
    """Evaluate supplier data backup success for control WP-0540-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_backup_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-10", "metric": "supplier_data_backup_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-10", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-10", "metric": "supplier_data_backup_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-10", "metric": "supplier_data_backup_success_pct", "label": "supplier data backup success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data backup success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_model_incident_count_11(record):
    """Evaluate supplier model incidents for control WP-0540-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-11", "metric": "supplier_model_incident_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-11", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-11", "metric": "supplier_model_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-11", "metric": "supplier_model_incident_count", "label": "supplier model incidents",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model incidents must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_api_contract_drift_count_12(record):
    """Evaluate supplier API contract drift for control WP-0540-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_contract_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-12", "metric": "supplier_api_contract_drift_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-12", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-12", "metric": "supplier_api_contract_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-12", "metric": "supplier_api_contract_drift_count", "label": "supplier API contract drift",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "supplier API contract drift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_sso_success_pct_13(record):
    """Evaluate supplier SSO success for control WP-0540-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sso_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-13", "metric": "supplier_sso_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-13", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-13", "metric": "supplier_sso_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-13", "metric": "supplier_sso_success_pct", "label": "supplier SSO success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier SSO success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_anonymization_score_14(record):
    """Evaluate supplier anonymization score for control WP-0540-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_anonymization_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-14", "metric": "supplier_anonymization_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-14", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-14", "metric": "supplier_anonymization_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-14", "metric": "supplier_anonymization_score", "label": "supplier anonymization score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier anonymization score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_framework_coverage_pct_15(record):
    """Evaluate supplier framework coverage for control WP-0540-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_framework_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-15", "metric": "supplier_framework_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-15", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-15", "metric": "supplier_framework_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-15", "metric": "supplier_framework_coverage_pct", "label": "supplier framework coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier framework coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_rebate_capture_pct_16(record):
    """Evaluate supplier rebate capture for control WP-0540-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-16", "metric": "supplier_rebate_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-16", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-16", "metric": "supplier_rebate_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-16", "metric": "supplier_rebate_capture_pct", "label": "supplier rebate capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier rebate capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_cycle_count_age_days_17(record):
    """Evaluate supplier cycle-count age for control WP-0540-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cycle_count_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-17", "metric": "supplier_cycle_count_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-17", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-17", "metric": "supplier_cycle_count_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-17", "metric": "supplier_cycle_count_age_days", "label": "supplier cycle-count age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "supplier cycle-count age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_data_migration_match_pct_18(record):
    """Evaluate supplier data migration match for control WP-0540-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_migration_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-18", "metric": "supplier_data_migration_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-18", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-18", "metric": "supplier_data_migration_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-18", "metric": "supplier_data_migration_match_pct", "label": "supplier data migration match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data migration match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_reserved_qty_19(record):
    """Evaluate reserved quantity for control WP-0540-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserved_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-19", "metric": "reserved_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-19", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-19", "metric": "reserved_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-19", "metric": "reserved_qty", "label": "reserved quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "reserved quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_truck_fill_pct_20(record):
    """Evaluate truck fill rate for control WP-0540-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("truck_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-20", "metric": "truck_fill_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-20", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-20", "metric": "truck_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-20", "metric": "truck_fill_pct", "label": "truck fill rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "truck fill rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_proof_of_delivery_pct_21(record):
    """Evaluate proof of delivery for control WP-0540-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_of_delivery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-21", "metric": "proof_of_delivery_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-21", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-21", "metric": "proof_of_delivery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-21", "metric": "proof_of_delivery_pct", "label": "proof of delivery",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "proof of delivery falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_duplicate_sku_count_22(record):
    """Evaluate duplicate SKUs for control WP-0540-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("duplicate_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-22", "metric": "duplicate_sku_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-22", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-22", "metric": "duplicate_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-22", "metric": "duplicate_sku_count", "label": "duplicate SKUs",
        "status": "breach", "severity": "medium", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_restockable_return_pct_23(record):
    """Evaluate restockable returns for control WP-0540-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restockable_return_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-23", "metric": "restockable_return_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-23", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-23", "metric": "restockable_return_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-23", "metric": "restockable_return_pct", "label": "restockable returns",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restockable returns must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_scale_calibration_age_days_24(record):
    """Evaluate scale calibration age for control WP-0540-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0540-24", "metric": "scale_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0540-24", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0540-24", "metric": "scale_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0540-24", "metric": "scale_calibration_age_days", "label": "scale calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "scale calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_insurance_days_left_01, assess_supplier_8d_age_days_02, assess_supplier_cost_breakdown_pct_03, assess_supplier_test_evidence_pct_04, assess_supplier_color_spec_match_pct_05, assess_supplier_dispatch_photo_pct_06, assess_supplier_subtier_change_notice_days_07, assess_supplier_packaging_epr_pct_08, assess_supplier_bank_change_review_age_hours_09, assess_supplier_data_backup_success_pct_10, assess_supplier_model_incident_count_11, assess_supplier_api_contract_drift_count_12, assess_supplier_sso_success_pct_13, assess_supplier_anonymization_score_14, assess_supplier_framework_coverage_pct_15, assess_supplier_rebate_capture_pct_16, assess_supplier_cycle_count_age_days_17, assess_supplier_data_migration_match_pct_18, assess_reserved_qty_19, assess_truck_fill_pct_20, assess_proof_of_delivery_pct_21, assess_duplicate_sku_count_22, assess_restockable_return_pct_23, assess_scale_calibration_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

