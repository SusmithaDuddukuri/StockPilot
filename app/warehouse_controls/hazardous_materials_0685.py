"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_rollback_readiness_pct_01(record):
    """Evaluate supplier rollback readiness for control WP-0685-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rollback_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-01", "metric": "supplier_rollback_readiness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-01", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-01", "metric": "supplier_rollback_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-01", "metric": "supplier_rollback_readiness_pct", "label": "supplier rollback readiness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier rollback readiness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_identity_federation_pct_02(record):
    """Evaluate supplier identity federation for control WP-0685-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_identity_federation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-02", "metric": "supplier_identity_federation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-02", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-02", "metric": "supplier_identity_federation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-02", "metric": "supplier_identity_federation_pct", "label": "supplier identity federation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier identity federation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_retention_exception_count_03(record):
    """Evaluate supplier retention exceptions for control WP-0685-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_retention_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-03", "metric": "supplier_retention_exception_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-03", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-03", "metric": "supplier_retention_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-03", "metric": "supplier_retention_exception_count", "label": "supplier retention exceptions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier retention exceptions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_policy_exception_age_days_04(record):
    """Evaluate supplier policy exception age for control WP-0685-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_policy_exception_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-04", "metric": "supplier_policy_exception_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-04", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-04", "metric": "supplier_policy_exception_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-04", "metric": "supplier_policy_exception_age_days", "label": "supplier policy exception age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier policy exception age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_late_payment_fee_cost_05(record):
    """Evaluate late-payment fee cost for control WP-0685-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_late_payment_fee_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-05", "metric": "supplier_late_payment_fee_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-05", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-05", "metric": "supplier_late_payment_fee_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-05", "metric": "supplier_late_payment_fee_cost", "label": "late-payment fee cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "late-payment fee cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_raw_material_cover_days_06(record):
    """Evaluate supplier raw-material cover for control WP-0685-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_raw_material_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-06", "metric": "supplier_raw_material_cover_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-06", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-06", "metric": "supplier_raw_material_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-06", "metric": "supplier_raw_material_cover_days", "label": "supplier raw-material cover",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier raw-material cover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_cutover_readiness_pct_07(record):
    """Evaluate supplier cutover readiness for control WP-0685-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cutover_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-07", "metric": "supplier_cutover_readiness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-07", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-07", "metric": "supplier_cutover_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-07", "metric": "supplier_cutover_readiness_pct", "label": "supplier cutover readiness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cutover readiness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_quantity_08(record):
    """Evaluate on-hand quantity for control WP-0685-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quantity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-08", "metric": "quantity",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-08", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-08", "metric": "quantity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-08", "metric": "quantity", "label": "on-hand quantity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "on-hand quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_overtime_hours_09(record):
    """Evaluate overtime hours for control WP-0685-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-09", "metric": "overtime_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-09", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-09", "metric": "overtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-09", "metric": "overtime_hours", "label": "overtime hours",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "overtime hours exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_break_compliance_pct_10(record):
    """Evaluate break compliance for control WP-0685-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-10", "metric": "break_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-10", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-10", "metric": "break_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-10", "metric": "break_compliance_pct", "label": "break compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "break compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_restore_test_age_days_11(record):
    """Evaluate restore test age for control WP-0685-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-11", "metric": "restore_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-11", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-11", "metric": "restore_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-11", "metric": "restore_test_age_days", "label": "restore test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restore test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_claim_age_days_12(record):
    """Evaluate claim age for control WP-0685-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-12", "metric": "claim_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-12", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-12", "metric": "claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-12", "metric": "claim_age_days", "label": "claim age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "claim age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_trailer_seal_age_hours_13(record):
    """Evaluate trailer seal age for control WP-0685-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_seal_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-13", "metric": "trailer_seal_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-13", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-13", "metric": "trailer_seal_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-13", "metric": "trailer_seal_age_hours", "label": "trailer seal age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "trailer seal age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_accessibility_score_14(record):
    """Evaluate accessibility score for control WP-0685-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accessibility_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-14", "metric": "accessibility_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-14", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-14", "metric": "accessibility_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-14", "metric": "accessibility_score", "label": "accessibility score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "accessibility score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_conveyor_jam_count_15(record):
    """Evaluate conveyor jams for control WP-0685-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_jam_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-15", "metric": "conveyor_jam_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-15", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-15", "metric": "conveyor_jam_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-15", "metric": "conveyor_jam_count", "label": "conveyor jams",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "conveyor jams must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_seal_audit_gap_count_16(record):
    """Evaluate seal audit gaps for control WP-0685-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("seal_audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-16", "metric": "seal_audit_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-16", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-16", "metric": "seal_audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-16", "metric": "seal_audit_gap_count", "label": "seal audit gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "seal audit gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_cold_room_door_open_minutes_17(record):
    """Evaluate cold-room door open time for control WP-0685-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_room_door_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-17", "metric": "cold_room_door_open_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-17", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-17", "metric": "cold_room_door_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-17", "metric": "cold_room_door_open_minutes", "label": "cold-room door open time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "cold-room door open time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_serial_activation_match_pct_18(record):
    """Evaluate serial activation match for control WP-0685-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_activation_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-18", "metric": "serial_activation_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-18", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-18", "metric": "serial_activation_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-18", "metric": "serial_activation_match_pct", "label": "serial activation match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "serial activation match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_site_induction_age_days_19(record):
    """Evaluate site induction age for control WP-0685-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("site_induction_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-19", "metric": "site_induction_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-19", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-19", "metric": "site_induction_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-19", "metric": "site_induction_age_days", "label": "site induction age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "site induction age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_conveyor_utilization_pct_20(record):
    """Evaluate conveyor utilization for control WP-0685-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("conveyor_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-20", "metric": "conveyor_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-20", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-20", "metric": "conveyor_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-20", "metric": "conveyor_utilization_pct", "label": "conveyor utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "conveyor utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_change_record_gap_count_21(record):
    """Evaluate change record gaps for control WP-0685-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-21", "metric": "change_record_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-21", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-21", "metric": "change_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-21", "metric": "change_record_gap_count", "label": "change record gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "change record gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_report_access_review_age_days_22(record):
    """Evaluate report access review age for control WP-0685-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-22", "metric": "report_access_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-22", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-22", "metric": "report_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-22", "metric": "report_access_review_age_days", "label": "report access review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "report access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_product_classification_gap_count_23(record):
    """Evaluate product classification gaps for control WP-0685-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_classification_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-23", "metric": "product_classification_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-23", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-23", "metric": "product_classification_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-23", "metric": "product_classification_gap_count", "label": "product classification gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product classification gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_appointment_no_show_count_24(record):
    """Evaluate dock appointment no-shows for control WP-0685-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("appointment_no_show_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0685-24", "metric": "appointment_no_show_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0685-24", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0685-24", "metric": "appointment_no_show_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0685-24", "metric": "appointment_no_show_count", "label": "dock appointment no-shows",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock appointment no-shows must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_rollback_readiness_pct_01, assess_supplier_identity_federation_pct_02, assess_supplier_retention_exception_count_03, assess_supplier_policy_exception_age_days_04, assess_supplier_late_payment_fee_cost_05, assess_supplier_raw_material_cover_days_06, assess_supplier_cutover_readiness_pct_07, assess_quantity_08, assess_overtime_hours_09, assess_break_compliance_pct_10, assess_restore_test_age_days_11, assess_claim_age_days_12, assess_trailer_seal_age_hours_13, assess_accessibility_score_14, assess_conveyor_jam_count_15, assess_seal_audit_gap_count_16, assess_cold_room_door_open_minutes_17, assess_serial_activation_match_pct_18, assess_site_induction_age_days_19, assess_conveyor_utilization_pct_20, assess_change_record_gap_count_21, assess_report_access_review_age_days_22, assess_product_classification_gap_count_23, assess_appointment_no_show_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

