"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_customer_loss_pct_01(record):
    """Evaluate supplier customer loss for control WP-0364-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_customer_loss_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-01", "metric": "supplier_customer_loss_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-01", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-01", "metric": "supplier_customer_loss_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-01", "metric": "supplier_customer_loss_pct", "label": "supplier customer loss",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "supplier customer loss falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_continuous_improvement_count_02(record):
    """Evaluate supplier continuous improvement actions for control WP-0364-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_continuous_improvement_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-02", "metric": "supplier_continuous_improvement_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-02", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-02", "metric": "supplier_continuous_improvement_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-02", "metric": "supplier_continuous_improvement_count", "label": "supplier continuous improvement actions",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier continuous improvement actions must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_energy_per_inference_03(record):
    """Evaluate supplier energy per inference for control WP-0364-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_energy_per_inference")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-03", "metric": "supplier_energy_per_inference",
            "status": "insufficient_data",
            "severity": "high", "unit": "kWh",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-03", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-03", "metric": "supplier_energy_per_inference", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-03", "metric": "supplier_energy_per_inference", "label": "supplier energy per inference",
        "status": "breach", "severity": "high", "unit": "kWh",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier energy per inference must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_slo_burn_rate_04(record):
    """Evaluate supplier SLO burn rate for control WP-0364-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_slo_burn_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-04", "metric": "supplier_slo_burn_rate",
            "status": "insufficient_data",
            "severity": "critical", "unit": "index",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-04", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-04", "metric": "supplier_slo_burn_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-04", "metric": "supplier_slo_burn_rate", "label": "supplier SLO burn rate",
        "status": "breach", "severity": "critical", "unit": "index",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier SLO burn rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_build_provenance_pct_05(record):
    """Evaluate supplier build provenance completeness for control WP-0364-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_build_provenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-05", "metric": "supplier_build_provenance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-05", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-05", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-05", "metric": "supplier_build_provenance_pct", "label": "supplier build provenance completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier build provenance completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_control_test_age_days_06(record):
    """Evaluate supplier control test age for control WP-0364-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-06", "metric": "supplier_control_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-06", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-06", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-06", "metric": "supplier_control_test_age_days", "label": "supplier control test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier control test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_vendor_master_change_count_07(record):
    """Evaluate supplier vendor-master changes for control WP-0364-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_master_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-07", "metric": "supplier_vendor_master_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-07", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-07", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-07", "metric": "supplier_vendor_master_change_count", "label": "supplier vendor-master changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier vendor-master changes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_component_shortage_count_08(record):
    """Evaluate supplier component shortages for control WP-0364-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_component_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-08", "metric": "supplier_component_shortage_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-08", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-08", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-08", "metric": "supplier_component_shortage_count", "label": "supplier component shortages",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier component shortages exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_collaboration_score_09(record):
    """Evaluate supplier collaboration score for control WP-0364-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_collaboration_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-09", "metric": "supplier_collaboration_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-09", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-09", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-09", "metric": "supplier_collaboration_score", "label": "supplier collaboration score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier collaboration score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_knowledge_handover_pct_10(record):
    """Evaluate supplier knowledge handover for control WP-0364-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-10", "metric": "supplier_knowledge_handover_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-10", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-10", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-10", "metric": "supplier_knowledge_handover_pct", "label": "supplier knowledge handover",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier knowledge handover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_damage_rate_pct_11(record):
    """Evaluate damage rate for control WP-0364-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-11", "metric": "damage_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-11", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-11", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-11", "metric": "damage_rate_pct", "label": "damage rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "damage rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_api_error_rate_pct_12(record):
    """Evaluate API error rate for control WP-0364-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_error_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-12", "metric": "api_error_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-12", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-12", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-12", "metric": "api_error_rate_pct", "label": "API error rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "API error rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_service_recovery_hours_13(record):
    """Evaluate service recovery time for control WP-0364-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_recovery_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-13", "metric": "service_recovery_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-13", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-13", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-13", "metric": "service_recovery_hours", "label": "service recovery time",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "service recovery time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_inspection_pass_pct_14(record):
    """Evaluate inspection pass rate for control WP-0364-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_pass_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-14", "metric": "inspection_pass_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-14", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-14", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-14", "metric": "inspection_pass_pct", "label": "inspection pass rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inspection pass rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_customs_document_score_15(record):
    """Evaluate customs documentation for control WP-0364-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_document_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-15", "metric": "customs_document_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-15", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-15", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-15", "metric": "customs_document_score", "label": "customs documentation",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customs documentation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_security_patch_compliance_pct_16(record):
    """Evaluate security patch compliance for control WP-0364-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_patch_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-16", "metric": "security_patch_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-16", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-16", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-16", "metric": "security_patch_compliance_pct", "label": "security patch compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "security patch compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_order_confirmation_minutes_17(record):
    """Evaluate order confirmation time for control WP-0364-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_confirmation_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-17", "metric": "order_confirmation_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-17", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-17", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-17", "metric": "order_confirmation_minutes", "label": "order confirmation time",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "order confirmation time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_air_quality_index_18(record):
    """Evaluate air quality index for control WP-0364-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("air_quality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-18", "metric": "air_quality_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-18", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-18", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-18", "metric": "air_quality_index", "label": "air quality index",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "air quality index must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_refund_completion_pct_19(record):
    """Evaluate refund completion for control WP-0364-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-19", "metric": "refund_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-19", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-19", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-19", "metric": "refund_completion_pct", "label": "refund completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "refund completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_coa_document_pct_20(record):
    """Evaluate certificate of analysis completeness for control WP-0364-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coa_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-20", "metric": "coa_document_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-20", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-20", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-20", "metric": "coa_document_pct", "label": "certificate of analysis completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "certificate of analysis completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_battery_swelling_signal_21(record):
    """Evaluate battery swelling signal for control WP-0364-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_swelling_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-21", "metric": "battery_swelling_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-21", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-21", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-21", "metric": "battery_swelling_signal", "label": "battery swelling signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "battery swelling signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_corrective_action_age_days_22(record):
    """Evaluate corrective action age for control WP-0364-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-22", "metric": "corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-22", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-22", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-22", "metric": "corrective_action_age_days", "label": "corrective action age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "corrective action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_surge_protection_test_age_days_23(record):
    """Evaluate surge protection test age for control WP-0364-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("surge_protection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-23", "metric": "surge_protection_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-23", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-23", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-23", "metric": "surge_protection_test_age_days", "label": "surge protection test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "surge protection test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_secret_scan_findings_24(record):
    """Evaluate secret scan findings for control WP-0364-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secret_scan_findings")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0364-24", "metric": "secret_scan_findings",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0364-24", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0364-24", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0364-24", "metric": "secret_scan_findings", "label": "secret scan findings",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "secret scan findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_supplier_customer_loss_pct_01, assess_supplier_continuous_improvement_count_02, assess_supplier_energy_per_inference_03, assess_supplier_slo_burn_rate_04, assess_supplier_build_provenance_pct_05, assess_supplier_control_test_age_days_06, assess_supplier_vendor_master_change_count_07, assess_supplier_component_shortage_count_08, assess_supplier_collaboration_score_09, assess_supplier_knowledge_handover_pct_10, assess_damage_rate_pct_11, assess_api_error_rate_pct_12, assess_service_recovery_hours_13, assess_inspection_pass_pct_14, assess_customs_document_score_15, assess_security_patch_compliance_pct_16, assess_order_confirmation_minutes_17, assess_air_quality_index_18, assess_refund_completion_pct_19, assess_coa_document_pct_20, assess_battery_swelling_signal_21, assess_corrective_action_age_days_22, assess_surge_protection_test_age_days_23, assess_secret_scan_findings_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

