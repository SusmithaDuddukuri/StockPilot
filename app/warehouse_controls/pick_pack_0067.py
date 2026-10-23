"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_route_deviation_km_01(record):
    """Evaluate route deviation for control WP-0067-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-01", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "critical", "unit": "km",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-01", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-01", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-01", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "critical", "unit": "km",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "route deviation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_data_quality_score_02(record):
    """Evaluate data quality for control WP-0067-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-02", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-02", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-02", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-02", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_refund_age_days_03(record):
    """Evaluate refund age for control WP-0067-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-03", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-03", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-03", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-03", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "refund age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_temperature_calibration_age_days_04(record):
    """Evaluate temperature calibration age for control WP-0067-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-04", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-04", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-04", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-04", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "temperature calibration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_form_error_pct_05(record):
    """Evaluate form error rate for control WP-0067-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-05", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-05", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-05", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-05", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "form error rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_sorter_missort_count_06(record):
    """Evaluate sorter missorts for control WP-0067-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-06", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-06", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-06", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-06", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sorter missorts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_tamper_signal_count_07(record):
    """Evaluate tamper signals for control WP-0067-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_signal_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-07", "metric": "tamper_signal_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-07", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-07", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-07", "metric": "tamper_signal_count", "label": "tamper signals",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "tamper signals exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_temperature_excursion_count_08(record):
    """Evaluate temperature excursions for control WP-0067-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_excursion_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-08", "metric": "temperature_excursion_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-08", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-08", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-08", "metric": "temperature_excursion_count", "label": "temperature excursions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "temperature excursions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_warranty_registration_pct_09(record):
    """Evaluate warranty registration for control WP-0067-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warranty_registration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-09", "metric": "warranty_registration_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-09", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-09", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-09", "metric": "warranty_registration_pct", "label": "warranty registration",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "warranty registration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_forklift_speed_violation_count_10(record):
    """Evaluate forklift speed violations for control WP-0067-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_speed_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-10", "metric": "forklift_speed_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-10", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-10", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-10", "metric": "forklift_speed_violation_count", "label": "forklift speed violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forklift speed violations must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_sorter_utilization_pct_11(record):
    """Evaluate sorter utilization for control WP-0067-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-11", "metric": "sorter_utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-11", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-11", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-11", "metric": "sorter_utilization_pct", "label": "sorter utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "sorter utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_incident_postmortem_age_days_12(record):
    """Evaluate incident postmortem age for control WP-0067-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_postmortem_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-12", "metric": "incident_postmortem_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-12", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-12", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-12", "metric": "incident_postmortem_age_days", "label": "incident postmortem age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "incident postmortem age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_analytics_query_timeout_pct_13(record):
    """Evaluate analytics query timeout for control WP-0067-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("analytics_query_timeout_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-13", "metric": "analytics_query_timeout_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-13", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-13", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-13", "metric": "analytics_query_timeout_pct", "label": "analytics query timeout",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "analytics query timeout must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_product_recall_match_pct_14(record):
    """Evaluate product recall match for control WP-0067-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_recall_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-14", "metric": "product_recall_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-14", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-14", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-14", "metric": "product_recall_match_pct", "label": "product recall match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "product recall match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_unload_rate_pallets_hour_15(record):
    """Evaluate unload rate for control WP-0067-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unload_rate_pallets_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-15", "metric": "unload_rate_pallets_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "pallets/hour",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-15", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-15", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-15", "metric": "unload_rate_pallets_hour", "label": "unload rate",
        "status": "breach", "severity": "medium", "unit": "pallets/hour",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "unload rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_customer_refund_rate_pct_16(record):
    """Evaluate customer refund rate for control WP-0067-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_refund_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-16", "metric": "customer_refund_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-16", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-16", "metric": "customer_refund_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-16", "metric": "customer_refund_rate_pct", "label": "customer refund rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "customer refund rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_empty_container_balance_17(record):
    """Evaluate empty container balance for control WP-0067-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_container_balance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-17", "metric": "empty_container_balance",
            "status": "insufficient_data",
            "severity": "critical", "unit": "containers",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-17", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-17", "metric": "empty_container_balance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-17", "metric": "empty_container_balance", "label": "empty container balance",
        "status": "breach", "severity": "critical", "unit": "containers",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "empty container balance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_cost_per_order_18(record):
    """Evaluate cost per order for control WP-0067-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cost_per_order")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-18", "metric": "cost_per_order",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-18", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-18", "metric": "cost_per_order", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-18", "metric": "cost_per_order", "label": "cost per order",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cost per order must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_emissions_intensity_19(record):
    """Evaluate supplier emissions intensity for control WP-0067-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emissions_intensity")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-19", "metric": "supplier_emissions_intensity",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-19", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-19", "metric": "supplier_emissions_intensity", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-19", "metric": "supplier_emissions_intensity", "label": "supplier emissions intensity",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "supplier emissions intensity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_privacy_incident_count_20(record):
    """Evaluate supplier privacy incidents for control WP-0067-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-20", "metric": "supplier_privacy_incident_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-20", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-20", "metric": "supplier_privacy_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-20", "metric": "supplier_privacy_incident_count", "label": "supplier privacy incidents",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier privacy incidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_action_plan_completion_pct_21(record):
    """Evaluate supplier action-plan completion for control WP-0067-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_action_plan_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-21", "metric": "supplier_action_plan_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-21", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-21", "metric": "supplier_action_plan_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-21", "metric": "supplier_action_plan_completion_pct", "label": "supplier action-plan completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier action-plan completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_vulnerability_remediation_days_22(record):
    """Evaluate supplier vulnerability remediation time for control WP-0067-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vulnerability_remediation_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-22", "metric": "supplier_vulnerability_remediation_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-22", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-22", "metric": "supplier_vulnerability_remediation_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-22", "metric": "supplier_vulnerability_remediation_days", "label": "supplier vulnerability remediation time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier vulnerability remediation time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_labor_availability_pct_23(record):
    """Evaluate supplier labor availability for control WP-0067-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_availability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-23", "metric": "supplier_labor_availability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-23", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-23", "metric": "supplier_labor_availability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-23", "metric": "supplier_labor_availability_pct", "label": "supplier labor availability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier labor availability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_emission_audit_age_days_24(record):
    """Evaluate supplier emissions audit age for control WP-0067-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_emission_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0067-24", "metric": "supplier_emission_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0067-24", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0067-24", "metric": "supplier_emission_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0067-24", "metric": "supplier_emission_audit_age_days", "label": "supplier emissions audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier emissions audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_route_deviation_km_01, assess_data_quality_score_02, assess_refund_age_days_03, assess_temperature_calibration_age_days_04, assess_form_error_pct_05, assess_sorter_missort_count_06, assess_tamper_signal_count_07, assess_temperature_excursion_count_08, assess_warranty_registration_pct_09, assess_forklift_speed_violation_count_10, assess_sorter_utilization_pct_11, assess_incident_postmortem_age_days_12, assess_analytics_query_timeout_pct_13, assess_product_recall_match_pct_14, assess_unload_rate_pallets_hour_15, assess_customer_refund_rate_pct_16, assess_empty_container_balance_17, assess_cost_per_order_18, assess_supplier_emissions_intensity_19, assess_supplier_privacy_incident_count_20, assess_supplier_action_plan_completion_pct_21, assess_supplier_vulnerability_remediation_days_22, assess_supplier_labor_availability_pct_23, assess_supplier_emission_audit_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

