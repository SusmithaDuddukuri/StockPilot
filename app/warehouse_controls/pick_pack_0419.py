"""Operational control pack for pick and pack; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_runbook_age_days_01(record):
    """Evaluate supplier runbook age for control WP-0419-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_runbook_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-01", "metric": "supplier_runbook_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-01", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-01", "metric": "supplier_runbook_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-01", "metric": "supplier_runbook_age_days", "label": "supplier runbook age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier runbook age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_country_label_pct_02(record):
    """Evaluate supplier country-label compliance for control WP-0419-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_country_label_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-02", "metric": "supplier_country_label_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-02", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-02", "metric": "supplier_country_label_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-02", "metric": "supplier_country_label_pct", "label": "supplier country-label compliance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier country-label compliance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_driver_briefing_pct_03(record):
    """Evaluate supplier driver briefing completion for control WP-0419-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_driver_briefing_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-03", "metric": "supplier_driver_briefing_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-03", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-03", "metric": "supplier_driver_briefing_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-03", "metric": "supplier_driver_briefing_pct", "label": "supplier driver briefing completion",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 77, "comparison": "max",
        "finding": "supplier driver briefing completion exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_process_change_approval_pct_04(record):
    """Evaluate supplier process-change approval for control WP-0419-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_process_change_approval_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-04", "metric": "supplier_process_change_approval_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 22,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-04", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-04", "metric": "supplier_process_change_approval_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 22
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-04", "metric": "supplier_process_change_approval_pct", "label": "supplier process-change approval",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 22, "comparison": "min",
        "finding": "supplier process-change approval falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_waste_transport_license_days_05(record):
    """Evaluate supplier waste transport license validity for control WP-0419-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_waste_transport_license_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-05", "metric": "supplier_waste_transport_license_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-05", "metric": "supplier_waste_transport_license_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-05", "metric": "supplier_waste_transport_license_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-05", "metric": "supplier_waste_transport_license_days", "label": "supplier waste transport license validity",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier waste transport license validity must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_duplicate_payment_count_06(record):
    """Evaluate supplier duplicate payments for control WP-0419-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_duplicate_payment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-06", "metric": "supplier_duplicate_payment_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-06", "metric": "supplier_duplicate_payment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-06", "metric": "supplier_duplicate_payment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-06", "metric": "supplier_duplicate_payment_count", "label": "supplier duplicate payments",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier duplicate payments must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_critical_staff_backup_pct_07(record):
    """Evaluate supplier critical staff backup for control WP-0419-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_critical_staff_backup_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-07", "metric": "supplier_critical_staff_backup_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 97,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-07", "metric": "supplier_critical_staff_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-07", "metric": "supplier_critical_staff_backup_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 97
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-07", "metric": "supplier_critical_staff_backup_pct", "label": "supplier critical staff backup",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 97, "comparison": "max",
        "finding": "supplier critical staff backup exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_prediction_latency_ms_08(record):
    """Evaluate supplier prediction latency for control WP-0419-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_prediction_latency_ms")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-08", "metric": "supplier_prediction_latency_ms",
            "status": "insufficient_data",
            "severity": "high", "unit": "ms",
            "observed": None,
            "threshold": 66,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-08", "metric": "supplier_prediction_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-08", "metric": "supplier_prediction_latency_ms", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 66
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-08", "metric": "supplier_prediction_latency_ms", "label": "supplier prediction latency",
        "status": "breach", "severity": "high", "unit": "ms",
        "observed": observed,
        "threshold": 66, "comparison": "min",
        "finding": "supplier prediction latency falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_data_contract_violation_count_09(record):
    """Evaluate supplier data-contract violations for control WP-0419-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_contract_violation_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-09", "metric": "supplier_data_contract_violation_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-09", "metric": "supplier_data_contract_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-09", "metric": "supplier_data_contract_violation_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-09", "metric": "supplier_data_contract_violation_count", "label": "supplier data-contract violations",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier data-contract violations must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_service_account_review_age_days_10(record):
    """Evaluate supplier service-account review age for control WP-0419-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_account_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-10", "metric": "supplier_service_account_review_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-10", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-10", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-10", "metric": "supplier_service_account_review_age_days", "label": "supplier service-account review age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier service-account review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_privacy_training_pct_11(record):
    """Evaluate supplier privacy training for control WP-0419-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-11", "metric": "supplier_privacy_training_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 117,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-11", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-11", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 117
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-11", "metric": "supplier_privacy_training_pct", "label": "supplier privacy training",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 117, "comparison": "max",
        "finding": "supplier privacy training exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_supplier_evidence_integrity_pct_12(record):
    """Evaluate supplier evidence integrity for control WP-0419-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-12", "metric": "supplier_evidence_integrity_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 15,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-12", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-12", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 15
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-12", "metric": "supplier_evidence_integrity_pct", "label": "supplier evidence integrity",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 15, "comparison": "min",
        "finding": "supplier evidence integrity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_supplier_volume_commitment_pct_13(record):
    """Evaluate supplier volume commitment for control WP-0419-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_volume_commitment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-13", "metric": "supplier_volume_commitment_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-13", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-13", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-13", "metric": "supplier_volume_commitment_pct", "label": "supplier volume commitment",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier volume commitment must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_supplier_shipping_accuracy_pct_14(record):
    """Evaluate supplier shipping accuracy for control WP-0419-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-14", "metric": "supplier_shipping_accuracy_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-14", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-14", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-14", "metric": "supplier_shipping_accuracy_pct", "label": "supplier shipping accuracy",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier shipping accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_supplier_open_order_transfer_pct_15(record):
    """Evaluate open-order transfer completeness for control WP-0419-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_order_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-15", "metric": "supplier_open_order_transfer_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 137,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-15", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-15", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 137
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-15", "metric": "supplier_open_order_transfer_pct", "label": "open-order transfer completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 137, "comparison": "max",
        "finding": "open-order transfer completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_lead_days_16(record):
    """Evaluate supplier lead time for control WP-0419-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-16", "metric": "lead_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 59,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-16", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-16", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 59
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-16", "metric": "lead_days", "label": "supplier lead time",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 59, "comparison": "min",
        "finding": "supplier lead time falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_carbon_kg_17(record):
    """Evaluate carbon estimate for control WP-0419-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carbon_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-17", "metric": "carbon_kg",
            "status": "insufficient_data",
            "severity": "critical", "unit": "kg",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-17", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-17", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-17", "metric": "carbon_kg", "label": "carbon estimate",
        "status": "breach", "severity": "critical", "unit": "kg",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "carbon estimate must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_forecast_confidence_pct_18(record):
    """Evaluate forecast confidence for control WP-0419-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-18", "metric": "forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-18", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-18", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-18", "metric": "forecast_confidence_pct", "label": "forecast confidence",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "forecast confidence must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_orphan_receipt_count_19(record):
    """Evaluate orphan receipts for control WP-0419-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-19", "metric": "orphan_receipt_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "records",
            "observed": None,
            "threshold": 157,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-19", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-19", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 157
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-19", "metric": "orphan_receipt_count", "label": "orphan receipts",
        "status": "breach", "severity": "medium", "unit": "records",
        "observed": observed,
        "threshold": 157, "comparison": "max",
        "finding": "orphan receipts exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_recovery_value_pct_20(record):
    """Evaluate recovery value for control WP-0419-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_value_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-20", "metric": "recovery_value_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 8,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-20", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-20", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 8
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-20", "metric": "recovery_value_pct", "label": "recovery value",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 8, "comparison": "min",
        "finding": "recovery value falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

def assess_serial_mismatch_count_21(record):
    """Evaluate serial mismatches for control WP-0419-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-21", "metric": "serial_mismatch_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-21", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-21", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-21", "metric": "serial_mismatch_count", "label": "serial mismatches",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "serial mismatches must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "pick and pack",
    }

