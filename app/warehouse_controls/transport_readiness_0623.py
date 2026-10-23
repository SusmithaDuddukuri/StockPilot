"""Operational control pack for transport readiness; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_service_account_review_age_days_01(record):
    """Evaluate supplier service-account review age for control WP-0623-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_service_account_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-01", "metric": "supplier_service_account_review_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-01", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-01", "metric": "supplier_service_account_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-01", "metric": "supplier_service_account_review_age_days", "label": "supplier service-account review age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier service-account review age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_privacy_training_pct_02(record):
    """Evaluate supplier privacy training for control WP-0623-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_privacy_training_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-02", "metric": "supplier_privacy_training_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-02", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-02", "metric": "supplier_privacy_training_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-02", "metric": "supplier_privacy_training_pct", "label": "supplier privacy training",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier privacy training must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_supplier_evidence_integrity_pct_03(record):
    """Evaluate supplier evidence integrity for control WP-0623-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_evidence_integrity_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-03", "metric": "supplier_evidence_integrity_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 29,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-03", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-03", "metric": "supplier_evidence_integrity_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 29
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-03", "metric": "supplier_evidence_integrity_pct", "label": "supplier evidence integrity",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 29, "comparison": "max",
        "finding": "supplier evidence integrity exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_supplier_volume_commitment_pct_04(record):
    """Evaluate supplier volume commitment for control WP-0623-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_volume_commitment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-04", "metric": "supplier_volume_commitment_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 25,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-04", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-04", "metric": "supplier_volume_commitment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 25
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-04", "metric": "supplier_volume_commitment_pct", "label": "supplier volume commitment",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 25, "comparison": "min",
        "finding": "supplier volume commitment falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_supplier_shipping_accuracy_pct_05(record):
    """Evaluate supplier shipping accuracy for control WP-0623-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_shipping_accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-05", "metric": "supplier_shipping_accuracy_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-05", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-05", "metric": "supplier_shipping_accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-05", "metric": "supplier_shipping_accuracy_pct", "label": "supplier shipping accuracy",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier shipping accuracy must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_open_order_transfer_pct_06(record):
    """Evaluate open-order transfer completeness for control WP-0623-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_open_order_transfer_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-06", "metric": "supplier_open_order_transfer_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-06", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-06", "metric": "supplier_open_order_transfer_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-06", "metric": "supplier_open_order_transfer_pct", "label": "open-order transfer completeness",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "open-order transfer completeness must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_lead_days_07(record):
    """Evaluate supplier lead time for control WP-0623-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lead_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-07", "metric": "lead_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 49,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-07", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-07", "metric": "lead_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 49
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-07", "metric": "lead_days", "label": "supplier lead time",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 49, "comparison": "max",
        "finding": "supplier lead time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_carbon_kg_08(record):
    """Evaluate carbon estimate for control WP-0623-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carbon_kg")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-08", "metric": "carbon_kg",
            "status": "insufficient_data",
            "severity": "high", "unit": "kg",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-08", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-08", "metric": "carbon_kg", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-08", "metric": "carbon_kg", "label": "carbon estimate",
        "status": "breach", "severity": "high", "unit": "kg",
        "observed": observed,
        "threshold": 69, "comparison": "min",
        "finding": "carbon estimate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_forecast_confidence_pct_09(record):
    """Evaluate forecast confidence for control WP-0623-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_confidence_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-09", "metric": "forecast_confidence_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-09", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-09", "metric": "forecast_confidence_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-09", "metric": "forecast_confidence_pct", "label": "forecast confidence",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "forecast confidence must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_orphan_receipt_count_10(record):
    """Evaluate orphan receipts for control WP-0623-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("orphan_receipt_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-10", "metric": "orphan_receipt_count",
            "status": "insufficient_data",
            "severity": "low", "unit": "records",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-10", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-10", "metric": "orphan_receipt_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-10", "metric": "orphan_receipt_count", "label": "orphan receipts",
        "status": "breach", "severity": "low", "unit": "records",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "orphan receipts must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_recovery_value_pct_11(record):
    """Evaluate recovery value for control WP-0623-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recovery_value_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-11", "metric": "recovery_value_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 69,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-11", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-11", "metric": "recovery_value_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 69
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-11", "metric": "recovery_value_pct", "label": "recovery value",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 69, "comparison": "max",
        "finding": "recovery value exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_serial_mismatch_count_12(record):
    """Evaluate serial mismatches for control WP-0623-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("serial_mismatch_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-12", "metric": "serial_mismatch_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 18,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-12", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-12", "metric": "serial_mismatch_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 18
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-12", "metric": "serial_mismatch_count", "label": "serial mismatches",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 18, "comparison": "min",
        "finding": "serial mismatches falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_integration_failure_count_13(record):
    """Evaluate integration failures for control WP-0623-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("integration_failure_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-13", "metric": "integration_failure_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-13", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-13", "metric": "integration_failure_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-13", "metric": "integration_failure_count", "label": "integration failures",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "integration failures must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_carton_fill_pct_14(record):
    """Evaluate carton fill for control WP-0623-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("carton_fill_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-14", "metric": "carton_fill_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-14", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-14", "metric": "carton_fill_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-14", "metric": "carton_fill_pct", "label": "carton fill",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "carton fill must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_dispute_age_days_15(record):
    """Evaluate dispute age for control WP-0623-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dispute_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-15", "metric": "dispute_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 89,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-15", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-15", "metric": "dispute_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 89
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-15", "metric": "dispute_age_days", "label": "dispute age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 89, "comparison": "max",
        "finding": "dispute age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_reefer_fuel_remaining_pct_16(record):
    """Evaluate reefer fuel remaining for control WP-0623-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("reefer_fuel_remaining_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-16", "metric": "reefer_fuel_remaining_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 62,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-16", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-16", "metric": "reefer_fuel_remaining_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 62
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-16", "metric": "reefer_fuel_remaining_pct", "label": "reefer fuel remaining",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 62, "comparison": "min",
        "finding": "reefer fuel remaining falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_refurbishment_yield_pct_17(record):
    """Evaluate refurbishment yield for control WP-0623-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("refurbishment_yield_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-17", "metric": "refurbishment_yield_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-17", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-17", "metric": "refurbishment_yield_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-17", "metric": "refurbishment_yield_pct", "label": "refurbishment yield",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "refurbishment yield must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_rack_load_variance_pct_18(record):
    """Evaluate rack load variance for control WP-0623-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rack_load_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-18", "metric": "rack_load_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-18", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-18", "metric": "rack_load_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-18", "metric": "rack_load_variance_pct", "label": "rack load variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "rack load variance must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_robot_pick_success_pct_19(record):
    """Evaluate robot pick success for control WP-0623-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("robot_pick_success_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-19", "metric": "robot_pick_success_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 109,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-19", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-19", "metric": "robot_pick_success_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 109
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-19", "metric": "robot_pick_success_pct", "label": "robot pick success",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 109, "comparison": "max",
        "finding": "robot pick success exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_alert_noise_pct_20(record):
    """Evaluate alert noise rate for control WP-0623-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("alert_noise_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-20", "metric": "alert_noise_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 11,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-20", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-20", "metric": "alert_noise_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 11
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-20", "metric": "alert_noise_pct", "label": "alert noise rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 11, "comparison": "min",
        "finding": "alert noise rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

def assess_scanner_firmware_age_days_21(record):
    """Evaluate scanner firmware age for control WP-0623-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("scanner_firmware_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-21", "metric": "scanner_firmware_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-21", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-21", "metric": "scanner_firmware_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-21", "metric": "scanner_firmware_age_days", "label": "scanner firmware age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "scanner firmware age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "transport readiness",
    }

def assess_supplier_contact_valid_pct_22(record):
    """Evaluate supplier contact validity for control WP-0623-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_contact_valid_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-22", "metric": "supplier_contact_valid_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-22", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-22", "metric": "supplier_contact_valid_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-22", "metric": "supplier_contact_valid_pct", "label": "supplier contact validity",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier contact validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "transport readiness",
    }

def assess_inspection_cycle_minutes_23(record):
    """Evaluate inspection cycle time for control WP-0623-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("inspection_cycle_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-23", "metric": "inspection_cycle_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 129,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-23", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-23", "metric": "inspection_cycle_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 129
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-23", "metric": "inspection_cycle_minutes", "label": "inspection cycle time",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 129, "comparison": "max",
        "finding": "inspection cycle time exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "transport readiness",
    }

def assess_order_amendment_count_24(record):
    """Evaluate order amendments for control WP-0623-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_amendment_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0623-24", "metric": "order_amendment_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "events",
            "observed": None,
            "threshold": 55,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0623-24", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0623-24", "metric": "order_amendment_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 55
    if not failed:
        return None
    return {
        "rule_id": "WP-0623-24", "metric": "order_amendment_count", "label": "order amendments",
        "status": "breach", "severity": "high", "unit": "events",
        "observed": observed,
        "threshold": 55, "comparison": "min",
        "finding": "order amendments falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "transport readiness",
    }

RULES = (assess_supplier_service_account_review_age_days_01, assess_supplier_privacy_training_pct_02, assess_supplier_evidence_integrity_pct_03, assess_supplier_volume_commitment_pct_04, assess_supplier_shipping_accuracy_pct_05, assess_supplier_open_order_transfer_pct_06, assess_lead_days_07, assess_carbon_kg_08, assess_forecast_confidence_pct_09, assess_orphan_receipt_count_10, assess_recovery_value_pct_11, assess_serial_mismatch_count_12, assess_integration_failure_count_13, assess_carton_fill_pct_14, assess_dispute_age_days_15, assess_reefer_fuel_remaining_pct_16, assess_refurbishment_yield_pct_17, assess_rack_load_variance_pct_18, assess_robot_pick_success_pct_19, assess_alert_noise_pct_20, assess_scanner_firmware_age_days_21, assess_supplier_contact_valid_pct_22, assess_inspection_cycle_minutes_23, assess_order_amendment_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

