"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_incident_ack_minutes_01(record):
    """Evaluate incident acknowledgement for control WP-0136-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-01", "metric": "incident_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-01", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-01", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-01", "metric": "incident_ack_minutes", "label": "incident acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "incident acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_forecast_bias_pct_02(record):
    """Evaluate forecast bias for control WP-0136-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_bias_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-02", "metric": "forecast_bias_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-02", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-02", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-02", "metric": "forecast_bias_pct", "label": "forecast bias",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast bias must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_cold_exposure_minutes_03(record):
    """Evaluate cold exposure for control WP-0136-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_exposure_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-03", "metric": "cold_exposure_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-03", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-03", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-03", "metric": "cold_exposure_minutes", "label": "cold exposure",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cold exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_credit_age_days_04(record):
    """Evaluate supplier credit age for control WP-0136-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-04", "metric": "supplier_credit_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-04", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-04", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-04", "metric": "supplier_credit_age_days", "label": "supplier credit age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier credit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_recall_drill_age_days_05(record):
    """Evaluate recall drill age for control WP-0136-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-05", "metric": "recall_drill_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-05", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-05", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-05", "metric": "recall_drill_age_days", "label": "recall drill age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "recall drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_dangerous_goods_declaration_pct_06(record):
    """Evaluate dangerous goods declaration for control WP-0136-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dangerous_goods_declaration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-06", "metric": "dangerous_goods_declaration_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-06", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-06", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-06", "metric": "dangerous_goods_declaration_pct", "label": "dangerous goods declaration",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dangerous goods declaration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_safety_walk_age_days_07(record):
    """Evaluate safety walk age for control WP-0136-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_walk_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-07", "metric": "safety_walk_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-07", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-07", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-07", "metric": "safety_walk_age_days", "label": "safety walk age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "safety walk age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_emergency_alarm_test_age_days_08(record):
    """Evaluate emergency alarm test age for control WP-0136-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_alarm_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-08", "metric": "emergency_alarm_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-08", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-08", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-08", "metric": "emergency_alarm_test_age_days", "label": "emergency alarm test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "emergency alarm test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_software_bill_of_materials_age_days_09(record):
    """Evaluate SBOM age for control WP-0136-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("software_bill_of_materials_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-09", "metric": "software_bill_of_materials_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-09", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-09", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-09", "metric": "software_bill_of_materials_age_days", "label": "SBOM age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "SBOM age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_rfid_read_rate_pct_10(record):
    """Evaluate RFID read rate for control WP-0136-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-10", "metric": "rfid_read_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-10", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-10", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-10", "metric": "rfid_read_rate_pct", "label": "RFID read rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "RFID read rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_stock_age_median_days_11(record):
    """Evaluate median stock age for control WP-0136-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_median_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-11", "metric": "stock_age_median_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-11", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-11", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-11", "metric": "stock_age_median_days", "label": "median stock age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "median stock age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_packaging_damage_pct_12(record):
    """Evaluate packaging damage rate for control WP-0136-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-12", "metric": "packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-12", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-12", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-12", "metric": "packaging_damage_pct", "label": "packaging damage rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "packaging damage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_sanctions_screen_gap_count_13(record):
    """Evaluate sanctions screening gaps for control WP-0136-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sanctions_screen_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-13", "metric": "sanctions_screen_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-13", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-13", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-13", "metric": "sanctions_screen_gap_count", "label": "sanctions screening gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "sanctions screening gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_driver_training_age_days_14(record):
    """Evaluate driver training age for control WP-0136-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_training_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-14", "metric": "driver_training_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-14", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-14", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-14", "metric": "driver_training_age_days", "label": "driver training age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver training age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_automation_roi_pct_15(record):
    """Evaluate automation ROI for control WP-0136-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_roi_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-15", "metric": "automation_roi_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-15", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-15", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-15", "metric": "automation_roi_pct", "label": "automation ROI",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "automation ROI must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_license_days_left_16(record):
    """Evaluate supplier license validity for control WP-0136-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-16", "metric": "supplier_license_days_left",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-16", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-16", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-16", "metric": "supplier_license_days_left", "label": "supplier license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_root_cause_completeness_pct_17(record):
    """Evaluate supplier root-cause completeness for control WP-0136-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_root_cause_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-17", "metric": "supplier_root_cause_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-17", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-17", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-17", "metric": "supplier_root_cause_completeness_pct", "label": "supplier root-cause completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier root-cause completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_indexation_variance_pct_18(record):
    """Evaluate supplier indexation variance for control WP-0136-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_indexation_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-18", "metric": "supplier_indexation_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-18", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-18", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-18", "metric": "supplier_indexation_variance_pct", "label": "supplier indexation variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier indexation variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_document_version_gap_count_19(record):
    """Evaluate supplier document-version gaps for control WP-0136-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_version_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-19", "metric": "supplier_document_version_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-19", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-19", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-19", "metric": "supplier_document_version_gap_count", "label": "supplier document-version gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier document-version gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_language_label_pct_20(record):
    """Evaluate supplier language-label compliance for control WP-0136-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_language_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-20", "metric": "supplier_language_label_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-20", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-20", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-20", "metric": "supplier_language_label_pct", "label": "supplier language-label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier language-label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_vehicle_cleanliness_pct_21(record):
    """Evaluate supplier vehicle cleanliness for control WP-0136-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vehicle_cleanliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-21", "metric": "supplier_vehicle_cleanliness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-21", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-21", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-21", "metric": "supplier_vehicle_cleanliness_pct", "label": "supplier vehicle cleanliness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "supplier vehicle cleanliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_product_change_approval_pct_22(record):
    """Evaluate supplier product-change approval for control WP-0136-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-22", "metric": "supplier_product_change_approval_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-22", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-22", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-22", "metric": "supplier_product_change_approval_pct", "label": "supplier product-change approval",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier product-change approval must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_battery_regulatory_pct_23(record):
    """Evaluate supplier battery regulation compliance for control WP-0136-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_battery_regulatory_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-23", "metric": "supplier_battery_regulatory_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-23", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-23", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-23", "metric": "supplier_battery_regulatory_pct", "label": "supplier battery regulation compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier battery regulation compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_invoice_bank_match_pct_24(record):
    """Evaluate supplier invoice-bank match for control WP-0136-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_bank_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0136-24", "metric": "supplier_invoice_bank_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0136-24", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0136-24", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0136-24", "metric": "supplier_invoice_bank_match_pct", "label": "supplier invoice-bank match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier invoice-bank match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_incident_ack_minutes_01, assess_forecast_bias_pct_02, assess_cold_exposure_minutes_03, assess_supplier_credit_age_days_04, assess_recall_drill_age_days_05, assess_dangerous_goods_declaration_pct_06, assess_safety_walk_age_days_07, assess_emergency_alarm_test_age_days_08, assess_software_bill_of_materials_age_days_09, assess_rfid_read_rate_pct_10, assess_stock_age_median_days_11, assess_packaging_damage_pct_12, assess_sanctions_screen_gap_count_13, assess_driver_training_age_days_14, assess_automation_roi_pct_15, assess_supplier_license_days_left_16, assess_supplier_root_cause_completeness_pct_17, assess_supplier_indexation_variance_pct_18, assess_supplier_document_version_gap_count_19, assess_supplier_language_label_pct_20, assess_supplier_vehicle_cleanliness_pct_21, assess_supplier_product_change_approval_pct_22, assess_supplier_battery_regulatory_pct_23, assess_supplier_invoice_bank_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

