"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_quarantine_release_age_hours_01(record):
    """Evaluate quarantine release age for control WP-0522-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quarantine_release_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-01", "metric": "quarantine_release_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-01", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-01", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-01", "metric": "quarantine_release_age_hours", "label": "quarantine release age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quarantine release age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_battery_storage_temp_c_02(record):
    """Evaluate battery storage temperature for control WP-0522-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_storage_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-02", "metric": "battery_storage_temp_c",
            "status": "insufficient_data",
            "severity": "critical", "unit": "C",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-02", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-02", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-02", "metric": "battery_storage_temp_c", "label": "battery storage temperature",
        "status": "breach", "severity": "critical", "unit": "C",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "battery storage temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_working_at_height_permit_pct_03(record):
    """Evaluate working-at-height permit compliance for control WP-0522-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("working_at_height_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-03", "metric": "working_at_height_permit_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-03", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-03", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-03", "metric": "working_at_height_permit_pct", "label": "working-at-height permit compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "working-at-height permit compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_generator_fuel_pct_04(record):
    """Evaluate generator fuel for control WP-0522-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-04", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-04", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-04", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-04", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "generator fuel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_identity_sync_age_hours_05(record):
    """Evaluate identity sync age for control WP-0522-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-05", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-05", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-05", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-05", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "identity sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_weighing_error_pct_06(record):
    """Evaluate weighing error for control WP-0522-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-06", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-06", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-06", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-06", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "weighing error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_cycle_count_completion_pct_07(record):
    """Evaluate cycle-count completion for control WP-0522-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-07", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-07", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-07", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-07", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "cycle-count completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_pick_exception_rate_pct_08(record):
    """Evaluate pick exception rate for control WP-0522-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_exception_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-08", "metric": "pick_exception_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-08", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-08", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-08", "metric": "pick_exception_rate_pct", "label": "pick exception rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick exception rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_import_declaration_age_hours_09(record):
    """Evaluate import declaration age for control WP-0522-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-09", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-09", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-09", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-09", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "import declaration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_axle_load_variance_pct_10(record):
    """Evaluate axle load variance for control WP-0522-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-10", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-10", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-10", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-10", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "axle load variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_orders_per_labor_hour_11(record):
    """Evaluate orders per labor hour for control WP-0522-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orders_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-11", "metric": "orders_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders/hour",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-11", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-11", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-11", "metric": "orders_per_labor_hour", "label": "orders per labor hour",
        "status": "breach", "severity": "low", "unit": "orders/hour",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "orders per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_claim_response_hours_12(record):
    """Evaluate supplier claim response time for control WP-0522-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-12", "metric": "supplier_claim_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-12", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-12", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-12", "metric": "supplier_claim_response_hours", "label": "supplier claim response time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier claim response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_part_substitution_count_13(record):
    """Evaluate supplier part substitutions for control WP-0522-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_part_substitution_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-13", "metric": "supplier_part_substitution_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-13", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-13", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-13", "metric": "supplier_part_substitution_count", "label": "supplier part substitutions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier part substitutions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_invoice_match_rate_pct_14(record):
    """Evaluate supplier invoice match for control WP-0522-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_match_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-14", "metric": "supplier_invoice_match_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-14", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-14", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-14", "metric": "supplier_invoice_match_rate_pct", "label": "supplier invoice match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier invoice match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_escalation_age_hours_15(record):
    """Evaluate supplier escalation age for control WP-0522-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-15", "metric": "supplier_escalation_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-15", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-15", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-15", "metric": "supplier_escalation_age_hours", "label": "supplier escalation age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier escalation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_sds_accuracy_pct_16(record):
    """Evaluate supplier SDS accuracy for control WP-0522-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-16", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-16", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-16", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-16", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier SDS accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_cargo_security_score_17(record):
    """Evaluate supplier cargo security for control WP-0522-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-17", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-17", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-17", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-17", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cargo security must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_work_instruction_age_days_18(record):
    """Evaluate supplier work-instruction age for control WP-0522-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_instruction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-18", "metric": "supplier_work_instruction_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-18", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-18", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-18", "metric": "supplier_work_instruction_age_days", "label": "supplier work-instruction age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier work-instruction age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_conflict_mineral_pct_19(record):
    """Evaluate supplier conflict-mineral reporting for control WP-0522-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_mineral_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-19", "metric": "supplier_conflict_mineral_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-19", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-19", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-19", "metric": "supplier_conflict_mineral_pct", "label": "supplier conflict-mineral reporting",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier conflict-mineral reporting falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_sanctions_update_age_hours_20(record):
    """Evaluate supplier sanctions update age for control WP-0522-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_update_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-20", "metric": "supplier_sanctions_update_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-20", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-20", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-20", "metric": "supplier_sanctions_update_age_hours", "label": "supplier sanctions update age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sanctions update age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_backup_power_pct_21(record):
    """Evaluate supplier backup power coverage for control WP-0522-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_power_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-21", "metric": "supplier_backup_power_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-21", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-21", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-21", "metric": "supplier_backup_power_pct", "label": "supplier backup power coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier backup power coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_model_monitoring_pct_22(record):
    """Evaluate supplier model monitoring for control WP-0522-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-22", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-22", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-22", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-22", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier model monitoring exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_feature_flag_age_days_23(record):
    """Evaluate supplier feature flag age for control WP-0522-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-23", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-23", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-23", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-23", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier feature flag age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_access_token_age_hours_24(record):
    """Evaluate supplier access-token age for control WP-0522-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_token_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0522-24", "metric": "supplier_access_token_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0522-24", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0522-24", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0522-24", "metric": "supplier_access_token_age_hours", "label": "supplier access-token age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access-token age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_quarantine_release_age_hours_01, assess_battery_storage_temp_c_02, assess_working_at_height_permit_pct_03, assess_generator_fuel_pct_04, assess_identity_sync_age_hours_05, assess_weighing_error_pct_06, assess_cycle_count_completion_pct_07, assess_pick_exception_rate_pct_08, assess_import_declaration_age_hours_09, assess_axle_load_variance_pct_10, assess_orders_per_labor_hour_11, assess_supplier_claim_response_hours_12, assess_supplier_part_substitution_count_13, assess_supplier_invoice_match_rate_pct_14, assess_supplier_escalation_age_hours_15, assess_supplier_sds_accuracy_pct_16, assess_supplier_cargo_security_score_17, assess_supplier_work_instruction_age_days_18, assess_supplier_conflict_mineral_pct_19, assess_supplier_sanctions_update_age_hours_20, assess_supplier_backup_power_pct_21, assess_supplier_model_monitoring_pct_22, assess_supplier_feature_flag_age_days_23, assess_supplier_access_token_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

