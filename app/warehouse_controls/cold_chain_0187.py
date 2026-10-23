"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_raw_material_cover_days_01(record):
    """Evaluate supplier raw-material cover for control WP-0187-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-01", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-01", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-01", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-01", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier raw-material cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_cutover_readiness_pct_02(record):
    """Evaluate supplier cutover readiness for control WP-0187-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-02", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-02", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-02", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-02", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier cutover readiness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_quantity_03(record):
    """Evaluate on-hand quantity for control WP-0187-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quantity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-03", "metric": "quantity",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-03", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-03", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-03", "metric": "quantity", "label": "on-hand quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "on-hand quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_overtime_hours_04(record):
    """Evaluate overtime hours for control WP-0187-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-04", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-04", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-04", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-04", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "overtime hours falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_break_compliance_pct_05(record):
    """Evaluate break compliance for control WP-0187-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-05", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-05", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-05", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-05", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "break compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_restore_test_age_days_06(record):
    """Evaluate restore test age for control WP-0187-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-06", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-06", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-06", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-06", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restore test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_claim_age_days_07(record):
    """Evaluate claim age for control WP-0187-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-07", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-07", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-07", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-07", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "claim age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_trailer_seal_age_hours_08(record):
    """Evaluate trailer seal age for control WP-0187-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-08", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-08", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-08", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-08", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "trailer seal age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_accessibility_score_09(record):
    """Evaluate accessibility score for control WP-0187-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-09", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-09", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-09", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-09", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "accessibility score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_conveyor_jam_count_10(record):
    """Evaluate conveyor jams for control WP-0187-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_jam_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-10", "metric": "conveyor_jam_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-10", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-10", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-10", "metric": "conveyor_jam_count", "label": "conveyor jams",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "conveyor jams must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_seal_audit_gap_count_11(record):
    """Evaluate seal audit gaps for control WP-0187-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-11", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-11", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-11", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-11", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "seal audit gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_cold_room_door_open_minutes_12(record):
    """Evaluate cold-room door open time for control WP-0187-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-12", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-12", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-12", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-12", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "cold-room door open time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_serial_activation_match_pct_13(record):
    """Evaluate serial activation match for control WP-0187-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-13", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-13", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-13", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-13", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial activation match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_site_induction_age_days_14(record):
    """Evaluate site induction age for control WP-0187-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-14", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-14", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-14", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-14", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "site induction age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_conveyor_utilization_pct_15(record):
    """Evaluate conveyor utilization for control WP-0187-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-15", "metric": "conveyor_utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-15", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-15", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-15", "metric": "conveyor_utilization_pct", "label": "conveyor utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "conveyor utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_change_record_gap_count_16(record):
    """Evaluate change record gaps for control WP-0187-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-16", "metric": "change_record_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-16", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-16", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-16", "metric": "change_record_gap_count", "label": "change record gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "change record gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_report_access_review_age_days_17(record):
    """Evaluate report access review age for control WP-0187-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-17", "metric": "report_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-17", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-17", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-17", "metric": "report_access_review_age_days", "label": "report access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "report access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_product_classification_gap_count_18(record):
    """Evaluate product classification gaps for control WP-0187-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_classification_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-18", "metric": "product_classification_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-18", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-18", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-18", "metric": "product_classification_gap_count", "label": "product classification gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product classification gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_appointment_no_show_count_19(record):
    """Evaluate dock appointment no-shows for control WP-0187-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("appointment_no_show_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-19", "metric": "appointment_no_show_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-19", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-19", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-19", "metric": "appointment_no_show_count", "label": "dock appointment no-shows",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "dock appointment no-shows exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_complaint_resolution_pct_20(record):
    """Evaluate complaint resolution for control WP-0187-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("complaint_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-20", "metric": "complaint_resolution_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-20", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-20", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-20", "metric": "complaint_resolution_pct", "label": "complaint resolution",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "complaint resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_container_return_age_days_21(record):
    """Evaluate container return age for control WP-0187-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("container_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-21", "metric": "container_return_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-21", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-21", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-21", "metric": "container_return_age_days", "label": "container return age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "container return age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_vehicle_maintenance_cost_22(record):
    """Evaluate vehicle maintenance cost for control WP-0187-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_maintenance_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-22", "metric": "vehicle_maintenance_cost",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-22", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-22", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-22", "metric": "vehicle_maintenance_cost", "label": "vehicle maintenance cost",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle maintenance cost must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_esg_score_23(record):
    """Evaluate supplier ESG score for control WP-0187-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_esg_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-23", "metric": "supplier_esg_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-23", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-23", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-23", "metric": "supplier_esg_score", "label": "supplier ESG score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier ESG score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_training_pct_24(record):
    """Evaluate supplier training completion for control WP-0187-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0187-24", "metric": "supplier_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0187-24", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0187-24", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0187-24", "metric": "supplier_training_pct", "label": "supplier training completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier training completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_raw_material_cover_days_01, assess_supplier_cutover_readiness_pct_02, assess_quantity_03, assess_overtime_hours_04, assess_break_compliance_pct_05, assess_restore_test_age_days_06, assess_claim_age_days_07, assess_trailer_seal_age_hours_08, assess_accessibility_score_09, assess_conveyor_jam_count_10, assess_seal_audit_gap_count_11, assess_cold_room_door_open_minutes_12, assess_serial_activation_match_pct_13, assess_site_induction_age_days_14, assess_conveyor_utilization_pct_15, assess_change_record_gap_count_16, assess_report_access_review_age_days_17, assess_product_classification_gap_count_18, assess_appointment_no_show_count_19, assess_complaint_resolution_pct_20, assess_container_return_age_days_21, assess_vehicle_maintenance_cost_22, assess_supplier_esg_score_23, assess_supplier_training_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

