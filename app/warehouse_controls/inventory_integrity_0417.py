"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_cost_change_notice_days_01(record):
    """Evaluate supplier cost-change notice for control WP-0417-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-01", "metric": "supplier_cost_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-01", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-01", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-01", "metric": "supplier_cost_change_notice_days", "label": "supplier cost-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "supplier cost-change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_change_failure_pct_02(record):
    """Evaluate supplier change-failure rate for control WP-0417-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-02", "metric": "supplier_change_failure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-02", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-02", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-02", "metric": "supplier_change_failure_pct", "label": "supplier change-failure rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier change-failure rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_weight_spec_match_pct_03(record):
    """Evaluate supplier weight specification match for control WP-0417-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_weight_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-03", "metric": "supplier_weight_spec_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-03", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-03", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-03", "metric": "supplier_weight_spec_match_pct", "label": "supplier weight specification match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier weight specification match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_loading_supervision_pct_04(record):
    """Evaluate supplier loading supervision for control WP-0417-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_loading_supervision_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-04", "metric": "supplier_loading_supervision_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-04", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-04", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-04", "metric": "supplier_loading_supervision_pct", "label": "supplier loading supervision",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier loading supervision must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_site_change_notice_days_05(record):
    """Evaluate supplier site-change notice for control WP-0417-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-05", "metric": "supplier_site_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-05", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-05", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-05", "metric": "supplier_site_change_notice_days", "label": "supplier site-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "supplier site-change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_prop65_compliance_pct_06(record):
    """Evaluate supplier Prop 65 compliance for control WP-0417-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prop65_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-06", "metric": "supplier_prop65_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-06", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-06", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-06", "metric": "supplier_prop65_compliance_pct", "label": "supplier Prop 65 compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier Prop 65 compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_payment_fraud_signal_07(record):
    """Evaluate supplier payment-fraud signal for control WP-0417-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_fraud_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-07", "metric": "supplier_payment_fraud_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-07", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-07", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-07", "metric": "supplier_payment_fraud_signal", "label": "supplier payment-fraud signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier payment-fraud signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_it_recovery_minutes_08(record):
    """Evaluate supplier IT recovery time for control WP-0417-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_it_recovery_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-08", "metric": "supplier_it_recovery_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-08", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-08", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-08", "metric": "supplier_it_recovery_minutes", "label": "supplier IT recovery time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier IT recovery time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_algorithm_change_notice_days_09(record):
    """Evaluate supplier algorithm-change notice for control WP-0417-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_algorithm_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-09", "metric": "supplier_algorithm_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-09", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-09", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-09", "metric": "supplier_algorithm_change_notice_days", "label": "supplier algorithm-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier algorithm-change notice exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_dependency_update_age_days_10(record):
    """Evaluate supplier dependency update age for control WP-0417-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_update_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-10", "metric": "supplier_dependency_update_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-10", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-10", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-10", "metric": "supplier_dependency_update_age_days", "label": "supplier dependency update age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier dependency update age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_scim_sync_age_hours_11(record):
    """Evaluate supplier SCIM sync age for control WP-0417-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scim_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-11", "metric": "supplier_scim_sync_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-11", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-11", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-11", "metric": "supplier_scim_sync_age_hours", "label": "supplier SCIM sync age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier SCIM sync age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_deletion_verification_pct_12(record):
    """Evaluate supplier deletion verification for control WP-0417-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deletion_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-12", "metric": "supplier_deletion_verification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-12", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-12", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-12", "metric": "supplier_deletion_verification_pct", "label": "supplier deletion verification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier deletion verification must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_control_mapping_pct_13(record):
    """Evaluate supplier control mapping for control WP-0417-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_mapping_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-13", "metric": "supplier_control_mapping_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-13", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-13", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-13", "metric": "supplier_control_mapping_pct", "label": "supplier control mapping",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier control mapping exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_credit_note_match_pct_14(record):
    """Evaluate supplier credit-note match for control WP-0417-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-14", "metric": "supplier_credit_note_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-14", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-14", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-14", "metric": "supplier_credit_note_match_pct", "label": "supplier credit-note match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier credit-note match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_inventory_accuracy_pct_15(record):
    """Evaluate supplier inventory accuracy for control WP-0417-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-15", "metric": "supplier_inventory_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-15", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-15", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-15", "metric": "supplier_inventory_accuracy_pct", "label": "supplier inventory accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier inventory accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_parallel_run_days_16(record):
    """Evaluate supplier parallel run duration for control WP-0417-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_parallel_run_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-16", "metric": "supplier_parallel_run_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-16", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-16", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-16", "metric": "supplier_parallel_run_days", "label": "supplier parallel run duration",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier parallel run duration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_available_qty_17(record):
    """Evaluate available quantity for control WP-0417-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("available_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-17", "metric": "available_qty",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-17", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-17", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-17", "metric": "available_qty", "label": "available quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "available quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_dock_wait_minutes_18(record):
    """Evaluate dock waiting time for control WP-0417-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-18", "metric": "dock_wait_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-18", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-18", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-18", "metric": "dock_wait_minutes", "label": "dock waiting time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "dock waiting time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_route_deviation_km_19(record):
    """Evaluate route deviation for control WP-0417-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-19", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "critical", "unit": "km",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-19", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-19", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-19", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "critical", "unit": "km",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "route deviation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_data_quality_score_20(record):
    """Evaluate data quality for control WP-0417-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-20", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-20", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-20", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-20", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_refund_age_days_21(record):
    """Evaluate refund age for control WP-0417-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-21", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-21", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-21", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-21", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "refund age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_temperature_calibration_age_days_22(record):
    """Evaluate temperature calibration age for control WP-0417-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-22", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-22", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-22", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-22", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "temperature calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_form_error_pct_23(record):
    """Evaluate form error rate for control WP-0417-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-23", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-23", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-23", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-23", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "form error rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_sorter_missort_count_24(record):
    """Evaluate sorter missorts for control WP-0417-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0417-24", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0417-24", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0417-24", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0417-24", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sorter missorts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_cost_change_notice_days_01, assess_supplier_change_failure_pct_02, assess_supplier_weight_spec_match_pct_03, assess_supplier_loading_supervision_pct_04, assess_supplier_site_change_notice_days_05, assess_supplier_prop65_compliance_pct_06, assess_supplier_payment_fraud_signal_07, assess_supplier_it_recovery_minutes_08, assess_supplier_algorithm_change_notice_days_09, assess_supplier_dependency_update_age_days_10, assess_supplier_scim_sync_age_hours_11, assess_supplier_deletion_verification_pct_12, assess_supplier_control_mapping_pct_13, assess_supplier_credit_note_match_pct_14, assess_supplier_inventory_accuracy_pct_15, assess_supplier_parallel_run_days_16, assess_available_qty_17, assess_dock_wait_minutes_18, assess_route_deviation_km_19, assess_data_quality_score_20, assess_refund_age_days_21, assess_temperature_calibration_age_days_22, assess_form_error_pct_23, assess_sorter_missort_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

