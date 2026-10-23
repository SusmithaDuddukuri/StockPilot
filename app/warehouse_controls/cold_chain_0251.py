"""Operational control pack for cold-chain handling; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_invoice_upload_age_hours_01(record):
    """Evaluate supplier invoice upload age for control WP-0251-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-01", "metric": "supplier_invoice_upload_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-01", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-01", "metric": "supplier_invoice_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-01", "metric": "supplier_invoice_upload_age_hours", "label": "supplier invoice upload age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice upload age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_supplier_dns_cutover_age_hours_02(record):
    """Evaluate supplier DNS cutover age for control WP-0251-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dns_cutover_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-02", "metric": "supplier_dns_cutover_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-02", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-02", "metric": "supplier_dns_cutover_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-02", "metric": "supplier_dns_cutover_age_hours", "label": "supplier DNS cutover age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier DNS cutover age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_pack_rate_03(record):
    """Evaluate packing rate for control WP-0251-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pack_rate")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-03", "metric": "pack_rate",
            "status": "insufficient_data",
            "severity": "medium", "unit": "orders/hour",
            "observed": None,
            "threshold": 53,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-03", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-03", "metric": "pack_rate", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 53
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-03", "metric": "pack_rate", "label": "packing rate",
        "status": "breach", "severity": "medium", "unit": "orders/hour",
        "observed": observed,
        "threshold": 53, "comparison": "max",
        "finding": "packing rate exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_forklift_inspection_age_days_04(record):
    """Evaluate inspection age for control WP-0251-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forklift_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-04", "metric": "forklift_inspection_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 81,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-04", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-04", "metric": "forklift_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 81
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-04", "metric": "forklift_inspection_age_days", "label": "inspection age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 81, "comparison": "min",
        "finding": "inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_audit_gap_count_05(record):
    """Evaluate audit gaps for control WP-0251-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("audit_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-05", "metric": "audit_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-05", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-05", "metric": "audit_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-05", "metric": "audit_gap_count", "label": "audit gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "audit gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_stockout_hours_06(record):
    """Evaluate stockout duration for control WP-0251-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stockout_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-06", "metric": "stockout_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-06", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-06", "metric": "stockout_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-06", "metric": "stockout_hours", "label": "stockout duration",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "stockout duration must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_driver_hours_remaining_07(record):
    """Evaluate driver hours remaining for control WP-0251-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_hours_remaining")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-07", "metric": "driver_hours_remaining",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 73,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-07", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-07", "metric": "driver_hours_remaining", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 73
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-07", "metric": "driver_hours_remaining", "label": "driver hours remaining",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 73, "comparison": "max",
        "finding": "driver hours remaining exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_privileged_account_count_08(record):
    """Evaluate privileged accounts for control WP-0251-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privileged_account_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-08", "metric": "privileged_account_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "accounts",
            "observed": None,
            "threshold": 30,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-08", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-08", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 30
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-08", "metric": "privileged_account_count", "label": "privileged accounts",
        "status": "breach", "severity": "high", "unit": "accounts",
        "observed": observed,
        "threshold": 30, "comparison": "min",
        "finding": "privileged accounts falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_handover_gap_count_09(record):
    """Evaluate handover gaps for control WP-0251-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-09", "metric": "handover_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-09", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-09", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-09", "metric": "handover_gap_count", "label": "handover gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "handover gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_sprinkler_inspection_age_days_10(record):
    """Evaluate sprinkler inspection age for control WP-0251-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-10", "metric": "sprinkler_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-10", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-10", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-10", "metric": "sprinkler_inspection_age_days", "label": "sprinkler inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "sprinkler inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_recipient_match_pct_11(record):
    """Evaluate recipient match for control WP-0251-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recipient_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-11", "metric": "recipient_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 93,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-11", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-11", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 93
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-11", "metric": "recipient_match_pct", "label": "recipient match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 93, "comparison": "max",
        "finding": "recipient match exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_excursion_response_minutes_12(record):
    """Evaluate excursion response time for control WP-0251-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("excursion_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-12", "metric": "excursion_response_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 74,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-12", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-12", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 74
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-12", "metric": "excursion_response_minutes", "label": "excursion response time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 74, "comparison": "min",
        "finding": "excursion response time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_product_serial_capture_pct_13(record):
    """Evaluate product serial capture for control WP-0251-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-13", "metric": "product_serial_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-13", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-13", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-13", "metric": "product_serial_capture_pct", "label": "product serial capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "product serial capture must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_ladder_inspection_age_days_14(record):
    """Evaluate ladder inspection age for control WP-0251-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ladder_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-14", "metric": "ladder_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-14", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-14", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-14", "metric": "ladder_inspection_age_days", "label": "ladder inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "ladder inspection age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_backup_power_test_age_days_15(record):
    """Evaluate backup power test age for control WP-0251-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_power_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-15", "metric": "backup_power_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 113,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-15", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-15", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 113
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-15", "metric": "backup_power_test_age_days", "label": "backup power test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 113, "comparison": "max",
        "finding": "backup power test age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_tls_error_count_16(record):
    """Evaluate TLS errors for control WP-0251-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tls_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-16", "metric": "tls_error_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 23,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-16", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-16", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 23
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-16", "metric": "tls_error_count", "label": "TLS errors",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 23, "comparison": "min",
        "finding": "TLS errors falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_metrology_certificate_age_days_17(record):
    """Evaluate metrology certificate age for control WP-0251-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("metrology_certificate_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-17", "metric": "metrology_certificate_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-17", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-17", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-17", "metric": "metrology_certificate_age_days", "label": "metrology certificate age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "metrology certificate age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_inventory_reconciliation_age_hours_18(record):
    """Evaluate inventory reconciliation age for control WP-0251-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-18", "metric": "inventory_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-18", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-18", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-18", "metric": "inventory_reconciliation_age_hours", "label": "inventory reconciliation age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory reconciliation age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_slotting_revisit_age_days_19(record):
    """Evaluate slotting revisit age for control WP-0251-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_revisit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-19", "metric": "slotting_revisit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 133,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-19", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-19", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 133
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-19", "metric": "slotting_revisit_age_days", "label": "slotting revisit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 133, "comparison": "max",
        "finding": "slotting revisit age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_export_declaration_age_hours_20(record):
    """Evaluate export declaration age for control WP-0251-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-20", "metric": "export_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-20", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-20", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-20", "metric": "export_declaration_age_hours", "label": "export declaration age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 67, "comparison": "min",
        "finding": "export declaration age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

def assess_vehicle_capacity_overage_kg_21(record):
    """Evaluate vehicle capacity overage for control WP-0251-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_capacity_overage_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-21", "metric": "vehicle_capacity_overage_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-21", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-21", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-21", "metric": "vehicle_capacity_overage_kg", "label": "vehicle capacity overage",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "vehicle capacity overage must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cold-chain handling",
    }

def assess_units_per_labor_hour_22(record):
    """Evaluate units per labor hour for control WP-0251-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("units_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-22", "metric": "units_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "units/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-22", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-22", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-22", "metric": "units_per_labor_hour", "label": "units per labor hour",
        "status": "breach", "severity": "low", "unit": "units/hour",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "units per labor hour must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cold-chain handling",
    }

def assess_supplier_invoice_accuracy_pct_23(record):
    """Evaluate supplier invoice accuracy for control WP-0251-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-23", "metric": "supplier_invoice_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 153,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-23", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-23", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 153
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-23", "metric": "supplier_invoice_accuracy_pct", "label": "supplier invoice accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 153, "comparison": "max",
        "finding": "supplier invoice accuracy exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cold-chain handling",
    }

