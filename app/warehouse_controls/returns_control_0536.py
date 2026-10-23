"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_detention_charge_hours_01(record):
    """Evaluate detention charge hours for control WP-0536-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("detention_charge_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-01", "metric": "detention_charge_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-01", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-01", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-01", "metric": "detention_charge_hours", "label": "detention charge hours",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "detention charge hours falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_driver_settlement_age_days_02(record):
    """Evaluate driver settlement age for control WP-0536-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_settlement_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-02", "metric": "driver_settlement_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-02", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-02", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-02", "metric": "driver_settlement_age_days", "label": "driver settlement age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver settlement age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_financial_risk_score_03(record):
    """Evaluate supplier financial risk for control WP-0536-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_financial_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-03", "metric": "supplier_financial_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-03", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-03", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-03", "metric": "supplier_financial_risk_score", "label": "supplier financial risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier financial risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_safety_incident_rate_04(record):
    """Evaluate supplier safety incident rate for control WP-0536-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_incident_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-04", "metric": "supplier_safety_incident_rate",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-04", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-04", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-04", "metric": "supplier_safety_incident_rate", "label": "supplier safety incident rate",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier safety incident rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_border_delay_hours_05(record):
    """Evaluate supplier border delay for control WP-0536-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_border_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-05", "metric": "supplier_border_delay_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-05", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-05", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-05", "metric": "supplier_border_delay_hours", "label": "supplier border delay",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier border delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_privacy_request_age_days_06(record):
    """Evaluate supplier privacy request age for control WP-0536-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-06", "metric": "supplier_privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-06", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-06", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-06", "metric": "supplier_privacy_request_age_days", "label": "supplier privacy request age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy request age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_inventory_turns_07(record):
    """Evaluate supplier inventory turns for control WP-0536-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_turns")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-07", "metric": "supplier_inventory_turns",
            "status": "insufficient_data",
            "severity": "high", "unit": "turns",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-07", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-07", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-07", "metric": "supplier_inventory_turns", "label": "supplier inventory turns",
        "status": "breach", "severity": "high", "unit": "turns",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier inventory turns must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_circularity_score_08(record):
    """Evaluate supplier circularity for control WP-0536-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_circularity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-08", "metric": "supplier_circularity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-08", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-08", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-08", "metric": "supplier_circularity_score", "label": "supplier circularity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier circularity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_data_latency_minutes_09(record):
    """Evaluate supplier data latency for control WP-0536-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-09", "metric": "supplier_data_latency_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-09", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-09", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-09", "metric": "supplier_data_latency_minutes", "label": "supplier data latency",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier data latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_nonconformance_age_days_10(record):
    """Evaluate supplier nonconformance age for control WP-0536-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_nonconformance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-10", "metric": "supplier_nonconformance_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-10", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-10", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-10", "metric": "supplier_nonconformance_age_days", "label": "supplier nonconformance age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier nonconformance age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_working_hours_violation_count_11(record):
    """Evaluate supplier working-hours violations for control WP-0536-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_hours_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-11", "metric": "supplier_working_hours_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-11", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-11", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-11", "metric": "supplier_working_hours_violation_count", "label": "supplier working-hours violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier working-hours violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_going_concern_signal_12(record):
    """Evaluate supplier going-concern signal for control WP-0536-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_going_concern_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-12", "metric": "supplier_going_concern_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-12", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-12", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-12", "metric": "supplier_going_concern_signal", "label": "supplier going-concern signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier going-concern signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_kpi_review_age_days_13(record):
    """Evaluate supplier KPI review age for control WP-0536-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-13", "metric": "supplier_kpi_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-13", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-13", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-13", "metric": "supplier_kpi_review_age_days", "label": "supplier KPI review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier KPI review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_vendor_model_license_days_left_14(record):
    """Evaluate supplier model-license validity for control WP-0536-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_model_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-14", "metric": "supplier_vendor_model_license_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-14", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-14", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-14", "metric": "supplier_vendor_model_license_days_left", "label": "supplier model-license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier model-license validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_observability_score_15(record):
    """Evaluate supplier observability score for control WP-0536-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-15", "metric": "supplier_observability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-15", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-15", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-15", "metric": "supplier_observability_score", "label": "supplier observability score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier observability score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_container_scan_pct_16(record):
    """Evaluate supplier container scan coverage for control WP-0536-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_container_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-16", "metric": "supplier_container_scan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-16", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-16", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-16", "metric": "supplier_container_scan_pct", "label": "supplier container scan coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier container scan coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_exception_approval_age_hours_17(record):
    """Evaluate supplier exception approval age for control WP-0536-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-17", "metric": "supplier_exception_approval_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-17", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-17", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-17", "metric": "supplier_exception_approval_age_hours", "label": "supplier exception approval age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier exception approval age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_duplicate_bank_signal_18(record):
    """Evaluate supplier duplicate-bank signal for control WP-0536-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_bank_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-18", "metric": "supplier_duplicate_bank_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-18", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-18", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-18", "metric": "supplier_duplicate_bank_signal", "label": "supplier duplicate-bank signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier duplicate-bank signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_schedule_exception_age_hours_19(record):
    """Evaluate schedule exception age for control WP-0536-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-19", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-19", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-19", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-19", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schedule exception age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_edi_mapping_age_days_20(record):
    """Evaluate supplier EDI mapping age for control WP-0536-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-20", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-20", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-20", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-20", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier EDI mapping age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_monitoring_handover_pct_21(record):
    """Evaluate supplier monitoring handover for control WP-0536-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-21", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-21", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-21", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-21", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier monitoring handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_shipment_age_hours_22(record):
    """Evaluate shipment age for control WP-0536-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-22", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-22", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-22", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-22", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "shipment age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_battery_pct_23(record):
    """Evaluate equipment battery for control WP-0536-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-23", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-23", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-23", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-23", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment battery must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_serial_capture_pct_24(record):
    """Evaluate serial capture for control WP-0536-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0536-24", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0536-24", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0536-24", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0536-24", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "serial capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_detention_charge_hours_01, assess_driver_settlement_age_days_02, assess_supplier_financial_risk_score_03, assess_supplier_safety_incident_rate_04, assess_supplier_border_delay_hours_05, assess_supplier_privacy_request_age_days_06, assess_supplier_inventory_turns_07, assess_supplier_circularity_score_08, assess_supplier_data_latency_minutes_09, assess_supplier_nonconformance_age_days_10, assess_supplier_working_hours_violation_count_11, assess_supplier_going_concern_signal_12, assess_supplier_kpi_review_age_days_13, assess_supplier_vendor_model_license_days_left_14, assess_supplier_observability_score_15, assess_supplier_container_scan_pct_16, assess_supplier_exception_approval_age_hours_17, assess_supplier_duplicate_bank_signal_18, assess_supplier_schedule_exception_age_hours_19, assess_supplier_edi_mapping_age_days_20, assess_supplier_monitoring_handover_pct_21, assess_shipment_age_hours_22, assess_battery_pct_23, assess_serial_capture_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

