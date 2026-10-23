"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_plc_alarm_count_01(record):
    """Evaluate PLC alarms for control WP-0336-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("plc_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-01", "metric": "plc_alarm_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-01", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-01", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-01", "metric": "plc_alarm_count", "label": "PLC alarms",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "PLC alarms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_change_approval_pct_02(record):
    """Evaluate change approval completeness for control WP-0336-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-02", "metric": "change_approval_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-02", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-02", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-02", "metric": "change_approval_pct", "label": "change approval completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "change approval completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_data_export_age_hours_03(record):
    """Evaluate data export age for control WP-0336-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_export_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-03", "metric": "data_export_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-03", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-03", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-03", "metric": "data_export_age_hours", "label": "data export age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data export age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_harmonized_code_gap_count_04(record):
    """Evaluate harmonized-code gaps for control WP-0336-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-04", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-04", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-04", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-04", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "harmonized-code gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_asn_receipt_match_pct_05(record):
    """Evaluate ASN receipt match for control WP-0336-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-05", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-05", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-05", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-05", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "ASN receipt match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_customer_delivery_rating_06(record):
    """Evaluate customer delivery rating for control WP-0336-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-06", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-06", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-06", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-06", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer delivery rating must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_demurrage_charge_days_07(record):
    """Evaluate demurrage charge days for control WP-0336-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demurrage_charge_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-07", "metric": "demurrage_charge_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-07", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-07", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-07", "metric": "demurrage_charge_days", "label": "demurrage charge days",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "demurrage charge days must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_fuel_card_exception_count_08(record):
    """Evaluate fuel card exceptions for control WP-0336-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_card_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-08", "metric": "fuel_card_exception_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-08", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-08", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-08", "metric": "fuel_card_exception_count", "label": "fuel card exceptions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "fuel card exceptions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_geopolitical_risk_score_09(record):
    """Evaluate supplier geopolitical risk for control WP-0336-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_geopolitical_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-09", "metric": "supplier_geopolitical_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-09", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-09", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-09", "metric": "supplier_geopolitical_risk_score", "label": "supplier geopolitical risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier geopolitical risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_turnover_pct_10(record):
    """Evaluate supplier turnover rate for control WP-0336-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_turnover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-10", "metric": "supplier_turnover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-10", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-10", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-10", "metric": "supplier_turnover_pct", "label": "supplier turnover rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier turnover rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_disruption_alert_age_hours_11(record):
    """Evaluate supplier disruption alert age for control WP-0336-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-11", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-11", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-11", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-11", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier disruption alert age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_access_review_age_days_12(record):
    """Evaluate supplier access review age for control WP-0336-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-12", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-12", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-12", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-12", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier access review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_capacity_headroom_pct_13(record):
    """Evaluate supplier capacity headroom for control WP-0336-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-13", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-13", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-13", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-13", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier capacity headroom falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_product_carbon_score_14(record):
    """Evaluate supplier product carbon score for control WP-0336-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_carbon_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-14", "metric": "supplier_product_carbon_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-14", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-14", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-14", "metric": "supplier_product_carbon_score", "label": "supplier product carbon score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier product carbon score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_forecast_latency_hours_15(record):
    """Evaluate supplier forecast latency for control WP-0336-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_latency_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-15", "metric": "supplier_forecast_latency_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-15", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-15", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-15", "metric": "supplier_forecast_latency_hours", "label": "supplier forecast latency",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier forecast latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_containment_response_minutes_16(record):
    """Evaluate supplier containment response for control WP-0336-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_containment_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-16", "metric": "supplier_containment_response_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-16", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-16", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-16", "metric": "supplier_containment_response_minutes", "label": "supplier containment response",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier containment response exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_wage_audit_age_days_17(record):
    """Evaluate supplier wage audit age for control WP-0336-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wage_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-17", "metric": "supplier_wage_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-17", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-17", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-17", "metric": "supplier_wage_audit_age_days", "label": "supplier wage audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier wage audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_revenue_drop_pct_18(record):
    """Evaluate supplier revenue drop for control WP-0336-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-18", "metric": "supplier_revenue_drop_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-18", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-18", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-18", "metric": "supplier_revenue_drop_pct", "label": "supplier revenue drop",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier revenue drop must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_customer_feedback_age_days_19(record):
    """Evaluate supplier customer feedback age for control WP-0336-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-19", "metric": "supplier_customer_feedback_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-19", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-19", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-19", "metric": "supplier_customer_feedback_age_days", "label": "supplier customer feedback age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer feedback age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_compute_budget_variance_pct_20(record):
    """Evaluate supplier compute budget variance for control WP-0336-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-20", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-20", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-20", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-20", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier compute budget variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_alert_ack_minutes_21(record):
    """Evaluate supplier alert acknowledgement for control WP-0336-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-21", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-21", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-21", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-21", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier alert acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_artifact_signature_pct_22(record):
    """Evaluate supplier artifact signature coverage for control WP-0336-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_artifact_signature_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-22", "metric": "supplier_artifact_signature_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-22", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-22", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-22", "metric": "supplier_artifact_signature_pct", "label": "supplier artifact signature coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier artifact signature coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_risk_acceptance_age_days_23(record):
    """Evaluate supplier risk acceptance age for control WP-0336-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_acceptance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-23", "metric": "supplier_risk_acceptance_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-23", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-23", "metric": "supplier_risk_acceptance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-23", "metric": "supplier_risk_acceptance_age_days", "label": "supplier risk acceptance age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk acceptance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_related_party_match_count_24(record):
    """Evaluate supplier related-party matches for control WP-0336-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_related_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0336-24", "metric": "supplier_related_party_match_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0336-24", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0336-24", "metric": "supplier_related_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0336-24", "metric": "supplier_related_party_match_count", "label": "supplier related-party matches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier related-party matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_plc_alarm_count_01, assess_change_approval_pct_02, assess_data_export_age_hours_03, assess_harmonized_code_gap_count_04, assess_asn_receipt_match_pct_05, assess_customer_delivery_rating_06, assess_demurrage_charge_days_07, assess_fuel_card_exception_count_08, assess_supplier_geopolitical_risk_score_09, assess_supplier_turnover_pct_10, assess_supplier_disruption_alert_age_hours_11, assess_supplier_access_review_age_days_12, assess_supplier_capacity_headroom_pct_13, assess_supplier_product_carbon_score_14, assess_supplier_forecast_latency_hours_15, assess_supplier_containment_response_minutes_16, assess_supplier_wage_audit_age_days_17, assess_supplier_revenue_drop_pct_18, assess_supplier_customer_feedback_age_days_19, assess_supplier_compute_budget_variance_pct_20, assess_supplier_alert_ack_minutes_21, assess_supplier_artifact_signature_pct_22, assess_supplier_risk_acceptance_age_days_23, assess_supplier_related_party_match_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

