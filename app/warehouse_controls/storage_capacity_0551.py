"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_sorting_completion_pct_01(record):
    """Evaluate supplier sorting completion for control WP-0551-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_sorting_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-01", "metric": "supplier_sorting_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-01", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-01", "metric": "supplier_sorting_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-01", "metric": "supplier_sorting_completion_pct", "label": "supplier sorting completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier sorting completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_worker_safety_training_pct_02(record):
    """Evaluate supplier worker safety training for control WP-0551-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_worker_safety_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-02", "metric": "supplier_worker_safety_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-02", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-02", "metric": "supplier_worker_safety_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-02", "metric": "supplier_worker_safety_training_pct", "label": "supplier worker safety training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier worker safety training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_customer_loss_pct_03(record):
    """Evaluate supplier customer loss for control WP-0551-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_loss_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-03", "metric": "supplier_customer_loss_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 173,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-03", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-03", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 173
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-03", "metric": "supplier_customer_loss_pct", "label": "supplier customer loss",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 173, "comparison": "max",
        "finding": "supplier customer loss exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_continuous_improvement_count_04(record):
    """Evaluate supplier continuous improvement actions for control WP-0551-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuous_improvement_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-04", "metric": "supplier_continuous_improvement_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-04", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-04", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-04", "metric": "supplier_continuous_improvement_count", "label": "supplier continuous improvement actions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "supplier continuous improvement actions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_energy_per_inference_05(record):
    """Evaluate supplier energy per inference for control WP-0551-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-05", "metric": "supplier_energy_per_inference",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-05", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-05", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-05", "metric": "supplier_energy_per_inference", "label": "supplier energy per inference",
        "status": "breach", "severity": "critical", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier energy per inference must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_slo_burn_rate_06(record):
    """Evaluate supplier SLO burn rate for control WP-0551-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_slo_burn_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-06", "metric": "supplier_slo_burn_rate",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-06", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-06", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-06", "metric": "supplier_slo_burn_rate", "label": "supplier SLO burn rate",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SLO burn rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_build_provenance_pct_07(record):
    """Evaluate supplier build provenance completeness for control WP-0551-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_build_provenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-07", "metric": "supplier_build_provenance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 193,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-07", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-07", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 193
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-07", "metric": "supplier_build_provenance_pct", "label": "supplier build provenance completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 193, "comparison": "max",
        "finding": "supplier build provenance completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_control_test_age_days_08(record):
    """Evaluate supplier control test age for control WP-0551-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-08", "metric": "supplier_control_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-08", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-08", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-08", "metric": "supplier_control_test_age_days", "label": "supplier control test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "supplier control test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_vendor_master_change_count_09(record):
    """Evaluate supplier vendor-master changes for control WP-0551-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_master_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-09", "metric": "supplier_vendor_master_change_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-09", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-09", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-09", "metric": "supplier_vendor_master_change_count", "label": "supplier vendor-master changes",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier vendor-master changes must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_component_shortage_count_10(record):
    """Evaluate supplier component shortages for control WP-0551-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_component_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-10", "metric": "supplier_component_shortage_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-10", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-10", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-10", "metric": "supplier_component_shortage_count", "label": "supplier component shortages",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier component shortages must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_collaboration_score_11(record):
    """Evaluate supplier collaboration score for control WP-0551-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_collaboration_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-11", "metric": "supplier_collaboration_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-11", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-11", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-11", "metric": "supplier_collaboration_score", "label": "supplier collaboration score",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 33, "comparison": "max",
        "finding": "supplier collaboration score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_knowledge_handover_pct_12(record):
    """Evaluate supplier knowledge handover for control WP-0551-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-12", "metric": "supplier_knowledge_handover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-12", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-12", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-12", "metric": "supplier_knowledge_handover_pct", "label": "supplier knowledge handover",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "supplier knowledge handover falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_damage_rate_pct_13(record):
    """Evaluate damage rate for control WP-0551-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-13", "metric": "damage_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-13", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-13", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-13", "metric": "damage_rate_pct", "label": "damage rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "damage rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_api_error_rate_pct_14(record):
    """Evaluate API error rate for control WP-0551-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_error_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-14", "metric": "api_error_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-14", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-14", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-14", "metric": "api_error_rate_pct", "label": "API error rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "API error rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_service_recovery_hours_15(record):
    """Evaluate service recovery time for control WP-0551-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_recovery_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-15", "metric": "service_recovery_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-15", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-15", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-15", "metric": "service_recovery_hours", "label": "service recovery time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "service recovery time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_inspection_pass_pct_16(record):
    """Evaluate inspection pass rate for control WP-0551-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_pass_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-16", "metric": "inspection_pass_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-16", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-16", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-16", "metric": "inspection_pass_pct", "label": "inspection pass rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "inspection pass rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_customs_document_score_17(record):
    """Evaluate customs documentation for control WP-0551-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_document_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-17", "metric": "customs_document_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-17", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-17", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-17", "metric": "customs_document_score", "label": "customs documentation",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customs documentation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_security_patch_compliance_pct_18(record):
    """Evaluate security patch compliance for control WP-0551-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_patch_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-18", "metric": "security_patch_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-18", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-18", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-18", "metric": "security_patch_compliance_pct", "label": "security patch compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "security patch compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_order_confirmation_minutes_19(record):
    """Evaluate order confirmation time for control WP-0551-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_confirmation_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-19", "metric": "order_confirmation_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-19", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-19", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-19", "metric": "order_confirmation_minutes", "label": "order confirmation time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "order confirmation time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_air_quality_index_20(record):
    """Evaluate air quality index for control WP-0551-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("air_quality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-20", "metric": "air_quality_index",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-20", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-20", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-20", "metric": "air_quality_index", "label": "air quality index",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "air quality index falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_refund_completion_pct_21(record):
    """Evaluate refund completion for control WP-0551-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-21", "metric": "refund_completion_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-21", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-21", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-21", "metric": "refund_completion_pct", "label": "refund completion",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refund completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_coa_document_pct_22(record):
    """Evaluate certificate of analysis completeness for control WP-0551-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coa_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-22", "metric": "coa_document_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-22", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-22", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-22", "metric": "coa_document_pct", "label": "certificate of analysis completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "certificate of analysis completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_battery_swelling_signal_23(record):
    """Evaluate battery swelling signal for control WP-0551-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_swelling_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-23", "metric": "battery_swelling_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-23", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-23", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-23", "metric": "battery_swelling_signal", "label": "battery swelling signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "battery swelling signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_corrective_action_age_days_24(record):
    """Evaluate corrective action age for control WP-0551-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0551-24", "metric": "corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0551-24", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0551-24", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0551-24", "metric": "corrective_action_age_days", "label": "corrective action age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "corrective action age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_supplier_sorting_completion_pct_01, assess_supplier_worker_safety_training_pct_02, assess_supplier_customer_loss_pct_03, assess_supplier_continuous_improvement_count_04, assess_supplier_energy_per_inference_05, assess_supplier_slo_burn_rate_06, assess_supplier_build_provenance_pct_07, assess_supplier_control_test_age_days_08, assess_supplier_vendor_master_change_count_09, assess_supplier_component_shortage_count_10, assess_supplier_collaboration_score_11, assess_supplier_knowledge_handover_pct_12, assess_damage_rate_pct_13, assess_api_error_rate_pct_14, assess_service_recovery_hours_15, assess_inspection_pass_pct_16, assess_customs_document_score_17, assess_security_patch_compliance_pct_18, assess_order_confirmation_minutes_19, assess_air_quality_index_20, assess_refund_completion_pct_21, assess_coa_document_pct_22, assess_battery_swelling_signal_23, assess_corrective_action_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

