"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_driver_checkin_compliance_pct_01(record):
    """Evaluate driver check-in compliance for control WP-0157-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-01", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-01", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-01", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-01", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "max",
        "finding": "driver check-in compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_labor_productivity_index_02(record):
    """Evaluate labor productivity for control WP-0157-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-02", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-02", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-02", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-02", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "labor productivity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_label_compliance_pct_03(record):
    """Evaluate supplier label compliance for control WP-0157-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-03", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-03", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-03", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-03", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier label compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_obsolescence_notice_days_04(record):
    """Evaluate supplier obsolescence notice for control WP-0157-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-04", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-04", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-04", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-04", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier obsolescence notice must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_delivery_slot_compliance_pct_05(record):
    """Evaluate supplier delivery-slot compliance for control WP-0157-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-05", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-05", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-05", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-05", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "supplier delivery-slot compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_support_ack_minutes_06(record):
    """Evaluate supplier support acknowledgement for control WP-0157-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-06", "metric": "supplier_support_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-06", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-06", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-06", "metric": "supplier_support_ack_minutes", "label": "supplier support acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier support acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_serial_data_completeness_pct_07(record):
    """Evaluate supplier serial-data completeness for control WP-0157-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-07", "metric": "supplier_serial_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-07", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-07", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-07", "metric": "supplier_serial_data_completeness_pct", "label": "supplier serial-data completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier serial-data completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_personnel_screening_pct_08(record):
    """Evaluate supplier personnel screening for control WP-0157-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-08", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-08", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-08", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-08", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier personnel screening must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_knowledge_transfer_pct_09(record):
    """Evaluate supplier knowledge transfer for control WP-0157-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-09", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-09", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-09", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-09", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "supplier knowledge transfer exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_product_compliance_pct_10(record):
    """Evaluate supplier product compliance for control WP-0157-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-10", "metric": "supplier_product_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-10", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-10", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-10", "metric": "supplier_product_compliance_pct", "label": "supplier product compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier product compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_beneficial_owner_gap_count_11(record):
    """Evaluate supplier beneficial-owner gaps for control WP-0157-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_beneficial_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-11", "metric": "supplier_beneficial_owner_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-11", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-11", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-11", "metric": "supplier_beneficial_owner_gap_count", "label": "supplier beneficial-owner gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier beneficial-owner gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_substitute_material_pct_12(record):
    """Evaluate supplier substitute material coverage for control WP-0157-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_material_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-12", "metric": "supplier_substitute_material_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-12", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-12", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-12", "metric": "supplier_substitute_material_pct", "label": "supplier substitute material coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier substitute material coverage must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_iot_coverage_pct_13(record):
    """Evaluate supplier IoT coverage for control WP-0157-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_iot_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-13", "metric": "supplier_iot_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-13", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-13", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-13", "metric": "supplier_iot_coverage_pct", "label": "supplier IoT coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier IoT coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_experiment_guardrail_breach_count_14(record):
    """Evaluate supplier experiment guardrail breaches for control WP-0157-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_experiment_guardrail_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-14", "metric": "supplier_experiment_guardrail_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-14", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-14", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-14", "metric": "supplier_experiment_guardrail_breach_count", "label": "supplier experiment guardrail breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "supplier experiment guardrail breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_data_residency_gap_count_15(record):
    """Evaluate supplier data-residency gaps for control WP-0157-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_residency_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-15", "metric": "supplier_data_residency_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-15", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-15", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-15", "metric": "supplier_data_residency_gap_count", "label": "supplier data-residency gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-residency gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dpia_completion_pct_16(record):
    """Evaluate supplier DPIA completion for control WP-0157-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dpia_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-16", "metric": "supplier_dpia_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-16", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-16", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-16", "metric": "supplier_dpia_completion_pct", "label": "supplier DPIA completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier DPIA completion must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_risk_trend_score_17(record):
    """Evaluate supplier risk trend for control WP-0157-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_trend_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-17", "metric": "supplier_risk_trend_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-17", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-17", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-17", "metric": "supplier_risk_trend_score", "label": "supplier risk trend",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier risk trend exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_tax_rate_variance_pct_18(record):
    """Evaluate supplier tax-rate variance for control WP-0157-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-18", "metric": "supplier_tax_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-18", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-18", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-18", "metric": "supplier_tax_rate_variance_pct", "label": "supplier tax-rate variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "supplier tax-rate variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_queue_time_hours_19(record):
    """Evaluate supplier queue time for control WP-0157-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_queue_time_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-19", "metric": "supplier_queue_time_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-19", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-19", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-19", "metric": "supplier_queue_time_hours", "label": "supplier queue time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier queue time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_preferred_status_review_age_days_20(record):
    """Evaluate preferred status review age for control WP-0157-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-20", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-20", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-20", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-20", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "preferred status review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_post_exit_data_transfer_count_21(record):
    """Evaluate post-exit data transfers for control WP-0157-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-21", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-21", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-21", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-21", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "post-exit data transfers exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_lot_age_days_22(record):
    """Evaluate lot age for control WP-0157-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-22", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-22", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-22", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-22", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "lot age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_cold_chain_excursion_minutes_23(record):
    """Evaluate cold-chain excursion for control WP-0157-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-23", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-23", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-23", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-23", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold-chain excursion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_smoke_alarm_signal_24(record):
    """Evaluate smoke alarm signal for control WP-0157-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0157-24", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0157-24", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0157-24", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0157-24", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "smoke alarm signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_driver_checkin_compliance_pct_01, assess_labor_productivity_index_02, assess_supplier_label_compliance_pct_03, assess_supplier_obsolescence_notice_days_04, assess_supplier_delivery_slot_compliance_pct_05, assess_supplier_support_ack_minutes_06, assess_supplier_serial_data_completeness_pct_07, assess_supplier_personnel_screening_pct_08, assess_supplier_knowledge_transfer_pct_09, assess_supplier_product_compliance_pct_10, assess_supplier_beneficial_owner_gap_count_11, assess_supplier_substitute_material_pct_12, assess_supplier_iot_coverage_pct_13, assess_supplier_experiment_guardrail_breach_count_14, assess_supplier_data_residency_gap_count_15, assess_supplier_dpia_completion_pct_16, assess_supplier_risk_trend_score_17, assess_supplier_tax_rate_variance_pct_18, assess_supplier_queue_time_hours_19, assess_supplier_preferred_status_review_age_days_20, assess_supplier_post_exit_data_transfer_count_21, assess_lot_age_days_22, assess_cold_chain_excursion_minutes_23, assess_smoke_alarm_signal_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