def assess_supplier_lifecycle_risk_score_24(record):
    """Evaluate supplier lifecycle risk for control WP-0251-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lifecycle_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0251-24", "metric": "supplier_lifecycle_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 16,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0251-24", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0251-24", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 16
    if not failed:
        return None
    return {
        "rule_id": "WP-0251-24", "metric": "supplier_lifecycle_risk_score", "label": "supplier lifecycle risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 16, "comparison": "min",
        "finding": "supplier lifecycle risk falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cold-chain handling",
    }

RULES = (assess_supplier_invoice_upload_age_hours_01, assess_supplier_dns_cutover_age_hours_02, assess_pack_rate_03, assess_forklift_inspection_age_days_04, assess_audit_gap_count_05, assess_stockout_hours_06, assess_driver_hours_remaining_07, assess_privileged_account_count_08, assess_handover_gap_count_09, assess_sprinkler_inspection_age_days_10, assess_recipient_match_pct_11, assess_excursion_response_minutes_12, assess_product_serial_capture_pct_13, assess_ladder_inspection_age_days_14, assess_backup_power_test_age_days_15, assess_tls_error_count_16, assess_metrology_certificate_age_days_17, assess_inventory_reconciliation_age_hours_18, assess_slotting_revisit_age_days_19, assess_export_declaration_age_hours_20, assess_vehicle_capacity_overage_kg_21, assess_units_per_labor_hour_22, assess_supplier_invoice_accuracy_pct_23, assess_supplier_lifecycle_risk_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

