"""Operational control pack for returns control; rules are executable against warehouse records."""
from math import isfinite

def assess_invoice_duplicate_count_01(record):
    """Evaluate duplicate invoices for control WP-0152-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-01", "metric": "invoice_duplicate_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "invoices",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-01", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-01", "metric": "invoice_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-01", "metric": "invoice_duplicate_count", "label": "duplicate invoices",
        "status": "breach", "severity": "low", "unit": "invoices",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "duplicate invoices falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_putaway_travel_meters_02(record):
    """Evaluate putaway travel for control WP-0152-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_travel_meters")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-02", "metric": "putaway_travel_meters",
            "status": "insufficient_data",
            "severity": "medium", "unit": "meters",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-02", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-02", "metric": "putaway_travel_meters", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-02", "metric": "putaway_travel_meters", "label": "putaway travel",
        "status": "breach", "severity": "medium", "unit": "meters",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "putaway travel must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_credit_review_age_days_03(record):
    """Evaluate credit review age for control WP-0152-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credit_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-03", "metric": "credit_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-03", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-03", "metric": "credit_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-03", "metric": "credit_review_age_days", "label": "credit review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "credit review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_yard_move_count_04(record):
    """Evaluate yard moves for control WP-0152-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_move_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-04", "metric": "yard_move_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "moves",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-04", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-04", "metric": "yard_move_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-04", "metric": "yard_move_count", "label": "yard moves",
        "status": "breach", "severity": "critical", "unit": "moves",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "yard moves exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_inventory_carrying_cost_pct_05(record):
    """Evaluate inventory carrying cost for control WP-0152-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_carrying_cost_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-05", "metric": "inventory_carrying_cost_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-05", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-05", "metric": "inventory_carrying_cost_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-05", "metric": "inventory_carrying_cost_pct", "label": "inventory carrying cost",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "inventory carrying cost falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_commit_accuracy_pct_06(record):
    """Evaluate supplier commit accuracy for control WP-0152-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_commit_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-06", "metric": "supplier_commit_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-06", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-06", "metric": "supplier_commit_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-06", "metric": "supplier_commit_accuracy_pct", "label": "supplier commit accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier commit accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_api_error_pct_07(record):
    """Evaluate supplier API error rate for control WP-0152-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_api_error_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-07", "metric": "supplier_api_error_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-07", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-07", "metric": "supplier_api_error_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-07", "metric": "supplier_api_error_pct", "label": "supplier API error rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier API error rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_capacity_reservation_pct_08(record):
    """Evaluate supplier capacity reservation for control WP-0152-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_reservation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-08", "metric": "supplier_capacity_reservation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-08", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-08", "metric": "supplier_capacity_reservation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-08", "metric": "supplier_capacity_reservation_pct", "label": "supplier capacity reservation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier capacity reservation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_key_rotation_age_days_09(record):
    """Evaluate supplier key-rotation age for control WP-0152-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-09", "metric": "supplier_key_rotation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-09", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-09", "metric": "supplier_key_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-09", "metric": "supplier_key_rotation_age_days", "label": "supplier key-rotation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "supplier key-rotation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_substitute_qualification_days_10(record):
    """Evaluate substitute qualification time for control WP-0152-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_qualification_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-10", "metric": "supplier_substitute_qualification_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-10", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-10", "metric": "supplier_substitute_qualification_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-10", "metric": "supplier_substitute_qualification_days", "label": "substitute qualification time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "substitute qualification time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_site_flood_risk_score_11(record):
    """Evaluate supplier site flood risk for control WP-0152-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_flood_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-11", "metric": "supplier_site_flood_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-11", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-11", "metric": "supplier_site_flood_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-11", "metric": "supplier_site_flood_risk_score", "label": "supplier site flood risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier site flood risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_alternate_site_count_12(record):
    """Evaluate supplier alternate sites for control WP-0152-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_alternate_site_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-12", "metric": "supplier_alternate_site_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "sites",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-12", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-12", "metric": "supplier_alternate_site_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-12", "metric": "supplier_alternate_site_count", "label": "supplier alternate sites",
        "status": "breach", "severity": "critical", "unit": "sites",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier alternate sites exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_minor_finding_count_13(record):
    """Evaluate supplier minor findings for control WP-0152-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_minor_finding_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-13", "metric": "supplier_minor_finding_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-13", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-13", "metric": "supplier_minor_finding_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-13", "metric": "supplier_minor_finding_count", "label": "supplier minor findings",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "supplier minor findings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_ethics_hotline_age_days_14(record):
    """Evaluate supplier ethics hotline review age for control WP-0152-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ethics_hotline_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-14", "metric": "supplier_ethics_hotline_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-14", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-14", "metric": "supplier_ethics_hotline_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-14", "metric": "supplier_ethics_hotline_age_days", "label": "supplier ethics hotline review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ethics hotline review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_contingency_stock_days_15(record):
    """Evaluate supplier contingency stock for control WP-0152-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contingency_stock_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-15", "metric": "supplier_contingency_stock_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-15", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-15", "metric": "supplier_contingency_stock_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-15", "metric": "supplier_contingency_stock_days", "label": "supplier contingency stock",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contingency stock must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_innovation_pipeline_count_16(record):
    """Evaluate supplier innovation pipeline for control WP-0152-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_innovation_pipeline_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-16", "metric": "supplier_innovation_pipeline_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-16", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-16", "metric": "supplier_innovation_pipeline_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-16", "metric": "supplier_innovation_pipeline_count", "label": "supplier innovation pipeline",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier innovation pipeline exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_search_mrr_17(record):
    """Evaluate supplier search MRR for control WP-0152-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_search_mrr")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-17", "metric": "supplier_search_mrr",
            "status": "insufficient_data",
            "severity": "low", "unit": "score",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-17", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-17", "metric": "supplier_search_mrr", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-17", "metric": "supplier_search_mrr", "label": "supplier search MRR",
        "status": "breach", "severity": "low", "unit": "score",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier search MRR falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_load_test_age_days_18(record):
    """Evaluate supplier load-test age for control WP-0152-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_load_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-18", "metric": "supplier_load_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-18", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-18", "metric": "supplier_load_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-18", "metric": "supplier_load_test_age_days", "label": "supplier load-test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier load-test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_patent_dispute_count_19(record):
    """Evaluate supplier patent disputes for control WP-0152-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_patent_dispute_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-19", "metric": "supplier_patent_dispute_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-19", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-19", "metric": "supplier_patent_dispute_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-19", "metric": "supplier_patent_dispute_count", "label": "supplier patent disputes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier patent disputes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_control_owner_gap_count_20(record):
    """Evaluate supplier control-owner gaps for control WP-0152-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-20", "metric": "supplier_control_owner_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-20", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-20", "metric": "supplier_control_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-20", "metric": "supplier_control_owner_gap_count", "label": "supplier control-owner gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier control-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

