"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_vehicle_registration_days_left_01(record):
    """Evaluate vehicle registration validity for control WP-0474-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_registration_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-01", "metric": "vehicle_registration_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-01", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-01", "metric": "vehicle_registration_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-01", "metric": "vehicle_registration_days_left", "label": "vehicle registration validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle registration validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_project_milestone_delay_days_02(record):
    """Evaluate project milestone delay for control WP-0474-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("project_milestone_delay_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-02", "metric": "project_milestone_delay_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-02", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-02", "metric": "project_milestone_delay_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-02", "metric": "project_milestone_delay_days", "label": "project milestone delay",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "project milestone delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_capacity_review_age_days_03(record):
    """Evaluate supplier capacity review age for control WP-0474-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-03", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-03", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-03", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-03", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier capacity review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_process_audit_age_days_04(record):
    """Evaluate supplier process audit age for control WP-0474-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-04", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-04", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-04", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-04", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process audit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_tax_document_age_days_05(record):
    """Evaluate supplier tax document age for control WP-0474-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-05", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-05", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-05", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-05", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tax document age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_exit_plan_age_days_06(record):
    """Evaluate supplier exit-plan age for control WP-0474-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-06", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-06", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-06", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-06", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier exit-plan age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_recycling_label_pct_07(record):
    """Evaluate supplier recycling-label compliance for control WP-0474-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-07", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-07", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-07", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-07", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "supplier recycling-label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_route_monitoring_pct_08(record):
    """Evaluate supplier route monitoring for control WP-0474-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-08", "metric": "supplier_route_monitoring_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-08", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-08", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-08", "metric": "supplier_route_monitoring_pct", "label": "supplier route monitoring",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier route monitoring must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_deviation_age_days_09(record):
    """Evaluate supplier deviation age for control WP-0474-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deviation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-09", "metric": "supplier_deviation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-09", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-09", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-09", "metric": "supplier_deviation_age_days", "label": "supplier deviation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier deviation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_hazmat_training_pct_10(record):
    """Evaluate supplier hazmat training for control WP-0474-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_hazmat_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-10", "metric": "supplier_hazmat_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-10", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-10", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-10", "metric": "supplier_hazmat_training_pct", "label": "supplier hazmat training",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier hazmat training exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_payment_exception_age_days_11(record):
    """Evaluate supplier payment exception age for control WP-0474-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-11", "metric": "supplier_payment_exception_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-11", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-11", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-11", "metric": "supplier_payment_exception_age_days", "label": "supplier payment exception age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier payment exception age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_cross_training_pct_12(record):
    """Evaluate supplier cross-training for control WP-0474-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-12", "metric": "supplier_cross_training_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-12", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-12", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-12", "metric": "supplier_cross_training_pct", "label": "supplier cross-training",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cross-training must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_model_availability_pct_13(record):
    """Evaluate supplier model availability for control WP-0474-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-13", "metric": "supplier_model_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-13", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-13", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-13", "metric": "supplier_model_availability_pct", "label": "supplier model availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model availability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_event_schema_age_days_14(record):
    """Evaluate supplier event-schema age for control WP-0474-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_schema_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-14", "metric": "supplier_event_schema_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-14", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-14", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-14", "metric": "supplier_event_schema_age_days", "label": "supplier event-schema age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier event-schema age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_admin_session_age_minutes_15(record):
    """Evaluate supplier admin session age for control WP-0474-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_admin_session_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-15", "metric": "supplier_admin_session_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-15", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-15", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-15", "metric": "supplier_admin_session_age_minutes", "label": "supplier admin session age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier admin session age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_confidentiality_breach_count_16(record):
    """Evaluate supplier confidentiality breaches for control WP-0474-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_confidentiality_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-16", "metric": "supplier_confidentiality_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-16", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-16", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-16", "metric": "supplier_confidentiality_breach_count", "label": "supplier confidentiality breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier confidentiality breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_record_signoff_pct_17(record):
    """Evaluate supplier record signoff for control WP-0474-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-17", "metric": "supplier_record_signoff_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-17", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-17", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-17", "metric": "supplier_record_signoff_pct", "label": "supplier record signoff",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier record signoff must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_take_or_pay_exposure_18(record):
    """Evaluate take-or-pay exposure for control WP-0474-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_take_or_pay_exposure")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-18", "metric": "supplier_take_or_pay_exposure",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-18", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-18", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-18", "metric": "supplier_take_or_pay_exposure", "label": "take-or-pay exposure",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "take-or-pay exposure exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_pick_accuracy_pct_19(record):
    """Evaluate supplier pick accuracy for control WP-0474-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pick_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-19", "metric": "supplier_pick_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-19", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-19", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-19", "metric": "supplier_pick_accuracy_pct", "label": "supplier pick accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier pick accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_open_claim_transfer_pct_20(record):
    """Evaluate open-claim transfer completeness for control WP-0474-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_claim_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-20", "metric": "supplier_open_claim_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-20", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-20", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-20", "metric": "supplier_open_claim_transfer_pct", "label": "open-claim transfer completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "open-claim transfer completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_days_of_cover_21(record):
    """Evaluate stock cover for control WP-0474-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("days_of_cover")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-21", "metric": "days_of_cover",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-21", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-21", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-21", "metric": "days_of_cover", "label": "stock cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_sla_breach_count_22(record):
    """Evaluate SLA breaches for control WP-0474-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-22", "metric": "sla_breach_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-22", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-22", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-22", "metric": "sla_breach_count", "label": "SLA breaches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "SLA breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_promo_lift_pct_23(record):
    """Evaluate promotion lift for control WP-0474-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("promo_lift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-23", "metric": "promo_lift_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-23", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-23", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-23", "metric": "promo_lift_pct", "label": "promotion lift",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "promotion lift falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_orphan_shipment_count_24(record):
    """Evaluate orphan shipments for control WP-0474-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_shipment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0474-24", "metric": "orphan_shipment_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0474-24", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0474-24", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0474-24", "metric": "orphan_shipment_count", "label": "orphan shipments",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "orphan shipments must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_vehicle_registration_days_left_01, assess_project_milestone_delay_days_02, assess_supplier_capacity_review_age_days_03, assess_supplier_process_audit_age_days_04, assess_supplier_tax_document_age_days_05, assess_supplier_exit_plan_age_days_06, assess_supplier_recycling_label_pct_07, assess_supplier_route_monitoring_pct_08, assess_supplier_deviation_age_days_09, assess_supplier_hazmat_training_pct_10, assess_supplier_payment_exception_age_days_11, assess_supplier_cross_training_pct_12, assess_supplier_model_availability_pct_13, assess_supplier_event_schema_age_days_14, assess_supplier_admin_session_age_minutes_15, assess_supplier_confidentiality_breach_count_16, assess_supplier_record_signoff_pct_17, assess_supplier_take_or_pay_exposure_18, assess_supplier_pick_accuracy_pct_19, assess_supplier_open_claim_transfer_pct_20, assess_days_of_cover_21, assess_sla_breach_count_22, assess_promo_lift_pct_23, assess_orphan_shipment_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

