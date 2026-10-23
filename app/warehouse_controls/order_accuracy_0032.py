"""Operational control pack for order accuracy; rules are executable against warehouse records."""
from math import isfinite

def assess_shrinkage_rate_pct_01(record):
    """Evaluate shrinkage rate for control WP-0032-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shrinkage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-01", "metric": "shrinkage_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-01", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-01", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-01", "metric": "shrinkage_rate_pct", "label": "shrinkage rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "shrinkage rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_fill_rate_pct_02(record):
    """Evaluate supplier fill rate for control WP-0032-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-02", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-02", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-02", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-02", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier fill rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_edi_success_pct_03(record):
    """Evaluate supplier EDI success for control WP-0032-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-03", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-03", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-03", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-03", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier EDI success must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_forecast_sharing_pct_04(record):
    """Evaluate supplier forecast sharing for control WP-0032-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_sharing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-04", "metric": "supplier_forecast_sharing_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-04", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-04", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-04", "metric": "supplier_forecast_sharing_pct", "label": "supplier forecast sharing",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier forecast sharing exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_audit_log_retention_days_05(record):
    """Evaluate supplier audit-log retention for control WP-0032-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-05", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-05", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-05", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-05", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "supplier audit-log retention falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_requalification_age_days_06(record):
    """Evaluate supplier requalification age for control WP-0032-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_requalification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-06", "metric": "supplier_requalification_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-06", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-06", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-06", "metric": "supplier_requalification_age_days", "label": "supplier requalification age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier requalification age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_fire_risk_score_07(record):
    """Evaluate supplier site fire risk for control WP-0032-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-07", "metric": "supplier_fire_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-07", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-07", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-07", "metric": "supplier_fire_risk_score", "label": "supplier site fire risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier site fire risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_capacity_transfer_days_08(record):
    """Evaluate supplier capacity transfer time for control WP-0032-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-08", "metric": "supplier_capacity_transfer_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-08", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-08", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-08", "metric": "supplier_capacity_transfer_days", "label": "supplier capacity transfer time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier capacity transfer time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_observation_count_09(record):
    """Evaluate supplier observations for control WP-0032-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-09", "metric": "supplier_observation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-09", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-09", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-09", "metric": "supplier_observation_count", "label": "supplier observations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier observations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_bribery_training_pct_10(record):
    """Evaluate supplier anti-bribery training for control WP-0032-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bribery_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-10", "metric": "supplier_bribery_training_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-10", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-10", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-10", "metric": "supplier_bribery_training_pct", "label": "supplier anti-bribery training",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier anti-bribery training must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_recovery_drill_age_days_11(record):
    """Evaluate supplier recovery drill age for control WP-0032-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-11", "metric": "supplier_recovery_drill_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-11", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-11", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-11", "metric": "supplier_recovery_drill_age_days", "label": "supplier recovery drill age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recovery drill age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_technology_maturity_score_12(record):
    """Evaluate supplier technology maturity for control WP-0032-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_technology_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-12", "metric": "supplier_technology_maturity_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-12", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-12", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-12", "metric": "supplier_technology_maturity_score", "label": "supplier technology maturity",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier technology maturity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_ranking_ndcg_13(record):
    """Evaluate supplier ranking NDCG for control WP-0032-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ranking_ndcg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-13", "metric": "supplier_ranking_ndcg",
            "status": "insufficient_data",
            "severity": "low", "unit": "score",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-13", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-13", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-13", "metric": "supplier_ranking_ndcg", "label": "supplier ranking NDCG",
        "status": "breach", "severity": "low", "unit": "score",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier ranking NDCG falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_chaos_test_age_days_14(record):
    """Evaluate supplier chaos-test age for control WP-0032-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_chaos_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-14", "metric": "supplier_chaos_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-14", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-14", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-14", "metric": "supplier_chaos_test_age_days", "label": "supplier chaos-test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier chaos-test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_data_processing_agreement_pct_15(record):
    """Evaluate supplier DPA completeness for control WP-0032-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_processing_agreement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-15", "metric": "supplier_data_processing_agreement_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-15", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-15", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-15", "metric": "supplier_data_processing_agreement_pct", "label": "supplier DPA completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier DPA completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_risk_register_age_days_16(record):
    """Evaluate supplier risk register age for control WP-0032-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_register_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-16", "metric": "supplier_risk_register_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-16", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-16", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-16", "metric": "supplier_risk_register_age_days", "label": "supplier risk register age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "supplier risk register age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_supplier_receipt_before_invoice_pct_17(record):
    """Evaluate receipt-before-invoice compliance for control WP-0032-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_receipt_before_invoice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-17", "metric": "supplier_receipt_before_invoice_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-17", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-17", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-17", "metric": "supplier_receipt_before_invoice_pct", "label": "receipt-before-invoice compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "receipt-before-invoice compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_supplier_machine_uptime_pct_18(record):
    """Evaluate supplier machine uptime for control WP-0032-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_machine_uptime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-18", "metric": "supplier_machine_uptime_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-18", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-18", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-18", "metric": "supplier_machine_uptime_pct", "label": "supplier machine uptime",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier machine uptime must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_supplier_metric_definition_gap_count_19(record):
    """Evaluate supplier metric-definition gaps for control WP-0032-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_metric_definition_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-19", "metric": "supplier_metric_definition_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-19", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-19", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-19", "metric": "supplier_metric_definition_gap_count", "label": "supplier metric-definition gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier metric-definition gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_supplier_archive_completion_pct_20(record):
    """Evaluate supplier archive completion for control WP-0032-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_archive_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-20", "metric": "supplier_archive_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-20", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-20", "metric": "supplier_archive_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-20", "metric": "supplier_archive_completion_pct", "label": "supplier archive completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier archive completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

