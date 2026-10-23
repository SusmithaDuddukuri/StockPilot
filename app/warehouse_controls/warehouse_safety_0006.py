"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_budget_variance_pct_01(record):
    """Evaluate budget variance for control WP-0006-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-01", "metric": "budget_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-01", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-01", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-01", "metric": "budget_variance_pct", "label": "budget variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "budget variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_emissions_kg_per_order_02(record):
    """Evaluate emissions per order for control WP-0006-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emissions_kg_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-02", "metric": "emissions_kg_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-02", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-02", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-02", "metric": "emissions_kg_per_order", "label": "emissions per order",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "emissions per order exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_privacy_request_age_days_03(record):
    """Evaluate privacy request age for control WP-0006-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-03", "metric": "privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-03", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-03", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-03", "metric": "privacy_request_age_days", "label": "privacy request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "privacy request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_training_completion_pct_04(record):
    """Evaluate training completion for control WP-0006-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-04", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-04", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-04", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-04", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "training completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_ppe_compliance_pct_05(record):
    """Evaluate PPE compliance for control WP-0006-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-05", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-05", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-05", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-05", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "PPE compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_failed_delivery_rate_pct_06(record):
    """Evaluate failed delivery rate for control WP-0006-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-06", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-06", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-06", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-06", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "failed delivery rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_sensor_calibration_age_days_07(record):
    """Evaluate sensor calibration age for control WP-0006-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-07", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-07", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-07", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-07", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "sensor calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_repair_warranty_claim_pct_08(record):
    """Evaluate repair warranty claims for control WP-0006-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-08", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-08", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-08", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-08", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "repair warranty claims must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_trailer_restraint_test_age_days_09(record):
    """Evaluate trailer restraint test age for control WP-0006-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-09", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-09", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-09", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-09", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "trailer restraint test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_control_system_patch_age_days_10(record):
    """Evaluate control-system patch age for control WP-0006-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-10", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-10", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-10", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-10", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "control-system patch age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_certificate_expiry_days_11(record):
    """Evaluate certificate validity for control WP-0006-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-11", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-11", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-11", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-11", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "certificate validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_asset_tag_capture_pct_12(record):
    """Evaluate asset tag capture for control WP-0006-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-12", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-12", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-12", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-12", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "asset tag capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_transfer_duplicate_count_13(record):
    """Evaluate duplicate transfers for control WP-0006-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-13", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "transfers",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-13", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-13", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-13", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "high", "unit": "transfers",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "duplicate transfers must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_forward_pick_empty_count_14(record):
    """Evaluate empty forward-pick bins for control WP-0006-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-14", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "bins",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-14", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-14", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-14", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "critical", "unit": "bins",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "empty forward-pick bins exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_invoice_issue_age_days_15(record):
    """Evaluate invoice issue age for control WP-0006-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-15", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-15", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-15", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-15", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "invoice issue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_gate_checkin_minutes_16(record):
    """Evaluate gate check-in time for control WP-0006-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkin_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-16", "metric": "gate_checkin_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-16", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-16", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-16", "metric": "gate_checkin_minutes", "label": "gate check-in time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "gate check-in time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_overtime_cost_pct_17(record):
    """Evaluate overtime cost share for control WP-0006-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-17", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-17", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-17", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-17", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "overtime cost share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_over_ship_pct_18(record):
    """Evaluate supplier over-ship rate for control WP-0006-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-18", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-18", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-18", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-18", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier over-ship rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_invoice_timeliness_pct_19(record):
    """Evaluate supplier invoice timeliness for control WP-0006-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_timeliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-19", "metric": "supplier_invoice_timeliness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-19", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-19", "metric": "supplier_invoice_timeliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-19", "metric": "supplier_invoice_timeliness_pct", "label": "supplier invoice timeliness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier invoice timeliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_order_change_response_hours_20(record):
    """Evaluate supplier order-change response for control WP-0006-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_change_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-20", "metric": "supplier_order_change_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-20", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-20", "metric": "supplier_order_change_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-20", "metric": "supplier_order_change_response_hours", "label": "supplier order-change response",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier order-change response must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_supplier_sla_credit_age_days_21(record):
    """Evaluate supplier SLA-credit age for control WP-0006-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sla_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-21", "metric": "supplier_sla_credit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-21", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-21", "metric": "supplier_sla_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-21", "metric": "supplier_sla_credit_age_days", "label": "supplier SLA-credit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SLA-credit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_trace_query_minutes_22(record):
    """Evaluate supplier trace query time for control WP-0006-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_trace_query_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-22", "metric": "supplier_trace_query_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-22", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-22", "metric": "supplier_trace_query_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-22", "metric": "supplier_trace_query_minutes", "label": "supplier trace query time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier trace query time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_security_guard_coverage_pct_23(record):
    """Evaluate supplier guard coverage for control WP-0006-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_guard_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-23", "metric": "supplier_security_guard_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-23", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-23", "metric": "supplier_security_guard_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-23", "metric": "supplier_security_guard_coverage_pct", "label": "supplier guard coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier guard coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_mold_backup_pct_24(record):
    """Evaluate supplier mold backup coverage for control WP-0006-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_mold_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0006-24", "metric": "supplier_mold_backup_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0006-24", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0006-24", "metric": "supplier_mold_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0006-24", "metric": "supplier_mold_backup_pct", "label": "supplier mold backup coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier mold backup coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_budget_variance_pct_01, assess_emissions_kg_per_order_02, assess_privacy_request_age_days_03, assess_training_completion_pct_04, assess_ppe_compliance_pct_05, assess_failed_delivery_rate_pct_06, assess_sensor_calibration_age_days_07, assess_repair_warranty_claim_pct_08, assess_trailer_restraint_test_age_days_09, assess_control_system_patch_age_days_10, assess_certificate_expiry_days_11, assess_asset_tag_capture_pct_12, assess_transfer_duplicate_count_13, assess_forward_pick_empty_count_14, assess_invoice_issue_age_days_15, assess_gate_checkin_minutes_16, assess_overtime_cost_pct_17, assess_supplier_over_ship_pct_18, assess_supplier_invoice_timeliness_pct_19, assess_supplier_order_change_response_hours_20, assess_supplier_sla_credit_age_days_21, assess_supplier_trace_query_minutes_22, assess_supplier_security_guard_coverage_pct_23, assess_supplier_mold_backup_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

