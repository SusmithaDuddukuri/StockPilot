"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_predictive_maintenance_pct_01(record):
    """Evaluate supplier predictive maintenance for control WP-0493-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_predictive_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-01", "metric": "supplier_predictive_maintenance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-01", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-01", "metric": "supplier_predictive_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-01", "metric": "supplier_predictive_maintenance_pct", "label": "supplier predictive maintenance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "supplier predictive maintenance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_label_quality_score_02(record):
    """Evaluate supplier label quality for control WP-0493-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-02", "metric": "supplier_label_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-02", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-02", "metric": "supplier_label_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-02", "metric": "supplier_label_quality_score", "label": "supplier label quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier label quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_multi_region_coverage_pct_03(record):
    """Evaluate supplier multi-region coverage for control WP-0493-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_multi_region_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-03", "metric": "supplier_multi_region_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-03", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-03", "metric": "supplier_multi_region_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-03", "metric": "supplier_multi_region_coverage_pct", "label": "supplier multi-region coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier multi-region coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_privacy_impact_age_days_04(record):
    """Evaluate supplier privacy impact assessment age for control WP-0493-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_impact_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-04", "metric": "supplier_privacy_impact_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-04", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-04", "metric": "supplier_privacy_impact_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-04", "metric": "supplier_privacy_impact_age_days", "label": "supplier privacy impact assessment age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier privacy impact assessment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_residual_risk_score_05(record):
    """Evaluate supplier residual risk for control WP-0493-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_residual_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-05", "metric": "supplier_residual_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-05", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-05", "metric": "supplier_residual_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-05", "metric": "supplier_residual_risk_score", "label": "supplier residual risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "supplier residual risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_duplicate_invoice_signal_06(record):
    """Evaluate duplicate-invoice signal for control WP-0493-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_invoice_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-06", "metric": "supplier_duplicate_invoice_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-06", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-06", "metric": "supplier_duplicate_invoice_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-06", "metric": "supplier_duplicate_invoice_signal", "label": "duplicate-invoice signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "duplicate-invoice signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_batch_cycle_hours_07(record):
    """Evaluate supplier batch cycle for control WP-0493-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_batch_cycle_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-07", "metric": "supplier_batch_cycle_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-07", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-07", "metric": "supplier_batch_cycle_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-07", "metric": "supplier_batch_cycle_hours", "label": "supplier batch cycle",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier batch cycle must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_award_expiry_days_08(record):
    """Evaluate supplier award validity for control WP-0493-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_award_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-08", "metric": "supplier_award_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-08", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-08", "metric": "supplier_award_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-08", "metric": "supplier_award_expiry_days", "label": "supplier award validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier award validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_post_exit_access_count_09(record):
    """Evaluate post-exit access events for control WP-0493-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_access_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-09", "metric": "supplier_post_exit_access_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 169,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-09", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-09", "metric": "supplier_post_exit_access_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 169
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-09", "metric": "supplier_post_exit_access_count", "label": "post-exit access events",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 169, "comparison": "max",
        "finding": "post-exit access events exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_expiry_days_10(record):
    """Evaluate days to expiry for control WP-0493-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-10", "metric": "expiry_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-10", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-10", "metric": "expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-10", "metric": "expiry_days", "label": "days to expiry",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "days to expiry falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_customs_hold_hours_11(record):
    """Evaluate customs hold for control WP-0493-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_hold_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-11", "metric": "customs_hold_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-11", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-11", "metric": "customs_hold_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-11", "metric": "customs_hold_hours", "label": "customs hold",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customs hold must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_water_leak_signal_12(record):
    """Evaluate water leak signal for control WP-0493-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-12", "metric": "water_leak_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-12", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-12", "metric": "water_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-12", "metric": "water_leak_signal", "label": "water leak signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "water leak signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_scanner_disconnect_count_13(record):
    """Evaluate scanner disconnects for control WP-0493-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_disconnect_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-13", "metric": "scanner_disconnect_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-13", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-13", "metric": "scanner_disconnect_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-13", "metric": "scanner_disconnect_count", "label": "scanner disconnects",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "scanner disconnects exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_receiving_accuracy_pct_14(record):
    """Evaluate receiving accuracy for control WP-0493-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("receiving_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-14", "metric": "receiving_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-14", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-14", "metric": "receiving_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-14", "metric": "receiving_accuracy_pct", "label": "receiving accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "receiving accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_queue_retry_pct_15(record):
    """Evaluate queue retry rate for control WP-0493-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("queue_retry_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-15", "metric": "queue_retry_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-15", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-15", "metric": "queue_retry_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-15", "metric": "queue_retry_pct", "label": "queue retry rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "queue retry rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_case_pick_ratio_pct_16(record):
    """Evaluate case pick ratio for control WP-0493-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("case_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-16", "metric": "case_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-16", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-16", "metric": "case_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-16", "metric": "case_pick_ratio_pct", "label": "case pick ratio",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "case pick ratio must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_visitor_badge_gap_count_17(record):
    """Evaluate visitor badge gaps for control WP-0493-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("visitor_badge_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-17", "metric": "visitor_badge_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-17", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-17", "metric": "visitor_badge_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-17", "metric": "visitor_badge_gap_count", "label": "visitor badge gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "visitor badge gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_water_consumption_liters_18(record):
    """Evaluate water consumption for control WP-0493-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("water_consumption_liters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-18", "metric": "water_consumption_liters",
            "status": "insufficient_data",
            "severity": "high", "unit": "liters",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-18", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-18", "metric": "water_consumption_liters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-18", "metric": "water_consumption_liters", "label": "water consumption",
        "status": "breach", "severity": "high", "unit": "liters",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "water consumption falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_vault_access_review_age_days_19(record):
    """Evaluate vault access review age for control WP-0493-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vault_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-19", "metric": "vault_access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-19", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-19", "metric": "vault_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-19", "metric": "vault_access_review_age_days", "label": "vault access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vault access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_sds_access_pct_20(record):
    """Evaluate SDS access completeness for control WP-0493-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sds_access_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-20", "metric": "sds_access_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-20", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-20", "metric": "sds_access_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-20", "metric": "sds_access_pct", "label": "SDS access completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "SDS access completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_planned_maintenance_pct_21(record):
    """Evaluate planned maintenance share for control WP-0493-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("planned_maintenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-21", "metric": "planned_maintenance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-21", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-21", "metric": "planned_maintenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-21", "metric": "planned_maintenance_pct", "label": "planned maintenance share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "planned maintenance share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_service_availability_pct_22(record):
    """Evaluate service availability for control WP-0493-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-22", "metric": "service_availability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-22", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-22", "metric": "service_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-22", "metric": "service_availability_pct", "label": "service availability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "service availability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_record_uniqueness_pct_23(record):
    """Evaluate record uniqueness for control WP-0493-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_uniqueness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-23", "metric": "record_uniqueness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-23", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-23", "metric": "record_uniqueness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-23", "metric": "record_uniqueness_pct", "label": "record uniqueness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "record uniqueness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_carrier_master_gap_count_24(record):
    """Evaluate carrier master gaps for control WP-0493-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0493-24", "metric": "carrier_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0493-24", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0493-24", "metric": "carrier_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0493-24", "metric": "carrier_master_gap_count", "label": "carrier master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carrier master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_predictive_maintenance_pct_01, assess_supplier_label_quality_score_02, assess_supplier_multi_region_coverage_pct_03, assess_supplier_privacy_impact_age_days_04, assess_supplier_residual_risk_score_05, assess_supplier_duplicate_invoice_signal_06, assess_supplier_batch_cycle_hours_07, assess_supplier_award_expiry_days_08, assess_supplier_post_exit_access_count_09, assess_expiry_days_10, assess_customs_hold_hours_11, assess_water_leak_signal_12, assess_scanner_disconnect_count_13, assess_receiving_accuracy_pct_14, assess_queue_retry_pct_15, assess_case_pick_ratio_pct_16, assess_visitor_badge_gap_count_17, assess_water_consumption_liters_18, assess_vault_access_review_age_days_19, assess_sds_access_pct_20, assess_planned_maintenance_pct_21, assess_service_availability_pct_22, assess_record_uniqueness_pct_23, assess_carrier_master_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

