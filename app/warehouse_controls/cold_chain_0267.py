"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_customer_notification_pct_01(record):
    """Evaluate customer notification for control WP-0267-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-01", "metric": "customer_notification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-01", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-01", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-01", "metric": "customer_notification_pct", "label": "customer notification",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer notification must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_quarantine_release_age_hours_02(record):
    """Evaluate quarantine release age for control WP-0267-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quarantine_release_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-02", "metric": "quarantine_release_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-02", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-02", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-02", "metric": "quarantine_release_age_hours", "label": "quarantine release age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quarantine release age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_battery_storage_temp_c_03(record):
    """Evaluate battery storage temperature for control WP-0267-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_storage_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-03", "metric": "battery_storage_temp_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-03", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-03", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-03", "metric": "battery_storage_temp_c", "label": "battery storage temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "battery storage temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_working_at_height_permit_pct_04(record):
    """Evaluate working-at-height permit compliance for control WP-0267-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("working_at_height_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-04", "metric": "working_at_height_permit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-04", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-04", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-04", "metric": "working_at_height_permit_pct", "label": "working-at-height permit compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "working-at-height permit compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_generator_fuel_pct_05(record):
    """Evaluate generator fuel for control WP-0267-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-05", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-05", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-05", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-05", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "generator fuel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_identity_sync_age_hours_06(record):
    """Evaluate identity sync age for control WP-0267-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-06", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-06", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-06", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-06", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "identity sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_weighing_error_pct_07(record):
    """Evaluate weighing error for control WP-0267-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-07", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-07", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-07", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-07", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "weighing error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_cycle_count_completion_pct_08(record):
    """Evaluate cycle-count completion for control WP-0267-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-08", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-08", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-08", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-08", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "cycle-count completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_pick_exception_rate_pct_09(record):
    """Evaluate pick exception rate for control WP-0267-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_exception_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-09", "metric": "pick_exception_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-09", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-09", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-09", "metric": "pick_exception_rate_pct", "label": "pick exception rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pick exception rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_import_declaration_age_hours_10(record):
    """Evaluate import declaration age for control WP-0267-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-10", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-10", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-10", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-10", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "import declaration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_axle_load_variance_pct_11(record):
    """Evaluate axle load variance for control WP-0267-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-11", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-11", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-11", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-11", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "axle load variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_orders_per_labor_hour_12(record):
    """Evaluate orders per labor hour for control WP-0267-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orders_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-12", "metric": "orders_per_labor_hour",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders/hour",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-12", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-12", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-12", "metric": "orders_per_labor_hour", "label": "orders per labor hour",
        "status": "breach", "severity": "high", "unit": "orders/hour",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "orders per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_claim_response_hours_13(record):
    """Evaluate supplier claim response time for control WP-0267-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-13", "metric": "supplier_claim_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-13", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-13", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-13", "metric": "supplier_claim_response_hours", "label": "supplier claim response time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier claim response time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_part_substitution_count_14(record):
    """Evaluate supplier part substitutions for control WP-0267-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_part_substitution_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-14", "metric": "supplier_part_substitution_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-14", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-14", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-14", "metric": "supplier_part_substitution_count", "label": "supplier part substitutions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier part substitutions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_invoice_match_rate_pct_15(record):
    """Evaluate supplier invoice match for control WP-0267-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_match_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-15", "metric": "supplier_invoice_match_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-15", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-15", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-15", "metric": "supplier_invoice_match_rate_pct", "label": "supplier invoice match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier invoice match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_escalation_age_hours_16(record):
    """Evaluate supplier escalation age for control WP-0267-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-16", "metric": "supplier_escalation_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-16", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-16", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-16", "metric": "supplier_escalation_age_hours", "label": "supplier escalation age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier escalation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_sds_accuracy_pct_17(record):
    """Evaluate supplier SDS accuracy for control WP-0267-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-17", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-17", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-17", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-17", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier SDS accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_cargo_security_score_18(record):
    """Evaluate supplier cargo security for control WP-0267-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-18", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-18", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-18", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-18", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cargo security must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_work_instruction_age_days_19(record):
    """Evaluate supplier work-instruction age for control WP-0267-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_instruction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-19", "metric": "supplier_work_instruction_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-19", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-19", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-19", "metric": "supplier_work_instruction_age_days", "label": "supplier work-instruction age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier work-instruction age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_conflict_mineral_pct_20(record):
    """Evaluate supplier conflict-mineral reporting for control WP-0267-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_mineral_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-20", "metric": "supplier_conflict_mineral_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-20", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-20", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-20", "metric": "supplier_conflict_mineral_pct", "label": "supplier conflict-mineral reporting",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier conflict-mineral reporting falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_sanctions_update_age_hours_21(record):
    """Evaluate supplier sanctions update age for control WP-0267-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_update_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-21", "metric": "supplier_sanctions_update_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-21", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-21", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-21", "metric": "supplier_sanctions_update_age_hours", "label": "supplier sanctions update age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sanctions update age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_backup_power_pct_22(record):
    """Evaluate supplier backup power coverage for control WP-0267-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_power_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-22", "metric": "supplier_backup_power_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-22", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-22", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-22", "metric": "supplier_backup_power_pct", "label": "supplier backup power coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier backup power coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_model_monitoring_pct_23(record):
    """Evaluate supplier model monitoring for control WP-0267-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-23", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-23", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-23", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-23", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier model monitoring exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_feature_flag_age_days_24(record):
    """Evaluate supplier feature flag age for control WP-0267-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0267-24", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0267-24", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0267-24", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0267-24", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier feature flag age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_customer_notification_pct_01, assess_quarantine_release_age_hours_02, assess_battery_storage_temp_c_03, assess_working_at_height_permit_pct_04, assess_generator_fuel_pct_05, assess_identity_sync_age_hours_06, assess_weighing_error_pct_07, assess_cycle_count_completion_pct_08, assess_pick_exception_rate_pct_09, assess_import_declaration_age_hours_10, assess_axle_load_variance_pct_11, assess_orders_per_labor_hour_12, assess_supplier_claim_response_hours_13, assess_supplier_part_substitution_count_14, assess_supplier_invoice_match_rate_pct_15, assess_supplier_escalation_age_hours_16, assess_supplier_sds_accuracy_pct_17, assess_supplier_cargo_security_score_18, assess_supplier_work_instruction_age_days_19, assess_supplier_conflict_mineral_pct_20, assess_supplier_sanctions_update_age_hours_21, assess_supplier_backup_power_pct_22, assess_supplier_model_monitoring_pct_23, assess_supplier_feature_flag_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

