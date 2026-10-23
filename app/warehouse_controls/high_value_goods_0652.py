"""Operational control pack for high-value goods; rules are executable against warehouse records."""
from math import isfinite

def assess_license_validity_days_01(record):
    """Evaluate license validity for control WP-0652-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_validity_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-01", "metric": "license_validity_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-01", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-01", "metric": "license_validity_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-01", "metric": "license_validity_days", "label": "license validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "license validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_business_continuity_test_age_days_02(record):
    """Evaluate business continuity test age for control WP-0652-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("business_continuity_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-02", "metric": "business_continuity_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-02", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-02", "metric": "business_continuity_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-02", "metric": "business_continuity_test_age_days", "label": "business continuity test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "business continuity test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_etl_lag_minutes_03(record):
    """Evaluate ETL lag for control WP-0652-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("etl_lag_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-03", "metric": "etl_lag_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-03", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-03", "metric": "etl_lag_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-03", "metric": "etl_lag_minutes", "label": "ETL lag",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "ETL lag must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_uom_conversion_gap_count_04(record):
    """Evaluate unit conversion gaps for control WP-0652-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("uom_conversion_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-04", "metric": "uom_conversion_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "records",
            "observed": None,
            "threshold": 51,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-04", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-04", "metric": "uom_conversion_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 51
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-04", "metric": "uom_conversion_gap_count", "label": "unit conversion gaps",
        "status": "breach", "severity": "critical", "unit": "records",
        "observed": observed,
        "threshold": 51, "comparison": "max",
        "finding": "unit conversion gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_obsolete_sku_count_05(record):
    """Evaluate obsolete SKUs for control WP-0652-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("obsolete_sku_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-05", "metric": "obsolete_sku_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "SKUs",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-05", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-05", "metric": "obsolete_sku_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-05", "metric": "obsolete_sku_count", "label": "obsolete SKUs",
        "status": "breach", "severity": "low", "unit": "SKUs",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "obsolete SKUs falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_carrier_rate_variance_pct_06(record):
    """Evaluate carrier rate variance for control WP-0652-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_rate_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-06", "metric": "carrier_rate_variance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-06", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-06", "metric": "carrier_rate_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-06", "metric": "carrier_rate_variance_pct", "label": "carrier rate variance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier rate variance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_insurance_claim_count_07(record):
    """Evaluate insurance claims for control WP-0652-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("insurance_claim_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-07", "metric": "insurance_claim_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-07", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-07", "metric": "insurance_claim_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-07", "metric": "insurance_claim_count", "label": "insurance claims",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "insurance claims must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_roadside_assistance_age_days_08(record):
    """Evaluate roadside assistance review age for control WP-0652-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("roadside_assistance_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-08", "metric": "roadside_assistance_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-08", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-08", "metric": "roadside_assistance_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-08", "metric": "roadside_assistance_age_days", "label": "roadside assistance review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "max",
        "finding": "roadside assistance review age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_purchase_requisition_age_hours_09(record):
    """Evaluate purchase requisition age for control WP-0652-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("purchase_requisition_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-09", "metric": "purchase_requisition_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-09", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-09", "metric": "purchase_requisition_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-09", "metric": "purchase_requisition_age_hours", "label": "purchase requisition age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 93, "comparison": "min",
        "finding": "purchase requisition age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_single_site_pct_10(record):
    """Evaluate supplier single-site dependency for control WP-0652-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_single_site_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-10", "metric": "supplier_single_site_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-10", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-10", "metric": "supplier_single_site_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-10", "metric": "supplier_single_site_pct", "label": "supplier single-site dependency",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier single-site dependency must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_measurement_system_score_11(record):
    """Evaluate supplier measurement system score for control WP-0652-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_system_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-11", "metric": "supplier_measurement_system_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-11", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-11", "metric": "supplier_measurement_system_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-11", "metric": "supplier_measurement_system_score", "label": "supplier measurement system score",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier measurement system score must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_origin_document_pct_12(record):
    """Evaluate supplier origin-document completeness for control WP-0652-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_origin_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-12", "metric": "supplier_origin_document_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-12", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-12", "metric": "supplier_origin_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-12", "metric": "supplier_origin_document_pct", "label": "supplier origin-document completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "supplier origin-document completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_transition_readiness_pct_13(record):
    """Evaluate supplier transition readiness for control WP-0652-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_transition_readiness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-13", "metric": "supplier_transition_readiness_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 42,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-13", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-13", "metric": "supplier_transition_readiness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 42
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-13", "metric": "supplier_transition_readiness_pct", "label": "supplier transition readiness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 42, "comparison": "min",
        "finding": "supplier transition readiness falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_serial_warranty_match_pct_14(record):
    """Evaluate supplier serial/warranty match for control WP-0652-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_serial_warranty_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-14", "metric": "supplier_serial_warranty_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-14", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-14", "metric": "supplier_serial_warranty_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-14", "metric": "supplier_serial_warranty_match_pct", "label": "supplier serial/warranty match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier serial/warranty match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_claim_settlement_days_15(record):
    """Evaluate supplier claim settlement time for control WP-0652-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_claim_settlement_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-15", "metric": "supplier_claim_settlement_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-15", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-15", "metric": "supplier_claim_settlement_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-15", "metric": "supplier_claim_settlement_days", "label": "supplier claim settlement time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier claim settlement time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_ppap_approval_pct_16(record):
    """Evaluate supplier PPAP approval for control WP-0652-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ppap_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-16", "metric": "supplier_ppap_approval_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-16", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-16", "metric": "supplier_ppap_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-16", "metric": "supplier_ppap_approval_pct", "label": "supplier PPAP approval",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "supplier PPAP approval exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_spill_response_drill_age_days_17(record):
    """Evaluate supplier spill drill age for control WP-0652-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_spill_response_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-17", "metric": "supplier_spill_response_drill_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 86,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-17", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-17", "metric": "supplier_spill_response_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 86
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-17", "metric": "supplier_spill_response_drill_age_days", "label": "supplier spill drill age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 86, "comparison": "min",
        "finding": "supplier spill drill age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_ar_days_18(record):
    """Evaluate supplier accounts-receivable days for control WP-0652-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ar_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-18", "metric": "supplier_ar_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-18", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-18", "metric": "supplier_ar_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-18", "metric": "supplier_ar_days", "label": "supplier accounts-receivable days",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier accounts-receivable days must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_training_refresh_days_19(record):
    """Evaluate supplier training refresh interval for control WP-0652-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_training_refresh_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-19", "metric": "supplier_training_refresh_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-19", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-19", "metric": "supplier_training_refresh_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-19", "metric": "supplier_training_refresh_days", "label": "supplier training refresh interval",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier training refresh interval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_human_override_pct_20(record):
    """Evaluate supplier human override rate for control WP-0652-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_human_override_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-20", "metric": "supplier_human_override_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-20", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-20", "metric": "supplier_human_override_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-20", "metric": "supplier_human_override_pct", "label": "supplier human override rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "supplier human override rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

def assess_supplier_idempotency_violation_count_21(record):
    """Evaluate supplier idempotency violations for control WP-0652-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_idempotency_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-21", "metric": "supplier_idempotency_violation_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 35,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-21", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-21", "metric": "supplier_idempotency_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 35
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-21", "metric": "supplier_idempotency_violation_count", "label": "supplier idempotency violations",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 35, "comparison": "min",
        "finding": "supplier idempotency violations falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "high-value goods",
    }

def assess_supplier_threat_model_age_days_22(record):
    """Evaluate supplier threat-model age for control WP-0652-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_threat_model_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-22", "metric": "supplier_threat_model_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-22", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-22", "metric": "supplier_threat_model_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-22", "metric": "supplier_threat_model_age_days", "label": "supplier threat-model age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier threat-model age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "high-value goods",
    }

def assess_supplier_screen_lock_pct_23(record):
    """Evaluate supplier screen-lock compliance for control WP-0652-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_screen_lock_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-23", "metric": "supplier_screen_lock_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-23", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-23", "metric": "supplier_screen_lock_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-23", "metric": "supplier_screen_lock_pct", "label": "supplier screen-lock compliance",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier screen-lock compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "high-value goods",
    }

def assess_supplier_manual_override_count_24(record):
    """Evaluate supplier manual overrides for control WP-0652-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_manual_override_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0652-24", "metric": "supplier_manual_override_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0652-24", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0652-24", "metric": "supplier_manual_override_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0652-24", "metric": "supplier_manual_override_count", "label": "supplier manual overrides",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "supplier manual overrides exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "high-value goods",
    }

RULES = (assess_license_validity_days_01, assess_business_continuity_test_age_days_02, assess_etl_lag_minutes_03, assess_uom_conversion_gap_count_04, assess_obsolete_sku_count_05, assess_carrier_rate_variance_pct_06, assess_insurance_claim_count_07, assess_roadside_assistance_age_days_08, assess_purchase_requisition_age_hours_09, assess_supplier_single_site_pct_10, assess_supplier_measurement_system_score_11, assess_supplier_origin_document_pct_12, assess_supplier_transition_readiness_pct_13, assess_supplier_serial_warranty_match_pct_14, assess_supplier_claim_settlement_days_15, assess_supplier_ppap_approval_pct_16, assess_supplier_spill_response_drill_age_days_17, assess_supplier_ar_days_18, assess_supplier_training_refresh_days_19, assess_supplier_human_override_pct_20, assess_supplier_idempotency_violation_count_21, assess_supplier_threat_model_age_days_22, assess_supplier_screen_lock_pct_23, assess_supplier_manual_override_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

