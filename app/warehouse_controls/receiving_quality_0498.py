"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_retention_exception_count_01(record):
    """Evaluate supplier retention exceptions for control WP-0498-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-01", "metric": "supplier_retention_exception_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-01", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-01", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-01", "metric": "supplier_retention_exception_count", "label": "supplier retention exceptions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier retention exceptions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_policy_exception_age_days_02(record):
    """Evaluate supplier policy exception age for control WP-0498-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-02", "metric": "supplier_policy_exception_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-02", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-02", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-02", "metric": "supplier_policy_exception_age_days", "label": "supplier policy exception age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier policy exception age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_late_payment_fee_cost_03(record):
    """Evaluate late-payment fee cost for control WP-0498-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_late_payment_fee_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-03", "metric": "supplier_late_payment_fee_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-03", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-03", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-03", "metric": "supplier_late_payment_fee_cost", "label": "late-payment fee cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "late-payment fee cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_raw_material_cover_days_04(record):
    """Evaluate supplier raw-material cover for control WP-0498-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-04", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-04", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-04", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-04", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier raw-material cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_cutover_readiness_pct_05(record):
    """Evaluate supplier cutover readiness for control WP-0498-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-05", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-05", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-05", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-05", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cutover readiness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_quantity_06(record):
    """Evaluate on-hand quantity for control WP-0498-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quantity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-06", "metric": "quantity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-06", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-06", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-06", "metric": "quantity", "label": "on-hand quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "on-hand quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_overtime_hours_07(record):
    """Evaluate overtime hours for control WP-0498-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-07", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-07", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-07", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-07", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "overtime hours falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_break_compliance_pct_08(record):
    """Evaluate break compliance for control WP-0498-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-08", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-08", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-08", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-08", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "break compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_restore_test_age_days_09(record):
    """Evaluate restore test age for control WP-0498-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-09", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-09", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-09", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-09", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restore test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_claim_age_days_10(record):
    """Evaluate claim age for control WP-0498-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-10", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-10", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-10", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-10", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "claim age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_trailer_seal_age_hours_11(record):
    """Evaluate trailer seal age for control WP-0498-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-11", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-11", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-11", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-11", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "trailer seal age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_accessibility_score_12(record):
    """Evaluate accessibility score for control WP-0498-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-12", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-12", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-12", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-12", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "accessibility score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_conveyor_jam_count_13(record):
    """Evaluate conveyor jams for control WP-0498-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_jam_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-13", "metric": "conveyor_jam_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-13", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-13", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-13", "metric": "conveyor_jam_count", "label": "conveyor jams",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "conveyor jams must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_seal_audit_gap_count_14(record):
    """Evaluate seal audit gaps for control WP-0498-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-14", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-14", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-14", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-14", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "seal audit gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_cold_room_door_open_minutes_15(record):
    """Evaluate cold-room door open time for control WP-0498-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-15", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-15", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-15", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-15", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "cold-room door open time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_serial_activation_match_pct_16(record):
    """Evaluate serial activation match for control WP-0498-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-16", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-16", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-16", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-16", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial activation match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_site_induction_age_days_17(record):
    """Evaluate site induction age for control WP-0498-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-17", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-17", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-17", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-17", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "site induction age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_conveyor_utilization_pct_18(record):
    """Evaluate conveyor utilization for control WP-0498-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-18", "metric": "conveyor_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-18", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-18", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-18", "metric": "conveyor_utilization_pct", "label": "conveyor utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "conveyor utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_change_record_gap_count_19(record):
    """Evaluate change record gaps for control WP-0498-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-19", "metric": "change_record_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-19", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-19", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-19", "metric": "change_record_gap_count", "label": "change record gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "change record gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_report_access_review_age_days_20(record):
    """Evaluate report access review age for control WP-0498-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-20", "metric": "report_access_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-20", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-20", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-20", "metric": "report_access_review_age_days", "label": "report access review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "report access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_product_classification_gap_count_21(record):
    """Evaluate product classification gaps for control WP-0498-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_classification_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-21", "metric": "product_classification_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-21", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-21", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-21", "metric": "product_classification_gap_count", "label": "product classification gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product classification gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_appointment_no_show_count_22(record):
    """Evaluate dock appointment no-shows for control WP-0498-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("appointment_no_show_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-22", "metric": "appointment_no_show_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-22", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-22", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-22", "metric": "appointment_no_show_count", "label": "dock appointment no-shows",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "dock appointment no-shows exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_complaint_resolution_pct_23(record):
    """Evaluate complaint resolution for control WP-0498-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("complaint_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-23", "metric": "complaint_resolution_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-23", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-23", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-23", "metric": "complaint_resolution_pct", "label": "complaint resolution",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "complaint resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_container_return_age_days_24(record):
    """Evaluate container return age for control WP-0498-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("container_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0498-24", "metric": "container_return_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0498-24", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0498-24", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0498-24", "metric": "container_return_age_days", "label": "container return age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "container return age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_supplier_retention_exception_count_01, assess_supplier_policy_exception_age_days_02, assess_supplier_late_payment_fee_cost_03, assess_supplier_raw_material_cover_days_04, assess_supplier_cutover_readiness_pct_05, assess_quantity_06, assess_overtime_hours_07, assess_break_compliance_pct_08, assess_restore_test_age_days_09, assess_claim_age_days_10, assess_trailer_seal_age_hours_11, assess_accessibility_score_12, assess_conveyor_jam_count_13, assess_seal_audit_gap_count_14, assess_cold_room_door_open_minutes_15, assess_serial_activation_match_pct_16, assess_site_induction_age_days_17, assess_conveyor_utilization_pct_18, assess_change_record_gap_count_19, assess_report_access_review_age_days_20, assess_product_classification_gap_count_21, assess_appointment_no_show_count_22, assess_complaint_resolution_pct_23, assess_container_return_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

