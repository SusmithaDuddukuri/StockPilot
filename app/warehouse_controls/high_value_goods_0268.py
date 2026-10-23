"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_compressor_runtime_hours_01(record):
    """Evaluate compressor runtime for control WP-0268-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("compressor_runtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-01", "metric": "compressor_runtime_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-01", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-01", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-01", "metric": "compressor_runtime_hours", "label": "compressor runtime",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "compressor runtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_authentication_scan_pct_02(record):
    """Evaluate authentication scan rate for control WP-0268-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("authentication_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-02", "metric": "authentication_scan_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-02", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-02", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-02", "metric": "authentication_scan_pct", "label": "authentication scan rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "authentication scan rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_contractor_induction_pct_03(record):
    """Evaluate contractor induction completion for control WP-0268-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contractor_induction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-03", "metric": "contractor_induction_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-03", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-03", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-03", "metric": "contractor_induction_pct", "label": "contractor induction completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "contractor induction completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_plc_alarm_count_04(record):
    """Evaluate PLC alarms for control WP-0268-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("plc_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-04", "metric": "plc_alarm_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-04", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-04", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-04", "metric": "plc_alarm_count", "label": "PLC alarms",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "PLC alarms exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_change_approval_pct_05(record):
    """Evaluate change approval completeness for control WP-0268-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-05", "metric": "change_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-05", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-05", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-05", "metric": "change_approval_pct", "label": "change approval completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "change approval completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_data_export_age_hours_06(record):
    """Evaluate data export age for control WP-0268-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_export_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-06", "metric": "data_export_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-06", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-06", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-06", "metric": "data_export_age_hours", "label": "data export age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data export age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_harmonized_code_gap_count_07(record):
    """Evaluate harmonized-code gaps for control WP-0268-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-07", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-07", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-07", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-07", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "harmonized-code gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_asn_receipt_match_pct_08(record):
    """Evaluate ASN receipt match for control WP-0268-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-08", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-08", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-08", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-08", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "ASN receipt match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_customer_delivery_rating_09(record):
    """Evaluate customer delivery rating for control WP-0268-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-09", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-09", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-09", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-09", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "customer delivery rating falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_demurrage_charge_days_10(record):
    """Evaluate demurrage charge days for control WP-0268-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demurrage_charge_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-10", "metric": "demurrage_charge_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-10", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-10", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-10", "metric": "demurrage_charge_days", "label": "demurrage charge days",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "demurrage charge days must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_fuel_card_exception_count_11(record):
    """Evaluate fuel card exceptions for control WP-0268-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_card_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-11", "metric": "fuel_card_exception_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-11", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-11", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-11", "metric": "fuel_card_exception_count", "label": "fuel card exceptions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fuel card exceptions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_geopolitical_risk_score_12(record):
    """Evaluate supplier geopolitical risk for control WP-0268-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_geopolitical_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-12", "metric": "supplier_geopolitical_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-12", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-12", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-12", "metric": "supplier_geopolitical_risk_score", "label": "supplier geopolitical risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier geopolitical risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_turnover_pct_13(record):
    """Evaluate supplier turnover rate for control WP-0268-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_turnover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-13", "metric": "supplier_turnover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-13", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-13", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-13", "metric": "supplier_turnover_pct", "label": "supplier turnover rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier turnover rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_disruption_alert_age_hours_14(record):
    """Evaluate supplier disruption alert age for control WP-0268-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-14", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-14", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-14", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-14", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier disruption alert age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_access_review_age_days_15(record):
    """Evaluate supplier access review age for control WP-0268-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-15", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-15", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-15", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-15", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_capacity_headroom_pct_16(record):
    """Evaluate supplier capacity headroom for control WP-0268-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-16", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-16", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-16", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-16", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "supplier capacity headroom exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_product_carbon_score_17(record):
    """Evaluate supplier product carbon score for control WP-0268-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_carbon_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-17", "metric": "supplier_product_carbon_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-17", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-17", "metric": "supplier_product_carbon_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-17", "metric": "supplier_product_carbon_score", "label": "supplier product carbon score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier product carbon score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_forecast_latency_hours_18(record):
    """Evaluate supplier forecast latency for control WP-0268-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_latency_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-18", "metric": "supplier_forecast_latency_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-18", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-18", "metric": "supplier_forecast_latency_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-18", "metric": "supplier_forecast_latency_hours", "label": "supplier forecast latency",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier forecast latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_containment_response_minutes_19(record):
    """Evaluate supplier containment response for control WP-0268-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_containment_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-19", "metric": "supplier_containment_response_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-19", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-19", "metric": "supplier_containment_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-19", "metric": "supplier_containment_response_minutes", "label": "supplier containment response",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier containment response must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_wage_audit_age_days_20(record):
    """Evaluate supplier wage audit age for control WP-0268-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wage_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-20", "metric": "supplier_wage_audit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-20", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-20", "metric": "supplier_wage_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-20", "metric": "supplier_wage_audit_age_days", "label": "supplier wage audit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier wage audit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_revenue_drop_pct_21(record):
    """Evaluate supplier revenue drop for control WP-0268-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_drop_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-21", "metric": "supplier_revenue_drop_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-21", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-21", "metric": "supplier_revenue_drop_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-21", "metric": "supplier_revenue_drop_pct", "label": "supplier revenue drop",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier revenue drop falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_customer_feedback_age_days_22(record):
    """Evaluate supplier customer feedback age for control WP-0268-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_feedback_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-22", "metric": "supplier_customer_feedback_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-22", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-22", "metric": "supplier_customer_feedback_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-22", "metric": "supplier_customer_feedback_age_days", "label": "supplier customer feedback age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer feedback age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_compute_budget_variance_pct_23(record):
    """Evaluate supplier compute budget variance for control WP-0268-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compute_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-23", "metric": "supplier_compute_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-23", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-23", "metric": "supplier_compute_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-23", "metric": "supplier_compute_budget_variance_pct", "label": "supplier compute budget variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier compute budget variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_alert_ack_minutes_24(record):
    """Evaluate supplier alert acknowledgement for control WP-0268-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alert_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0268-24", "metric": "supplier_alert_ack_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0268-24", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0268-24", "metric": "supplier_alert_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0268-24", "metric": "supplier_alert_ack_minutes", "label": "supplier alert acknowledgement",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier alert acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_compressor_runtime_hours_01, assess_authentication_scan_pct_02, assess_contractor_induction_pct_03, assess_plc_alarm_count_04, assess_change_approval_pct_05, assess_data_export_age_hours_06, assess_harmonized_code_gap_count_07, assess_asn_receipt_match_pct_08, assess_customer_delivery_rating_09, assess_demurrage_charge_days_10, assess_fuel_card_exception_count_11, assess_supplier_geopolitical_risk_score_12, assess_supplier_turnover_pct_13, assess_supplier_disruption_alert_age_hours_14, assess_supplier_access_review_age_days_15, assess_supplier_capacity_headroom_pct_16, assess_supplier_product_carbon_score_17, assess_supplier_forecast_latency_hours_18, assess_supplier_containment_response_minutes_19, assess_supplier_wage_audit_age_days_20, assess_supplier_revenue_drop_pct_21, assess_supplier_customer_feedback_age_days_22, assess_supplier_compute_budget_variance_pct_23, assess_supplier_alert_ack_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

