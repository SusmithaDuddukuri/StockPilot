"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_minor_finding_count_01(record):
    """Evaluate supplier minor findings for control WP-0045-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minor_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-01", "metric": "supplier_minor_finding_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-01", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-01", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-01", "metric": "supplier_minor_finding_count", "label": "supplier minor findings",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier minor findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_ethics_hotline_age_days_02(record):
    """Evaluate supplier ethics hotline review age for control WP-0045-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_hotline_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-02", "metric": "supplier_ethics_hotline_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-02", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-02", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-02", "metric": "supplier_ethics_hotline_age_days", "label": "supplier ethics hotline review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier ethics hotline review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_contingency_stock_days_03(record):
    """Evaluate supplier contingency stock for control WP-0045-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contingency_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-03", "metric": "supplier_contingency_stock_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-03", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-03", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-03", "metric": "supplier_contingency_stock_days", "label": "supplier contingency stock",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier contingency stock must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_innovation_pipeline_count_04(record):
    """Evaluate supplier innovation pipeline for control WP-0045-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_innovation_pipeline_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-04", "metric": "supplier_innovation_pipeline_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-04", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-04", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-04", "metric": "supplier_innovation_pipeline_count", "label": "supplier innovation pipeline",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier innovation pipeline must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_search_mrr_05(record):
    """Evaluate supplier search MRR for control WP-0045-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_search_mrr")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-05", "metric": "supplier_search_mrr",
            "status": "insufficient_data",
            "severity": "medium", "unit": "score",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-05", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-05", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-05", "metric": "supplier_search_mrr", "label": "supplier search MRR",
        "status": "breach", "severity": "medium", "unit": "score",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier search MRR exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_load_test_age_days_06(record):
    """Evaluate supplier load-test age for control WP-0045-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_load_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-06", "metric": "supplier_load_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-06", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-06", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-06", "metric": "supplier_load_test_age_days", "label": "supplier load-test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier load-test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_patent_dispute_count_07(record):
    """Evaluate supplier patent disputes for control WP-0045-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patent_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-07", "metric": "supplier_patent_dispute_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-07", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-07", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-07", "metric": "supplier_patent_dispute_count", "label": "supplier patent disputes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier patent disputes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_control_owner_gap_count_08(record):
    """Evaluate supplier control-owner gaps for control WP-0045-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-08", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-08", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-08", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-08", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control-owner gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_three_way_match_pct_09(record):
    """Evaluate supplier three-way match for control WP-0045-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-09", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-09", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-09", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-09", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier three-way match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_process_capability_score_10(record):
    """Evaluate supplier process capability for control WP-0045-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-10", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-10", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-10", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-10", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "supplier process capability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_kpi_data_quality_pct_11(record):
    """Evaluate supplier KPI data quality for control WP-0045-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-11", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-11", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-11", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-11", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier KPI data quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_final_reconciliation_pct_12(record):
    """Evaluate supplier final reconciliation for control WP-0045-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-12", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-12", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-12", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-12", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier final reconciliation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_temperature_c_13(record):
    """Evaluate storage temperature for control WP-0045-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-13", "metric": "temperature_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-13", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-13", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-13", "metric": "temperature_c", "label": "storage temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "storage temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_aisle_obstruction_count_14(record):
    """Evaluate aisle obstructions for control WP-0045-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-14", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-14", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-14", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-14", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "aisle obstructions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_crossdock_share_pct_15(record):
    """Evaluate cross-dock share for control WP-0045-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-15", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-15", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-15", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-15", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cross-dock share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_maintenance_due_days_16(record):
    """Evaluate maintenance due for control WP-0045-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-16", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-16", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-16", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-16", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "maintenance due must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_capacity_pct_17(record):
    """Evaluate supplier capacity utilization for control WP-0045-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-17", "metric": "supplier_capacity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-17", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-17", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-17", "metric": "supplier_capacity_pct", "label": "supplier capacity utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier capacity utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_replication_lag_seconds_18(record):
    """Evaluate replication lag for control WP-0045-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replication_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-18", "metric": "replication_lag_seconds",
            "status": "insufficient_data",
            "severity": "high", "unit": "seconds",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-18", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-18", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-18", "metric": "replication_lag_seconds", "label": "replication lag",
        "status": "breach", "severity": "high", "unit": "seconds",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "replication lag falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_economic_order_qty_19(record):
    """Evaluate economic order quantity for control WP-0045-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("economic_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-19", "metric": "economic_order_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-19", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-19", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-19", "metric": "economic_order_qty", "label": "economic order quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "economic order quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_break_overdue_minutes_20(record):
    """Evaluate break overdue for control WP-0045-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-20", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-20", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-20", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-20", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "break overdue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_donation_age_days_21(record):
    """Evaluate donation processing age for control WP-0045-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-21", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-21", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-21", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-21", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "donation processing age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_high_value_variance_22(record):
    """Evaluate high-value inventory variance for control WP-0045-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-22", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-22", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-22", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-22", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "high-value inventory variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_incompatible_storage_count_23(record):
    """Evaluate incompatible storage pairs for control WP-0045-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incompatible_storage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-23", "metric": "incompatible_storage_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "pairs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-23", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-23", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-23", "metric": "incompatible_storage_count", "label": "incompatible storage pairs",
        "status": "breach", "severity": "critical", "unit": "pairs",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "incompatible storage pairs must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_license_validity_days_24(record):
    """Evaluate license validity for control WP-0045-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0045-24", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0045-24", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0045-24", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0045-24", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "license validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_supplier_minor_finding_count_01, assess_supplier_ethics_hotline_age_days_02, assess_supplier_contingency_stock_days_03, assess_supplier_innovation_pipeline_count_04, assess_supplier_search_mrr_05, assess_supplier_load_test_age_days_06, assess_supplier_patent_dispute_count_07, assess_supplier_control_owner_gap_count_08, assess_supplier_three_way_match_pct_09, assess_supplier_process_capability_score_10, assess_supplier_kpi_data_quality_pct_11, assess_supplier_final_reconciliation_pct_12, assess_temperature_c_13, assess_aisle_obstruction_count_14, assess_crossdock_share_pct_15, assess_maintenance_due_days_16, assess_supplier_capacity_pct_17, assess_replication_lag_seconds_18, assess_economic_order_qty_19, assess_break_overdue_minutes_20, assess_donation_age_days_21, assess_high_value_variance_22, assess_incompatible_storage_count_23, assess_license_validity_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

