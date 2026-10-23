"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_freight_audit_savings_pct_01(record):
    """Evaluate freight audit savings for control WP-0156-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_audit_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-01", "metric": "freight_audit_savings_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 48,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-01", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-01", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 48
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-01", "metric": "freight_audit_savings_pct", "label": "freight audit savings",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 48, "comparison": "min",
        "finding": "freight audit savings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_temperature_record_gap_count_02(record):
    """Evaluate temperature record gaps for control WP-0156-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-02", "metric": "temperature_record_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-02", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-02", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-02", "metric": "temperature_record_gap_count", "label": "temperature record gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "temperature record gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_scorecard_age_days_03(record):
    """Evaluate supplier scorecard age for control WP-0156-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-03", "metric": "supplier_scorecard_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-03", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-03", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-03", "metric": "supplier_scorecard_age_days", "label": "supplier scorecard age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier scorecard age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_recycled_content_pct_04(record):
    """Evaluate supplier recycled content for control WP-0156-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycled_content_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-04", "metric": "supplier_recycled_content_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-04", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-04", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-04", "metric": "supplier_recycled_content_pct", "label": "supplier recycled content",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier recycled content exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_shipment_consolidation_pct_05(record):
    """Evaluate supplier shipment consolidation for control WP-0156-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipment_consolidation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-05", "metric": "supplier_shipment_consolidation_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 92,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-05", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-05", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 92
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-05", "metric": "supplier_shipment_consolidation_pct", "label": "supplier shipment consolidation",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 92, "comparison": "min",
        "finding": "supplier shipment consolidation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_compliance_attestation_age_days_06(record):
    """Evaluate supplier compliance attestation age for control WP-0156-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compliance_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-06", "metric": "supplier_compliance_attestation_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-06", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-06", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-06", "metric": "supplier_compliance_attestation_age_days", "label": "supplier compliance attestation age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier compliance attestation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_revenue_dependency_pct_07(record):
    """Evaluate supplier revenue dependency for control WP-0156-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-07", "metric": "supplier_revenue_dependency_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-07", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-07", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-07", "metric": "supplier_revenue_dependency_pct", "label": "supplier revenue dependency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier revenue dependency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_recyclability_score_08(record):
    """Evaluate supplier recyclability for control WP-0156-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recyclability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-08", "metric": "supplier_recyclability_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-08", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-08", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-08", "metric": "supplier_recyclability_score", "label": "supplier recyclability",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier recyclability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_order_visibility_pct_09(record):
    """Evaluate supplier order visibility for control WP-0156-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-09", "metric": "supplier_order_visibility_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 41,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-09", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-09", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 41
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-09", "metric": "supplier_order_visibility_pct", "label": "supplier order visibility",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 41, "comparison": "min",
        "finding": "supplier order visibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_pfmea_age_days_10(record):
    """Evaluate supplier PFMEA age for control WP-0156-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pfmea_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-10", "metric": "supplier_pfmea_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-10", "metric": "supplier_pfmea_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-10", "metric": "supplier_pfmea_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-10", "metric": "supplier_pfmea_age_days", "label": "supplier PFMEA age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier PFMEA age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_health_surveillance_pct_11(record):
    """Evaluate supplier health surveillance for control WP-0156-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_health_surveillance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-11", "metric": "supplier_health_surveillance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-11", "metric": "supplier_health_surveillance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-11", "metric": "supplier_health_surveillance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-11", "metric": "supplier_health_surveillance_pct", "label": "supplier health surveillance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier health surveillance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_debt_ratio_pct_12(record):
    """Evaluate supplier debt ratio for control WP-0156-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_debt_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-12", "metric": "supplier_debt_ratio_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-12", "metric": "supplier_debt_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-12", "metric": "supplier_debt_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-12", "metric": "supplier_debt_ratio_pct", "label": "supplier debt ratio",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier debt ratio exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_record_retention_pct_13(record):
    """Evaluate supplier record retention for control WP-0156-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-13", "metric": "supplier_record_retention_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-13", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-13", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-13", "metric": "supplier_record_retention_pct", "label": "supplier record retention",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier record retention falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_training_data_lineage_pct_14(record):
    """Evaluate supplier training-data lineage for control WP-0156-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_data_lineage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-14", "metric": "supplier_training_data_lineage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-14", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-14", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-14", "metric": "supplier_training_data_lineage_pct", "label": "supplier training-data lineage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training-data lineage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_clock_skew_ms_15(record):
    """Evaluate supplier clock skew for control WP-0156-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clock_skew_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-15", "metric": "supplier_clock_skew_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-15", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-15", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-15", "metric": "supplier_clock_skew_ms", "label": "supplier clock skew",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier clock skew must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_secure_development_score_16(record):
    """Evaluate supplier secure-development score for control WP-0156-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_development_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-16", "metric": "supplier_secure_development_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-16", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-16", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-16", "metric": "supplier_secure_development_score", "label": "supplier secure-development score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier secure-development score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_asset_return_age_days_17(record):
    """Evaluate supplier asset return age for control WP-0156-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-17", "metric": "supplier_asset_return_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-17", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-17", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-17", "metric": "supplier_asset_return_age_days", "label": "supplier asset return age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier asset return age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_approval_limit_breach_count_18(record):
    """Evaluate supplier approval-limit breaches for control WP-0156-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_approval_limit_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-18", "metric": "supplier_approval_limit_breach_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-18", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-18", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-18", "metric": "supplier_approval_limit_breach_count", "label": "supplier approval-limit breaches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier approval-limit breaches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_frozen_horizon_change_count_19(record):
    """Evaluate frozen-horizon changes for control WP-0156-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_frozen_horizon_change_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-19", "metric": "supplier_frozen_horizon_change_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-19", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-19", "metric": "supplier_frozen_horizon_change_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-19", "metric": "supplier_frozen_horizon_change_count", "label": "frozen-horizon changes",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "frozen-horizon changes must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_delivery_confirmation_pct_20(record):
    """Evaluate supplier delivery confirmation for control WP-0156-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_confirmation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-20", "metric": "supplier_delivery_confirmation_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-20", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-20", "metric": "supplier_delivery_confirmation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-20", "metric": "supplier_delivery_confirmation_pct", "label": "supplier delivery confirmation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "supplier delivery confirmation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_data_wipe_verification_pct_21(record):
    """Evaluate supplier data-wipe verification for control WP-0156-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_wipe_verification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-21", "metric": "supplier_data_wipe_verification_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-21", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-21", "metric": "supplier_data_wipe_verification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-21", "metric": "supplier_data_wipe_verification_pct", "label": "supplier data-wipe verification",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier data-wipe verification falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_utilization_pct_22(record):
    """Evaluate capacity utilization for control WP-0156-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("utilization_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-22", "metric": "utilization_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-22", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-22", "metric": "utilization_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-22", "metric": "utilization_pct", "label": "capacity utilization",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "capacity utilization must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_replenishment_age_hours_23(record):
    """Evaluate replenishment age for control WP-0156-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replenishment_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-23", "metric": "replenishment_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-23", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-23", "metric": "replenishment_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-23", "metric": "replenishment_age_hours", "label": "replenishment age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "replenishment age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_slow_mover_pct_24(record):
    """Evaluate slow-moving inventory for control WP-0156-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slow_mover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0156-24", "metric": "slow_mover_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0156-24", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0156-24", "metric": "slow_mover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0156-24", "metric": "slow_mover_pct", "label": "slow-moving inventory",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "slow-moving inventory exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_freight_audit_savings_pct_01, assess_temperature_record_gap_count_02, assess_supplier_scorecard_age_days_03, assess_supplier_recycled_content_pct_04, assess_supplier_shipment_consolidation_pct_05, assess_supplier_compliance_attestation_age_days_06, assess_supplier_revenue_dependency_pct_07, assess_supplier_recyclability_score_08, assess_supplier_order_visibility_pct_09, assess_supplier_pfmea_age_days_10, assess_supplier_health_surveillance_pct_11, assess_supplier_debt_ratio_pct_12, assess_supplier_record_retention_pct_13, assess_supplier_training_data_lineage_pct_14, assess_supplier_clock_skew_ms_15, assess_supplier_secure_development_score_16, assess_supplier_asset_return_age_days_17, assess_supplier_approval_limit_breach_count_18, assess_supplier_frozen_horizon_change_count_19, assess_supplier_delivery_confirmation_pct_20, assess_supplier_data_wipe_verification_pct_21, assess_utilization_pct_22, assess_replenishment_age_hours_23, assess_slow_mover_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

