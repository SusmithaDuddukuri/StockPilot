"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_overtime_hours_01(record):
    """Evaluate overtime hours for control WP-0255-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-01", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-01", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-01", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-01", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "overtime hours must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_break_compliance_pct_02(record):
    """Evaluate break compliance for control WP-0255-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-02", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-02", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-02", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-02", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "break compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_restore_test_age_days_03(record):
    """Evaluate restore test age for control WP-0255-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-03", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-03", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-03", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-03", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "restore test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_claim_age_days_04(record):
    """Evaluate claim age for control WP-0255-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-04", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-04", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-04", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-04", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "claim age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_trailer_seal_age_hours_05(record):
    """Evaluate trailer seal age for control WP-0255-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-05", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-05", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-05", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-05", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trailer seal age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_accessibility_score_06(record):
    """Evaluate accessibility score for control WP-0255-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-06", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-06", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-06", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-06", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "accessibility score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_conveyor_jam_count_07(record):
    """Evaluate conveyor jams for control WP-0255-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_jam_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-07", "metric": "conveyor_jam_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-07", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-07", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-07", "metric": "conveyor_jam_count", "label": "conveyor jams",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "conveyor jams exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_seal_audit_gap_count_08(record):
    """Evaluate seal audit gaps for control WP-0255-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-08", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-08", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-08", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-08", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "seal audit gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_cold_room_door_open_minutes_09(record):
    """Evaluate cold-room door open time for control WP-0255-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-09", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-09", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-09", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-09", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold-room door open time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_serial_activation_match_pct_10(record):
    """Evaluate serial activation match for control WP-0255-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-10", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-10", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-10", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-10", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "serial activation match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_site_induction_age_days_11(record):
    """Evaluate site induction age for control WP-0255-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-11", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-11", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-11", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-11", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "site induction age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_conveyor_utilization_pct_12(record):
    """Evaluate conveyor utilization for control WP-0255-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-12", "metric": "conveyor_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-12", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-12", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-12", "metric": "conveyor_utilization_pct", "label": "conveyor utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "conveyor utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_change_record_gap_count_13(record):
    """Evaluate change record gaps for control WP-0255-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-13", "metric": "change_record_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-13", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-13", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-13", "metric": "change_record_gap_count", "label": "change record gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "change record gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_report_access_review_age_days_14(record):
    """Evaluate report access review age for control WP-0255-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-14", "metric": "report_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-14", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-14", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-14", "metric": "report_access_review_age_days", "label": "report access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "report access review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_product_classification_gap_count_15(record):
    """Evaluate product classification gaps for control WP-0255-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_classification_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-15", "metric": "product_classification_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-15", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-15", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-15", "metric": "product_classification_gap_count", "label": "product classification gaps",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "product classification gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_appointment_no_show_count_16(record):
    """Evaluate dock appointment no-shows for control WP-0255-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("appointment_no_show_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-16", "metric": "appointment_no_show_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-16", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-16", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-16", "metric": "appointment_no_show_count", "label": "dock appointment no-shows",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "dock appointment no-shows falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_complaint_resolution_pct_17(record):
    """Evaluate complaint resolution for control WP-0255-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("complaint_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-17", "metric": "complaint_resolution_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-17", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-17", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-17", "metric": "complaint_resolution_pct", "label": "complaint resolution",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "complaint resolution must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_container_return_age_days_18(record):
    """Evaluate container return age for control WP-0255-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("container_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-18", "metric": "container_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-18", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-18", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-18", "metric": "container_return_age_days", "label": "container return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "container return age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_vehicle_maintenance_cost_19(record):
    """Evaluate vehicle maintenance cost for control WP-0255-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_maintenance_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-19", "metric": "vehicle_maintenance_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-19", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-19", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-19", "metric": "vehicle_maintenance_cost", "label": "vehicle maintenance cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "vehicle maintenance cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_esg_score_20(record):
    """Evaluate supplier ESG score for control WP-0255-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_esg_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-20", "metric": "supplier_esg_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-20", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-20", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-20", "metric": "supplier_esg_score", "label": "supplier ESG score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier ESG score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_training_pct_21(record):
    """Evaluate supplier training completion for control WP-0255-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-21", "metric": "supplier_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-21", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-21", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-21", "metric": "supplier_training_pct", "label": "supplier training completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_risk_review_age_days_22(record):
    """Evaluate supplier risk review age for control WP-0255-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-22", "metric": "supplier_risk_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-22", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-22", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-22", "metric": "supplier_risk_review_age_days", "label": "supplier risk review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_security_assessment_age_days_23(record):
    """Evaluate supplier security assessment age for control WP-0255-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-23", "metric": "supplier_security_assessment_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-23", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-23", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-23", "metric": "supplier_security_assessment_age_days", "label": "supplier security assessment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier security assessment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_tooling_spare_days_24(record):
    """Evaluate supplier tooling spare lead time for control WP-0255-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0255-24", "metric": "supplier_tooling_spare_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0255-24", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0255-24", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0255-24", "metric": "supplier_tooling_spare_days", "label": "supplier tooling spare lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier tooling spare lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_overtime_hours_01, assess_break_compliance_pct_02, assess_restore_test_age_days_03, assess_claim_age_days_04, assess_trailer_seal_age_hours_05, assess_accessibility_score_06, assess_conveyor_jam_count_07, assess_seal_audit_gap_count_08, assess_cold_room_door_open_minutes_09, assess_serial_activation_match_pct_10, assess_site_induction_age_days_11, assess_conveyor_utilization_pct_12, assess_change_record_gap_count_13, assess_report_access_review_age_days_14, assess_product_classification_gap_count_15, assess_appointment_no_show_count_16, assess_complaint_resolution_pct_17, assess_container_return_age_days_18, assess_vehicle_maintenance_cost_19, assess_supplier_esg_score_20, assess_supplier_training_pct_21, assess_supplier_risk_review_age_days_22, assess_supplier_security_assessment_age_days_23, assess_supplier_tooling_spare_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

