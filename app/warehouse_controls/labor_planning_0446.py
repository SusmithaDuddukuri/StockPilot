"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_quality_score_01(record):
    """Evaluate quality score for control WP-0446-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-01", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-01", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-01", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-01", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quality score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_carrier_exception_count_02(record):
    """Evaluate carrier exceptions for control WP-0446-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-02", "metric": "carrier_exception_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-02", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-02", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-02", "metric": "carrier_exception_count", "label": "carrier exceptions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "carrier exceptions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_ergonomic_risk_score_03(record):
    """Evaluate ergonomic risk for control WP-0446-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-03", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-03", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-03", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-03", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "ergonomic risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_insurance_days_left_04(record):
    """Evaluate insurance validity for control WP-0446-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-04", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-04", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-04", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-04", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insurance validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_incident_resolution_hours_05(record):
    """Evaluate incident resolution for control WP-0446-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-05", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-05", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-05", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-05", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident resolution must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_forecast_wape_pct_06(record):
    """Evaluate forecast WAPE for control WP-0446-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_wape_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-06", "metric": "forecast_wape_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-06", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-06", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-06", "metric": "forecast_wape_pct", "label": "forecast WAPE",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "forecast WAPE exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_lift_assist_usage_pct_07(record):
    """Evaluate lift-assist usage for control WP-0446-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lift_assist_usage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-07", "metric": "lift_assist_usage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-07", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-07", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-07", "metric": "lift_assist_usage_pct", "label": "lift-assist usage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "lift-assist usage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_recovery_case_age_days_08(record):
    """Evaluate recovery case age for control WP-0446-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_case_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-08", "metric": "recovery_case_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-08", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-08", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-08", "metric": "recovery_case_age_days", "label": "recovery case age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recovery case age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_traceability_query_minutes_09(record):
    """Evaluate traceability query time for control WP-0446-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("traceability_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-09", "metric": "traceability_query_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-09", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-09", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-09", "metric": "traceability_query_minutes", "label": "traceability query time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "traceability query time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_lithium_battery_label_pct_10(record):
    """Evaluate lithium battery label compliance for control WP-0446-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lithium_battery_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-10", "metric": "lithium_battery_label_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-10", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-10", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-10", "metric": "lithium_battery_label_pct", "label": "lithium battery label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "lithium battery label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_near_miss_close_rate_pct_11(record):
    """Evaluate near-miss close rate for control WP-0446-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_close_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-11", "metric": "near_miss_close_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-11", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-11", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-11", "metric": "near_miss_close_rate_pct", "label": "near-miss close rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "near-miss close rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_public_address_test_age_days_12(record):
    """Evaluate public-address test age for control WP-0446-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("public_address_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-12", "metric": "public_address_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-12", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-12", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-12", "metric": "public_address_test_age_days", "label": "public-address test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "public-address test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_license_compliance_pct_13(record):
    """Evaluate license compliance for control WP-0446-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-13", "metric": "license_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-13", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-13", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-13", "metric": "license_compliance_pct", "label": "license compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "license compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_rfid_collision_count_14(record):
    """Evaluate RFID collisions for control WP-0446-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_collision_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-14", "metric": "rfid_collision_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-14", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-14", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-14", "metric": "rfid_collision_count", "label": "RFID collisions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "RFID collisions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_stock_age_p95_days_15(record):
    """Evaluate 95th percentile stock age for control WP-0446-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_p95_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-15", "metric": "stock_age_p95_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-15", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-15", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-15", "metric": "stock_age_p95_days", "label": "95th percentile stock age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "95th percentile stock age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_cartonization_savings_pct_16(record):
    """Evaluate cartonization savings for control WP-0446-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cartonization_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-16", "metric": "cartonization_savings_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-16", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-16", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-16", "metric": "cartonization_savings_pct", "label": "cartonization savings",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cartonization savings must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_restricted_party_match_count_17(record):
    """Evaluate restricted-party matches for control WP-0446-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-17", "metric": "restricted_party_match_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-17", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-17", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-17", "metric": "restricted_party_match_count", "label": "restricted-party matches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restricted-party matches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_driver_license_days_left_18(record):
    """Evaluate driver license validity for control WP-0446-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-18", "metric": "driver_license_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-18", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-18", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-18", "metric": "driver_license_days_left", "label": "driver license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "driver license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_capital_budget_variance_pct_19(record):
    """Evaluate capital budget variance for control WP-0446-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capital_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-19", "metric": "capital_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-19", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-19", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-19", "metric": "capital_budget_variance_pct", "label": "capital budget variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "capital budget variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_bcp_test_age_days_20(record):
    """Evaluate supplier continuity test age for control WP-0446-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-20", "metric": "supplier_bcp_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-20", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-20", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-20", "metric": "supplier_bcp_test_age_days", "label": "supplier continuity test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier continuity test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_capability_index_21(record):
    """Evaluate supplier capability index for control WP-0446-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-21", "metric": "supplier_capability_index",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-21", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-21", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-21", "metric": "supplier_capability_index", "label": "supplier capability index",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capability index must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_currency_exposure_pct_22(record):
    """Evaluate supplier currency exposure for control WP-0446-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_currency_exposure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-22", "metric": "supplier_currency_exposure_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-22", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-22", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-22", "metric": "supplier_currency_exposure_pct", "label": "supplier currency exposure",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier currency exposure exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_runbook_age_days_23(record):
    """Evaluate supplier runbook age for control WP-0446-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-23", "metric": "supplier_runbook_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-23", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-23", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-23", "metric": "supplier_runbook_age_days", "label": "supplier runbook age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier runbook age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_country_label_pct_24(record):
    """Evaluate supplier country-label compliance for control WP-0446-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0446-24", "metric": "supplier_country_label_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0446-24", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0446-24", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0446-24", "metric": "supplier_country_label_pct", "label": "supplier country-label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier country-label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_quality_score_01, assess_carrier_exception_count_02, assess_ergonomic_risk_score_03, assess_insurance_days_left_04, assess_incident_resolution_hours_05, assess_forecast_wape_pct_06, assess_lift_assist_usage_pct_07, assess_recovery_case_age_days_08, assess_traceability_query_minutes_09, assess_lithium_battery_label_pct_10, assess_near_miss_close_rate_pct_11, assess_public_address_test_age_days_12, assess_license_compliance_pct_13, assess_rfid_collision_count_14, assess_stock_age_p95_days_15, assess_cartonization_savings_pct_16, assess_restricted_party_match_count_17, assess_driver_license_days_left_18, assess_capital_budget_variance_pct_19, assess_supplier_bcp_test_age_days_20, assess_supplier_capability_index_21, assess_supplier_currency_exposure_pct_22, assess_supplier_runbook_age_days_23, assess_supplier_country_label_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

