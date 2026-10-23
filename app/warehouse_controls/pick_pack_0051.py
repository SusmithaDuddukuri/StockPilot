"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_ai_redteam_age_days_01(record):
    """Evaluate supplier AI red-team age for control WP-0051-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_redteam_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-01", "metric": "supplier_ai_redteam_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-01", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-01", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-01", "metric": "supplier_ai_redteam_age_days", "label": "supplier AI red-team age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier AI red-team age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_log_redaction_pct_02(record):
    """Evaluate supplier log redaction for control WP-0051-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_log_redaction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-02", "metric": "supplier_log_redaction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-02", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-02", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-02", "metric": "supplier_log_redaction_pct", "label": "supplier log redaction",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier log redaction must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_dynamic_analysis_age_days_03(record):
    """Evaluate supplier dynamic analysis age for control WP-0051-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dynamic_analysis_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-03", "metric": "supplier_dynamic_analysis_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-03", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-03", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-03", "metric": "supplier_dynamic_analysis_age_days", "label": "supplier dynamic analysis age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier dynamic analysis age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_access_certification_pct_04(record):
    """Evaluate supplier access certification for control WP-0051-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_certification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-04", "metric": "supplier_access_certification_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-04", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-04", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-04", "metric": "supplier_access_certification_pct", "label": "supplier access certification",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "supplier access certification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_round_sum_signal_05(record):
    """Evaluate supplier round-sum signal for control WP-0051-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_round_sum_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-05", "metric": "supplier_round_sum_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-05", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-05", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-05", "metric": "supplier_round_sum_signal", "label": "supplier round-sum signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier round-sum signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_schedule_ack_pct_06(record):
    """Evaluate schedule acknowledgement for control WP-0051-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-06", "metric": "supplier_schedule_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-06", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-06", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-06", "metric": "supplier_schedule_ack_pct", "label": "schedule acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "schedule acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_asn_upload_age_hours_07(record):
    """Evaluate supplier ASN upload age for control WP-0051-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-07", "metric": "supplier_asn_upload_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-07", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-07", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-07", "metric": "supplier_asn_upload_age_hours", "label": "supplier ASN upload age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "supplier ASN upload age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_endpoint_cutover_pct_08(record):
    """Evaluate supplier endpoint cutover for control WP-0051-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_endpoint_cutover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-08", "metric": "supplier_endpoint_cutover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-08", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-08", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-08", "metric": "supplier_endpoint_cutover_pct", "label": "supplier endpoint cutover",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier endpoint cutover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_order_age_hours_09(record):
    """Evaluate order age for control WP-0051-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-09", "metric": "order_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-09", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-09", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-09", "metric": "order_age_hours", "label": "order age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_training_expiry_days_10(record):
    """Evaluate training validity for control WP-0051-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-10", "metric": "training_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-10", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-10", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-10", "metric": "training_expiry_days", "label": "training validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "training validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_lot_traceability_pct_11(record):
    """Evaluate lot traceability for control WP-0051-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-11", "metric": "lot_traceability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-11", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-11", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-11", "metric": "lot_traceability_pct", "label": "lot traceability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "lot traceability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_backorder_units_12(record):
    """Evaluate backordered units for control WP-0051-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backorder_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-12", "metric": "backorder_units",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-12", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-12", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-12", "metric": "backorder_units", "label": "backordered units",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "backordered units falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_vehicle_inspection_age_days_13(record):
    """Evaluate vehicle inspection age for control WP-0051-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-13", "metric": "vehicle_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-13", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-13", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-13", "metric": "vehicle_inspection_age_days", "label": "vehicle inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle inspection age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_credential_rotation_age_days_14(record):
    """Evaluate credential rotation age for control WP-0051-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credential_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-14", "metric": "credential_rotation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-14", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-14", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-14", "metric": "credential_rotation_age_days", "label": "credential rotation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "credential rotation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_work_queue_age_minutes_15(record):
    """Evaluate work queue age for control WP-0051-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("work_queue_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-15", "metric": "work_queue_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-15", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-15", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-15", "metric": "work_queue_age_minutes", "label": "work queue age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "work queue age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_first_aid_kit_check_age_days_16(record):
    """Evaluate first-aid kit check age for control WP-0051-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("first_aid_kit_check_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-16", "metric": "first_aid_kit_check_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-16", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-16", "metric": "first_aid_kit_check_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-16", "metric": "first_aid_kit_check_age_days", "label": "first-aid kit check age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "first-aid kit check age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_customer_notification_pct_17(record):
    """Evaluate customer notification for control WP-0051-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_notification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-17", "metric": "customer_notification_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-17", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-17", "metric": "customer_notification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-17", "metric": "customer_notification_pct", "label": "customer notification",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer notification must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_quarantine_release_age_hours_18(record):
    """Evaluate quarantine release age for control WP-0051-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quarantine_release_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-18", "metric": "quarantine_release_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-18", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-18", "metric": "quarantine_release_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-18", "metric": "quarantine_release_age_hours", "label": "quarantine release age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "quarantine release age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_battery_storage_temp_c_19(record):
    """Evaluate battery storage temperature for control WP-0051-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_storage_temp_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-19", "metric": "battery_storage_temp_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-19", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-19", "metric": "battery_storage_temp_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-19", "metric": "battery_storage_temp_c", "label": "battery storage temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "battery storage temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_working_at_height_permit_pct_20(record):
    """Evaluate working-at-height permit compliance for control WP-0051-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("working_at_height_permit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-20", "metric": "working_at_height_permit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-20", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-20", "metric": "working_at_height_permit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-20", "metric": "working_at_height_permit_pct", "label": "working-at-height permit compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "working-at-height permit compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_generator_fuel_pct_21(record):
    """Evaluate generator fuel for control WP-0051-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("generator_fuel_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-21", "metric": "generator_fuel_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-21", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-21", "metric": "generator_fuel_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-21", "metric": "generator_fuel_pct", "label": "generator fuel",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "generator fuel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_identity_sync_age_hours_22(record):
    """Evaluate identity sync age for control WP-0051-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("identity_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-22", "metric": "identity_sync_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-22", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-22", "metric": "identity_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-22", "metric": "identity_sync_age_hours", "label": "identity sync age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "identity sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_weighing_error_pct_23(record):
    """Evaluate weighing error for control WP-0051-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("weighing_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-23", "metric": "weighing_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-23", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-23", "metric": "weighing_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-23", "metric": "weighing_error_pct", "label": "weighing error",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "weighing error exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_cycle_count_completion_pct_24(record):
    """Evaluate cycle-count completion for control WP-0051-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cycle_count_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0051-24", "metric": "cycle_count_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0051-24", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0051-24", "metric": "cycle_count_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0051-24", "metric": "cycle_count_completion_pct", "label": "cycle-count completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "cycle-count completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_ai_redteam_age_days_01, assess_supplier_log_redaction_pct_02, assess_supplier_dynamic_analysis_age_days_03, assess_supplier_access_certification_pct_04, assess_supplier_round_sum_signal_05, assess_supplier_schedule_ack_pct_06, assess_supplier_asn_upload_age_hours_07, assess_supplier_endpoint_cutover_pct_08, assess_order_age_hours_09, assess_training_expiry_days_10, assess_lot_traceability_pct_11, assess_backorder_units_12, assess_vehicle_inspection_age_days_13, assess_credential_rotation_age_days_14, assess_work_queue_age_minutes_15, assess_first_aid_kit_check_age_days_16, assess_customer_notification_pct_17, assess_quarantine_release_age_hours_18, assess_battery_storage_temp_c_19, assess_working_at_height_permit_pct_20, assess_generator_fuel_pct_21, assess_identity_sync_age_hours_22, assess_weighing_error_pct_23, assess_cycle_count_completion_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

