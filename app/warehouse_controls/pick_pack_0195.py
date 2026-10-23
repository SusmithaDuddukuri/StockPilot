"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_congestion_score_01(record):
    """Evaluate congestion score for control WP-0195-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-01", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-01", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-01", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-01", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "congestion score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_charger_queue_minutes_02(record):
    """Evaluate charger queue for control WP-0195-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-02", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-02", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-02", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-02", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "charger queue must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_invoice_age_days_03(record):
    """Evaluate invoice age for control WP-0195-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-03", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-03", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-03", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-03", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "invoice age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_cache_hit_pct_04(record):
    """Evaluate cache hit rate for control WP-0195-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-04", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-04", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-04", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-04", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "cache hit rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_pack_size_variance_05(record):
    """Evaluate pack-size variance for control WP-0195-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_size_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-05", "metric": "pack_size_variance",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-05", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-05", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-05", "metric": "pack_size_variance", "label": "pack-size variance",
        "status": "breach", "severity": "critical", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pack-size variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_handover_ack_pct_06(record):
    """Evaluate handover acknowledgement for control WP-0195-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-06", "metric": "handover_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-06", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-06", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-06", "metric": "handover_ack_pct", "label": "handover acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "handover acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_environmental_incident_count_07(record):
    """Evaluate environmental incidents for control WP-0195-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("environmental_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-07", "metric": "environmental_incident_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-07", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-07", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-07", "metric": "environmental_incident_count", "label": "environmental incidents",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "environmental incidents exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_dual_control_compliance_pct_08(record):
    """Evaluate dual control compliance for control WP-0195-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dual_control_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-08", "metric": "dual_control_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-08", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-08", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-08", "metric": "dual_control_compliance_pct", "label": "dual control compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "dual control compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_chemical_inventory_reconcile_pct_09(record):
    """Evaluate chemical inventory reconciliation for control WP-0195-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chemical_inventory_reconcile_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-09", "metric": "chemical_inventory_reconcile_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-09", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-09", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-09", "metric": "chemical_inventory_reconcile_pct", "label": "chemical inventory reconciliation",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "chemical inventory reconciliation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_spare_part_stockout_count_10(record):
    """Evaluate spare part stockouts for control WP-0195-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_part_stockout_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-10", "metric": "spare_part_stockout_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-10", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-10", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-10", "metric": "spare_part_stockout_count", "label": "spare part stockouts",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "spare part stockouts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_recovery_point_minutes_11(record):
    """Evaluate recovery point for control WP-0195-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_point_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-11", "metric": "recovery_point_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-11", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-11", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-11", "metric": "recovery_point_minutes", "label": "recovery point",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "recovery point exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_record_completeness_pct_12(record):
    """Evaluate record completeness for control WP-0195-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-12", "metric": "record_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-12", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-12", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-12", "metric": "record_completeness_pct", "label": "record completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "record completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_customer_master_gap_count_13(record):
    """Evaluate customer master gaps for control WP-0195-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-13", "metric": "customer_master_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-13", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-13", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-13", "metric": "customer_master_gap_count", "label": "customer master gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "customer master gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_backup_days_14(record):
    """Evaluate backup supplier lead time for control WP-0195-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-14", "metric": "supplier_backup_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-14", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-14", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-14", "metric": "supplier_backup_days", "label": "backup supplier lead time",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backup supplier lead time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_last_mile_handoff_age_hours_15(record):
    """Evaluate last-mile handoff age for control WP-0195-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("last_mile_handoff_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-15", "metric": "last_mile_handoff_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-15", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-15", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-15", "metric": "last_mile_handoff_age_hours", "label": "last-mile handoff age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "last-mile handoff age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_freight_audit_savings_pct_16(record):
    """Evaluate freight audit savings for control WP-0195-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_audit_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-16", "metric": "freight_audit_savings_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-16", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-16", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-16", "metric": "freight_audit_savings_pct", "label": "freight audit savings",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "freight audit savings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_temperature_record_gap_count_17(record):
    """Evaluate temperature record gaps for control WP-0195-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-17", "metric": "temperature_record_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-17", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-17", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-17", "metric": "temperature_record_gap_count", "label": "temperature record gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "temperature record gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_scorecard_age_days_18(record):
    """Evaluate supplier scorecard age for control WP-0195-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-18", "metric": "supplier_scorecard_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-18", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-18", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-18", "metric": "supplier_scorecard_age_days", "label": "supplier scorecard age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier scorecard age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_recycled_content_pct_19(record):
    """Evaluate supplier recycled content for control WP-0195-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycled_content_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-19", "metric": "supplier_recycled_content_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 125,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-19", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-19", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 125
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-19", "metric": "supplier_recycled_content_pct", "label": "supplier recycled content",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 125, "comparison": "max",
        "finding": "supplier recycled content exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_shipment_consolidation_pct_20(record):
    """Evaluate supplier shipment consolidation for control WP-0195-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipment_consolidation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-20", "metric": "supplier_shipment_consolidation_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-20", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-20", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-20", "metric": "supplier_shipment_consolidation_pct", "label": "supplier shipment consolidation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "supplier shipment consolidation falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_compliance_attestation_age_days_21(record):
    """Evaluate supplier compliance attestation age for control WP-0195-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compliance_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-21", "metric": "supplier_compliance_attestation_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-21", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-21", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-21", "metric": "supplier_compliance_attestation_age_days", "label": "supplier compliance attestation age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier compliance attestation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_revenue_dependency_pct_22(record):
    """Evaluate supplier revenue dependency for control WP-0195-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-22", "metric": "supplier_revenue_dependency_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-22", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-22", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-22", "metric": "supplier_revenue_dependency_pct", "label": "supplier revenue dependency",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier revenue dependency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_recyclability_score_23(record):
    """Evaluate supplier recyclability for control WP-0195-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recyclability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-23", "metric": "supplier_recyclability_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 145,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-23", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-23", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 145
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-23", "metric": "supplier_recyclability_score", "label": "supplier recyclability",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 145, "comparison": "max",
        "finding": "supplier recyclability exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_order_visibility_pct_24(record):
    """Evaluate supplier order visibility for control WP-0195-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0195-24", "metric": "supplier_order_visibility_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 4,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0195-24", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0195-24", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 4
    if not failed:
        return None
    return {
        "rule_id": "WP-0195-24", "metric": "supplier_order_visibility_pct", "label": "supplier order visibility",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 4, "comparison": "min",
        "finding": "supplier order visibility falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_congestion_score_01, assess_charger_queue_minutes_02, assess_invoice_age_days_03, assess_cache_hit_pct_04, assess_pack_size_variance_05, assess_handover_ack_pct_06, assess_environmental_incident_count_07, assess_dual_control_compliance_pct_08, assess_chemical_inventory_reconcile_pct_09, assess_spare_part_stockout_count_10, assess_recovery_point_minutes_11, assess_record_completeness_pct_12, assess_customer_master_gap_count_13, assess_supplier_backup_days_14, assess_last_mile_handoff_age_hours_15, assess_freight_audit_savings_pct_16, assess_temperature_record_gap_count_17, assess_supplier_scorecard_age_days_18, assess_supplier_recycled_content_pct_19, assess_supplier_shipment_consolidation_pct_20, assess_supplier_compliance_attestation_age_days_21, assess_supplier_revenue_dependency_pct_22, assess_supplier_recyclability_score_23, assess_supplier_order_visibility_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

