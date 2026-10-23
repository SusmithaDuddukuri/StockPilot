"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_dock_appointment_delay_minutes_01(record):
    """Evaluate dock appointment delay for control WP-0388-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_appointment_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-01", "metric": "dock_appointment_delay_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-01", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-01", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-01", "metric": "dock_appointment_delay_minutes", "label": "dock appointment delay",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "dock appointment delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_report_freshness_minutes_02(record):
    """Evaluate report freshness for control WP-0388-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_freshness_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-02", "metric": "report_freshness_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-02", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-02", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-02", "metric": "report_freshness_minutes", "label": "report freshness",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "report freshness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_wave_completion_pct_03(record):
    """Evaluate wave completion for control WP-0388-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("wave_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-03", "metric": "wave_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-03", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-03", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-03", "metric": "wave_completion_pct", "label": "wave completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "wave completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_door_forced_open_count_04(record):
    """Evaluate forced doors for control WP-0388-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-04", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-04", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-04", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-04", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "forced doors exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_refrigerant_leak_signal_05(record):
    """Evaluate refrigerant leak signal for control WP-0388-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-05", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-05", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-05", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-05", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "refrigerant leak signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_counterfeit_signal_score_06(record):
    """Evaluate counterfeit signal score for control WP-0388-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("counterfeit_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-06", "metric": "counterfeit_signal_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-06", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-06", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-06", "metric": "counterfeit_signal_score", "label": "counterfeit signal score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "counterfeit signal score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_confined_space_permit_pct_07(record):
    """Evaluate confined-space permit compliance for control WP-0388-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("confined_space_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-07", "metric": "confined_space_permit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-07", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-07", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-07", "metric": "confined_space_permit_pct", "label": "confined-space permit compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "confined-space permit compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_sensor_fault_count_08(record):
    """Evaluate sensor faults for control WP-0388-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_fault_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-08", "metric": "sensor_fault_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-08", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-08", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-08", "metric": "sensor_fault_count", "label": "sensor faults",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "sensor faults exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_deployment_failure_pct_09(record):
    """Evaluate deployment failure rate for control WP-0388-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deployment_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-09", "metric": "deployment_failure_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-09", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-09", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-09", "metric": "deployment_failure_pct", "label": "deployment failure rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "deployment failure rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_deletion_request_age_days_10(record):
    """Evaluate deletion request age for control WP-0388-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deletion_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-10", "metric": "deletion_request_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-10", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-10", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-10", "metric": "deletion_request_age_days", "label": "deletion request age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "deletion request age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_country_of_origin_gap_count_11(record):
    """Evaluate country-of-origin gaps for control WP-0388-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_of_origin_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-11", "metric": "country_of_origin_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-11", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-11", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-11", "metric": "country_of_origin_gap_count", "label": "country-of-origin gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "country-of-origin gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_asn_accuracy_pct_12(record):
    """Evaluate supplier ASN accuracy for control WP-0388-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-12", "metric": "supplier_asn_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-12", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-12", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-12", "metric": "supplier_asn_accuracy_pct", "label": "supplier ASN accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "supplier ASN accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_delivery_window_success_pct_13(record):
    """Evaluate delivery-window success for control WP-0388-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_window_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-13", "metric": "delivery_window_success_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-13", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-13", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-13", "metric": "delivery_window_success_pct", "label": "delivery-window success",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "delivery-window success falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_detention_charge_hours_14(record):
    """Evaluate detention charge hours for control WP-0388-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("detention_charge_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-14", "metric": "detention_charge_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-14", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-14", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-14", "metric": "detention_charge_hours", "label": "detention charge hours",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "detention charge hours must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_driver_settlement_age_days_15(record):
    """Evaluate driver settlement age for control WP-0388-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_settlement_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-15", "metric": "driver_settlement_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-15", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-15", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-15", "metric": "driver_settlement_age_days", "label": "driver settlement age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "driver settlement age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_financial_risk_score_16(record):
    """Evaluate supplier financial risk for control WP-0388-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_financial_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-16", "metric": "supplier_financial_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-16", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-16", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-16", "metric": "supplier_financial_risk_score", "label": "supplier financial risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "supplier financial risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_safety_incident_rate_17(record):
    """Evaluate supplier safety incident rate for control WP-0388-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_incident_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-17", "metric": "supplier_safety_incident_rate",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-17", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-17", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-17", "metric": "supplier_safety_incident_rate", "label": "supplier safety incident rate",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier safety incident rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_border_delay_hours_18(record):
    """Evaluate supplier border delay for control WP-0388-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_border_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-18", "metric": "supplier_border_delay_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-18", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-18", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-18", "metric": "supplier_border_delay_hours", "label": "supplier border delay",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier border delay must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_privacy_request_age_days_19(record):
    """Evaluate supplier privacy request age for control WP-0388-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-19", "metric": "supplier_privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-19", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-19", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-19", "metric": "supplier_privacy_request_age_days", "label": "supplier privacy request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier privacy request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_inventory_turns_20(record):
    """Evaluate supplier inventory turns for control WP-0388-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_turns")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-20", "metric": "supplier_inventory_turns",
            "status": "insufficient_data",
            "severity": "critical", "unit": "turns",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-20", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-20", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-20", "metric": "supplier_inventory_turns", "label": "supplier inventory turns",
        "status": "breach", "severity": "critical", "unit": "turns",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "supplier inventory turns exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_circularity_score_21(record):
    """Evaluate supplier circularity for control WP-0388-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_circularity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-21", "metric": "supplier_circularity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-21", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-21", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-21", "metric": "supplier_circularity_score", "label": "supplier circularity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier circularity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_data_latency_minutes_22(record):
    """Evaluate supplier data latency for control WP-0388-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-22", "metric": "supplier_data_latency_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-22", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-22", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-22", "metric": "supplier_data_latency_minutes", "label": "supplier data latency",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data latency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_nonconformance_age_days_23(record):
    """Evaluate supplier nonconformance age for control WP-0388-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_nonconformance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-23", "metric": "supplier_nonconformance_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-23", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-23", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-23", "metric": "supplier_nonconformance_age_days", "label": "supplier nonconformance age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier nonconformance age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_working_hours_violation_count_24(record):
    """Evaluate supplier working-hours violations for control WP-0388-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_hours_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0388-24", "metric": "supplier_working_hours_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0388-24", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0388-24", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0388-24", "metric": "supplier_working_hours_violation_count", "label": "supplier working-hours violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier working-hours violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_dock_appointment_delay_minutes_01, assess_report_freshness_minutes_02, assess_wave_completion_pct_03, assess_door_forced_open_count_04, assess_refrigerant_leak_signal_05, assess_counterfeit_signal_score_06, assess_confined_space_permit_pct_07, assess_sensor_fault_count_08, assess_deployment_failure_pct_09, assess_deletion_request_age_days_10, assess_country_of_origin_gap_count_11, assess_supplier_asn_accuracy_pct_12, assess_delivery_window_success_pct_13, assess_detention_charge_hours_14, assess_driver_settlement_age_days_15, assess_supplier_financial_risk_score_16, assess_supplier_safety_incident_rate_17, assess_supplier_border_delay_hours_18, assess_supplier_privacy_request_age_days_19, assess_supplier_inventory_turns_20, assess_supplier_circularity_score_21, assess_supplier_data_latency_minutes_22, assess_supplier_nonconformance_age_days_23, assess_supplier_working_hours_violation_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

