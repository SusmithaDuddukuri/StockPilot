"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_labor_productivity_index_01(record):
    """Evaluate labor productivity for control WP-0412-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-01", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-01", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-01", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-01", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "labor productivity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_label_compliance_pct_02(record):
    """Evaluate supplier label compliance for control WP-0412-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-02", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-02", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-02", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-02", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_obsolescence_notice_days_03(record):
    """Evaluate supplier obsolescence notice for control WP-0412-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-03", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-03", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-03", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-03", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier obsolescence notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_delivery_slot_compliance_pct_04(record):
    """Evaluate supplier delivery-slot compliance for control WP-0412-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-04", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-04", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-04", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-04", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier delivery-slot compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_support_ack_minutes_05(record):
    """Evaluate supplier support acknowledgement for control WP-0412-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-05", "metric": "supplier_support_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-05", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-05", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-05", "metric": "supplier_support_ack_minutes", "label": "supplier support acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "supplier support acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_serial_data_completeness_pct_06(record):
    """Evaluate supplier serial-data completeness for control WP-0412-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-06", "metric": "supplier_serial_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-06", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-06", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-06", "metric": "supplier_serial_data_completeness_pct", "label": "supplier serial-data completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier serial-data completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_personnel_screening_pct_07(record):
    """Evaluate supplier personnel screening for control WP-0412-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-07", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-07", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-07", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-07", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier personnel screening must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_knowledge_transfer_pct_08(record):
    """Evaluate supplier knowledge transfer for control WP-0412-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-08", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-08", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-08", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-08", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier knowledge transfer exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_product_compliance_pct_09(record):
    """Evaluate supplier product compliance for control WP-0412-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-09", "metric": "supplier_product_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-09", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-09", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-09", "metric": "supplier_product_compliance_pct", "label": "supplier product compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "supplier product compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_beneficial_owner_gap_count_10(record):
    """Evaluate supplier beneficial-owner gaps for control WP-0412-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_beneficial_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-10", "metric": "supplier_beneficial_owner_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-10", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-10", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-10", "metric": "supplier_beneficial_owner_gap_count", "label": "supplier beneficial-owner gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier beneficial-owner gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_substitute_material_pct_11(record):
    """Evaluate supplier substitute material coverage for control WP-0412-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_material_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-11", "metric": "supplier_substitute_material_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-11", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-11", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-11", "metric": "supplier_substitute_material_pct", "label": "supplier substitute material coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier substitute material coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_iot_coverage_pct_12(record):
    """Evaluate supplier IoT coverage for control WP-0412-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_iot_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-12", "metric": "supplier_iot_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-12", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-12", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-12", "metric": "supplier_iot_coverage_pct", "label": "supplier IoT coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "supplier IoT coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_experiment_guardrail_breach_count_13(record):
    """Evaluate supplier experiment guardrail breaches for control WP-0412-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_experiment_guardrail_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-13", "metric": "supplier_experiment_guardrail_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-13", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-13", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-13", "metric": "supplier_experiment_guardrail_breach_count", "label": "supplier experiment guardrail breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier experiment guardrail breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_data_residency_gap_count_14(record):
    """Evaluate supplier data-residency gaps for control WP-0412-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_residency_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-14", "metric": "supplier_data_residency_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-14", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-14", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-14", "metric": "supplier_data_residency_gap_count", "label": "supplier data-residency gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-residency gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_dpia_completion_pct_15(record):
    """Evaluate supplier DPIA completion for control WP-0412-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dpia_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-15", "metric": "supplier_dpia_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-15", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-15", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-15", "metric": "supplier_dpia_completion_pct", "label": "supplier DPIA completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier DPIA completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_risk_trend_score_16(record):
    """Evaluate supplier risk trend for control WP-0412-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_trend_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-16", "metric": "supplier_risk_trend_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-16", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-16", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-16", "metric": "supplier_risk_trend_score", "label": "supplier risk trend",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "supplier risk trend exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_tax_rate_variance_pct_17(record):
    """Evaluate supplier tax-rate variance for control WP-0412-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-17", "metric": "supplier_tax_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-17", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-17", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-17", "metric": "supplier_tax_rate_variance_pct", "label": "supplier tax-rate variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "supplier tax-rate variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_queue_time_hours_18(record):
    """Evaluate supplier queue time for control WP-0412-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_queue_time_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-18", "metric": "supplier_queue_time_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-18", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-18", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-18", "metric": "supplier_queue_time_hours", "label": "supplier queue time",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier queue time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_preferred_status_review_age_days_19(record):
    """Evaluate preferred status review age for control WP-0412-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-19", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-19", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-19", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-19", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "preferred status review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_post_exit_data_transfer_count_20(record):
    """Evaluate post-exit data transfers for control WP-0412-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-20", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-20", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-20", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-20", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "post-exit data transfers exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_lot_age_days_21(record):
    """Evaluate lot age for control WP-0412-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-21", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-21", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-21", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-21", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "lot age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_cold_chain_excursion_minutes_22(record):
    """Evaluate cold-chain excursion for control WP-0412-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-22", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-22", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-22", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-22", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold-chain excursion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_smoke_alarm_signal_23(record):
    """Evaluate smoke alarm signal for control WP-0412-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-23", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-23", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-23", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-23", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "smoke alarm signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_label_reprint_count_24(record):
    """Evaluate label reprints for control WP-0412-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_reprint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0412-24", "metric": "label_reprint_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0412-24", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0412-24", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0412-24", "metric": "label_reprint_count", "label": "label reprints",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "label reprints exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_labor_productivity_index_01, assess_supplier_label_compliance_pct_02, assess_supplier_obsolescence_notice_days_03, assess_supplier_delivery_slot_compliance_pct_04, assess_supplier_support_ack_minutes_05, assess_supplier_serial_data_completeness_pct_06, assess_supplier_personnel_screening_pct_07, assess_supplier_knowledge_transfer_pct_08, assess_supplier_product_compliance_pct_09, assess_supplier_beneficial_owner_gap_count_10, assess_supplier_substitute_material_pct_11, assess_supplier_iot_coverage_pct_12, assess_supplier_experiment_guardrail_breach_count_13, assess_supplier_data_residency_gap_count_14, assess_supplier_dpia_completion_pct_15, assess_supplier_risk_trend_score_16, assess_supplier_tax_rate_variance_pct_17, assess_supplier_queue_time_hours_18, assess_supplier_preferred_status_review_age_days_19, assess_supplier_post_exit_data_transfer_count_20, assess_lot_age_days_21, assess_cold_chain_excursion_minutes_22, assess_smoke_alarm_signal_23, assess_label_reprint_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

