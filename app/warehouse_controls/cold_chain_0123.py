"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_first_pass_yield_pct_01(record):
    """Evaluate supplier first-pass yield for control WP-0123-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_first_pass_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-01", "metric": "supplier_first_pass_yield_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-01", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-01", "metric": "supplier_first_pass_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-01", "metric": "supplier_first_pass_yield_pct", "label": "supplier first-pass yield",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier first-pass yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_joint_planning_age_days_02(record):
    """Evaluate joint planning age for control WP-0123-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_joint_planning_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-02", "metric": "supplier_joint_planning_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-02", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-02", "metric": "supplier_joint_planning_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-02", "metric": "supplier_joint_planning_age_days", "label": "joint planning age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "joint planning age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_partner_notice_pct_03(record):
    """Evaluate supplier partner notice completion for control WP-0123-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_partner_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-03", "metric": "supplier_partner_notice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-03", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-03", "metric": "supplier_partner_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-03", "metric": "supplier_partner_notice_pct", "label": "supplier partner notice completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "supplier partner notice completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_forecast_error_pct_04(record):
    """Evaluate forecast error for control WP-0123-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-04", "metric": "forecast_error_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-04", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-04", "metric": "forecast_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-04", "metric": "forecast_error_pct", "label": "forecast error",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "forecast error falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_quality_score_05(record):
    """Evaluate quality score for control WP-0123-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-05", "metric": "quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-05", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-05", "metric": "quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-05", "metric": "quality_score", "label": "quality score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quality score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_carrier_exception_count_06(record):
    """Evaluate carrier exceptions for control WP-0123-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-06", "metric": "carrier_exception_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-06", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-06", "metric": "carrier_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-06", "metric": "carrier_exception_count", "label": "carrier exceptions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carrier exceptions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_ergonomic_risk_score_07(record):
    """Evaluate ergonomic risk for control WP-0123-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ergonomic_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-07", "metric": "ergonomic_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-07", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-07", "metric": "ergonomic_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-07", "metric": "ergonomic_risk_score", "label": "ergonomic risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "ergonomic risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_insurance_days_left_08(record):
    """Evaluate insurance validity for control WP-0123-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-08", "metric": "insurance_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-08", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-08", "metric": "insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-08", "metric": "insurance_days_left", "label": "insurance validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "insurance validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_incident_resolution_hours_09(record):
    """Evaluate incident resolution for control WP-0123-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-09", "metric": "incident_resolution_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-09", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-09", "metric": "incident_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-09", "metric": "incident_resolution_hours", "label": "incident resolution",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "incident resolution must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_forecast_wape_pct_10(record):
    """Evaluate forecast WAPE for control WP-0123-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_wape_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-10", "metric": "forecast_wape_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-10", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-10", "metric": "forecast_wape_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-10", "metric": "forecast_wape_pct", "label": "forecast WAPE",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forecast WAPE must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_lift_assist_usage_pct_11(record):
    """Evaluate lift-assist usage for control WP-0123-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lift_assist_usage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-11", "metric": "lift_assist_usage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-11", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-11", "metric": "lift_assist_usage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-11", "metric": "lift_assist_usage_pct", "label": "lift-assist usage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "lift-assist usage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_recovery_case_age_days_12(record):
    """Evaluate recovery case age for control WP-0123-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_case_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-12", "metric": "recovery_case_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-12", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-12", "metric": "recovery_case_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-12", "metric": "recovery_case_age_days", "label": "recovery case age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "recovery case age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_traceability_query_minutes_13(record):
    """Evaluate traceability query time for control WP-0123-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("traceability_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-13", "metric": "traceability_query_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-13", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-13", "metric": "traceability_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-13", "metric": "traceability_query_minutes", "label": "traceability query time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "traceability query time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_lithium_battery_label_pct_14(record):
    """Evaluate lithium battery label compliance for control WP-0123-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lithium_battery_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-14", "metric": "lithium_battery_label_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-14", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-14", "metric": "lithium_battery_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-14", "metric": "lithium_battery_label_pct", "label": "lithium battery label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lithium battery label compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_near_miss_close_rate_pct_15(record):
    """Evaluate near-miss close rate for control WP-0123-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("near_miss_close_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-15", "metric": "near_miss_close_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-15", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-15", "metric": "near_miss_close_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-15", "metric": "near_miss_close_rate_pct", "label": "near-miss close rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "near-miss close rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_public_address_test_age_days_16(record):
    """Evaluate public-address test age for control WP-0123-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("public_address_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-16", "metric": "public_address_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-16", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-16", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-16", "metric": "public_address_test_age_days", "label": "public-address test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "public-address test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_license_compliance_pct_17(record):
    """Evaluate license compliance for control WP-0123-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-17", "metric": "license_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-17", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-17", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-17", "metric": "license_compliance_pct", "label": "license compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "license compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_rfid_collision_count_18(record):
    """Evaluate RFID collisions for control WP-0123-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_collision_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-18", "metric": "rfid_collision_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-18", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-18", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-18", "metric": "rfid_collision_count", "label": "RFID collisions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "RFID collisions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_stock_age_p95_days_19(record):
    """Evaluate 95th percentile stock age for control WP-0123-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_p95_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-19", "metric": "stock_age_p95_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-19", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-19", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-19", "metric": "stock_age_p95_days", "label": "95th percentile stock age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "95th percentile stock age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_cartonization_savings_pct_20(record):
    """Evaluate cartonization savings for control WP-0123-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cartonization_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-20", "metric": "cartonization_savings_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-20", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-20", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-20", "metric": "cartonization_savings_pct", "label": "cartonization savings",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "cartonization savings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_restricted_party_match_count_21(record):
    """Evaluate restricted-party matches for control WP-0123-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-21", "metric": "restricted_party_match_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-21", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-21", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-21", "metric": "restricted_party_match_count", "label": "restricted-party matches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restricted-party matches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_driver_license_days_left_22(record):
    """Evaluate driver license validity for control WP-0123-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-22", "metric": "driver_license_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-22", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-22", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-22", "metric": "driver_license_days_left", "label": "driver license validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "driver license validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_capital_budget_variance_pct_23(record):
    """Evaluate capital budget variance for control WP-0123-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capital_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-23", "metric": "capital_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-23", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-23", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-23", "metric": "capital_budget_variance_pct", "label": "capital budget variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "capital budget variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_bcp_test_age_days_24(record):
    """Evaluate supplier continuity test age for control WP-0123-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0123-24", "metric": "supplier_bcp_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0123-24", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0123-24", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0123-24", "metric": "supplier_bcp_test_age_days", "label": "supplier continuity test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier continuity test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_first_pass_yield_pct_01, assess_supplier_joint_planning_age_days_02, assess_supplier_partner_notice_pct_03, assess_forecast_error_pct_04, assess_quality_score_05, assess_carrier_exception_count_06, assess_ergonomic_risk_score_07, assess_insurance_days_left_08, assess_incident_resolution_hours_09, assess_forecast_wape_pct_10, assess_lift_assist_usage_pct_11, assess_recovery_case_age_days_12, assess_traceability_query_minutes_13, assess_lithium_battery_label_pct_14, assess_near_miss_close_rate_pct_15, assess_public_address_test_age_days_16, assess_license_compliance_pct_17, assess_rfid_collision_count_18, assess_stock_age_p95_days_19, assess_cartonization_savings_pct_20, assess_restricted_party_match_count_21, assess_driver_license_days_left_22, assess_capital_budget_variance_pct_23, assess_supplier_bcp_test_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