def assess_supplier_three_way_match_pct_21(record):
    """Evaluate supplier three-way match for control WP-0152-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_three_way_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-21", "metric": "supplier_three_way_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-21", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-21", "metric": "supplier_three_way_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-21", "metric": "supplier_three_way_match_pct", "label": "supplier three-way match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "supplier three-way match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "returns control",
    }

def assess_supplier_process_capability_score_22(record):
    """Evaluate supplier process capability for control WP-0152-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_capability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-22", "metric": "supplier_process_capability_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-22", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-22", "metric": "supplier_process_capability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-22", "metric": "supplier_process_capability_score", "label": "supplier process capability",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier process capability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "returns control",
    }

def assess_supplier_kpi_data_quality_pct_23(record):
    """Evaluate supplier KPI data quality for control WP-0152-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_kpi_data_quality_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-23", "metric": "supplier_kpi_data_quality_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-23", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-23", "metric": "supplier_kpi_data_quality_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-23", "metric": "supplier_kpi_data_quality_pct", "label": "supplier KPI data quality",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier KPI data quality must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "returns control",
    }

def assess_supplier_final_reconciliation_pct_24(record):
    """Evaluate supplier final reconciliation for control WP-0152-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_final_reconciliation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0152-24", "metric": "supplier_final_reconciliation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0152-24", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0152-24", "metric": "supplier_final_reconciliation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0152-24", "metric": "supplier_final_reconciliation_pct", "label": "supplier final reconciliation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier final reconciliation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "returns control",
    }

RULES = (assess_invoice_duplicate_count_01, assess_putaway_travel_meters_02, assess_credit_review_age_days_03, assess_yard_move_count_04, assess_inventory_carrying_cost_pct_05, assess_supplier_commit_accuracy_pct_06, assess_supplier_api_error_pct_07, assess_supplier_capacity_reservation_pct_08, assess_supplier_key_rotation_age_days_09, assess_supplier_substitute_qualification_days_10, assess_supplier_site_flood_risk_score_11, assess_supplier_alternate_site_count_12, assess_supplier_minor_finding_count_13, assess_supplier_ethics_hotline_age_days_14, assess_supplier_contingency_stock_days_15, assess_supplier_innovation_pipeline_count_16, assess_supplier_search_mrr_17, assess_supplier_load_test_age_days_18, assess_supplier_patent_dispute_count_19, assess_supplier_control_owner_gap_count_20, assess_supplier_three_way_match_pct_21, assess_supplier_process_capability_score_22, assess_supplier_kpi_data_quality_pct_23, assess_supplier_final_reconciliation_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

