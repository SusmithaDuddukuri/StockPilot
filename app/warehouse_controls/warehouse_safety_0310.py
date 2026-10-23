"""Operational control pack for warehouse safety; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_control_mapping_pct_01(record):
    """Evaluate supplier control mapping for control WP-0310-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_mapping_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-01", "metric": "supplier_control_mapping_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-01", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-01", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-01", "metric": "supplier_control_mapping_pct", "label": "supplier control mapping",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control mapping must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_supplier_credit_note_match_pct_02(record):
    """Evaluate supplier credit-note match for control WP-0310-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-02", "metric": "supplier_credit_note_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-02", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-02", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-02", "metric": "supplier_credit_note_match_pct", "label": "supplier credit-note match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "supplier credit-note match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_supplier_inventory_accuracy_pct_03(record):
    """Evaluate supplier inventory accuracy for control WP-0310-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-03", "metric": "supplier_inventory_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-03", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-03", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-03", "metric": "supplier_inventory_accuracy_pct", "label": "supplier inventory accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier inventory accuracy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_supplier_parallel_run_days_04(record):
    """Evaluate supplier parallel run duration for control WP-0310-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_parallel_run_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-04", "metric": "supplier_parallel_run_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-04", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-04", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-04", "metric": "supplier_parallel_run_days", "label": "supplier parallel run duration",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier parallel run duration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_available_qty_05(record):
    """Evaluate available quantity for control WP-0310-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("available_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-05", "metric": "available_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-05", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-05", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-05", "metric": "available_qty", "label": "available quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "available quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_dock_wait_minutes_06(record):
    """Evaluate dock waiting time for control WP-0310-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-06", "metric": "dock_wait_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-06", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-06", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-06", "metric": "dock_wait_minutes", "label": "dock waiting time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "dock waiting time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_route_deviation_km_07(record):
    """Evaluate route deviation for control WP-0310-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-07", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "low", "unit": "km",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-07", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-07", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-07", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "low", "unit": "km",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "route deviation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_data_quality_score_08(record):
    """Evaluate data quality for control WP-0310-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-08", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-08", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-08", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-08", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "data quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_refund_age_days_09(record):
    """Evaluate refund age for control WP-0310-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-09", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-09", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-09", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-09", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "refund age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_temperature_calibration_age_days_10(record):
    """Evaluate temperature calibration age for control WP-0310-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-10", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-10", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-10", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-10", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "temperature calibration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_form_error_pct_11(record):
    """Evaluate form error rate for control WP-0310-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-11", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-11", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-11", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-11", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "form error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_sorter_missort_count_12(record):
    """Evaluate sorter missorts for control WP-0310-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-12", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-12", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-12", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-12", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sorter missorts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_tamper_signal_count_13(record):
    """Evaluate tamper signals for control WP-0310-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_signal_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-13", "metric": "tamper_signal_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-13", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-13", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-13", "metric": "tamper_signal_count", "label": "tamper signals",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "tamper signals must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_temperature_excursion_count_14(record):
    """Evaluate temperature excursions for control WP-0310-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_excursion_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-14", "metric": "temperature_excursion_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-14", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-14", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-14", "metric": "temperature_excursion_count", "label": "temperature excursions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "temperature excursions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_warranty_registration_pct_15(record):
    """Evaluate warranty registration for control WP-0310-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warranty_registration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-15", "metric": "warranty_registration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-15", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-15", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-15", "metric": "warranty_registration_pct", "label": "warranty registration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "warranty registration falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_forklift_speed_violation_count_16(record):
    """Evaluate forklift speed violations for control WP-0310-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_speed_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-16", "metric": "forklift_speed_violation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-16", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-16", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-16", "metric": "forklift_speed_violation_count", "label": "forklift speed violations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forklift speed violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_sorter_utilization_pct_17(record):
    """Evaluate sorter utilization for control WP-0310-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-17", "metric": "sorter_utilization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-17", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-17", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-17", "metric": "sorter_utilization_pct", "label": "sorter utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sorter utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_incident_postmortem_age_days_18(record):
    """Evaluate incident postmortem age for control WP-0310-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_postmortem_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-18", "metric": "incident_postmortem_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-18", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-18", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-18", "metric": "incident_postmortem_age_days", "label": "incident postmortem age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "incident postmortem age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_analytics_query_timeout_pct_19(record):
    """Evaluate analytics query timeout for control WP-0310-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("analytics_query_timeout_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-19", "metric": "analytics_query_timeout_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-19", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-19", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-19", "metric": "analytics_query_timeout_pct", "label": "analytics query timeout",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "analytics query timeout falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_product_recall_match_pct_20(record):
    """Evaluate product recall match for control WP-0310-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_recall_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-20", "metric": "product_recall_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-20", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-20", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-20", "metric": "product_recall_match_pct", "label": "product recall match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product recall match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

def assess_unload_rate_pallets_hour_21(record):
    """Evaluate unload rate for control WP-0310-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unload_rate_pallets_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-21", "metric": "unload_rate_pallets_hour",
            "status": "insufficient_data",
            "severity": "high", "unit": "pallets/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-21", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-21", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-21", "metric": "unload_rate_pallets_hour", "label": "unload rate",
        "status": "breach", "severity": "high", "unit": "pallets/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unload rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "warehouse safety",
    }

def assess_customer_refund_rate_pct_22(record):
    """Evaluate customer refund rate for control WP-0310-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_refund_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-22", "metric": "customer_refund_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 195,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-22", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-22", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 195
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-22", "metric": "customer_refund_rate_pct", "label": "customer refund rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 195, "comparison": "max",
        "finding": "customer refund rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "warehouse safety",
    }

def assess_empty_container_balance_23(record):
    """Evaluate empty container balance for control WP-0310-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_container_balance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-23", "metric": "empty_container_balance",
            "status": "insufficient_data",
            "severity": "low", "unit": "containers",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-23", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-23", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-23", "metric": "empty_container_balance", "label": "empty container balance",
        "status": "breach", "severity": "low", "unit": "containers",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "empty container balance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "warehouse safety",
    }

def assess_cost_per_order_24(record):
    """Evaluate cost per order for control WP-0310-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0310-24", "metric": "cost_per_order",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0310-24", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0310-24", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0310-24", "metric": "cost_per_order", "label": "cost per order",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cost per order must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "warehouse safety",
    }

RULES = (assess_supplier_control_mapping_pct_01, assess_supplier_credit_note_match_pct_02, assess_supplier_inventory_accuracy_pct_03, assess_supplier_parallel_run_days_04, assess_available_qty_05, assess_dock_wait_minutes_06, assess_route_deviation_km_07, assess_data_quality_score_08, assess_refund_age_days_09, assess_temperature_calibration_age_days_10, assess_form_error_pct_11, assess_sorter_missort_count_12, assess_tamper_signal_count_13, assess_temperature_excursion_count_14, assess_warranty_registration_pct_15, assess_forklift_speed_violation_count_16, assess_sorter_utilization_pct_17, assess_incident_postmortem_age_days_18, assess_analytics_query_timeout_pct_19, assess_product_recall_match_pct_20, assess_unload_rate_pallets_hour_21, assess_customer_refund_rate_pct_22, assess_empty_container_balance_23, assess_cost_per_order_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

