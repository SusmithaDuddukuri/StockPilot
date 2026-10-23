"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_door_forced_open_count_01(record):
    """Evaluate forced doors for control WP-0456-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-01", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-01", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-01", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-01", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "forced doors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_refrigerant_leak_signal_02(record):
    """Evaluate refrigerant leak signal for control WP-0456-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-02", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-02", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-02", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-02", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refrigerant leak signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_counterfeit_signal_score_03(record):
    """Evaluate counterfeit signal score for control WP-0456-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("counterfeit_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-03", "metric": "counterfeit_signal_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-03", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-03", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-03", "metric": "counterfeit_signal_score", "label": "counterfeit signal score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "counterfeit signal score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_confined_space_permit_pct_04(record):
    """Evaluate confined-space permit compliance for control WP-0456-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("confined_space_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-04", "metric": "confined_space_permit_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-04", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-04", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-04", "metric": "confined_space_permit_pct", "label": "confined-space permit compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "confined-space permit compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_sensor_fault_count_05(record):
    """Evaluate sensor faults for control WP-0456-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_fault_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-05", "metric": "sensor_fault_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-05", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-05", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-05", "metric": "sensor_fault_count", "label": "sensor faults",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "sensor faults falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_deployment_failure_pct_06(record):
    """Evaluate deployment failure rate for control WP-0456-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deployment_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-06", "metric": "deployment_failure_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-06", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-06", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-06", "metric": "deployment_failure_pct", "label": "deployment failure rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "deployment failure rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_deletion_request_age_days_07(record):
    """Evaluate deletion request age for control WP-0456-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deletion_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-07", "metric": "deletion_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-07", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-07", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-07", "metric": "deletion_request_age_days", "label": "deletion request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "deletion request age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_country_of_origin_gap_count_08(record):
    """Evaluate country-of-origin gaps for control WP-0456-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_of_origin_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-08", "metric": "country_of_origin_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-08", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-08", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-08", "metric": "country_of_origin_gap_count", "label": "country-of-origin gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "country-of-origin gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_asn_accuracy_pct_09(record):
    """Evaluate supplier ASN accuracy for control WP-0456-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-09", "metric": "supplier_asn_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-09", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-09", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-09", "metric": "supplier_asn_accuracy_pct", "label": "supplier ASN accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier ASN accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_delivery_window_success_pct_10(record):
    """Evaluate delivery-window success for control WP-0456-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_window_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-10", "metric": "delivery_window_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-10", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-10", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-10", "metric": "delivery_window_success_pct", "label": "delivery-window success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "delivery-window success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_detention_charge_hours_11(record):
    """Evaluate detention charge hours for control WP-0456-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("detention_charge_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-11", "metric": "detention_charge_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-11", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-11", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-11", "metric": "detention_charge_hours", "label": "detention charge hours",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "detention charge hours must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_driver_settlement_age_days_12(record):
    """Evaluate driver settlement age for control WP-0456-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_settlement_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-12", "metric": "driver_settlement_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-12", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-12", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-12", "metric": "driver_settlement_age_days", "label": "driver settlement age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "driver settlement age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_financial_risk_score_13(record):
    """Evaluate supplier financial risk for control WP-0456-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_financial_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-13", "metric": "supplier_financial_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-13", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-13", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-13", "metric": "supplier_financial_risk_score", "label": "supplier financial risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier financial risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_safety_incident_rate_14(record):
    """Evaluate supplier safety incident rate for control WP-0456-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_incident_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-14", "metric": "supplier_safety_incident_rate",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-14", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-14", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-14", "metric": "supplier_safety_incident_rate", "label": "supplier safety incident rate",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier safety incident rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_border_delay_hours_15(record):
    """Evaluate supplier border delay for control WP-0456-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_border_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-15", "metric": "supplier_border_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-15", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-15", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-15", "metric": "supplier_border_delay_hours", "label": "supplier border delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier border delay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_privacy_request_age_days_16(record):
    """Evaluate supplier privacy request age for control WP-0456-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-16", "metric": "supplier_privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-16", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-16", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-16", "metric": "supplier_privacy_request_age_days", "label": "supplier privacy request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier privacy request age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_inventory_turns_17(record):
    """Evaluate supplier inventory turns for control WP-0456-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_turns")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-17", "metric": "supplier_inventory_turns",
            "status": "insufficient_data",
            "severity": "low", "unit": "turns",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-17", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-17", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-17", "metric": "supplier_inventory_turns", "label": "supplier inventory turns",
        "status": "breach", "severity": "low", "unit": "turns",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier inventory turns falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_circularity_score_18(record):
    """Evaluate supplier circularity for control WP-0456-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_circularity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-18", "metric": "supplier_circularity_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-18", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-18", "metric": "supplier_circularity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-18", "metric": "supplier_circularity_score", "label": "supplier circularity",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier circularity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_data_latency_minutes_19(record):
    """Evaluate supplier data latency for control WP-0456-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-19", "metric": "supplier_data_latency_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-19", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-19", "metric": "supplier_data_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-19", "metric": "supplier_data_latency_minutes", "label": "supplier data latency",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_nonconformance_age_days_20(record):
    """Evaluate supplier nonconformance age for control WP-0456-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_nonconformance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-20", "metric": "supplier_nonconformance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-20", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-20", "metric": "supplier_nonconformance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-20", "metric": "supplier_nonconformance_age_days", "label": "supplier nonconformance age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier nonconformance age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_working_hours_violation_count_21(record):
    """Evaluate supplier working-hours violations for control WP-0456-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_hours_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-21", "metric": "supplier_working_hours_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-21", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-21", "metric": "supplier_working_hours_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-21", "metric": "supplier_working_hours_violation_count", "label": "supplier working-hours violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "supplier working-hours violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_going_concern_signal_22(record):
    """Evaluate supplier going-concern signal for control WP-0456-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_going_concern_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-22", "metric": "supplier_going_concern_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-22", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-22", "metric": "supplier_going_concern_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-22", "metric": "supplier_going_concern_signal", "label": "supplier going-concern signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier going-concern signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_kpi_review_age_days_23(record):
    """Evaluate supplier KPI review age for control WP-0456-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-23", "metric": "supplier_kpi_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-23", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-23", "metric": "supplier_kpi_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-23", "metric": "supplier_kpi_review_age_days", "label": "supplier KPI review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KPI review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_vendor_model_license_days_left_24(record):
    """Evaluate supplier model-license validity for control WP-0456-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_model_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0456-24", "metric": "supplier_vendor_model_license_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0456-24", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0456-24", "metric": "supplier_vendor_model_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0456-24", "metric": "supplier_vendor_model_license_days_left", "label": "supplier model-license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier model-license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_door_forced_open_count_01, assess_refrigerant_leak_signal_02, assess_counterfeit_signal_score_03, assess_confined_space_permit_pct_04, assess_sensor_fault_count_05, assess_deployment_failure_pct_06, assess_deletion_request_age_days_07, assess_country_of_origin_gap_count_08, assess_supplier_asn_accuracy_pct_09, assess_delivery_window_success_pct_10, assess_detention_charge_hours_11, assess_driver_settlement_age_days_12, assess_supplier_financial_risk_score_13, assess_supplier_safety_incident_rate_14, assess_supplier_border_delay_hours_15, assess_supplier_privacy_request_age_days_16, assess_supplier_inventory_turns_17, assess_supplier_circularity_score_18, assess_supplier_data_latency_minutes_19, assess_supplier_nonconformance_age_days_20, assess_supplier_working_hours_violation_count_21, assess_supplier_going_concern_signal_22, assess_supplier_kpi_review_age_days_23, assess_supplier_vendor_model_license_days_left_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

