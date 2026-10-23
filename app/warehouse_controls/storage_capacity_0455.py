"""Operational control pack for storage capacity; rules are executable against warehouse records."""
from math import isfinite

def assess_sprinkler_inspection_age_days_01(record):
    """Evaluate sprinkler inspection age for control WP-0455-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sprinkler_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-01", "metric": "sprinkler_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-01", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-01", "metric": "sprinkler_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-01", "metric": "sprinkler_inspection_age_days", "label": "sprinkler inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "sprinkler inspection age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_recipient_match_pct_02(record):
    """Evaluate recipient match for control WP-0455-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recipient_match_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-02", "metric": "recipient_match_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-02", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-02", "metric": "recipient_match_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-02", "metric": "recipient_match_pct", "label": "recipient match",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "recipient match must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_excursion_response_minutes_03(record):
    """Evaluate excursion response time for control WP-0455-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("excursion_response_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-03", "metric": "excursion_response_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 185,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-03", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-03", "metric": "excursion_response_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 185
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-03", "metric": "excursion_response_minutes", "label": "excursion response time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 185, "comparison": "max",
        "finding": "excursion response time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_product_serial_capture_pct_04(record):
    """Evaluate product serial capture for control WP-0455-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("product_serial_capture_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-04", "metric": "product_serial_capture_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-04", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-04", "metric": "product_serial_capture_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-04", "metric": "product_serial_capture_pct", "label": "product serial capture",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "product serial capture falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_ladder_inspection_age_days_05(record):
    """Evaluate ladder inspection age for control WP-0455-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("ladder_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-05", "metric": "ladder_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-05", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-05", "metric": "ladder_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-05", "metric": "ladder_inspection_age_days", "label": "ladder inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "ladder inspection age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_backup_power_test_age_days_06(record):
    """Evaluate backup power test age for control WP-0455-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backup_power_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-06", "metric": "backup_power_test_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-06", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-06", "metric": "backup_power_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-06", "metric": "backup_power_test_age_days", "label": "backup power test age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backup power test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_tls_error_count_07(record):
    """Evaluate TLS errors for control WP-0455-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("tls_error_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-07", "metric": "tls_error_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-07", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-07", "metric": "tls_error_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-07", "metric": "tls_error_count", "label": "TLS errors",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 25, "comparison": "max",
        "finding": "TLS errors exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_metrology_certificate_age_days_08(record):
    """Evaluate metrology certificate age for control WP-0455-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("metrology_certificate_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-08", "metric": "metrology_certificate_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-08", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-08", "metric": "metrology_certificate_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-08", "metric": "metrology_certificate_age_days", "label": "metrology certificate age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "metrology certificate age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_inventory_reconciliation_age_hours_09(record):
    """Evaluate inventory reconciliation age for control WP-0455-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inventory_reconciliation_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-09", "metric": "inventory_reconciliation_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-09", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-09", "metric": "inventory_reconciliation_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-09", "metric": "inventory_reconciliation_age_hours", "label": "inventory reconciliation age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "inventory reconciliation age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_slotting_revisit_age_days_10(record):
    """Evaluate slotting revisit age for control WP-0455-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("slotting_revisit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-10", "metric": "slotting_revisit_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-10", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-10", "metric": "slotting_revisit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-10", "metric": "slotting_revisit_age_days", "label": "slotting revisit age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "slotting revisit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_export_declaration_age_hours_11(record):
    """Evaluate export declaration age for control WP-0455-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("export_declaration_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-11", "metric": "export_declaration_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 45,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-11", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-11", "metric": "export_declaration_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 45
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-11", "metric": "export_declaration_age_hours", "label": "export declaration age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 45, "comparison": "max",
        "finding": "export declaration age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_vehicle_capacity_overage_kg_12(record):
    """Evaluate vehicle capacity overage for control WP-0455-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_capacity_overage_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-12", "metric": "vehicle_capacity_overage_kg",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-12", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-12", "metric": "vehicle_capacity_overage_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-12", "metric": "vehicle_capacity_overage_kg", "label": "vehicle capacity overage",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "vehicle capacity overage falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_units_per_labor_hour_13(record):
    """Evaluate units per labor hour for control WP-0455-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("units_per_labor_hour")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-13", "metric": "units_per_labor_hour",
            "status": "insufficient_data",
            "severity": "critical", "unit": "units/hour",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-13", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-13", "metric": "units_per_labor_hour", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-13", "metric": "units_per_labor_hour", "label": "units per labor hour",
        "status": "breach", "severity": "critical", "unit": "units/hour",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "units per labor hour must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_invoice_accuracy_pct_14(record):
    """Evaluate supplier invoice accuracy for control WP-0455-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_invoice_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-14", "metric": "supplier_invoice_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-14", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-14", "metric": "supplier_invoice_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-14", "metric": "supplier_invoice_accuracy_pct", "label": "supplier invoice accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier invoice accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_lifecycle_risk_score_15(record):
    """Evaluate supplier lifecycle risk for control WP-0455-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_lifecycle_risk_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-15", "metric": "supplier_lifecycle_risk_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 65,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-15", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-15", "metric": "supplier_lifecycle_risk_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 65
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-15", "metric": "supplier_lifecycle_risk_score", "label": "supplier lifecycle risk",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 65, "comparison": "max",
        "finding": "supplier lifecycle risk exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_delivery_evidence_pct_16(record):
    """Evaluate supplier delivery evidence for control WP-0455-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_delivery_evidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-16", "metric": "supplier_delivery_evidence_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-16", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-16", "metric": "supplier_delivery_evidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-16", "metric": "supplier_delivery_evidence_pct", "label": "supplier delivery evidence",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier delivery evidence falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_support_resolution_hours_17(record):
    """Evaluate supplier support resolution for control WP-0455-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_support_resolution_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-17", "metric": "supplier_support_resolution_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-17", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-17", "metric": "supplier_support_resolution_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-17", "metric": "supplier_support_resolution_hours", "label": "supplier support resolution",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier support resolution must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_coa_accuracy_pct_18(record):
    """Evaluate supplier CoA accuracy for control WP-0455-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_coa_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-18", "metric": "supplier_coa_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-18", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-18", "metric": "supplier_coa_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-18", "metric": "supplier_coa_accuracy_pct", "label": "supplier CoA accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier CoA accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_visitor_control_pct_19(record):
    """Evaluate supplier visitor control for control WP-0455-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_visitor_control_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-19", "metric": "supplier_visitor_control_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-19", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-19", "metric": "supplier_visitor_control_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-19", "metric": "supplier_visitor_control_pct", "label": "supplier visitor control",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 85, "comparison": "max",
        "finding": "supplier visitor control exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_key_person_dependency_pct_20(record):
    """Evaluate supplier key-person dependency for control WP-0455-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_key_person_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-20", "metric": "supplier_key_person_dependency_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 70,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-20", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-20", "metric": "supplier_key_person_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 70
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-20", "metric": "supplier_key_person_dependency_pct", "label": "supplier key-person dependency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 70, "comparison": "min",
        "finding": "supplier key-person dependency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

def assess_supplier_material_restriction_gap_count_21(record):
    """Evaluate supplier material restriction gaps for control WP-0455-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_material_restriction_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-21", "metric": "supplier_material_restriction_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-21", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-21", "metric": "supplier_material_restriction_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-21", "metric": "supplier_material_restriction_gap_count", "label": "supplier material restriction gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier material restriction gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "storage capacity",
    }

def assess_supplier_ownership_review_age_days_22(record):
    """Evaluate supplier ownership review age for control WP-0455-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ownership_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-22", "metric": "supplier_ownership_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-22", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-22", "metric": "supplier_ownership_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-22", "metric": "supplier_ownership_review_age_days", "label": "supplier ownership review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier ownership review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "storage capacity",
    }

def assess_supplier_tooling_spare_pct_23(record):
    """Evaluate supplier spare tooling coverage for control WP-0455-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_tooling_spare_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-23", "metric": "supplier_tooling_spare_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 105,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-23", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-23", "metric": "supplier_tooling_spare_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 105
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-23", "metric": "supplier_tooling_spare_pct", "label": "supplier spare tooling coverage",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 105, "comparison": "max",
        "finding": "supplier spare tooling coverage exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "storage capacity",
    }

def assess_supplier_ai_governance_score_24(record):
    """Evaluate supplier AI governance for control WP-0455-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_governance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0455-24", "metric": "supplier_ai_governance_score",
            "status": "insufficient_data",
            "severity": "high", "unit": "points",
            "observed": None,
            "threshold": 19,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0455-24", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0455-24", "metric": "supplier_ai_governance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 19
    if not failed:
        return None
    return {
        "rule_id": "WP-0455-24", "metric": "supplier_ai_governance_score", "label": "supplier AI governance",
        "status": "breach", "severity": "high", "unit": "points",
        "observed": observed,
        "threshold": 19, "comparison": "min",
        "finding": "supplier AI governance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "storage capacity",
    }

RULES = (assess_sprinkler_inspection_age_days_01, assess_recipient_match_pct_02, assess_excursion_response_minutes_03, assess_product_serial_capture_pct_04, assess_ladder_inspection_age_days_05, assess_backup_power_test_age_days_06, assess_tls_error_count_07, assess_metrology_certificate_age_days_08, assess_inventory_reconciliation_age_hours_09, assess_slotting_revisit_age_days_10, assess_export_declaration_age_hours_11, assess_vehicle_capacity_overage_kg_12, assess_units_per_labor_hour_13, assess_supplier_invoice_accuracy_pct_14, assess_supplier_lifecycle_risk_score_15, assess_supplier_delivery_evidence_pct_16, assess_supplier_support_resolution_hours_17, assess_supplier_coa_accuracy_pct_18, assess_supplier_visitor_control_pct_19, assess_supplier_key_person_dependency_pct_20, assess_supplier_material_restriction_gap_count_21, assess_supplier_ownership_review_age_days_22, assess_supplier_tooling_spare_pct_23, assess_supplier_ai_governance_score_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

