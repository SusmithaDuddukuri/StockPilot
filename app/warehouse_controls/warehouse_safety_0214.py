"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_scale_zero_drift_01(record):
    """Evaluate scale zero drift for control WP-0214-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_zero_drift")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-01", "metric": "scale_zero_drift",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-01", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-01", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-01", "metric": "scale_zero_drift", "label": "scale zero drift",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "scale zero drift must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_variance_approval_age_hours_02(record):
    """Evaluate variance approval age for control WP-0214-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("variance_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-02", "metric": "variance_approval_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-02", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-02", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-02", "metric": "variance_approval_age_hours", "label": "variance approval age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "variance approval age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_pick_substitution_pct_03(record):
    """Evaluate pick substitution rate for control WP-0214-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_substitution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-03", "metric": "pick_substitution_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-03", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-03", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-03", "metric": "pick_substitution_pct", "label": "pick substitution rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "pick substitution rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_customs_exam_age_hours_04(record):
    """Evaluate customs exam age for control WP-0214-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_exam_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-04", "metric": "customs_exam_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-04", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-04", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-04", "metric": "customs_exam_age_hours", "label": "customs exam age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customs exam age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_fleet_utilization_pct_05(record):
    """Evaluate fleet utilization for control WP-0214-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fleet_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-05", "metric": "fleet_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-05", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-05", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-05", "metric": "fleet_utilization_pct", "label": "fleet utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fleet utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_travel_time_pct_06(record):
    """Evaluate travel time share for control WP-0214-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("travel_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-06", "metric": "travel_time_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-06", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-06", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-06", "metric": "travel_time_pct", "label": "travel time share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "travel time share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_audit_score_07(record):
    """Evaluate supplier audit score for control WP-0214-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-07", "metric": "supplier_audit_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-07", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-07", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-07", "metric": "supplier_audit_score", "label": "supplier audit score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier audit score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_ppm_defects_08(record):
    """Evaluate supplier PPM defects for control WP-0214-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppm_defects")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-08", "metric": "supplier_ppm_defects",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ppm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-08", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-08", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-08", "metric": "supplier_ppm_defects", "label": "supplier PPM defects",
        "status": "breach", "severity": "medium", "unit": "ppm",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier PPM defects must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_credit_note_age_days_09(record):
    """Evaluate supplier credit-note age for control WP-0214-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-09", "metric": "supplier_credit_note_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-09", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-09", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-09", "metric": "supplier_credit_note_age_days", "label": "supplier credit-note age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit-note age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_release_notice_days_10(record):
    """Evaluate supplier release notice for control WP-0214-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-10", "metric": "supplier_release_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-10", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-10", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-10", "metric": "supplier_release_notice_days", "label": "supplier release notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier release notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_dimension_spec_match_pct_11(record):
    """Evaluate supplier dimension specification match for control WP-0214-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dimension_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-11", "metric": "supplier_dimension_spec_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-11", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-11", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-11", "metric": "supplier_dimension_spec_match_pct", "label": "supplier dimension specification match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "supplier dimension specification match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_seal_control_pct_12(record):
    """Evaluate supplier seal control for control WP-0214-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seal_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-12", "metric": "supplier_seal_control_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-12", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-12", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-12", "metric": "supplier_seal_control_pct", "label": "supplier seal control",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier seal control must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_material_change_notice_days_13(record):
    """Evaluate supplier material-change notice for control WP-0214-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-13", "metric": "supplier_material_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-13", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-13", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-13", "metric": "supplier_material_change_notice_days", "label": "supplier material-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier material-change notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_reach_compliance_pct_14(record):
    """Evaluate supplier REACH compliance for control WP-0214-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reach_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-14", "metric": "supplier_reach_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-14", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-14", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-14", "metric": "supplier_reach_compliance_pct", "label": "supplier REACH compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier REACH compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_country_of_risk_score_15(record):
    """Evaluate supplier country-of-risk score for control WP-0214-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_of_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-15", "metric": "supplier_country_of_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-15", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-15", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-15", "metric": "supplier_country_of_risk_score", "label": "supplier country-of-risk score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier country-of-risk score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_fuel_storage_hours_16(record):
    """Evaluate supplier fuel storage for control WP-0214-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fuel_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-16", "metric": "supplier_fuel_storage_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-16", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-16", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-16", "metric": "supplier_fuel_storage_hours", "label": "supplier fuel storage",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier fuel storage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_data_access_review_age_days_17(record):
    """Evaluate supplier data-access review age for control WP-0214-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-17", "metric": "supplier_data_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-17", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-17", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-17", "metric": "supplier_data_access_review_age_days", "label": "supplier data-access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data-access review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_rollback_readiness_pct_18(record):
    """Evaluate supplier rollback readiness for control WP-0214-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rollback_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-18", "metric": "supplier_rollback_readiness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-18", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-18", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-18", "metric": "supplier_rollback_readiness_pct", "label": "supplier rollback readiness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier rollback readiness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_identity_federation_pct_19(record):
    """Evaluate supplier identity federation for control WP-0214-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_identity_federation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-19", "metric": "supplier_identity_federation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-19", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-19", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-19", "metric": "supplier_identity_federation_pct", "label": "supplier identity federation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier identity federation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_retention_exception_count_20(record):
    """Evaluate supplier retention exceptions for control WP-0214-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-20", "metric": "supplier_retention_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-20", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-20", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-20", "metric": "supplier_retention_exception_count", "label": "supplier retention exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier retention exceptions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_policy_exception_age_days_21(record):
    """Evaluate supplier policy exception age for control WP-0214-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-21", "metric": "supplier_policy_exception_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-21", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-21", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-21", "metric": "supplier_policy_exception_age_days", "label": "supplier policy exception age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier policy exception age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_late_payment_fee_cost_22(record):
    """Evaluate late-payment fee cost for control WP-0214-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_late_payment_fee_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-22", "metric": "supplier_late_payment_fee_cost",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-22", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-22", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-22", "metric": "supplier_late_payment_fee_cost", "label": "late-payment fee cost",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "late-payment fee cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_raw_material_cover_days_23(record):
    """Evaluate supplier raw-material cover for control WP-0214-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-23", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-23", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-23", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-23", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier raw-material cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_cutover_readiness_pct_24(record):
    """Evaluate supplier cutover readiness for control WP-0214-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0214-24", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0214-24", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0214-24", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0214-24", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cutover readiness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_scale_zero_drift_01, assess_variance_approval_age_hours_02, assess_pick_substitution_pct_03, assess_customs_exam_age_hours_04, assess_fleet_utilization_pct_05, assess_travel_time_pct_06, assess_supplier_audit_score_07, assess_supplier_ppm_defects_08, assess_supplier_credit_note_age_days_09, assess_supplier_release_notice_days_10, assess_supplier_dimension_spec_match_pct_11, assess_supplier_seal_control_pct_12, assess_supplier_material_change_notice_days_13, assess_supplier_reach_compliance_pct_14, assess_supplier_country_of_risk_score_15, assess_supplier_fuel_storage_hours_16, assess_supplier_data_access_review_age_days_17, assess_supplier_rollback_readiness_pct_18, assess_supplier_identity_federation_pct_19, assess_supplier_retention_exception_count_20, assess_supplier_policy_exception_age_days_21, assess_supplier_late_payment_fee_cost_22, assess_supplier_raw_material_cover_days_23, assess_supplier_cutover_readiness_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

