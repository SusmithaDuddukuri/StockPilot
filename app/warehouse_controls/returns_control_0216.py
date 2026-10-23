"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_stock_age_median_days_01(record):
    """Evaluate median stock age for control WP-0216-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_median_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-01", "metric": "stock_age_median_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-01", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-01", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-01", "metric": "stock_age_median_days", "label": "median stock age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "median stock age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_packaging_damage_pct_02(record):
    """Evaluate packaging damage rate for control WP-0216-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-02", "metric": "packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-02", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-02", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-02", "metric": "packaging_damage_pct", "label": "packaging damage rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "packaging damage rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_sanctions_screen_gap_count_03(record):
    """Evaluate sanctions screening gaps for control WP-0216-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sanctions_screen_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-03", "metric": "sanctions_screen_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-03", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-03", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-03", "metric": "sanctions_screen_gap_count", "label": "sanctions screening gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sanctions screening gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_driver_training_age_days_04(record):
    """Evaluate driver training age for control WP-0216-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_training_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-04", "metric": "driver_training_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-04", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-04", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-04", "metric": "driver_training_age_days", "label": "driver training age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "driver training age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_automation_roi_pct_05(record):
    """Evaluate automation ROI for control WP-0216-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_roi_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-05", "metric": "automation_roi_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-05", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-05", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-05", "metric": "automation_roi_pct", "label": "automation ROI",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "automation ROI falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_license_days_left_06(record):
    """Evaluate supplier license validity for control WP-0216-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-06", "metric": "supplier_license_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-06", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-06", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-06", "metric": "supplier_license_days_left", "label": "supplier license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier license validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_root_cause_completeness_pct_07(record):
    """Evaluate supplier root-cause completeness for control WP-0216-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_root_cause_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-07", "metric": "supplier_root_cause_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-07", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-07", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-07", "metric": "supplier_root_cause_completeness_pct", "label": "supplier root-cause completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier root-cause completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_indexation_variance_pct_08(record):
    """Evaluate supplier indexation variance for control WP-0216-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_indexation_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-08", "metric": "supplier_indexation_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-08", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-08", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-08", "metric": "supplier_indexation_variance_pct", "label": "supplier indexation variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier indexation variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_document_version_gap_count_09(record):
    """Evaluate supplier document-version gaps for control WP-0216-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_version_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-09", "metric": "supplier_document_version_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-09", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-09", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-09", "metric": "supplier_document_version_gap_count", "label": "supplier document-version gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier document-version gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_language_label_pct_10(record):
    """Evaluate supplier language-label compliance for control WP-0216-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_language_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-10", "metric": "supplier_language_label_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-10", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-10", "metric": "supplier_language_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-10", "metric": "supplier_language_label_pct", "label": "supplier language-label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier language-label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_vehicle_cleanliness_pct_11(record):
    """Evaluate supplier vehicle cleanliness for control WP-0216-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vehicle_cleanliness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-11", "metric": "supplier_vehicle_cleanliness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-11", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-11", "metric": "supplier_vehicle_cleanliness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-11", "metric": "supplier_vehicle_cleanliness_pct", "label": "supplier vehicle cleanliness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier vehicle cleanliness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_product_change_approval_pct_12(record):
    """Evaluate supplier product-change approval for control WP-0216-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-12", "metric": "supplier_product_change_approval_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-12", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-12", "metric": "supplier_product_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-12", "metric": "supplier_product_change_approval_pct", "label": "supplier product-change approval",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "supplier product-change approval exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_battery_regulatory_pct_13(record):
    """Evaluate supplier battery regulation compliance for control WP-0216-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_battery_regulatory_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-13", "metric": "supplier_battery_regulatory_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-13", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-13", "metric": "supplier_battery_regulatory_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-13", "metric": "supplier_battery_regulatory_pct", "label": "supplier battery regulation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier battery regulation compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_invoice_bank_match_pct_14(record):
    """Evaluate supplier invoice-bank match for control WP-0216-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_bank_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-14", "metric": "supplier_invoice_bank_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-14", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-14", "metric": "supplier_invoice_bank_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-14", "metric": "supplier_invoice_bank_match_pct", "label": "supplier invoice-bank match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice-bank match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_communication_redundancy_pct_15(record):
    """Evaluate supplier communications redundancy for control WP-0216-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_communication_redundancy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-15", "metric": "supplier_communication_redundancy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-15", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-15", "metric": "supplier_communication_redundancy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-15", "metric": "supplier_communication_redundancy_pct", "label": "supplier communications redundancy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier communications redundancy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_model_drift_pct_16(record):
    """Evaluate supplier model drift for control WP-0216-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_model_drift_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-16", "metric": "supplier_model_drift_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-16", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-16", "metric": "supplier_model_drift_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-16", "metric": "supplier_model_drift_pct", "label": "supplier model drift",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "supplier model drift exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_schema_compatibility_pct_17(record):
    """Evaluate supplier schema compatibility for control WP-0216-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schema_compatibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-17", "metric": "supplier_schema_compatibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-17", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-17", "metric": "supplier_schema_compatibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-17", "metric": "supplier_schema_compatibility_pct", "label": "supplier schema compatibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier schema compatibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_account_deprovision_age_hours_18(record):
    """Evaluate supplier account deprovision age for control WP-0216-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_account_deprovision_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-18", "metric": "supplier_account_deprovision_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-18", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-18", "metric": "supplier_account_deprovision_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-18", "metric": "supplier_account_deprovision_age_hours", "label": "supplier account deprovision age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier account deprovision age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_data_minimization_pct_19(record):
    """Evaluate supplier data minimization for control WP-0216-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_minimization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-19", "metric": "supplier_data_minimization_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-19", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-19", "metric": "supplier_data_minimization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-19", "metric": "supplier_data_minimization_pct", "label": "supplier data minimization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier data minimization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_attestation_age_days_20(record):
    """Evaluate supplier attestation age for control WP-0216-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-20", "metric": "supplier_attestation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-20", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-20", "metric": "supplier_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-20", "metric": "supplier_attestation_age_days", "label": "supplier attestation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier attestation age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_rebate_claim_age_days_21(record):
    """Evaluate supplier rebate claim age for control WP-0216-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_rebate_claim_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-21", "metric": "supplier_rebate_claim_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-21", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-21", "metric": "supplier_rebate_claim_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-21", "metric": "supplier_rebate_claim_age_days", "label": "supplier rebate claim age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier rebate claim age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_warehouse_capacity_pct_22(record):
    """Evaluate supplier warehouse capacity for control WP-0216-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warehouse_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-22", "metric": "supplier_warehouse_capacity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-22", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-22", "metric": "supplier_warehouse_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-22", "metric": "supplier_warehouse_capacity_pct", "label": "supplier warehouse capacity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier warehouse capacity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_transaction_replay_pct_23(record):
    """Evaluate supplier transaction replay for control WP-0216-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transaction_replay_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-23", "metric": "supplier_transaction_replay_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-23", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-23", "metric": "supplier_transaction_replay_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-23", "metric": "supplier_transaction_replay_pct", "label": "supplier transaction replay",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier transaction replay must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_reorder_level_24(record):
    """Evaluate reorder point for control WP-0216-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reorder_level")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0216-24", "metric": "reorder_level",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0216-24", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0216-24", "metric": "reorder_level", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0216-24", "metric": "reorder_level", "label": "reorder point",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "reorder point exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_stock_age_median_days_01, assess_packaging_damage_pct_02, assess_sanctions_screen_gap_count_03, assess_driver_training_age_days_04, assess_automation_roi_pct_05, assess_supplier_license_days_left_06, assess_supplier_root_cause_completeness_pct_07, assess_supplier_indexation_variance_pct_08, assess_supplier_document_version_gap_count_09, assess_supplier_language_label_pct_10, assess_supplier_vehicle_cleanliness_pct_11, assess_supplier_product_change_approval_pct_12, assess_supplier_battery_regulatory_pct_13, assess_supplier_invoice_bank_match_pct_14, assess_supplier_communication_redundancy_pct_15, assess_supplier_model_drift_pct_16, assess_supplier_schema_compatibility_pct_17, assess_supplier_account_deprovision_age_hours_18, assess_supplier_data_minimization_pct_19, assess_supplier_attestation_age_days_20, assess_supplier_rebate_claim_age_days_21, assess_supplier_warehouse_capacity_pct_22, assess_supplier_transaction_replay_pct_23, assess_reorder_level_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

