"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_labor_hours_01(record):
    """Evaluate labor hours for control WP-0698-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("labor_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-01", "metric": "labor_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-01", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-01", "metric": "labor_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-01", "metric": "labor_hours", "label": "labor hours",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "labor hours must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_worker_load_pct_02(record):
    """Evaluate worker load for control WP-0698-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("worker_load_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-02", "metric": "worker_load_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 99,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-02", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-02", "metric": "worker_load_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 99
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-02", "metric": "worker_load_pct", "label": "worker load",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 99, "comparison": "max",
        "finding": "worker load exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_backup_age_hours_03(record):
    """Evaluate backup age for control WP-0698-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-03", "metric": "backup_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 64,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-03", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-03", "metric": "backup_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 64
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-03", "metric": "backup_age_hours", "label": "backup age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 64, "comparison": "min",
        "finding": "backup age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_carrier_claim_rate_pct_04(record):
    """Evaluate carrier claim rate for control WP-0698-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carrier_claim_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-04", "metric": "carrier_claim_rate_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-04", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-04", "metric": "carrier_claim_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-04", "metric": "carrier_claim_rate_pct", "label": "carrier claim rate",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carrier claim rate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_yard_dwell_hours_05(record):
    """Evaluate yard dwell for control WP-0698-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("yard_dwell_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-05", "metric": "yard_dwell_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-05", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-05", "metric": "yard_dwell_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-05", "metric": "yard_dwell_hours", "label": "yard dwell",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "yard dwell must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_dashboard_load_ms_06(record):
    """Evaluate dashboard load time for control WP-0698-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dashboard_load_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-06", "metric": "dashboard_load_ms",
            "status": "insufficient_data",
            "severity": "critical", "unit": "ms",
            "observed": None,
            "threshold": 119,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-06", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-06", "metric": "dashboard_load_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 119
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-06", "metric": "dashboard_load_ms", "label": "dashboard load time",
        "status": "breach", "severity": "critical", "unit": "ms",
        "observed": observed,
        "threshold": 119, "comparison": "max",
        "finding": "dashboard load time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_batch_release_age_minutes_07(record):
    """Evaluate batch release age for control WP-0698-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("batch_release_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-07", "metric": "batch_release_age_minutes",
            "status": "insufficient_data",
            "severity": "low", "unit": "minutes",
            "observed": None,
            "threshold": 13,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-07", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-07", "metric": "batch_release_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 13
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-07", "metric": "batch_release_age_minutes", "label": "batch release age",
        "status": "breach", "severity": "low", "unit": "minutes",
        "observed": observed,
        "threshold": 13, "comparison": "min",
        "finding": "batch release age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_high_value_cage_open_minutes_08(record):
    """Evaluate high-value cage open time for control WP-0698-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("high_value_cage_open_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-08", "metric": "high_value_cage_open_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-08", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-08", "metric": "high_value_cage_open_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-08", "metric": "high_value_cage_open_minutes", "label": "high-value cage open time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "high-value cage open time must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_compressor_runtime_hours_09(record):
    """Evaluate compressor runtime for control WP-0698-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("compressor_runtime_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-09", "metric": "compressor_runtime_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-09", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-09", "metric": "compressor_runtime_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-09", "metric": "compressor_runtime_hours", "label": "compressor runtime",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "compressor runtime must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_authentication_scan_pct_10(record):
    """Evaluate authentication scan rate for control WP-0698-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("authentication_scan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-10", "metric": "authentication_scan_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 139,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-10", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-10", "metric": "authentication_scan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 139
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-10", "metric": "authentication_scan_pct", "label": "authentication scan rate",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 139, "comparison": "max",
        "finding": "authentication scan rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_contractor_induction_pct_11(record):
    """Evaluate contractor induction completion for control WP-0698-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("contractor_induction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-11", "metric": "contractor_induction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 57,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-11", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-11", "metric": "contractor_induction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 57
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-11", "metric": "contractor_induction_pct", "label": "contractor induction completion",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 57, "comparison": "min",
        "finding": "contractor induction completion falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_plc_alarm_count_12(record):
    """Evaluate PLC alarms for control WP-0698-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("plc_alarm_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-12", "metric": "plc_alarm_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-12", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-12", "metric": "plc_alarm_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-12", "metric": "plc_alarm_count", "label": "PLC alarms",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "PLC alarms must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_change_approval_pct_13(record):
    """Evaluate change approval completeness for control WP-0698-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-13", "metric": "change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-13", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-13", "metric": "change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-13", "metric": "change_approval_pct", "label": "change approval completeness",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "change approval completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_data_export_age_hours_14(record):
    """Evaluate data export age for control WP-0698-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("data_export_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-14", "metric": "data_export_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 159,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-14", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-14", "metric": "data_export_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 159
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-14", "metric": "data_export_age_hours", "label": "data export age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 159, "comparison": "max",
        "finding": "data export age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_harmonized_code_gap_count_15(record):
    """Evaluate harmonized-code gaps for control WP-0698-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("harmonized_code_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-15", "metric": "harmonized_code_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 6,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-15", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-15", "metric": "harmonized_code_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 6
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-15", "metric": "harmonized_code_gap_count", "label": "harmonized-code gaps",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 6, "comparison": "min",
        "finding": "harmonized-code gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_asn_receipt_match_pct_16(record):
    """Evaluate ASN receipt match for control WP-0698-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("asn_receipt_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-16", "metric": "asn_receipt_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-16", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-16", "metric": "asn_receipt_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-16", "metric": "asn_receipt_match_pct", "label": "ASN receipt match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ASN receipt match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_customer_delivery_rating_17(record):
    """Evaluate customer delivery rating for control WP-0698-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("customer_delivery_rating")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-17", "metric": "customer_delivery_rating",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-17", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-17", "metric": "customer_delivery_rating", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-17", "metric": "customer_delivery_rating", "label": "customer delivery rating",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "customer delivery rating must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_demurrage_charge_days_18(record):
    """Evaluate demurrage charge days for control WP-0698-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("demurrage_charge_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-18", "metric": "demurrage_charge_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 179,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-18", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-18", "metric": "demurrage_charge_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 179
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-18", "metric": "demurrage_charge_days", "label": "demurrage charge days",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 179, "comparison": "max",
        "finding": "demurrage charge days exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_fuel_card_exception_count_19(record):
    """Evaluate fuel card exceptions for control WP-0698-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fuel_card_exception_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-19", "metric": "fuel_card_exception_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 50,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-19", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-19", "metric": "fuel_card_exception_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 50
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-19", "metric": "fuel_card_exception_count", "label": "fuel card exceptions",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 50, "comparison": "min",
        "finding": "fuel card exceptions falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_geopolitical_risk_score_20(record):
    """Evaluate supplier geopolitical risk for control WP-0698-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_geopolitical_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-20", "metric": "supplier_geopolitical_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-20", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-20", "metric": "supplier_geopolitical_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-20", "metric": "supplier_geopolitical_risk_score", "label": "supplier geopolitical risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier geopolitical risk must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_turnover_pct_21(record):
    """Evaluate supplier turnover rate for control WP-0698-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_turnover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-21", "metric": "supplier_turnover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-21", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-21", "metric": "supplier_turnover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-21", "metric": "supplier_turnover_pct", "label": "supplier turnover rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier turnover rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_disruption_alert_age_hours_22(record):
    """Evaluate supplier disruption alert age for control WP-0698-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_disruption_alert_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-22", "metric": "supplier_disruption_alert_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 199,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-22", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-22", "metric": "supplier_disruption_alert_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 199
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-22", "metric": "supplier_disruption_alert_age_hours", "label": "supplier disruption alert age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 199, "comparison": "max",
        "finding": "supplier disruption alert age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_access_review_age_days_23(record):
    """Evaluate supplier access review age for control WP-0698-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-23", "metric": "supplier_access_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 94,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-23", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-23", "metric": "supplier_access_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 94
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-23", "metric": "supplier_access_review_age_days", "label": "supplier access review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 94, "comparison": "min",
        "finding": "supplier access review age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_capacity_headroom_pct_24(record):
    """Evaluate supplier capacity headroom for control WP-0698-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_capacity_headroom_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0698-24", "metric": "supplier_capacity_headroom_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0698-24", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0698-24", "metric": "supplier_capacity_headroom_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0698-24", "metric": "supplier_capacity_headroom_pct", "label": "supplier capacity headroom",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier capacity headroom must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_labor_hours_01, assess_worker_load_pct_02, assess_backup_age_hours_03, assess_carrier_claim_rate_pct_04, assess_yard_dwell_hours_05, assess_dashboard_load_ms_06, assess_batch_release_age_minutes_07, assess_high_value_cage_open_minutes_08, assess_compressor_runtime_hours_09, assess_authentication_scan_pct_10, assess_contractor_induction_pct_11, assess_plc_alarm_count_12, assess_change_approval_pct_13, assess_data_export_age_hours_14, assess_harmonized_code_gap_count_15, assess_asn_receipt_match_pct_16, assess_customer_delivery_rating_17, assess_demurrage_charge_days_18, assess_fuel_card_exception_count_19, assess_supplier_geopolitical_risk_score_20, assess_supplier_turnover_pct_21, assess_supplier_disruption_alert_age_hours_22, assess_supplier_access_review_age_days_23, assess_supplier_capacity_headroom_pct_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

