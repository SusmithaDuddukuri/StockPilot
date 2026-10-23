"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_recall_drill_age_days_01(record):
    """Evaluate recall drill age for control WP-0459-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-01", "metric": "recall_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-01", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-01", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-01", "metric": "recall_drill_age_days", "label": "recall drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recall drill age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_dangerous_goods_declaration_pct_02(record):
    """Evaluate dangerous goods declaration for control WP-0459-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dangerous_goods_declaration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-02", "metric": "dangerous_goods_declaration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-02", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-02", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-02", "metric": "dangerous_goods_declaration_pct", "label": "dangerous goods declaration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "dangerous goods declaration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_safety_walk_age_days_03(record):
    """Evaluate safety walk age for control WP-0459-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_walk_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-03", "metric": "safety_walk_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-03", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-03", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-03", "metric": "safety_walk_age_days", "label": "safety walk age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "safety walk age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_emergency_alarm_test_age_days_04(record):
    """Evaluate emergency alarm test age for control WP-0459-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_alarm_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-04", "metric": "emergency_alarm_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 17,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-04", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-04", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 17
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-04", "metric": "emergency_alarm_test_age_days", "label": "emergency alarm test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 17, "comparison": "min",
        "finding": "emergency alarm test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_software_bill_of_materials_age_days_05(record):
    """Evaluate SBOM age for control WP-0459-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("software_bill_of_materials_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-05", "metric": "software_bill_of_materials_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-05", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-05", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-05", "metric": "software_bill_of_materials_age_days", "label": "SBOM age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "SBOM age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_rfid_read_rate_pct_06(record):
    """Evaluate RFID read rate for control WP-0459-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-06", "metric": "rfid_read_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-06", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-06", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-06", "metric": "rfid_read_rate_pct", "label": "RFID read rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "RFID read rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_stock_age_median_days_07(record):
    """Evaluate median stock age for control WP-0459-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_median_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-07", "metric": "stock_age_median_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-07", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-07", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-07", "metric": "stock_age_median_days", "label": "median stock age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "median stock age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_packaging_damage_pct_08(record):
    """Evaluate packaging damage rate for control WP-0459-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-08", "metric": "packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-08", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-08", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-08", "metric": "packaging_damage_pct", "label": "packaging damage rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 61, "comparison": "min",
        "finding": "packaging damage rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_sanctions_screen_gap_count_09(record):
    """Evaluate sanctions screening gaps for control WP-0459-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sanctions_screen_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-09", "metric": "sanctions_screen_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-09", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-09", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-09", "metric": "sanctions_screen_gap_count", "label": "sanctions screening gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sanctions screening gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_driver_training_age_days_10(record):
    """Evaluate driver training age for control WP-0459-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_training_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-10", "metric": "driver_training_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-10", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-10", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-10", "metric": "driver_training_age_days", "label": "driver training age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "driver training age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_automation_roi_pct_11(record):
    """Evaluate automation ROI for control WP-0459-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_roi_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-11", "metric": "automation_roi_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-11", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-11", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-11", "metric": "automation_roi_pct", "label": "automation ROI",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "automation ROI exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_license_days_left_12(record):
    """Evaluate supplier license validity for control WP-0459-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-12", "metric": "supplier_license_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 10,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-12", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-12", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 10
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-12", "metric": "supplier_license_days_left", "label": "supplier license validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 10, "comparison": "min",
        "finding": "supplier license validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_root_cause_completeness_pct_13(record):
    """Evaluate supplier root-cause completeness for control WP-0459-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_root_cause_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-13", "metric": "supplier_root_cause_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-13", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-13", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-13", "metric": "supplier_root_cause_completeness_pct", "label": "supplier root-cause completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier root-cause completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_indexation_variance_pct_14(record):
    """Evaluate supplier indexation variance for control WP-0459-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_indexation_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-14", "metric": "supplier_indexation_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-14", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-14", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-14", "metric": "supplier_indexation_variance_pct", "label": "supplier indexation variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier indexation variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_document_version_gap_count_15(record):
    """Evaluate supplier document-version gaps for control WP-0459-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_version_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-15", "metric": "supplier_document_version_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-15", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-15", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-15", "metric": "supplier_document_version_gap_count", "label": "supplier document-version gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier document-version gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_language_label_pct_16(record):
    """Evaluate supplier language-label compliance for control WP-0459-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_language_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-16", "metric": "supplier_language_label_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 54,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-16", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-16", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 54
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-16", "metric": "supplier_language_label_pct", "label": "supplier language-label compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 54, "comparison": "min",
        "finding": "supplier language-label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_vehicle_cleanliness_pct_17(record):
    """Evaluate supplier vehicle cleanliness for control WP-0459-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vehicle_cleanliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-17", "metric": "supplier_vehicle_cleanliness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-17", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-17", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-17", "metric": "supplier_vehicle_cleanliness_pct", "label": "supplier vehicle cleanliness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vehicle cleanliness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_product_change_approval_pct_18(record):
    """Evaluate supplier product-change approval for control WP-0459-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-18", "metric": "supplier_product_change_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-18", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-18", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-18", "metric": "supplier_product_change_approval_pct", "label": "supplier product-change approval",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier product-change approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_battery_regulatory_pct_19(record):
    """Evaluate supplier battery regulation compliance for control WP-0459-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_battery_regulatory_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-19", "metric": "supplier_battery_regulatory_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-19", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-19", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-19", "metric": "supplier_battery_regulatory_pct", "label": "supplier battery regulation compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "supplier battery regulation compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_invoice_bank_match_pct_20(record):
    """Evaluate supplier invoice-bank match for control WP-0459-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_bank_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-20", "metric": "supplier_invoice_bank_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 3,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-20", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-20", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 3
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-20", "metric": "supplier_invoice_bank_match_pct", "label": "supplier invoice-bank match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 3, "comparison": "min",
        "finding": "supplier invoice-bank match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_communication_redundancy_pct_21(record):
    """Evaluate supplier communications redundancy for control WP-0459-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_communication_redundancy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-21", "metric": "supplier_communication_redundancy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-21", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-21", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-21", "metric": "supplier_communication_redundancy_pct", "label": "supplier communications redundancy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier communications redundancy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_model_drift_pct_22(record):
    """Evaluate supplier model drift for control WP-0459-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_drift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-22", "metric": "supplier_model_drift_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-22", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-22", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-22", "metric": "supplier_model_drift_pct", "label": "supplier model drift",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier model drift must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_schema_compatibility_pct_23(record):
    """Evaluate supplier schema compatibility for control WP-0459-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schema_compatibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-23", "metric": "supplier_schema_compatibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-23", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-23", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-23", "metric": "supplier_schema_compatibility_pct", "label": "supplier schema compatibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier schema compatibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_account_deprovision_age_hours_24(record):
    """Evaluate supplier account deprovision age for control WP-0459-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_account_deprovision_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0459-24", "metric": "supplier_account_deprovision_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0459-24", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0459-24", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0459-24", "metric": "supplier_account_deprovision_age_hours", "label": "supplier account deprovision age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 47, "comparison": "min",
        "finding": "supplier account deprovision age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_recall_drill_age_days_01, assess_dangerous_goods_declaration_pct_02, assess_safety_walk_age_days_03, assess_emergency_alarm_test_age_days_04, assess_software_bill_of_materials_age_days_05, assess_rfid_read_rate_pct_06, assess_stock_age_median_days_07, assess_packaging_damage_pct_08, assess_sanctions_screen_gap_count_09, assess_driver_training_age_days_10, assess_automation_roi_pct_11, assess_supplier_license_days_left_12, assess_supplier_root_cause_completeness_pct_13, assess_supplier_indexation_variance_pct_14, assess_supplier_document_version_gap_count_15, assess_supplier_language_label_pct_16, assess_supplier_vehicle_cleanliness_pct_17, assess_supplier_product_change_approval_pct_18, assess_supplier_battery_regulatory_pct_19, assess_supplier_invoice_bank_match_pct_20, assess_supplier_communication_redundancy_pct_21, assess_supplier_model_drift_pct_22, assess_supplier_schema_compatibility_pct_23, assess_supplier_account_deprovision_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

