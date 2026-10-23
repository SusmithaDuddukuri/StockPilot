"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_invoice_accuracy_pct_01(record):
    """Evaluate supplier invoice accuracy for control WP-0603-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-01", "metric": "supplier_invoice_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-01", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-01", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-01", "metric": "supplier_invoice_accuracy_pct", "label": "supplier invoice accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_lifecycle_risk_score_02(record):
    """Evaluate supplier lifecycle risk for control WP-0603-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lifecycle_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-02", "metric": "supplier_lifecycle_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-02", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-02", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-02", "metric": "supplier_lifecycle_risk_score", "label": "supplier lifecycle risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier lifecycle risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_delivery_evidence_pct_03(record):
    """Evaluate supplier delivery evidence for control WP-0603-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-03", "metric": "supplier_delivery_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-03", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-03", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-03", "metric": "supplier_delivery_evidence_pct", "label": "supplier delivery evidence",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier delivery evidence exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_support_resolution_hours_04(record):
    """Evaluate supplier support resolution for control WP-0603-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-04", "metric": "supplier_support_resolution_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-04", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-04", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-04", "metric": "supplier_support_resolution_hours", "label": "supplier support resolution",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "supplier support resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_coa_accuracy_pct_05(record):
    """Evaluate supplier CoA accuracy for control WP-0603-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_coa_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-05", "metric": "supplier_coa_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-05", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-05", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-05", "metric": "supplier_coa_accuracy_pct", "label": "supplier CoA accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier CoA accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_visitor_control_pct_06(record):
    """Evaluate supplier visitor control for control WP-0603-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_visitor_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-06", "metric": "supplier_visitor_control_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-06", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-06", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-06", "metric": "supplier_visitor_control_pct", "label": "supplier visitor control",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier visitor control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_key_person_dependency_pct_07(record):
    """Evaluate supplier key-person dependency for control WP-0603-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_person_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-07", "metric": "supplier_key_person_dependency_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-07", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-07", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-07", "metric": "supplier_key_person_dependency_pct", "label": "supplier key-person dependency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier key-person dependency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_material_restriction_gap_count_08(record):
    """Evaluate supplier material restriction gaps for control WP-0603-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_restriction_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-08", "metric": "supplier_material_restriction_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-08", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-08", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-08", "metric": "supplier_material_restriction_gap_count", "label": "supplier material restriction gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "supplier material restriction gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_ownership_review_age_days_09(record):
    """Evaluate supplier ownership review age for control WP-0603-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ownership_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-09", "metric": "supplier_ownership_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-09", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-09", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-09", "metric": "supplier_ownership_review_age_days", "label": "supplier ownership review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ownership review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tooling_spare_pct_10(record):
    """Evaluate supplier spare tooling coverage for control WP-0603-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-10", "metric": "supplier_tooling_spare_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-10", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-10", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-10", "metric": "supplier_tooling_spare_pct", "label": "supplier spare tooling coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier spare tooling coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_ai_governance_score_11(record):
    """Evaluate supplier AI governance for control WP-0603-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_governance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-11", "metric": "supplier_ai_governance_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-11", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-11", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-11", "metric": "supplier_ai_governance_score", "label": "supplier AI governance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "supplier AI governance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_ab_test_age_days_12(record):
    """Evaluate supplier A/B test age for control WP-0603-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ab_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-12", "metric": "supplier_ab_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-12", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-12", "metric": "supplier_ab_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-12", "metric": "supplier_ab_test_age_days", "label": "supplier A/B test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "supplier A/B test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_encryption_key_age_days_13(record):
    """Evaluate supplier encryption-key age for control WP-0603-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_encryption_key_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-13", "metric": "supplier_encryption_key_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-13", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-13", "metric": "supplier_encryption_key_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-13", "metric": "supplier_encryption_key_age_days", "label": "supplier encryption-key age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier encryption-key age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_consent_withdrawal_age_hours_14(record):
    """Evaluate supplier consent withdrawal age for control WP-0603-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_consent_withdrawal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-14", "metric": "supplier_consent_withdrawal_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-14", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-14", "metric": "supplier_consent_withdrawal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-14", "metric": "supplier_consent_withdrawal_age_hours", "label": "supplier consent withdrawal age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier consent withdrawal age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_action_overdue_count_15(record):
    """Evaluate supplier overdue actions for control WP-0603-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_overdue_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-15", "metric": "supplier_action_overdue_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-15", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-15", "metric": "supplier_action_overdue_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-15", "metric": "supplier_action_overdue_count", "label": "supplier overdue actions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "supplier overdue actions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_fx_variance_pct_16(record):
    """Evaluate supplier FX variance for control WP-0603-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fx_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-16", "metric": "supplier_fx_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-16", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-16", "metric": "supplier_fx_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-16", "metric": "supplier_fx_variance_pct", "label": "supplier FX variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "supplier FX variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_work_in_process_units_17(record):
    """Evaluate supplier WIP units for control WP-0603-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_in_process_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-17", "metric": "supplier_work_in_process_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-17", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-17", "metric": "supplier_work_in_process_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-17", "metric": "supplier_work_in_process_units", "label": "supplier WIP units",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier WIP units must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_exit_criteria_gap_count_18(record):
    """Evaluate supplier exit-criteria gaps for control WP-0603-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_criteria_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-18", "metric": "supplier_exit_criteria_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-18", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-18", "metric": "supplier_exit_criteria_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-18", "metric": "supplier_exit_criteria_gap_count", "label": "supplier exit-criteria gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier exit-criteria gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_post_exit_billing_count_19(record):
    """Evaluate post-exit billing events for control WP-0603-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_billing_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-19", "metric": "supplier_post_exit_billing_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-19", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-19", "metric": "supplier_post_exit_billing_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-19", "metric": "supplier_post_exit_billing_count", "label": "post-exit billing events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "post-exit billing events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_count_variance_20(record):
    """Evaluate cycle-count variance for control WP-0603-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("count_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-20", "metric": "count_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-20", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-20", "metric": "count_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-20", "metric": "count_variance", "label": "cycle-count variance",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "cycle-count variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_battery_health_pct_21(record):
    """Evaluate battery health for control WP-0603-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_health_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-21", "metric": "battery_health_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-21", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-21", "metric": "battery_health_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-21", "metric": "battery_health_pct", "label": "battery health",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery health must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_security_incident_count_22(record):
    """Evaluate security incidents for control WP-0603-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-22", "metric": "security_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-22", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-22", "metric": "security_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-22", "metric": "security_incident_count", "label": "security incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "security incidents must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_temperature_sensor_gap_minutes_23(record):
    """Evaluate sensor data gap for control WP-0603-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-23", "metric": "temperature_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-23", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-23", "metric": "temperature_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-23", "metric": "temperature_sensor_gap_minutes", "label": "sensor data gap",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "sensor data gap exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_staging_age_minutes_24(record):
    """Evaluate staging age for control WP-0603-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("staging_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0603-24", "metric": "staging_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0603-24", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0603-24", "metric": "staging_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0603-24", "metric": "staging_age_minutes", "label": "staging age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "staging age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_invoice_accuracy_pct_01, assess_supplier_lifecycle_risk_score_02, assess_supplier_delivery_evidence_pct_03, assess_supplier_support_resolution_hours_04, assess_supplier_coa_accuracy_pct_05, assess_supplier_visitor_control_pct_06, assess_supplier_key_person_dependency_pct_07, assess_supplier_material_restriction_gap_count_08, assess_supplier_ownership_review_age_days_09, assess_supplier_tooling_spare_pct_10, assess_supplier_ai_governance_score_11, assess_supplier_ab_test_age_days_12, assess_supplier_encryption_key_age_days_13, assess_supplier_consent_withdrawal_age_hours_14, assess_supplier_action_overdue_count_15, assess_supplier_fx_variance_pct_16, assess_supplier_work_in_process_units_17, assess_supplier_exit_criteria_gap_count_18, assess_supplier_post_exit_billing_count_19, assess_count_variance_20, assess_battery_health_pct_21, assess_security_incident_count_22, assess_temperature_sensor_gap_minutes_23, assess_staging_age_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

