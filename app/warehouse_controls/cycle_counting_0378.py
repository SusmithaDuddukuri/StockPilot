"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_parallel_run_days_01(record):
    """Evaluate supplier parallel run duration for control WP-0378-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_parallel_run_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-01", "metric": "supplier_parallel_run_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-01", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-01", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-01", "metric": "supplier_parallel_run_days", "label": "supplier parallel run duration",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier parallel run duration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_available_qty_02(record):
    """Evaluate available quantity for control WP-0378-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("available_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-02", "metric": "available_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-02", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-02", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-02", "metric": "available_qty", "label": "available quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 79, "comparison": "max",
        "finding": "available quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_dock_wait_minutes_03(record):
    """Evaluate dock waiting time for control WP-0378-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-03", "metric": "dock_wait_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-03", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-03", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-03", "metric": "dock_wait_minutes", "label": "dock waiting time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "dock waiting time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_route_deviation_km_04(record):
    """Evaluate route deviation for control WP-0378-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-04", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "medium", "unit": "km",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-04", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-04", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-04", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "medium", "unit": "km",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "route deviation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_data_quality_score_05(record):
    """Evaluate data quality for control WP-0378-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-05", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-05", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-05", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-05", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_refund_age_days_06(record):
    """Evaluate refund age for control WP-0378-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-06", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-06", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-06", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-06", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "refund age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_temperature_calibration_age_days_07(record):
    """Evaluate temperature calibration age for control WP-0378-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-07", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-07", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-07", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-07", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "temperature calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_form_error_pct_08(record):
    """Evaluate form error rate for control WP-0378-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-08", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-08", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-08", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-08", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "form error rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_sorter_missort_count_09(record):
    """Evaluate sorter missorts for control WP-0378-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-09", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-09", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-09", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-09", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sorter missorts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_tamper_signal_count_10(record):
    """Evaluate tamper signals for control WP-0378-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_signal_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-10", "metric": "tamper_signal_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-10", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-10", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-10", "metric": "tamper_signal_count", "label": "tamper signals",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "tamper signals exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_temperature_excursion_count_11(record):
    """Evaluate temperature excursions for control WP-0378-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_excursion_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-11", "metric": "temperature_excursion_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-11", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-11", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-11", "metric": "temperature_excursion_count", "label": "temperature excursions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "temperature excursions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_warranty_registration_pct_12(record):
    """Evaluate warranty registration for control WP-0378-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warranty_registration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-12", "metric": "warranty_registration_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-12", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-12", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-12", "metric": "warranty_registration_pct", "label": "warranty registration",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "warranty registration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_forklift_speed_violation_count_13(record):
    """Evaluate forklift speed violations for control WP-0378-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_speed_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-13", "metric": "forklift_speed_violation_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-13", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-13", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-13", "metric": "forklift_speed_violation_count", "label": "forklift speed violations",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forklift speed violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_sorter_utilization_pct_14(record):
    """Evaluate sorter utilization for control WP-0378-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-14", "metric": "sorter_utilization_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-14", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-14", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-14", "metric": "sorter_utilization_pct", "label": "sorter utilization",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "sorter utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_incident_postmortem_age_days_15(record):
    """Evaluate incident postmortem age for control WP-0378-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_postmortem_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-15", "metric": "incident_postmortem_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-15", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-15", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-15", "metric": "incident_postmortem_age_days", "label": "incident postmortem age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "incident postmortem age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_analytics_query_timeout_pct_16(record):
    """Evaluate analytics query timeout for control WP-0378-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("analytics_query_timeout_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-16", "metric": "analytics_query_timeout_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-16", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-16", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-16", "metric": "analytics_query_timeout_pct", "label": "analytics query timeout",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "analytics query timeout must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_product_recall_match_pct_17(record):
    """Evaluate product recall match for control WP-0378-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_recall_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-17", "metric": "product_recall_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-17", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-17", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-17", "metric": "product_recall_match_pct", "label": "product recall match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product recall match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_unload_rate_pallets_hour_18(record):
    """Evaluate unload rate for control WP-0378-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unload_rate_pallets_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-18", "metric": "unload_rate_pallets_hour",
            "status": "insufficient_data",
            "severity": "critical", "unit": "pallets/hour",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-18", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-18", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-18", "metric": "unload_rate_pallets_hour", "label": "unload rate",
        "status": "breach", "severity": "critical", "unit": "pallets/hour",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "unload rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_customer_refund_rate_pct_19(record):
    """Evaluate customer refund rate for control WP-0378-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_refund_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-19", "metric": "customer_refund_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-19", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-19", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-19", "metric": "customer_refund_rate_pct", "label": "customer refund rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "customer refund rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_empty_container_balance_20(record):
    """Evaluate empty container balance for control WP-0378-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_container_balance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-20", "metric": "empty_container_balance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "containers",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-20", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-20", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-20", "metric": "empty_container_balance", "label": "empty container balance",
        "status": "breach", "severity": "medium", "unit": "containers",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "empty container balance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_cost_per_order_21(record):
    """Evaluate cost per order for control WP-0378-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-21", "metric": "cost_per_order",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-21", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-21", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-21", "metric": "cost_per_order", "label": "cost per order",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cost per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_emissions_intensity_22(record):
    """Evaluate supplier emissions intensity for control WP-0378-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emissions_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-22", "metric": "supplier_emissions_intensity",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-22", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-22", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-22", "metric": "supplier_emissions_intensity", "label": "supplier emissions intensity",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier emissions intensity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_privacy_incident_count_23(record):
    """Evaluate supplier privacy incidents for control WP-0378-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-23", "metric": "supplier_privacy_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-23", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-23", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-23", "metric": "supplier_privacy_incident_count", "label": "supplier privacy incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "supplier privacy incidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_action_plan_completion_pct_24(record):
    """Evaluate supplier action-plan completion for control WP-0378-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0378-24", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0378-24", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0378-24", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0378-24", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier action-plan completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_parallel_run_days_01, assess_available_qty_02, assess_dock_wait_minutes_03, assess_route_deviation_km_04, assess_data_quality_score_05, assess_refund_age_days_06, assess_temperature_calibration_age_days_07, assess_form_error_pct_08, assess_sorter_missort_count_09, assess_tamper_signal_count_10, assess_temperature_excursion_count_11, assess_warranty_registration_pct_12, assess_forklift_speed_violation_count_13, assess_sorter_utilization_pct_14, assess_incident_postmortem_age_days_15, assess_analytics_query_timeout_pct_16, assess_product_recall_match_pct_17, assess_unload_rate_pallets_hour_18, assess_customer_refund_rate_pct_19, assess_empty_container_balance_20, assess_cost_per_order_21, assess_supplier_emissions_intensity_22, assess_supplier_privacy_incident_count_23, assess_supplier_action_plan_completion_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

