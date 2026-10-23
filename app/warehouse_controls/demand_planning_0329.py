"""Operational control pack for demand planning; rules are executable against warehouse records."""
from math import isfinite

def assess_break_overdue_minutes_01(record):
    """Evaluate break overdue for control WP-0329-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("break_overdue_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-01", "metric": "break_overdue_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-01", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-01", "metric": "break_overdue_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-01", "metric": "break_overdue_minutes", "label": "break overdue",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "break overdue exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_donation_age_days_02(record):
    """Evaluate donation processing age for control WP-0329-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("donation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-02", "metric": "donation_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-02", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-02", "metric": "donation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-02", "metric": "donation_age_days", "label": "donation processing age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "donation processing age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_high_value_variance_03(record):
    """Evaluate high-value inventory variance for control WP-0329-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-03", "metric": "high_value_variance",
            "status": "insufficient_data",
            "severity": "critical", "unit": "currency",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-03", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-03", "metric": "high_value_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-03", "metric": "high_value_variance", "label": "high-value inventory variance",
        "status": "breach", "severity": "critical", "unit": "currency",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "high-value inventory variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_incompatible_storage_count_04(record):
    """Evaluate incompatible storage pairs for control WP-0329-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incompatible_storage_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-04", "metric": "incompatible_storage_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "pairs",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-04", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-04", "metric": "incompatible_storage_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-04", "metric": "incompatible_storage_count", "label": "incompatible storage pairs",
        "status": "breach", "severity": "low", "unit": "pairs",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "incompatible storage pairs must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_license_validity_days_05(record):
    """Evaluate license validity for control WP-0329-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-05", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-05", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-05", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-05", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_business_continuity_test_age_days_06(record):
    """Evaluate business continuity test age for control WP-0329-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("business_continuity_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-06", "metric": "business_continuity_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 79,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-06", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-06", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 79
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-06", "metric": "business_continuity_test_age_days", "label": "business continuity test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 79, "comparison": "min",
        "finding": "business continuity test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_etl_lag_minutes_07(record):
    """Evaluate ETL lag for control WP-0329-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("etl_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-07", "metric": "etl_lag_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-07", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-07", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-07", "metric": "etl_lag_minutes", "label": "ETL lag",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ETL lag must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_uom_conversion_gap_count_08(record):
    """Evaluate unit conversion gaps for control WP-0329-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("uom_conversion_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-08", "metric": "uom_conversion_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-08", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-08", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-08", "metric": "uom_conversion_gap_count", "label": "unit conversion gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "unit conversion gaps must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_obsolete_sku_count_09(record):
    """Evaluate obsolete SKUs for control WP-0329-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-09", "metric": "obsolete_sku_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "SKUs",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-09", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-09", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-09", "metric": "obsolete_sku_count", "label": "obsolete SKUs",
        "status": "breach", "severity": "medium", "unit": "SKUs",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "obsolete SKUs exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_carrier_rate_variance_pct_10(record):
    """Evaluate carrier rate variance for control WP-0329-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-10", "metric": "carrier_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 28,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-10", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-10", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 28
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-10", "metric": "carrier_rate_variance_pct", "label": "carrier rate variance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 28, "comparison": "min",
        "finding": "carrier rate variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_insurance_claim_count_11(record):
    """Evaluate insurance claims for control WP-0329-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-11", "metric": "insurance_claim_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-11", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-11", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-11", "metric": "insurance_claim_count", "label": "insurance claims",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "insurance claims must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_roadside_assistance_age_days_12(record):
    """Evaluate roadside assistance review age for control WP-0329-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("roadside_assistance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-12", "metric": "roadside_assistance_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-12", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-12", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-12", "metric": "roadside_assistance_age_days", "label": "roadside assistance review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "roadside assistance review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_purchase_requisition_age_hours_13(record):
    """Evaluate purchase requisition age for control WP-0329-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_requisition_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-13", "metric": "purchase_requisition_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 37,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-13", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-13", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 37
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-13", "metric": "purchase_requisition_age_hours", "label": "purchase requisition age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 37, "comparison": "max",
        "finding": "purchase requisition age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_single_site_pct_14(record):
    """Evaluate supplier single-site dependency for control WP-0329-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_single_site_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-14", "metric": "supplier_single_site_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 72,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-14", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-14", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 72
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-14", "metric": "supplier_single_site_pct", "label": "supplier single-site dependency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 72, "comparison": "min",
        "finding": "supplier single-site dependency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_measurement_system_score_15(record):
    """Evaluate supplier measurement system score for control WP-0329-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_system_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-15", "metric": "supplier_measurement_system_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-15", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-15", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-15", "metric": "supplier_measurement_system_score", "label": "supplier measurement system score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier measurement system score must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_origin_document_pct_16(record):
    """Evaluate supplier origin-document completeness for control WP-0329-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_origin_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-16", "metric": "supplier_origin_document_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-16", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-16", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-16", "metric": "supplier_origin_document_pct", "label": "supplier origin-document completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier origin-document completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_transition_readiness_pct_17(record):
    """Evaluate supplier transition readiness for control WP-0329-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-17", "metric": "supplier_transition_readiness_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-17", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-17", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-17", "metric": "supplier_transition_readiness_pct", "label": "supplier transition readiness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "max",
        "finding": "supplier transition readiness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_serial_warranty_match_pct_18(record):
    """Evaluate supplier serial/warranty match for control WP-0329-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_warranty_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-18", "metric": "supplier_serial_warranty_match_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 21,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-18", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-18", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 21
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-18", "metric": "supplier_serial_warranty_match_pct", "label": "supplier serial/warranty match",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 21, "comparison": "min",
        "finding": "supplier serial/warranty match falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_claim_settlement_days_19(record):
    """Evaluate supplier claim settlement time for control WP-0329-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_settlement_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-19", "metric": "supplier_claim_settlement_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-19", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-19", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-19", "metric": "supplier_claim_settlement_days", "label": "supplier claim settlement time",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier claim settlement time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_ppap_approval_pct_20(record):
    """Evaluate supplier PPAP approval for control WP-0329-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppap_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-20", "metric": "supplier_ppap_approval_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-20", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-20", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-20", "metric": "supplier_ppap_approval_pct", "label": "supplier PPAP approval",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier PPAP approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

def assess_supplier_spill_response_drill_age_days_21(record):
    """Evaluate supplier spill drill age for control WP-0329-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spill_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-21", "metric": "supplier_spill_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-21", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-21", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-21", "metric": "supplier_spill_response_drill_age_days", "label": "supplier spill drill age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier spill drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "demand planning",
    }

def assess_supplier_ar_days_22(record):
    """Evaluate supplier accounts-receivable days for control WP-0329-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ar_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-22", "metric": "supplier_ar_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-22", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-22", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-22", "metric": "supplier_ar_days", "label": "supplier accounts-receivable days",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 65, "comparison": "min",
        "finding": "supplier accounts-receivable days falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "demand planning",
    }

def assess_supplier_training_refresh_days_23(record):
    """Evaluate supplier training refresh interval for control WP-0329-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_refresh_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-23", "metric": "supplier_training_refresh_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-23", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-23", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-23", "metric": "supplier_training_refresh_days", "label": "supplier training refresh interval",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier training refresh interval must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "demand planning",
    }

def assess_supplier_human_override_pct_24(record):
    """Evaluate supplier human override rate for control WP-0329-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_override_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0329-24", "metric": "supplier_human_override_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0329-24", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0329-24", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0329-24", "metric": "supplier_human_override_pct", "label": "supplier human override rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier human override rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "demand planning",
    }

RULES = (assess_break_overdue_minutes_01, assess_donation_age_days_02, assess_high_value_variance_03, assess_incompatible_storage_count_04, assess_license_validity_days_05, assess_business_continuity_test_age_days_06, assess_etl_lag_minutes_07, assess_uom_conversion_gap_count_08, assess_obsolete_sku_count_09, assess_carrier_rate_variance_pct_10, assess_insurance_claim_count_11, assess_roadside_assistance_age_days_12, assess_purchase_requisition_age_hours_13, assess_supplier_single_site_pct_14, assess_supplier_measurement_system_score_15, assess_supplier_origin_document_pct_16, assess_supplier_transition_readiness_pct_17, assess_supplier_serial_warranty_match_pct_18, assess_supplier_claim_settlement_days_19, assess_supplier_ppap_approval_pct_20, assess_supplier_spill_response_drill_age_days_21, assess_supplier_ar_days_22, assess_supplier_training_refresh_days_23, assess_supplier_human_override_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

