"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_issue_transparency_pct_01(record):
    """Evaluate supplier issue transparency for control WP-0567-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_issue_transparency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-01", "metric": "supplier_issue_transparency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-01", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-01", "metric": "supplier_issue_transparency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-01", "metric": "supplier_issue_transparency_pct", "label": "supplier issue transparency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier issue transparency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_customer_notice_pct_02(record):
    """Evaluate supplier customer notice completion for control WP-0567-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_notice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-02", "metric": "supplier_customer_notice_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-02", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-02", "metric": "supplier_customer_notice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-02", "metric": "supplier_customer_notice_pct", "label": "supplier customer notice completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer notice completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_return_rate_pct_03(record):
    """Evaluate return rate for control WP-0567-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("return_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-03", "metric": "return_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-03", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-03", "metric": "return_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-03", "metric": "return_rate_pct", "label": "return rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "return rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_payment_hold_count_04(record):
    """Evaluate payment holds for control WP-0567-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_hold_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-04", "metric": "payment_hold_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "orders",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-04", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-04", "metric": "payment_hold_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-04", "metric": "payment_hold_count", "label": "payment holds",
        "status": "breach", "severity": "high", "unit": "orders",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "payment holds falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_order_split_count_05(record):
    """Evaluate order splits for control WP-0567-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_split_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-05", "metric": "order_split_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "orders",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-05", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-05", "metric": "order_split_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-05", "metric": "order_split_count", "label": "order splits",
        "status": "breach", "severity": "critical", "unit": "orders",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order splits must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_packaging_compliance_pct_06(record):
    """Evaluate packaging compliance for control WP-0567-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-06", "metric": "packaging_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-06", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-06", "metric": "packaging_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-06", "metric": "packaging_compliance_pct", "label": "packaging compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "packaging compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_export_license_days_left_07(record):
    """Evaluate export license validity for control WP-0567-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-07", "metric": "export_license_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-07", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-07", "metric": "export_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-07", "metric": "export_license_days_left", "label": "export license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "export license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_phishing_report_delay_minutes_08(record):
    """Evaluate phishing report delay for control WP-0567-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("phishing_report_delay_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-08", "metric": "phishing_report_delay_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-08", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-08", "metric": "phishing_report_delay_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-08", "metric": "phishing_report_delay_minutes", "label": "phishing report delay",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "phishing report delay falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_quote_age_hours_09(record):
    """Evaluate quote age for control WP-0567-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("quote_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-09", "metric": "quote_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-09", "metric": "quote_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-09", "metric": "quote_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-09", "metric": "quote_age_hours", "label": "quote age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "quote age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_heat_stress_score_10(record):
    """Evaluate heat stress for control WP-0567-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("heat_stress_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-10", "metric": "heat_stress_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-10", "metric": "heat_stress_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-10", "metric": "heat_stress_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-10", "metric": "heat_stress_score", "label": "heat stress",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "heat stress must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_restock_delay_hours_11(record):
    """Evaluate restock delay for control WP-0567-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restock_delay_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-11", "metric": "restock_delay_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-11", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-11", "metric": "restock_delay_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-11", "metric": "restock_delay_hours", "label": "restock delay",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "restock delay exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_batch_release_approval_pct_12(record):
    """Evaluate batch release approval for control WP-0567-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-12", "metric": "batch_release_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-12", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-12", "metric": "batch_release_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-12", "metric": "batch_release_approval_pct", "label": "batch release approval",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "batch release approval falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_e_waste_manifest_pct_13(record):
    """Evaluate e-waste manifest completeness for control WP-0567-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("e_waste_manifest_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-13", "metric": "e_waste_manifest_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-13", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-13", "metric": "e_waste_manifest_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-13", "metric": "e_waste_manifest_pct", "label": "e-waste manifest completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "e-waste manifest completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_risk_assessment_age_days_14(record):
    """Evaluate risk assessment age for control WP-0567-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("risk_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-14", "metric": "risk_assessment_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-14", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-14", "metric": "risk_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-14", "metric": "risk_assessment_age_days", "label": "risk assessment age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "risk assessment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_lighting_lux_15(record):
    """Evaluate lighting level for control WP-0567-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lighting_lux")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-15", "metric": "lighting_lux",
            "status": "insufficient_data",
            "severity": "medium", "unit": "lux",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-15", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-15", "metric": "lighting_lux", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-15", "metric": "lighting_lux", "label": "lighting level",
        "status": "breach", "severity": "medium", "unit": "lux",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "lighting level exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_dependency_vulnerability_count_16(record):
    """Evaluate dependency vulnerabilities for control WP-0567-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dependency_vulnerability_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-16", "metric": "dependency_vulnerability_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-16", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-16", "metric": "dependency_vulnerability_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-16", "metric": "dependency_vulnerability_count", "label": "dependency vulnerabilities",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "dependency vulnerabilities falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_barcode_quality_score_17(record):
    """Evaluate barcode quality for control WP-0567-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("barcode_quality_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-17", "metric": "barcode_quality_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-17", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-17", "metric": "barcode_quality_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-17", "metric": "barcode_quality_score", "label": "barcode quality",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "barcode quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_inventory_writeoff_pct_18(record):
    """Evaluate inventory write-off rate for control WP-0567-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_writeoff_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-18", "metric": "inventory_writeoff_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-18", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-18", "metric": "inventory_writeoff_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-18", "metric": "inventory_writeoff_pct", "label": "inventory write-off rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory write-off rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_pack_station_queue_19(record):
    """Evaluate pack-station queue for control WP-0567-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_station_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-19", "metric": "pack_station_queue",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-19", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-19", "metric": "pack_station_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-19", "metric": "pack_station_queue", "label": "pack-station queue",
        "status": "breach", "severity": "medium", "unit": "orders",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "pack-station queue exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_trade_compliance_score_20(record):
    """Evaluate trade compliance score for control WP-0567-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("trade_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-20", "metric": "trade_compliance_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-20", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-20", "metric": "trade_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-20", "metric": "trade_compliance_score", "label": "trade compliance score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "trade compliance score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_preventable_accident_count_21(record):
    """Evaluate preventable accidents for control WP-0567-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("preventable_accident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-21", "metric": "preventable_accident_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-21", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-21", "metric": "preventable_accident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-21", "metric": "preventable_accident_count", "label": "preventable accidents",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "preventable accidents must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_equipment_cost_per_hour_22(record):
    """Evaluate equipment cost per hour for control WP-0567-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("equipment_cost_per_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-22", "metric": "equipment_cost_per_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-22", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-22", "metric": "equipment_cost_per_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-22", "metric": "equipment_cost_per_hour", "label": "equipment cost per hour",
        "status": "breach", "severity": "low", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "equipment cost per hour must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_insurance_days_left_23(record):
    """Evaluate supplier insurance validity for control WP-0567-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_insurance_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-23", "metric": "supplier_insurance_days_left",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-23", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-23", "metric": "supplier_insurance_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-23", "metric": "supplier_insurance_days_left", "label": "supplier insurance validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier insurance validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_8d_age_days_24(record):
    """Evaluate supplier 8D report age for control WP-0567-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_8d_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0567-24", "metric": "supplier_8d_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0567-24", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0567-24", "metric": "supplier_8d_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0567-24", "metric": "supplier_8d_age_days", "label": "supplier 8D report age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier 8D report age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_issue_transparency_pct_01, assess_supplier_customer_notice_pct_02, assess_return_rate_pct_03, assess_payment_hold_count_04, assess_order_split_count_05, assess_packaging_compliance_pct_06, assess_export_license_days_left_07, assess_phishing_report_delay_minutes_08, assess_quote_age_hours_09, assess_heat_stress_score_10, assess_restock_delay_hours_11, assess_batch_release_approval_pct_12, assess_e_waste_manifest_pct_13, assess_risk_assessment_age_days_14, assess_lighting_lux_15, assess_dependency_vulnerability_count_16, assess_barcode_quality_score_17, assess_inventory_writeoff_pct_18, assess_pack_station_queue_19, assess_trade_compliance_score_20, assess_preventable_accident_count_21, assess_equipment_cost_per_hour_22, assess_supplier_insurance_days_left_23, assess_supplier_8d_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

