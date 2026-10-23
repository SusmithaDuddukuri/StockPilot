"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_order_freeze_violation_count_01(record):
    """Evaluate order-freeze violations for control WP-0249-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_freeze_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-01", "metric": "supplier_order_freeze_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-01", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-01", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-01", "metric": "supplier_order_freeze_violation_count", "label": "order-freeze violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "order-freeze violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_tracking_upload_pct_02(record):
    """Evaluate supplier tracking upload for control WP-0249-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tracking_upload_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-02", "metric": "supplier_tracking_upload_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-02", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-02", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-02", "metric": "supplier_tracking_upload_pct", "label": "supplier tracking upload",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "supplier tracking upload falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_access_revocation_pct_03(record):
    """Evaluate supplier access revocation for control WP-0249-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-03", "metric": "supplier_access_revocation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-03", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-03", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-03", "metric": "supplier_access_revocation_pct", "label": "supplier access revocation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access revocation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_occupied_units_04(record):
    """Evaluate occupied capacity for control WP-0249-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("occupied_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-04", "metric": "occupied_units",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-04", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-04", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-04", "metric": "occupied_units", "label": "occupied capacity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "occupied capacity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_queue_depth_05(record):
    """Evaluate queue depth for control WP-0249-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-05", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "medium", "unit": "jobs",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-05", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-05", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-05", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "medium", "unit": "jobs",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "queue depth exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_obsolete_stock_value_06(record):
    """Evaluate obsolete stock value for control WP-0249-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-06", "metric": "obsolete_stock_value",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-06", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-06", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-06", "metric": "obsolete_stock_value", "label": "obsolete stock value",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "obsolete stock value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_budget_variance_pct_07(record):
    """Evaluate budget variance for control WP-0249-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-07", "metric": "budget_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-07", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-07", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-07", "metric": "budget_variance_pct", "label": "budget variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "budget variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_emissions_kg_per_order_08(record):
    """Evaluate emissions per order for control WP-0249-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emissions_kg_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-08", "metric": "emissions_kg_per_order",
            "status": "insufficient_data",
            "severity": "low", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-08", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-08", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-08", "metric": "emissions_kg_per_order", "label": "emissions per order",
        "status": "breach", "severity": "low", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "emissions per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_privacy_request_age_days_09(record):
    """Evaluate privacy request age for control WP-0249-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-09", "metric": "privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-09", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-09", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-09", "metric": "privacy_request_age_days", "label": "privacy request age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "privacy request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_training_completion_pct_10(record):
    """Evaluate training completion for control WP-0249-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-10", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-10", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-10", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-10", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "training completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_ppe_compliance_pct_11(record):
    """Evaluate PPE compliance for control WP-0249-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-11", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-11", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-11", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-11", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "PPE compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_failed_delivery_rate_pct_12(record):
    """Evaluate failed delivery rate for control WP-0249-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-12", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-12", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-12", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-12", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "failed delivery rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_sensor_calibration_age_days_13(record):
    """Evaluate sensor calibration age for control WP-0249-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-13", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-13", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-13", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-13", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "sensor calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_repair_warranty_claim_pct_14(record):
    """Evaluate repair warranty claims for control WP-0249-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-14", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-14", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-14", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-14", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "repair warranty claims falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_trailer_restraint_test_age_days_15(record):
    """Evaluate trailer restraint test age for control WP-0249-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-15", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-15", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-15", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-15", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "trailer restraint test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_control_system_patch_age_days_16(record):
    """Evaluate control-system patch age for control WP-0249-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-16", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-16", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-16", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-16", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "control-system patch age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_certificate_expiry_days_17(record):
    """Evaluate certificate validity for control WP-0249-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-17", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-17", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-17", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-17", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "certificate validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_asset_tag_capture_pct_18(record):
    """Evaluate asset tag capture for control WP-0249-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-18", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-18", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-18", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-18", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "asset tag capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_transfer_duplicate_count_19(record):
    """Evaluate duplicate transfers for control WP-0249-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-19", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "transfers",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-19", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-19", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-19", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "critical", "unit": "transfers",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "duplicate transfers must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_forward_pick_empty_count_20(record):
    """Evaluate empty forward-pick bins for control WP-0249-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-20", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "bins",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-20", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-20", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-20", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "low", "unit": "bins",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "empty forward-pick bins must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_invoice_issue_age_days_21(record):
    """Evaluate invoice issue age for control WP-0249-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-21", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-21", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-21", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-21", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "invoice issue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_gate_checkin_minutes_22(record):
    """Evaluate gate check-in time for control WP-0249-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkin_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-22", "metric": "gate_checkin_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-22", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-22", "metric": "gate_checkin_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-22", "metric": "gate_checkin_minutes", "label": "gate check-in time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "gate check-in time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_overtime_cost_pct_23(record):
    """Evaluate overtime cost share for control WP-0249-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("overtime_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-23", "metric": "overtime_cost_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-23", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-23", "metric": "overtime_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-23", "metric": "overtime_cost_pct", "label": "overtime cost share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "overtime cost share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_over_ship_pct_24(record):
    """Evaluate supplier over-ship rate for control WP-0249-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_over_ship_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0249-24", "metric": "supplier_over_ship_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0249-24", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0249-24", "metric": "supplier_over_ship_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0249-24", "metric": "supplier_over_ship_pct", "label": "supplier over-ship rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier over-ship rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_supplier_order_freeze_violation_count_01, assess_supplier_tracking_upload_pct_02, assess_supplier_access_revocation_pct_03, assess_occupied_units_04, assess_queue_depth_05, assess_obsolete_stock_value_06, assess_budget_variance_pct_07, assess_emissions_kg_per_order_08, assess_privacy_request_age_days_09, assess_training_completion_pct_10, assess_ppe_compliance_pct_11, assess_failed_delivery_rate_pct_12, assess_sensor_calibration_age_days_13, assess_repair_warranty_claim_pct_14, assess_trailer_restraint_test_age_days_15, assess_control_system_patch_age_days_16, assess_certificate_expiry_days_17, assess_asset_tag_capture_pct_18, assess_transfer_duplicate_count_19, assess_forward_pick_empty_count_20, assess_invoice_issue_age_days_21, assess_gate_checkin_minutes_22, assess_overtime_cost_pct_23, assess_supplier_over_ship_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

