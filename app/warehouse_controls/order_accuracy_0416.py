"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_disruption_alert_age_hours_01(record):
    """Evaluate supplier disruption alert age for control WP-0416-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-01", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-01", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-01", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-01", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "supplier disruption alert age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_access_review_age_days_02(record):
    """Evaluate supplier access review age for control WP-0416-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-02", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-02", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-02", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-02", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_capacity_headroom_pct_03(record):
    """Evaluate supplier capacity headroom for control WP-0416-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-03", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-03", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-03", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-03", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity headroom must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_product_carbon_score_04(record):
    """Evaluate supplier product carbon score for control WP-0416-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_carbon_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-04", "metric": "supplier_product_carbon_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-04", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-04", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-04", "metric": "supplier_product_carbon_score", "label": "supplier product carbon score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier product carbon score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_forecast_latency_hours_05(record):
    """Evaluate supplier forecast latency for control WP-0416-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_latency_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-05", "metric": "supplier_forecast_latency_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-05", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-05", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-05", "metric": "supplier_forecast_latency_hours", "label": "supplier forecast latency",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier forecast latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_containment_response_minutes_06(record):
    """Evaluate supplier containment response for control WP-0416-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_containment_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-06", "metric": "supplier_containment_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-06", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-06", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-06", "metric": "supplier_containment_response_minutes", "label": "supplier containment response",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier containment response must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_wage_audit_age_days_07(record):
    """Evaluate supplier wage audit age for control WP-0416-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wage_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-07", "metric": "supplier_wage_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-07", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-07", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-07", "metric": "supplier_wage_audit_age_days", "label": "supplier wage audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier wage audit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_revenue_drop_pct_08(record):
    """Evaluate supplier revenue drop for control WP-0416-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-08", "metric": "supplier_revenue_drop_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-08", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-08", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-08", "metric": "supplier_revenue_drop_pct", "label": "supplier revenue drop",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier revenue drop exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_customer_feedback_age_days_09(record):
    """Evaluate supplier customer feedback age for control WP-0416-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-09", "metric": "supplier_customer_feedback_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-09", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-09", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-09", "metric": "supplier_customer_feedback_age_days", "label": "supplier customer feedback age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "supplier customer feedback age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_compute_budget_variance_pct_10(record):
    """Evaluate supplier compute budget variance for control WP-0416-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-10", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-10", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-10", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-10", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier compute budget variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_alert_ack_minutes_11(record):
    """Evaluate supplier alert acknowledgement for control WP-0416-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-11", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-11", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-11", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-11", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier alert acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_artifact_signature_pct_12(record):
    """Evaluate supplier artifact signature coverage for control WP-0416-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_artifact_signature_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-12", "metric": "supplier_artifact_signature_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-12", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-12", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-12", "metric": "supplier_artifact_signature_pct", "label": "supplier artifact signature coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier artifact signature coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_risk_acceptance_age_days_13(record):
    """Evaluate supplier risk acceptance age for control WP-0416-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_acceptance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-13", "metric": "supplier_risk_acceptance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-13", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-13", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-13", "metric": "supplier_risk_acceptance_age_days", "label": "supplier risk acceptance age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier risk acceptance age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_related_party_match_count_14(record):
    """Evaluate supplier related-party matches for control WP-0416-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_related_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-14", "metric": "supplier_related_party_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-14", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-14", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-14", "metric": "supplier_related_party_match_count", "label": "supplier related-party matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier related-party matches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_material_availability_pct_15(record):
    """Evaluate supplier material availability for control WP-0416-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-15", "metric": "supplier_material_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-15", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-15", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-15", "metric": "supplier_material_availability_pct", "label": "supplier material availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier material availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_portal_login_age_days_16(record):
    """Evaluate supplier portal login age for control WP-0416-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_portal_login_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-16", "metric": "supplier_portal_login_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-16", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-16", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-16", "metric": "supplier_portal_login_age_days", "label": "supplier portal login age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier portal login age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_runbook_handover_pct_17(record):
    """Evaluate supplier runbook handover for control WP-0416-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-17", "metric": "supplier_runbook_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-17", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-17", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-17", "metric": "supplier_runbook_handover_pct", "label": "supplier runbook handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier runbook handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_delivery_days_18(record):
    """Evaluate delivery duration for control WP-0416-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-18", "metric": "delivery_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-18", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-18", "metric": "delivery_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-18", "metric": "delivery_days", "label": "delivery duration",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery duration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_network_latency_ms_19(record):
    """Evaluate network latency for control WP-0416-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("network_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-19", "metric": "network_latency_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-19", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-19", "metric": "network_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-19", "metric": "network_latency_ms", "label": "network latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "network latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_customer_complaint_count_20(record):
    """Evaluate customer complaints for control WP-0416-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_complaint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-20", "metric": "customer_complaint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-20", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-20", "metric": "customer_complaint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-20", "metric": "customer_complaint_count", "label": "customer complaints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "customer complaints exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_response_hours_21(record):
    """Evaluate supplier response time for control WP-0416-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-21", "metric": "supplier_response_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-21", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-21", "metric": "supplier_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-21", "metric": "supplier_response_hours", "label": "supplier response time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_load_balance_score_22(record):
    """Evaluate load balance for control WP-0416-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("load_balance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-22", "metric": "load_balance_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-22", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-22", "metric": "load_balance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-22", "metric": "load_balance_score", "label": "load balance",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "load balance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_critical_vulnerability_count_23(record):
    """Evaluate critical vulnerabilities for control WP-0416-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("critical_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-23", "metric": "critical_vulnerability_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-23", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-23", "metric": "critical_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-23", "metric": "critical_vulnerability_count", "label": "critical vulnerabilities",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "critical vulnerabilities must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_customer_wait_minutes_24(record):
    """Evaluate customer wait time for control WP-0416-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0416-24", "metric": "customer_wait_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0416-24", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0416-24", "metric": "customer_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0416-24", "metric": "customer_wait_minutes", "label": "customer wait time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "customer wait time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_disruption_alert_age_hours_01, assess_supplier_access_review_age_days_02, assess_supplier_capacity_headroom_pct_03, assess_supplier_product_carbon_score_04, assess_supplier_forecast_latency_hours_05, assess_supplier_containment_response_minutes_06, assess_supplier_wage_audit_age_days_07, assess_supplier_revenue_drop_pct_08, assess_supplier_customer_feedback_age_days_09, assess_supplier_compute_budget_variance_pct_10, assess_supplier_alert_ack_minutes_11, assess_supplier_artifact_signature_pct_12, assess_supplier_risk_acceptance_age_days_13, assess_supplier_related_party_match_count_14, assess_supplier_material_availability_pct_15, assess_supplier_portal_login_age_days_16, assess_supplier_runbook_handover_pct_17, assess_delivery_days_18, assess_network_latency_ms_19, assess_customer_complaint_count_20, assess_supplier_response_hours_21, assess_load_balance_score_22, assess_critical_vulnerability_count_23, assess_customer_wait_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

