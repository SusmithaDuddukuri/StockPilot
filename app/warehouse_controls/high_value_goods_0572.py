"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_queue_depth_01(record):
    """Evaluate queue depth for control WP-0572-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-01", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "low", "unit": "jobs",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-01", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-01", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-01", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "low", "unit": "jobs",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "queue depth falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_obsolete_stock_value_02(record):
    """Evaluate obsolete stock value for control WP-0572-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-02", "metric": "obsolete_stock_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-02", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-02", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-02", "metric": "obsolete_stock_value", "label": "obsolete stock value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "obsolete stock value must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_budget_variance_pct_03(record):
    """Evaluate budget variance for control WP-0572-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-03", "metric": "budget_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-03", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-03", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-03", "metric": "budget_variance_pct", "label": "budget variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "budget variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_emissions_kg_per_order_04(record):
    """Evaluate emissions per order for control WP-0572-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emissions_kg_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-04", "metric": "emissions_kg_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-04", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-04", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-04", "metric": "emissions_kg_per_order", "label": "emissions per order",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "emissions per order exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_privacy_request_age_days_05(record):
    """Evaluate privacy request age for control WP-0572-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-05", "metric": "privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-05", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-05", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-05", "metric": "privacy_request_age_days", "label": "privacy request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "privacy request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_training_completion_pct_06(record):
    """Evaluate training completion for control WP-0572-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-06", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-06", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-06", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-06", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "training completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_ppe_compliance_pct_07(record):
    """Evaluate PPE compliance for control WP-0572-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-07", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-07", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-07", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-07", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "PPE compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_failed_delivery_rate_pct_08(record):
    """Evaluate failed delivery rate for control WP-0572-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-08", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-08", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-08", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-08", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "failed delivery rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_sensor_calibration_age_days_09(record):
    """Evaluate sensor calibration age for control WP-0572-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-09", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-09", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-09", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-09", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "sensor calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_repair_warranty_claim_pct_10(record):
    """Evaluate repair warranty claims for control WP-0572-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-10", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-10", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-10", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-10", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "repair warranty claims must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_trailer_restraint_test_age_days_11(record):
    """Evaluate trailer restraint test age for control WP-0572-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-11", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-11", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-11", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-11", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trailer restraint test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_control_system_patch_age_days_12(record):
    """Evaluate control-system patch age for control WP-0572-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-12", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-12", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-12", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-12", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "control-system patch age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_certificate_expiry_days_13(record):
    """Evaluate certificate validity for control WP-0572-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-13", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-13", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-13", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-13", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "certificate validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_asset_tag_capture_pct_14(record):
    """Evaluate asset tag capture for control WP-0572-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-14", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-14", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-14", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-14", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "asset tag capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_transfer_duplicate_count_15(record):
    """Evaluate duplicate transfers for control WP-0572-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-15", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "transfers",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-15", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-15", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-15", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "high", "unit": "transfers",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate transfers must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_forward_pick_empty_count_16(record):
    """Evaluate empty forward-pick bins for control WP-0572-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-16", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "bins",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-16", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-16", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-16", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "critical", "unit": "bins",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "empty forward-pick bins exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_invoice_issue_age_days_17(record):
    """Evaluate invoice issue age for control WP-0572-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-17", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-17", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-17", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-17", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "invoice issue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_gate_checkin_minutes_18(record):
    """Evaluate gate check-in time for control WP-0572-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkin_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-18", "metric": "gate_checkin_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-18", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-18", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-18", "metric": "gate_checkin_minutes", "label": "gate check-in time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "gate check-in time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_overtime_cost_pct_19(record):
    """Evaluate overtime cost share for control WP-0572-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-19", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-19", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-19", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-19", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "overtime cost share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_over_ship_pct_20(record):
    """Evaluate supplier over-ship rate for control WP-0572-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-20", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-20", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-20", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-20", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier over-ship rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_invoice_timeliness_pct_21(record):
    """Evaluate supplier invoice timeliness for control WP-0572-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-21", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-21", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-21", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-21", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier invoice timeliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_order_change_response_hours_22(record):
    """Evaluate supplier order-change response for control WP-0572-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-22", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-22", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-22", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-22", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier order-change response must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_sla_credit_age_days_23(record):
    """Evaluate supplier SLA-credit age for control WP-0572-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-23", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-23", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-23", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-23", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SLA-credit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_trace_query_minutes_24(record):
    """Evaluate supplier trace query time for control WP-0572-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0572-24", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0572-24", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0572-24", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0572-24", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier trace query time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_queue_depth_01, assess_obsolete_stock_value_02, assess_budget_variance_pct_03, assess_emissions_kg_per_order_04, assess_privacy_request_age_days_05, assess_training_completion_pct_06, assess_ppe_compliance_pct_07, assess_failed_delivery_rate_pct_08, assess_sensor_calibration_age_days_09, assess_repair_warranty_claim_pct_10, assess_trailer_restraint_test_age_days_11, assess_control_system_patch_age_days_12, assess_certificate_expiry_days_13, assess_asset_tag_capture_pct_14, assess_transfer_duplicate_count_15, assess_forward_pick_empty_count_16, assess_invoice_issue_age_days_17, assess_gate_checkin_minutes_18, assess_overtime_cost_pct_19, assess_supplier_over_ship_pct_20, assess_supplier_invoice_timeliness_pct_21, assess_supplier_order_change_response_hours_22, assess_supplier_sla_credit_age_days_23, assess_supplier_trace_query_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

