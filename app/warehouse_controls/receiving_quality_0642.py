"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_privileged_account_count_01(record):
    """Evaluate privileged accounts for control WP-0642-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("privileged_account_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-01", "metric": "privileged_account_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "accounts",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-01", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-01", "metric": "privileged_account_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-01", "metric": "privileged_account_count", "label": "privileged accounts",
        "status": "breach", "severity": "high", "unit": "accounts",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "privileged accounts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_handover_gap_count_02(record):
    """Evaluate handover gaps for control WP-0642-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("handover_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-02", "metric": "handover_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-02", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-02", "metric": "handover_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-02", "metric": "handover_gap_count", "label": "handover gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 91, "comparison": "max",
        "finding": "handover gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_sprinkler_inspection_age_days_03(record):
    """Evaluate sprinkler inspection age for control WP-0642-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-03", "metric": "sprinkler_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-03", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-03", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-03", "metric": "sprinkler_inspection_age_days", "label": "sprinkler inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "sprinkler inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_recipient_match_pct_04(record):
    """Evaluate recipient match for control WP-0642-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recipient_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-04", "metric": "recipient_match_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-04", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-04", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-04", "metric": "recipient_match_pct", "label": "recipient match",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "recipient match must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_excursion_response_minutes_05(record):
    """Evaluate excursion response time for control WP-0642-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("excursion_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-05", "metric": "excursion_response_minutes",
            "status": "insufficient_data",
            "severity": "high", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-05", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-05", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-05", "metric": "excursion_response_minutes", "label": "excursion response time",
        "status": "breach", "severity": "high", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "excursion response time must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_product_serial_capture_pct_06(record):
    """Evaluate product serial capture for control WP-0642-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-06", "metric": "product_serial_capture_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 111,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-06", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-06", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 111
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-06", "metric": "product_serial_capture_pct", "label": "product serial capture",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 111, "comparison": "max",
        "finding": "product serial capture exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_ladder_inspection_age_days_07(record):
    """Evaluate ladder inspection age for control WP-0642-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ladder_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-07", "metric": "ladder_inspection_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 1,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-07", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-07", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 1
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-07", "metric": "ladder_inspection_age_days", "label": "ladder inspection age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 1, "comparison": "min",
        "finding": "ladder inspection age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_backup_power_test_age_days_08(record):
    """Evaluate backup power test age for control WP-0642-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_power_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-08", "metric": "backup_power_test_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-08", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-08", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-08", "metric": "backup_power_test_age_days", "label": "backup power test age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "backup power test age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_tls_error_count_09(record):
    """Evaluate TLS errors for control WP-0642-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tls_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-09", "metric": "tls_error_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-09", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-09", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-09", "metric": "tls_error_count", "label": "TLS errors",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "TLS errors must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_metrology_certificate_age_days_10(record):
    """Evaluate metrology certificate age for control WP-0642-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("metrology_certificate_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-10", "metric": "metrology_certificate_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 131,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-10", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-10", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 131
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-10", "metric": "metrology_certificate_age_days", "label": "metrology certificate age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 131, "comparison": "max",
        "finding": "metrology certificate age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_inventory_reconciliation_age_hours_11(record):
    """Evaluate inventory reconciliation age for control WP-0642-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-11", "metric": "inventory_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-11", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-11", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-11", "metric": "inventory_reconciliation_age_hours", "label": "inventory reconciliation age",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 45, "comparison": "min",
        "finding": "inventory reconciliation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_slotting_revisit_age_days_12(record):
    """Evaluate slotting revisit age for control WP-0642-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_revisit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-12", "metric": "slotting_revisit_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-12", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-12", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-12", "metric": "slotting_revisit_age_days", "label": "slotting revisit age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "slotting revisit age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_export_declaration_age_hours_13(record):
    """Evaluate export declaration age for control WP-0642-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-13", "metric": "export_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "high", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-13", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-13", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-13", "metric": "export_declaration_age_hours", "label": "export declaration age",
        "status": "breach", "severity": "high", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "export declaration age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_vehicle_capacity_overage_kg_14(record):
    """Evaluate vehicle capacity overage for control WP-0642-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_capacity_overage_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-14", "metric": "vehicle_capacity_overage_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 151,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-14", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-14", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 151
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-14", "metric": "vehicle_capacity_overage_kg", "label": "vehicle capacity overage",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 151, "comparison": "max",
        "finding": "vehicle capacity overage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_units_per_labor_hour_15(record):
    """Evaluate units per labor hour for control WP-0642-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("units_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-15", "metric": "units_per_labor_hour",
            "status": "insufficient_data",
            "severity": "low", "unit": "units/hour",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-15", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-15", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-15", "metric": "units_per_labor_hour", "label": "units per labor hour",
        "status": "breach", "severity": "low", "unit": "units/hour",
        "observed": observed,
        "threshold": 89, "comparison": "min",
        "finding": "units per labor hour falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_invoice_accuracy_pct_16(record):
    """Evaluate supplier invoice accuracy for control WP-0642-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-16", "metric": "supplier_invoice_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-16", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-16", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-16", "metric": "supplier_invoice_accuracy_pct", "label": "supplier invoice accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier invoice accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_lifecycle_risk_score_17(record):
    """Evaluate supplier lifecycle risk for control WP-0642-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lifecycle_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-17", "metric": "supplier_lifecycle_risk_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-17", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-17", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-17", "metric": "supplier_lifecycle_risk_score", "label": "supplier lifecycle risk",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier lifecycle risk must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_delivery_evidence_pct_18(record):
    """Evaluate supplier delivery evidence for control WP-0642-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-18", "metric": "supplier_delivery_evidence_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 171,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-18", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-18", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 171
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-18", "metric": "supplier_delivery_evidence_pct", "label": "supplier delivery evidence",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 171, "comparison": "max",
        "finding": "supplier delivery evidence exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_support_resolution_hours_19(record):
    """Evaluate supplier support resolution for control WP-0642-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-19", "metric": "supplier_support_resolution_hours",
            "status": "insufficient_data",
            "severity": "low", "unit": "hours",
            "observed": None,
            "threshold": 38,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-19", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-19", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 38
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-19", "metric": "supplier_support_resolution_hours", "label": "supplier support resolution",
        "status": "breach", "severity": "low", "unit": "hours",
        "observed": observed,
        "threshold": 38, "comparison": "min",
        "finding": "supplier support resolution falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_coa_accuracy_pct_20(record):
    """Evaluate supplier CoA accuracy for control WP-0642-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_coa_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-20", "metric": "supplier_coa_accuracy_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-20", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-20", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-20", "metric": "supplier_coa_accuracy_pct", "label": "supplier CoA accuracy",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier CoA accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_visitor_control_pct_21(record):
    """Evaluate supplier visitor control for control WP-0642-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_visitor_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-21", "metric": "supplier_visitor_control_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-21", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-21", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-21", "metric": "supplier_visitor_control_pct", "label": "supplier visitor control",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier visitor control must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_key_person_dependency_pct_22(record):
    """Evaluate supplier key-person dependency for control WP-0642-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_person_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-22", "metric": "supplier_key_person_dependency_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 191,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-22", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-22", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 191
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-22", "metric": "supplier_key_person_dependency_pct", "label": "supplier key-person dependency",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 191, "comparison": "max",
        "finding": "supplier key-person dependency exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_material_restriction_gap_count_23(record):
    """Evaluate supplier material restriction gaps for control WP-0642-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_restriction_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-23", "metric": "supplier_material_restriction_gap_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 82,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-23", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-23", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 82
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-23", "metric": "supplier_material_restriction_gap_count", "label": "supplier material restriction gaps",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 82, "comparison": "min",
        "finding": "supplier material restriction gaps falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_ownership_review_age_days_24(record):
    """Evaluate supplier ownership review age for control WP-0642-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ownership_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0642-24", "metric": "supplier_ownership_review_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0642-24", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0642-24", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0642-24", "metric": "supplier_ownership_review_age_days", "label": "supplier ownership review age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ownership review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_privileged_account_count_01, assess_handover_gap_count_02, assess_sprinkler_inspection_age_days_03, assess_recipient_match_pct_04, assess_excursion_response_minutes_05, assess_product_serial_capture_pct_06, assess_ladder_inspection_age_days_07, assess_backup_power_test_age_days_08, assess_tls_error_count_09, assess_metrology_certificate_age_days_10, assess_inventory_reconciliation_age_hours_11, assess_slotting_revisit_age_days_12, assess_export_declaration_age_hours_13, assess_vehicle_capacity_overage_kg_14, assess_units_per_labor_hour_15, assess_supplier_invoice_accuracy_pct_16, assess_supplier_lifecycle_risk_score_17, assess_supplier_delivery_evidence_pct_18, assess_supplier_support_resolution_hours_19, assess_supplier_coa_accuracy_pct_20, assess_supplier_visitor_control_pct_21, assess_supplier_key_person_dependency_pct_22, assess_supplier_material_restriction_gap_count_23, assess_supplier_ownership_review_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

