"""Operational control pack for supplier performance; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_loading_supervision_pct_01(record):
    """Evaluate supplier loading supervision for control WP-0485-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_loading_supervision_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-01", "metric": "supplier_loading_supervision_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-01", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-01", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-01", "metric": "supplier_loading_supervision_pct", "label": "supplier loading supervision",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier loading supervision exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_site_change_notice_days_02(record):
    """Evaluate supplier site-change notice for control WP-0485-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-02", "metric": "supplier_site_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-02", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-02", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-02", "metric": "supplier_site_change_notice_days", "label": "supplier site-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier site-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_prop65_compliance_pct_03(record):
    """Evaluate supplier Prop 65 compliance for control WP-0485-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prop65_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-03", "metric": "supplier_prop65_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-03", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-03", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-03", "metric": "supplier_prop65_compliance_pct", "label": "supplier Prop 65 compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier Prop 65 compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_payment_fraud_signal_04(record):
    """Evaluate supplier payment-fraud signal for control WP-0485-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_fraud_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-04", "metric": "supplier_payment_fraud_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-04", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-04", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-04", "metric": "supplier_payment_fraud_signal", "label": "supplier payment-fraud signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment-fraud signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_it_recovery_minutes_05(record):
    """Evaluate supplier IT recovery time for control WP-0485-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_it_recovery_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-05", "metric": "supplier_it_recovery_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-05", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-05", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-05", "metric": "supplier_it_recovery_minutes", "label": "supplier IT recovery time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "supplier IT recovery time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_algorithm_change_notice_days_06(record):
    """Evaluate supplier algorithm-change notice for control WP-0485-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_algorithm_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-06", "metric": "supplier_algorithm_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-06", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-06", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-06", "metric": "supplier_algorithm_change_notice_days", "label": "supplier algorithm-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier algorithm-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_dependency_update_age_days_07(record):
    """Evaluate supplier dependency update age for control WP-0485-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_update_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-07", "metric": "supplier_dependency_update_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-07", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-07", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-07", "metric": "supplier_dependency_update_age_days", "label": "supplier dependency update age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dependency update age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_scim_sync_age_hours_08(record):
    """Evaluate supplier SCIM sync age for control WP-0485-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scim_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-08", "metric": "supplier_scim_sync_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-08", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-08", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-08", "metric": "supplier_scim_sync_age_hours", "label": "supplier SCIM sync age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SCIM sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_deletion_verification_pct_09(record):
    """Evaluate supplier deletion verification for control WP-0485-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deletion_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-09", "metric": "supplier_deletion_verification_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-09", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-09", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-09", "metric": "supplier_deletion_verification_pct", "label": "supplier deletion verification",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier deletion verification exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_supplier_control_mapping_pct_10(record):
    """Evaluate supplier control mapping for control WP-0485-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_mapping_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-10", "metric": "supplier_control_mapping_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-10", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-10", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-10", "metric": "supplier_control_mapping_pct", "label": "supplier control mapping",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "supplier control mapping falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_supplier_credit_note_match_pct_11(record):
    """Evaluate supplier credit-note match for control WP-0485-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-11", "metric": "supplier_credit_note_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-11", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-11", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-11", "metric": "supplier_credit_note_match_pct", "label": "supplier credit-note match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier credit-note match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_supplier_inventory_accuracy_pct_12(record):
    """Evaluate supplier inventory accuracy for control WP-0485-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-12", "metric": "supplier_inventory_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-12", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-12", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-12", "metric": "supplier_inventory_accuracy_pct", "label": "supplier inventory accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier inventory accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_supplier_parallel_run_days_13(record):
    """Evaluate supplier parallel run duration for control WP-0485-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_parallel_run_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-13", "metric": "supplier_parallel_run_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-13", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-13", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-13", "metric": "supplier_parallel_run_days", "label": "supplier parallel run duration",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier parallel run duration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_available_qty_14(record):
    """Evaluate available quantity for control WP-0485-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("available_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-14", "metric": "available_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 24,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-14", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-14", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 24
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-14", "metric": "available_qty", "label": "available quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 24, "comparison": "min",
        "finding": "available quantity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_dock_wait_minutes_15(record):
    """Evaluate dock waiting time for control WP-0485-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-15", "metric": "dock_wait_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-15", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-15", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-15", "metric": "dock_wait_minutes", "label": "dock waiting time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dock waiting time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_route_deviation_km_16(record):
    """Evaluate route deviation for control WP-0485-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-16", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "low", "unit": "km",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-16", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-16", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-16", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "low", "unit": "km",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "route deviation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_data_quality_score_17(record):
    """Evaluate data quality for control WP-0485-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-17", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-17", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-17", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-17", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "data quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_refund_age_days_18(record):
    """Evaluate refund age for control WP-0485-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-18", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 68,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-18", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-18", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 68
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-18", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 68, "comparison": "min",
        "finding": "refund age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_temperature_calibration_age_days_19(record):
    """Evaluate temperature calibration age for control WP-0485-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-19", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-19", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-19", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-19", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "temperature calibration age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_form_error_pct_20(record):
    """Evaluate form error rate for control WP-0485-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-20", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-20", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-20", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-20", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "form error rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

def assess_sorter_missort_count_21(record):
    """Evaluate sorter missorts for control WP-0485-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-21", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-21", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-21", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-21", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "sorter missorts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "supplier performance",
    }

def assess_tamper_signal_count_22(record):
    """Evaluate tamper signals for control WP-0485-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_signal_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-22", "metric": "tamper_signal_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-22", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-22", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-22", "metric": "tamper_signal_count", "label": "tamper signals",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "tamper signals falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "supplier performance",
    }

def assess_temperature_excursion_count_23(record):
    """Evaluate temperature excursions for control WP-0485-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_excursion_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-23", "metric": "temperature_excursion_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-23", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-23", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-23", "metric": "temperature_excursion_count", "label": "temperature excursions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "temperature excursions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "supplier performance",
    }

def assess_warranty_registration_pct_24(record):
    """Evaluate warranty registration for control WP-0485-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warranty_registration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0485-24", "metric": "warranty_registration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0485-24", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0485-24", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0485-24", "metric": "warranty_registration_pct", "label": "warranty registration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "warranty registration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "supplier performance",
    }

RULES = (assess_supplier_loading_supervision_pct_01, assess_supplier_site_change_notice_days_02, assess_supplier_prop65_compliance_pct_03, assess_supplier_payment_fraud_signal_04, assess_supplier_it_recovery_minutes_05, assess_supplier_algorithm_change_notice_days_06, assess_supplier_dependency_update_age_days_07, assess_supplier_scim_sync_age_hours_08, assess_supplier_deletion_verification_pct_09, assess_supplier_control_mapping_pct_10, assess_supplier_credit_note_match_pct_11, assess_supplier_inventory_accuracy_pct_12, assess_supplier_parallel_run_days_13, assess_available_qty_14, assess_dock_wait_minutes_15, assess_route_deviation_km_16, assess_data_quality_score_17, assess_refund_age_days_18, assess_temperature_calibration_age_days_19, assess_form_error_pct_20, assess_sorter_missort_count_21, assess_tamper_signal_count_22, assess_temperature_excursion_count_23, assess_warranty_registration_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

