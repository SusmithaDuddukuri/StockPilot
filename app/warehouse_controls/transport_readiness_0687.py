"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_build_provenance_pct_01(record):
    """Evaluate supplier build provenance completeness for control WP-0687-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_build_provenance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-01", "metric": "supplier_build_provenance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-01", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-01", "metric": "supplier_build_provenance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-01", "metric": "supplier_build_provenance_pct", "label": "supplier build provenance completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier build provenance completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_control_test_age_days_02(record):
    """Evaluate supplier control test age for control WP-0687-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_control_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-02", "metric": "supplier_control_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-02", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-02", "metric": "supplier_control_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-02", "metric": "supplier_control_test_age_days", "label": "supplier control test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier control test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_vendor_master_change_count_03(record):
    """Evaluate supplier vendor-master changes for control WP-0687-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_vendor_master_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-03", "metric": "supplier_vendor_master_change_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-03", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-03", "metric": "supplier_vendor_master_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-03", "metric": "supplier_vendor_master_change_count", "label": "supplier vendor-master changes",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier vendor-master changes exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_component_shortage_count_04(record):
    """Evaluate supplier component shortages for control WP-0687-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_component_shortage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-04", "metric": "supplier_component_shortage_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-04", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-04", "metric": "supplier_component_shortage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-04", "metric": "supplier_component_shortage_count", "label": "supplier component shortages",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "supplier component shortages falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_collaboration_score_05(record):
    """Evaluate supplier collaboration score for control WP-0687-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_collaboration_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-05", "metric": "supplier_collaboration_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-05", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-05", "metric": "supplier_collaboration_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-05", "metric": "supplier_collaboration_score", "label": "supplier collaboration score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier collaboration score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_knowledge_handover_pct_06(record):
    """Evaluate supplier knowledge handover for control WP-0687-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_handover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-06", "metric": "supplier_knowledge_handover_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-06", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-06", "metric": "supplier_knowledge_handover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-06", "metric": "supplier_knowledge_handover_pct", "label": "supplier knowledge handover",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier knowledge handover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_damage_rate_pct_07(record):
    """Evaluate damage rate for control WP-0687-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("damage_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-07", "metric": "damage_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-07", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-07", "metric": "damage_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-07", "metric": "damage_rate_pct", "label": "damage rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "damage rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_api_error_rate_pct_08(record):
    """Evaluate API error rate for control WP-0687-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("api_error_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-08", "metric": "api_error_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-08", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-08", "metric": "api_error_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-08", "metric": "api_error_rate_pct", "label": "API error rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "API error rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_service_recovery_hours_09(record):
    """Evaluate service recovery time for control WP-0687-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("service_recovery_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-09", "metric": "service_recovery_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-09", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-09", "metric": "service_recovery_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-09", "metric": "service_recovery_hours", "label": "service recovery time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "service recovery time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_inspection_pass_pct_10(record):
    """Evaluate inspection pass rate for control WP-0687-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_pass_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-10", "metric": "inspection_pass_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-10", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-10", "metric": "inspection_pass_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-10", "metric": "inspection_pass_pct", "label": "inspection pass rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inspection pass rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_customs_document_score_11(record):
    """Evaluate customs documentation for control WP-0687-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customs_document_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-11", "metric": "customs_document_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-11", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-11", "metric": "customs_document_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-11", "metric": "customs_document_score", "label": "customs documentation",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "customs documentation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_security_patch_compliance_pct_12(record):
    """Evaluate security patch compliance for control WP-0687-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("security_patch_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-12", "metric": "security_patch_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-12", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-12", "metric": "security_patch_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-12", "metric": "security_patch_compliance_pct", "label": "security patch compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "security patch compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_order_confirmation_minutes_13(record):
    """Evaluate order confirmation time for control WP-0687-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_confirmation_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-13", "metric": "order_confirmation_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-13", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-13", "metric": "order_confirmation_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-13", "metric": "order_confirmation_minutes", "label": "order confirmation time",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "order confirmation time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_air_quality_index_14(record):
    """Evaluate air quality index for control WP-0687-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("air_quality_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-14", "metric": "air_quality_index",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-14", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-14", "metric": "air_quality_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-14", "metric": "air_quality_index", "label": "air quality index",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "air quality index must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_refund_completion_pct_15(record):
    """Evaluate refund completion for control WP-0687-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refund_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-15", "metric": "refund_completion_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-15", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-15", "metric": "refund_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-15", "metric": "refund_completion_pct", "label": "refund completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "refund completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_coa_document_pct_16(record):
    """Evaluate certificate of analysis completeness for control WP-0687-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coa_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-16", "metric": "coa_document_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-16", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-16", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-16", "metric": "coa_document_pct", "label": "certificate of analysis completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "certificate of analysis completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_battery_swelling_signal_17(record):
    """Evaluate battery swelling signal for control WP-0687-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_swelling_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-17", "metric": "battery_swelling_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-17", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-17", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-17", "metric": "battery_swelling_signal", "label": "battery swelling signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "battery swelling signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_corrective_action_age_days_18(record):
    """Evaluate corrective action age for control WP-0687-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-18", "metric": "corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-18", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-18", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-18", "metric": "corrective_action_age_days", "label": "corrective action age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "corrective action age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_surge_protection_test_age_days_19(record):
    """Evaluate surge protection test age for control WP-0687-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("surge_protection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-19", "metric": "surge_protection_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-19", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-19", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-19", "metric": "surge_protection_test_age_days", "label": "surge protection test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 41, "comparison": "max",
        "finding": "surge protection test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_secret_scan_findings_20(record):
    """Evaluate secret scan findings for control WP-0687-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secret_scan_findings")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-20", "metric": "secret_scan_findings",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-20", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-20", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-20", "metric": "secret_scan_findings", "label": "secret scan findings",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "secret scan findings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_scanner_read_rate_pct_21(record):
    """Evaluate scanner read rate for control WP-0687-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-21", "metric": "scanner_read_rate_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-21", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-21", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-21", "metric": "scanner_read_rate_pct", "label": "scanner read rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner read rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_adjustment_reason_completeness_pct_22(record):
    """Evaluate adjustment reason completeness for control WP-0687-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("adjustment_reason_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-22", "metric": "adjustment_reason_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-22", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-22", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-22", "metric": "adjustment_reason_completeness_pct", "label": "adjustment reason completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "adjustment reason completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_pick_confirmation_latency_ms_23(record):
    """Evaluate pick confirmation latency for control WP-0687-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_confirmation_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-23", "metric": "pick_confirmation_latency_ms",
            "status": "insufficient_data",
            "severity": "medium", "unit": "ms",
            "observed": None,
            "threshold": 61,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-23", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-23", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 61
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-23", "metric": "pick_confirmation_latency_ms", "label": "pick confirmation latency",
        "status": "breach", "severity": "medium", "unit": "ms",
        "observed": observed,
        "threshold": 61, "comparison": "max",
        "finding": "pick confirmation latency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_bonded_stock_variance_24(record):
    """Evaluate bonded stock variance for control WP-0687-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bonded_stock_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0687-24", "metric": "bonded_stock_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0687-24", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0687-24", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0687-24", "metric": "bonded_stock_variance", "label": "bonded stock variance",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "bonded stock variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_build_provenance_pct_01, assess_supplier_control_test_age_days_02, assess_supplier_vendor_master_change_count_03, assess_supplier_component_shortage_count_04, assess_supplier_collaboration_score_05, assess_supplier_knowledge_handover_pct_06, assess_damage_rate_pct_07, assess_api_error_rate_pct_08, assess_service_recovery_hours_09, assess_inspection_pass_pct_10, assess_customs_document_score_11, assess_security_patch_compliance_pct_12, assess_order_confirmation_minutes_13, assess_air_quality_index_14, assess_refund_completion_pct_15, assess_coa_document_pct_16, assess_battery_swelling_signal_17, assess_corrective_action_age_days_18, assess_surge_protection_test_age_days_19, assess_secret_scan_findings_20, assess_scanner_read_rate_pct_21, assess_adjustment_reason_completeness_pct_22, assess_pick_confirmation_latency_ms_23, assess_bonded_stock_variance_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

