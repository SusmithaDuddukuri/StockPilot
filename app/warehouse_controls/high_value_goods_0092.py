"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_import_declaration_age_hours_01(record):
    """Evaluate import declaration age for control WP-0092-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-01", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-01", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-01", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-01", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "import declaration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_axle_load_variance_pct_02(record):
    """Evaluate axle load variance for control WP-0092-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-02", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-02", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-02", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-02", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "axle load variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_orders_per_labor_hour_03(record):
    """Evaluate orders per labor hour for control WP-0092-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orders_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-03", "metric": "orders_per_labor_hour",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-03", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-03", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-03", "metric": "orders_per_labor_hour", "label": "orders per labor hour",
        "status": "breach", "severity": "high", "unit": "orders/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "orders per labor hour must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_claim_response_hours_04(record):
    """Evaluate supplier claim response time for control WP-0092-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-04", "metric": "supplier_claim_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-04", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-04", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-04", "metric": "supplier_claim_response_hours", "label": "supplier claim response time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "supplier claim response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_part_substitution_count_05(record):
    """Evaluate supplier part substitutions for control WP-0092-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_part_substitution_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-05", "metric": "supplier_part_substitution_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-05", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-05", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-05", "metric": "supplier_part_substitution_count", "label": "supplier part substitutions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "supplier part substitutions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_invoice_match_rate_pct_06(record):
    """Evaluate supplier invoice match for control WP-0092-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_match_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-06", "metric": "supplier_invoice_match_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-06", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-06", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-06", "metric": "supplier_invoice_match_rate_pct", "label": "supplier invoice match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_escalation_age_hours_07(record):
    """Evaluate supplier escalation age for control WP-0092-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-07", "metric": "supplier_escalation_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-07", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-07", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-07", "metric": "supplier_escalation_age_hours", "label": "supplier escalation age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier escalation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_sds_accuracy_pct_08(record):
    """Evaluate supplier SDS accuracy for control WP-0092-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-08", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-08", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-08", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-08", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier SDS accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_cargo_security_score_09(record):
    """Evaluate supplier cargo security for control WP-0092-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-09", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-09", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-09", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-09", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "supplier cargo security falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_work_instruction_age_days_10(record):
    """Evaluate supplier work-instruction age for control WP-0092-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_work_instruction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-10", "metric": "supplier_work_instruction_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-10", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-10", "metric": "supplier_work_instruction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-10", "metric": "supplier_work_instruction_age_days", "label": "supplier work-instruction age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier work-instruction age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_conflict_mineral_pct_11(record):
    """Evaluate supplier conflict-mineral reporting for control WP-0092-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_mineral_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-11", "metric": "supplier_conflict_mineral_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-11", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-11", "metric": "supplier_conflict_mineral_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-11", "metric": "supplier_conflict_mineral_pct", "label": "supplier conflict-mineral reporting",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier conflict-mineral reporting must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_sanctions_update_age_hours_12(record):
    """Evaluate supplier sanctions update age for control WP-0092-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sanctions_update_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-12", "metric": "supplier_sanctions_update_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-12", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-12", "metric": "supplier_sanctions_update_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-12", "metric": "supplier_sanctions_update_age_hours", "label": "supplier sanctions update age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier sanctions update age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_backup_power_pct_13(record):
    """Evaluate supplier backup power coverage for control WP-0092-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_power_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-13", "metric": "supplier_backup_power_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-13", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-13", "metric": "supplier_backup_power_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-13", "metric": "supplier_backup_power_pct", "label": "supplier backup power coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "supplier backup power coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_model_monitoring_pct_14(record):
    """Evaluate supplier model monitoring for control WP-0092-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-14", "metric": "supplier_model_monitoring_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-14", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-14", "metric": "supplier_model_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-14", "metric": "supplier_model_monitoring_pct", "label": "supplier model monitoring",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model monitoring must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_feature_flag_age_days_15(record):
    """Evaluate supplier feature flag age for control WP-0092-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feature_flag_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-15", "metric": "supplier_feature_flag_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-15", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-15", "metric": "supplier_feature_flag_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-15", "metric": "supplier_feature_flag_age_days", "label": "supplier feature flag age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier feature flag age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_access_token_age_hours_16(record):
    """Evaluate supplier access-token age for control WP-0092-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_token_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-16", "metric": "supplier_access_token_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-16", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-16", "metric": "supplier_access_token_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-16", "metric": "supplier_access_token_age_hours", "label": "supplier access-token age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier access-token age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_subject_access_age_days_17(record):
    """Evaluate supplier subject-access request age for control WP-0092-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_subject_access_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-17", "metric": "supplier_subject_access_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-17", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-17", "metric": "supplier_subject_access_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-17", "metric": "supplier_subject_access_age_days", "label": "supplier subject-access request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "supplier subject-access request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_control_exception_count_18(record):
    """Evaluate supplier control exceptions for control WP-0092-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-18", "metric": "supplier_control_exception_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-18", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-18", "metric": "supplier_control_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-18", "metric": "supplier_control_exception_count", "label": "supplier control exceptions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier control exceptions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_payment_term_variance_days_19(record):
    """Evaluate supplier payment-term variance for control WP-0092-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_term_variance_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-19", "metric": "supplier_payment_term_variance_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-19", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-19", "metric": "supplier_payment_term_variance_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-19", "metric": "supplier_payment_term_variance_days", "label": "supplier payment-term variance",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment-term variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_wip_age_days_20(record):
    """Evaluate supplier WIP age for control WP-0092-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_wip_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-20", "metric": "supplier_wip_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-20", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-20", "metric": "supplier_wip_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-20", "metric": "supplier_wip_age_days", "label": "supplier WIP age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier WIP age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_transition_plan_pct_21(record):
    """Evaluate supplier transition plan completeness for control WP-0092-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-21", "metric": "supplier_transition_plan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-21", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-21", "metric": "supplier_transition_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-21", "metric": "supplier_transition_plan_pct", "label": "supplier transition plan completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier transition plan completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_exit_evidence_pct_22(record):
    """Evaluate supplier exit evidence completeness for control WP-0092-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-22", "metric": "supplier_exit_evidence_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-22", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-22", "metric": "supplier_exit_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-22", "metric": "supplier_exit_evidence_pct", "label": "supplier exit evidence completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exit evidence completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_backlog_orders_23(record):
    """Evaluate order backlog for control WP-0092-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backlog_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-23", "metric": "backlog_orders",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-23", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-23", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-23", "metric": "backlog_orders", "label": "order backlog",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order backlog must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_equipment_downtime_hours_24(record):
    """Evaluate equipment downtime for control WP-0092-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_downtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0092-24", "metric": "equipment_downtime_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0092-24", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0092-24", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0092-24", "metric": "equipment_downtime_hours", "label": "equipment downtime",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "equipment downtime exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_import_declaration_age_hours_01, assess_axle_load_variance_pct_02, assess_orders_per_labor_hour_03, assess_supplier_claim_response_hours_04, assess_supplier_part_substitution_count_05, assess_supplier_invoice_match_rate_pct_06, assess_supplier_escalation_age_hours_07, assess_supplier_sds_accuracy_pct_08, assess_supplier_cargo_security_score_09, assess_supplier_work_instruction_age_days_10, assess_supplier_conflict_mineral_pct_11, assess_supplier_sanctions_update_age_hours_12, assess_supplier_backup_power_pct_13, assess_supplier_model_monitoring_pct_14, assess_supplier_feature_flag_age_days_15, assess_supplier_access_token_age_hours_16, assess_supplier_subject_access_age_days_17, assess_supplier_control_exception_count_18, assess_supplier_payment_term_variance_days_19, assess_supplier_wip_age_days_20, assess_supplier_transition_plan_pct_21, assess_supplier_exit_evidence_pct_22, assess_backlog_orders_23, assess_equipment_downtime_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

