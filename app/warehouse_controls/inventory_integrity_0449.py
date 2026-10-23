"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_incident_rate_pct_01(record):
    """Evaluate incident rate for control WP-0449-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-01", "metric": "incident_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-01", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-01", "metric": "incident_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-01", "metric": "incident_rate_pct", "label": "incident rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "incident rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_audit_age_days_02(record):
    """Evaluate supplier audit age for control WP-0449-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-02", "metric": "supplier_audit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-02", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-02", "metric": "supplier_audit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-02", "metric": "supplier_audit_age_days", "label": "supplier audit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier audit age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_restore_success_pct_03(record):
    """Evaluate restore success rate for control WP-0449-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restore_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-03", "metric": "restore_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-03", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-03", "metric": "restore_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-03", "metric": "restore_success_pct", "label": "restore success rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restore success rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_safety_stock_days_04(record):
    """Evaluate safety stock cover for control WP-0449-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-04", "metric": "safety_stock_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-04", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-04", "metric": "safety_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-04", "metric": "safety_stock_days", "label": "safety stock cover",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "safety stock cover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_fatigue_score_05(record):
    """Evaluate fatigue score for control WP-0449-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fatigue_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-05", "metric": "fatigue_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-05", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-05", "metric": "fatigue_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-05", "metric": "fatigue_score", "label": "fatigue score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "fatigue score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_scrap_approval_age_hours_06(record):
    """Evaluate scrap approval age for control WP-0449-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scrap_approval_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-06", "metric": "scrap_approval_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-06", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-06", "metric": "scrap_approval_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-06", "metric": "scrap_approval_age_hours", "label": "scrap approval age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "scrap approval age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_serial_audit_match_pct_07(record):
    """Evaluate serial audit match for control WP-0449-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_audit_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-07", "metric": "serial_audit_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-07", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-07", "metric": "serial_audit_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-07", "metric": "serial_audit_match_pct", "label": "serial audit match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial audit match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_hazmat_segregation_pct_08(record):
    """Evaluate hazmat segregation compliance for control WP-0449-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("hazmat_segregation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-08", "metric": "hazmat_segregation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-08", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-08", "metric": "hazmat_segregation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-08", "metric": "hazmat_segregation_pct", "label": "hazmat segregation compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "hazmat segregation compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_training_assessment_pct_09(record):
    """Evaluate training assessment score for control WP-0449-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_assessment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-09", "metric": "training_assessment_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-09", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-09", "metric": "training_assessment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-09", "metric": "training_assessment_pct", "label": "training assessment score",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "training assessment score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_assembly_point_signage_pct_10(record):
    """Evaluate assembly point signage for control WP-0449-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("assembly_point_signage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-10", "metric": "assembly_point_signage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-10", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-10", "metric": "assembly_point_signage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-10", "metric": "assembly_point_signage_pct", "label": "assembly point signage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "assembly point signage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_schema_drift_count_11(record):
    """Evaluate schema drift events for control WP-0449-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("schema_drift_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-11", "metric": "schema_drift_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-11", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-11", "metric": "schema_drift_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-11", "metric": "schema_drift_count", "label": "schema drift events",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "schema drift events must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_sku_master_gap_count_12(record):
    """Evaluate SKU master gaps for control WP-0449-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sku_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-12", "metric": "sku_master_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-12", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-12", "metric": "sku_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-12", "metric": "sku_master_gap_count", "label": "SKU master gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "SKU master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_dead_stock_value_13(record):
    """Evaluate dead stock value for control WP-0449-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_stock_value")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-13", "metric": "dead_stock_value",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-13", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-13", "metric": "dead_stock_value", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-13", "metric": "dead_stock_value", "label": "dead stock value",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "dead stock value exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_label_purchase_cost_14(record):
    """Evaluate label purchase cost for control WP-0449-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_purchase_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-14", "metric": "label_purchase_cost",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-14", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-14", "metric": "label_purchase_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-14", "metric": "label_purchase_cost", "label": "label purchase cost",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "label purchase cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_country_risk_score_15(record):
    """Evaluate country risk score for control WP-0449-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("country_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-15", "metric": "country_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-15", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-15", "metric": "country_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-15", "metric": "country_risk_score", "label": "country risk score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "country risk score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_vehicle_insurance_days_left_16(record):
    """Evaluate vehicle insurance validity for control WP-0449-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-16", "metric": "vehicle_insurance_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-16", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-16", "metric": "vehicle_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-16", "metric": "vehicle_insurance_days_left", "label": "vehicle insurance validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "vehicle insurance validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_vendor_invoice_age_days_17(record):
    """Evaluate vendor invoice age for control WP-0449-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vendor_invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-17", "metric": "vendor_invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-17", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-17", "metric": "vendor_invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-17", "metric": "vendor_invoice_age_days", "label": "vendor invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "vendor invoice age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_tooling_risk_score_18(record):
    """Evaluate supplier tooling risk for control WP-0449-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-18", "metric": "supplier_tooling_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-18", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-18", "metric": "supplier_tooling_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-18", "metric": "supplier_tooling_risk_score", "label": "supplier tooling risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier tooling risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_gauge_calibration_age_days_19(record):
    """Evaluate supplier gauge calibration age for control WP-0449-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_gauge_calibration_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-19", "metric": "supplier_gauge_calibration_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-19", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-19", "metric": "supplier_gauge_calibration_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-19", "metric": "supplier_gauge_calibration_age_days", "label": "supplier gauge calibration age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier gauge calibration age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_customs_code_accuracy_pct_20(record):
    """Evaluate supplier customs-code accuracy for control WP-0449-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customs_code_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-20", "metric": "supplier_customs_code_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-20", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-20", "metric": "supplier_customs_code_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-20", "metric": "supplier_customs_code_accuracy_pct", "label": "supplier customs-code accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customs-code accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_data_return_age_days_21(record):
    """Evaluate supplier data-return age for control WP-0449-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-21", "metric": "supplier_data_return_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-21", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-21", "metric": "supplier_data_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-21", "metric": "supplier_data_return_age_days", "label": "supplier data-return age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "supplier data-return age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_warranty_compliance_pct_22(record):
    """Evaluate supplier warranty compliance for control WP-0449-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_warranty_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-22", "metric": "supplier_warranty_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-22", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-22", "metric": "supplier_warranty_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-22", "metric": "supplier_warranty_compliance_pct", "label": "supplier warranty compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "supplier warranty compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_delivery_exception_age_hours_23(record):
    """Evaluate supplier delivery exception age for control WP-0449-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_exception_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-23", "metric": "supplier_delivery_exception_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-23", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-23", "metric": "supplier_delivery_exception_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-23", "metric": "supplier_delivery_exception_age_hours", "label": "supplier delivery exception age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier delivery exception age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_concession_expiry_days_24(record):
    """Evaluate supplier concession validity for control WP-0449-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_concession_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0449-24", "metric": "supplier_concession_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0449-24", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0449-24", "metric": "supplier_concession_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0449-24", "metric": "supplier_concession_expiry_days", "label": "supplier concession validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier concession validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_incident_rate_pct_01, assess_supplier_audit_age_days_02, assess_restore_success_pct_03, assess_safety_stock_days_04, assess_fatigue_score_05, assess_scrap_approval_age_hours_06, assess_serial_audit_match_pct_07, assess_hazmat_segregation_pct_08, assess_training_assessment_pct_09, assess_assembly_point_signage_pct_10, assess_schema_drift_count_11, assess_sku_master_gap_count_12, assess_dead_stock_value_13, assess_label_purchase_cost_14, assess_country_risk_score_15, assess_vehicle_insurance_days_left_16, assess_vendor_invoice_age_days_17, assess_supplier_tooling_risk_score_18, assess_supplier_gauge_calibration_age_days_19, assess_supplier_customs_code_accuracy_pct_20, assess_supplier_data_return_age_days_21, assess_supplier_warranty_compliance_pct_22, assess_supplier_delivery_exception_age_hours_23, assess_supplier_concession_expiry_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

