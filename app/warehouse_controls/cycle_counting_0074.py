"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_training_completion_pct_01(record):
    """Evaluate training completion for control WP-0074-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-01", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-01", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-01", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-01", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "training completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_ppe_compliance_pct_02(record):
    """Evaluate PPE compliance for control WP-0074-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-02", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-02", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-02", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-02", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "PPE compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_failed_delivery_rate_pct_03(record):
    """Evaluate failed delivery rate for control WP-0074-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-03", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-03", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-03", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-03", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "failed delivery rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_sensor_calibration_age_days_04(record):
    """Evaluate sensor calibration age for control WP-0074-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-04", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-04", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-04", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-04", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sensor calibration age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_repair_warranty_claim_pct_05(record):
    """Evaluate repair warranty claims for control WP-0074-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-05", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-05", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-05", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-05", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "repair warranty claims must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_trailer_restraint_test_age_days_06(record):
    """Evaluate trailer restraint test age for control WP-0074-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-06", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-06", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-06", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-06", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "trailer restraint test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_control_system_patch_age_days_07(record):
    """Evaluate control-system patch age for control WP-0074-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-07", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-07", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-07", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-07", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "control-system patch age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_certificate_expiry_days_08(record):
    """Evaluate certificate validity for control WP-0074-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-08", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-08", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-08", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-08", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "certificate validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_asset_tag_capture_pct_09(record):
    """Evaluate asset tag capture for control WP-0074-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-09", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-09", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-09", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-09", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "asset tag capture must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_transfer_duplicate_count_10(record):
    """Evaluate duplicate transfers for control WP-0074-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-10", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "transfers",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-10", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-10", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-10", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "critical", "unit": "transfers",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "duplicate transfers exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_forward_pick_empty_count_11(record):
    """Evaluate empty forward-pick bins for control WP-0074-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-11", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "bins",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-11", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-11", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-11", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "low", "unit": "bins",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "empty forward-pick bins falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_invoice_issue_age_days_12(record):
    """Evaluate invoice issue age for control WP-0074-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-12", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-12", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-12", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-12", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice issue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_gate_checkin_minutes_13(record):
    """Evaluate gate check-in time for control WP-0074-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkin_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-13", "metric": "gate_checkin_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-13", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-13", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-13", "metric": "gate_checkin_minutes", "label": "gate check-in time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "gate check-in time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_overtime_cost_pct_14(record):
    """Evaluate overtime cost share for control WP-0074-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-14", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-14", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-14", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-14", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "overtime cost share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_over_ship_pct_15(record):
    """Evaluate supplier over-ship rate for control WP-0074-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-15", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-15", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-15", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-15", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier over-ship rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_invoice_timeliness_pct_16(record):
    """Evaluate supplier invoice timeliness for control WP-0074-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-16", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-16", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-16", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-16", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice timeliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_order_change_response_hours_17(record):
    """Evaluate supplier order-change response for control WP-0074-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-17", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-17", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-17", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-17", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier order-change response must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_sla_credit_age_days_18(record):
    """Evaluate supplier SLA-credit age for control WP-0074-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-18", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-18", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-18", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-18", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier SLA-credit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_trace_query_minutes_19(record):
    """Evaluate supplier trace query time for control WP-0074-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-19", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-19", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-19", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-19", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "supplier trace query time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_security_guard_coverage_pct_20(record):
    """Evaluate supplier guard coverage for control WP-0074-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-20", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-20", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-20", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-20", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier guard coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_mold_backup_pct_21(record):
    """Evaluate supplier mold backup coverage for control WP-0074-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-21", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-21", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-21", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-21", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier mold backup coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_certificate_verification_age_days_22(record):
    """Evaluate supplier certificate verification age for control WP-0074-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certificate_verification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-22", "metric": "supplier_certificate_verification_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-22", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-22", "metric": "supplier_certificate_verification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-22", "metric": "supplier_certificate_verification_age_days", "label": "supplier certificate verification age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier certificate verification age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_conflict_disclosure_pct_23(record):
    """Evaluate supplier conflict disclosure for control WP-0074-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_disclosure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-23", "metric": "supplier_conflict_disclosure_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-23", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-23", "metric": "supplier_conflict_disclosure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-23", "metric": "supplier_conflict_disclosure_pct", "label": "supplier conflict disclosure",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "supplier conflict disclosure falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_crisis_comms_test_age_days_24(record):
    """Evaluate supplier crisis communications test age for control WP-0074-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_crisis_comms_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0074-24", "metric": "supplier_crisis_comms_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0074-24", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0074-24", "metric": "supplier_crisis_comms_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0074-24", "metric": "supplier_crisis_comms_test_age_days", "label": "supplier crisis communications test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier crisis communications test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_training_completion_pct_01, assess_ppe_compliance_pct_02, assess_failed_delivery_rate_pct_03, assess_sensor_calibration_age_days_04, assess_repair_warranty_claim_pct_05, assess_trailer_restraint_test_age_days_06, assess_control_system_patch_age_days_07, assess_certificate_expiry_days_08, assess_asset_tag_capture_pct_09, assess_transfer_duplicate_count_10, assess_forward_pick_empty_count_11, assess_invoice_issue_age_days_12, assess_gate_checkin_minutes_13, assess_overtime_cost_pct_14, assess_supplier_over_ship_pct_15, assess_supplier_invoice_timeliness_pct_16, assess_supplier_order_change_response_hours_17, assess_supplier_sla_credit_age_days_18, assess_supplier_trace_query_minutes_19, assess_supplier_security_guard_coverage_pct_20, assess_supplier_mold_backup_pct_21, assess_supplier_certificate_verification_age_days_22, assess_supplier_conflict_disclosure_pct_23, assess_supplier_crisis_comms_test_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

