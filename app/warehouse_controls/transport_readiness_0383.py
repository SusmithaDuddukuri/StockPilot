"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_seal_mismatch_count_01(record):
    """Evaluate seal mismatches for control WP-0383-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-01", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-01", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-01", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-01", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "seal mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_pick_path_efficiency_pct_02(record):
    """Evaluate pick path efficiency for control WP-0383-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-02", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-02", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-02", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-02", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick path efficiency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_mean_time_between_failures_hours_03(record):
    """Evaluate mean time between failures for control WP-0383-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-03", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-03", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-03", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-03", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "mean time between failures exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_payment_term_days_04(record):
    """Evaluate payment terms for control WP-0383-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-04", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-04", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-04", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-04", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "payment terms falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_database_connection_pct_05(record):
    """Evaluate database connection utilization for control WP-0383-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-05", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-05", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-05", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-05", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "database connection utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_moq_violation_count_06(record):
    """Evaluate minimum order quantity violations for control WP-0383-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("moq_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-06", "metric": "moq_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-06", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-06", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-06", "metric": "moq_violation_count", "label": "minimum order quantity violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "minimum order quantity violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_shift_length_hours_07(record):
    """Evaluate shift length for control WP-0383-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_length_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-07", "metric": "shift_length_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-07", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-07", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-07", "metric": "shift_length_hours", "label": "shift length",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "shift length exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_waste_manifest_pct_08(record):
    """Evaluate waste manifest completion for control WP-0383-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-08", "metric": "waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-08", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-08", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-08", "metric": "waste_manifest_pct", "label": "waste manifest completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "waste manifest completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_tamper_evident_seal_pct_09(record):
    """Evaluate tamper-evident seal use for control WP-0383-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_evident_seal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-09", "metric": "tamper_evident_seal_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-09", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-09", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-09", "metric": "tamper_evident_seal_pct", "label": "tamper-evident seal use",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tamper-evident seal use must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_gas_detector_test_age_days_10(record):
    """Evaluate gas detector test age for control WP-0383-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gas_detector_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-10", "metric": "gas_detector_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-10", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-10", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-10", "metric": "gas_detector_test_age_days", "label": "gas detector test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "gas detector test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_maintenance_backlog_count_11(record):
    """Evaluate maintenance backlog for control WP-0383-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_backlog_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-11", "metric": "maintenance_backlog_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "jobs",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-11", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-11", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-11", "metric": "maintenance_backlog_count", "label": "maintenance backlog",
        "status": "breach", "severity": "medium", "unit": "jobs",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "maintenance backlog exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_recovery_time_minutes_12(record):
    """Evaluate recovery time for control WP-0383-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-12", "metric": "recovery_time_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-12", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-12", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-12", "metric": "recovery_time_minutes", "label": "recovery time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "recovery time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_data_validation_failure_pct_13(record):
    """Evaluate data validation failure rate for control WP-0383-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_validation_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-13", "metric": "data_validation_failure_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-13", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-13", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-13", "metric": "data_validation_failure_pct", "label": "data validation failure rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data validation failure rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_master_gap_count_14(record):
    """Evaluate supplier master gaps for control WP-0383-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-14", "metric": "supplier_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-14", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-14", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-14", "metric": "supplier_master_gap_count", "label": "supplier master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_alternative_supplier_coverage_pct_15(record):
    """Evaluate alternative supplier coverage for control WP-0383-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alternative_supplier_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-15", "metric": "alternative_supplier_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-15", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-15", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-15", "metric": "alternative_supplier_coverage_pct", "label": "alternative supplier coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "alternative supplier coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_linehaul_departure_delay_minutes_16(record):
    """Evaluate linehaul departure delay for control WP-0383-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("linehaul_departure_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-16", "metric": "linehaul_departure_delay_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-16", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-16", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-16", "metric": "linehaul_departure_delay_minutes", "label": "linehaul departure delay",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "linehaul departure delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_carrier_invoice_match_pct_17(record):
    """Evaluate carrier invoice match for control WP-0383-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-17", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-17", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-17", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-17", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_geofence_breach_count_18(record):
    """Evaluate geofence breaches for control WP-0383-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("geofence_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-18", "metric": "geofence_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-18", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-18", "metric": "geofence_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-18", "metric": "geofence_breach_count", "label": "geofence breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "geofence breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_contract_renewal_days_left_19(record):
    """Evaluate contract renewal validity for control WP-0383-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contract_renewal_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-19", "metric": "contract_renewal_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-19", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-19", "metric": "contract_renewal_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-19", "metric": "contract_renewal_days_left", "label": "contract renewal validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "contract renewal validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_material_traceability_pct_20(record):
    """Evaluate supplier material traceability for control WP-0383-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-20", "metric": "supplier_material_traceability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-20", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-20", "metric": "supplier_material_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-20", "metric": "supplier_material_traceability_pct", "label": "supplier material traceability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier material traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_label_validation_age_days_21(record):
    """Evaluate supplier label validation age for control WP-0383-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_validation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-21", "metric": "supplier_label_validation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-21", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-21", "metric": "supplier_label_validation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-21", "metric": "supplier_label_validation_age_days", "label": "supplier label validation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label validation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_sanctions_screen_age_days_22(record):
    """Evaluate supplier sanctions-screen age for control WP-0383-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_screen_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-22", "metric": "supplier_sanctions_screen_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-22", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-22", "metric": "supplier_sanctions_screen_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-22", "metric": "supplier_sanctions_screen_age_days", "label": "supplier sanctions-screen age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sanctions-screen age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_concentration_risk_score_23(record):
    """Evaluate supplier concentration risk for control WP-0383-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-23", "metric": "supplier_concentration_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-23", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-23", "metric": "supplier_concentration_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-23", "metric": "supplier_concentration_risk_score", "label": "supplier concentration risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "supplier concentration risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_repairability_score_24(record):
    """Evaluate supplier repairability for control WP-0383-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_repairability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0383-24", "metric": "supplier_repairability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0383-24", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0383-24", "metric": "supplier_repairability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0383-24", "metric": "supplier_repairability_score", "label": "supplier repairability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier repairability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_seal_mismatch_count_01, assess_pick_path_efficiency_pct_02, assess_mean_time_between_failures_hours_03, assess_payment_term_days_04, assess_database_connection_pct_05, assess_moq_violation_count_06, assess_shift_length_hours_07, assess_waste_manifest_pct_08, assess_tamper_evident_seal_pct_09, assess_gas_detector_test_age_days_10, assess_maintenance_backlog_count_11, assess_recovery_time_minutes_12, assess_data_validation_failure_pct_13, assess_supplier_master_gap_count_14, assess_alternative_supplier_coverage_pct_15, assess_linehaul_departure_delay_minutes_16, assess_carrier_invoice_match_pct_17, assess_geofence_breach_count_18, assess_contract_renewal_days_left_19, assess_supplier_material_traceability_pct_20, assess_supplier_label_validation_age_days_21, assess_supplier_sanctions_screen_age_days_22, assess_supplier_concentration_risk_score_23, assess_supplier_repairability_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

