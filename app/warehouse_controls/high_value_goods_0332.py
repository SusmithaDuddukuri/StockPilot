"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_chain_temperature_coverage_pct_01(record):
    """Evaluate temperature coverage for control WP-0332-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("chain_temperature_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-01", "metric": "chain_temperature_coverage_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-01", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-01", "metric": "chain_temperature_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-01", "metric": "chain_temperature_coverage_pct", "label": "temperature coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "temperature coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_replacement_stock_cover_days_02(record):
    """Evaluate replacement stock cover for control WP-0332-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("replacement_stock_cover_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-02", "metric": "replacement_stock_cover_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-02", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-02", "metric": "replacement_stock_cover_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-02", "metric": "replacement_stock_cover_days", "label": "replacement stock cover",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "replacement stock cover must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_fall_protection_compliance_pct_03(record):
    """Evaluate fall protection compliance for control WP-0332-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fall_protection_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-03", "metric": "fall_protection_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-03", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-03", "metric": "fall_protection_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-03", "metric": "fall_protection_compliance_pct", "label": "fall protection compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "fall protection compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_control_room_access_gap_count_04(record):
    """Evaluate control-room access gaps for control WP-0332-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("control_room_access_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-04", "metric": "control_room_access_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-04", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-04", "metric": "control_room_access_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-04", "metric": "control_room_access_gap_count", "label": "control-room access gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 31, "comparison": "max",
        "finding": "control-room access gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_dns_failure_count_05(record):
    """Evaluate DNS failures for control WP-0332-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dns_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-05", "metric": "dns_failure_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-05", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-05", "metric": "dns_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-05", "metric": "dns_failure_count", "label": "DNS failures",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "DNS failures falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_calibration_due_count_06(record):
    """Evaluate calibration due for control WP-0332-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("calibration_due_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-06", "metric": "calibration_due_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-06", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-06", "metric": "calibration_due_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-06", "metric": "calibration_due_count", "label": "calibration due",
        "status": "breach", "severity": "medium", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "calibration due must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_inventory_snapshot_age_minutes_07(record):
    """Evaluate inventory snapshot age for control WP-0332-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_snapshot_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-07", "metric": "inventory_snapshot_age_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-07", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-07", "metric": "inventory_snapshot_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-07", "metric": "inventory_snapshot_age_minutes", "label": "inventory snapshot age",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory snapshot age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_slotting_recommendation_accept_pct_08(record):
    """Evaluate slotting acceptance for control WP-0332-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_recommendation_accept_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-08", "metric": "slotting_recommendation_accept_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-08", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-08", "metric": "slotting_recommendation_accept_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-08", "metric": "slotting_recommendation_accept_pct", "label": "slotting acceptance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "slotting acceptance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_tax_document_completeness_pct_09(record):
    """Evaluate tax document completeness for control WP-0332-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tax_document_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-09", "metric": "tax_document_completeness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-09", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-09", "metric": "tax_document_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-09", "metric": "tax_document_completeness_pct", "label": "tax document completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "tax document completeness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_driver_checkin_compliance_pct_10(record):
    """Evaluate driver check-in compliance for control WP-0332-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_checkin_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-10", "metric": "driver_checkin_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-10", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-10", "metric": "driver_checkin_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-10", "metric": "driver_checkin_compliance_pct", "label": "driver check-in compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "driver check-in compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_labor_productivity_index_11(record):
    """Evaluate labor productivity for control WP-0332-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_productivity_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-11", "metric": "labor_productivity_index",
            "status": "insufficient_data",
            "severity": "high", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-11", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-11", "metric": "labor_productivity_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-11", "metric": "labor_productivity_index", "label": "labor productivity",
        "status": "breach", "severity": "high", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor productivity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_label_compliance_pct_12(record):
    """Evaluate supplier label compliance for control WP-0332-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_label_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-12", "metric": "supplier_label_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-12", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-12", "metric": "supplier_label_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-12", "metric": "supplier_label_compliance_pct", "label": "supplier label compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "supplier label compliance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_obsolescence_notice_days_13(record):
    """Evaluate supplier obsolescence notice for control WP-0332-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_obsolescence_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-13", "metric": "supplier_obsolescence_notice_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-13", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-13", "metric": "supplier_obsolescence_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-13", "metric": "supplier_obsolescence_notice_days", "label": "supplier obsolescence notice",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier obsolescence notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_delivery_slot_compliance_pct_14(record):
    """Evaluate supplier delivery-slot compliance for control WP-0332-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_slot_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-14", "metric": "supplier_delivery_slot_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-14", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-14", "metric": "supplier_delivery_slot_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-14", "metric": "supplier_delivery_slot_compliance_pct", "label": "supplier delivery-slot compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier delivery-slot compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_support_ack_minutes_15(record):
    """Evaluate supplier support acknowledgement for control WP-0332-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-15", "metric": "supplier_support_ack_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-15", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-15", "metric": "supplier_support_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-15", "metric": "supplier_support_ack_minutes", "label": "supplier support acknowledgement",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier support acknowledgement must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_serial_data_completeness_pct_16(record):
    """Evaluate supplier serial-data completeness for control WP-0332-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_data_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-16", "metric": "supplier_serial_data_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-16", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-16", "metric": "supplier_serial_data_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-16", "metric": "supplier_serial_data_completeness_pct", "label": "supplier serial-data completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier serial-data completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_personnel_screening_pct_17(record):
    """Evaluate supplier personnel screening for control WP-0332-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_personnel_screening_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-17", "metric": "supplier_personnel_screening_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 31,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-17", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-17", "metric": "supplier_personnel_screening_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 31
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-17", "metric": "supplier_personnel_screening_pct", "label": "supplier personnel screening",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 31, "comparison": "min",
        "finding": "supplier personnel screening falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_knowledge_transfer_pct_18(record):
    """Evaluate supplier knowledge transfer for control WP-0332-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_knowledge_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-18", "metric": "supplier_knowledge_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-18", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-18", "metric": "supplier_knowledge_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-18", "metric": "supplier_knowledge_transfer_pct", "label": "supplier knowledge transfer",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier knowledge transfer must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_product_compliance_pct_19(record):
    """Evaluate supplier product compliance for control WP-0332-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_product_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-19", "metric": "supplier_product_compliance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-19", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-19", "metric": "supplier_product_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-19", "metric": "supplier_product_compliance_pct", "label": "supplier product compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier product compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_beneficial_owner_gap_count_20(record):
    """Evaluate supplier beneficial-owner gaps for control WP-0332-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_beneficial_owner_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-20", "metric": "supplier_beneficial_owner_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-20", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-20", "metric": "supplier_beneficial_owner_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-20", "metric": "supplier_beneficial_owner_gap_count", "label": "supplier beneficial-owner gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier beneficial-owner gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_substitute_material_pct_21(record):
    """Evaluate supplier substitute material coverage for control WP-0332-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_substitute_material_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-21", "metric": "supplier_substitute_material_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 75,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-21", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-21", "metric": "supplier_substitute_material_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 75
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-21", "metric": "supplier_substitute_material_pct", "label": "supplier substitute material coverage",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 75, "comparison": "min",
        "finding": "supplier substitute material coverage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_iot_coverage_pct_22(record):
    """Evaluate supplier IoT coverage for control WP-0332-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_iot_coverage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-22", "metric": "supplier_iot_coverage_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-22", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-22", "metric": "supplier_iot_coverage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-22", "metric": "supplier_iot_coverage_pct", "label": "supplier IoT coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier IoT coverage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_experiment_guardrail_breach_count_23(record):
    """Evaluate supplier experiment guardrail breaches for control WP-0332-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_experiment_guardrail_breach_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-23", "metric": "supplier_experiment_guardrail_breach_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-23", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-23", "metric": "supplier_experiment_guardrail_breach_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-23", "metric": "supplier_experiment_guardrail_breach_count", "label": "supplier experiment guardrail breaches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier experiment guardrail breaches must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_data_residency_gap_count_24(record):
    """Evaluate supplier data-residency gaps for control WP-0332-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_residency_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0332-24", "metric": "supplier_data_residency_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0332-24", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0332-24", "metric": "supplier_data_residency_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0332-24", "metric": "supplier_data_residency_gap_count", "label": "supplier data-residency gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier data-residency gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_chain_temperature_coverage_pct_01, assess_replacement_stock_cover_days_02, assess_fall_protection_compliance_pct_03, assess_control_room_access_gap_count_04, assess_dns_failure_count_05, assess_calibration_due_count_06, assess_inventory_snapshot_age_minutes_07, assess_slotting_recommendation_accept_pct_08, assess_tax_document_completeness_pct_09, assess_driver_checkin_compliance_pct_10, assess_labor_productivity_index_11, assess_supplier_label_compliance_pct_12, assess_supplier_obsolescence_notice_days_13, assess_supplier_delivery_slot_compliance_pct_14, assess_supplier_support_ack_minutes_15, assess_supplier_serial_data_completeness_pct_16, assess_supplier_personnel_screening_pct_17, assess_supplier_knowledge_transfer_pct_18, assess_supplier_product_compliance_pct_19, assess_supplier_beneficial_owner_gap_count_20, assess_supplier_substitute_material_pct_21, assess_supplier_iot_coverage_pct_22, assess_supplier_experiment_guardrail_breach_count_23, assess_supplier_data_residency_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

