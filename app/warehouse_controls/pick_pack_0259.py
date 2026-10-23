"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_ergonomic_risk_score_01(record):
    """Evaluate ergonomic risk for control WP-0259-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-01", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-01", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-01", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-01", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ergonomic risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_insurance_days_left_02(record):
    """Evaluate insurance validity for control WP-0259-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-02", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-02", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-02", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-02", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insurance validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_incident_resolution_hours_03(record):
    """Evaluate incident resolution for control WP-0259-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-03", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-03", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-03", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-03", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "incident resolution exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_forecast_wape_pct_04(record):
    """Evaluate forecast WAPE for control WP-0259-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_wape_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-04", "metric": "forecast_wape_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-04", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-04", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-04", "metric": "forecast_wape_pct", "label": "forecast WAPE",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "forecast WAPE falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_lift_assist_usage_pct_05(record):
    """Evaluate lift-assist usage for control WP-0259-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lift_assist_usage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-05", "metric": "lift_assist_usage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-05", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-05", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-05", "metric": "lift_assist_usage_pct", "label": "lift-assist usage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lift-assist usage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_recovery_case_age_days_06(record):
    """Evaluate recovery case age for control WP-0259-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_case_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-06", "metric": "recovery_case_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-06", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-06", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-06", "metric": "recovery_case_age_days", "label": "recovery case age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recovery case age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_traceability_query_minutes_07(record):
    """Evaluate traceability query time for control WP-0259-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("traceability_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-07", "metric": "traceability_query_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-07", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-07", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-07", "metric": "traceability_query_minutes", "label": "traceability query time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "traceability query time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_lithium_battery_label_pct_08(record):
    """Evaluate lithium battery label compliance for control WP-0259-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lithium_battery_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-08", "metric": "lithium_battery_label_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-08", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-08", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-08", "metric": "lithium_battery_label_pct", "label": "lithium battery label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "lithium battery label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_near_miss_close_rate_pct_09(record):
    """Evaluate near-miss close rate for control WP-0259-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_close_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-09", "metric": "near_miss_close_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-09", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-09", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-09", "metric": "near_miss_close_rate_pct", "label": "near-miss close rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "near-miss close rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_public_address_test_age_days_10(record):
    """Evaluate public-address test age for control WP-0259-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("public_address_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-10", "metric": "public_address_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-10", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-10", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-10", "metric": "public_address_test_age_days", "label": "public-address test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "public-address test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_license_compliance_pct_11(record):
    """Evaluate license compliance for control WP-0259-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-11", "metric": "license_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-11", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-11", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-11", "metric": "license_compliance_pct", "label": "license compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "license compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_rfid_collision_count_12(record):
    """Evaluate RFID collisions for control WP-0259-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_collision_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-12", "metric": "rfid_collision_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-12", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-12", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-12", "metric": "rfid_collision_count", "label": "RFID collisions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "RFID collisions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_stock_age_p95_days_13(record):
    """Evaluate 95th percentile stock age for control WP-0259-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_p95_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-13", "metric": "stock_age_p95_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-13", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-13", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-13", "metric": "stock_age_p95_days", "label": "95th percentile stock age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "95th percentile stock age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_cartonization_savings_pct_14(record):
    """Evaluate cartonization savings for control WP-0259-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cartonization_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-14", "metric": "cartonization_savings_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-14", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-14", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-14", "metric": "cartonization_savings_pct", "label": "cartonization savings",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cartonization savings must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_restricted_party_match_count_15(record):
    """Evaluate restricted-party matches for control WP-0259-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-15", "metric": "restricted_party_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-15", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-15", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-15", "metric": "restricted_party_match_count", "label": "restricted-party matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "restricted-party matches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_driver_license_days_left_16(record):
    """Evaluate driver license validity for control WP-0259-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-16", "metric": "driver_license_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-16", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-16", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-16", "metric": "driver_license_days_left", "label": "driver license validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "driver license validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_capital_budget_variance_pct_17(record):
    """Evaluate capital budget variance for control WP-0259-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capital_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-17", "metric": "capital_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-17", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-17", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-17", "metric": "capital_budget_variance_pct", "label": "capital budget variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "capital budget variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_bcp_test_age_days_18(record):
    """Evaluate supplier continuity test age for control WP-0259-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-18", "metric": "supplier_bcp_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-18", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-18", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-18", "metric": "supplier_bcp_test_age_days", "label": "supplier continuity test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier continuity test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_capability_index_19(record):
    """Evaluate supplier capability index for control WP-0259-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-19", "metric": "supplier_capability_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-19", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-19", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-19", "metric": "supplier_capability_index", "label": "supplier capability index",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier capability index exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_currency_exposure_pct_20(record):
    """Evaluate supplier currency exposure for control WP-0259-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_currency_exposure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-20", "metric": "supplier_currency_exposure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-20", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-20", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-20", "metric": "supplier_currency_exposure_pct", "label": "supplier currency exposure",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier currency exposure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_runbook_age_days_21(record):
    """Evaluate supplier runbook age for control WP-0259-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-21", "metric": "supplier_runbook_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-21", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-21", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-21", "metric": "supplier_runbook_age_days", "label": "supplier runbook age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier runbook age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_country_label_pct_22(record):
    """Evaluate supplier country-label compliance for control WP-0259-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-22", "metric": "supplier_country_label_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-22", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-22", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-22", "metric": "supplier_country_label_pct", "label": "supplier country-label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier country-label compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_driver_briefing_pct_23(record):
    """Evaluate supplier driver briefing completion for control WP-0259-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_driver_briefing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-23", "metric": "supplier_driver_briefing_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-23", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-23", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-23", "metric": "supplier_driver_briefing_pct", "label": "supplier driver briefing completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier driver briefing completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_process_change_approval_pct_24(record):
    """Evaluate supplier process-change approval for control WP-0259-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0259-24", "metric": "supplier_process_change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0259-24", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0259-24", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0259-24", "metric": "supplier_process_change_approval_pct", "label": "supplier process-change approval",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier process-change approval falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_ergonomic_risk_score_01, assess_insurance_days_left_02, assess_incident_resolution_hours_03, assess_forecast_wape_pct_04, assess_lift_assist_usage_pct_05, assess_recovery_case_age_days_06, assess_traceability_query_minutes_07, assess_lithium_battery_label_pct_08, assess_near_miss_close_rate_pct_09, assess_public_address_test_age_days_10, assess_license_compliance_pct_11, assess_rfid_collision_count_12, assess_stock_age_p95_days_13, assess_cartonization_savings_pct_14, assess_restricted_party_match_count_15, assess_driver_license_days_left_16, assess_capital_budget_variance_pct_17, assess_supplier_bcp_test_age_days_18, assess_supplier_capability_index_19, assess_supplier_currency_exposure_pct_20, assess_supplier_runbook_age_days_21, assess_supplier_country_label_pct_22, assess_supplier_driver_briefing_pct_23, assess_supplier_process_change_approval_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

