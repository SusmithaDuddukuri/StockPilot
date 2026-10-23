"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_inspection_queue_age_hours_01(record):
    """Evaluate inspection queue age for control WP-0457-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_queue_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-01", "metric": "inspection_queue_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-01", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-01", "metric": "inspection_queue_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-01", "metric": "inspection_queue_age_hours", "label": "inspection queue age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "inspection queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_inspection_sample_pct_02(record):
    """Evaluate inspection sample rate for control WP-0457-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_sample_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-02", "metric": "inspection_sample_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-02", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-02", "metric": "inspection_sample_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-02", "metric": "inspection_sample_pct", "label": "inspection sample rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "inspection sample rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_battery_cycle_count_03(record):
    """Evaluate battery cycle count for control WP-0457-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_cycle_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-03", "metric": "battery_cycle_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "cycles",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-03", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-03", "metric": "battery_cycle_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-03", "metric": "battery_cycle_count", "label": "battery cycle count",
        "status": "breach", "severity": "critical", "unit": "cycles",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery cycle count must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_incident_report_age_hours_04(record):
    """Evaluate incident report age for control WP-0457-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_report_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-04", "metric": "incident_report_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-04", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-04", "metric": "incident_report_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-04", "metric": "incident_report_age_hours", "label": "incident report age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident report age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_power_quality_score_05(record):
    """Evaluate power quality for control WP-0457-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("power_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-05", "metric": "power_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-05", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-05", "metric": "power_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-05", "metric": "power_quality_score", "label": "power quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "power quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_least_privilege_score_06(record):
    """Evaluate least privilege score for control WP-0457-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("least_privilege_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-06", "metric": "least_privilege_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-06", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-06", "metric": "least_privilege_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-06", "metric": "least_privilege_score", "label": "least privilege score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "least privilege score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_scale_zero_drift_07(record):
    """Evaluate scale zero drift for control WP-0457-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scale_zero_drift")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-07", "metric": "scale_zero_drift",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-07", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-07", "metric": "scale_zero_drift", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-07", "metric": "scale_zero_drift", "label": "scale zero drift",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scale zero drift must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_variance_approval_age_hours_08(record):
    """Evaluate variance approval age for control WP-0457-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("variance_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-08", "metric": "variance_approval_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-08", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-08", "metric": "variance_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-08", "metric": "variance_approval_age_hours", "label": "variance approval age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "variance approval age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_pick_substitution_pct_09(record):
    """Evaluate pick substitution rate for control WP-0457-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_substitution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-09", "metric": "pick_substitution_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-09", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-09", "metric": "pick_substitution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-09", "metric": "pick_substitution_pct", "label": "pick substitution rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "pick substitution rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_customs_exam_age_hours_10(record):
    """Evaluate customs exam age for control WP-0457-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_exam_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-10", "metric": "customs_exam_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-10", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-10", "metric": "customs_exam_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-10", "metric": "customs_exam_age_hours", "label": "customs exam age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "customs exam age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_fleet_utilization_pct_11(record):
    """Evaluate fleet utilization for control WP-0457-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fleet_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-11", "metric": "fleet_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-11", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-11", "metric": "fleet_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-11", "metric": "fleet_utilization_pct", "label": "fleet utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fleet utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_travel_time_pct_12(record):
    """Evaluate travel time share for control WP-0457-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("travel_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-12", "metric": "travel_time_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-12", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-12", "metric": "travel_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-12", "metric": "travel_time_pct", "label": "travel time share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "travel time share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_audit_score_13(record):
    """Evaluate supplier audit score for control WP-0457-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-13", "metric": "supplier_audit_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-13", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-13", "metric": "supplier_audit_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-13", "metric": "supplier_audit_score", "label": "supplier audit score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier audit score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_ppm_defects_14(record):
    """Evaluate supplier PPM defects for control WP-0457-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppm_defects")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-14", "metric": "supplier_ppm_defects",
            "status": "insufficient_data",
            "severity": "high", "unit": "ppm",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-14", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-14", "metric": "supplier_ppm_defects", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-14", "metric": "supplier_ppm_defects", "label": "supplier PPM defects",
        "status": "breach", "severity": "high", "unit": "ppm",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "supplier PPM defects falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_credit_note_age_days_15(record):
    """Evaluate supplier credit-note age for control WP-0457-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-15", "metric": "supplier_credit_note_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-15", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-15", "metric": "supplier_credit_note_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-15", "metric": "supplier_credit_note_age_days", "label": "supplier credit-note age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier credit-note age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_release_notice_days_16(record):
    """Evaluate supplier release notice for control WP-0457-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_release_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-16", "metric": "supplier_release_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-16", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-16", "metric": "supplier_release_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-16", "metric": "supplier_release_notice_days", "label": "supplier release notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier release notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_dimension_spec_match_pct_17(record):
    """Evaluate supplier dimension specification match for control WP-0457-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dimension_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-17", "metric": "supplier_dimension_spec_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-17", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-17", "metric": "supplier_dimension_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-17", "metric": "supplier_dimension_spec_match_pct", "label": "supplier dimension specification match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier dimension specification match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_seal_control_pct_18(record):
    """Evaluate supplier seal control for control WP-0457-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_seal_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-18", "metric": "supplier_seal_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-18", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-18", "metric": "supplier_seal_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-18", "metric": "supplier_seal_control_pct", "label": "supplier seal control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "supplier seal control falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_material_change_notice_days_19(record):
    """Evaluate supplier material-change notice for control WP-0457-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-19", "metric": "supplier_material_change_notice_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-19", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-19", "metric": "supplier_material_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-19", "metric": "supplier_material_change_notice_days", "label": "supplier material-change notice",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier material-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_reach_compliance_pct_20(record):
    """Evaluate supplier REACH compliance for control WP-0457-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_reach_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-20", "metric": "supplier_reach_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-20", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-20", "metric": "supplier_reach_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-20", "metric": "supplier_reach_compliance_pct", "label": "supplier REACH compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier REACH compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_country_of_risk_score_21(record):
    """Evaluate supplier country-of-risk score for control WP-0457-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_of_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-21", "metric": "supplier_country_of_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-21", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-21", "metric": "supplier_country_of_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-21", "metric": "supplier_country_of_risk_score", "label": "supplier country-of-risk score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier country-of-risk score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_fuel_storage_hours_22(record):
    """Evaluate supplier fuel storage for control WP-0457-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fuel_storage_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-22", "metric": "supplier_fuel_storage_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-22", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-22", "metric": "supplier_fuel_storage_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-22", "metric": "supplier_fuel_storage_hours", "label": "supplier fuel storage",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "supplier fuel storage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_data_access_review_age_days_23(record):
    """Evaluate supplier data-access review age for control WP-0457-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-23", "metric": "supplier_data_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-23", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-23", "metric": "supplier_data_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-23", "metric": "supplier_data_access_review_age_days", "label": "supplier data-access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_rollback_readiness_pct_24(record):
    """Evaluate supplier rollback readiness for control WP-0457-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rollback_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0457-24", "metric": "supplier_rollback_readiness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0457-24", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0457-24", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0457-24", "metric": "supplier_rollback_readiness_pct", "label": "supplier rollback readiness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier rollback readiness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_inspection_queue_age_hours_01, assess_inspection_sample_pct_02, assess_battery_cycle_count_03, assess_incident_report_age_hours_04, assess_power_quality_score_05, assess_least_privilege_score_06, assess_scale_zero_drift_07, assess_variance_approval_age_hours_08, assess_pick_substitution_pct_09, assess_customs_exam_age_hours_10, assess_fleet_utilization_pct_11, assess_travel_time_pct_12, assess_supplier_audit_score_13, assess_supplier_ppm_defects_14, assess_supplier_credit_note_age_days_15, assess_supplier_release_notice_days_16, assess_supplier_dimension_spec_match_pct_17, assess_supplier_seal_control_pct_18, assess_supplier_material_change_notice_days_19, assess_supplier_reach_compliance_pct_20, assess_supplier_country_of_risk_score_21, assess_supplier_fuel_storage_hours_22, assess_supplier_data_access_review_age_days_23, assess_supplier_rollback_readiness_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

