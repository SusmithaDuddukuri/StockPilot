"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_authentication_scan_pct_01(record):
    """Evaluate authentication scan rate for control WP-0523-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("authentication_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-01", "metric": "authentication_scan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-01", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-01", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-01", "metric": "authentication_scan_pct", "label": "authentication scan rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "authentication scan rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_contractor_induction_pct_02(record):
    """Evaluate contractor induction completion for control WP-0523-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contractor_induction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-02", "metric": "contractor_induction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-02", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-02", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-02", "metric": "contractor_induction_pct", "label": "contractor induction completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "contractor induction completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_plc_alarm_count_03(record):
    """Evaluate PLC alarms for control WP-0523-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("plc_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-03", "metric": "plc_alarm_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-03", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-03", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-03", "metric": "plc_alarm_count", "label": "PLC alarms",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "PLC alarms exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_change_approval_pct_04(record):
    """Evaluate change approval completeness for control WP-0523-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-04", "metric": "change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-04", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-04", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-04", "metric": "change_approval_pct", "label": "change approval completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "change approval completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_data_export_age_hours_05(record):
    """Evaluate data export age for control WP-0523-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_export_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-05", "metric": "data_export_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-05", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-05", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-05", "metric": "data_export_age_hours", "label": "data export age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data export age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_harmonized_code_gap_count_06(record):
    """Evaluate harmonized-code gaps for control WP-0523-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-06", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-06", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-06", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-06", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "harmonized-code gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_asn_receipt_match_pct_07(record):
    """Evaluate ASN receipt match for control WP-0523-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-07", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-07", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-07", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-07", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "ASN receipt match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_customer_delivery_rating_08(record):
    """Evaluate customer delivery rating for control WP-0523-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-08", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-08", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-08", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-08", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "customer delivery rating falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_demurrage_charge_days_09(record):
    """Evaluate demurrage charge days for control WP-0523-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demurrage_charge_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-09", "metric": "demurrage_charge_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-09", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-09", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-09", "metric": "demurrage_charge_days", "label": "demurrage charge days",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "demurrage charge days must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_fuel_card_exception_count_10(record):
    """Evaluate fuel card exceptions for control WP-0523-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_card_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-10", "metric": "fuel_card_exception_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-10", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-10", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-10", "metric": "fuel_card_exception_count", "label": "fuel card exceptions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fuel card exceptions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_geopolitical_risk_score_11(record):
    """Evaluate supplier geopolitical risk for control WP-0523-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_geopolitical_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-11", "metric": "supplier_geopolitical_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-11", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-11", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-11", "metric": "supplier_geopolitical_risk_score", "label": "supplier geopolitical risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "supplier geopolitical risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_turnover_pct_12(record):
    """Evaluate supplier turnover rate for control WP-0523-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_turnover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-12", "metric": "supplier_turnover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-12", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-12", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-12", "metric": "supplier_turnover_pct", "label": "supplier turnover rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier turnover rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_disruption_alert_age_hours_13(record):
    """Evaluate supplier disruption alert age for control WP-0523-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-13", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-13", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-13", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-13", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disruption alert age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_access_review_age_days_14(record):
    """Evaluate supplier access review age for control WP-0523-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-14", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-14", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-14", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-14", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_capacity_headroom_pct_15(record):
    """Evaluate supplier capacity headroom for control WP-0523-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-15", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-15", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-15", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-15", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier capacity headroom exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_product_carbon_score_16(record):
    """Evaluate supplier product carbon score for control WP-0523-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_carbon_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-16", "metric": "supplier_product_carbon_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-16", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-16", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-16", "metric": "supplier_product_carbon_score", "label": "supplier product carbon score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier product carbon score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_forecast_latency_hours_17(record):
    """Evaluate supplier forecast latency for control WP-0523-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_latency_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-17", "metric": "supplier_forecast_latency_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-17", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-17", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-17", "metric": "supplier_forecast_latency_hours", "label": "supplier forecast latency",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier forecast latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_containment_response_minutes_18(record):
    """Evaluate supplier containment response for control WP-0523-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_containment_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-18", "metric": "supplier_containment_response_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-18", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-18", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-18", "metric": "supplier_containment_response_minutes", "label": "supplier containment response",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier containment response must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_wage_audit_age_days_19(record):
    """Evaluate supplier wage audit age for control WP-0523-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wage_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-19", "metric": "supplier_wage_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-19", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-19", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-19", "metric": "supplier_wage_audit_age_days", "label": "supplier wage audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "supplier wage audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_revenue_drop_pct_20(record):
    """Evaluate supplier revenue drop for control WP-0523-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-20", "metric": "supplier_revenue_drop_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-20", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-20", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-20", "metric": "supplier_revenue_drop_pct", "label": "supplier revenue drop",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier revenue drop falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_customer_feedback_age_days_21(record):
    """Evaluate supplier customer feedback age for control WP-0523-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-21", "metric": "supplier_customer_feedback_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-21", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-21", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-21", "metric": "supplier_customer_feedback_age_days", "label": "supplier customer feedback age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer feedback age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_compute_budget_variance_pct_22(record):
    """Evaluate supplier compute budget variance for control WP-0523-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-22", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-22", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-22", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-22", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier compute budget variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_alert_ack_minutes_23(record):
    """Evaluate supplier alert acknowledgement for control WP-0523-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-23", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-23", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-23", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-23", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier alert acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_artifact_signature_pct_24(record):
    """Evaluate supplier artifact signature coverage for control WP-0523-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_artifact_signature_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0523-24", "metric": "supplier_artifact_signature_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0523-24", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0523-24", "metric": "supplier_artifact_signature_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0523-24", "metric": "supplier_artifact_signature_pct", "label": "supplier artifact signature coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier artifact signature coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_authentication_scan_pct_01, assess_contractor_induction_pct_02, assess_plc_alarm_count_03, assess_change_approval_pct_04, assess_data_export_age_hours_05, assess_harmonized_code_gap_count_06, assess_asn_receipt_match_pct_07, assess_customer_delivery_rating_08, assess_demurrage_charge_days_09, assess_fuel_card_exception_count_10, assess_supplier_geopolitical_risk_score_11, assess_supplier_turnover_pct_12, assess_supplier_disruption_alert_age_hours_13, assess_supplier_access_review_age_days_14, assess_supplier_capacity_headroom_pct_15, assess_supplier_product_carbon_score_16, assess_supplier_forecast_latency_hours_17, assess_supplier_containment_response_minutes_18, assess_supplier_wage_audit_age_days_19, assess_supplier_revenue_drop_pct_20, assess_supplier_customer_feedback_age_days_21, assess_supplier_compute_budget_variance_pct_22, assess_supplier_alert_ack_minutes_23, assess_supplier_artifact_signature_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

