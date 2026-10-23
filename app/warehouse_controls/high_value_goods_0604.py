"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_safety_incident_rate_01(record):
    """Evaluate supplier safety incident rate for control WP-0604-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_incident_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-01", "metric": "supplier_safety_incident_rate",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-01", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-01", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-01", "metric": "supplier_safety_incident_rate", "label": "supplier safety incident rate",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier safety incident rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_border_delay_hours_02(record):
    """Evaluate supplier border delay for control WP-0604-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_border_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-02", "metric": "supplier_border_delay_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-02", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-02", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-02", "metric": "supplier_border_delay_hours", "label": "supplier border delay",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier border delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_privacy_request_age_days_03(record):
    """Evaluate supplier privacy request age for control WP-0604-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-03", "metric": "supplier_privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-03", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-03", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-03", "metric": "supplier_privacy_request_age_days", "label": "supplier privacy request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier privacy request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_inventory_turns_04(record):
    """Evaluate supplier inventory turns for control WP-0604-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_turns")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-04", "metric": "supplier_inventory_turns",
            "status": "insufficient_data",
            "severity": "critical", "unit": "turns",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-04", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-04", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-04", "metric": "supplier_inventory_turns", "label": "supplier inventory turns",
        "status": "breach", "severity": "critical", "unit": "turns",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier inventory turns exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_circularity_score_05(record):
    """Evaluate supplier circularity for control WP-0604-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_circularity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-05", "metric": "supplier_circularity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-05", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-05", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-05", "metric": "supplier_circularity_score", "label": "supplier circularity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier circularity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_data_latency_minutes_06(record):
    """Evaluate supplier data latency for control WP-0604-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-06", "metric": "supplier_data_latency_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-06", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-06", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-06", "metric": "supplier_data_latency_minutes", "label": "supplier data latency",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_nonconformance_age_days_07(record):
    """Evaluate supplier nonconformance age for control WP-0604-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_nonconformance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-07", "metric": "supplier_nonconformance_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-07", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-07", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-07", "metric": "supplier_nonconformance_age_days", "label": "supplier nonconformance age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier nonconformance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_working_hours_violation_count_08(record):
    """Evaluate supplier working-hours violations for control WP-0604-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_hours_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-08", "metric": "supplier_working_hours_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-08", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-08", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-08", "metric": "supplier_working_hours_violation_count", "label": "supplier working-hours violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "supplier working-hours violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_going_concern_signal_09(record):
    """Evaluate supplier going-concern signal for control WP-0604-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_going_concern_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-09", "metric": "supplier_going_concern_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-09", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-09", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-09", "metric": "supplier_going_concern_signal", "label": "supplier going-concern signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier going-concern signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_kpi_review_age_days_10(record):
    """Evaluate supplier KPI review age for control WP-0604-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-10", "metric": "supplier_kpi_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-10", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-10", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-10", "metric": "supplier_kpi_review_age_days", "label": "supplier KPI review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier KPI review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_vendor_model_license_days_left_11(record):
    """Evaluate supplier model-license validity for control WP-0604-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_model_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-11", "metric": "supplier_vendor_model_license_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-11", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-11", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-11", "metric": "supplier_vendor_model_license_days_left", "label": "supplier model-license validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model-license validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_observability_score_12(record):
    """Evaluate supplier observability score for control WP-0604-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-12", "metric": "supplier_observability_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-12", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-12", "metric": "supplier_observability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-12", "metric": "supplier_observability_score", "label": "supplier observability score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier observability score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_container_scan_pct_13(record):
    """Evaluate supplier container scan coverage for control WP-0604-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_container_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-13", "metric": "supplier_container_scan_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-13", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-13", "metric": "supplier_container_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-13", "metric": "supplier_container_scan_pct", "label": "supplier container scan coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier container scan coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_exception_approval_age_hours_14(record):
    """Evaluate supplier exception approval age for control WP-0604-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_exception_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-14", "metric": "supplier_exception_approval_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-14", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-14", "metric": "supplier_exception_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-14", "metric": "supplier_exception_approval_age_hours", "label": "supplier exception approval age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier exception approval age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_duplicate_bank_signal_15(record):
    """Evaluate supplier duplicate-bank signal for control WP-0604-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_bank_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-15", "metric": "supplier_duplicate_bank_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-15", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-15", "metric": "supplier_duplicate_bank_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-15", "metric": "supplier_duplicate_bank_signal", "label": "supplier duplicate-bank signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier duplicate-bank signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_schedule_exception_age_hours_16(record):
    """Evaluate schedule exception age for control WP-0604-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-16", "metric": "supplier_schedule_exception_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-16", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-16", "metric": "supplier_schedule_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-16", "metric": "supplier_schedule_exception_age_hours", "label": "schedule exception age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "schedule exception age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_edi_mapping_age_days_17(record):
    """Evaluate supplier EDI mapping age for control WP-0604-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_mapping_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-17", "metric": "supplier_edi_mapping_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-17", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-17", "metric": "supplier_edi_mapping_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-17", "metric": "supplier_edi_mapping_age_days", "label": "supplier EDI mapping age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "supplier EDI mapping age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_monitoring_handover_pct_18(record):
    """Evaluate supplier monitoring handover for control WP-0604-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_monitoring_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-18", "metric": "supplier_monitoring_handover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-18", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-18", "metric": "supplier_monitoring_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-18", "metric": "supplier_monitoring_handover_pct", "label": "supplier monitoring handover",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier monitoring handover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_shipment_age_hours_19(record):
    """Evaluate shipment age for control WP-0604-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-19", "metric": "shipment_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-19", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-19", "metric": "shipment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-19", "metric": "shipment_age_hours", "label": "shipment age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "shipment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_battery_pct_20(record):
    """Evaluate equipment battery for control WP-0604-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-20", "metric": "battery_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-20", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-20", "metric": "battery_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-20", "metric": "battery_pct", "label": "equipment battery",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "equipment battery exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_serial_capture_pct_21(record):
    """Evaluate serial capture for control WP-0604-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-21", "metric": "serial_capture_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-21", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-21", "metric": "serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-21", "metric": "serial_capture_pct", "label": "serial capture",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "serial capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_expedite_cost_22(record):
    """Evaluate expedite cost for control WP-0604-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("expedite_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-22", "metric": "expedite_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-22", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-22", "metric": "expedite_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-22", "metric": "expedite_cost", "label": "expedite cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "expedite cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_tire_pressure_variance_pct_23(record):
    """Evaluate tire pressure variance for control WP-0604-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tire_pressure_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-23", "metric": "tire_pressure_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-23", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-23", "metric": "tire_pressure_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-23", "metric": "tire_pressure_variance_pct", "label": "tire pressure variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "tire pressure variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_endpoint_patch_age_days_24(record):
    """Evaluate endpoint patch age for control WP-0604-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("endpoint_patch_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0604-24", "metric": "endpoint_patch_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0604-24", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0604-24", "metric": "endpoint_patch_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0604-24", "metric": "endpoint_patch_age_days", "label": "endpoint patch age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "endpoint patch age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_safety_incident_rate_01, assess_supplier_border_delay_hours_02, assess_supplier_privacy_request_age_days_03, assess_supplier_inventory_turns_04, assess_supplier_circularity_score_05, assess_supplier_data_latency_minutes_06, assess_supplier_nonconformance_age_days_07, assess_supplier_working_hours_violation_count_08, assess_supplier_going_concern_signal_09, assess_supplier_kpi_review_age_days_10, assess_supplier_vendor_model_license_days_left_11, assess_supplier_observability_score_12, assess_supplier_container_scan_pct_13, assess_supplier_exception_approval_age_hours_14, assess_supplier_duplicate_bank_signal_15, assess_supplier_schedule_exception_age_hours_16, assess_supplier_edi_mapping_age_days_17, assess_supplier_monitoring_handover_pct_18, assess_shipment_age_hours_19, assess_battery_pct_20, assess_serial_capture_pct_21, assess_expedite_cost_22, assess_tire_pressure_variance_pct_23, assess_endpoint_patch_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

