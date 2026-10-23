"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_training_data_lineage_pct_01(record):
    """Evaluate supplier training-data lineage for control WP-0304-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_data_lineage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-01", "metric": "supplier_training_data_lineage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-01", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-01", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-01", "metric": "supplier_training_data_lineage_pct", "label": "supplier training-data lineage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier training-data lineage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_clock_skew_ms_02(record):
    """Evaluate supplier clock skew for control WP-0304-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clock_skew_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-02", "metric": "supplier_clock_skew_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-02", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-02", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-02", "metric": "supplier_clock_skew_ms", "label": "supplier clock skew",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier clock skew must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_secure_development_score_03(record):
    """Evaluate supplier secure-development score for control WP-0304-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_development_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-03", "metric": "supplier_secure_development_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-03", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-03", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-03", "metric": "supplier_secure_development_score", "label": "supplier secure-development score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier secure-development score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_asset_return_age_days_04(record):
    """Evaluate supplier asset return age for control WP-0304-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-04", "metric": "supplier_asset_return_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-04", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-04", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-04", "metric": "supplier_asset_return_age_days", "label": "supplier asset return age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier asset return age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_approval_limit_breach_count_05(record):
    """Evaluate supplier approval-limit breaches for control WP-0304-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_approval_limit_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-05", "metric": "supplier_approval_limit_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-05", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-05", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-05", "metric": "supplier_approval_limit_breach_count", "label": "supplier approval-limit breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "supplier approval-limit breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_frozen_horizon_change_count_06(record):
    """Evaluate frozen-horizon changes for control WP-0304-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_frozen_horizon_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-06", "metric": "supplier_frozen_horizon_change_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-06", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-06", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-06", "metric": "supplier_frozen_horizon_change_count", "label": "frozen-horizon changes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "frozen-horizon changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_delivery_confirmation_pct_07(record):
    """Evaluate supplier delivery confirmation for control WP-0304-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_confirmation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-07", "metric": "supplier_delivery_confirmation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-07", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-07", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-07", "metric": "supplier_delivery_confirmation_pct", "label": "supplier delivery confirmation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier delivery confirmation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_data_wipe_verification_pct_08(record):
    """Evaluate supplier data-wipe verification for control WP-0304-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_wipe_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-08", "metric": "supplier_data_wipe_verification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-08", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-08", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-08", "metric": "supplier_data_wipe_verification_pct", "label": "supplier data-wipe verification",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "supplier data-wipe verification exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_utilization_pct_09(record):
    """Evaluate capacity utilization for control WP-0304-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-09", "metric": "utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-09", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-09", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-09", "metric": "utilization_pct", "label": "capacity utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "capacity utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_replenishment_age_hours_10(record):
    """Evaluate replenishment age for control WP-0304-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-10", "metric": "replenishment_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-10", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-10", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-10", "metric": "replenishment_age_hours", "label": "replenishment age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replenishment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_slow_mover_pct_11(record):
    """Evaluate slow-moving inventory for control WP-0304-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-11", "metric": "slow_mover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-11", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-11", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-11", "metric": "slow_mover_pct", "label": "slow-moving inventory",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slow-moving inventory must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_purchase_price_variance_pct_12(record):
    """Evaluate purchase price variance for control WP-0304-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_price_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-12", "metric": "purchase_price_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-12", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-12", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-12", "metric": "purchase_price_variance_pct", "label": "purchase price variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "purchase price variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_vehicle_idle_minutes_13(record):
    """Evaluate vehicle idle time for control WP-0304-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_idle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-13", "metric": "vehicle_idle_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-13", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-13", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-13", "metric": "vehicle_idle_minutes", "label": "vehicle idle time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "vehicle idle time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_access_violation_count_14(record):
    """Evaluate access violations for control WP-0304-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-14", "metric": "access_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-14", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-14", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-14", "metric": "access_violation_count", "label": "access violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "access violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_shift_coverage_pct_15(record):
    """Evaluate shift coverage for control WP-0304-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-15", "metric": "shift_coverage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-15", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-15", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-15", "metric": "shift_coverage_pct", "label": "shift coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "shift coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_fire_drill_age_days_16(record):
    """Evaluate fire drill age for control WP-0304-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-16", "metric": "fire_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-16", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-16", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-16", "metric": "fire_drill_age_days", "label": "fire drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "fire drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_proof_photo_pct_17(record):
    """Evaluate proof photo completion for control WP-0304-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-17", "metric": "proof_photo_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-17", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-17", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-17", "metric": "proof_photo_pct", "label": "proof photo completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "proof photo completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_data_logger_download_age_hours_18(record):
    """Evaluate data logger download age for control WP-0304-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_logger_download_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-18", "metric": "data_logger_download_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-18", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-18", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-18", "metric": "data_logger_download_age_hours", "label": "data logger download age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data logger download age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_customer_replacement_age_hours_19(record):
    """Evaluate replacement age for control WP-0304-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_replacement_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-19", "metric": "customer_replacement_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-19", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-19", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-19", "metric": "customer_replacement_age_hours", "label": "replacement age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replacement age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_dock_edge_protection_pct_20(record):
    """Evaluate dock edge protection for control WP-0304-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-20", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-20", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-20", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-20", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "dock edge protection exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_industrial_network_segmentation_pct_21(record):
    """Evaluate industrial network segmentation for control WP-0304-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-21", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-21", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-21", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-21", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "industrial network segmentation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_domain_expiry_days_22(record):
    """Evaluate domain validity for control WP-0304-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-22", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-22", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-22", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-22", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "domain validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_equipment_assignment_gap_count_23(record):
    """Evaluate equipment assignment gaps for control WP-0304-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-23", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-23", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-23", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-23", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment assignment gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_movement_duplicate_count_24(record):
    """Evaluate duplicate movements for control WP-0304-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("movement_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0304-24", "metric": "movement_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "movements",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0304-24", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0304-24", "metric": "movement_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0304-24", "metric": "movement_duplicate_count", "label": "duplicate movements",
        "status": "breach", "severity": "critical", "unit": "movements",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "duplicate movements exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_supplier_training_data_lineage_pct_01, assess_supplier_clock_skew_ms_02, assess_supplier_secure_development_score_03, assess_supplier_asset_return_age_days_04, assess_supplier_approval_limit_breach_count_05, assess_supplier_frozen_horizon_change_count_06, assess_supplier_delivery_confirmation_pct_07, assess_supplier_data_wipe_verification_pct_08, assess_utilization_pct_09, assess_replenishment_age_hours_10, assess_slow_mover_pct_11, assess_purchase_price_variance_pct_12, assess_vehicle_idle_minutes_13, assess_access_violation_count_14, assess_shift_coverage_pct_15, assess_fire_drill_age_days_16, assess_proof_photo_pct_17, assess_data_logger_download_age_hours_18, assess_customer_replacement_age_hours_19, assess_dock_edge_protection_pct_20, assess_industrial_network_segmentation_pct_21, assess_domain_expiry_days_22, assess_equipment_assignment_gap_count_23, assess_movement_duplicate_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

