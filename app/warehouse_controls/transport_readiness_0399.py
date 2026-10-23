"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_spare_part_stockout_count_01(record):
    """Evaluate spare part stockouts for control WP-0399-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_part_stockout_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-01", "metric": "spare_part_stockout_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-01", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-01", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-01", "metric": "spare_part_stockout_count", "label": "spare part stockouts",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "spare part stockouts must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_recovery_point_minutes_02(record):
    """Evaluate recovery point for control WP-0399-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_point_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-02", "metric": "recovery_point_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-02", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-02", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-02", "metric": "recovery_point_minutes", "label": "recovery point",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recovery point must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_record_completeness_pct_03(record):
    """Evaluate record completeness for control WP-0399-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-03", "metric": "record_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-03", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-03", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-03", "metric": "record_completeness_pct", "label": "record completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "record completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_customer_master_gap_count_04(record):
    """Evaluate customer master gaps for control WP-0399-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-04", "metric": "customer_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-04", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-04", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-04", "metric": "customer_master_gap_count", "label": "customer master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "customer master gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_backup_days_05(record):
    """Evaluate backup supplier lead time for control WP-0399-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-05", "metric": "supplier_backup_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-05", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-05", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-05", "metric": "supplier_backup_days", "label": "backup supplier lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backup supplier lead time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_last_mile_handoff_age_hours_06(record):
    """Evaluate last-mile handoff age for control WP-0399-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("last_mile_handoff_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-06", "metric": "last_mile_handoff_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-06", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-06", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-06", "metric": "last_mile_handoff_age_hours", "label": "last-mile handoff age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "last-mile handoff age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_freight_audit_savings_pct_07(record):
    """Evaluate freight audit savings for control WP-0399-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_audit_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-07", "metric": "freight_audit_savings_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-07", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-07", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-07", "metric": "freight_audit_savings_pct", "label": "freight audit savings",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "freight audit savings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_temperature_record_gap_count_08(record):
    """Evaluate temperature record gaps for control WP-0399-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-08", "metric": "temperature_record_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-08", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-08", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-08", "metric": "temperature_record_gap_count", "label": "temperature record gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "temperature record gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_scorecard_age_days_09(record):
    """Evaluate supplier scorecard age for control WP-0399-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-09", "metric": "supplier_scorecard_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-09", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-09", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-09", "metric": "supplier_scorecard_age_days", "label": "supplier scorecard age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier scorecard age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_recycled_content_pct_10(record):
    """Evaluate supplier recycled content for control WP-0399-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycled_content_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-10", "metric": "supplier_recycled_content_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-10", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-10", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-10", "metric": "supplier_recycled_content_pct", "label": "supplier recycled content",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recycled content must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_shipment_consolidation_pct_11(record):
    """Evaluate supplier shipment consolidation for control WP-0399-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipment_consolidation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-11", "metric": "supplier_shipment_consolidation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-11", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-11", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-11", "metric": "supplier_shipment_consolidation_pct", "label": "supplier shipment consolidation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "supplier shipment consolidation exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_compliance_attestation_age_days_12(record):
    """Evaluate supplier compliance attestation age for control WP-0399-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compliance_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-12", "metric": "supplier_compliance_attestation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-12", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-12", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-12", "metric": "supplier_compliance_attestation_age_days", "label": "supplier compliance attestation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "supplier compliance attestation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_revenue_dependency_pct_13(record):
    """Evaluate supplier revenue dependency for control WP-0399-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-13", "metric": "supplier_revenue_dependency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-13", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-13", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-13", "metric": "supplier_revenue_dependency_pct", "label": "supplier revenue dependency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier revenue dependency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_recyclability_score_14(record):
    """Evaluate supplier recyclability for control WP-0399-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recyclability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-14", "metric": "supplier_recyclability_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-14", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-14", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-14", "metric": "supplier_recyclability_score", "label": "supplier recyclability",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier recyclability must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_order_visibility_pct_15(record):
    """Evaluate supplier order visibility for control WP-0399-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-15", "metric": "supplier_order_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-15", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-15", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-15", "metric": "supplier_order_visibility_pct", "label": "supplier order visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier order visibility exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_pfmea_age_days_16(record):
    """Evaluate supplier PFMEA age for control WP-0399-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_pfmea_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-16", "metric": "supplier_pfmea_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 14,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-16", "metric": "supplier_pfmea_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-16", "metric": "supplier_pfmea_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 14
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-16", "metric": "supplier_pfmea_age_days", "label": "supplier PFMEA age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 14, "comparison": "min",
        "finding": "supplier PFMEA age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_health_surveillance_pct_17(record):
    """Evaluate supplier health surveillance for control WP-0399-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_health_surveillance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-17", "metric": "supplier_health_surveillance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-17", "metric": "supplier_health_surveillance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-17", "metric": "supplier_health_surveillance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-17", "metric": "supplier_health_surveillance_pct", "label": "supplier health surveillance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier health surveillance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_debt_ratio_pct_18(record):
    """Evaluate supplier debt ratio for control WP-0399-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_debt_ratio_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-18", "metric": "supplier_debt_ratio_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-18", "metric": "supplier_debt_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-18", "metric": "supplier_debt_ratio_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-18", "metric": "supplier_debt_ratio_pct", "label": "supplier debt ratio",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier debt ratio must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_record_retention_pct_19(record):
    """Evaluate supplier record retention for control WP-0399-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_record_retention_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-19", "metric": "supplier_record_retention_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-19", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-19", "metric": "supplier_record_retention_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-19", "metric": "supplier_record_retention_pct", "label": "supplier record retention",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier record retention exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_training_data_lineage_pct_20(record):
    """Evaluate supplier training-data lineage for control WP-0399-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_data_lineage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-20", "metric": "supplier_training_data_lineage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-20", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-20", "metric": "supplier_training_data_lineage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-20", "metric": "supplier_training_data_lineage_pct", "label": "supplier training-data lineage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "supplier training-data lineage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_clock_skew_ms_21(record):
    """Evaluate supplier clock skew for control WP-0399-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_clock_skew_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-21", "metric": "supplier_clock_skew_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-21", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-21", "metric": "supplier_clock_skew_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-21", "metric": "supplier_clock_skew_ms", "label": "supplier clock skew",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier clock skew must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_secure_development_score_22(record):
    """Evaluate supplier secure-development score for control WP-0399-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_secure_development_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-22", "metric": "supplier_secure_development_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-22", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-22", "metric": "supplier_secure_development_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-22", "metric": "supplier_secure_development_score", "label": "supplier secure-development score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier secure-development score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_asset_return_age_days_23(record):
    """Evaluate supplier asset return age for control WP-0399-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asset_return_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-23", "metric": "supplier_asset_return_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-23", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-23", "metric": "supplier_asset_return_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-23", "metric": "supplier_asset_return_age_days", "label": "supplier asset return age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier asset return age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_approval_limit_breach_count_24(record):
    """Evaluate supplier approval-limit breaches for control WP-0399-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_approval_limit_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0399-24", "metric": "supplier_approval_limit_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0399-24", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0399-24", "metric": "supplier_approval_limit_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0399-24", "metric": "supplier_approval_limit_breach_count", "label": "supplier approval-limit breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "supplier approval-limit breaches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_spare_part_stockout_count_01, assess_recovery_point_minutes_02, assess_record_completeness_pct_03, assess_customer_master_gap_count_04, assess_supplier_backup_days_05, assess_last_mile_handoff_age_hours_06, assess_freight_audit_savings_pct_07, assess_temperature_record_gap_count_08, assess_supplier_scorecard_age_days_09, assess_supplier_recycled_content_pct_10, assess_supplier_shipment_consolidation_pct_11, assess_supplier_compliance_attestation_age_days_12, assess_supplier_revenue_dependency_pct_13, assess_supplier_recyclability_score_14, assess_supplier_order_visibility_pct_15, assess_supplier_pfmea_age_days_16, assess_supplier_health_surveillance_pct_17, assess_supplier_debt_ratio_pct_18, assess_supplier_record_retention_pct_19, assess_supplier_training_data_lineage_pct_20, assess_supplier_clock_skew_ms_21, assess_supplier_secure_development_score_22, assess_supplier_asset_return_age_days_23, assess_supplier_approval_limit_breach_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

