"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_forecast_bias_pct_01(record):
    """Evaluate forecast bias for control WP-0391-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_bias_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-01", "metric": "forecast_bias_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-01", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-01", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-01", "metric": "forecast_bias_pct", "label": "forecast bias",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast bias must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_cold_exposure_minutes_02(record):
    """Evaluate cold exposure for control WP-0391-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_exposure_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-02", "metric": "cold_exposure_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-02", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-02", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-02", "metric": "cold_exposure_minutes", "label": "cold exposure",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cold exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_credit_age_days_03(record):
    """Evaluate supplier credit age for control WP-0391-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-03", "metric": "supplier_credit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-03", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-03", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-03", "metric": "supplier_credit_age_days", "label": "supplier credit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier credit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_recall_drill_age_days_04(record):
    """Evaluate recall drill age for control WP-0391-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-04", "metric": "recall_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-04", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-04", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-04", "metric": "recall_drill_age_days", "label": "recall drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "recall drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_dangerous_goods_declaration_pct_05(record):
    """Evaluate dangerous goods declaration for control WP-0391-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dangerous_goods_declaration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-05", "metric": "dangerous_goods_declaration_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-05", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-05", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-05", "metric": "dangerous_goods_declaration_pct", "label": "dangerous goods declaration",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dangerous goods declaration must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_safety_walk_age_days_06(record):
    """Evaluate safety walk age for control WP-0391-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_walk_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-06", "metric": "safety_walk_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-06", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-06", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-06", "metric": "safety_walk_age_days", "label": "safety walk age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "safety walk age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_emergency_alarm_test_age_days_07(record):
    """Evaluate emergency alarm test age for control WP-0391-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_alarm_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-07", "metric": "emergency_alarm_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-07", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-07", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-07", "metric": "emergency_alarm_test_age_days", "label": "emergency alarm test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "emergency alarm test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_software_bill_of_materials_age_days_08(record):
    """Evaluate SBOM age for control WP-0391-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("software_bill_of_materials_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-08", "metric": "software_bill_of_materials_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-08", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-08", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-08", "metric": "software_bill_of_materials_age_days", "label": "SBOM age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "SBOM age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_rfid_read_rate_pct_09(record):
    """Evaluate RFID read rate for control WP-0391-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-09", "metric": "rfid_read_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-09", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-09", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-09", "metric": "rfid_read_rate_pct", "label": "RFID read rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "RFID read rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_stock_age_median_days_10(record):
    """Evaluate median stock age for control WP-0391-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_median_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-10", "metric": "stock_age_median_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-10", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-10", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-10", "metric": "stock_age_median_days", "label": "median stock age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "median stock age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_packaging_damage_pct_11(record):
    """Evaluate packaging damage rate for control WP-0391-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-11", "metric": "packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-11", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-11", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-11", "metric": "packaging_damage_pct", "label": "packaging damage rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "packaging damage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_sanctions_screen_gap_count_12(record):
    """Evaluate sanctions screening gaps for control WP-0391-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sanctions_screen_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-12", "metric": "sanctions_screen_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 9,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-12", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-12", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 9
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-12", "metric": "sanctions_screen_gap_count", "label": "sanctions screening gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 9, "comparison": "min",
        "finding": "sanctions screening gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_driver_training_age_days_13(record):
    """Evaluate driver training age for control WP-0391-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_training_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-13", "metric": "driver_training_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-13", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-13", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-13", "metric": "driver_training_age_days", "label": "driver training age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver training age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_automation_roi_pct_14(record):
    """Evaluate automation ROI for control WP-0391-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_roi_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-14", "metric": "automation_roi_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-14", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-14", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-14", "metric": "automation_roi_pct", "label": "automation ROI",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "automation ROI must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_license_days_left_15(record):
    """Evaluate supplier license validity for control WP-0391-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-15", "metric": "supplier_license_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-15", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-15", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-15", "metric": "supplier_license_days_left", "label": "supplier license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "supplier license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_root_cause_completeness_pct_16(record):
    """Evaluate supplier root-cause completeness for control WP-0391-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_root_cause_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-16", "metric": "supplier_root_cause_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-16", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-16", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-16", "metric": "supplier_root_cause_completeness_pct", "label": "supplier root-cause completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 53, "comparison": "min",
        "finding": "supplier root-cause completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_indexation_variance_pct_17(record):
    """Evaluate supplier indexation variance for control WP-0391-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_indexation_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-17", "metric": "supplier_indexation_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-17", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-17", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-17", "metric": "supplier_indexation_variance_pct", "label": "supplier indexation variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier indexation variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_document_version_gap_count_18(record):
    """Evaluate supplier document-version gaps for control WP-0391-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_version_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-18", "metric": "supplier_document_version_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-18", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-18", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-18", "metric": "supplier_document_version_gap_count", "label": "supplier document-version gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier document-version gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_language_label_pct_19(record):
    """Evaluate supplier language-label compliance for control WP-0391-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_language_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-19", "metric": "supplier_language_label_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-19", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-19", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-19", "metric": "supplier_language_label_pct", "label": "supplier language-label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier language-label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_vehicle_cleanliness_pct_20(record):
    """Evaluate supplier vehicle cleanliness for control WP-0391-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vehicle_cleanliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-20", "metric": "supplier_vehicle_cleanliness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 2,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-20", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-20", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 2
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-20", "metric": "supplier_vehicle_cleanliness_pct", "label": "supplier vehicle cleanliness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 2, "comparison": "min",
        "finding": "supplier vehicle cleanliness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_product_change_approval_pct_21(record):
    """Evaluate supplier product-change approval for control WP-0391-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-21", "metric": "supplier_product_change_approval_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-21", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-21", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-21", "metric": "supplier_product_change_approval_pct", "label": "supplier product-change approval",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier product-change approval must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_battery_regulatory_pct_22(record):
    """Evaluate supplier battery regulation compliance for control WP-0391-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_battery_regulatory_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-22", "metric": "supplier_battery_regulatory_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-22", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-22", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-22", "metric": "supplier_battery_regulatory_pct", "label": "supplier battery regulation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier battery regulation compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_invoice_bank_match_pct_23(record):
    """Evaluate supplier invoice-bank match for control WP-0391-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_bank_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-23", "metric": "supplier_invoice_bank_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-23", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-23", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-23", "metric": "supplier_invoice_bank_match_pct", "label": "supplier invoice-bank match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "supplier invoice-bank match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_communication_redundancy_pct_24(record):
    """Evaluate supplier communications redundancy for control WP-0391-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_communication_redundancy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0391-24", "metric": "supplier_communication_redundancy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 46,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0391-24", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0391-24", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 46
    if not failed:
        return None
    return {
        "rule_id": "WP-0391-24", "metric": "supplier_communication_redundancy_pct", "label": "supplier communications redundancy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 46, "comparison": "min",
        "finding": "supplier communications redundancy falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_forecast_bias_pct_01, assess_cold_exposure_minutes_02, assess_supplier_credit_age_days_03, assess_recall_drill_age_days_04, assess_dangerous_goods_declaration_pct_05, assess_safety_walk_age_days_06, assess_emergency_alarm_test_age_days_07, assess_software_bill_of_materials_age_days_08, assess_rfid_read_rate_pct_09, assess_stock_age_median_days_10, assess_packaging_damage_pct_11, assess_sanctions_screen_gap_count_12, assess_driver_training_age_days_13, assess_automation_roi_pct_14, assess_supplier_license_days_left_15, assess_supplier_root_cause_completeness_pct_16, assess_supplier_indexation_variance_pct_17, assess_supplier_document_version_gap_count_18, assess_supplier_language_label_pct_19, assess_supplier_vehicle_cleanliness_pct_20, assess_supplier_product_change_approval_pct_21, assess_supplier_battery_regulatory_pct_22, assess_supplier_invoice_bank_match_pct_23, assess_supplier_communication_redundancy_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

