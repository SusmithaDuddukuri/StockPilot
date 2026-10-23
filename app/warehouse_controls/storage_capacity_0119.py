"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_access_certification_pct_01(record):
    """Evaluate supplier access certification for control WP-0119-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_certification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-01", "metric": "supplier_access_certification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-01", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-01", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-01", "metric": "supplier_access_certification_pct", "label": "supplier access certification",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier access certification must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_round_sum_signal_02(record):
    """Evaluate supplier round-sum signal for control WP-0119-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_round_sum_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-02", "metric": "supplier_round_sum_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-02", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-02", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-02", "metric": "supplier_round_sum_signal", "label": "supplier round-sum signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier round-sum signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_schedule_ack_pct_03(record):
    """Evaluate schedule acknowledgement for control WP-0119-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-03", "metric": "supplier_schedule_ack_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-03", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-03", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-03", "metric": "supplier_schedule_ack_pct", "label": "schedule acknowledgement",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "schedule acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_asn_upload_age_hours_04(record):
    """Evaluate supplier ASN upload age for control WP-0119-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-04", "metric": "supplier_asn_upload_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-04", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-04", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-04", "metric": "supplier_asn_upload_age_hours", "label": "supplier ASN upload age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier ASN upload age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_endpoint_cutover_pct_05(record):
    """Evaluate supplier endpoint cutover for control WP-0119-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_endpoint_cutover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-05", "metric": "supplier_endpoint_cutover_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-05", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-05", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-05", "metric": "supplier_endpoint_cutover_pct", "label": "supplier endpoint cutover",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier endpoint cutover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_order_age_hours_06(record):
    """Evaluate order age for control WP-0119-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-06", "metric": "order_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-06", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-06", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-06", "metric": "order_age_hours", "label": "order age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "order age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_training_expiry_days_07(record):
    """Evaluate training validity for control WP-0119-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-07", "metric": "training_expiry_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-07", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-07", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-07", "metric": "training_expiry_days", "label": "training validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "training validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_lot_traceability_pct_08(record):
    """Evaluate lot traceability for control WP-0119-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-08", "metric": "lot_traceability_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-08", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-08", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-08", "metric": "lot_traceability_pct", "label": "lot traceability",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "lot traceability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_backorder_units_09(record):
    """Evaluate backordered units for control WP-0119-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backorder_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-09", "metric": "backorder_units",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-09", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-09", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-09", "metric": "backorder_units", "label": "backordered units",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backordered units must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_vehicle_inspection_age_days_10(record):
    """Evaluate vehicle inspection age for control WP-0119-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-10", "metric": "vehicle_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-10", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-10", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-10", "metric": "vehicle_inspection_age_days", "label": "vehicle inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_credential_rotation_age_days_11(record):
    """Evaluate credential rotation age for control WP-0119-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credential_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-11", "metric": "credential_rotation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-11", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-11", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-11", "metric": "credential_rotation_age_days", "label": "credential rotation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "credential rotation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_work_queue_age_minutes_12(record):
    """Evaluate work queue age for control WP-0119-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("work_queue_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-12", "metric": "work_queue_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-12", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-12", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-12", "metric": "work_queue_age_minutes", "label": "work queue age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "work queue age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_first_aid_kit_check_age_days_13(record):
    """Evaluate first-aid kit check age for control WP-0119-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-13", "metric": "first_aid_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-13", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-13", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-13", "metric": "first_aid_kit_check_age_days", "label": "first-aid kit check age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "first-aid kit check age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_customer_notification_pct_14(record):
    """Evaluate customer notification for control WP-0119-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-14", "metric": "customer_notification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-14", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-14", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-14", "metric": "customer_notification_pct", "label": "customer notification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer notification must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_quarantine_release_age_hours_15(record):
    """Evaluate quarantine release age for control WP-0119-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quarantine_release_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-15", "metric": "quarantine_release_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-15", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-15", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-15", "metric": "quarantine_release_age_hours", "label": "quarantine release age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "quarantine release age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_battery_storage_temp_c_16(record):
    """Evaluate battery storage temperature for control WP-0119-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_storage_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-16", "metric": "battery_storage_temp_c",
            "status": "insufficient_data",
            "severity": "high", "unit": "C",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-16", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-16", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-16", "metric": "battery_storage_temp_c", "label": "battery storage temperature",
        "status": "breach", "severity": "high", "unit": "C",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "battery storage temperature falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_working_at_height_permit_pct_17(record):
    """Evaluate working-at-height permit compliance for control WP-0119-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("working_at_height_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-17", "metric": "working_at_height_permit_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-17", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-17", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-17", "metric": "working_at_height_permit_pct", "label": "working-at-height permit compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "working-at-height permit compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_generator_fuel_pct_18(record):
    """Evaluate generator fuel for control WP-0119-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-18", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-18", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-18", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-18", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "generator fuel must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_identity_sync_age_hours_19(record):
    """Evaluate identity sync age for control WP-0119-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-19", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-19", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-19", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-19", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "identity sync age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_weighing_error_pct_20(record):
    """Evaluate weighing error for control WP-0119-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-20", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-20", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-20", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-20", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "weighing error falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_cycle_count_completion_pct_21(record):
    """Evaluate cycle-count completion for control WP-0119-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-21", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-21", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-21", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-21", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cycle-count completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_pick_exception_rate_pct_22(record):
    """Evaluate pick exception rate for control WP-0119-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_exception_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-22", "metric": "pick_exception_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-22", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-22", "metric": "pick_exception_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-22", "metric": "pick_exception_rate_pct", "label": "pick exception rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick exception rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_import_declaration_age_hours_23(record):
    """Evaluate import declaration age for control WP-0119-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("import_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-23", "metric": "import_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-23", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-23", "metric": "import_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-23", "metric": "import_declaration_age_hours", "label": "import declaration age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "import declaration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_axle_load_variance_pct_24(record):
    """Evaluate axle load variance for control WP-0119-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("axle_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0119-24", "metric": "axle_load_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0119-24", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0119-24", "metric": "axle_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0119-24", "metric": "axle_load_variance_pct", "label": "axle load variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "axle load variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_access_certification_pct_01, assess_supplier_round_sum_signal_02, assess_supplier_schedule_ack_pct_03, assess_supplier_asn_upload_age_hours_04, assess_supplier_endpoint_cutover_pct_05, assess_order_age_hours_06, assess_training_expiry_days_07, assess_lot_traceability_pct_08, assess_backorder_units_09, assess_vehicle_inspection_age_days_10, assess_credential_rotation_age_days_11, assess_work_queue_age_minutes_12, assess_first_aid_kit_check_age_days_13, assess_customer_notification_pct_14, assess_quarantine_release_age_hours_15, assess_battery_storage_temp_c_16, assess_working_at_height_permit_pct_17, assess_generator_fuel_pct_18, assess_identity_sync_age_hours_19, assess_weighing_error_pct_20, assess_cycle_count_completion_pct_21, assess_pick_exception_rate_pct_22, assess_import_declaration_age_hours_23, assess_axle_load_variance_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

