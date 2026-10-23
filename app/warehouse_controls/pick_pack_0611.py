"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_site_flood_risk_score_01(record):
    """Evaluate supplier site flood risk for control WP-0611-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_flood_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-01", "metric": "supplier_site_flood_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-01", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-01", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-01", "metric": "supplier_site_flood_risk_score", "label": "supplier site flood risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier site flood risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_alternate_site_count_02(record):
    """Evaluate supplier alternate sites for control WP-0611-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_site_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-02", "metric": "supplier_alternate_site_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "sites",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-02", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-02", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-02", "metric": "supplier_alternate_site_count", "label": "supplier alternate sites",
        "status": "breach", "severity": "low", "unit": "sites",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier alternate sites must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_minor_finding_count_03(record):
    """Evaluate supplier minor findings for control WP-0611-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minor_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-03", "metric": "supplier_minor_finding_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-03", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-03", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-03", "metric": "supplier_minor_finding_count", "label": "supplier minor findings",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier minor findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_ethics_hotline_age_days_04(record):
    """Evaluate supplier ethics hotline review age for control WP-0611-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_hotline_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-04", "metric": "supplier_ethics_hotline_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-04", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-04", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-04", "metric": "supplier_ethics_hotline_age_days", "label": "supplier ethics hotline review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "supplier ethics hotline review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_contingency_stock_days_05(record):
    """Evaluate supplier contingency stock for control WP-0611-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contingency_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-05", "metric": "supplier_contingency_stock_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-05", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-05", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-05", "metric": "supplier_contingency_stock_days", "label": "supplier contingency stock",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier contingency stock must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_innovation_pipeline_count_06(record):
    """Evaluate supplier innovation pipeline for control WP-0611-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_innovation_pipeline_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-06", "metric": "supplier_innovation_pipeline_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-06", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-06", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-06", "metric": "supplier_innovation_pipeline_count", "label": "supplier innovation pipeline",
        "status": "breach", "severity": "low", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier innovation pipeline must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_search_mrr_07(record):
    """Evaluate supplier search MRR for control WP-0611-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_search_mrr")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-07", "metric": "supplier_search_mrr",
            "status": "insufficient_data",
            "severity": "medium", "unit": "score",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-07", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-07", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-07", "metric": "supplier_search_mrr", "label": "supplier search MRR",
        "status": "breach", "severity": "medium", "unit": "score",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier search MRR exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_load_test_age_days_08(record):
    """Evaluate supplier load-test age for control WP-0611-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_load_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-08", "metric": "supplier_load_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 80,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-08", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-08", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 80
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-08", "metric": "supplier_load_test_age_days", "label": "supplier load-test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 80, "comparison": "min",
        "finding": "supplier load-test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_patent_dispute_count_09(record):
    """Evaluate supplier patent disputes for control WP-0611-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patent_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-09", "metric": "supplier_patent_dispute_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-09", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-09", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-09", "metric": "supplier_patent_dispute_count", "label": "supplier patent disputes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier patent disputes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_control_owner_gap_count_10(record):
    """Evaluate supplier control-owner gaps for control WP-0611-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-10", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-10", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-10", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-10", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control-owner gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_three_way_match_pct_11(record):
    """Evaluate supplier three-way match for control WP-0611-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-11", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-11", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-11", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-11", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier three-way match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_process_capability_score_12(record):
    """Evaluate supplier process capability for control WP-0611-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-12", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-12", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-12", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-12", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 29, "comparison": "min",
        "finding": "supplier process capability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_kpi_data_quality_pct_13(record):
    """Evaluate supplier KPI data quality for control WP-0611-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-13", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-13", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-13", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-13", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier KPI data quality must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_final_reconciliation_pct_14(record):
    """Evaluate supplier final reconciliation for control WP-0611-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-14", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-14", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-14", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-14", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier final reconciliation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_temperature_c_15(record):
    """Evaluate storage temperature for control WP-0611-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-15", "metric": "temperature_c",
            "status": "insufficient_data",
            "severity": "medium", "unit": "C",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-15", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-15", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-15", "metric": "temperature_c", "label": "storage temperature",
        "status": "breach", "severity": "medium", "unit": "C",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "storage temperature exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_aisle_obstruction_count_16(record):
    """Evaluate aisle obstructions for control WP-0611-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-16", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-16", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-16", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-16", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 73, "comparison": "min",
        "finding": "aisle obstructions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_crossdock_share_pct_17(record):
    """Evaluate cross-dock share for control WP-0611-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-17", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-17", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-17", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-17", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cross-dock share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_maintenance_due_days_18(record):
    """Evaluate maintenance due for control WP-0611-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-18", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-18", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-18", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-18", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "maintenance due must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_capacity_pct_19(record):
    """Evaluate supplier capacity utilization for control WP-0611-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-19", "metric": "supplier_capacity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-19", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-19", "metric": "supplier_capacity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-19", "metric": "supplier_capacity_pct", "label": "supplier capacity utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "supplier capacity utilization exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_replication_lag_seconds_20(record):
    """Evaluate replication lag for control WP-0611-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replication_lag_seconds")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-20", "metric": "replication_lag_seconds",
            "status": "insufficient_data",
            "severity": "high", "unit": "seconds",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-20", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-20", "metric": "replication_lag_seconds", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-20", "metric": "replication_lag_seconds", "label": "replication lag",
        "status": "breach", "severity": "high", "unit": "seconds",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "replication lag falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_economic_order_qty_21(record):
    """Evaluate economic order quantity for control WP-0611-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("economic_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-21", "metric": "economic_order_qty",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-21", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-21", "metric": "economic_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-21", "metric": "economic_order_qty", "label": "economic order quantity",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "economic order quantity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_break_overdue_minutes_22(record):
    """Evaluate break overdue for control WP-0611-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-22", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-22", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-22", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-22", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "break overdue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_donation_age_days_23(record):
    """Evaluate donation processing age for control WP-0611-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-23", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-23", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-23", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-23", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "donation processing age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_high_value_variance_24(record):
    """Evaluate high-value inventory variance for control WP-0611-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0611-24", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "currency",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0611-24", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0611-24", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0611-24", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "high", "unit": "currency",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "high-value inventory variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_site_flood_risk_score_01, assess_supplier_alternate_site_count_02, assess_supplier_minor_finding_count_03, assess_supplier_ethics_hotline_age_days_04, assess_supplier_contingency_stock_days_05, assess_supplier_innovation_pipeline_count_06, assess_supplier_search_mrr_07, assess_supplier_load_test_age_days_08, assess_supplier_patent_dispute_count_09, assess_supplier_control_owner_gap_count_10, assess_supplier_three_way_match_pct_11, assess_supplier_process_capability_score_12, assess_supplier_kpi_data_quality_pct_13, assess_supplier_final_reconciliation_pct_14, assess_temperature_c_15, assess_aisle_obstruction_count_16, assess_crossdock_share_pct_17, assess_maintenance_due_days_18, assess_supplier_capacity_pct_19, assess_replication_lag_seconds_20, assess_economic_order_qty_21, assess_break_overdue_minutes_22, assess_donation_age_days_23, assess_high_value_variance_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

