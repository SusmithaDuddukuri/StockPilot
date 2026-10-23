"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_aisle_obstruction_count_01(record):
    """Evaluate aisle obstructions for control WP-0193-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-01", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 189,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-01", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-01", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 189
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-01", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 189, "comparison": "max",
        "finding": "aisle obstructions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_crossdock_share_pct_02(record):
    """Evaluate cross-dock share for control WP-0193-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-02", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-02", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-02", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-02", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "cross-dock share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_maintenance_due_days_03(record):
    """Evaluate maintenance due for control WP-0193-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-03", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-03", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-03", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-03", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "maintenance due must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_capacity_pct_04(record):
    """Evaluate supplier capacity utilization for control WP-0193-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-04", "metric": "supplier_capacity_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-04", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-04", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-04", "metric": "supplier_capacity_pct", "label": "supplier capacity utilization",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity utilization must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_replication_lag_seconds_05(record):
    """Evaluate replication lag for control WP-0193-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replication_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-05", "metric": "replication_lag_seconds",
            "status": "insufficient_data",
            "severity": "medium", "unit": "seconds",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-05", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-05", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-05", "metric": "replication_lag_seconds", "label": "replication lag",
        "status": "breach", "severity": "medium", "unit": "seconds",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "replication lag exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_economic_order_qty_06(record):
    """Evaluate economic order quantity for control WP-0193-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("economic_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-06", "metric": "economic_order_qty",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-06", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-06", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-06", "metric": "economic_order_qty", "label": "economic order quantity",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "economic order quantity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_break_overdue_minutes_07(record):
    """Evaluate break overdue for control WP-0193-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-07", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-07", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-07", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-07", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "break overdue must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_donation_age_days_08(record):
    """Evaluate donation processing age for control WP-0193-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-08", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-08", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-08", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-08", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "donation processing age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_high_value_variance_09(record):
    """Evaluate high-value inventory variance for control WP-0193-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-09", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-09", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-09", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-09", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "high-value inventory variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_incompatible_storage_count_10(record):
    """Evaluate incompatible storage pairs for control WP-0193-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incompatible_storage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-10", "metric": "incompatible_storage_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "pairs",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-10", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-10", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-10", "metric": "incompatible_storage_count", "label": "incompatible storage pairs",
        "status": "breach", "severity": "high", "unit": "pairs",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "incompatible storage pairs falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_license_validity_days_11(record):
    """Evaluate license validity for control WP-0193-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-11", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-11", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-11", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-11", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "license validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_business_continuity_test_age_days_12(record):
    """Evaluate business continuity test age for control WP-0193-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("business_continuity_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-12", "metric": "business_continuity_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-12", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-12", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-12", "metric": "business_continuity_test_age_days", "label": "business continuity test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "business continuity test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_etl_lag_minutes_13(record):
    """Evaluate ETL lag for control WP-0193-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("etl_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-13", "metric": "etl_lag_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-13", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-13", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-13", "metric": "etl_lag_minutes", "label": "ETL lag",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "ETL lag exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_uom_conversion_gap_count_14(record):
    """Evaluate unit conversion gaps for control WP-0193-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("uom_conversion_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-14", "metric": "uom_conversion_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-14", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-14", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-14", "metric": "uom_conversion_gap_count", "label": "unit conversion gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "unit conversion gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_obsolete_sku_count_15(record):
    """Evaluate obsolete SKUs for control WP-0193-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-15", "metric": "obsolete_sku_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "SKUs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-15", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-15", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-15", "metric": "obsolete_sku_count", "label": "obsolete SKUs",
        "status": "breach", "severity": "critical", "unit": "SKUs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "obsolete SKUs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_carrier_rate_variance_pct_16(record):
    """Evaluate carrier rate variance for control WP-0193-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-16", "metric": "carrier_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-16", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-16", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-16", "metric": "carrier_rate_variance_pct", "label": "carrier rate variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carrier rate variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_insurance_claim_count_17(record):
    """Evaluate insurance claims for control WP-0193-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-17", "metric": "insurance_claim_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-17", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-17", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-17", "metric": "insurance_claim_count", "label": "insurance claims",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "insurance claims exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_roadside_assistance_age_days_18(record):
    """Evaluate roadside assistance review age for control WP-0193-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("roadside_assistance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-18", "metric": "roadside_assistance_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-18", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-18", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-18", "metric": "roadside_assistance_age_days", "label": "roadside assistance review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "roadside assistance review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_purchase_requisition_age_hours_19(record):
    """Evaluate purchase requisition age for control WP-0193-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_requisition_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-19", "metric": "purchase_requisition_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-19", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-19", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-19", "metric": "purchase_requisition_age_hours", "label": "purchase requisition age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "purchase requisition age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_single_site_pct_20(record):
    """Evaluate supplier single-site dependency for control WP-0193-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_single_site_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-20", "metric": "supplier_single_site_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-20", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-20", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-20", "metric": "supplier_single_site_pct", "label": "supplier single-site dependency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier single-site dependency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_measurement_system_score_21(record):
    """Evaluate supplier measurement system score for control WP-0193-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_system_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-21", "metric": "supplier_measurement_system_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-21", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-21", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-21", "metric": "supplier_measurement_system_score", "label": "supplier measurement system score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "supplier measurement system score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_origin_document_pct_22(record):
    """Evaluate supplier origin-document completeness for control WP-0193-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_origin_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-22", "metric": "supplier_origin_document_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-22", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-22", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-22", "metric": "supplier_origin_document_pct", "label": "supplier origin-document completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "supplier origin-document completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_transition_readiness_pct_23(record):
    """Evaluate supplier transition readiness for control WP-0193-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-23", "metric": "supplier_transition_readiness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-23", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-23", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-23", "metric": "supplier_transition_readiness_pct", "label": "supplier transition readiness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier transition readiness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_serial_warranty_match_pct_24(record):
    """Evaluate supplier serial/warranty match for control WP-0193-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_warranty_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0193-24", "metric": "supplier_serial_warranty_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0193-24", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0193-24", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0193-24", "metric": "supplier_serial_warranty_match_pct", "label": "supplier serial/warranty match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier serial/warranty match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_aisle_obstruction_count_01, assess_crossdock_share_pct_02, assess_maintenance_due_days_03, assess_supplier_capacity_pct_04, assess_replication_lag_seconds_05, assess_economic_order_qty_06, assess_break_overdue_minutes_07, assess_donation_age_days_08, assess_high_value_variance_09, assess_incompatible_storage_count_10, assess_license_validity_days_11, assess_business_continuity_test_age_days_12, assess_etl_lag_minutes_13, assess_uom_conversion_gap_count_14, assess_obsolete_sku_count_15, assess_carrier_rate_variance_pct_16, assess_insurance_claim_count_17, assess_roadside_assistance_age_days_18, assess_purchase_requisition_age_hours_19, assess_supplier_single_site_pct_20, assess_supplier_measurement_system_score_21, assess_supplier_origin_document_pct_22, assess_supplier_transition_readiness_pct_23, assess_supplier_serial_warranty_match_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

