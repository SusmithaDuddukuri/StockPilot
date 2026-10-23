"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_backlog_orders_01(record):
    """Evaluate order backlog for control WP-0065-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backlog_orders")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-01", "metric": "backlog_orders",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-01", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-01", "metric": "backlog_orders", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-01", "metric": "backlog_orders", "label": "order backlog",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "order backlog exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_equipment_downtime_hours_02(record):
    """Evaluate equipment downtime for control WP-0065-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_downtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-02", "metric": "equipment_downtime_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-02", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-02", "metric": "equipment_downtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-02", "metric": "equipment_downtime_hours", "label": "equipment downtime",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "equipment downtime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_access_review_age_days_03(record):
    """Evaluate access review age for control WP-0065-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-03", "metric": "access_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-03", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-03", "metric": "access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-03", "metric": "access_review_age_days", "label": "access review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "access review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_humidity_sensor_gap_minutes_04(record):
    """Evaluate humidity data gap for control WP-0065-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_sensor_gap_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-04", "metric": "humidity_sensor_gap_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-04", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-04", "metric": "humidity_sensor_gap_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-04", "metric": "humidity_sensor_gap_minutes", "label": "humidity data gap",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "humidity data gap must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_dock_appointment_delay_minutes_05(record):
    """Evaluate dock appointment delay for control WP-0065-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_appointment_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-05", "metric": "dock_appointment_delay_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-05", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-05", "metric": "dock_appointment_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-05", "metric": "dock_appointment_delay_minutes", "label": "dock appointment delay",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "dock appointment delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_report_freshness_minutes_06(record):
    """Evaluate report freshness for control WP-0065-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("report_freshness_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-06", "metric": "report_freshness_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-06", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-06", "metric": "report_freshness_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-06", "metric": "report_freshness_minutes", "label": "report freshness",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "report freshness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_wave_completion_pct_07(record):
    """Evaluate wave completion for control WP-0065-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("wave_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-07", "metric": "wave_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-07", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-07", "metric": "wave_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-07", "metric": "wave_completion_pct", "label": "wave completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "wave completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_door_forced_open_count_08(record):
    """Evaluate forced doors for control WP-0065-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("door_forced_open_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-08", "metric": "door_forced_open_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-08", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-08", "metric": "door_forced_open_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-08", "metric": "door_forced_open_count", "label": "forced doors",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forced doors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_refrigerant_leak_signal_09(record):
    """Evaluate refrigerant leak signal for control WP-0065-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refrigerant_leak_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-09", "metric": "refrigerant_leak_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-09", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-09", "metric": "refrigerant_leak_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-09", "metric": "refrigerant_leak_signal", "label": "refrigerant leak signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "refrigerant leak signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_counterfeit_signal_score_10(record):
    """Evaluate counterfeit signal score for control WP-0065-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("counterfeit_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-10", "metric": "counterfeit_signal_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-10", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-10", "metric": "counterfeit_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-10", "metric": "counterfeit_signal_score", "label": "counterfeit signal score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "counterfeit signal score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_confined_space_permit_pct_11(record):
    """Evaluate confined-space permit compliance for control WP-0065-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("confined_space_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-11", "metric": "confined_space_permit_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-11", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-11", "metric": "confined_space_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-11", "metric": "confined_space_permit_pct", "label": "confined-space permit compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "confined-space permit compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_sensor_fault_count_12(record):
    """Evaluate sensor faults for control WP-0065-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sensor_fault_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-12", "metric": "sensor_fault_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-12", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-12", "metric": "sensor_fault_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-12", "metric": "sensor_fault_count", "label": "sensor faults",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sensor faults must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_deployment_failure_pct_13(record):
    """Evaluate deployment failure rate for control WP-0065-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deployment_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-13", "metric": "deployment_failure_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-13", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-13", "metric": "deployment_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-13", "metric": "deployment_failure_pct", "label": "deployment failure rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "deployment failure rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_deletion_request_age_days_14(record):
    """Evaluate deletion request age for control WP-0065-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("deletion_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-14", "metric": "deletion_request_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-14", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-14", "metric": "deletion_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-14", "metric": "deletion_request_age_days", "label": "deletion request age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "deletion request age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_country_of_origin_gap_count_15(record):
    """Evaluate country-of-origin gaps for control WP-0065-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_of_origin_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-15", "metric": "country_of_origin_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-15", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-15", "metric": "country_of_origin_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-15", "metric": "country_of_origin_gap_count", "label": "country-of-origin gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "country-of-origin gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_asn_accuracy_pct_16(record):
    """Evaluate supplier ASN accuracy for control WP-0065-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-16", "metric": "supplier_asn_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-16", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-16", "metric": "supplier_asn_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-16", "metric": "supplier_asn_accuracy_pct", "label": "supplier ASN accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ASN accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_delivery_window_success_pct_17(record):
    """Evaluate delivery-window success for control WP-0065-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("delivery_window_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-17", "metric": "delivery_window_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-17", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-17", "metric": "delivery_window_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-17", "metric": "delivery_window_success_pct", "label": "delivery-window success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "delivery-window success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_detention_charge_hours_18(record):
    """Evaluate detention charge hours for control WP-0065-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("detention_charge_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-18", "metric": "detention_charge_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-18", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-18", "metric": "detention_charge_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-18", "metric": "detention_charge_hours", "label": "detention charge hours",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "detention charge hours falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_driver_settlement_age_days_19(record):
    """Evaluate driver settlement age for control WP-0065-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_settlement_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-19", "metric": "driver_settlement_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-19", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-19", "metric": "driver_settlement_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-19", "metric": "driver_settlement_age_days", "label": "driver settlement age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver settlement age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_financial_risk_score_20(record):
    """Evaluate supplier financial risk for control WP-0065-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_financial_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-20", "metric": "supplier_financial_risk_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-20", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-20", "metric": "supplier_financial_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-20", "metric": "supplier_financial_risk_score", "label": "supplier financial risk",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier financial risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_safety_incident_rate_21(record):
    """Evaluate supplier safety incident rate for control WP-0065-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_safety_incident_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-21", "metric": "supplier_safety_incident_rate",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-21", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-21", "metric": "supplier_safety_incident_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-21", "metric": "supplier_safety_incident_rate", "label": "supplier safety incident rate",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier safety incident rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_border_delay_hours_22(record):
    """Evaluate supplier border delay for control WP-0065-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_border_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-22", "metric": "supplier_border_delay_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-22", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-22", "metric": "supplier_border_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-22", "metric": "supplier_border_delay_hours", "label": "supplier border delay",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier border delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_privacy_request_age_days_23(record):
    """Evaluate supplier privacy request age for control WP-0065-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_request_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-23", "metric": "supplier_privacy_request_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-23", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-23", "metric": "supplier_privacy_request_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-23", "metric": "supplier_privacy_request_age_days", "label": "supplier privacy request age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy request age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_inventory_turns_24(record):
    """Evaluate supplier inventory turns for control WP-0065-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_turns")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0065-24", "metric": "supplier_inventory_turns",
            "status": "insufficient_data",
            "severity": "low", "unit": "turns",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0065-24", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0065-24", "metric": "supplier_inventory_turns", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0065-24", "metric": "supplier_inventory_turns", "label": "supplier inventory turns",
        "status": "breach", "severity": "low", "unit": "turns",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier inventory turns must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_backlog_orders_01, assess_equipment_downtime_hours_02, assess_access_review_age_days_03, assess_humidity_sensor_gap_minutes_04, assess_dock_appointment_delay_minutes_05, assess_report_freshness_minutes_06, assess_wave_completion_pct_07, assess_door_forced_open_count_08, assess_refrigerant_leak_signal_09, assess_counterfeit_signal_score_10, assess_confined_space_permit_pct_11, assess_sensor_fault_count_12, assess_deployment_failure_pct_13, assess_deletion_request_age_days_14, assess_country_of_origin_gap_count_15, assess_supplier_asn_accuracy_pct_16, assess_delivery_window_success_pct_17, assess_detention_charge_hours_18, assess_driver_settlement_age_days_19, assess_supplier_financial_risk_score_20, assess_supplier_safety_incident_rate_21, assess_supplier_border_delay_hours_22, assess_supplier_privacy_request_age_days_23, assess_supplier_inventory_turns_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

