"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_asset_return_age_days_01(record):
    """Evaluate supplier asset return age for control WP-0372-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-01", "metric": "supplier_asset_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-01", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-01", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-01", "metric": "supplier_asset_return_age_days", "label": "supplier asset return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier asset return age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_approval_limit_breach_count_02(record):
    """Evaluate supplier approval-limit breaches for control WP-0372-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_approval_limit_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-02", "metric": "supplier_approval_limit_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-02", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-02", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-02", "metric": "supplier_approval_limit_breach_count", "label": "supplier approval-limit breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier approval-limit breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_frozen_horizon_change_count_03(record):
    """Evaluate frozen-horizon changes for control WP-0372-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_frozen_horizon_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-03", "metric": "supplier_frozen_horizon_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-03", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-03", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-03", "metric": "supplier_frozen_horizon_change_count", "label": "frozen-horizon changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "frozen-horizon changes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_delivery_confirmation_pct_04(record):
    """Evaluate supplier delivery confirmation for control WP-0372-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_confirmation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-04", "metric": "supplier_delivery_confirmation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-04", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-04", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-04", "metric": "supplier_delivery_confirmation_pct", "label": "supplier delivery confirmation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier delivery confirmation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_data_wipe_verification_pct_05(record):
    """Evaluate supplier data-wipe verification for control WP-0372-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_wipe_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-05", "metric": "supplier_data_wipe_verification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-05", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-05", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-05", "metric": "supplier_data_wipe_verification_pct", "label": "supplier data-wipe verification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier data-wipe verification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_utilization_pct_06(record):
    """Evaluate capacity utilization for control WP-0372-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-06", "metric": "utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-06", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-06", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-06", "metric": "utilization_pct", "label": "capacity utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "capacity utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_replenishment_age_hours_07(record):
    """Evaluate replenishment age for control WP-0372-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-07", "metric": "replenishment_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-07", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-07", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-07", "metric": "replenishment_age_hours", "label": "replenishment age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replenishment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_slow_mover_pct_08(record):
    """Evaluate slow-moving inventory for control WP-0372-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-08", "metric": "slow_mover_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-08", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-08", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-08", "metric": "slow_mover_pct", "label": "slow-moving inventory",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "slow-moving inventory exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_purchase_price_variance_pct_09(record):
    """Evaluate purchase price variance for control WP-0372-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_price_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-09", "metric": "purchase_price_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-09", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-09", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-09", "metric": "purchase_price_variance_pct", "label": "purchase price variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "purchase price variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_vehicle_idle_minutes_10(record):
    """Evaluate vehicle idle time for control WP-0372-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_idle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-10", "metric": "vehicle_idle_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-10", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-10", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-10", "metric": "vehicle_idle_minutes", "label": "vehicle idle time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle idle time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_access_violation_count_11(record):
    """Evaluate access violations for control WP-0372-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-11", "metric": "access_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-11", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-11", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-11", "metric": "access_violation_count", "label": "access violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "access violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_shift_coverage_pct_12(record):
    """Evaluate shift coverage for control WP-0372-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-12", "metric": "shift_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-12", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-12", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-12", "metric": "shift_coverage_pct", "label": "shift coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "shift coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_fire_drill_age_days_13(record):
    """Evaluate fire drill age for control WP-0372-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-13", "metric": "fire_drill_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-13", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-13", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-13", "metric": "fire_drill_age_days", "label": "fire drill age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "fire drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_proof_photo_pct_14(record):
    """Evaluate proof photo completion for control WP-0372-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-14", "metric": "proof_photo_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-14", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-14", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-14", "metric": "proof_photo_pct", "label": "proof photo completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "proof photo completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_data_logger_download_age_hours_15(record):
    """Evaluate data logger download age for control WP-0372-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_logger_download_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-15", "metric": "data_logger_download_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-15", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-15", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-15", "metric": "data_logger_download_age_hours", "label": "data logger download age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data logger download age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_customer_replacement_age_hours_16(record):
    """Evaluate replacement age for control WP-0372-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_replacement_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-16", "metric": "customer_replacement_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-16", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-16", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-16", "metric": "customer_replacement_age_hours", "label": "replacement age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "replacement age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_dock_edge_protection_pct_17(record):
    """Evaluate dock edge protection for control WP-0372-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-17", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-17", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-17", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-17", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "dock edge protection falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_industrial_network_segmentation_pct_18(record):
    """Evaluate industrial network segmentation for control WP-0372-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-18", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-18", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-18", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-18", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "industrial network segmentation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_domain_expiry_days_19(record):
    """Evaluate domain validity for control WP-0372-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-19", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-19", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-19", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-19", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "domain validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_equipment_assignment_gap_count_20(record):
    """Evaluate equipment assignment gaps for control WP-0372-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-20", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-20", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-20", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-20", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "equipment assignment gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_movement_duplicate_count_21(record):
    """Evaluate duplicate movements for control WP-0372-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("movement_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-21", "metric": "movement_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "movements",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-21", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-21", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-21", "metric": "movement_duplicate_count", "label": "duplicate movements",
        "status": "breach", "severity": "low", "unit": "movements",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "duplicate movements falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_reserve_pick_access_pct_22(record):
    """Evaluate reserve-pick access for control WP-0372-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reserve_pick_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-22", "metric": "reserve_pick_access_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-22", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-22", "metric": "reserve_pick_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-22", "metric": "reserve_pick_access_pct", "label": "reserve-pick access",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "reserve-pick access must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_dispute_resolution_days_23(record):
    """Evaluate dispute resolution time for control WP-0372-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_resolution_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-23", "metric": "dispute_resolution_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-23", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-23", "metric": "dispute_resolution_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-23", "metric": "dispute_resolution_days", "label": "dispute resolution time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dispute resolution time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_gate_checkout_minutes_24(record):
    """Evaluate gate check-out time for control WP-0372-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("gate_checkout_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0372-24", "metric": "gate_checkout_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0372-24", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0372-24", "metric": "gate_checkout_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0372-24", "metric": "gate_checkout_minutes", "label": "gate check-out time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "gate check-out time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_asset_return_age_days_01, assess_supplier_approval_limit_breach_count_02, assess_supplier_frozen_horizon_change_count_03, assess_supplier_delivery_confirmation_pct_04, assess_supplier_data_wipe_verification_pct_05, assess_utilization_pct_06, assess_replenishment_age_hours_07, assess_slow_mover_pct_08, assess_purchase_price_variance_pct_09, assess_vehicle_idle_minutes_10, assess_access_violation_count_11, assess_shift_coverage_pct_12, assess_fire_drill_age_days_13, assess_proof_photo_pct_14, assess_data_logger_download_age_hours_15, assess_customer_replacement_age_hours_16, assess_dock_edge_protection_pct_17, assess_industrial_network_segmentation_pct_18, assess_domain_expiry_days_19, assess_equipment_assignment_gap_count_20, assess_movement_duplicate_count_21, assess_reserve_pick_access_pct_22, assess_dispute_resolution_days_23, assess_gate_checkout_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

