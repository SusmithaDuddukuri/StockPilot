"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_replacement_stock_cover_days_01(record):
    """Evaluate replacement stock cover for control WP-0587-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-01", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-01", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-01", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-01", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replacement stock cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_fall_protection_compliance_pct_02(record):
    """Evaluate fall protection compliance for control WP-0587-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-02", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-02", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-02", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-02", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fall protection compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_control_room_access_gap_count_03(record):
    """Evaluate control-room access gaps for control WP-0587-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-03", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 101,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-03", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-03", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 101
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-03", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 101, "comparison": "max",
        "finding": "control-room access gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_dns_failure_count_04(record):
    """Evaluate DNS failures for control WP-0587-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-04", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 58,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-04", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-04", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 58
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-04", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 58, "comparison": "min",
        "finding": "DNS failures falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_calibration_due_count_05(record):
    """Evaluate calibration due for control WP-0587-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("calibration_due_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-05", "metric": "calibration_due_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-05", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-05", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-05", "metric": "calibration_due_count", "label": "calibration due",
        "status": "breach", "severity": "critical", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "calibration due must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_inventory_snapshot_age_minutes_06(record):
    """Evaluate inventory snapshot age for control WP-0587-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_snapshot_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-06", "metric": "inventory_snapshot_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-06", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-06", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-06", "metric": "inventory_snapshot_age_minutes", "label": "inventory snapshot age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory snapshot age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_slotting_recommendation_accept_pct_07(record):
    """Evaluate slotting acceptance for control WP-0587-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_recommendation_accept_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-07", "metric": "slotting_recommendation_accept_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 121,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-07", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-07", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 121
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-07", "metric": "slotting_recommendation_accept_pct", "label": "slotting acceptance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 121, "comparison": "max",
        "finding": "slotting acceptance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_tax_document_completeness_pct_08(record):
    """Evaluate tax document completeness for control WP-0587-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_document_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-08", "metric": "tax_document_completeness_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 7,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-08", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-08", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 7
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-08", "metric": "tax_document_completeness_pct", "label": "tax document completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 7, "comparison": "min",
        "finding": "tax document completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_driver_checkin_compliance_pct_09(record):
    """Evaluate driver check-in compliance for control WP-0587-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-09", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-09", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-09", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-09", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver check-in compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_labor_productivity_index_10(record):
    """Evaluate labor productivity for control WP-0587-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-10", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "low", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-10", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-10", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-10", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "low", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor productivity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_label_compliance_pct_11(record):
    """Evaluate supplier label compliance for control WP-0587-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-11", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 141,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-11", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-11", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 141
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-11", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 141, "comparison": "max",
        "finding": "supplier label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_obsolescence_notice_days_12(record):
    """Evaluate supplier obsolescence notice for control WP-0587-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-12", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-12", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-12", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-12", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 51, "comparison": "min",
        "finding": "supplier obsolescence notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_delivery_slot_compliance_pct_13(record):
    """Evaluate supplier delivery-slot compliance for control WP-0587-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-13", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-13", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-13", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-13", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier delivery-slot compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_support_ack_minutes_14(record):
    """Evaluate supplier support acknowledgement for control WP-0587-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-14", "metric": "supplier_support_ack_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-14", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-14", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-14", "metric": "supplier_support_ack_minutes", "label": "supplier support acknowledgement",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier support acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_serial_data_completeness_pct_15(record):
    """Evaluate supplier serial-data completeness for control WP-0587-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-15", "metric": "supplier_serial_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 161,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-15", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-15", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 161
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-15", "metric": "supplier_serial_data_completeness_pct", "label": "supplier serial-data completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 161, "comparison": "max",
        "finding": "supplier serial-data completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_personnel_screening_pct_16(record):
    """Evaluate supplier personnel screening for control WP-0587-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-16", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 95,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-16", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-16", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 95
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-16", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 95, "comparison": "min",
        "finding": "supplier personnel screening falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_knowledge_transfer_pct_17(record):
    """Evaluate supplier knowledge transfer for control WP-0587-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-17", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-17", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-17", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-17", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier knowledge transfer must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_product_compliance_pct_18(record):
    """Evaluate supplier product compliance for control WP-0587-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-18", "metric": "supplier_product_compliance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-18", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-18", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-18", "metric": "supplier_product_compliance_pct", "label": "supplier product compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier product compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_beneficial_owner_gap_count_19(record):
    """Evaluate supplier beneficial-owner gaps for control WP-0587-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_beneficial_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-19", "metric": "supplier_beneficial_owner_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 181,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-19", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-19", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 181
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-19", "metric": "supplier_beneficial_owner_gap_count", "label": "supplier beneficial-owner gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 181, "comparison": "max",
        "finding": "supplier beneficial-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_substitute_material_pct_20(record):
    """Evaluate supplier substitute material coverage for control WP-0587-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_material_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-20", "metric": "supplier_substitute_material_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 44,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-20", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-20", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 44
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-20", "metric": "supplier_substitute_material_pct", "label": "supplier substitute material coverage",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 44, "comparison": "min",
        "finding": "supplier substitute material coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_supplier_iot_coverage_pct_21(record):
    """Evaluate supplier IoT coverage for control WP-0587-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_iot_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-21", "metric": "supplier_iot_coverage_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-21", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-21", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-21", "metric": "supplier_iot_coverage_pct", "label": "supplier IoT coverage",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier IoT coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_experiment_guardrail_breach_count_22(record):
    """Evaluate supplier experiment guardrail breaches for control WP-0587-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_experiment_guardrail_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-22", "metric": "supplier_experiment_guardrail_breach_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-22", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-22", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-22", "metric": "supplier_experiment_guardrail_breach_count", "label": "supplier experiment guardrail breaches",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier experiment guardrail breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_data_residency_gap_count_23(record):
    """Evaluate supplier data-residency gaps for control WP-0587-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_residency_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-23", "metric": "supplier_data_residency_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-23", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-23", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-23", "metric": "supplier_data_residency_gap_count", "label": "supplier data-residency gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 21, "comparison": "max",
        "finding": "supplier data-residency gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_dpia_completion_pct_24(record):
    """Evaluate supplier DPIA completion for control WP-0587-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dpia_completion_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0587-24", "metric": "supplier_dpia_completion_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 88,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0587-24", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0587-24", "metric": "supplier_dpia_completion_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 88
    if not failed:
        return None
    return {
        "rule_id": "WP-0587-24", "metric": "supplier_dpia_completion_pct", "label": "supplier DPIA completion",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 88, "comparison": "min",
        "finding": "supplier DPIA completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_replacement_stock_cover_days_01, assess_fall_protection_compliance_pct_02, assess_control_room_access_gap_count_03, assess_dns_failure_count_04, assess_calibration_due_count_05, assess_inventory_snapshot_age_minutes_06, assess_slotting_recommendation_accept_pct_07, assess_tax_document_completeness_pct_08, assess_driver_checkin_compliance_pct_09, assess_labor_productivity_index_10, assess_supplier_label_compliance_pct_11, assess_supplier_obsolescence_notice_days_12, assess_supplier_delivery_slot_compliance_pct_13, assess_supplier_support_ack_minutes_14, assess_supplier_serial_data_completeness_pct_15, assess_supplier_personnel_screening_pct_16, assess_supplier_knowledge_transfer_pct_17, assess_supplier_product_compliance_pct_18, assess_supplier_beneficial_owner_gap_count_19, assess_supplier_substitute_material_pct_20, assess_supplier_iot_coverage_pct_21, assess_supplier_experiment_guardrail_breach_count_22, assess_supplier_data_residency_gap_count_23, assess_supplier_dpia_completion_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

