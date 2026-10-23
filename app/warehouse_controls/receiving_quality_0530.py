"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_remote_wipe_test_age_days_01(record):
    """Evaluate remote wipe test age for control WP-0530-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("remote_wipe_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-01", "metric": "remote_wipe_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-01", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-01", "metric": "remote_wipe_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-01", "metric": "remote_wipe_test_age_days", "label": "remote wipe test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "remote wipe test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_shipment_duplicate_count_02(record):
    """Evaluate duplicate shipments for control WP-0530-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shipment_duplicate_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-02", "metric": "shipment_duplicate_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "shipments",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-02", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-02", "metric": "shipment_duplicate_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-02", "metric": "shipment_duplicate_count", "label": "duplicate shipments",
        "status": "breach", "severity": "critical", "unit": "shipments",
        "observed": observed,
        "threshold": 75, "comparison": "max",
        "finding": "duplicate shipments exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_replenishment_task_queue_03(record):
    """Evaluate replenishment task queue for control WP-0530-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_task_queue")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-03", "metric": "replenishment_task_queue",
            "status": "insufficient_data",
            "severity": "low", "unit": "tasks",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-03", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-03", "metric": "replenishment_task_queue", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-03", "metric": "replenishment_task_queue", "label": "replenishment task queue",
        "status": "breach", "severity": "low", "unit": "tasks",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "replenishment task queue falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_payment_capture_success_pct_04(record):
    """Evaluate payment capture success for control WP-0530-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("payment_capture_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-04", "metric": "payment_capture_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-04", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-04", "metric": "payment_capture_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-04", "metric": "payment_capture_success_pct", "label": "payment capture success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "payment capture success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_yard_spot_accuracy_pct_05(record):
    """Evaluate yard spot accuracy for control WP-0530-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_spot_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-05", "metric": "yard_spot_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-05", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-05", "metric": "yard_spot_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-05", "metric": "yard_spot_accuracy_pct", "label": "yard spot accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "yard spot accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_shrinkage_rate_pct_06(record):
    """Evaluate shrinkage rate for control WP-0530-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("shrinkage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-06", "metric": "shrinkage_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-06", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-06", "metric": "shrinkage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-06", "metric": "shrinkage_rate_pct", "label": "shrinkage rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "max",
        "finding": "shrinkage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_fill_rate_pct_07(record):
    """Evaluate supplier fill rate for control WP-0530-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fill_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-07", "metric": "supplier_fill_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-07", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-07", "metric": "supplier_fill_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-07", "metric": "supplier_fill_rate_pct", "label": "supplier fill rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier fill rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_edi_success_pct_08(record):
    """Evaluate supplier EDI success for control WP-0530-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_edi_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-08", "metric": "supplier_edi_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-08", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-08", "metric": "supplier_edi_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-08", "metric": "supplier_edi_success_pct", "label": "supplier EDI success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier EDI success must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_forecast_sharing_pct_09(record):
    """Evaluate supplier forecast sharing for control WP-0530-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_forecast_sharing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-09", "metric": "supplier_forecast_sharing_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-09", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-09", "metric": "supplier_forecast_sharing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-09", "metric": "supplier_forecast_sharing_pct", "label": "supplier forecast sharing",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier forecast sharing must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_audit_log_retention_days_10(record):
    """Evaluate supplier audit-log retention for control WP-0530-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_audit_log_retention_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-10", "metric": "supplier_audit_log_retention_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 115,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-10", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-10", "metric": "supplier_audit_log_retention_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 115
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-10", "metric": "supplier_audit_log_retention_days", "label": "supplier audit-log retention",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 115, "comparison": "max",
        "finding": "supplier audit-log retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_requalification_age_days_11(record):
    """Evaluate supplier requalification age for control WP-0530-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_requalification_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-11", "metric": "supplier_requalification_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-11", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-11", "metric": "supplier_requalification_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-11", "metric": "supplier_requalification_age_days", "label": "supplier requalification age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "supplier requalification age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_fire_risk_score_12(record):
    """Evaluate supplier site fire risk for control WP-0530-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_fire_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-12", "metric": "supplier_fire_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-12", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-12", "metric": "supplier_fire_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-12", "metric": "supplier_fire_risk_score", "label": "supplier site fire risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier site fire risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_capacity_transfer_days_13(record):
    """Evaluate supplier capacity transfer time for control WP-0530-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_transfer_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-13", "metric": "supplier_capacity_transfer_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-13", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-13", "metric": "supplier_capacity_transfer_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-13", "metric": "supplier_capacity_transfer_days", "label": "supplier capacity transfer time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier capacity transfer time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_observation_count_14(record):
    """Evaluate supplier observations for control WP-0530-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_observation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-14", "metric": "supplier_observation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 135,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-14", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-14", "metric": "supplier_observation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 135
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-14", "metric": "supplier_observation_count", "label": "supplier observations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 135, "comparison": "max",
        "finding": "supplier observations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_bribery_training_pct_15(record):
    """Evaluate supplier anti-bribery training for control WP-0530-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bribery_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-15", "metric": "supplier_bribery_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-15", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-15", "metric": "supplier_bribery_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-15", "metric": "supplier_bribery_training_pct", "label": "supplier anti-bribery training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "supplier anti-bribery training falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_recovery_drill_age_days_16(record):
    """Evaluate supplier recovery drill age for control WP-0530-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recovery_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-16", "metric": "supplier_recovery_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-16", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-16", "metric": "supplier_recovery_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-16", "metric": "supplier_recovery_drill_age_days", "label": "supplier recovery drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier recovery drill age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_technology_maturity_score_17(record):
    """Evaluate supplier technology maturity for control WP-0530-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_technology_maturity_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-17", "metric": "supplier_technology_maturity_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-17", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-17", "metric": "supplier_technology_maturity_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-17", "metric": "supplier_technology_maturity_score", "label": "supplier technology maturity",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier technology maturity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_ranking_ndcg_18(record):
    """Evaluate supplier ranking NDCG for control WP-0530-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ranking_ndcg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-18", "metric": "supplier_ranking_ndcg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "score",
            "observed": None,
            "threshold": 155,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-18", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-18", "metric": "supplier_ranking_ndcg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 155
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-18", "metric": "supplier_ranking_ndcg", "label": "supplier ranking NDCG",
        "status": "breach", "severity": "critical", "unit": "score",
        "observed": observed,
        "threshold": 155, "comparison": "max",
        "finding": "supplier ranking NDCG exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_chaos_test_age_days_19(record):
    """Evaluate supplier chaos-test age for control WP-0530-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_chaos_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-19", "metric": "supplier_chaos_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-19", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-19", "metric": "supplier_chaos_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-19", "metric": "supplier_chaos_test_age_days", "label": "supplier chaos-test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier chaos-test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_data_processing_agreement_pct_20(record):
    """Evaluate supplier DPA completeness for control WP-0530-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_processing_agreement_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-20", "metric": "supplier_data_processing_agreement_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-20", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-20", "metric": "supplier_data_processing_agreement_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-20", "metric": "supplier_data_processing_agreement_pct", "label": "supplier DPA completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier DPA completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_risk_register_age_days_21(record):
    """Evaluate supplier risk register age for control WP-0530-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_register_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-21", "metric": "supplier_risk_register_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-21", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-21", "metric": "supplier_risk_register_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-21", "metric": "supplier_risk_register_age_days", "label": "supplier risk register age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk register age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_receipt_before_invoice_pct_22(record):
    """Evaluate receipt-before-invoice compliance for control WP-0530-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_receipt_before_invoice_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-22", "metric": "supplier_receipt_before_invoice_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 175,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-22", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-22", "metric": "supplier_receipt_before_invoice_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 175
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-22", "metric": "supplier_receipt_before_invoice_pct", "label": "receipt-before-invoice compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 175, "comparison": "max",
        "finding": "receipt-before-invoice compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_machine_uptime_pct_23(record):
    """Evaluate supplier machine uptime for control WP-0530-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_machine_uptime_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-23", "metric": "supplier_machine_uptime_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-23", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-23", "metric": "supplier_machine_uptime_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-23", "metric": "supplier_machine_uptime_pct", "label": "supplier machine uptime",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier machine uptime falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_metric_definition_gap_count_24(record):
    """Evaluate supplier metric-definition gaps for control WP-0530-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_metric_definition_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0530-24", "metric": "supplier_metric_definition_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0530-24", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0530-24", "metric": "supplier_metric_definition_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0530-24", "metric": "supplier_metric_definition_gap_count", "label": "supplier metric-definition gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier metric-definition gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_remote_wipe_test_age_days_01, assess_shipment_duplicate_count_02, assess_replenishment_task_queue_03, assess_payment_capture_success_pct_04, assess_yard_spot_accuracy_pct_05, assess_shrinkage_rate_pct_06, assess_supplier_fill_rate_pct_07, assess_supplier_edi_success_pct_08, assess_supplier_forecast_sharing_pct_09, assess_supplier_audit_log_retention_days_10, assess_supplier_requalification_age_days_11, assess_supplier_fire_risk_score_12, assess_supplier_capacity_transfer_days_13, assess_supplier_observation_count_14, assess_supplier_bribery_training_pct_15, assess_supplier_recovery_drill_age_days_16, assess_supplier_technology_maturity_score_17, assess_supplier_ranking_ndcg_18, assess_supplier_chaos_test_age_days_19, assess_supplier_data_processing_agreement_pct_20, assess_supplier_risk_register_age_days_21, assess_supplier_receipt_before_invoice_pct_22, assess_supplier_machine_uptime_pct_23, assess_supplier_metric_definition_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

