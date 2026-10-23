"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_audit_log_retention_days_01(record):
    """Evaluate supplier audit-log retention for control WP-0355-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-01", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-01", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-01", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-01", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit-log retention must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_requalification_age_days_02(record):
    """Evaluate supplier requalification age for control WP-0355-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_requalification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-02", "metric": "supplier_requalification_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-02", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-02", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-02", "metric": "supplier_requalification_age_days", "label": "supplier requalification age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier requalification age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_fire_risk_score_03(record):
    """Evaluate supplier site fire risk for control WP-0355-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-03", "metric": "supplier_fire_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-03", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-03", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-03", "metric": "supplier_fire_risk_score", "label": "supplier site fire risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier site fire risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_capacity_transfer_days_04(record):
    """Evaluate supplier capacity transfer time for control WP-0355-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-04", "metric": "supplier_capacity_transfer_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-04", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-04", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-04", "metric": "supplier_capacity_transfer_days", "label": "supplier capacity transfer time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier capacity transfer time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_observation_count_05(record):
    """Evaluate supplier observations for control WP-0355-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-05", "metric": "supplier_observation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-05", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-05", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-05", "metric": "supplier_observation_count", "label": "supplier observations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier observations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_bribery_training_pct_06(record):
    """Evaluate supplier anti-bribery training for control WP-0355-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bribery_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-06", "metric": "supplier_bribery_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-06", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-06", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-06", "metric": "supplier_bribery_training_pct", "label": "supplier anti-bribery training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier anti-bribery training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_recovery_drill_age_days_07(record):
    """Evaluate supplier recovery drill age for control WP-0355-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-07", "metric": "supplier_recovery_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 165,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-07", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-07", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 165
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-07", "metric": "supplier_recovery_drill_age_days", "label": "supplier recovery drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 165, "comparison": "max",
        "finding": "supplier recovery drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_technology_maturity_score_08(record):
    """Evaluate supplier technology maturity for control WP-0355-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_technology_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-08", "metric": "supplier_technology_maturity_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-08", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-08", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-08", "metric": "supplier_technology_maturity_score", "label": "supplier technology maturity",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier technology maturity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_ranking_ndcg_09(record):
    """Evaluate supplier ranking NDCG for control WP-0355-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ranking_ndcg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-09", "metric": "supplier_ranking_ndcg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "score",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-09", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-09", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-09", "metric": "supplier_ranking_ndcg", "label": "supplier ranking NDCG",
        "status": "breach", "severity": "critical", "unit": "score",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ranking NDCG must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_chaos_test_age_days_10(record):
    """Evaluate supplier chaos-test age for control WP-0355-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_chaos_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-10", "metric": "supplier_chaos_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-10", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-10", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-10", "metric": "supplier_chaos_test_age_days", "label": "supplier chaos-test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier chaos-test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_data_processing_agreement_pct_11(record):
    """Evaluate supplier DPA completeness for control WP-0355-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_processing_agreement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-11", "metric": "supplier_data_processing_agreement_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-11", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-11", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-11", "metric": "supplier_data_processing_agreement_pct", "label": "supplier DPA completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "supplier DPA completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_risk_register_age_days_12(record):
    """Evaluate supplier risk register age for control WP-0355-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_register_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-12", "metric": "supplier_risk_register_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-12", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-12", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-12", "metric": "supplier_risk_register_age_days", "label": "supplier risk register age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier risk register age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_receipt_before_invoice_pct_13(record):
    """Evaluate receipt-before-invoice compliance for control WP-0355-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_receipt_before_invoice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-13", "metric": "supplier_receipt_before_invoice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-13", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-13", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-13", "metric": "supplier_receipt_before_invoice_pct", "label": "receipt-before-invoice compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receipt-before-invoice compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_machine_uptime_pct_14(record):
    """Evaluate supplier machine uptime for control WP-0355-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_machine_uptime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-14", "metric": "supplier_machine_uptime_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-14", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-14", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-14", "metric": "supplier_machine_uptime_pct", "label": "supplier machine uptime",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier machine uptime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_metric_definition_gap_count_15(record):
    """Evaluate supplier metric-definition gaps for control WP-0355-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_metric_definition_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-15", "metric": "supplier_metric_definition_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-15", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-15", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-15", "metric": "supplier_metric_definition_gap_count", "label": "supplier metric-definition gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "supplier metric-definition gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_archive_completion_pct_16(record):
    """Evaluate supplier archive completion for control WP-0355-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_archive_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-16", "metric": "supplier_archive_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-16", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-16", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-16", "metric": "supplier_archive_completion_pct", "label": "supplier archive completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier archive completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_humidity_pct_17(record):
    """Evaluate storage humidity for control WP-0355-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-17", "metric": "humidity_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-17", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-17", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-17", "metric": "humidity_pct", "label": "storage humidity",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage humidity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_fire_exit_clearance_cm_18(record):
    """Evaluate fire exit clearance for control WP-0355-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_exit_clearance_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-18", "metric": "fire_exit_clearance_cm",
            "status": "insufficient_data",
            "severity": "low", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-18", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-18", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-18", "metric": "fire_exit_clearance_cm", "label": "fire exit clearance",
        "status": "breach", "severity": "low", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fire exit clearance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_slotting_score_19(record):
    """Evaluate slotting score for control WP-0355-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-19", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-19", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-19", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-19", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "slotting score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_mean_time_to_repair_hours_20(record):
    """Evaluate mean time to repair for control WP-0355-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-20", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-20", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-20", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-20", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "mean time to repair falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_risk_score_21(record):
    """Evaluate supplier risk for control WP-0355-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-21", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-21", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-21", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-21", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_database_lock_wait_ms_22(record):
    """Evaluate database lock wait for control WP-0355-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("database_lock_wait_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-22", "metric": "database_lock_wait_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-22", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-22", "metric": "database_lock_wait_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-22", "metric": "database_lock_wait_ms", "label": "database lock wait",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "database lock wait must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_min_order_qty_23(record):
    """Evaluate minimum order quantity for control WP-0355-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("min_order_qty")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-23", "metric": "min_order_qty",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-23", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-23", "metric": "min_order_qty", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-23", "metric": "min_order_qty", "label": "minimum order quantity",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "minimum order quantity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_rest_period_hours_24(record):
    """Evaluate rest period for control WP-0355-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rest_period_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0355-24", "metric": "rest_period_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0355-24", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0355-24", "metric": "rest_period_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0355-24", "metric": "rest_period_hours", "label": "rest period",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "rest period falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_audit_log_retention_days_01, assess_supplier_requalification_age_days_02, assess_supplier_fire_risk_score_03, assess_supplier_capacity_transfer_days_04, assess_supplier_observation_count_05, assess_supplier_bribery_training_pct_06, assess_supplier_recovery_drill_age_days_07, assess_supplier_technology_maturity_score_08, assess_supplier_ranking_ndcg_09, assess_supplier_chaos_test_age_days_10, assess_supplier_data_processing_agreement_pct_11, assess_supplier_risk_register_age_days_12, assess_supplier_receipt_before_invoice_pct_13, assess_supplier_machine_uptime_pct_14, assess_supplier_metric_definition_gap_count_15, assess_supplier_archive_completion_pct_16, assess_humidity_pct_17, assess_fire_exit_clearance_cm_18, assess_slotting_score_19, assess_mean_time_to_repair_hours_20, assess_supplier_risk_score_21, assess_database_lock_wait_ms_22, assess_min_order_qty_23, assess_rest_period_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

