"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_ppap_approval_pct_01(record):
    """Evaluate supplier PPAP approval for control WP-0234-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppap_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-01", "metric": "supplier_ppap_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-01", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-01", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-01", "metric": "supplier_ppap_approval_pct", "label": "supplier PPAP approval",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier PPAP approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_spill_response_drill_age_days_02(record):
    """Evaluate supplier spill drill age for control WP-0234-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spill_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-02", "metric": "supplier_spill_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-02", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-02", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-02", "metric": "supplier_spill_response_drill_age_days", "label": "supplier spill drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier spill drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_ar_days_03(record):
    """Evaluate supplier accounts-receivable days for control WP-0234-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ar_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-03", "metric": "supplier_ar_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-03", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-03", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-03", "metric": "supplier_ar_days", "label": "supplier accounts-receivable days",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier accounts-receivable days falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_training_refresh_days_04(record):
    """Evaluate supplier training refresh interval for control WP-0234-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_refresh_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-04", "metric": "supplier_training_refresh_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-04", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-04", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-04", "metric": "supplier_training_refresh_days", "label": "supplier training refresh interval",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training refresh interval must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_human_override_pct_05(record):
    """Evaluate supplier human override rate for control WP-0234-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_override_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-05", "metric": "supplier_human_override_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-05", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-05", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-05", "metric": "supplier_human_override_pct", "label": "supplier human override rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier human override rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_idempotency_violation_count_06(record):
    """Evaluate supplier idempotency violations for control WP-0234-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_idempotency_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-06", "metric": "supplier_idempotency_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-06", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-06", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-06", "metric": "supplier_idempotency_violation_count", "label": "supplier idempotency violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier idempotency violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_threat_model_age_days_07(record):
    """Evaluate supplier threat-model age for control WP-0234-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_threat_model_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-07", "metric": "supplier_threat_model_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-07", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-07", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-07", "metric": "supplier_threat_model_age_days", "label": "supplier threat-model age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "supplier threat-model age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_screen_lock_pct_08(record):
    """Evaluate supplier screen-lock compliance for control WP-0234-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_screen_lock_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-08", "metric": "supplier_screen_lock_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-08", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-08", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-08", "metric": "supplier_screen_lock_pct", "label": "supplier screen-lock compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier screen-lock compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_manual_override_count_09(record):
    """Evaluate supplier manual overrides for control WP-0234-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-09", "metric": "supplier_manual_override_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-09", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-09", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-09", "metric": "supplier_manual_override_count", "label": "supplier manual overrides",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier manual overrides must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_forecast_commitment_accuracy_pct_10(record):
    """Evaluate forecast commitment accuracy for control WP-0234-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_commitment_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-10", "metric": "supplier_forecast_commitment_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-10", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-10", "metric": "supplier_forecast_commitment_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-10", "metric": "supplier_forecast_commitment_accuracy_pct", "label": "forecast commitment accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "forecast commitment accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_dispatch_accuracy_pct_11(record):
    """Evaluate supplier dispatch accuracy for control WP-0234-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dispatch_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-11", "metric": "supplier_dispatch_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-11", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-11", "metric": "supplier_dispatch_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-11", "metric": "supplier_dispatch_accuracy_pct", "label": "supplier dispatch accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier dispatch accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_inventory_transfer_match_pct_12(record):
    """Evaluate inventory transfer match for control WP-0234-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_transfer_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-12", "metric": "supplier_inventory_transfer_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-12", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-12", "metric": "supplier_inventory_transfer_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-12", "metric": "supplier_inventory_transfer_match_pct", "label": "inventory transfer match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory transfer match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_inventory_value_13(record):
    """Evaluate inventory value for control WP-0234-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-13", "metric": "inventory_value",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-13", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-13", "metric": "inventory_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-13", "metric": "inventory_value", "label": "inventory value",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory value must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_label_error_count_14(record):
    """Evaluate label errors for control WP-0234-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-14", "metric": "label_error_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-14", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-14", "metric": "label_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-14", "metric": "label_error_count", "label": "label errors",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "label errors exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_concentration_pct_15(record):
    """Evaluate supplier concentration for control WP-0234-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concentration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-15", "metric": "supplier_concentration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-15", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-15", "metric": "supplier_concentration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-15", "metric": "supplier_concentration_pct", "label": "supplier concentration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "supplier concentration falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_invoice_match_pct_16(record):
    """Evaluate invoice match rate for control WP-0234-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-16", "metric": "invoice_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-16", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-16", "metric": "invoice_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-16", "metric": "invoice_match_pct", "label": "invoice match rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "invoice match rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_energy_kwh_per_order_17(record):
    """Evaluate energy per order for control WP-0234-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_kwh_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-17", "metric": "energy_kwh_per_order",
            "status": "insufficient_data",
            "severity": "high", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-17", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-17", "metric": "energy_kwh_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-17", "metric": "energy_kwh_per_order", "label": "energy per order",
        "status": "breach", "severity": "high", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "energy per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_batch_recall_trace_minutes_18(record):
    """Evaluate recall trace time for control WP-0234-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_recall_trace_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-18", "metric": "batch_recall_trace_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-18", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-18", "metric": "batch_recall_trace_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-18", "metric": "batch_recall_trace_minutes", "label": "recall trace time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "recall trace time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_data_retention_age_days_19(record):
    """Evaluate data retention age for control WP-0234-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_retention_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-19", "metric": "data_retention_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-19", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-19", "metric": "data_retention_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-19", "metric": "data_retention_age_days", "label": "data retention age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "data retention age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_hazmat_manifest_pct_20(record):
    """Evaluate hazmat manifest completion for control WP-0234-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-20", "metric": "hazmat_manifest_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-20", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-20", "metric": "hazmat_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-20", "metric": "hazmat_manifest_pct", "label": "hazmat manifest completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "hazmat manifest completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_address_correction_count_21(record):
    """Evaluate address corrections for control WP-0234-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("address_correction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-21", "metric": "address_correction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-21", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-21", "metric": "address_correction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-21", "metric": "address_correction_count", "label": "address corrections",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "address corrections must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_insulated_container_age_days_22(record):
    """Evaluate insulated container age for control WP-0234-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insulated_container_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-22", "metric": "insulated_container_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-22", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-22", "metric": "insulated_container_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-22", "metric": "insulated_container_age_days", "label": "insulated container age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "insulated container age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_technician_utilization_pct_23(record):
    """Evaluate technician utilization for control WP-0234-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("technician_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-23", "metric": "technician_utilization_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-23", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-23", "metric": "technician_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-23", "metric": "technician_utilization_pct", "label": "technician utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "technician utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_egress_route_obstruction_count_24(record):
    """Evaluate egress route obstructions for control WP-0234-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("egress_route_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0234-24", "metric": "egress_route_obstruction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0234-24", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0234-24", "metric": "egress_route_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0234-24", "metric": "egress_route_obstruction_count", "label": "egress route obstructions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "egress route obstructions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_ppap_approval_pct_01, assess_supplier_spill_response_drill_age_days_02, assess_supplier_ar_days_03, assess_supplier_training_refresh_days_04, assess_supplier_human_override_pct_05, assess_supplier_idempotency_violation_count_06, assess_supplier_threat_model_age_days_07, assess_supplier_screen_lock_pct_08, assess_supplier_manual_override_count_09, assess_supplier_forecast_commitment_accuracy_pct_10, assess_supplier_dispatch_accuracy_pct_11, assess_supplier_inventory_transfer_match_pct_12, assess_inventory_value_13, assess_label_error_count_14, assess_supplier_concentration_pct_15, assess_invoice_match_pct_16, assess_energy_kwh_per_order_17, assess_batch_recall_trace_minutes_18, assess_data_retention_age_days_19, assess_hazmat_manifest_pct_20, assess_address_correction_count_21, assess_insulated_container_age_days_22, assess_technician_utilization_pct_23, assess_egress_route_obstruction_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

