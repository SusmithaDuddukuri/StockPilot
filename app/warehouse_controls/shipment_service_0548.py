"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_personnel_screening_pct_01(record):
    """Evaluate supplier personnel screening for control WP-0548-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-01", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-01", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-01", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-01", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier personnel screening falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_knowledge_transfer_pct_02(record):
    """Evaluate supplier knowledge transfer for control WP-0548-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-02", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-02", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-02", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-02", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier knowledge transfer must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_product_compliance_pct_03(record):
    """Evaluate supplier product compliance for control WP-0548-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-03", "metric": "supplier_product_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-03", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-03", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-03", "metric": "supplier_product_compliance_pct", "label": "supplier product compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier product compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_beneficial_owner_gap_count_04(record):
    """Evaluate supplier beneficial-owner gaps for control WP-0548-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_beneficial_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-04", "metric": "supplier_beneficial_owner_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-04", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-04", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-04", "metric": "supplier_beneficial_owner_gap_count", "label": "supplier beneficial-owner gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "supplier beneficial-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_substitute_material_pct_05(record):
    """Evaluate supplier substitute material coverage for control WP-0548-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_material_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-05", "metric": "supplier_substitute_material_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-05", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-05", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-05", "metric": "supplier_substitute_material_pct", "label": "supplier substitute material coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier substitute material coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_iot_coverage_pct_06(record):
    """Evaluate supplier IoT coverage for control WP-0548-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_iot_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-06", "metric": "supplier_iot_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-06", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-06", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-06", "metric": "supplier_iot_coverage_pct", "label": "supplier IoT coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier IoT coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_experiment_guardrail_breach_count_07(record):
    """Evaluate supplier experiment guardrail breaches for control WP-0548-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_experiment_guardrail_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-07", "metric": "supplier_experiment_guardrail_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-07", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-07", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-07", "metric": "supplier_experiment_guardrail_breach_count", "label": "supplier experiment guardrail breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier experiment guardrail breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_data_residency_gap_count_08(record):
    """Evaluate supplier data-residency gaps for control WP-0548-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_residency_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-08", "metric": "supplier_data_residency_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-08", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-08", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-08", "metric": "supplier_data_residency_gap_count", "label": "supplier data-residency gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "supplier data-residency gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_dpia_completion_pct_09(record):
    """Evaluate supplier DPIA completion for control WP-0548-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dpia_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-09", "metric": "supplier_dpia_completion_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-09", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-09", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-09", "metric": "supplier_dpia_completion_pct", "label": "supplier DPIA completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "supplier DPIA completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_risk_trend_score_10(record):
    """Evaluate supplier risk trend for control WP-0548-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_risk_trend_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-10", "metric": "supplier_risk_trend_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-10", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-10", "metric": "supplier_risk_trend_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-10", "metric": "supplier_risk_trend_score", "label": "supplier risk trend",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier risk trend must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_tax_rate_variance_pct_11(record):
    """Evaluate supplier tax-rate variance for control WP-0548-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tax_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-11", "metric": "supplier_tax_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-11", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-11", "metric": "supplier_tax_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-11", "metric": "supplier_tax_rate_variance_pct", "label": "supplier tax-rate variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier tax-rate variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_queue_time_hours_12(record):
    """Evaluate supplier queue time for control WP-0548-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_queue_time_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-12", "metric": "supplier_queue_time_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-12", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-12", "metric": "supplier_queue_time_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-12", "metric": "supplier_queue_time_hours", "label": "supplier queue time",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "supplier queue time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_preferred_status_review_age_days_13(record):
    """Evaluate preferred status review age for control WP-0548-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_preferred_status_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-13", "metric": "supplier_preferred_status_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-13", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-13", "metric": "supplier_preferred_status_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-13", "metric": "supplier_preferred_status_review_age_days", "label": "preferred status review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "preferred status review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_post_exit_data_transfer_count_14(record):
    """Evaluate post-exit data transfers for control WP-0548-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_post_exit_data_transfer_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-14", "metric": "supplier_post_exit_data_transfer_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-14", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-14", "metric": "supplier_post_exit_data_transfer_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-14", "metric": "supplier_post_exit_data_transfer_count", "label": "post-exit data transfers",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "post-exit data transfers must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_lot_age_days_15(record):
    """Evaluate lot age for control WP-0548-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-15", "metric": "lot_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-15", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-15", "metric": "lot_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-15", "metric": "lot_age_days", "label": "lot age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "lot age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_cold_chain_excursion_minutes_16(record):
    """Evaluate cold-chain excursion for control WP-0548-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_chain_excursion_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-16", "metric": "cold_chain_excursion_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-16", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-16", "metric": "cold_chain_excursion_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-16", "metric": "cold_chain_excursion_minutes", "label": "cold-chain excursion",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "cold-chain excursion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_smoke_alarm_signal_17(record):
    """Evaluate smoke alarm signal for control WP-0548-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("smoke_alarm_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-17", "metric": "smoke_alarm_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-17", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-17", "metric": "smoke_alarm_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-17", "metric": "smoke_alarm_signal", "label": "smoke alarm signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "smoke alarm signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_label_reprint_count_18(record):
    """Evaluate label reprints for control WP-0548-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("label_reprint_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-18", "metric": "label_reprint_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-18", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-18", "metric": "label_reprint_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-18", "metric": "label_reprint_count", "label": "label reprints",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "label reprints must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_putaway_accuracy_pct_19(record):
    """Evaluate putaway accuracy for control WP-0548-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("putaway_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-19", "metric": "putaway_accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-19", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-19", "metric": "putaway_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-19", "metric": "putaway_accuracy_pct", "label": "putaway accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "putaway accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_dead_letter_count_20(record):
    """Evaluate dead-letter messages for control WP-0548-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dead_letter_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-20", "metric": "dead_letter_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "messages",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-20", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-20", "metric": "dead_letter_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-20", "metric": "dead_letter_count", "label": "dead-letter messages",
        "status": "breach", "severity": "critical", "unit": "messages",
        "observed": observed,
        "threshold": 39, "comparison": "max",
        "finding": "dead-letter messages exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_each_pick_ratio_pct_21(record):
    """Evaluate each pick ratio for control WP-0548-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("each_pick_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-21", "metric": "each_pick_ratio_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-21", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-21", "metric": "each_pick_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-21", "metric": "each_pick_ratio_pct", "label": "each pick ratio",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "each pick ratio falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_camera_coverage_pct_22(record):
    """Evaluate camera coverage for control WP-0548-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("camera_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-22", "metric": "camera_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-22", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-22", "metric": "camera_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-22", "metric": "camera_coverage_pct", "label": "camera coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "camera coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_energy_peak_kw_23(record):
    """Evaluate peak power demand for control WP-0548-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("energy_peak_kw")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-23", "metric": "energy_peak_kw",
            "status": "insufficient_data",
            "severity": "high", "unit": "kW",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-23", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-23", "metric": "energy_peak_kw", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-23", "metric": "energy_peak_kw", "label": "peak power demand",
        "status": "breach", "severity": "high", "unit": "kW",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "peak power demand must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_insurance_coverage_pct_24(record):
    """Evaluate insurance coverage for control WP-0548-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0548-24", "metric": "insurance_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0548-24", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0548-24", "metric": "insurance_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0548-24", "metric": "insurance_coverage_pct", "label": "insurance coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 59, "comparison": "max",
        "finding": "insurance coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_supplier_personnel_screening_pct_01, assess_supplier_knowledge_transfer_pct_02, assess_supplier_product_compliance_pct_03, assess_supplier_beneficial_owner_gap_count_04, assess_supplier_substitute_material_pct_05, assess_supplier_iot_coverage_pct_06, assess_supplier_experiment_guardrail_breach_count_07, assess_supplier_data_residency_gap_count_08, assess_supplier_dpia_completion_pct_09, assess_supplier_risk_trend_score_10, assess_supplier_tax_rate_variance_pct_11, assess_supplier_queue_time_hours_12, assess_supplier_preferred_status_review_age_days_13, assess_supplier_post_exit_data_transfer_count_14, assess_lot_age_days_15, assess_cold_chain_excursion_minutes_16, assess_smoke_alarm_signal_17, assess_label_reprint_count_18, assess_putaway_accuracy_pct_19, assess_dead_letter_count_20, assess_each_pick_ratio_pct_21, assess_camera_coverage_pct_22, assess_energy_peak_kw_23, assess_insurance_coverage_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

