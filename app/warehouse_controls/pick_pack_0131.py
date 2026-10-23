"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_lot_traceability_pct_01(record):
    """Evaluate lot traceability for control WP-0131-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-01", "metric": "lot_traceability_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-01", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-01", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-01", "metric": "lot_traceability_pct", "label": "lot traceability",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lot traceability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_backorder_units_02(record):
    """Evaluate backordered units for control WP-0131-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backorder_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-02", "metric": "backorder_units",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-02", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-02", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-02", "metric": "backorder_units", "label": "backordered units",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backordered units must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_vehicle_inspection_age_days_03(record):
    """Evaluate vehicle inspection age for control WP-0131-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-03", "metric": "vehicle_inspection_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-03", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-03", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-03", "metric": "vehicle_inspection_age_days", "label": "vehicle inspection age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "vehicle inspection age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_credential_rotation_age_days_04(record):
    """Evaluate credential rotation age for control WP-0131-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credential_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-04", "metric": "credential_rotation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-04", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-04", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-04", "metric": "credential_rotation_age_days", "label": "credential rotation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "credential rotation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_work_queue_age_minutes_05(record):
    """Evaluate work queue age for control WP-0131-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("work_queue_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-05", "metric": "work_queue_age_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-05", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-05", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-05", "metric": "work_queue_age_minutes", "label": "work queue age",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "work queue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_first_aid_kit_check_age_days_06(record):
    """Evaluate first-aid kit check age for control WP-0131-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-06", "metric": "first_aid_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-06", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-06", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-06", "metric": "first_aid_kit_check_age_days", "label": "first-aid kit check age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "first-aid kit check age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_customer_notification_pct_07(record):
    """Evaluate customer notification for control WP-0131-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-07", "metric": "customer_notification_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-07", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-07", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-07", "metric": "customer_notification_pct", "label": "customer notification",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "customer notification exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_quarantine_release_age_hours_08(record):
    """Evaluate quarantine release age for control WP-0131-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quarantine_release_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-08", "metric": "quarantine_release_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-08", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-08", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-08", "metric": "quarantine_release_age_hours", "label": "quarantine release age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "quarantine release age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_battery_storage_temp_c_09(record):
    """Evaluate battery storage temperature for control WP-0131-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_storage_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-09", "metric": "battery_storage_temp_c",
            "status": "insufficient_data",
            "severity": "critical", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-09", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-09", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-09", "metric": "battery_storage_temp_c", "label": "battery storage temperature",
        "status": "breach", "severity": "critical", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery storage temperature must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_working_at_height_permit_pct_10(record):
    """Evaluate working-at-height permit compliance for control WP-0131-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("working_at_height_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-10", "metric": "working_at_height_permit_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-10", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-10", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-10", "metric": "working_at_height_permit_pct", "label": "working-at-height permit compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "working-at-height permit compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_generator_fuel_pct_11(record):
    """Evaluate generator fuel for control WP-0131-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-11", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-11", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-11", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-11", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "generator fuel exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_identity_sync_age_hours_12(record):
    """Evaluate identity sync age for control WP-0131-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-12", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-12", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-12", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-12", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "identity sync age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_weighing_error_pct_13(record):
    """Evaluate weighing error for control WP-0131-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-13", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-13", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-13", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-13", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "weighing error must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_cycle_count_completion_pct_14(record):
    """Evaluate cycle-count completion for control WP-0131-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-14", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-14", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-14", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-14", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cycle-count completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_pick_exception_rate_pct_15(record):
    """Evaluate pick exception rate for control WP-0131-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_exception_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-15", "metric": "pick_exception_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-15", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-15", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-15", "metric": "pick_exception_rate_pct", "label": "pick exception rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "pick exception rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_import_declaration_age_hours_16(record):
    """Evaluate import declaration age for control WP-0131-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-16", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-16", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-16", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-16", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "import declaration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_axle_load_variance_pct_17(record):
    """Evaluate axle load variance for control WP-0131-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-17", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-17", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-17", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-17", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "axle load variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_orders_per_labor_hour_18(record):
    """Evaluate orders per labor hour for control WP-0131-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orders_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-18", "metric": "orders_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "orders/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-18", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-18", "metric": "orders_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-18", "metric": "orders_per_labor_hour", "label": "orders per labor hour",
        "status": "breach", "severity": "low", "unit": "orders/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "orders per labor hour must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_claim_response_hours_19(record):
    """Evaluate supplier claim response time for control WP-0131-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_response_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-19", "metric": "supplier_claim_response_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-19", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-19", "metric": "supplier_claim_response_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-19", "metric": "supplier_claim_response_hours", "label": "supplier claim response time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "supplier claim response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_part_substitution_count_20(record):
    """Evaluate supplier part substitutions for control WP-0131-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_part_substitution_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-20", "metric": "supplier_part_substitution_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-20", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-20", "metric": "supplier_part_substitution_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-20", "metric": "supplier_part_substitution_count", "label": "supplier part substitutions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier part substitutions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_invoice_match_rate_pct_21(record):
    """Evaluate supplier invoice match for control WP-0131-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_match_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-21", "metric": "supplier_invoice_match_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-21", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-21", "metric": "supplier_invoice_match_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-21", "metric": "supplier_invoice_match_rate_pct", "label": "supplier invoice match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_escalation_age_hours_22(record):
    """Evaluate supplier escalation age for control WP-0131-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_escalation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-22", "metric": "supplier_escalation_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-22", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-22", "metric": "supplier_escalation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-22", "metric": "supplier_escalation_age_hours", "label": "supplier escalation age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier escalation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_sds_accuracy_pct_23(record):
    """Evaluate supplier SDS accuracy for control WP-0131-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sds_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-23", "metric": "supplier_sds_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-23", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-23", "metric": "supplier_sds_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-23", "metric": "supplier_sds_accuracy_pct", "label": "supplier SDS accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier SDS accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_cargo_security_score_24(record):
    """Evaluate supplier cargo security for control WP-0131-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cargo_security_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0131-24", "metric": "supplier_cargo_security_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0131-24", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0131-24", "metric": "supplier_cargo_security_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0131-24", "metric": "supplier_cargo_security_score", "label": "supplier cargo security",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier cargo security falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_lot_traceability_pct_01, assess_backorder_units_02, assess_vehicle_inspection_age_days_03, assess_credential_rotation_age_days_04, assess_work_queue_age_minutes_05, assess_first_aid_kit_check_age_days_06, assess_customer_notification_pct_07, assess_quarantine_release_age_hours_08, assess_battery_storage_temp_c_09, assess_working_at_height_permit_pct_10, assess_generator_fuel_pct_11, assess_identity_sync_age_hours_12, assess_weighing_error_pct_13, assess_cycle_count_completion_pct_14, assess_pick_exception_rate_pct_15, assess_import_declaration_age_hours_16, assess_axle_load_variance_pct_17, assess_orders_per_labor_hour_18, assess_supplier_claim_response_hours_19, assess_supplier_part_substitution_count_20, assess_supplier_invoice_match_rate_pct_21, assess_supplier_escalation_age_hours_22, assess_supplier_sds_accuracy_pct_23, assess_supplier_cargo_security_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

