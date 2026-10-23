"""Operational control pack for inventory integrity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_innovation_pipeline_count_01(record):
    """Evaluate supplier innovation pipeline for control WP-0113-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_innovation_pipeline_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-01", "metric": "supplier_innovation_pipeline_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "items",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-01", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-01", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-01", "metric": "supplier_innovation_pipeline_count", "label": "supplier innovation pipeline",
        "status": "breach", "severity": "medium", "unit": "items",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier innovation pipeline exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_search_mrr_02(record):
    """Evaluate supplier search MRR for control WP-0113-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_search_mrr")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-02", "metric": "supplier_search_mrr",
            "status": "insufficient_data",
            "severity": "high", "unit": "score",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-02", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-02", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-02", "metric": "supplier_search_mrr", "label": "supplier search MRR",
        "status": "breach", "severity": "high", "unit": "score",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier search MRR falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_load_test_age_days_03(record):
    """Evaluate supplier load-test age for control WP-0113-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_load_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-03", "metric": "supplier_load_test_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-03", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-03", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-03", "metric": "supplier_load_test_age_days", "label": "supplier load-test age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier load-test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_patent_dispute_count_04(record):
    """Evaluate supplier patent disputes for control WP-0113-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patent_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-04", "metric": "supplier_patent_dispute_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-04", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-04", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-04", "metric": "supplier_patent_dispute_count", "label": "supplier patent disputes",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier patent disputes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_control_owner_gap_count_05(record):
    """Evaluate supplier control-owner gaps for control WP-0113-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-05", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-05", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-05", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-05", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "supplier control-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_three_way_match_pct_06(record):
    """Evaluate supplier three-way match for control WP-0113-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-06", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-06", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-06", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-06", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier three-way match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_supplier_process_capability_score_07(record):
    """Evaluate supplier process capability for control WP-0113-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-07", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-07", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-07", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-07", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process capability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_supplier_kpi_data_quality_pct_08(record):
    """Evaluate supplier KPI data quality for control WP-0113-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-08", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-08", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-08", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-08", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KPI data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_supplier_final_reconciliation_pct_09(record):
    """Evaluate supplier final reconciliation for control WP-0113-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-09", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-09", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-09", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-09", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "supplier final reconciliation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_temperature_c_10(record):
    """Evaluate storage temperature for control WP-0113-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-10", "metric": "temperature_c",
            "status": "insufficient_data",
            "severity": "high", "unit": "C",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-10", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-10", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-10", "metric": "temperature_c", "label": "storage temperature",
        "status": "breach", "severity": "high", "unit": "C",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "storage temperature falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_aisle_obstruction_count_11(record):
    """Evaluate aisle obstructions for control WP-0113-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-11", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-11", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-11", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-11", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "aisle obstructions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_crossdock_share_pct_12(record):
    """Evaluate cross-dock share for control WP-0113-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-12", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-12", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-12", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-12", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "cross-dock share must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_maintenance_due_days_13(record):
    """Evaluate maintenance due for control WP-0113-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-13", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-13", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-13", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-13", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "maintenance due exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_supplier_capacity_pct_14(record):
    """Evaluate supplier capacity utilization for control WP-0113-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-14", "metric": "supplier_capacity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-14", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-14", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-14", "metric": "supplier_capacity_pct", "label": "supplier capacity utilization",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier capacity utilization falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_replication_lag_seconds_15(record):
    """Evaluate replication lag for control WP-0113-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replication_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-15", "metric": "replication_lag_seconds",
            "status": "insufficient_data",
            "severity": "critical", "unit": "seconds",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-15", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-15", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-15", "metric": "replication_lag_seconds", "label": "replication lag",
        "status": "breach", "severity": "critical", "unit": "seconds",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replication lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_economic_order_qty_16(record):
    """Evaluate economic order quantity for control WP-0113-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("economic_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-16", "metric": "economic_order_qty",
            "status": "insufficient_data",
            "severity": "low", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-16", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-16", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-16", "metric": "economic_order_qty", "label": "economic order quantity",
        "status": "breach", "severity": "low", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "economic order quantity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_break_overdue_minutes_17(record):
    """Evaluate break overdue for control WP-0113-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-17", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-17", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-17", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-17", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "break overdue exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_donation_age_days_18(record):
    """Evaluate donation processing age for control WP-0113-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-18", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-18", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-18", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-18", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "donation processing age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_high_value_variance_19(record):
    """Evaluate high-value inventory variance for control WP-0113-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-19", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-19", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-19", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-19", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "high-value inventory variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_incompatible_storage_count_20(record):
    """Evaluate incompatible storage pairs for control WP-0113-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incompatible_storage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-20", "metric": "incompatible_storage_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "pairs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-20", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-20", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-20", "metric": "incompatible_storage_count", "label": "incompatible storage pairs",
        "status": "breach", "severity": "low", "unit": "pairs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incompatible storage pairs must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

def assess_license_validity_days_21(record):
    """Evaluate license validity for control WP-0113-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-21", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 149,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-21", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-21", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 149
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-21", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 149, "comparison": "max",
        "finding": "license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "inventory integrity",
    }

def assess_business_continuity_test_age_days_22(record):
    """Evaluate business continuity test age for control WP-0113-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("business_continuity_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-22", "metric": "business_continuity_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-22", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-22", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-22", "metric": "business_continuity_test_age_days", "label": "business continuity test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "business continuity test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "inventory integrity",
    }

def assess_etl_lag_minutes_23(record):
    """Evaluate ETL lag for control WP-0113-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("etl_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-23", "metric": "etl_lag_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-23", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-23", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-23", "metric": "etl_lag_minutes", "label": "ETL lag",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ETL lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "inventory integrity",
    }

def assess_uom_conversion_gap_count_24(record):
    """Evaluate unit conversion gaps for control WP-0113-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("uom_conversion_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0113-24", "metric": "uom_conversion_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0113-24", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0113-24", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0113-24", "metric": "uom_conversion_gap_count", "label": "unit conversion gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unit conversion gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "inventory integrity",
    }

RULES = (assess_supplier_innovation_pipeline_count_01, assess_supplier_search_mrr_02, assess_supplier_load_test_age_days_03, assess_supplier_patent_dispute_count_04, assess_supplier_control_owner_gap_count_05, assess_supplier_three_way_match_pct_06, assess_supplier_process_capability_score_07, assess_supplier_kpi_data_quality_pct_08, assess_supplier_final_reconciliation_pct_09, assess_temperature_c_10, assess_aisle_obstruction_count_11, assess_crossdock_share_pct_12, assess_maintenance_due_days_13, assess_supplier_capacity_pct_14, assess_replication_lag_seconds_15, assess_economic_order_qty_16, assess_break_overdue_minutes_17, assess_donation_age_days_18, assess_high_value_variance_19, assess_incompatible_storage_count_20, assess_license_validity_days_21, assess_business_continuity_test_age_days_22, assess_etl_lag_minutes_23, assess_uom_conversion_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