def assess_integration_failure_count_22(record):
    """Evaluate integration failures for control WP-0419-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("integration_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-22", "metric": "integration_failure_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-22", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-22", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-22", "metric": "integration_failure_count", "label": "integration failures",
        "status": "breach", "severity": "low", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "integration failures must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "pick and pack",
    }

def assess_carton_fill_pct_23(record):
    """Evaluate carton fill for control WP-0419-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carton_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-23", "metric": "carton_fill_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 177,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-23", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-23", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 177
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-23", "metric": "carton_fill_pct", "label": "carton fill",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 177, "comparison": "max",
        "finding": "carton fill exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "pick and pack",
    }

def assess_dispute_age_days_24(record):
    """Evaluate dispute age for control WP-0419-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0419-24", "metric": "dispute_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 52,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0419-24", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0419-24", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 52
    if not failed:
        return None
    return {
        "rule_id": "WP-0419-24", "metric": "dispute_age_days", "label": "dispute age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 52, "comparison": "min",
        "finding": "dispute age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "pick and pack",
    }

RULES = (assess_supplier_runbook_age_days_01, assess_supplier_country_label_pct_02, assess_supplier_driver_briefing_pct_03, assess_supplier_process_change_approval_pct_04, assess_supplier_waste_transport_license_days_05, assess_supplier_duplicate_payment_count_06, assess_supplier_critical_staff_backup_pct_07, assess_supplier_prediction_latency_ms_08, assess_supplier_data_contract_violation_count_09, assess_supplier_service_account_review_age_days_10, assess_supplier_privacy_training_pct_11, assess_supplier_evidence_integrity_pct_12, assess_supplier_volume_commitment_pct_13, assess_supplier_shipping_accuracy_pct_14, assess_supplier_open_order_transfer_pct_15, assess_lead_days_16, assess_carbon_kg_17, assess_forecast_confidence_pct_18, assess_orphan_receipt_count_19, assess_recovery_value_pct_20, assess_serial_mismatch_count_21, assess_integration_failure_count_22, assess_carton_fill_pct_23, assess_dispute_age_days_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

