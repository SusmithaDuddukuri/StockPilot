"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_inventory_carrying_cost_pct_01(record):
    """Evaluate inventory carrying cost for control WP-0475-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-01", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-01", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-01", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-01", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory carrying cost must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_commit_accuracy_pct_02(record):
    """Evaluate supplier commit accuracy for control WP-0475-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_commit_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-02", "metric": "supplier_commit_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-02", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-02", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-02", "metric": "supplier_commit_accuracy_pct", "label": "supplier commit accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier commit accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_api_error_pct_03(record):
    """Evaluate supplier API error rate for control WP-0475-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-03", "metric": "supplier_api_error_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-03", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-03", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-03", "metric": "supplier_api_error_pct", "label": "supplier API error rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier API error rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_capacity_reservation_pct_04(record):
    """Evaluate supplier capacity reservation for control WP-0475-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_reservation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-04", "metric": "supplier_capacity_reservation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-04", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-04", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-04", "metric": "supplier_capacity_reservation_pct", "label": "supplier capacity reservation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier capacity reservation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_key_rotation_age_days_05(record):
    """Evaluate supplier key-rotation age for control WP-0475-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-05", "metric": "supplier_key_rotation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-05", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-05", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-05", "metric": "supplier_key_rotation_age_days", "label": "supplier key-rotation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier key-rotation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_substitute_qualification_days_06(record):
    """Evaluate substitute qualification time for control WP-0475-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_qualification_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-06", "metric": "supplier_substitute_qualification_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-06", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-06", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-06", "metric": "supplier_substitute_qualification_days", "label": "substitute qualification time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "substitute qualification time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_site_flood_risk_score_07(record):
    """Evaluate supplier site flood risk for control WP-0475-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_flood_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-07", "metric": "supplier_site_flood_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-07", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-07", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-07", "metric": "supplier_site_flood_risk_score", "label": "supplier site flood risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier site flood risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_alternate_site_count_08(record):
    """Evaluate supplier alternate sites for control WP-0475-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_site_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-08", "metric": "supplier_alternate_site_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "sites",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-08", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-08", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-08", "metric": "supplier_alternate_site_count", "label": "supplier alternate sites",
        "status": "breach", "severity": "high", "unit": "sites",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier alternate sites falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_minor_finding_count_09(record):
    """Evaluate supplier minor findings for control WP-0475-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minor_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-09", "metric": "supplier_minor_finding_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-09", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-09", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-09", "metric": "supplier_minor_finding_count", "label": "supplier minor findings",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier minor findings must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_ethics_hotline_age_days_10(record):
    """Evaluate supplier ethics hotline review age for control WP-0475-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_hotline_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-10", "metric": "supplier_ethics_hotline_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-10", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-10", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-10", "metric": "supplier_ethics_hotline_age_days", "label": "supplier ethics hotline review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ethics hotline review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_contingency_stock_days_11(record):
    """Evaluate supplier contingency stock for control WP-0475-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contingency_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-11", "metric": "supplier_contingency_stock_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-11", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-11", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-11", "metric": "supplier_contingency_stock_days", "label": "supplier contingency stock",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "supplier contingency stock exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_innovation_pipeline_count_12(record):
    """Evaluate supplier innovation pipeline for control WP-0475-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_innovation_pipeline_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-12", "metric": "supplier_innovation_pipeline_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-12", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-12", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-12", "metric": "supplier_innovation_pipeline_count", "label": "supplier innovation pipeline",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "supplier innovation pipeline falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_search_mrr_13(record):
    """Evaluate supplier search MRR for control WP-0475-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_search_mrr")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-13", "metric": "supplier_search_mrr",
            "status": "insufficient_data",
            "severity": "critical", "unit": "score",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-13", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-13", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-13", "metric": "supplier_search_mrr", "label": "supplier search MRR",
        "status": "breach", "severity": "critical", "unit": "score",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier search MRR must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_load_test_age_days_14(record):
    """Evaluate supplier load-test age for control WP-0475-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_load_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-14", "metric": "supplier_load_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-14", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-14", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-14", "metric": "supplier_load_test_age_days", "label": "supplier load-test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier load-test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_patent_dispute_count_15(record):
    """Evaluate supplier patent disputes for control WP-0475-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patent_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-15", "metric": "supplier_patent_dispute_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-15", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-15", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-15", "metric": "supplier_patent_dispute_count", "label": "supplier patent disputes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier patent disputes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_control_owner_gap_count_16(record):
    """Evaluate supplier control-owner gaps for control WP-0475-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-16", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-16", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-16", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-16", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "supplier control-owner gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_three_way_match_pct_17(record):
    """Evaluate supplier three-way match for control WP-0475-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-17", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-17", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-17", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-17", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier three-way match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_process_capability_score_18(record):
    """Evaluate supplier process capability for control WP-0475-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-18", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-18", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-18", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-18", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process capability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_kpi_data_quality_pct_19(record):
    """Evaluate supplier KPI data quality for control WP-0475-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-19", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-19", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-19", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-19", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier KPI data quality exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_final_reconciliation_pct_20(record):
    """Evaluate supplier final reconciliation for control WP-0475-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-20", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-20", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-20", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-20", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "supplier final reconciliation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_temperature_c_21(record):
    """Evaluate storage temperature for control WP-0475-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_c")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-21", "metric": "temperature_c",
            "status": "insufficient_data",
            "severity": "critical", "unit": "C",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-21", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-21", "metric": "temperature_c", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-21", "metric": "temperature_c", "label": "storage temperature",
        "status": "breach", "severity": "critical", "unit": "C",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage temperature must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_aisle_obstruction_count_22(record):
    """Evaluate aisle obstructions for control WP-0475-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("aisle_obstruction_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-22", "metric": "aisle_obstruction_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-22", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-22", "metric": "aisle_obstruction_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-22", "metric": "aisle_obstruction_count", "label": "aisle obstructions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "aisle obstructions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_crossdock_share_pct_23(record):
    """Evaluate cross-dock share for control WP-0475-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("crossdock_share_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-23", "metric": "crossdock_share_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-23", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-23", "metric": "crossdock_share_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-23", "metric": "crossdock_share_pct", "label": "cross-dock share",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "cross-dock share exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_maintenance_due_days_24(record):
    """Evaluate maintenance due for control WP-0475-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("maintenance_due_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0475-24", "metric": "maintenance_due_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0475-24", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0475-24", "metric": "maintenance_due_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0475-24", "metric": "maintenance_due_days", "label": "maintenance due",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "maintenance due falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_inventory_carrying_cost_pct_01, assess_supplier_commit_accuracy_pct_02, assess_supplier_api_error_pct_03, assess_supplier_capacity_reservation_pct_04, assess_supplier_key_rotation_age_days_05, assess_supplier_substitute_qualification_days_06, assess_supplier_site_flood_risk_score_07, assess_supplier_alternate_site_count_08, assess_supplier_minor_finding_count_09, assess_supplier_ethics_hotline_age_days_10, assess_supplier_contingency_stock_days_11, assess_supplier_innovation_pipeline_count_12, assess_supplier_search_mrr_13, assess_supplier_load_test_age_days_14, assess_supplier_patent_dispute_count_15, assess_supplier_control_owner_gap_count_16, assess_supplier_three_way_match_pct_17, assess_supplier_process_capability_score_18, assess_supplier_kpi_data_quality_pct_19, assess_supplier_final_reconciliation_pct_20, assess_temperature_c_21, assess_aisle_obstruction_count_22, assess_crossdock_share_pct_23, assess_maintenance_due_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

