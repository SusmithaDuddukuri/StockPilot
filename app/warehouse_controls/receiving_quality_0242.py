"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_dependency_update_age_days_01(record):
    """Evaluate supplier dependency update age for control WP-0242-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_update_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-01", "metric": "supplier_dependency_update_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-01", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-01", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-01", "metric": "supplier_dependency_update_age_days", "label": "supplier dependency update age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier dependency update age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_scim_sync_age_hours_02(record):
    """Evaluate supplier SCIM sync age for control WP-0242-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scim_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-02", "metric": "supplier_scim_sync_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-02", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-02", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-02", "metric": "supplier_scim_sync_age_hours", "label": "supplier SCIM sync age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier SCIM sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_deletion_verification_pct_03(record):
    """Evaluate supplier deletion verification for control WP-0242-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_deletion_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-03", "metric": "supplier_deletion_verification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-03", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-03", "metric": "supplier_deletion_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-03", "metric": "supplier_deletion_verification_pct", "label": "supplier deletion verification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier deletion verification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_control_mapping_pct_04(record):
    """Evaluate supplier control mapping for control WP-0242-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_mapping_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-04", "metric": "supplier_control_mapping_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-04", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-04", "metric": "supplier_control_mapping_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-04", "metric": "supplier_control_mapping_pct", "label": "supplier control mapping",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier control mapping must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_credit_note_match_pct_05(record):
    """Evaluate supplier credit-note match for control WP-0242-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_note_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-05", "metric": "supplier_credit_note_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-05", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-05", "metric": "supplier_credit_note_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-05", "metric": "supplier_credit_note_match_pct", "label": "supplier credit-note match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit-note match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_inventory_accuracy_pct_06(record):
    """Evaluate supplier inventory accuracy for control WP-0242-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_inventory_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-06", "metric": "supplier_inventory_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-06", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-06", "metric": "supplier_inventory_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-06", "metric": "supplier_inventory_accuracy_pct", "label": "supplier inventory accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier inventory accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_parallel_run_days_07(record):
    """Evaluate supplier parallel run duration for control WP-0242-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_parallel_run_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-07", "metric": "supplier_parallel_run_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-07", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-07", "metric": "supplier_parallel_run_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-07", "metric": "supplier_parallel_run_days", "label": "supplier parallel run duration",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier parallel run duration falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_available_qty_08(record):
    """Evaluate available quantity for control WP-0242-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("available_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-08", "metric": "available_qty",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-08", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-08", "metric": "available_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-08", "metric": "available_qty", "label": "available quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "available quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_dock_wait_minutes_09(record):
    """Evaluate dock waiting time for control WP-0242-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dock_wait_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-09", "metric": "dock_wait_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-09", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-09", "metric": "dock_wait_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-09", "metric": "dock_wait_minutes", "label": "dock waiting time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dock waiting time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_route_deviation_km_10(record):
    """Evaluate route deviation for control WP-0242-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("route_deviation_km")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-10", "metric": "route_deviation_km",
            "status": "insufficient_data",
            "severity": "critical", "unit": "km",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-10", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-10", "metric": "route_deviation_km", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-10", "metric": "route_deviation_km", "label": "route deviation",
        "status": "breach", "severity": "critical", "unit": "km",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "route deviation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_data_quality_score_11(record):
    """Evaluate data quality for control WP-0242-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-11", "metric": "data_quality_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-11", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-11", "metric": "data_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-11", "metric": "data_quality_score", "label": "data quality",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "data quality falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_refund_age_days_12(record):
    """Evaluate refund age for control WP-0242-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-12", "metric": "refund_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-12", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-12", "metric": "refund_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-12", "metric": "refund_age_days", "label": "refund age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refund age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_temperature_calibration_age_days_13(record):
    """Evaluate temperature calibration age for control WP-0242-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-13", "metric": "temperature_calibration_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-13", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-13", "metric": "temperature_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-13", "metric": "temperature_calibration_age_days", "label": "temperature calibration age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "temperature calibration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_form_error_pct_14(record):
    """Evaluate form error rate for control WP-0242-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("form_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-14", "metric": "form_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-14", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-14", "metric": "form_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-14", "metric": "form_error_pct", "label": "form error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "form error rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_sorter_missort_count_15(record):
    """Evaluate sorter missorts for control WP-0242-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_missort_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-15", "metric": "sorter_missort_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-15", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-15", "metric": "sorter_missort_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-15", "metric": "sorter_missort_count", "label": "sorter missorts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "sorter missorts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_tamper_signal_count_16(record):
    """Evaluate tamper signals for control WP-0242-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tamper_signal_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-16", "metric": "tamper_signal_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-16", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-16", "metric": "tamper_signal_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-16", "metric": "tamper_signal_count", "label": "tamper signals",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "tamper signals must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_temperature_excursion_count_17(record):
    """Evaluate temperature excursions for control WP-0242-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_excursion_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-17", "metric": "temperature_excursion_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-17", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-17", "metric": "temperature_excursion_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-17", "metric": "temperature_excursion_count", "label": "temperature excursions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "temperature excursions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_warranty_registration_pct_18(record):
    """Evaluate warranty registration for control WP-0242-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("warranty_registration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-18", "metric": "warranty_registration_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-18", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-18", "metric": "warranty_registration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-18", "metric": "warranty_registration_pct", "label": "warranty registration",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "warranty registration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_forklift_speed_violation_count_19(record):
    """Evaluate forklift speed violations for control WP-0242-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_speed_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-19", "metric": "forklift_speed_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-19", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-19", "metric": "forklift_speed_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-19", "metric": "forklift_speed_violation_count", "label": "forklift speed violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "forklift speed violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_sorter_utilization_pct_20(record):
    """Evaluate sorter utilization for control WP-0242-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sorter_utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-20", "metric": "sorter_utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-20", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-20", "metric": "sorter_utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-20", "metric": "sorter_utilization_pct", "label": "sorter utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sorter utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_incident_postmortem_age_days_21(record):
    """Evaluate incident postmortem age for control WP-0242-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_postmortem_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-21", "metric": "incident_postmortem_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-21", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-21", "metric": "incident_postmortem_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-21", "metric": "incident_postmortem_age_days", "label": "incident postmortem age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incident postmortem age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_analytics_query_timeout_pct_22(record):
    """Evaluate analytics query timeout for control WP-0242-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("analytics_query_timeout_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-22", "metric": "analytics_query_timeout_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-22", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-22", "metric": "analytics_query_timeout_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-22", "metric": "analytics_query_timeout_pct", "label": "analytics query timeout",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "analytics query timeout exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_product_recall_match_pct_23(record):
    """Evaluate product recall match for control WP-0242-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_recall_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-23", "metric": "product_recall_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-23", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-23", "metric": "product_recall_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-23", "metric": "product_recall_match_pct", "label": "product recall match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "product recall match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_unload_rate_pallets_hour_24(record):
    """Evaluate unload rate for control WP-0242-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("unload_rate_pallets_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0242-24", "metric": "unload_rate_pallets_hour",
            "status": "insufficient_data",
            "severity": "medium", "unit": "pallets/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0242-24", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0242-24", "metric": "unload_rate_pallets_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0242-24", "metric": "unload_rate_pallets_hour", "label": "unload rate",
        "status": "breach", "severity": "medium", "unit": "pallets/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "unload rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_supplier_dependency_update_age_days_01, assess_supplier_scim_sync_age_hours_02, assess_supplier_deletion_verification_pct_03, assess_supplier_control_mapping_pct_04, assess_supplier_credit_note_match_pct_05, assess_supplier_inventory_accuracy_pct_06, assess_supplier_parallel_run_days_07, assess_available_qty_08, assess_dock_wait_minutes_09, assess_route_deviation_km_10, assess_data_quality_score_11, assess_refund_age_days_12, assess_temperature_calibration_age_days_13, assess_form_error_pct_14, assess_sorter_missort_count_15, assess_tamper_signal_count_16, assess_temperature_excursion_count_17, assess_warranty_registration_pct_18, assess_forklift_speed_violation_count_19, assess_sorter_utilization_pct_20, assess_incident_postmortem_age_days_21, assess_analytics_query_timeout_pct_22, assess_product_recall_match_pct_23, assess_unload_rate_pallets_hour_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

