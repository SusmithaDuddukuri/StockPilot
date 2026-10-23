"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_sensor_calibration_age_days_01(record):
    """Evaluate sensor calibration age for control WP-0142-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-01", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-01", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-01", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-01", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sensor calibration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_repair_warranty_claim_pct_02(record):
    """Evaluate repair warranty claims for control WP-0142-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-02", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-02", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-02", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-02", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "repair warranty claims exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_trailer_restraint_test_age_days_03(record):
    """Evaluate trailer restraint test age for control WP-0142-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-03", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-03", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-03", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-03", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "trailer restraint test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_control_system_patch_age_days_04(record):
    """Evaluate control-system patch age for control WP-0142-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-04", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-04", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-04", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-04", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "control-system patch age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_certificate_expiry_days_05(record):
    """Evaluate certificate validity for control WP-0142-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-05", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-05", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-05", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-05", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "certificate validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_asset_tag_capture_pct_06(record):
    """Evaluate asset tag capture for control WP-0142-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-06", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-06", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-06", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-06", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "asset tag capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_transfer_duplicate_count_07(record):
    """Evaluate duplicate transfers for control WP-0142-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-07", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "transfers",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-07", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-07", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-07", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "low", "unit": "transfers",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "duplicate transfers falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_forward_pick_empty_count_08(record):
    """Evaluate empty forward-pick bins for control WP-0142-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-08", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "bins",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-08", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-08", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-08", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "medium", "unit": "bins",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "empty forward-pick bins must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_invoice_issue_age_days_09(record):
    """Evaluate invoice issue age for control WP-0142-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-09", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-09", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-09", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-09", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "invoice issue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_gate_checkin_minutes_10(record):
    """Evaluate gate check-in time for control WP-0142-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkin_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-10", "metric": "gate_checkin_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-10", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-10", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-10", "metric": "gate_checkin_minutes", "label": "gate check-in time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "gate check-in time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_overtime_cost_pct_11(record):
    """Evaluate overtime cost share for control WP-0142-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-11", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-11", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-11", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-11", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "overtime cost share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_over_ship_pct_12(record):
    """Evaluate supplier over-ship rate for control WP-0142-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-12", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-12", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-12", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-12", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier over-ship rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_invoice_timeliness_pct_13(record):
    """Evaluate supplier invoice timeliness for control WP-0142-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-13", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-13", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-13", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-13", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier invoice timeliness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_order_change_response_hours_14(record):
    """Evaluate supplier order-change response for control WP-0142-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-14", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-14", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-14", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-14", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier order-change response exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_sla_credit_age_days_15(record):
    """Evaluate supplier SLA-credit age for control WP-0142-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-15", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-15", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-15", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-15", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "supplier SLA-credit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_trace_query_minutes_16(record):
    """Evaluate supplier trace query time for control WP-0142-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-16", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-16", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-16", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-16", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier trace query time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_security_guard_coverage_pct_17(record):
    """Evaluate supplier guard coverage for control WP-0142-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-17", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-17", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-17", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-17", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier guard coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_mold_backup_pct_18(record):
    """Evaluate supplier mold backup coverage for control WP-0142-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-18", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-18", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-18", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-18", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "supplier mold backup coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_certificate_verification_age_days_19(record):
    """Evaluate supplier certificate verification age for control WP-0142-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_verification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-19", "metric": "supplier_certificate_verification_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-19", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-19", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-19", "metric": "supplier_certificate_verification_age_days", "label": "supplier certificate verification age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier certificate verification age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_conflict_disclosure_pct_20(record):
    """Evaluate supplier conflict disclosure for control WP-0142-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_disclosure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-20", "metric": "supplier_conflict_disclosure_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-20", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-20", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-20", "metric": "supplier_conflict_disclosure_pct", "label": "supplier conflict disclosure",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier conflict disclosure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_crisis_comms_test_age_days_21(record):
    """Evaluate supplier crisis communications test age for control WP-0142-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-21", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-21", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-21", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-21", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier crisis communications test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_digital_twin_coverage_pct_22(record):
    """Evaluate supplier digital-twin coverage for control WP-0142-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_digital_twin_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-22", "metric": "supplier_digital_twin_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-22", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-22", "metric": "supplier_digital_twin_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-22", "metric": "supplier_digital_twin_coverage_pct", "label": "supplier digital-twin coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier digital-twin coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_feedback_capture_pct_23(record):
    """Evaluate supplier feedback capture for control WP-0142-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_feedback_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-23", "metric": "supplier_feedback_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-23", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-23", "metric": "supplier_feedback_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-23", "metric": "supplier_feedback_capture_pct", "label": "supplier feedback capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier feedback capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_region_failover_minutes_24(record):
    """Evaluate supplier region failover time for control WP-0142-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_region_failover_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0142-24", "metric": "supplier_region_failover_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0142-24", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0142-24", "metric": "supplier_region_failover_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0142-24", "metric": "supplier_region_failover_minutes", "label": "supplier region failover time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier region failover time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

RULES = (assess_sensor_calibration_age_days_01, assess_repair_warranty_claim_pct_02, assess_trailer_restraint_test_age_days_03, assess_control_system_patch_age_days_04, assess_certificate_expiry_days_05, assess_asset_tag_capture_pct_06, assess_transfer_duplicate_count_07, assess_forward_pick_empty_count_08, assess_invoice_issue_age_days_09, assess_gate_checkin_minutes_10, assess_overtime_cost_pct_11, assess_supplier_over_ship_pct_12, assess_supplier_invoice_timeliness_pct_13, assess_supplier_order_change_response_hours_14, assess_supplier_sla_credit_age_days_15, assess_supplier_trace_query_minutes_16, assess_supplier_security_guard_coverage_pct_17, assess_supplier_mold_backup_pct_18, assess_supplier_certificate_verification_age_days_19, assess_supplier_conflict_disclosure_pct_20, assess_supplier_crisis_comms_test_age_days_21, assess_supplier_digital_twin_coverage_pct_22, assess_supplier_feedback_capture_pct_23, assess_supplier_region_failover_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

