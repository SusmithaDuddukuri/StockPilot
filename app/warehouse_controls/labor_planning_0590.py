"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_generator_fuel_pct_01(record):
    """Evaluate generator fuel for control WP-0590-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-01", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-01", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-01", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-01", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "generator fuel must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_identity_sync_age_hours_02(record):
    """Evaluate identity sync age for control WP-0590-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-02", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-02", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-02", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-02", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "identity sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_weighing_error_pct_03(record):
    """Evaluate weighing error for control WP-0590-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-03", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-03", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-03", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-03", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "weighing error falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_cycle_count_completion_pct_04(record):
    """Evaluate cycle-count completion for control WP-0590-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-04", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-04", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-04", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-04", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cycle-count completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_pick_exception_rate_pct_05(record):
    """Evaluate pick exception rate for control WP-0590-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_exception_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-05", "metric": "pick_exception_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-05", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-05", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-05", "metric": "pick_exception_rate_pct", "label": "pick exception rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick exception rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_import_declaration_age_hours_06(record):
    """Evaluate import declaration age for control WP-0590-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-06", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-06", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-06", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-06", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "import declaration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_axle_load_variance_pct_07(record):
    """Evaluate axle load variance for control WP-0590-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-07", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-07", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-07", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-07", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "axle load variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_orders_per_labor_hour_08(record):
    """Evaluate orders per labor hour for control WP-0590-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orders_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-08", "metric": "orders_per_labor_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-08", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-08", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-08", "metric": "orders_per_labor_hour", "label": "orders per labor hour",
        "status": "breach", "severity": "medium", "unit": "orders/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "orders per labor hour must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_claim_response_hours_09(record):
    """Evaluate supplier claim response time for control WP-0590-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-09", "metric": "supplier_claim_response_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-09", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-09", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-09", "metric": "supplier_claim_response_hours", "label": "supplier claim response time",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier claim response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_part_substitution_count_10(record):
    """Evaluate supplier part substitutions for control WP-0590-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_part_substitution_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-10", "metric": "supplier_part_substitution_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-10", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-10", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-10", "metric": "supplier_part_substitution_count", "label": "supplier part substitutions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "supplier part substitutions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_invoice_match_rate_pct_11(record):
    """Evaluate supplier invoice match for control WP-0590-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_match_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-11", "metric": "supplier_invoice_match_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-11", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-11", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-11", "metric": "supplier_invoice_match_rate_pct", "label": "supplier invoice match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "supplier invoice match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_escalation_age_hours_12(record):
    """Evaluate supplier escalation age for control WP-0590-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-12", "metric": "supplier_escalation_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-12", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-12", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-12", "metric": "supplier_escalation_age_hours", "label": "supplier escalation age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier escalation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_sds_accuracy_pct_13(record):
    """Evaluate supplier SDS accuracy for control WP-0590-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-13", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-13", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-13", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-13", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SDS accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_cargo_security_score_14(record):
    """Evaluate supplier cargo security for control WP-0590-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-14", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-14", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-14", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-14", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "supplier cargo security exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_work_instruction_age_days_15(record):
    """Evaluate supplier work-instruction age for control WP-0590-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_instruction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-15", "metric": "supplier_work_instruction_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-15", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-15", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-15", "metric": "supplier_work_instruction_age_days", "label": "supplier work-instruction age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier work-instruction age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_conflict_mineral_pct_16(record):
    """Evaluate supplier conflict-mineral reporting for control WP-0590-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_mineral_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-16", "metric": "supplier_conflict_mineral_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-16", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-16", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-16", "metric": "supplier_conflict_mineral_pct", "label": "supplier conflict-mineral reporting",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier conflict-mineral reporting must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_sanctions_update_age_hours_17(record):
    """Evaluate supplier sanctions update age for control WP-0590-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_update_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-17", "metric": "supplier_sanctions_update_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-17", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-17", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-17", "metric": "supplier_sanctions_update_age_hours", "label": "supplier sanctions update age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier sanctions update age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_backup_power_pct_18(record):
    """Evaluate supplier backup power coverage for control WP-0590-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_power_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-18", "metric": "supplier_backup_power_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-18", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-18", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-18", "metric": "supplier_backup_power_pct", "label": "supplier backup power coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "max",
        "finding": "supplier backup power coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_model_monitoring_pct_19(record):
    """Evaluate supplier model monitoring for control WP-0590-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-19", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-19", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-19", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-19", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "supplier model monitoring falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_feature_flag_age_days_20(record):
    """Evaluate supplier feature flag age for control WP-0590-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-20", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-20", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-20", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-20", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier feature flag age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_access_token_age_hours_21(record):
    """Evaluate supplier access-token age for control WP-0590-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_token_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-21", "metric": "supplier_access_token_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-21", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-21", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-21", "metric": "supplier_access_token_age_hours", "label": "supplier access-token age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access-token age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_subject_access_age_days_22(record):
    """Evaluate supplier subject-access request age for control WP-0590-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subject_access_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-22", "metric": "supplier_subject_access_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-22", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-22", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-22", "metric": "supplier_subject_access_age_days", "label": "supplier subject-access request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 55, "comparison": "max",
        "finding": "supplier subject-access request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_control_exception_count_23(record):
    """Evaluate supplier control exceptions for control WP-0590-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-23", "metric": "supplier_control_exception_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-23", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-23", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-23", "metric": "supplier_control_exception_count", "label": "supplier control exceptions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier control exceptions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_payment_term_variance_days_24(record):
    """Evaluate supplier payment-term variance for control WP-0590-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_term_variance_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0590-24", "metric": "supplier_payment_term_variance_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0590-24", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0590-24", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0590-24", "metric": "supplier_payment_term_variance_days", "label": "supplier payment-term variance",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment-term variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_generator_fuel_pct_01, assess_identity_sync_age_hours_02, assess_weighing_error_pct_03, assess_cycle_count_completion_pct_04, assess_pick_exception_rate_pct_05, assess_import_declaration_age_hours_06, assess_axle_load_variance_pct_07, assess_orders_per_labor_hour_08, assess_supplier_claim_response_hours_09, assess_supplier_part_substitution_count_10, assess_supplier_invoice_match_rate_pct_11, assess_supplier_escalation_age_hours_12, assess_supplier_sds_accuracy_pct_13, assess_supplier_cargo_security_score_14, assess_supplier_work_instruction_age_days_15, assess_supplier_conflict_mineral_pct_16, assess_supplier_sanctions_update_age_hours_17, assess_supplier_backup_power_pct_18, assess_supplier_model_monitoring_pct_19, assess_supplier_feature_flag_age_days_20, assess_supplier_access_token_age_hours_21, assess_supplier_subject_access_age_days_22, assess_supplier_control_exception_count_23, assess_supplier_payment_term_variance_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

