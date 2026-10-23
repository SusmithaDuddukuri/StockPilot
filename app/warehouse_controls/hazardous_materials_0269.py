"""Operational control pack for hazardous material handling; rules are executable against warehouse records."""
from math import isfinite

def assess_coa_document_pct_01(record):
    """Evaluate certificate of analysis completeness for control WP-0269-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("coa_document_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-01", "metric": "coa_document_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-01", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-01", "metric": "coa_document_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-01", "metric": "coa_document_pct", "label": "certificate of analysis completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "certificate of analysis completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_battery_swelling_signal_02(record):
    """Evaluate battery swelling signal for control WP-0269-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("battery_swelling_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-02", "metric": "battery_swelling_signal",
            "status": "insufficient_data",
            "severity": "high", "unit": "binary",
            "observed": None,
            "threshold": 90,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-02", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-02", "metric": "battery_swelling_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 90
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-02", "metric": "battery_swelling_signal", "label": "battery swelling signal",
        "status": "breach", "severity": "high", "unit": "binary",
        "observed": observed,
        "threshold": 90, "comparison": "min",
        "finding": "battery swelling signal falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_corrective_action_age_days_03(record):
    """Evaluate corrective action age for control WP-0269-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("corrective_action_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-03", "metric": "corrective_action_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-03", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-03", "metric": "corrective_action_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-03", "metric": "corrective_action_age_days", "label": "corrective action age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "corrective action age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_surge_protection_test_age_days_04(record):
    """Evaluate surge protection test age for control WP-0269-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("surge_protection_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-04", "metric": "surge_protection_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-04", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-04", "metric": "surge_protection_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-04", "metric": "surge_protection_test_age_days", "label": "surge protection test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "surge protection test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_secret_scan_findings_05(record):
    """Evaluate secret scan findings for control WP-0269-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("secret_scan_findings")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-05", "metric": "secret_scan_findings",
            "status": "insufficient_data",
            "severity": "medium", "unit": "items",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-05", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-05", "metric": "secret_scan_findings", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-05", "metric": "secret_scan_findings", "label": "secret scan findings",
        "status": "breach", "severity": "medium", "unit": "items",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "secret scan findings exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_scanner_read_rate_pct_06(record):
    """Evaluate scanner read rate for control WP-0269-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-06", "metric": "scanner_read_rate_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 39,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-06", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-06", "metric": "scanner_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 39
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-06", "metric": "scanner_read_rate_pct", "label": "scanner read rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 39, "comparison": "min",
        "finding": "scanner read rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_adjustment_reason_completeness_pct_07(record):
    """Evaluate adjustment reason completeness for control WP-0269-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("adjustment_reason_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-07", "metric": "adjustment_reason_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-07", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-07", "metric": "adjustment_reason_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-07", "metric": "adjustment_reason_completeness_pct", "label": "adjustment reason completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "adjustment reason completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_pick_confirmation_latency_ms_08(record):
    """Evaluate pick confirmation latency for control WP-0269-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pick_confirmation_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-08", "metric": "pick_confirmation_latency_ms",
            "status": "insufficient_data",
            "severity": "low", "unit": "ms",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-08", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-08", "metric": "pick_confirmation_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-08", "metric": "pick_confirmation_latency_ms", "label": "pick confirmation latency",
        "status": "breach", "severity": "low", "unit": "ms",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "pick confirmation latency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_bonded_stock_variance_09(record):
    """Evaluate bonded stock variance for control WP-0269-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("bonded_stock_variance")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-09", "metric": "bonded_stock_variance",
            "status": "insufficient_data",
            "severity": "medium", "unit": "units",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-09", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-09", "metric": "bonded_stock_variance", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-09", "metric": "bonded_stock_variance", "label": "bonded stock variance",
        "status": "breach", "severity": "medium", "unit": "units",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "bonded stock variance exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_empty_miles_pct_10(record):
    """Evaluate empty miles share for control WP-0269-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("empty_miles_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-10", "metric": "empty_miles_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-10", "metric": "empty_miles_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-10", "metric": "empty_miles_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-10", "metric": "empty_miles_pct", "label": "empty miles share",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 83, "comparison": "min",
        "finding": "empty miles share falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_idle_time_pct_11(record):
    """Evaluate idle time share for control WP-0269-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("idle_time_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-11", "metric": "idle_time_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-11", "metric": "idle_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-11", "metric": "idle_time_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-11", "metric": "idle_time_pct", "label": "idle time share",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "idle time share must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_certification_days_left_12(record):
    """Evaluate supplier certification validity for control WP-0269-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_certification_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-12", "metric": "supplier_certification_days_left",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-12", "metric": "supplier_certification_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-12", "metric": "supplier_certification_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-12", "metric": "supplier_certification_days_left", "label": "supplier certification validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier certification validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_return_material_age_days_13(record):
    """Evaluate supplier return material age for control WP-0269-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_return_material_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-13", "metric": "supplier_return_material_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-13", "metric": "supplier_return_material_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-13", "metric": "supplier_return_material_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-13", "metric": "supplier_return_material_age_days", "label": "supplier return material age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "supplier return material age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_cost_change_notice_days_14(record):
    """Evaluate supplier cost-change notice for control WP-0269-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_cost_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-14", "metric": "supplier_cost_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 32,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-14", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-14", "metric": "supplier_cost_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 32
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-14", "metric": "supplier_cost_change_notice_days", "label": "supplier cost-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 32, "comparison": "min",
        "finding": "supplier cost-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_change_failure_pct_15(record):
    """Evaluate supplier change-failure rate for control WP-0269-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_change_failure_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-15", "metric": "supplier_change_failure_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-15", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-15", "metric": "supplier_change_failure_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-15", "metric": "supplier_change_failure_pct", "label": "supplier change-failure rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier change-failure rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_weight_spec_match_pct_16(record):
    """Evaluate supplier weight specification match for control WP-0269-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_weight_spec_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-16", "metric": "supplier_weight_spec_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-16", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-16", "metric": "supplier_weight_spec_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-16", "metric": "supplier_weight_spec_match_pct", "label": "supplier weight specification match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier weight specification match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_loading_supervision_pct_17(record):
    """Evaluate supplier loading supervision for control WP-0269-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_loading_supervision_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-17", "metric": "supplier_loading_supervision_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-17", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-17", "metric": "supplier_loading_supervision_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-17", "metric": "supplier_loading_supervision_pct", "label": "supplier loading supervision",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "supplier loading supervision exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_site_change_notice_days_18(record):
    """Evaluate supplier site-change notice for control WP-0269-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_site_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-18", "metric": "supplier_site_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 76,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-18", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-18", "metric": "supplier_site_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 76
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-18", "metric": "supplier_site_change_notice_days", "label": "supplier site-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 76, "comparison": "min",
        "finding": "supplier site-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_prop65_compliance_pct_19(record):
    """Evaluate supplier Prop 65 compliance for control WP-0269-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prop65_compliance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-19", "metric": "supplier_prop65_compliance_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-19", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-19", "metric": "supplier_prop65_compliance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-19", "metric": "supplier_prop65_compliance_pct", "label": "supplier Prop 65 compliance",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier Prop 65 compliance must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_payment_fraud_signal_20(record):
    """Evaluate supplier payment-fraud signal for control WP-0269-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_payment_fraud_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-20", "metric": "supplier_payment_fraud_signal",
            "status": "insufficient_data",
            "severity": "low", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-20", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-20", "metric": "supplier_payment_fraud_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-20", "metric": "supplier_payment_fraud_signal", "label": "supplier payment-fraud signal",
        "status": "breach", "severity": "low", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier payment-fraud signal must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

def assess_supplier_it_recovery_minutes_21(record):
    """Evaluate supplier IT recovery time for control WP-0269-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_it_recovery_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-21", "metric": "supplier_it_recovery_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 197,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-21", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-21", "metric": "supplier_it_recovery_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 197
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-21", "metric": "supplier_it_recovery_minutes", "label": "supplier IT recovery time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 197, "comparison": "max",
        "finding": "supplier IT recovery time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "hazardous material handling",
    }

def assess_supplier_algorithm_change_notice_days_22(record):
    """Evaluate supplier algorithm-change notice for control WP-0269-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_algorithm_change_notice_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-22", "metric": "supplier_algorithm_change_notice_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-22", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-22", "metric": "supplier_algorithm_change_notice_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-22", "metric": "supplier_algorithm_change_notice_days", "label": "supplier algorithm-change notice",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier algorithm-change notice falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "hazardous material handling",
    }

def assess_supplier_dependency_update_age_days_23(record):
    """Evaluate supplier dependency update age for control WP-0269-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dependency_update_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-23", "metric": "supplier_dependency_update_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-23", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-23", "metric": "supplier_dependency_update_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-23", "metric": "supplier_dependency_update_age_days", "label": "supplier dependency update age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dependency update age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "hazardous material handling",
    }

def assess_supplier_scim_sync_age_hours_24(record):
    """Evaluate supplier SCIM sync age for control WP-0269-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_scim_sync_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0269-24", "metric": "supplier_scim_sync_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0269-24", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0269-24", "metric": "supplier_scim_sync_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0269-24", "metric": "supplier_scim_sync_age_hours", "label": "supplier SCIM sync age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier SCIM sync age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "hazardous material handling",
    }

RULES = (assess_coa_document_pct_01, assess_battery_swelling_signal_02, assess_corrective_action_age_days_03, assess_surge_protection_test_age_days_04, assess_secret_scan_findings_05, assess_scanner_read_rate_pct_06, assess_adjustment_reason_completeness_pct_07, assess_pick_confirmation_latency_ms_08, assess_bonded_stock_variance_09, assess_empty_miles_pct_10, assess_idle_time_pct_11, assess_supplier_certification_days_left_12, assess_supplier_return_material_age_days_13, assess_supplier_cost_change_notice_days_14, assess_supplier_change_failure_pct_15, assess_supplier_weight_spec_match_pct_16, assess_supplier_loading_supervision_pct_17, assess_supplier_site_change_notice_days_18, assess_supplier_prop65_compliance_pct_19, assess_supplier_payment_fraud_signal_20, assess_supplier_it_recovery_minutes_21, assess_supplier_algorithm_change_notice_days_22, assess_supplier_dependency_update_age_days_23, assess_supplier_scim_sync_age_hours_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

