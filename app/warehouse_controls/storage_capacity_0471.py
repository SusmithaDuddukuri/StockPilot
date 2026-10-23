"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_complaint_resolution_pct_01(record):
    """Evaluate complaint resolution for control WP-0471-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("complaint_resolution_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-01", "metric": "complaint_resolution_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-01", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-01", "metric": "complaint_resolution_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-01", "metric": "complaint_resolution_pct", "label": "complaint resolution",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "complaint resolution must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_container_return_age_days_02(record):
    """Evaluate container return age for control WP-0471-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("container_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-02", "metric": "container_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-02", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-02", "metric": "container_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-02", "metric": "container_return_age_days", "label": "container return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "container return age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_vehicle_maintenance_cost_03(record):
    """Evaluate vehicle maintenance cost for control WP-0471-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_maintenance_cost")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-03", "metric": "vehicle_maintenance_cost",
            "status": "insufficient_data",
            "severity": "medium", "unit": "currency",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-03", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-03", "metric": "vehicle_maintenance_cost", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-03", "metric": "vehicle_maintenance_cost", "label": "vehicle maintenance cost",
        "status": "breach", "severity": "medium", "unit": "currency",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "vehicle maintenance cost exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_esg_score_04(record):
    """Evaluate supplier ESG score for control WP-0471-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_esg_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-04", "metric": "supplier_esg_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-04", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-04", "metric": "supplier_esg_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-04", "metric": "supplier_esg_score", "label": "supplier ESG score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "supplier ESG score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_training_pct_05(record):
    """Evaluate supplier training completion for control WP-0471-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-05", "metric": "supplier_training_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-05", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-05", "metric": "supplier_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-05", "metric": "supplier_training_pct", "label": "supplier training completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_risk_review_age_days_06(record):
    """Evaluate supplier risk review age for control WP-0471-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-06", "metric": "supplier_risk_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-06", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-06", "metric": "supplier_risk_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-06", "metric": "supplier_risk_review_age_days", "label": "supplier risk review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier risk review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_security_assessment_age_days_07(record):
    """Evaluate supplier security assessment age for control WP-0471-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_security_assessment_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-07", "metric": "supplier_security_assessment_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-07", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-07", "metric": "supplier_security_assessment_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-07", "metric": "supplier_security_assessment_age_days", "label": "supplier security assessment age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "supplier security assessment age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_tooling_spare_days_08(record):
    """Evaluate supplier tooling spare lead time for control WP-0471-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-08", "metric": "supplier_tooling_spare_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-08", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-08", "metric": "supplier_tooling_spare_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-08", "metric": "supplier_tooling_spare_days", "label": "supplier tooling spare lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "supplier tooling spare lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_scope3_data_pct_09(record):
    """Evaluate supplier Scope 3 data completeness for control WP-0471-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scope3_data_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-09", "metric": "supplier_scope3_data_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-09", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-09", "metric": "supplier_scope3_data_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-09", "metric": "supplier_scope3_data_pct", "label": "supplier Scope 3 data completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier Scope 3 data completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_ack_latency_minutes_10(record):
    """Evaluate supplier acknowledgement latency for control WP-0471-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ack_latency_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-10", "metric": "supplier_ack_latency_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-10", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-10", "metric": "supplier_ack_latency_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-10", "metric": "supplier_ack_latency_minutes", "label": "supplier acknowledgement latency",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier acknowledgement latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_sorting_completion_pct_11(record):
    """Evaluate supplier sorting completion for control WP-0471-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sorting_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-11", "metric": "supplier_sorting_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-11", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-11", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-11", "metric": "supplier_sorting_completion_pct", "label": "supplier sorting completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "supplier sorting completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_worker_safety_training_pct_12(record):
    """Evaluate supplier worker safety training for control WP-0471-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_safety_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-12", "metric": "supplier_worker_safety_training_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-12", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-12", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-12", "metric": "supplier_worker_safety_training_pct", "label": "supplier worker safety training",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "supplier worker safety training falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_customer_loss_pct_13(record):
    """Evaluate supplier customer loss for control WP-0471-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_loss_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-13", "metric": "supplier_customer_loss_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-13", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-13", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-13", "metric": "supplier_customer_loss_pct", "label": "supplier customer loss",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier customer loss must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_continuous_improvement_count_14(record):
    """Evaluate supplier continuous improvement actions for control WP-0471-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuous_improvement_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-14", "metric": "supplier_continuous_improvement_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-14", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-14", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-14", "metric": "supplier_continuous_improvement_count", "label": "supplier continuous improvement actions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier continuous improvement actions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_energy_per_inference_15(record):
    """Evaluate supplier energy per inference for control WP-0471-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-15", "metric": "supplier_energy_per_inference",
            "status": "insufficient_data",
            "severity": "medium", "unit": "kWh",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-15", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-15", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-15", "metric": "supplier_energy_per_inference", "label": "supplier energy per inference",
        "status": "breach", "severity": "medium", "unit": "kWh",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "supplier energy per inference exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_slo_burn_rate_16(record):
    """Evaluate supplier SLO burn rate for control WP-0471-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_slo_burn_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-16", "metric": "supplier_slo_burn_rate",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 43,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-16", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-16", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 43
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-16", "metric": "supplier_slo_burn_rate", "label": "supplier SLO burn rate",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 43, "comparison": "min",
        "finding": "supplier SLO burn rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_build_provenance_pct_17(record):
    """Evaluate supplier build provenance completeness for control WP-0471-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_build_provenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-17", "metric": "supplier_build_provenance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-17", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-17", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-17", "metric": "supplier_build_provenance_pct", "label": "supplier build provenance completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier build provenance completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_control_test_age_days_18(record):
    """Evaluate supplier control test age for control WP-0471-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-18", "metric": "supplier_control_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-18", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-18", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-18", "metric": "supplier_control_test_age_days", "label": "supplier control test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_vendor_master_change_count_19(record):
    """Evaluate supplier vendor-master changes for control WP-0471-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_master_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-19", "metric": "supplier_vendor_master_change_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-19", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-19", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-19", "metric": "supplier_vendor_master_change_count", "label": "supplier vendor-master changes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "supplier vendor-master changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_component_shortage_count_20(record):
    """Evaluate supplier component shortages for control WP-0471-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_component_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-20", "metric": "supplier_component_shortage_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-20", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-20", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-20", "metric": "supplier_component_shortage_count", "label": "supplier component shortages",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 87, "comparison": "min",
        "finding": "supplier component shortages falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_collaboration_score_21(record):
    """Evaluate supplier collaboration score for control WP-0471-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_collaboration_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-21", "metric": "supplier_collaboration_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-21", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-21", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-21", "metric": "supplier_collaboration_score", "label": "supplier collaboration score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier collaboration score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_knowledge_handover_pct_22(record):
    """Evaluate supplier knowledge handover for control WP-0471-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-22", "metric": "supplier_knowledge_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-22", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-22", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-22", "metric": "supplier_knowledge_handover_pct", "label": "supplier knowledge handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier knowledge handover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_damage_rate_pct_23(record):
    """Evaluate damage rate for control WP-0471-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-23", "metric": "damage_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-23", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-23", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-23", "metric": "damage_rate_pct", "label": "damage rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "damage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_api_error_rate_pct_24(record):
    """Evaluate API error rate for control WP-0471-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_error_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0471-24", "metric": "api_error_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 36,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0471-24", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0471-24", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 36
    if not failed:
        return None
    return {
        "rule_id": "WP-0471-24", "metric": "api_error_rate_pct", "label": "API error rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 36, "comparison": "min",
        "finding": "API error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_complaint_resolution_pct_01, assess_container_return_age_days_02, assess_vehicle_maintenance_cost_03, assess_supplier_esg_score_04, assess_supplier_training_pct_05, assess_supplier_risk_review_age_days_06, assess_supplier_security_assessment_age_days_07, assess_supplier_tooling_spare_days_08, assess_supplier_scope3_data_pct_09, assess_supplier_ack_latency_minutes_10, assess_supplier_sorting_completion_pct_11, assess_supplier_worker_safety_training_pct_12, assess_supplier_customer_loss_pct_13, assess_supplier_continuous_improvement_count_14, assess_supplier_energy_per_inference_15, assess_supplier_slo_burn_rate_16, assess_supplier_build_provenance_pct_17, assess_supplier_control_test_age_days_18, assess_supplier_vendor_master_change_count_19, assess_supplier_component_shortage_count_20, assess_supplier_collaboration_score_21, assess_supplier_knowledge_handover_pct_22, assess_damage_rate_pct_23, assess_api_error_rate_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

