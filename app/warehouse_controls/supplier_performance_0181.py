"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_vulnerability_sla_breach_count_01(record):
    """Evaluate supplier vulnerability SLA breaches for control WP-0181-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_sla_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-01", "metric": "supplier_vulnerability_sla_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-01", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-01", "metric": "supplier_vulnerability_sla_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-01", "metric": "supplier_vulnerability_sla_breach_count", "label": "supplier vulnerability SLA breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier vulnerability SLA breaches exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_media_encryption_pct_02(record):
    """Evaluate supplier media encryption for control WP-0181-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_media_encryption_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-02", "metric": "supplier_media_encryption_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-02", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-02", "metric": "supplier_media_encryption_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-02", "metric": "supplier_media_encryption_pct", "label": "supplier media encryption",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier media encryption falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_conflict_check_pct_03(record):
    """Evaluate supplier conflict checks for control WP-0181-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_conflict_check_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-03", "metric": "supplier_conflict_check_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-03", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-03", "metric": "supplier_conflict_check_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-03", "metric": "supplier_conflict_check_pct", "label": "supplier conflict checks",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier conflict checks must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_order_freeze_violation_count_04(record):
    """Evaluate order-freeze violations for control WP-0181-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_freeze_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-04", "metric": "supplier_order_freeze_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-04", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-04", "metric": "supplier_order_freeze_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-04", "metric": "supplier_order_freeze_violation_count", "label": "order-freeze violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order-freeze violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_tracking_upload_pct_05(record):
    """Evaluate supplier tracking upload for control WP-0181-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tracking_upload_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-05", "metric": "supplier_tracking_upload_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-05", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-05", "metric": "supplier_tracking_upload_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-05", "metric": "supplier_tracking_upload_pct", "label": "supplier tracking upload",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier tracking upload exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_access_revocation_pct_06(record):
    """Evaluate supplier access revocation for control WP-0181-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_revocation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-06", "metric": "supplier_access_revocation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-06", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-06", "metric": "supplier_access_revocation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-06", "metric": "supplier_access_revocation_pct", "label": "supplier access revocation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "supplier access revocation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_occupied_units_07(record):
    """Evaluate occupied capacity for control WP-0181-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("occupied_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-07", "metric": "occupied_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-07", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-07", "metric": "occupied_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-07", "metric": "occupied_units", "label": "occupied capacity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "occupied capacity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_queue_depth_08(record):
    """Evaluate queue depth for control WP-0181-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_depth")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-08", "metric": "queue_depth",
            "status": "insufficient_data",
            "severity": "low", "unit": "jobs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-08", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-08", "metric": "queue_depth", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-08", "metric": "queue_depth", "label": "queue depth",
        "status": "breach", "severity": "low", "unit": "jobs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "queue depth must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_obsolete_stock_value_09(record):
    """Evaluate obsolete stock value for control WP-0181-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-09", "metric": "obsolete_stock_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-09", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-09", "metric": "obsolete_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-09", "metric": "obsolete_stock_value", "label": "obsolete stock value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "obsolete stock value exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_budget_variance_pct_10(record):
    """Evaluate budget variance for control WP-0181-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-10", "metric": "budget_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-10", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-10", "metric": "budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-10", "metric": "budget_variance_pct", "label": "budget variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "budget variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_emissions_kg_per_order_11(record):
    """Evaluate emissions per order for control WP-0181-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emissions_kg_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-11", "metric": "emissions_kg_per_order",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-11", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-11", "metric": "emissions_kg_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-11", "metric": "emissions_kg_per_order", "label": "emissions per order",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "emissions per order must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_privacy_request_age_days_12(record):
    """Evaluate privacy request age for control WP-0181-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-12", "metric": "privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-12", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-12", "metric": "privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-12", "metric": "privacy_request_age_days", "label": "privacy request age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "privacy request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_training_completion_pct_13(record):
    """Evaluate training completion for control WP-0181-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-13", "metric": "training_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-13", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-13", "metric": "training_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-13", "metric": "training_completion_pct", "label": "training completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "training completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_ppe_compliance_pct_14(record):
    """Evaluate PPE compliance for control WP-0181-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ppe_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-14", "metric": "ppe_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-14", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-14", "metric": "ppe_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-14", "metric": "ppe_compliance_pct", "label": "PPE compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "PPE compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_failed_delivery_rate_pct_15(record):
    """Evaluate failed delivery rate for control WP-0181-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("failed_delivery_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-15", "metric": "failed_delivery_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-15", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-15", "metric": "failed_delivery_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-15", "metric": "failed_delivery_rate_pct", "label": "failed delivery rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "failed delivery rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_sensor_calibration_age_days_16(record):
    """Evaluate sensor calibration age for control WP-0181-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-16", "metric": "sensor_calibration_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-16", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-16", "metric": "sensor_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-16", "metric": "sensor_calibration_age_days", "label": "sensor calibration age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sensor calibration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_repair_warranty_claim_pct_17(record):
    """Evaluate repair warranty claims for control WP-0181-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("repair_warranty_claim_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-17", "metric": "repair_warranty_claim_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-17", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-17", "metric": "repair_warranty_claim_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-17", "metric": "repair_warranty_claim_pct", "label": "repair warranty claims",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "repair warranty claims exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_trailer_restraint_test_age_days_18(record):
    """Evaluate trailer restraint test age for control WP-0181-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trailer_restraint_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-18", "metric": "trailer_restraint_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-18", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-18", "metric": "trailer_restraint_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-18", "metric": "trailer_restraint_test_age_days", "label": "trailer restraint test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "trailer restraint test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_control_system_patch_age_days_19(record):
    """Evaluate control-system patch age for control WP-0181-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_system_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-19", "metric": "control_system_patch_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-19", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-19", "metric": "control_system_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-19", "metric": "control_system_patch_age_days", "label": "control-system patch age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "control-system patch age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_certificate_expiry_days_20(record):
    """Evaluate certificate validity for control WP-0181-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("certificate_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-20", "metric": "certificate_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-20", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-20", "metric": "certificate_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-20", "metric": "certificate_expiry_days", "label": "certificate validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "certificate validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_asset_tag_capture_pct_21(record):
    """Evaluate asset tag capture for control WP-0181-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asset_tag_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-21", "metric": "asset_tag_capture_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-21", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-21", "metric": "asset_tag_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-21", "metric": "asset_tag_capture_pct", "label": "asset tag capture",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "asset tag capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_transfer_duplicate_count_22(record):
    """Evaluate duplicate transfers for control WP-0181-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("transfer_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-22", "metric": "transfer_duplicate_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "transfers",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-22", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-22", "metric": "transfer_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-22", "metric": "transfer_duplicate_count", "label": "duplicate transfers",
        "status": "breach", "severity": "high", "unit": "transfers",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "duplicate transfers falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_forward_pick_empty_count_23(record):
    """Evaluate empty forward-pick bins for control WP-0181-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forward_pick_empty_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-23", "metric": "forward_pick_empty_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "bins",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-23", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-23", "metric": "forward_pick_empty_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-23", "metric": "forward_pick_empty_count", "label": "empty forward-pick bins",
        "status": "breach", "severity": "critical", "unit": "bins",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "empty forward-pick bins must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_invoice_issue_age_days_24(record):
    """Evaluate invoice issue age for control WP-0181-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_issue_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0181-24", "metric": "invoice_issue_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0181-24", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0181-24", "metric": "invoice_issue_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0181-24", "metric": "invoice_issue_age_days", "label": "invoice issue age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "invoice issue age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_supplier_vulnerability_sla_breach_count_01, assess_supplier_media_encryption_pct_02, assess_supplier_conflict_check_pct_03, assess_supplier_order_freeze_violation_count_04, assess_supplier_tracking_upload_pct_05, assess_supplier_access_revocation_pct_06, assess_occupied_units_07, assess_queue_depth_08, assess_obsolete_stock_value_09, assess_budget_variance_pct_10, assess_emissions_kg_per_order_11, assess_privacy_request_age_days_12, assess_training_completion_pct_13, assess_ppe_compliance_pct_14, assess_failed_delivery_rate_pct_15, assess_sensor_calibration_age_days_16, assess_repair_warranty_claim_pct_17, assess_trailer_restraint_test_age_days_18, assess_control_system_patch_age_days_19, assess_certificate_expiry_days_20, assess_asset_tag_capture_pct_21, assess_transfer_duplicate_count_22, assess_forward_pick_empty_count_23, assess_invoice_issue_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

