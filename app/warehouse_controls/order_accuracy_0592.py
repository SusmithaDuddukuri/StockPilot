"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_secret_scan_findings_01(record):
    """Evaluate secret scan findings for control WP-0592-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secret_scan_findings")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-01", "metric": "secret_scan_findings",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-01", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-01", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-01", "metric": "secret_scan_findings", "label": "secret scan findings",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "secret scan findings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_scanner_read_rate_pct_02(record):
    """Evaluate scanner read rate for control WP-0592-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-02", "metric": "scanner_read_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-02", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-02", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-02", "metric": "scanner_read_rate_pct", "label": "scanner read rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner read rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_adjustment_reason_completeness_pct_03(record):
    """Evaluate adjustment reason completeness for control WP-0592-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("adjustment_reason_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-03", "metric": "adjustment_reason_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-03", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-03", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-03", "metric": "adjustment_reason_completeness_pct", "label": "adjustment reason completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "adjustment reason completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_pick_confirmation_latency_ms_04(record):
    """Evaluate pick confirmation latency for control WP-0592-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_confirmation_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-04", "metric": "pick_confirmation_latency_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-04", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-04", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-04", "metric": "pick_confirmation_latency_ms", "label": "pick confirmation latency",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "pick confirmation latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_bonded_stock_variance_05(record):
    """Evaluate bonded stock variance for control WP-0592-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bonded_stock_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-05", "metric": "bonded_stock_variance",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-05", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-05", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-05", "metric": "bonded_stock_variance", "label": "bonded stock variance",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "bonded stock variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_empty_miles_pct_06(record):
    """Evaluate empty miles share for control WP-0592-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_miles_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-06", "metric": "empty_miles_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-06", "metric": "empty_miles_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-06", "metric": "empty_miles_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-06", "metric": "empty_miles_pct", "label": "empty miles share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "empty miles share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_idle_time_pct_07(record):
    """Evaluate idle time share for control WP-0592-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("idle_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-07", "metric": "idle_time_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-07", "metric": "idle_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-07", "metric": "idle_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-07", "metric": "idle_time_pct", "label": "idle time share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "idle time share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_certification_days_left_08(record):
    """Evaluate supplier certification validity for control WP-0592-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-08", "metric": "supplier_certification_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-08", "metric": "supplier_certification_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-08", "metric": "supplier_certification_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-08", "metric": "supplier_certification_days_left", "label": "supplier certification validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier certification validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_return_material_age_days_09(record):
    """Evaluate supplier return material age for control WP-0592-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_return_material_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-09", "metric": "supplier_return_material_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-09", "metric": "supplier_return_material_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-09", "metric": "supplier_return_material_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-09", "metric": "supplier_return_material_age_days", "label": "supplier return material age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier return material age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_cost_change_notice_days_10(record):
    """Evaluate supplier cost-change notice for control WP-0592-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-10", "metric": "supplier_cost_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-10", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-10", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-10", "metric": "supplier_cost_change_notice_days", "label": "supplier cost-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier cost-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_change_failure_pct_11(record):
    """Evaluate supplier change-failure rate for control WP-0592-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-11", "metric": "supplier_change_failure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-11", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-11", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-11", "metric": "supplier_change_failure_pct", "label": "supplier change-failure rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier change-failure rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_weight_spec_match_pct_12(record):
    """Evaluate supplier weight specification match for control WP-0592-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_weight_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-12", "metric": "supplier_weight_spec_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-12", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-12", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-12", "metric": "supplier_weight_spec_match_pct", "label": "supplier weight specification match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier weight specification match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_loading_supervision_pct_13(record):
    """Evaluate supplier loading supervision for control WP-0592-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_loading_supervision_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-13", "metric": "supplier_loading_supervision_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-13", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-13", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-13", "metric": "supplier_loading_supervision_pct", "label": "supplier loading supervision",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier loading supervision falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_site_change_notice_days_14(record):
    """Evaluate supplier site-change notice for control WP-0592-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-14", "metric": "supplier_site_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-14", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-14", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-14", "metric": "supplier_site_change_notice_days", "label": "supplier site-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier site-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_prop65_compliance_pct_15(record):
    """Evaluate supplier Prop 65 compliance for control WP-0592-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prop65_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-15", "metric": "supplier_prop65_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-15", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-15", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-15", "metric": "supplier_prop65_compliance_pct", "label": "supplier Prop 65 compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier Prop 65 compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_payment_fraud_signal_16(record):
    """Evaluate supplier payment-fraud signal for control WP-0592-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_fraud_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-16", "metric": "supplier_payment_fraud_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-16", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-16", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-16", "metric": "supplier_payment_fraud_signal", "label": "supplier payment-fraud signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier payment-fraud signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_it_recovery_minutes_17(record):
    """Evaluate supplier IT recovery time for control WP-0592-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_it_recovery_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-17", "metric": "supplier_it_recovery_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-17", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-17", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-17", "metric": "supplier_it_recovery_minutes", "label": "supplier IT recovery time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier IT recovery time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_algorithm_change_notice_days_18(record):
    """Evaluate supplier algorithm-change notice for control WP-0592-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_algorithm_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-18", "metric": "supplier_algorithm_change_notice_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-18", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-18", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-18", "metric": "supplier_algorithm_change_notice_days", "label": "supplier algorithm-change notice",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier algorithm-change notice must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_dependency_update_age_days_19(record):
    """Evaluate supplier dependency update age for control WP-0592-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_update_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-19", "metric": "supplier_dependency_update_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-19", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-19", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-19", "metric": "supplier_dependency_update_age_days", "label": "supplier dependency update age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dependency update age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_scim_sync_age_hours_20(record):
    """Evaluate supplier SCIM sync age for control WP-0592-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scim_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-20", "metric": "supplier_scim_sync_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-20", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-20", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-20", "metric": "supplier_scim_sync_age_hours", "label": "supplier SCIM sync age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier SCIM sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_deletion_verification_pct_21(record):
    """Evaluate supplier deletion verification for control WP-0592-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deletion_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-21", "metric": "supplier_deletion_verification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-21", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-21", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-21", "metric": "supplier_deletion_verification_pct", "label": "supplier deletion verification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "supplier deletion verification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_control_mapping_pct_22(record):
    """Evaluate supplier control mapping for control WP-0592-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_mapping_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-22", "metric": "supplier_control_mapping_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-22", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-22", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-22", "metric": "supplier_control_mapping_pct", "label": "supplier control mapping",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier control mapping must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_credit_note_match_pct_23(record):
    """Evaluate supplier credit-note match for control WP-0592-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-23", "metric": "supplier_credit_note_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-23", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-23", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-23", "metric": "supplier_credit_note_match_pct", "label": "supplier credit-note match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit-note match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_inventory_accuracy_pct_24(record):
    """Evaluate supplier inventory accuracy for control WP-0592-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0592-24", "metric": "supplier_inventory_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0592-24", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0592-24", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0592-24", "metric": "supplier_inventory_accuracy_pct", "label": "supplier inventory accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier inventory accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_secret_scan_findings_01, assess_scanner_read_rate_pct_02, assess_adjustment_reason_completeness_pct_03, assess_pick_confirmation_latency_ms_04, assess_bonded_stock_variance_05, assess_empty_miles_pct_06, assess_idle_time_pct_07, assess_supplier_certification_days_left_08, assess_supplier_return_material_age_days_09, assess_supplier_cost_change_notice_days_10, assess_supplier_change_failure_pct_11, assess_supplier_weight_spec_match_pct_12, assess_supplier_loading_supervision_pct_13, assess_supplier_site_change_notice_days_14, assess_supplier_prop65_compliance_pct_15, assess_supplier_payment_fraud_signal_16, assess_supplier_it_recovery_minutes_17, assess_supplier_algorithm_change_notice_days_18, assess_supplier_dependency_update_age_days_19, assess_supplier_scim_sync_age_hours_20, assess_supplier_deletion_verification_pct_21, assess_supplier_control_mapping_pct_22, assess_supplier_credit_note_match_pct_23, assess_supplier_inventory_accuracy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

