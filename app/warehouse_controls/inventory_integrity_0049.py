"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_record_retention_pct_01(record):
    """Evaluate supplier record retention for control WP-0049-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-01", "metric": "supplier_record_retention_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-01", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-01", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-01", "metric": "supplier_record_retention_pct", "label": "supplier record retention",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier record retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_training_data_lineage_pct_02(record):
    """Evaluate supplier training-data lineage for control WP-0049-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_data_lineage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-02", "metric": "supplier_training_data_lineage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-02", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-02", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-02", "metric": "supplier_training_data_lineage_pct", "label": "supplier training-data lineage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier training-data lineage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_clock_skew_ms_03(record):
    """Evaluate supplier clock skew for control WP-0049-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clock_skew_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-03", "metric": "supplier_clock_skew_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-03", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-03", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-03", "metric": "supplier_clock_skew_ms", "label": "supplier clock skew",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier clock skew must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_secure_development_score_04(record):
    """Evaluate supplier secure-development score for control WP-0049-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_development_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-04", "metric": "supplier_secure_development_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-04", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-04", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-04", "metric": "supplier_secure_development_score", "label": "supplier secure-development score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier secure-development score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_asset_return_age_days_05(record):
    """Evaluate supplier asset return age for control WP-0049-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-05", "metric": "supplier_asset_return_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-05", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-05", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-05", "metric": "supplier_asset_return_age_days", "label": "supplier asset return age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier asset return age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_approval_limit_breach_count_06(record):
    """Evaluate supplier approval-limit breaches for control WP-0049-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_approval_limit_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-06", "metric": "supplier_approval_limit_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-06", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-06", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-06", "metric": "supplier_approval_limit_breach_count", "label": "supplier approval-limit breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "supplier approval-limit breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_frozen_horizon_change_count_07(record):
    """Evaluate frozen-horizon changes for control WP-0049-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_frozen_horizon_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-07", "metric": "supplier_frozen_horizon_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-07", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-07", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-07", "metric": "supplier_frozen_horizon_change_count", "label": "frozen-horizon changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "frozen-horizon changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_delivery_confirmation_pct_08(record):
    """Evaluate supplier delivery confirmation for control WP-0049-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_confirmation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-08", "metric": "supplier_delivery_confirmation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-08", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-08", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-08", "metric": "supplier_delivery_confirmation_pct", "label": "supplier delivery confirmation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier delivery confirmation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_data_wipe_verification_pct_09(record):
    """Evaluate supplier data-wipe verification for control WP-0049-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_wipe_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-09", "metric": "supplier_data_wipe_verification_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-09", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-09", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-09", "metric": "supplier_data_wipe_verification_pct", "label": "supplier data-wipe verification",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier data-wipe verification exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_utilization_pct_10(record):
    """Evaluate capacity utilization for control WP-0049-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-10", "metric": "utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-10", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-10", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-10", "metric": "utilization_pct", "label": "capacity utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "capacity utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_replenishment_age_hours_11(record):
    """Evaluate replenishment age for control WP-0049-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-11", "metric": "replenishment_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-11", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-11", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-11", "metric": "replenishment_age_hours", "label": "replenishment age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replenishment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_slow_mover_pct_12(record):
    """Evaluate slow-moving inventory for control WP-0049-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-12", "metric": "slow_mover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-12", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-12", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-12", "metric": "slow_mover_pct", "label": "slow-moving inventory",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slow-moving inventory must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_purchase_price_variance_pct_13(record):
    """Evaluate purchase price variance for control WP-0049-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_price_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-13", "metric": "purchase_price_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-13", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-13", "metric": "purchase_price_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-13", "metric": "purchase_price_variance_pct", "label": "purchase price variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "purchase price variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_vehicle_idle_minutes_14(record):
    """Evaluate vehicle idle time for control WP-0049-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_idle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-14", "metric": "vehicle_idle_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-14", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-14", "metric": "vehicle_idle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-14", "metric": "vehicle_idle_minutes", "label": "vehicle idle time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "vehicle idle time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_access_violation_count_15(record):
    """Evaluate access violations for control WP-0049-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-15", "metric": "access_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-15", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-15", "metric": "access_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-15", "metric": "access_violation_count", "label": "access violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "access violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_shift_coverage_pct_16(record):
    """Evaluate shift coverage for control WP-0049-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shift_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-16", "metric": "shift_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-16", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-16", "metric": "shift_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-16", "metric": "shift_coverage_pct", "label": "shift coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "shift coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_fire_drill_age_days_17(record):
    """Evaluate fire drill age for control WP-0049-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-17", "metric": "fire_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-17", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-17", "metric": "fire_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-17", "metric": "fire_drill_age_days", "label": "fire drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "fire drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_proof_photo_pct_18(record):
    """Evaluate proof photo completion for control WP-0049-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("proof_photo_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-18", "metric": "proof_photo_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-18", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-18", "metric": "proof_photo_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-18", "metric": "proof_photo_pct", "label": "proof photo completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "proof photo completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_data_logger_download_age_hours_19(record):
    """Evaluate data logger download age for control WP-0049-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_logger_download_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-19", "metric": "data_logger_download_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-19", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-19", "metric": "data_logger_download_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-19", "metric": "data_logger_download_age_hours", "label": "data logger download age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data logger download age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_customer_replacement_age_hours_20(record):
    """Evaluate replacement age for control WP-0049-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_replacement_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-20", "metric": "customer_replacement_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-20", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-20", "metric": "customer_replacement_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-20", "metric": "customer_replacement_age_hours", "label": "replacement age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replacement age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_dock_edge_protection_pct_21(record):
    """Evaluate dock edge protection for control WP-0049-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_edge_protection_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-21", "metric": "dock_edge_protection_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-21", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-21", "metric": "dock_edge_protection_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-21", "metric": "dock_edge_protection_pct", "label": "dock edge protection",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "dock edge protection exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_industrial_network_segmentation_pct_22(record):
    """Evaluate industrial network segmentation for control WP-0049-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("industrial_network_segmentation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-22", "metric": "industrial_network_segmentation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-22", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-22", "metric": "industrial_network_segmentation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-22", "metric": "industrial_network_segmentation_pct", "label": "industrial network segmentation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "industrial network segmentation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_domain_expiry_days_23(record):
    """Evaluate domain validity for control WP-0049-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("domain_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-23", "metric": "domain_expiry_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-23", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-23", "metric": "domain_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-23", "metric": "domain_expiry_days", "label": "domain validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "domain validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_equipment_assignment_gap_count_24(record):
    """Evaluate equipment assignment gaps for control WP-0049-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_assignment_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0049-24", "metric": "equipment_assignment_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0049-24", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0049-24", "metric": "equipment_assignment_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0049-24", "metric": "equipment_assignment_gap_count", "label": "equipment assignment gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment assignment gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_record_retention_pct_01, assess_supplier_training_data_lineage_pct_02, assess_supplier_clock_skew_ms_03, assess_supplier_secure_development_score_04, assess_supplier_asset_return_age_days_05, assess_supplier_approval_limit_breach_count_06, assess_supplier_frozen_horizon_change_count_07, assess_supplier_delivery_confirmation_pct_08, assess_supplier_data_wipe_verification_pct_09, assess_utilization_pct_10, assess_replenishment_age_hours_11, assess_slow_mover_pct_12, assess_purchase_price_variance_pct_13, assess_vehicle_idle_minutes_14, assess_access_violation_count_15, assess_shift_coverage_pct_16, assess_fire_drill_age_days_17, assess_proof_photo_pct_18, assess_data_logger_download_age_hours_19, assess_customer_replacement_age_hours_20, assess_dock_edge_protection_pct_21, assess_industrial_network_segmentation_pct_22, assess_domain_expiry_days_23, assess_equipment_assignment_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

