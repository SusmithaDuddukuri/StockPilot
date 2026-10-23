"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_export_control_review_age_hours_01(record):
    """Evaluate export-control review age for control WP-0219-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_control_review_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-01", "metric": "export_control_review_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-01", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-01", "metric": "export_control_review_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-01", "metric": "export_control_review_age_hours", "label": "export-control review age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "export-control review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_vehicle_registration_days_left_02(record):
    """Evaluate vehicle registration validity for control WP-0219-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-02", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-02", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-02", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-02", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle registration validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_project_milestone_delay_days_03(record):
    """Evaluate project milestone delay for control WP-0219-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-03", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-03", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-03", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-03", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "project milestone delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_capacity_review_age_days_04(record):
    """Evaluate supplier capacity review age for control WP-0219-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-04", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-04", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-04", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-04", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "supplier capacity review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_process_audit_age_days_05(record):
    """Evaluate supplier process audit age for control WP-0219-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-05", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-05", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-05", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-05", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tax_document_age_days_06(record):
    """Evaluate supplier tax document age for control WP-0219-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-06", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-06", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-06", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-06", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tax document age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_exit_plan_age_days_07(record):
    """Evaluate supplier exit-plan age for control WP-0219-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-07", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-07", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-07", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-07", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "supplier exit-plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_recycling_label_pct_08(record):
    """Evaluate supplier recycling-label compliance for control WP-0219-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-08", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-08", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-08", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-08", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "supplier recycling-label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_route_monitoring_pct_09(record):
    """Evaluate supplier route monitoring for control WP-0219-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-09", "metric": "supplier_route_monitoring_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-09", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-09", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-09", "metric": "supplier_route_monitoring_pct", "label": "supplier route monitoring",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier route monitoring must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_deviation_age_days_10(record):
    """Evaluate supplier deviation age for control WP-0219-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deviation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-10", "metric": "supplier_deviation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-10", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-10", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-10", "metric": "supplier_deviation_age_days", "label": "supplier deviation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier deviation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_hazmat_training_pct_11(record):
    """Evaluate supplier hazmat training for control WP-0219-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_hazmat_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-11", "metric": "supplier_hazmat_training_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-11", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-11", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-11", "metric": "supplier_hazmat_training_pct", "label": "supplier hazmat training",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "supplier hazmat training exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_payment_exception_age_days_12(record):
    """Evaluate supplier payment exception age for control WP-0219-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-12", "metric": "supplier_payment_exception_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-12", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-12", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-12", "metric": "supplier_payment_exception_age_days", "label": "supplier payment exception age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier payment exception age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_cross_training_pct_13(record):
    """Evaluate supplier cross-training for control WP-0219-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-13", "metric": "supplier_cross_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-13", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-13", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-13", "metric": "supplier_cross_training_pct", "label": "supplier cross-training",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cross-training must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_model_availability_pct_14(record):
    """Evaluate supplier model availability for control WP-0219-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-14", "metric": "supplier_model_availability_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-14", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-14", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-14", "metric": "supplier_model_availability_pct", "label": "supplier model availability",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_event_schema_age_days_15(record):
    """Evaluate supplier event-schema age for control WP-0219-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_schema_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-15", "metric": "supplier_event_schema_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-15", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-15", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-15", "metric": "supplier_event_schema_age_days", "label": "supplier event-schema age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier event-schema age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_admin_session_age_minutes_16(record):
    """Evaluate supplier admin session age for control WP-0219-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_admin_session_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-16", "metric": "supplier_admin_session_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-16", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-16", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-16", "metric": "supplier_admin_session_age_minutes", "label": "supplier admin session age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier admin session age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_confidentiality_breach_count_17(record):
    """Evaluate supplier confidentiality breaches for control WP-0219-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_confidentiality_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-17", "metric": "supplier_confidentiality_breach_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-17", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-17", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-17", "metric": "supplier_confidentiality_breach_count", "label": "supplier confidentiality breaches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier confidentiality breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_record_signoff_pct_18(record):
    """Evaluate supplier record signoff for control WP-0219-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-18", "metric": "supplier_record_signoff_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-18", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-18", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-18", "metric": "supplier_record_signoff_pct", "label": "supplier record signoff",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier record signoff must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_take_or_pay_exposure_19(record):
    """Evaluate take-or-pay exposure for control WP-0219-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_take_or_pay_exposure")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-19", "metric": "supplier_take_or_pay_exposure",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-19", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-19", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-19", "metric": "supplier_take_or_pay_exposure", "label": "take-or-pay exposure",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "take-or-pay exposure exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_pick_accuracy_pct_20(record):
    """Evaluate supplier pick accuracy for control WP-0219-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pick_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-20", "metric": "supplier_pick_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-20", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-20", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-20", "metric": "supplier_pick_accuracy_pct", "label": "supplier pick accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier pick accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_open_claim_transfer_pct_21(record):
    """Evaluate open-claim transfer completeness for control WP-0219-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_claim_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-21", "metric": "supplier_open_claim_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-21", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-21", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-21", "metric": "supplier_open_claim_transfer_pct", "label": "open-claim transfer completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-claim transfer completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_days_of_cover_22(record):
    """Evaluate stock cover for control WP-0219-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("days_of_cover")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-22", "metric": "days_of_cover",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-22", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-22", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-22", "metric": "days_of_cover", "label": "stock cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_sla_breach_count_23(record):
    """Evaluate SLA breaches for control WP-0219-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-23", "metric": "sla_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-23", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-23", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-23", "metric": "sla_breach_count", "label": "SLA breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "SLA breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_promo_lift_pct_24(record):
    """Evaluate promotion lift for control WP-0219-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("promo_lift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0219-24", "metric": "promo_lift_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0219-24", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0219-24", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0219-24", "metric": "promo_lift_pct", "label": "promotion lift",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "promotion lift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_export_control_review_age_hours_01, assess_vehicle_registration_days_left_02, assess_project_milestone_delay_days_03, assess_supplier_capacity_review_age_days_04, assess_supplier_process_audit_age_days_05, assess_supplier_tax_document_age_days_06, assess_supplier_exit_plan_age_days_07, assess_supplier_recycling_label_pct_08, assess_supplier_route_monitoring_pct_09, assess_supplier_deviation_age_days_10, assess_supplier_hazmat_training_pct_11, assess_supplier_payment_exception_age_days_12, assess_supplier_cross_training_pct_13, assess_supplier_model_availability_pct_14, assess_supplier_event_schema_age_days_15, assess_supplier_admin_session_age_minutes_16, assess_supplier_confidentiality_breach_count_17, assess_supplier_record_signoff_pct_18, assess_supplier_take_or_pay_exposure_19, assess_supplier_pick_accuracy_pct_20, assess_supplier_open_claim_transfer_pct_21, assess_days_of_cover_22, assess_sla_breach_count_23, assess_promo_lift_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

