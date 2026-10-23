"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_weight_kg_01(record):
    """Evaluate handling weight for control WP-0128-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-01", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-01", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-01", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-01", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "handling weight falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_seal_mismatch_count_02(record):
    """Evaluate seal mismatches for control WP-0128-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-02", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-02", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-02", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-02", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seal mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_pick_path_efficiency_pct_03(record):
    """Evaluate pick path efficiency for control WP-0128-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-03", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-03", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-03", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-03", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick path efficiency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_mean_time_between_failures_hours_04(record):
    """Evaluate mean time between failures for control WP-0128-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-04", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-04", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-04", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-04", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "mean time between failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_payment_term_days_05(record):
    """Evaluate payment terms for control WP-0128-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-05", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-05", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-05", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-05", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "payment terms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_database_connection_pct_06(record):
    """Evaluate database connection utilization for control WP-0128-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-06", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-06", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-06", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-06", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "database connection utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_moq_violation_count_07(record):
    """Evaluate minimum order quantity violations for control WP-0128-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("moq_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-07", "metric": "moq_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-07", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-07", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-07", "metric": "moq_violation_count", "label": "minimum order quantity violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum order quantity violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_shift_length_hours_08(record):
    """Evaluate shift length for control WP-0128-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_length_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-08", "metric": "shift_length_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-08", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-08", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-08", "metric": "shift_length_hours", "label": "shift length",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "shift length exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_waste_manifest_pct_09(record):
    """Evaluate waste manifest completion for control WP-0128-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-09", "metric": "waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-09", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-09", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-09", "metric": "waste_manifest_pct", "label": "waste manifest completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "waste manifest completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_tamper_evident_seal_pct_10(record):
    """Evaluate tamper-evident seal use for control WP-0128-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_evident_seal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-10", "metric": "tamper_evident_seal_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-10", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-10", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-10", "metric": "tamper_evident_seal_pct", "label": "tamper-evident seal use",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tamper-evident seal use must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_gas_detector_test_age_days_11(record):
    """Evaluate gas detector test age for control WP-0128-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gas_detector_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-11", "metric": "gas_detector_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-11", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-11", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-11", "metric": "gas_detector_test_age_days", "label": "gas detector test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "gas detector test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_maintenance_backlog_count_12(record):
    """Evaluate maintenance backlog for control WP-0128-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_backlog_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-12", "metric": "maintenance_backlog_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "jobs",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-12", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-12", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-12", "metric": "maintenance_backlog_count", "label": "maintenance backlog",
        "status": "breach", "severity": "critical", "unit": "jobs",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "maintenance backlog exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_recovery_time_minutes_13(record):
    """Evaluate recovery time for control WP-0128-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-13", "metric": "recovery_time_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-13", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-13", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-13", "metric": "recovery_time_minutes", "label": "recovery time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "recovery time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_data_validation_failure_pct_14(record):
    """Evaluate data validation failure rate for control WP-0128-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_validation_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-14", "metric": "data_validation_failure_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-14", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-14", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-14", "metric": "data_validation_failure_pct", "label": "data validation failure rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data validation failure rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_master_gap_count_15(record):
    """Evaluate supplier master gaps for control WP-0128-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-15", "metric": "supplier_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-15", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-15", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-15", "metric": "supplier_master_gap_count", "label": "supplier master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_alternative_supplier_coverage_pct_16(record):
    """Evaluate alternative supplier coverage for control WP-0128-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alternative_supplier_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-16", "metric": "alternative_supplier_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-16", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-16", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-16", "metric": "alternative_supplier_coverage_pct", "label": "alternative supplier coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "alternative supplier coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_linehaul_departure_delay_minutes_17(record):
    """Evaluate linehaul departure delay for control WP-0128-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("linehaul_departure_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-17", "metric": "linehaul_departure_delay_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-17", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-17", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-17", "metric": "linehaul_departure_delay_minutes", "label": "linehaul departure delay",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "linehaul departure delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_carrier_invoice_match_pct_18(record):
    """Evaluate carrier invoice match for control WP-0128-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-18", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-18", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-18", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-18", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_geofence_breach_count_19(record):
    """Evaluate geofence breaches for control WP-0128-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("geofence_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-19", "metric": "geofence_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-19", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-19", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-19", "metric": "geofence_breach_count", "label": "geofence breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "geofence breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_contract_renewal_days_left_20(record):
    """Evaluate contract renewal validity for control WP-0128-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_renewal_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-20", "metric": "contract_renewal_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-20", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-20", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-20", "metric": "contract_renewal_days_left", "label": "contract renewal validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "contract renewal validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_material_traceability_pct_21(record):
    """Evaluate supplier material traceability for control WP-0128-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-21", "metric": "supplier_material_traceability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-21", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-21", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-21", "metric": "supplier_material_traceability_pct", "label": "supplier material traceability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier material traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_label_validation_age_days_22(record):
    """Evaluate supplier label validation age for control WP-0128-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-22", "metric": "supplier_label_validation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-22", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-22", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-22", "metric": "supplier_label_validation_age_days", "label": "supplier label validation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label validation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_sanctions_screen_age_days_23(record):
    """Evaluate supplier sanctions-screen age for control WP-0128-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_screen_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-23", "metric": "supplier_sanctions_screen_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-23", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-23", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-23", "metric": "supplier_sanctions_screen_age_days", "label": "supplier sanctions-screen age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sanctions-screen age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_concentration_risk_score_24(record):
    """Evaluate supplier concentration risk for control WP-0128-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0128-24", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0128-24", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0128-24", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0128-24", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier concentration risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_weight_kg_01, assess_seal_mismatch_count_02, assess_pick_path_efficiency_pct_03, assess_mean_time_between_failures_hours_04, assess_payment_term_days_05, assess_database_connection_pct_06, assess_moq_violation_count_07, assess_shift_length_hours_08, assess_waste_manifest_pct_09, assess_tamper_evident_seal_pct_10, assess_gas_detector_test_age_days_11, assess_maintenance_backlog_count_12, assess_recovery_time_minutes_13, assess_data_validation_failure_pct_14, assess_supplier_master_gap_count_15, assess_alternative_supplier_coverage_pct_16, assess_linehaul_departure_delay_minutes_17, assess_carrier_invoice_match_pct_18, assess_geofence_breach_count_19, assess_contract_renewal_days_left_20, assess_supplier_material_traceability_pct_21, assess_supplier_label_validation_age_days_22, assess_supplier_sanctions_screen_age_days_23, assess_supplier_concentration_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

