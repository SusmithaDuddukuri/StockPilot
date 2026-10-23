"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_delivery_evidence_pct_01(record):
    """Evaluate supplier delivery evidence for control WP-0037-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-01", "metric": "supplier_delivery_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-01", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-01", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-01", "metric": "supplier_delivery_evidence_pct", "label": "supplier delivery evidence",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier delivery evidence exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_support_resolution_hours_02(record):
    """Evaluate supplier support resolution for control WP-0037-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-02", "metric": "supplier_support_resolution_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-02", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-02", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-02", "metric": "supplier_support_resolution_hours", "label": "supplier support resolution",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier support resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_coa_accuracy_pct_03(record):
    """Evaluate supplier CoA accuracy for control WP-0037-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_coa_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-03", "metric": "supplier_coa_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-03", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-03", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-03", "metric": "supplier_coa_accuracy_pct", "label": "supplier CoA accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier CoA accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_visitor_control_pct_04(record):
    """Evaluate supplier visitor control for control WP-0037-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_visitor_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-04", "metric": "supplier_visitor_control_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-04", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-04", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-04", "metric": "supplier_visitor_control_pct", "label": "supplier visitor control",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier visitor control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_key_person_dependency_pct_05(record):
    """Evaluate supplier key-person dependency for control WP-0037-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_person_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-05", "metric": "supplier_key_person_dependency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-05", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-05", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-05", "metric": "supplier_key_person_dependency_pct", "label": "supplier key-person dependency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier key-person dependency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_material_restriction_gap_count_06(record):
    """Evaluate supplier material restriction gaps for control WP-0037-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_restriction_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-06", "metric": "supplier_material_restriction_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-06", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-06", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-06", "metric": "supplier_material_restriction_gap_count", "label": "supplier material restriction gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier material restriction gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_ownership_review_age_days_07(record):
    """Evaluate supplier ownership review age for control WP-0037-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ownership_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-07", "metric": "supplier_ownership_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-07", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-07", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-07", "metric": "supplier_ownership_review_age_days", "label": "supplier ownership review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ownership review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_tooling_spare_pct_08(record):
    """Evaluate supplier spare tooling coverage for control WP-0037-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-08", "metric": "supplier_tooling_spare_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-08", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-08", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-08", "metric": "supplier_tooling_spare_pct", "label": "supplier spare tooling coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier spare tooling coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_ai_governance_score_09(record):
    """Evaluate supplier AI governance for control WP-0037-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_governance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-09", "metric": "supplier_ai_governance_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-09", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-09", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-09", "metric": "supplier_ai_governance_score", "label": "supplier AI governance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier AI governance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_ab_test_age_days_10(record):
    """Evaluate supplier A/B test age for control WP-0037-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ab_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-10", "metric": "supplier_ab_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-10", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-10", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-10", "metric": "supplier_ab_test_age_days", "label": "supplier A/B test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier A/B test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_encryption_key_age_days_11(record):
    """Evaluate supplier encryption-key age for control WP-0037-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_key_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-11", "metric": "supplier_encryption_key_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-11", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-11", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-11", "metric": "supplier_encryption_key_age_days", "label": "supplier encryption-key age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier encryption-key age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_consent_withdrawal_age_hours_12(record):
    """Evaluate supplier consent withdrawal age for control WP-0037-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_consent_withdrawal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-12", "metric": "supplier_consent_withdrawal_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-12", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-12", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-12", "metric": "supplier_consent_withdrawal_age_hours", "label": "supplier consent withdrawal age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier consent withdrawal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_action_overdue_count_13(record):
    """Evaluate supplier overdue actions for control WP-0037-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_overdue_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-13", "metric": "supplier_action_overdue_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-13", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-13", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-13", "metric": "supplier_action_overdue_count", "label": "supplier overdue actions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier overdue actions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_fx_variance_pct_14(record):
    """Evaluate supplier FX variance for control WP-0037-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fx_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-14", "metric": "supplier_fx_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-14", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-14", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-14", "metric": "supplier_fx_variance_pct", "label": "supplier FX variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier FX variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_work_in_process_units_15(record):
    """Evaluate supplier WIP units for control WP-0037-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_in_process_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-15", "metric": "supplier_work_in_process_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-15", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-15", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-15", "metric": "supplier_work_in_process_units", "label": "supplier WIP units",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier WIP units must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_exit_criteria_gap_count_16(record):
    """Evaluate supplier exit-criteria gaps for control WP-0037-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_criteria_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-16", "metric": "supplier_exit_criteria_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-16", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-16", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-16", "metric": "supplier_exit_criteria_gap_count", "label": "supplier exit-criteria gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit-criteria gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_post_exit_billing_count_17(record):
    """Evaluate post-exit billing events for control WP-0037-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_billing_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-17", "metric": "supplier_post_exit_billing_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-17", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-17", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-17", "metric": "supplier_post_exit_billing_count", "label": "post-exit billing events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "post-exit billing events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_count_variance_18(record):
    """Evaluate cycle-count variance for control WP-0037-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("count_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-18", "metric": "count_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-18", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-18", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-18", "metric": "count_variance", "label": "cycle-count variance",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "cycle-count variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_battery_health_pct_19(record):
    """Evaluate battery health for control WP-0037-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_health_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-19", "metric": "battery_health_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-19", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-19", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-19", "metric": "battery_health_pct", "label": "battery health",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery health must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_security_incident_count_20(record):
    """Evaluate security incidents for control WP-0037-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-20", "metric": "security_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-20", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-20", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-20", "metric": "security_incident_count", "label": "security incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "security incidents must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_temperature_sensor_gap_minutes_21(record):
    """Evaluate sensor data gap for control WP-0037-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-21", "metric": "temperature_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-21", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-21", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-21", "metric": "temperature_sensor_gap_minutes", "label": "sensor data gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "sensor data gap exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_staging_age_minutes_22(record):
    """Evaluate staging age for control WP-0037-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("staging_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-22", "metric": "staging_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-22", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-22", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-22", "metric": "staging_age_minutes", "label": "staging age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "staging age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_event_lag_seconds_23(record):
    """Evaluate event processing lag for control WP-0037-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("event_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-23", "metric": "event_lag_seconds",
            "status": "insufficient_data",
            "severity": "critical", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-23", "metric": "event_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-23", "metric": "event_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-23", "metric": "event_lag_seconds", "label": "event processing lag",
        "status": "breach", "severity": "critical", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "event processing lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_pallet_pick_ratio_pct_24(record):
    """Evaluate pallet pick ratio for control WP-0037-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0037-24", "metric": "pallet_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0037-24", "metric": "pallet_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0037-24", "metric": "pallet_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0037-24", "metric": "pallet_pick_ratio_pct", "label": "pallet pick ratio",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pallet pick ratio must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_supplier_delivery_evidence_pct_01, assess_supplier_support_resolution_hours_02, assess_supplier_coa_accuracy_pct_03, assess_supplier_visitor_control_pct_04, assess_supplier_key_person_dependency_pct_05, assess_supplier_material_restriction_gap_count_06, assess_supplier_ownership_review_age_days_07, assess_supplier_tooling_spare_pct_08, assess_supplier_ai_governance_score_09, assess_supplier_ab_test_age_days_10, assess_supplier_encryption_key_age_days_11, assess_supplier_consent_withdrawal_age_hours_12, assess_supplier_action_overdue_count_13, assess_supplier_fx_variance_pct_14, assess_supplier_work_in_process_units_15, assess_supplier_exit_criteria_gap_count_16, assess_supplier_post_exit_billing_count_17, assess_count_variance_18, assess_battery_health_pct_19, assess_security_incident_count_20, assess_temperature_sensor_gap_minutes_21, assess_staging_age_minutes_22, assess_event_lag_seconds_23, assess_pallet_pick_ratio_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

