"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_harmonized_code_gap_count_01(record):
    """Evaluate harmonized-code gaps for control WP-0025-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-01", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-01", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-01", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-01", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "harmonized-code gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_asn_receipt_match_pct_02(record):
    """Evaluate ASN receipt match for control WP-0025-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-02", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-02", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-02", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-02", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "ASN receipt match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_customer_delivery_rating_03(record):
    """Evaluate customer delivery rating for control WP-0025-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-03", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-03", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-03", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-03", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer delivery rating must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_demurrage_charge_days_04(record):
    """Evaluate demurrage charge days for control WP-0025-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demurrage_charge_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-04", "metric": "demurrage_charge_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-04", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-04", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-04", "metric": "demurrage_charge_days", "label": "demurrage charge days",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "demurrage charge days must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_fuel_card_exception_count_05(record):
    """Evaluate fuel card exceptions for control WP-0025-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_card_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-05", "metric": "fuel_card_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-05", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-05", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-05", "metric": "fuel_card_exception_count", "label": "fuel card exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "fuel card exceptions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_geopolitical_risk_score_06(record):
    """Evaluate supplier geopolitical risk for control WP-0025-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_geopolitical_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-06", "metric": "supplier_geopolitical_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-06", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-06", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-06", "metric": "supplier_geopolitical_risk_score", "label": "supplier geopolitical risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier geopolitical risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_turnover_pct_07(record):
    """Evaluate supplier turnover rate for control WP-0025-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_turnover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-07", "metric": "supplier_turnover_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-07", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-07", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-07", "metric": "supplier_turnover_pct", "label": "supplier turnover rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier turnover rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_disruption_alert_age_hours_08(record):
    """Evaluate supplier disruption alert age for control WP-0025-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-08", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-08", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-08", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-08", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier disruption alert age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_access_review_age_days_09(record):
    """Evaluate supplier access review age for control WP-0025-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-09", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-09", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-09", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-09", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier access review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_capacity_headroom_pct_10(record):
    """Evaluate supplier capacity headroom for control WP-0025-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-10", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-10", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-10", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-10", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier capacity headroom falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_product_carbon_score_11(record):
    """Evaluate supplier product carbon score for control WP-0025-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_carbon_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-11", "metric": "supplier_product_carbon_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-11", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-11", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-11", "metric": "supplier_product_carbon_score", "label": "supplier product carbon score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier product carbon score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_forecast_latency_hours_12(record):
    """Evaluate supplier forecast latency for control WP-0025-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_latency_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-12", "metric": "supplier_forecast_latency_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-12", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-12", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-12", "metric": "supplier_forecast_latency_hours", "label": "supplier forecast latency",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier forecast latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_containment_response_minutes_13(record):
    """Evaluate supplier containment response for control WP-0025-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_containment_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-13", "metric": "supplier_containment_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-13", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-13", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-13", "metric": "supplier_containment_response_minutes", "label": "supplier containment response",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier containment response exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_wage_audit_age_days_14(record):
    """Evaluate supplier wage audit age for control WP-0025-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wage_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-14", "metric": "supplier_wage_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-14", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-14", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-14", "metric": "supplier_wage_audit_age_days", "label": "supplier wage audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier wage audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_revenue_drop_pct_15(record):
    """Evaluate supplier revenue drop for control WP-0025-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-15", "metric": "supplier_revenue_drop_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-15", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-15", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-15", "metric": "supplier_revenue_drop_pct", "label": "supplier revenue drop",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier revenue drop must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_customer_feedback_age_days_16(record):
    """Evaluate supplier customer feedback age for control WP-0025-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-16", "metric": "supplier_customer_feedback_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-16", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-16", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-16", "metric": "supplier_customer_feedback_age_days", "label": "supplier customer feedback age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer feedback age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_compute_budget_variance_pct_17(record):
    """Evaluate supplier compute budget variance for control WP-0025-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-17", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-17", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-17", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-17", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier compute budget variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_alert_ack_minutes_18(record):
    """Evaluate supplier alert acknowledgement for control WP-0025-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-18", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-18", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-18", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-18", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier alert acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_artifact_signature_pct_19(record):
    """Evaluate supplier artifact signature coverage for control WP-0025-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_artifact_signature_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-19", "metric": "supplier_artifact_signature_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-19", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-19", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-19", "metric": "supplier_artifact_signature_pct", "label": "supplier artifact signature coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier artifact signature coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_risk_acceptance_age_days_20(record):
    """Evaluate supplier risk acceptance age for control WP-0025-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_acceptance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-20", "metric": "supplier_risk_acceptance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-20", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-20", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-20", "metric": "supplier_risk_acceptance_age_days", "label": "supplier risk acceptance age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk acceptance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_related_party_match_count_21(record):
    """Evaluate supplier related-party matches for control WP-0025-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_related_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-21", "metric": "supplier_related_party_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-21", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-21", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-21", "metric": "supplier_related_party_match_count", "label": "supplier related-party matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier related-party matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_material_availability_pct_22(record):
    """Evaluate supplier material availability for control WP-0025-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-22", "metric": "supplier_material_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-22", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-22", "metric": "supplier_material_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-22", "metric": "supplier_material_availability_pct", "label": "supplier material availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier material availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_portal_login_age_days_23(record):
    """Evaluate supplier portal login age for control WP-0025-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_portal_login_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-23", "metric": "supplier_portal_login_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-23", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-23", "metric": "supplier_portal_login_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-23", "metric": "supplier_portal_login_age_days", "label": "supplier portal login age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier portal login age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_runbook_handover_pct_24(record):
    """Evaluate supplier runbook handover for control WP-0025-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0025-24", "metric": "supplier_runbook_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0025-24", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0025-24", "metric": "supplier_runbook_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0025-24", "metric": "supplier_runbook_handover_pct", "label": "supplier runbook handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier runbook handover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_harmonized_code_gap_count_01, assess_asn_receipt_match_pct_02, assess_customer_delivery_rating_03, assess_demurrage_charge_days_04, assess_fuel_card_exception_count_05, assess_supplier_geopolitical_risk_score_06, assess_supplier_turnover_pct_07, assess_supplier_disruption_alert_age_hours_08, assess_supplier_access_review_age_days_09, assess_supplier_capacity_headroom_pct_10, assess_supplier_product_carbon_score_11, assess_supplier_forecast_latency_hours_12, assess_supplier_containment_response_minutes_13, assess_supplier_wage_audit_age_days_14, assess_supplier_revenue_drop_pct_15, assess_supplier_customer_feedback_age_days_16, assess_supplier_compute_budget_variance_pct_17, assess_supplier_alert_ack_minutes_18, assess_supplier_artifact_signature_pct_19, assess_supplier_risk_acceptance_age_days_20, assess_supplier_related_party_match_count_21, assess_supplier_material_availability_pct_22, assess_supplier_portal_login_age_days_23, assess_supplier_runbook_handover_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

