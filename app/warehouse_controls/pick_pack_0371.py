"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_subprocessor_notice_pct_01(record):
    """Evaluate supplier subprocessor notice compliance for control WP-0371-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subprocessor_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-01", "metric": "supplier_subprocessor_notice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-01", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-01", "metric": "supplier_subprocessor_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-01", "metric": "supplier_subprocessor_notice_pct", "label": "supplier subprocessor notice compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier subprocessor notice compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_kri_breach_count_02(record):
    """Evaluate supplier KRI breaches for control WP-0371-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kri_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-02", "metric": "supplier_kri_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-02", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-02", "metric": "supplier_kri_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-02", "metric": "supplier_kri_breach_count", "label": "supplier KRI breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KRI breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_po_after_invoice_count_03(record):
    """Evaluate PO-after-invoice events for control WP-0371-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_po_after_invoice_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-03", "metric": "supplier_po_after_invoice_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-03", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-03", "metric": "supplier_po_after_invoice_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-03", "metric": "supplier_po_after_invoice_count", "label": "PO-after-invoice events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "PO-after-invoice events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_tool_changeover_minutes_04(record):
    """Evaluate supplier tool changeover for control WP-0371-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tool_changeover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-04", "metric": "supplier_tool_changeover_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-04", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-04", "metric": "supplier_tool_changeover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-04", "metric": "supplier_tool_changeover_minutes", "label": "supplier tool changeover",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier tool changeover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_reporting_lag_hours_05(record):
    """Evaluate supplier reporting lag for control WP-0371-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reporting_lag_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-05", "metric": "supplier_reporting_lag_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-05", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-05", "metric": "supplier_reporting_lag_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-05", "metric": "supplier_reporting_lag_hours", "label": "supplier reporting lag",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier reporting lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_retention_exception_resolution_pct_06(record):
    """Evaluate supplier retention exception resolution for control WP-0371-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-06", "metric": "supplier_retention_exception_resolution_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-06", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-06", "metric": "supplier_retention_exception_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-06", "metric": "supplier_retention_exception_resolution_pct", "label": "supplier retention exception resolution",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier retention exception resolution must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_weight_kg_07(record):
    """Evaluate handling weight for control WP-0371-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-07", "metric": "weight_kg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-07", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-07", "metric": "weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-07", "metric": "weight_kg", "label": "handling weight",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "handling weight exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_seal_mismatch_count_08(record):
    """Evaluate seal mismatches for control WP-0371-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-08", "metric": "seal_mismatch_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-08", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-08", "metric": "seal_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-08", "metric": "seal_mismatch_count", "label": "seal mismatches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "seal mismatches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_pick_path_efficiency_pct_09(record):
    """Evaluate pick path efficiency for control WP-0371-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_path_efficiency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-09", "metric": "pick_path_efficiency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-09", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-09", "metric": "pick_path_efficiency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-09", "metric": "pick_path_efficiency_pct", "label": "pick path efficiency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick path efficiency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_mean_time_between_failures_hours_10(record):
    """Evaluate mean time between failures for control WP-0371-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_between_failures_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-10", "metric": "mean_time_between_failures_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-10", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-10", "metric": "mean_time_between_failures_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-10", "metric": "mean_time_between_failures_hours", "label": "mean time between failures",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "mean time between failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_payment_term_days_11(record):
    """Evaluate payment terms for control WP-0371-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_term_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-11", "metric": "payment_term_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-11", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-11", "metric": "payment_term_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-11", "metric": "payment_term_days", "label": "payment terms",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "payment terms exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_database_connection_pct_12(record):
    """Evaluate database connection utilization for control WP-0371-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_connection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-12", "metric": "database_connection_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-12", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-12", "metric": "database_connection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-12", "metric": "database_connection_pct", "label": "database connection utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "database connection utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_moq_violation_count_13(record):
    """Evaluate minimum order quantity violations for control WP-0371-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("moq_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-13", "metric": "moq_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-13", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-13", "metric": "moq_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-13", "metric": "moq_violation_count", "label": "minimum order quantity violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "minimum order quantity violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_shift_length_hours_14(record):
    """Evaluate shift length for control WP-0371-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_length_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-14", "metric": "shift_length_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-14", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-14", "metric": "shift_length_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-14", "metric": "shift_length_hours", "label": "shift length",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "shift length must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_waste_manifest_pct_15(record):
    """Evaluate waste manifest completion for control WP-0371-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-15", "metric": "waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-15", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-15", "metric": "waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-15", "metric": "waste_manifest_pct", "label": "waste manifest completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "waste manifest completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_tamper_evident_seal_pct_16(record):
    """Evaluate tamper-evident seal use for control WP-0371-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_evident_seal_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-16", "metric": "tamper_evident_seal_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-16", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-16", "metric": "tamper_evident_seal_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-16", "metric": "tamper_evident_seal_pct", "label": "tamper-evident seal use",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "tamper-evident seal use falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_gas_detector_test_age_days_17(record):
    """Evaluate gas detector test age for control WP-0371-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gas_detector_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-17", "metric": "gas_detector_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-17", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-17", "metric": "gas_detector_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-17", "metric": "gas_detector_test_age_days", "label": "gas detector test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "gas detector test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_maintenance_backlog_count_18(record):
    """Evaluate maintenance backlog for control WP-0371-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_backlog_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-18", "metric": "maintenance_backlog_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "jobs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-18", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-18", "metric": "maintenance_backlog_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-18", "metric": "maintenance_backlog_count", "label": "maintenance backlog",
        "status": "breach", "severity": "low", "unit": "jobs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "maintenance backlog must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_recovery_time_minutes_19(record):
    """Evaluate recovery time for control WP-0371-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_time_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-19", "metric": "recovery_time_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-19", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-19", "metric": "recovery_time_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-19", "metric": "recovery_time_minutes", "label": "recovery time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "recovery time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_data_validation_failure_pct_20(record):
    """Evaluate data validation failure rate for control WP-0371-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_validation_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-20", "metric": "data_validation_failure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-20", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-20", "metric": "data_validation_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-20", "metric": "data_validation_failure_pct", "label": "data validation failure rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "data validation failure rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_master_gap_count_21(record):
    """Evaluate supplier master gaps for control WP-0371-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-21", "metric": "supplier_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-21", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-21", "metric": "supplier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-21", "metric": "supplier_master_gap_count", "label": "supplier master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_alternative_supplier_coverage_pct_22(record):
    """Evaluate alternative supplier coverage for control WP-0371-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alternative_supplier_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-22", "metric": "alternative_supplier_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-22", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-22", "metric": "alternative_supplier_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-22", "metric": "alternative_supplier_coverage_pct", "label": "alternative supplier coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "alternative supplier coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_linehaul_departure_delay_minutes_23(record):
    """Evaluate linehaul departure delay for control WP-0371-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("linehaul_departure_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-23", "metric": "linehaul_departure_delay_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-23", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-23", "metric": "linehaul_departure_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-23", "metric": "linehaul_departure_delay_minutes", "label": "linehaul departure delay",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "linehaul departure delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_carrier_invoice_match_pct_24(record):
    """Evaluate carrier invoice match for control WP-0371-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0371-24", "metric": "carrier_invoice_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0371-24", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0371-24", "metric": "carrier_invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0371-24", "metric": "carrier_invoice_match_pct", "label": "carrier invoice match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "carrier invoice match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_subprocessor_notice_pct_01, assess_supplier_kri_breach_count_02, assess_supplier_po_after_invoice_count_03, assess_supplier_tool_changeover_minutes_04, assess_supplier_reporting_lag_hours_05, assess_supplier_retention_exception_resolution_pct_06, assess_weight_kg_07, assess_seal_mismatch_count_08, assess_pick_path_efficiency_pct_09, assess_mean_time_between_failures_hours_10, assess_payment_term_days_11, assess_database_connection_pct_12, assess_moq_violation_count_13, assess_shift_length_hours_14, assess_waste_manifest_pct_15, assess_tamper_evident_seal_pct_16, assess_gas_detector_test_age_days_17, assess_maintenance_backlog_count_18, assess_recovery_time_minutes_19, assess_data_validation_failure_pct_20, assess_supplier_master_gap_count_21, assess_alternative_supplier_coverage_pct_22, assess_linehaul_departure_delay_minutes_23, assess_carrier_invoice_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

