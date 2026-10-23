"""Operational control pack for shipment service; rules are executable against warehouse records."""
from math import isfinite

def assess_public_address_test_age_days_01(record):
    """Evaluate public-address test age for control WP-0084-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("public_address_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-01", "metric": "public_address_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-01", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-01", "metric": "public_address_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-01", "metric": "public_address_test_age_days", "label": "public-address test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "public-address test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_license_compliance_pct_02(record):
    """Evaluate license compliance for control WP-0084-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("license_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-02", "metric": "license_compliance_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-02", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-02", "metric": "license_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-02", "metric": "license_compliance_pct", "label": "license compliance",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "license compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_rfid_collision_count_03(record):
    """Evaluate RFID collisions for control WP-0084-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_collision_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-03", "metric": "rfid_collision_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-03", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-03", "metric": "rfid_collision_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-03", "metric": "rfid_collision_count", "label": "RFID collisions",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "RFID collisions must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_stock_age_p95_days_04(record):
    """Evaluate 95th percentile stock age for control WP-0084-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_p95_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-04", "metric": "stock_age_p95_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-04", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-04", "metric": "stock_age_p95_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-04", "metric": "stock_age_p95_days", "label": "95th percentile stock age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "95th percentile stock age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_cartonization_savings_pct_05(record):
    """Evaluate cartonization savings for control WP-0084-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cartonization_savings_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-05", "metric": "cartonization_savings_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 63,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-05", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-05", "metric": "cartonization_savings_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 63
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-05", "metric": "cartonization_savings_pct", "label": "cartonization savings",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 63, "comparison": "min",
        "finding": "cartonization savings falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_restricted_party_match_count_06(record):
    """Evaluate restricted-party matches for control WP-0084-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_party_match_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-06", "metric": "restricted_party_match_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-06", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-06", "metric": "restricted_party_match_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-06", "metric": "restricted_party_match_count", "label": "restricted-party matches",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "restricted-party matches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_driver_license_days_left_07(record):
    """Evaluate driver license validity for control WP-0084-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-07", "metric": "driver_license_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-07", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-07", "metric": "driver_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-07", "metric": "driver_license_days_left", "label": "driver license validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "driver license validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_capital_budget_variance_pct_08(record):
    """Evaluate capital budget variance for control WP-0084-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("capital_budget_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-08", "metric": "capital_budget_variance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-08", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-08", "metric": "capital_budget_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-08", "metric": "capital_budget_variance_pct", "label": "capital budget variance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "capital budget variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_bcp_test_age_days_09(record):
    """Evaluate supplier continuity test age for control WP-0084-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bcp_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-09", "metric": "supplier_bcp_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 12,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-09", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-09", "metric": "supplier_bcp_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 12
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-09", "metric": "supplier_bcp_test_age_days", "label": "supplier continuity test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 12, "comparison": "min",
        "finding": "supplier continuity test age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_capability_index_10(record):
    """Evaluate supplier capability index for control WP-0084-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capability_index")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-10", "metric": "supplier_capability_index",
            "status": "insufficient_data",
            "severity": "medium", "unit": "index",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-10", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-10", "metric": "supplier_capability_index", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-10", "metric": "supplier_capability_index", "label": "supplier capability index",
        "status": "breach", "severity": "medium", "unit": "index",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capability index must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_currency_exposure_pct_11(record):
    """Evaluate supplier currency exposure for control WP-0084-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_currency_exposure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-11", "metric": "supplier_currency_exposure_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-11", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-11", "metric": "supplier_currency_exposure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-11", "metric": "supplier_currency_exposure_pct", "label": "supplier currency exposure",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier currency exposure must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_runbook_age_days_12(record):
    """Evaluate supplier runbook age for control WP-0084-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-12", "metric": "supplier_runbook_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-12", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-12", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-12", "metric": "supplier_runbook_age_days", "label": "supplier runbook age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier runbook age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_country_label_pct_13(record):
    """Evaluate supplier country-label compliance for control WP-0084-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-13", "metric": "supplier_country_label_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 56,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-13", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-13", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 56
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-13", "metric": "supplier_country_label_pct", "label": "supplier country-label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 56, "comparison": "min",
        "finding": "supplier country-label compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_driver_briefing_pct_14(record):
    """Evaluate supplier driver briefing completion for control WP-0084-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_driver_briefing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-14", "metric": "supplier_driver_briefing_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-14", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-14", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-14", "metric": "supplier_driver_briefing_pct", "label": "supplier driver briefing completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier driver briefing completion must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_process_change_approval_pct_15(record):
    """Evaluate supplier process-change approval for control WP-0084-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-15", "metric": "supplier_process_change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-15", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-15", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-15", "metric": "supplier_process_change_approval_pct", "label": "supplier process-change approval",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier process-change approval must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_waste_transport_license_days_16(record):
    """Evaluate supplier waste transport license validity for control WP-0084-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waste_transport_license_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-16", "metric": "supplier_waste_transport_license_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 107,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-16", "metric": "supplier_waste_transport_license_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-16", "metric": "supplier_waste_transport_license_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 107
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-16", "metric": "supplier_waste_transport_license_days", "label": "supplier waste transport license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 107, "comparison": "max",
        "finding": "supplier waste transport license validity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_duplicate_payment_count_17(record):
    """Evaluate supplier duplicate payments for control WP-0084-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_payment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-17", "metric": "supplier_duplicate_payment_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 5,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-17", "metric": "supplier_duplicate_payment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-17", "metric": "supplier_duplicate_payment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 5
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-17", "metric": "supplier_duplicate_payment_count", "label": "supplier duplicate payments",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 5, "comparison": "min",
        "finding": "supplier duplicate payments falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_critical_staff_backup_pct_18(record):
    """Evaluate supplier critical staff backup for control WP-0084-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_staff_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-18", "metric": "supplier_critical_staff_backup_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-18", "metric": "supplier_critical_staff_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-18", "metric": "supplier_critical_staff_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-18", "metric": "supplier_critical_staff_backup_pct", "label": "supplier critical staff backup",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier critical staff backup must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_prediction_latency_ms_19(record):
    """Evaluate supplier prediction latency for control WP-0084-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prediction_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-19", "metric": "supplier_prediction_latency_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-19", "metric": "supplier_prediction_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-19", "metric": "supplier_prediction_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-19", "metric": "supplier_prediction_latency_ms", "label": "supplier prediction latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier prediction latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_data_contract_violation_count_20(record):
    """Evaluate supplier data-contract violations for control WP-0084-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_contract_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-20", "metric": "supplier_data_contract_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 127,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-20", "metric": "supplier_data_contract_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-20", "metric": "supplier_data_contract_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 127
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-20", "metric": "supplier_data_contract_violation_count", "label": "supplier data-contract violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 127, "comparison": "max",
        "finding": "supplier data-contract violations exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

def assess_supplier_service_account_review_age_days_21(record):
    """Evaluate supplier service-account review age for control WP-0084-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_account_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-21", "metric": "supplier_service_account_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-21", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-21", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-21", "metric": "supplier_service_account_review_age_days", "label": "supplier service-account review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "min",
        "finding": "supplier service-account review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "shipment service",
    }

def assess_supplier_privacy_training_pct_22(record):
    """Evaluate supplier privacy training for control WP-0084-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-22", "metric": "supplier_privacy_training_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-22", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-22", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-22", "metric": "supplier_privacy_training_pct", "label": "supplier privacy training",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier privacy training must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "shipment service",
    }

def assess_supplier_evidence_integrity_pct_23(record):
    """Evaluate supplier evidence integrity for control WP-0084-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-23", "metric": "supplier_evidence_integrity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-23", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-23", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-23", "metric": "supplier_evidence_integrity_pct", "label": "supplier evidence integrity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier evidence integrity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "shipment service",
    }

def assess_supplier_volume_commitment_pct_24(record):
    """Evaluate supplier volume commitment for control WP-0084-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_volume_commitment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0084-24", "metric": "supplier_volume_commitment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 147,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0084-24", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0084-24", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 147
    if not failed:
        return None
    return {
        "rule_id": "WP-0084-24", "metric": "supplier_volume_commitment_pct", "label": "supplier volume commitment",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 147, "comparison": "max",
        "finding": "supplier volume commitment exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "shipment service",
    }

RULES = (assess_public_address_test_age_days_01, assess_license_compliance_pct_02, assess_rfid_collision_count_03, assess_stock_age_p95_days_04, assess_cartonization_savings_pct_05, assess_restricted_party_match_count_06, assess_driver_license_days_left_07, assess_capital_budget_variance_pct_08, assess_supplier_bcp_test_age_days_09, assess_supplier_capability_index_10, assess_supplier_currency_exposure_pct_11, assess_supplier_runbook_age_days_12, assess_supplier_country_label_pct_13, assess_supplier_driver_briefing_pct_14, assess_supplier_process_change_approval_pct_15, assess_supplier_waste_transport_license_days_16, assess_supplier_duplicate_payment_count_17, assess_supplier_critical_staff_backup_pct_18, assess_supplier_prediction_latency_ms_19, assess_supplier_data_contract_violation_count_20, assess_supplier_service_account_review_age_days_21, assess_supplier_privacy_training_pct_22, assess_supplier_evidence_integrity_pct_23, assess_supplier_volume_commitment_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

