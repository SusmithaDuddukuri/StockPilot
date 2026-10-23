"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_fill_rate_pct_01(record):
    """Evaluate supplier fill rate for control WP-0666-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-01", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-01", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-01", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-01", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier fill rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_edi_success_pct_02(record):
    """Evaluate supplier EDI success for control WP-0666-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-02", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-02", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-02", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-02", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 43, "comparison": "max",
        "finding": "supplier EDI success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_forecast_sharing_pct_03(record):
    """Evaluate supplier forecast sharing for control WP-0666-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_sharing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-03", "metric": "supplier_forecast_sharing_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-03", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-03", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-03", "metric": "supplier_forecast_sharing_pct", "label": "supplier forecast sharing",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier forecast sharing falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_audit_log_retention_days_04(record):
    """Evaluate supplier audit-log retention for control WP-0666-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-04", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-04", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-04", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-04", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier audit-log retention must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_requalification_age_days_05(record):
    """Evaluate supplier requalification age for control WP-0666-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_requalification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-05", "metric": "supplier_requalification_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-05", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-05", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-05", "metric": "supplier_requalification_age_days", "label": "supplier requalification age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier requalification age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_fire_risk_score_06(record):
    """Evaluate supplier site fire risk for control WP-0666-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-06", "metric": "supplier_fire_risk_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-06", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-06", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-06", "metric": "supplier_fire_risk_score", "label": "supplier site fire risk",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 63, "comparison": "max",
        "finding": "supplier site fire risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_capacity_transfer_days_07(record):
    """Evaluate supplier capacity transfer time for control WP-0666-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-07", "metric": "supplier_capacity_transfer_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-07", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-07", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-07", "metric": "supplier_capacity_transfer_days", "label": "supplier capacity transfer time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "supplier capacity transfer time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_observation_count_08(record):
    """Evaluate supplier observations for control WP-0666-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-08", "metric": "supplier_observation_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-08", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-08", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-08", "metric": "supplier_observation_count", "label": "supplier observations",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier observations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_bribery_training_pct_09(record):
    """Evaluate supplier anti-bribery training for control WP-0666-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bribery_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-09", "metric": "supplier_bribery_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-09", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-09", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-09", "metric": "supplier_bribery_training_pct", "label": "supplier anti-bribery training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier anti-bribery training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_recovery_drill_age_days_10(record):
    """Evaluate supplier recovery drill age for control WP-0666-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-10", "metric": "supplier_recovery_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-10", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-10", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-10", "metric": "supplier_recovery_drill_age_days", "label": "supplier recovery drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier recovery drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_technology_maturity_score_11(record):
    """Evaluate supplier technology maturity for control WP-0666-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_technology_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-11", "metric": "supplier_technology_maturity_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-11", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-11", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-11", "metric": "supplier_technology_maturity_score", "label": "supplier technology maturity",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "supplier technology maturity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_ranking_ndcg_12(record):
    """Evaluate supplier ranking NDCG for control WP-0666-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ranking_ndcg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-12", "metric": "supplier_ranking_ndcg",
            "status": "insufficient_data",
            "severity": "medium", "unit": "score",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-12", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-12", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-12", "metric": "supplier_ranking_ndcg", "label": "supplier ranking NDCG",
        "status": "breach", "severity": "medium", "unit": "score",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ranking NDCG must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_chaos_test_age_days_13(record):
    """Evaluate supplier chaos-test age for control WP-0666-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_chaos_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-13", "metric": "supplier_chaos_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-13", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-13", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-13", "metric": "supplier_chaos_test_age_days", "label": "supplier chaos-test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier chaos-test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_data_processing_agreement_pct_14(record):
    """Evaluate supplier DPA completeness for control WP-0666-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_processing_agreement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-14", "metric": "supplier_data_processing_agreement_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-14", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-14", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-14", "metric": "supplier_data_processing_agreement_pct", "label": "supplier DPA completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier DPA completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_risk_register_age_days_15(record):
    """Evaluate supplier risk register age for control WP-0666-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_register_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-15", "metric": "supplier_risk_register_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-15", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-15", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-15", "metric": "supplier_risk_register_age_days", "label": "supplier risk register age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "supplier risk register age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_receipt_before_invoice_pct_16(record):
    """Evaluate receipt-before-invoice compliance for control WP-0666-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_receipt_before_invoice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-16", "metric": "supplier_receipt_before_invoice_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-16", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-16", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-16", "metric": "supplier_receipt_before_invoice_pct", "label": "receipt-before-invoice compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "receipt-before-invoice compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_machine_uptime_pct_17(record):
    """Evaluate supplier machine uptime for control WP-0666-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_machine_uptime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-17", "metric": "supplier_machine_uptime_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-17", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-17", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-17", "metric": "supplier_machine_uptime_pct", "label": "supplier machine uptime",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier machine uptime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_metric_definition_gap_count_18(record):
    """Evaluate supplier metric-definition gaps for control WP-0666-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_metric_definition_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-18", "metric": "supplier_metric_definition_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-18", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-18", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-18", "metric": "supplier_metric_definition_gap_count", "label": "supplier metric-definition gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier metric-definition gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_archive_completion_pct_19(record):
    """Evaluate supplier archive completion for control WP-0666-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_archive_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-19", "metric": "supplier_archive_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-19", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-19", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-19", "metric": "supplier_archive_completion_pct", "label": "supplier archive completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier archive completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_humidity_pct_20(record):
    """Evaluate storage humidity for control WP-0666-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-20", "metric": "humidity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-20", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-20", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-20", "metric": "humidity_pct", "label": "storage humidity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "storage humidity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_fire_exit_clearance_cm_21(record):
    """Evaluate fire exit clearance for control WP-0666-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_exit_clearance_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-21", "metric": "fire_exit_clearance_cm",
            "status": "insufficient_data",
            "severity": "high", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-21", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-21", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-21", "metric": "fire_exit_clearance_cm", "label": "fire exit clearance",
        "status": "breach", "severity": "high", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fire exit clearance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_slotting_score_22(record):
    """Evaluate slotting score for control WP-0666-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-22", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-22", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-22", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-22", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "slotting score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_mean_time_to_repair_hours_23(record):
    """Evaluate mean time to repair for control WP-0666-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-23", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 60,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-23", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-23", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 60
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-23", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 60, "comparison": "min",
        "finding": "mean time to repair falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_risk_score_24(record):
    """Evaluate supplier risk for control WP-0666-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0666-24", "metric": "supplier_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0666-24", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0666-24", "metric": "supplier_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0666-24", "metric": "supplier_risk_score", "label": "supplier risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_supplier_fill_rate_pct_01, assess_supplier_edi_success_pct_02, assess_supplier_forecast_sharing_pct_03, assess_supplier_audit_log_retention_days_04, assess_supplier_requalification_age_days_05, assess_supplier_fire_risk_score_06, assess_supplier_capacity_transfer_days_07, assess_supplier_observation_count_08, assess_supplier_bribery_training_pct_09, assess_supplier_recovery_drill_age_days_10, assess_supplier_technology_maturity_score_11, assess_supplier_ranking_ndcg_12, assess_supplier_chaos_test_age_days_13, assess_supplier_data_processing_agreement_pct_14, assess_supplier_risk_register_age_days_15, assess_supplier_receipt_before_invoice_pct_16, assess_supplier_machine_uptime_pct_17, assess_supplier_metric_definition_gap_count_18, assess_supplier_archive_completion_pct_19, assess_humidity_pct_20, assess_fire_exit_clearance_cm_21, assess_slotting_score_22, assess_mean_time_to_repair_hours_23, assess_supplier_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

