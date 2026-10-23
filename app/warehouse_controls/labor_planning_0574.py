"""Operational control pack for labor planning; rules are executable against warehouse records."""
from math import isfinite

def assess_congestion_score_01(record):
    """Evaluate congestion score for control WP-0574-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("congestion_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-01", "metric": "congestion_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-01", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-01", "metric": "congestion_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-01", "metric": "congestion_score", "label": "congestion score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "congestion score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_charger_queue_minutes_02(record):
    """Evaluate charger queue for control WP-0574-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("charger_queue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-02", "metric": "charger_queue_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-02", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-02", "metric": "charger_queue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-02", "metric": "charger_queue_minutes", "label": "charger queue",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "charger queue exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_invoice_age_days_03(record):
    """Evaluate invoice age for control WP-0574-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("invoice_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-03", "metric": "invoice_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-03", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-03", "metric": "invoice_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-03", "metric": "invoice_age_days", "label": "invoice age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "invoice age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_cache_hit_pct_04(record):
    """Evaluate cache hit rate for control WP-0574-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cache_hit_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-04", "metric": "cache_hit_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-04", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-04", "metric": "cache_hit_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-04", "metric": "cache_hit_pct", "label": "cache hit rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cache hit rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_pack_size_variance_05(record):
    """Evaluate pack-size variance for control WP-0574-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_size_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-05", "metric": "pack_size_variance",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-05", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-05", "metric": "pack_size_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-05", "metric": "pack_size_variance", "label": "pack-size variance",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pack-size variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_handover_ack_pct_06(record):
    """Evaluate handover acknowledgement for control WP-0574-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-06", "metric": "handover_ack_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-06", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-06", "metric": "handover_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-06", "metric": "handover_ack_pct", "label": "handover acknowledgement",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "handover acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_environmental_incident_count_07(record):
    """Evaluate environmental incidents for control WP-0574-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("environmental_incident_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-07", "metric": "environmental_incident_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-07", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-07", "metric": "environmental_incident_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-07", "metric": "environmental_incident_count", "label": "environmental incidents",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "environmental incidents falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_dual_control_compliance_pct_08(record):
    """Evaluate dual control compliance for control WP-0574-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dual_control_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-08", "metric": "dual_control_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-08", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-08", "metric": "dual_control_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-08", "metric": "dual_control_compliance_pct", "label": "dual control compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "dual control compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_chemical_inventory_reconcile_pct_09(record):
    """Evaluate chemical inventory reconciliation for control WP-0574-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chemical_inventory_reconcile_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-09", "metric": "chemical_inventory_reconcile_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-09", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-09", "metric": "chemical_inventory_reconcile_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-09", "metric": "chemical_inventory_reconcile_pct", "label": "chemical inventory reconciliation",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "chemical inventory reconciliation must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_spare_part_stockout_count_10(record):
    """Evaluate spare part stockouts for control WP-0574-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("spare_part_stockout_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-10", "metric": "spare_part_stockout_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-10", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-10", "metric": "spare_part_stockout_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-10", "metric": "spare_part_stockout_count", "label": "spare part stockouts",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "spare part stockouts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_recovery_point_minutes_11(record):
    """Evaluate recovery point for control WP-0574-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_point_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-11", "metric": "recovery_point_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-11", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-11", "metric": "recovery_point_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-11", "metric": "recovery_point_minutes", "label": "recovery point",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "recovery point falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_record_completeness_pct_12(record):
    """Evaluate record completeness for control WP-0574-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("record_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-12", "metric": "record_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-12", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-12", "metric": "record_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-12", "metric": "record_completeness_pct", "label": "record completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "record completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_customer_master_gap_count_13(record):
    """Evaluate customer master gaps for control WP-0574-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_master_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-13", "metric": "customer_master_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-13", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-13", "metric": "customer_master_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-13", "metric": "customer_master_gap_count", "label": "customer master gaps",
        "status": "breach", "severity": "high", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer master gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_backup_days_14(record):
    """Evaluate backup supplier lead time for control WP-0574-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_backup_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-14", "metric": "supplier_backup_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-14", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-14", "metric": "supplier_backup_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-14", "metric": "supplier_backup_days", "label": "backup supplier lead time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "backup supplier lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_last_mile_handoff_age_hours_15(record):
    """Evaluate last-mile handoff age for control WP-0574-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("last_mile_handoff_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-15", "metric": "last_mile_handoff_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-15", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-15", "metric": "last_mile_handoff_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-15", "metric": "last_mile_handoff_age_hours", "label": "last-mile handoff age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "last-mile handoff age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_freight_audit_savings_pct_16(record):
    """Evaluate freight audit savings for control WP-0574-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("freight_audit_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-16", "metric": "freight_audit_savings_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-16", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-16", "metric": "freight_audit_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-16", "metric": "freight_audit_savings_pct", "label": "freight audit savings",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "freight audit savings must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_temperature_record_gap_count_17(record):
    """Evaluate temperature record gaps for control WP-0574-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("temperature_record_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-17", "metric": "temperature_record_gap_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-17", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-17", "metric": "temperature_record_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-17", "metric": "temperature_record_gap_count", "label": "temperature record gaps",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "temperature record gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_scorecard_age_days_18(record):
    """Evaluate supplier scorecard age for control WP-0574-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scorecard_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-18", "metric": "supplier_scorecard_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-18", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-18", "metric": "supplier_scorecard_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-18", "metric": "supplier_scorecard_age_days", "label": "supplier scorecard age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "supplier scorecard age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_recycled_content_pct_19(record):
    """Evaluate supplier recycled content for control WP-0574-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recycled_content_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-19", "metric": "supplier_recycled_content_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-19", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-19", "metric": "supplier_recycled_content_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-19", "metric": "supplier_recycled_content_pct", "label": "supplier recycled content",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 37, "comparison": "min",
        "finding": "supplier recycled content falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_shipment_consolidation_pct_20(record):
    """Evaluate supplier shipment consolidation for control WP-0574-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipment_consolidation_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-20", "metric": "supplier_shipment_consolidation_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-20", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-20", "metric": "supplier_shipment_consolidation_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-20", "metric": "supplier_shipment_consolidation_pct", "label": "supplier shipment consolidation",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier shipment consolidation must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
    }

def assess_supplier_compliance_attestation_age_days_21(record):
    """Evaluate supplier compliance attestation age for control WP-0574-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_compliance_attestation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-21", "metric": "supplier_compliance_attestation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-21", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-21", "metric": "supplier_compliance_attestation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-21", "metric": "supplier_compliance_attestation_age_days", "label": "supplier compliance attestation age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier compliance attestation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "labor planning",
    }

def assess_supplier_revenue_dependency_pct_22(record):
    """Evaluate supplier revenue dependency for control WP-0574-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_revenue_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-22", "metric": "supplier_revenue_dependency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-22", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-22", "metric": "supplier_revenue_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-22", "metric": "supplier_revenue_dependency_pct", "label": "supplier revenue dependency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "supplier revenue dependency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "labor planning",
    }

def assess_supplier_recyclability_score_23(record):
    """Evaluate supplier recyclability for control WP-0574-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_recyclability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-23", "metric": "supplier_recyclability_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-23", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-23", "metric": "supplier_recyclability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-23", "metric": "supplier_recyclability_score", "label": "supplier recyclability",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "supplier recyclability falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "labor planning",
    }

def assess_supplier_order_visibility_pct_24(record):
    """Evaluate supplier order visibility for control WP-0574-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_order_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0574-24", "metric": "supplier_order_visibility_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0574-24", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0574-24", "metric": "supplier_order_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0574-24", "metric": "supplier_order_visibility_pct", "label": "supplier order visibility",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier order visibility must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "labor planning",
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

