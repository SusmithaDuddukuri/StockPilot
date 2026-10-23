"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_seal_audit_gap_count_01(record):
    """Evaluate seal audit gaps for control WP-0646-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-01", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-01", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-01", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-01", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "seal audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_cold_room_door_open_minutes_02(record):
    """Evaluate cold-room door open time for control WP-0646-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-02", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-02", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-02", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-02", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "cold-room door open time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_serial_activation_match_pct_03(record):
    """Evaluate serial activation match for control WP-0646-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-03", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-03", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-03", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-03", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "serial activation match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_site_induction_age_days_04(record):
    """Evaluate site induction age for control WP-0646-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-04", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-04", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-04", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-04", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "site induction age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_conveyor_utilization_pct_05(record):
    """Evaluate conveyor utilization for control WP-0646-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-05", "metric": "conveyor_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-05", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-05", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-05", "metric": "conveyor_utilization_pct", "label": "conveyor utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "conveyor utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_change_record_gap_count_06(record):
    """Evaluate change record gaps for control WP-0646-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-06", "metric": "change_record_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-06", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-06", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-06", "metric": "change_record_gap_count", "label": "change record gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "change record gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_report_access_review_age_days_07(record):
    """Evaluate report access review age for control WP-0646-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-07", "metric": "report_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-07", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-07", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-07", "metric": "report_access_review_age_days", "label": "report access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "report access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_product_classification_gap_count_08(record):
    """Evaluate product classification gaps for control WP-0646-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_classification_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-08", "metric": "product_classification_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-08", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-08", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-08", "metric": "product_classification_gap_count", "label": "product classification gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product classification gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_appointment_no_show_count_09(record):
    """Evaluate dock appointment no-shows for control WP-0646-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("appointment_no_show_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-09", "metric": "appointment_no_show_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-09", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-09", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-09", "metric": "appointment_no_show_count", "label": "dock appointment no-shows",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock appointment no-shows must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_complaint_resolution_pct_10(record):
    """Evaluate complaint resolution for control WP-0646-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("complaint_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-10", "metric": "complaint_resolution_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-10", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-10", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-10", "metric": "complaint_resolution_pct", "label": "complaint resolution",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "complaint resolution exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_container_return_age_days_11(record):
    """Evaluate container return age for control WP-0646-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("container_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-11", "metric": "container_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-11", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-11", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-11", "metric": "container_return_age_days", "label": "container return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "container return age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_vehicle_maintenance_cost_12(record):
    """Evaluate vehicle maintenance cost for control WP-0646-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_maintenance_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-12", "metric": "vehicle_maintenance_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-12", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-12", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-12", "metric": "vehicle_maintenance_cost", "label": "vehicle maintenance cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle maintenance cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_esg_score_13(record):
    """Evaluate supplier ESG score for control WP-0646-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_esg_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-13", "metric": "supplier_esg_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-13", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-13", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-13", "metric": "supplier_esg_score", "label": "supplier ESG score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ESG score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_training_pct_14(record):
    """Evaluate supplier training completion for control WP-0646-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-14", "metric": "supplier_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-14", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-14", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-14", "metric": "supplier_training_pct", "label": "supplier training completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier training completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_risk_review_age_days_15(record):
    """Evaluate supplier risk review age for control WP-0646-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-15", "metric": "supplier_risk_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-15", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-15", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-15", "metric": "supplier_risk_review_age_days", "label": "supplier risk review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier risk review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_security_assessment_age_days_16(record):
    """Evaluate supplier security assessment age for control WP-0646-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-16", "metric": "supplier_security_assessment_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-16", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-16", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-16", "metric": "supplier_security_assessment_age_days", "label": "supplier security assessment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier security assessment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_tooling_spare_days_17(record):
    """Evaluate supplier tooling spare lead time for control WP-0646-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-17", "metric": "supplier_tooling_spare_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-17", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-17", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-17", "metric": "supplier_tooling_spare_days", "label": "supplier tooling spare lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tooling spare lead time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_scope3_data_pct_18(record):
    """Evaluate supplier Scope 3 data completeness for control WP-0646-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scope3_data_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-18", "metric": "supplier_scope3_data_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-18", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-18", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-18", "metric": "supplier_scope3_data_pct", "label": "supplier Scope 3 data completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier Scope 3 data completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_ack_latency_minutes_19(record):
    """Evaluate supplier acknowledgement latency for control WP-0646-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ack_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-19", "metric": "supplier_ack_latency_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-19", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-19", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-19", "metric": "supplier_ack_latency_minutes", "label": "supplier acknowledgement latency",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier acknowledgement latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_sorting_completion_pct_20(record):
    """Evaluate supplier sorting completion for control WP-0646-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sorting_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-20", "metric": "supplier_sorting_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-20", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-20", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-20", "metric": "supplier_sorting_completion_pct", "label": "supplier sorting completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sorting completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_worker_safety_training_pct_21(record):
    """Evaluate supplier worker safety training for control WP-0646-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_safety_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-21", "metric": "supplier_worker_safety_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-21", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-21", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-21", "metric": "supplier_worker_safety_training_pct", "label": "supplier worker safety training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier worker safety training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_customer_loss_pct_22(record):
    """Evaluate supplier customer loss for control WP-0646-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_loss_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-22", "metric": "supplier_customer_loss_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-22", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-22", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-22", "metric": "supplier_customer_loss_pct", "label": "supplier customer loss",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier customer loss exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_continuous_improvement_count_23(record):
    """Evaluate supplier continuous improvement actions for control WP-0646-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuous_improvement_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-23", "metric": "supplier_continuous_improvement_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-23", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-23", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-23", "metric": "supplier_continuous_improvement_count", "label": "supplier continuous improvement actions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier continuous improvement actions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_energy_per_inference_24(record):
    """Evaluate supplier energy per inference for control WP-0646-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0646-24", "metric": "supplier_energy_per_inference",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0646-24", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0646-24", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0646-24", "metric": "supplier_energy_per_inference", "label": "supplier energy per inference",
        "status": "breach", "severity": "medium", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy per inference must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_seal_audit_gap_count_01, assess_cold_room_door_open_minutes_02, assess_serial_activation_match_pct_03, assess_site_induction_age_days_04, assess_conveyor_utilization_pct_05, assess_change_record_gap_count_06, assess_report_access_review_age_days_07, assess_product_classification_gap_count_08, assess_appointment_no_show_count_09, assess_complaint_resolution_pct_10, assess_container_return_age_days_11, assess_vehicle_maintenance_cost_12, assess_supplier_esg_score_13, assess_supplier_training_pct_14, assess_supplier_risk_review_age_days_15, assess_supplier_security_assessment_age_days_16, assess_supplier_tooling_spare_days_17, assess_supplier_scope3_data_pct_18, assess_supplier_ack_latency_minutes_19, assess_supplier_sorting_completion_pct_20, assess_supplier_worker_safety_training_pct_21, assess_supplier_customer_loss_pct_22, assess_supplier_continuous_improvement_count_23, assess_supplier_energy_per_inference_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

