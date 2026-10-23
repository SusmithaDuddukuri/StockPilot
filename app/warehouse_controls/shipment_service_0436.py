"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_control_owner_gap_count_01(record):
    """Evaluate supplier control-owner gaps for control WP-0436-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-01", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-01", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-01", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-01", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "supplier control-owner gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_three_way_match_pct_02(record):
    """Evaluate supplier three-way match for control WP-0436-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-02", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-02", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-02", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-02", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier three-way match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_process_capability_score_03(record):
    """Evaluate supplier process capability for control WP-0436-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-03", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-03", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-03", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-03", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process capability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_kpi_data_quality_pct_04(record):
    """Evaluate supplier KPI data quality for control WP-0436-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-04", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-04", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-04", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-04", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier KPI data quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_final_reconciliation_pct_05(record):
    """Evaluate supplier final reconciliation for control WP-0436-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-05", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-05", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-05", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-05", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier final reconciliation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_temperature_c_06(record):
    """Evaluate storage temperature for control WP-0436-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-06", "metric": "temperature_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-06", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-06", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-06", "metric": "temperature_c", "label": "storage temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage temperature must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_aisle_obstruction_count_07(record):
    """Evaluate aisle obstructions for control WP-0436-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-07", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-07", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-07", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-07", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "aisle obstructions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_crossdock_share_pct_08(record):
    """Evaluate cross-dock share for control WP-0436-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-08", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-08", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-08", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-08", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "cross-dock share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_maintenance_due_days_09(record):
    """Evaluate maintenance due for control WP-0436-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-09", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-09", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-09", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-09", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "maintenance due falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_capacity_pct_10(record):
    """Evaluate supplier capacity utilization for control WP-0436-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-10", "metric": "supplier_capacity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-10", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-10", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-10", "metric": "supplier_capacity_pct", "label": "supplier capacity utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_replication_lag_seconds_11(record):
    """Evaluate replication lag for control WP-0436-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replication_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-11", "metric": "replication_lag_seconds",
            "status": "insufficient_data",
            "severity": "high", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-11", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-11", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-11", "metric": "replication_lag_seconds", "label": "replication lag",
        "status": "breach", "severity": "high", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replication lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_economic_order_qty_12(record):
    """Evaluate economic order quantity for control WP-0436-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("economic_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-12", "metric": "economic_order_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-12", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-12", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-12", "metric": "economic_order_qty", "label": "economic order quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "economic order quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_break_overdue_minutes_13(record):
    """Evaluate break overdue for control WP-0436-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-13", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-13", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-13", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-13", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "break overdue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_donation_age_days_14(record):
    """Evaluate donation processing age for control WP-0436-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-14", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-14", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-14", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-14", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "donation processing age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_high_value_variance_15(record):
    """Evaluate high-value inventory variance for control WP-0436-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-15", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-15", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-15", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-15", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "high-value inventory variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_incompatible_storage_count_16(record):
    """Evaluate incompatible storage pairs for control WP-0436-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incompatible_storage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-16", "metric": "incompatible_storage_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "pairs",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-16", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-16", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-16", "metric": "incompatible_storage_count", "label": "incompatible storage pairs",
        "status": "breach", "severity": "critical", "unit": "pairs",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "incompatible storage pairs exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_license_validity_days_17(record):
    """Evaluate license validity for control WP-0436-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-17", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-17", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-17", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-17", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "license validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_business_continuity_test_age_days_18(record):
    """Evaluate business continuity test age for control WP-0436-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("business_continuity_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-18", "metric": "business_continuity_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-18", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-18", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-18", "metric": "business_continuity_test_age_days", "label": "business continuity test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "business continuity test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_etl_lag_minutes_19(record):
    """Evaluate ETL lag for control WP-0436-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("etl_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-19", "metric": "etl_lag_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-19", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-19", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-19", "metric": "etl_lag_minutes", "label": "ETL lag",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "ETL lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_uom_conversion_gap_count_20(record):
    """Evaluate unit conversion gaps for control WP-0436-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("uom_conversion_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-20", "metric": "uom_conversion_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-20", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-20", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-20", "metric": "uom_conversion_gap_count", "label": "unit conversion gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 23, "comparison": "max",
        "finding": "unit conversion gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_obsolete_sku_count_21(record):
    """Evaluate obsolete SKUs for control WP-0436-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-21", "metric": "obsolete_sku_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "SKUs",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-21", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-21", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-21", "metric": "obsolete_sku_count", "label": "obsolete SKUs",
        "status": "breach", "severity": "low", "unit": "SKUs",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "obsolete SKUs falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_carrier_rate_variance_pct_22(record):
    """Evaluate carrier rate variance for control WP-0436-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-22", "metric": "carrier_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-22", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-22", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-22", "metric": "carrier_rate_variance_pct", "label": "carrier rate variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier rate variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_insurance_claim_count_23(record):
    """Evaluate insurance claims for control WP-0436-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-23", "metric": "insurance_claim_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-23", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-23", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-23", "metric": "insurance_claim_count", "label": "insurance claims",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insurance claims must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_roadside_assistance_age_days_24(record):
    """Evaluate roadside assistance review age for control WP-0436-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("roadside_assistance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0436-24", "metric": "roadside_assistance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0436-24", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0436-24", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0436-24", "metric": "roadside_assistance_age_days", "label": "roadside assistance review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "roadside assistance review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_control_owner_gap_count_01, assess_supplier_three_way_match_pct_02, assess_supplier_process_capability_score_03, assess_supplier_kpi_data_quality_pct_04, assess_supplier_final_reconciliation_pct_05, assess_temperature_c_06, assess_aisle_obstruction_count_07, assess_crossdock_share_pct_08, assess_maintenance_due_days_09, assess_supplier_capacity_pct_10, assess_replication_lag_seconds_11, assess_economic_order_qty_12, assess_break_overdue_minutes_13, assess_donation_age_days_14, assess_high_value_variance_15, assess_incompatible_storage_count_16, assess_license_validity_days_17, assess_business_continuity_test_age_days_18, assess_etl_lag_minutes_19, assess_uom_conversion_gap_count_20, assess_obsolete_sku_count_21, assess_carrier_rate_variance_pct_22, assess_insurance_claim_count_23, assess_roadside_assistance_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