def assess_humidity_pct_21(record):
    """Evaluate storage humidity for control WP-0032-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("humidity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-21", "metric": "humidity_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-21", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-21", "metric": "humidity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-21", "metric": "humidity_pct", "label": "storage humidity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "storage humidity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "order accuracy",
    }

def assess_fire_exit_clearance_cm_22(record):
    """Evaluate fire exit clearance for control WP-0032-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fire_exit_clearance_cm")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-22", "metric": "fire_exit_clearance_cm",
            "status": "insufficient_data",
            "severity": "medium", "unit": "cm",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-22", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-22", "metric": "fire_exit_clearance_cm", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-22", "metric": "fire_exit_clearance_cm", "label": "fire exit clearance",
        "status": "breach", "severity": "medium", "unit": "cm",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "fire exit clearance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "order accuracy",
    }

def assess_slotting_score_23(record):
    """Evaluate slotting score for control WP-0032-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-23", "metric": "slotting_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-23", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-23", "metric": "slotting_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-23", "metric": "slotting_score", "label": "slotting score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slotting score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "order accuracy",
    }

def assess_mean_time_to_repair_hours_24(record):
    """Evaluate mean time to repair for control WP-0032-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("mean_time_to_repair_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0032-24", "metric": "mean_time_to_repair_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0032-24", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0032-24", "metric": "mean_time_to_repair_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0032-24", "metric": "mean_time_to_repair_hours", "label": "mean time to repair",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "mean time to repair exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "order accuracy",
    }

RULES = (assess_shrinkage_rate_pct_01, assess_supplier_fill_rate_pct_02, assess_supplier_edi_success_pct_03, assess_supplier_forecast_sharing_pct_04, assess_supplier_audit_log_retention_days_05, assess_supplier_requalification_age_days_06, assess_supplier_fire_risk_score_07, assess_supplier_capacity_transfer_days_08, assess_supplier_observation_count_09, assess_supplier_bribery_training_pct_10, assess_supplier_recovery_drill_age_days_11, assess_supplier_technology_maturity_score_12, assess_supplier_ranking_ndcg_13, assess_supplier_chaos_test_age_days_14, assess_supplier_data_processing_agreement_pct_15, assess_supplier_risk_register_age_days_16, assess_supplier_receipt_before_invoice_pct_17, assess_supplier_machine_uptime_pct_18, assess_supplier_metric_definition_gap_count_19, assess_supplier_archive_completion_pct_20, assess_humidity_pct_21, assess_fire_exit_clearance_cm_22, assess_slotting_score_23, assess_mean_time_to_repair_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

