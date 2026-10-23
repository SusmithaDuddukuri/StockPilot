"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_capacity_review_age_days_01(record):
    """Evaluate supplier capacity review age for control WP-0287-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-01", "metric": "supplier_capacity_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-01", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-01", "metric": "supplier_capacity_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-01", "metric": "supplier_capacity_review_age_days", "label": "supplier capacity review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_process_audit_age_days_02(record):
    """Evaluate supplier process audit age for control WP-0287-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-02", "metric": "supplier_process_audit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-02", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-02", "metric": "supplier_process_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-02", "metric": "supplier_process_audit_age_days", "label": "supplier process audit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process audit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_tax_document_age_days_03(record):
    """Evaluate supplier tax document age for control WP-0287-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_document_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-03", "metric": "supplier_tax_document_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-03", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-03", "metric": "supplier_tax_document_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-03", "metric": "supplier_tax_document_age_days", "label": "supplier tax document age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier tax document age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_exit_plan_age_days_04(record):
    """Evaluate supplier exit-plan age for control WP-0287-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exit_plan_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-04", "metric": "supplier_exit_plan_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-04", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-04", "metric": "supplier_exit_plan_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-04", "metric": "supplier_exit_plan_age_days", "label": "supplier exit-plan age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "supplier exit-plan age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_recycling_label_pct_05(record):
    """Evaluate supplier recycling-label compliance for control WP-0287-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycling_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-05", "metric": "supplier_recycling_label_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-05", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-05", "metric": "supplier_recycling_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-05", "metric": "supplier_recycling_label_pct", "label": "supplier recycling-label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recycling-label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_route_monitoring_pct_06(record):
    """Evaluate supplier route monitoring for control WP-0287-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_route_monitoring_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-06", "metric": "supplier_route_monitoring_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-06", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-06", "metric": "supplier_route_monitoring_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-06", "metric": "supplier_route_monitoring_pct", "label": "supplier route monitoring",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier route monitoring must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_deviation_age_days_07(record):
    """Evaluate supplier deviation age for control WP-0287-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deviation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-07", "metric": "supplier_deviation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-07", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-07", "metric": "supplier_deviation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-07", "metric": "supplier_deviation_age_days", "label": "supplier deviation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier deviation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_hazmat_training_pct_08(record):
    """Evaluate supplier hazmat training for control WP-0287-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_hazmat_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-08", "metric": "supplier_hazmat_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-08", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-08", "metric": "supplier_hazmat_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-08", "metric": "supplier_hazmat_training_pct", "label": "supplier hazmat training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier hazmat training falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_payment_exception_age_days_09(record):
    """Evaluate supplier payment exception age for control WP-0287-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-09", "metric": "supplier_payment_exception_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-09", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-09", "metric": "supplier_payment_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-09", "metric": "supplier_payment_exception_age_days", "label": "supplier payment exception age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment exception age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_cross_training_pct_10(record):
    """Evaluate supplier cross-training for control WP-0287-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cross_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-10", "metric": "supplier_cross_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-10", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-10", "metric": "supplier_cross_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-10", "metric": "supplier_cross_training_pct", "label": "supplier cross-training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cross-training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_model_availability_pct_11(record):
    """Evaluate supplier model availability for control WP-0287-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-11", "metric": "supplier_model_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-11", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-11", "metric": "supplier_model_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-11", "metric": "supplier_model_availability_pct", "label": "supplier model availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier model availability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_event_schema_age_days_12(record):
    """Evaluate supplier event-schema age for control WP-0287-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_schema_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-12", "metric": "supplier_event_schema_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-12", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-12", "metric": "supplier_event_schema_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-12", "metric": "supplier_event_schema_age_days", "label": "supplier event-schema age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier event-schema age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_admin_session_age_minutes_13(record):
    """Evaluate supplier admin session age for control WP-0287-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_admin_session_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-13", "metric": "supplier_admin_session_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-13", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-13", "metric": "supplier_admin_session_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-13", "metric": "supplier_admin_session_age_minutes", "label": "supplier admin session age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier admin session age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_confidentiality_breach_count_14(record):
    """Evaluate supplier confidentiality breaches for control WP-0287-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_confidentiality_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-14", "metric": "supplier_confidentiality_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-14", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-14", "metric": "supplier_confidentiality_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-14", "metric": "supplier_confidentiality_breach_count", "label": "supplier confidentiality breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier confidentiality breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_record_signoff_pct_15(record):
    """Evaluate supplier record signoff for control WP-0287-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_signoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-15", "metric": "supplier_record_signoff_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-15", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-15", "metric": "supplier_record_signoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-15", "metric": "supplier_record_signoff_pct", "label": "supplier record signoff",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier record signoff exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_take_or_pay_exposure_16(record):
    """Evaluate take-or-pay exposure for control WP-0287-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_take_or_pay_exposure")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-16", "metric": "supplier_take_or_pay_exposure",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-16", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-16", "metric": "supplier_take_or_pay_exposure", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-16", "metric": "supplier_take_or_pay_exposure", "label": "take-or-pay exposure",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "take-or-pay exposure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_pick_accuracy_pct_17(record):
    """Evaluate supplier pick accuracy for control WP-0287-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pick_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-17", "metric": "supplier_pick_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-17", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-17", "metric": "supplier_pick_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-17", "metric": "supplier_pick_accuracy_pct", "label": "supplier pick accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier pick accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_open_claim_transfer_pct_18(record):
    """Evaluate open-claim transfer completeness for control WP-0287-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_claim_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-18", "metric": "supplier_open_claim_transfer_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-18", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-18", "metric": "supplier_open_claim_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-18", "metric": "supplier_open_claim_transfer_pct", "label": "open-claim transfer completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "open-claim transfer completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_days_of_cover_19(record):
    """Evaluate stock cover for control WP-0287-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("days_of_cover")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-19", "metric": "days_of_cover",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-19", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-19", "metric": "days_of_cover", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-19", "metric": "days_of_cover", "label": "stock cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "stock cover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_sla_breach_count_20(record):
    """Evaluate SLA breaches for control WP-0287-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-20", "metric": "sla_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-20", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-20", "metric": "sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-20", "metric": "sla_breach_count", "label": "SLA breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "SLA breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_promo_lift_pct_21(record):
    """Evaluate promotion lift for control WP-0287-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("promo_lift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-21", "metric": "promo_lift_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-21", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-21", "metric": "promo_lift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-21", "metric": "promo_lift_pct", "label": "promotion lift",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "promotion lift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_orphan_shipment_count_22(record):
    """Evaluate orphan shipments for control WP-0287-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_shipment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-22", "metric": "orphan_shipment_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-22", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-22", "metric": "orphan_shipment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-22", "metric": "orphan_shipment_count", "label": "orphan shipments",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "orphan shipments must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_waste_weight_kg_23(record):
    """Evaluate waste weight for control WP-0287-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("waste_weight_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-23", "metric": "waste_weight_kg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kg",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-23", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-23", "metric": "waste_weight_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-23", "metric": "waste_weight_kg", "label": "waste weight",
        "status": "breach", "severity": "medium", "unit": "kg",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "waste weight exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_lot_mismatch_count_24(record):
    """Evaluate lot mismatches for control WP-0287-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0287-24", "metric": "lot_mismatch_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0287-24", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0287-24", "metric": "lot_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0287-24", "metric": "lot_mismatch_count", "label": "lot mismatches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "lot mismatches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_capacity_review_age_days_01, assess_supplier_process_audit_age_days_02, assess_supplier_tax_document_age_days_03, assess_supplier_exit_plan_age_days_04, assess_supplier_recycling_label_pct_05, assess_supplier_route_monitoring_pct_06, assess_supplier_deviation_age_days_07, assess_supplier_hazmat_training_pct_08, assess_supplier_payment_exception_age_days_09, assess_supplier_cross_training_pct_10, assess_supplier_model_availability_pct_11, assess_supplier_event_schema_age_days_12, assess_supplier_admin_session_age_minutes_13, assess_supplier_confidentiality_breach_count_14, assess_supplier_record_signoff_pct_15, assess_supplier_take_or_pay_exposure_16, assess_supplier_pick_accuracy_pct_17, assess_supplier_open_claim_transfer_pct_18, assess_days_of_cover_19, assess_sla_breach_count_20, assess_promo_lift_pct_21, assess_orphan_shipment_count_22, assess_waste_weight_kg_23, assess_lot_mismatch_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

