"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_esg_score_01(record):
    """Evaluate supplier ESG score for control WP-0539-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_esg_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-01", "metric": "supplier_esg_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-01", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-01", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-01", "metric": "supplier_esg_score", "label": "supplier ESG score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ESG score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_training_pct_02(record):
    """Evaluate supplier training completion for control WP-0539-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-02", "metric": "supplier_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-02", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-02", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-02", "metric": "supplier_training_pct", "label": "supplier training completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier training completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_risk_review_age_days_03(record):
    """Evaluate supplier risk review age for control WP-0539-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-03", "metric": "supplier_risk_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-03", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-03", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-03", "metric": "supplier_risk_review_age_days", "label": "supplier risk review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "supplier risk review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_security_assessment_age_days_04(record):
    """Evaluate supplier security assessment age for control WP-0539-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-04", "metric": "supplier_security_assessment_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-04", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-04", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-04", "metric": "supplier_security_assessment_age_days", "label": "supplier security assessment age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier security assessment age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_tooling_spare_days_05(record):
    """Evaluate supplier tooling spare lead time for control WP-0539-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-05", "metric": "supplier_tooling_spare_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-05", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-05", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-05", "metric": "supplier_tooling_spare_days", "label": "supplier tooling spare lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier tooling spare lead time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_scope3_data_pct_06(record):
    """Evaluate supplier Scope 3 data completeness for control WP-0539-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scope3_data_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-06", "metric": "supplier_scope3_data_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-06", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-06", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-06", "metric": "supplier_scope3_data_pct", "label": "supplier Scope 3 data completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier Scope 3 data completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_ack_latency_minutes_07(record):
    """Evaluate supplier acknowledgement latency for control WP-0539-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ack_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-07", "metric": "supplier_ack_latency_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-07", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-07", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-07", "metric": "supplier_ack_latency_minutes", "label": "supplier acknowledgement latency",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "supplier acknowledgement latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_sorting_completion_pct_08(record):
    """Evaluate supplier sorting completion for control WP-0539-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sorting_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-08", "metric": "supplier_sorting_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-08", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-08", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-08", "metric": "supplier_sorting_completion_pct", "label": "supplier sorting completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier sorting completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_worker_safety_training_pct_09(record):
    """Evaluate supplier worker safety training for control WP-0539-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_safety_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-09", "metric": "supplier_worker_safety_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-09", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-09", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-09", "metric": "supplier_worker_safety_training_pct", "label": "supplier worker safety training",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier worker safety training must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_customer_loss_pct_10(record):
    """Evaluate supplier customer loss for control WP-0539-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_loss_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-10", "metric": "supplier_customer_loss_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-10", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-10", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-10", "metric": "supplier_customer_loss_pct", "label": "supplier customer loss",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier customer loss must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_continuous_improvement_count_11(record):
    """Evaluate supplier continuous improvement actions for control WP-0539-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuous_improvement_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-11", "metric": "supplier_continuous_improvement_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-11", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-11", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-11", "metric": "supplier_continuous_improvement_count", "label": "supplier continuous improvement actions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier continuous improvement actions exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_energy_per_inference_12(record):
    """Evaluate supplier energy per inference for control WP-0539-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-12", "metric": "supplier_energy_per_inference",
            "status": "insufficient_data",
            "severity": "high", "unit": "kWh",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-12", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-12", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-12", "metric": "supplier_energy_per_inference", "label": "supplier energy per inference",
        "status": "breach", "severity": "high", "unit": "kWh",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier energy per inference falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_slo_burn_rate_13(record):
    """Evaluate supplier SLO burn rate for control WP-0539-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_slo_burn_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-13", "metric": "supplier_slo_burn_rate",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-13", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-13", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-13", "metric": "supplier_slo_burn_rate", "label": "supplier SLO burn rate",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier SLO burn rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_build_provenance_pct_14(record):
    """Evaluate supplier build provenance completeness for control WP-0539-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_build_provenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-14", "metric": "supplier_build_provenance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-14", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-14", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-14", "metric": "supplier_build_provenance_pct", "label": "supplier build provenance completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier build provenance completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_control_test_age_days_15(record):
    """Evaluate supplier control test age for control WP-0539-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-15", "metric": "supplier_control_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-15", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-15", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-15", "metric": "supplier_control_test_age_days", "label": "supplier control test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier control test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_vendor_master_change_count_16(record):
    """Evaluate supplier vendor-master changes for control WP-0539-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_master_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-16", "metric": "supplier_vendor_master_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-16", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-16", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-16", "metric": "supplier_vendor_master_change_count", "label": "supplier vendor-master changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier vendor-master changes falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_component_shortage_count_17(record):
    """Evaluate supplier component shortages for control WP-0539-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_component_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-17", "metric": "supplier_component_shortage_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-17", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-17", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-17", "metric": "supplier_component_shortage_count", "label": "supplier component shortages",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier component shortages must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_collaboration_score_18(record):
    """Evaluate supplier collaboration score for control WP-0539-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_collaboration_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-18", "metric": "supplier_collaboration_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-18", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-18", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-18", "metric": "supplier_collaboration_score", "label": "supplier collaboration score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier collaboration score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_knowledge_handover_pct_19(record):
    """Evaluate supplier knowledge handover for control WP-0539-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-19", "metric": "supplier_knowledge_handover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-19", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-19", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-19", "metric": "supplier_knowledge_handover_pct", "label": "supplier knowledge handover",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier knowledge handover exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_damage_rate_pct_20(record):
    """Evaluate damage rate for control WP-0539-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-20", "metric": "damage_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-20", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-20", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-20", "metric": "damage_rate_pct", "label": "damage rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "damage rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_api_error_rate_pct_21(record):
    """Evaluate API error rate for control WP-0539-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_error_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-21", "metric": "api_error_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-21", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-21", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-21", "metric": "api_error_rate_pct", "label": "API error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "API error rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_service_recovery_hours_22(record):
    """Evaluate service recovery time for control WP-0539-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_recovery_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-22", "metric": "service_recovery_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-22", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-22", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-22", "metric": "service_recovery_hours", "label": "service recovery time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "service recovery time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_inspection_pass_pct_23(record):
    """Evaluate inspection pass rate for control WP-0539-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_pass_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-23", "metric": "inspection_pass_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-23", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-23", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-23", "metric": "inspection_pass_pct", "label": "inspection pass rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "inspection pass rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_customs_document_score_24(record):
    """Evaluate customs documentation for control WP-0539-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_document_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0539-24", "metric": "customs_document_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0539-24", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0539-24", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0539-24", "metric": "customs_document_score", "label": "customs documentation",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "customs documentation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_esg_score_01, assess_supplier_training_pct_02, assess_supplier_risk_review_age_days_03, assess_supplier_security_assessment_age_days_04, assess_supplier_tooling_spare_days_05, assess_supplier_scope3_data_pct_06, assess_supplier_ack_latency_minutes_07, assess_supplier_sorting_completion_pct_08, assess_supplier_worker_safety_training_pct_09, assess_supplier_customer_loss_pct_10, assess_supplier_continuous_improvement_count_11, assess_supplier_energy_per_inference_12, assess_supplier_slo_burn_rate_13, assess_supplier_build_provenance_pct_14, assess_supplier_control_test_age_days_15, assess_supplier_vendor_master_change_count_16, assess_supplier_component_shortage_count_17, assess_supplier_collaboration_score_18, assess_supplier_knowledge_handover_pct_19, assess_damage_rate_pct_20, assess_api_error_rate_pct_21, assess_service_recovery_hours_22, assess_inspection_pass_pct_23, assess_customs_document_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

