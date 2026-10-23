"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_gas_detector_test_age_days_01(record):
    """Evaluate gas detector test age for control WP-0208-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gas_detector_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-01", "metric": "gas_detector_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-01", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-01", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-01", "metric": "gas_detector_test_age_days", "label": "gas detector test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "gas detector test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_maintenance_backlog_count_02(record):
    """Evaluate maintenance backlog for control WP-0208-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_backlog_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-02", "metric": "maintenance_backlog_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "jobs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-02", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-02", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-02", "metric": "maintenance_backlog_count", "label": "maintenance backlog",
        "status": "breach", "severity": "medium", "unit": "jobs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "maintenance backlog must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_recovery_time_minutes_03(record):
    """Evaluate recovery time for control WP-0208-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-03", "metric": "recovery_time_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-03", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-03", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-03", "metric": "recovery_time_minutes", "label": "recovery time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recovery time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_data_validation_failure_pct_04(record):
    """Evaluate data validation failure rate for control WP-0208-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_validation_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-04", "metric": "data_validation_failure_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-04", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-04", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-04", "metric": "data_validation_failure_pct", "label": "data validation failure rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "data validation failure rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_master_gap_count_05(record):
    """Evaluate supplier master gaps for control WP-0208-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-05", "metric": "supplier_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-05", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-05", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-05", "metric": "supplier_master_gap_count", "label": "supplier master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_alternative_supplier_coverage_pct_06(record):
    """Evaluate alternative supplier coverage for control WP-0208-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alternative_supplier_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-06", "metric": "alternative_supplier_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-06", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-06", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-06", "metric": "alternative_supplier_coverage_pct", "label": "alternative supplier coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "alternative supplier coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_linehaul_departure_delay_minutes_07(record):
    """Evaluate linehaul departure delay for control WP-0208-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("linehaul_departure_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-07", "metric": "linehaul_departure_delay_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-07", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-07", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-07", "metric": "linehaul_departure_delay_minutes", "label": "linehaul departure delay",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "linehaul departure delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_carrier_invoice_match_pct_08(record):
    """Evaluate carrier invoice match for control WP-0208-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-08", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-08", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-08", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-08", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "carrier invoice match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_geofence_breach_count_09(record):
    """Evaluate geofence breaches for control WP-0208-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("geofence_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-09", "metric": "geofence_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-09", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-09", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-09", "metric": "geofence_breach_count", "label": "geofence breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "geofence breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_contract_renewal_days_left_10(record):
    """Evaluate contract renewal validity for control WP-0208-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_renewal_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-10", "metric": "contract_renewal_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-10", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-10", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-10", "metric": "contract_renewal_days_left", "label": "contract renewal validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "contract renewal validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_material_traceability_pct_11(record):
    """Evaluate supplier material traceability for control WP-0208-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-11", "metric": "supplier_material_traceability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-11", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-11", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-11", "metric": "supplier_material_traceability_pct", "label": "supplier material traceability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier material traceability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_label_validation_age_days_12(record):
    """Evaluate supplier label validation age for control WP-0208-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-12", "metric": "supplier_label_validation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-12", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-12", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-12", "metric": "supplier_label_validation_age_days", "label": "supplier label validation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier label validation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_sanctions_screen_age_days_13(record):
    """Evaluate supplier sanctions-screen age for control WP-0208-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_screen_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-13", "metric": "supplier_sanctions_screen_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-13", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-13", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-13", "metric": "supplier_sanctions_screen_age_days", "label": "supplier sanctions-screen age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "supplier sanctions-screen age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_concentration_risk_score_14(record):
    """Evaluate supplier concentration risk for control WP-0208-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-14", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-14", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-14", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-14", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier concentration risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_repairability_score_15(record):
    """Evaluate supplier repairability for control WP-0208-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repairability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-15", "metric": "supplier_repairability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-15", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-15", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-15", "metric": "supplier_repairability_score", "label": "supplier repairability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier repairability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_customer_complaint_rate_pct_16(record):
    """Evaluate supplier customer complaint rate for control WP-0208-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_complaint_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-16", "metric": "supplier_customer_complaint_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-16", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-16", "metric": "supplier_customer_complaint_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-16", "metric": "supplier_customer_complaint_rate_pct", "label": "supplier customer complaint rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier customer complaint rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_control_plan_age_days_17(record):
    """Evaluate supplier control-plan age for control WP-0208-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-17", "metric": "supplier_control_plan_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-17", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-17", "metric": "supplier_control_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-17", "metric": "supplier_control_plan_age_days", "label": "supplier control-plan age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier control-plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_evacuation_drill_age_days_18(record):
    """Evaluate supplier evacuation drill age for control WP-0208-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evacuation_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-18", "metric": "supplier_evacuation_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-18", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-18", "metric": "supplier_evacuation_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-18", "metric": "supplier_evacuation_drill_age_days", "label": "supplier evacuation drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier evacuation drill age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_cash_runway_days_19(record):
    """Evaluate supplier cash runway for control WP-0208-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cash_runway_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-19", "metric": "supplier_cash_runway_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-19", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-19", "metric": "supplier_cash_runway_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-19", "metric": "supplier_cash_runway_days", "label": "supplier cash runway",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cash runway must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_document_control_pct_20(record):
    """Evaluate supplier document control for control WP-0208-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-20", "metric": "supplier_document_control_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-20", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-20", "metric": "supplier_document_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-20", "metric": "supplier_document_control_pct", "label": "supplier document control",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier document control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_model_card_age_days_21(record):
    """Evaluate supplier model-card age for control WP-0208-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_card_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-21", "metric": "supplier_model_card_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-21", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-21", "metric": "supplier_model_card_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-21", "metric": "supplier_model_card_age_days", "label": "supplier model-card age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "supplier model-card age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_ordering_violation_count_22(record):
    """Evaluate supplier ordering violations for control WP-0208-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ordering_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-22", "metric": "supplier_ordering_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-22", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-22", "metric": "supplier_ordering_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-22", "metric": "supplier_ordering_violation_count", "label": "supplier ordering violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ordering violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_vulnerability_sla_breach_count_23(record):
    """Evaluate supplier vulnerability SLA breaches for control WP-0208-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-23", "metric": "supplier_vulnerability_sla_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-23", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-23", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-23", "metric": "supplier_vulnerability_sla_breach_count", "label": "supplier vulnerability SLA breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier vulnerability SLA breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_media_encryption_pct_24(record):
    """Evaluate supplier media encryption for control WP-0208-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_media_encryption_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0208-24", "metric": "supplier_media_encryption_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0208-24", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0208-24", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0208-24", "metric": "supplier_media_encryption_pct", "label": "supplier media encryption",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier media encryption exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_gas_detector_test_age_days_01, assess_maintenance_backlog_count_02, assess_recovery_time_minutes_03, assess_data_validation_failure_pct_04, assess_supplier_master_gap_count_05, assess_alternative_supplier_coverage_pct_06, assess_linehaul_departure_delay_minutes_07, assess_carrier_invoice_match_pct_08, assess_geofence_breach_count_09, assess_contract_renewal_days_left_10, assess_supplier_material_traceability_pct_11, assess_supplier_label_validation_age_days_12, assess_supplier_sanctions_screen_age_days_13, assess_supplier_concentration_risk_score_14, assess_supplier_repairability_score_15, assess_supplier_customer_complaint_rate_pct_16, assess_supplier_control_plan_age_days_17, assess_supplier_evacuation_drill_age_days_18, assess_supplier_cash_runway_days_19, assess_supplier_document_control_pct_20, assess_supplier_model_card_age_days_21, assess_supplier_ordering_violation_count_22, assess_supplier_vulnerability_sla_breach_count_23, assess_supplier_media_encryption_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

