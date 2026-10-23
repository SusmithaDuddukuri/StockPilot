"""Operational control pack for cycle counting; rules are executable against warehouse records."""
from math import isfinite

def assess_accuracy_pct_01(record):
    """Evaluate inventory accuracy for control WP-0634-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("accuracy_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-01", "metric": "accuracy_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-01", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-01", "metric": "accuracy_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-01", "metric": "accuracy_pct", "label": "inventory accuracy",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "inventory accuracy must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_fraud_signal_score_02(record):
    """Evaluate fraud signal score for control WP-0634-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("fraud_signal_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-02", "metric": "fraud_signal_score",
            "status": "insufficient_data",
            "severity": "critical", "unit": "points",
            "observed": None,
            "threshold": 167,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-02", "metric": "fraud_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-02", "metric": "fraud_signal_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 167
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-02", "metric": "fraud_signal_score", "label": "fraud signal score",
        "status": "breach", "severity": "critical", "unit": "points",
        "observed": observed,
        "threshold": 167, "comparison": "max",
        "finding": "fraud signal score exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_partial_shipment_pct_03(record):
    """Evaluate partial shipment rate for control WP-0634-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("partial_shipment_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-03", "metric": "partial_shipment_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 91,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-03", "metric": "partial_shipment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-03", "metric": "partial_shipment_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 91
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-03", "metric": "partial_shipment_pct", "label": "partial shipment rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 91, "comparison": "min",
        "finding": "partial shipment rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_pallet_stability_score_04(record):
    """Evaluate pallet stability for control WP-0634-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("pallet_stability_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-04", "metric": "pallet_stability_score",
            "status": "insufficient_data",
            "severity": "medium", "unit": "points",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-04", "metric": "pallet_stability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-04", "metric": "pallet_stability_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-04", "metric": "pallet_stability_score", "label": "pallet stability",
        "status": "breach", "severity": "medium", "unit": "points",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "pallet stability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_restricted_item_count_05(record):
    """Evaluate restricted items for control WP-0634-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("restricted_item_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-05", "metric": "restricted_item_count",
            "status": "insufficient_data",
            "severity": "high", "unit": "items",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-05", "metric": "restricted_item_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-05", "metric": "restricted_item_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-05", "metric": "restricted_item_count", "label": "restricted items",
        "status": "breach", "severity": "high", "unit": "items",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "restricted items must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_incident_ack_minutes_06(record):
    """Evaluate incident acknowledgement for control WP-0634-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("incident_ack_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-06", "metric": "incident_ack_minutes",
            "status": "insufficient_data",
            "severity": "critical", "unit": "minutes",
            "observed": None,
            "threshold": 187,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-06", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-06", "metric": "incident_ack_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 187
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-06", "metric": "incident_ack_minutes", "label": "incident acknowledgement",
        "status": "breach", "severity": "critical", "unit": "minutes",
        "observed": observed,
        "threshold": 187, "comparison": "max",
        "finding": "incident acknowledgement exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_forecast_bias_pct_07(record):
    """Evaluate forecast bias for control WP-0634-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("forecast_bias_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-07", "metric": "forecast_bias_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 40,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-07", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-07", "metric": "forecast_bias_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 40
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-07", "metric": "forecast_bias_pct", "label": "forecast bias",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 40, "comparison": "min",
        "finding": "forecast bias falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_cold_exposure_minutes_08(record):
    """Evaluate cold exposure for control WP-0634-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("cold_exposure_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-08", "metric": "cold_exposure_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-08", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-08", "metric": "cold_exposure_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-08", "metric": "cold_exposure_minutes", "label": "cold exposure",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "cold exposure must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_credit_age_days_09(record):
    """Evaluate supplier credit age for control WP-0634-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_credit_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-09", "metric": "supplier_credit_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-09", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-09", "metric": "supplier_credit_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-09", "metric": "supplier_credit_age_days", "label": "supplier credit age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier credit age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_recall_drill_age_days_10(record):
    """Evaluate recall drill age for control WP-0634-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("recall_drill_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-10", "metric": "recall_drill_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-10", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-10", "metric": "recall_drill_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-10", "metric": "recall_drill_age_days", "label": "recall drill age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 27, "comparison": "max",
        "finding": "recall drill age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_dangerous_goods_declaration_pct_11(record):
    """Evaluate dangerous goods declaration for control WP-0634-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("dangerous_goods_declaration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-11", "metric": "dangerous_goods_declaration_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 84,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-11", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-11", "metric": "dangerous_goods_declaration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 84
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-11", "metric": "dangerous_goods_declaration_pct", "label": "dangerous goods declaration",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 84, "comparison": "min",
        "finding": "dangerous goods declaration falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_safety_walk_age_days_12(record):
    """Evaluate safety walk age for control WP-0634-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("safety_walk_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-12", "metric": "safety_walk_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-12", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-12", "metric": "safety_walk_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-12", "metric": "safety_walk_age_days", "label": "safety walk age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "safety walk age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_emergency_alarm_test_age_days_13(record):
    """Evaluate emergency alarm test age for control WP-0634-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("emergency_alarm_test_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-13", "metric": "emergency_alarm_test_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-13", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-13", "metric": "emergency_alarm_test_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-13", "metric": "emergency_alarm_test_age_days", "label": "emergency alarm test age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "emergency alarm test age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_software_bill_of_materials_age_days_14(record):
    """Evaluate SBOM age for control WP-0634-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("software_bill_of_materials_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-14", "metric": "software_bill_of_materials_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 47,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-14", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-14", "metric": "software_bill_of_materials_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 47
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-14", "metric": "software_bill_of_materials_age_days", "label": "SBOM age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 47, "comparison": "max",
        "finding": "SBOM age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_rfid_read_rate_pct_15(record):
    """Evaluate RFID read rate for control WP-0634-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("rfid_read_rate_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-15", "metric": "rfid_read_rate_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 33,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-15", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-15", "metric": "rfid_read_rate_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 33
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-15", "metric": "rfid_read_rate_pct", "label": "RFID read rate",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 33, "comparison": "min",
        "finding": "RFID read rate falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_stock_age_median_days_16(record):
    """Evaluate median stock age for control WP-0634-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("stock_age_median_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-16", "metric": "stock_age_median_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-16", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-16", "metric": "stock_age_median_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-16", "metric": "stock_age_median_days", "label": "median stock age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "median stock age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_packaging_damage_pct_17(record):
    """Evaluate packaging damage rate for control WP-0634-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("packaging_damage_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-17", "metric": "packaging_damage_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-17", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-17", "metric": "packaging_damage_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-17", "metric": "packaging_damage_pct", "label": "packaging damage rate",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "packaging damage rate must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_sanctions_screen_gap_count_18(record):
    """Evaluate sanctions screening gaps for control WP-0634-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("sanctions_screen_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-18", "metric": "sanctions_screen_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 67,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-18", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-18", "metric": "sanctions_screen_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 67
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-18", "metric": "sanctions_screen_gap_count", "label": "sanctions screening gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 67, "comparison": "max",
        "finding": "sanctions screening gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_driver_training_age_days_19(record):
    """Evaluate driver training age for control WP-0634-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("driver_training_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-19", "metric": "driver_training_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 77,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-19", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-19", "metric": "driver_training_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 77
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-19", "metric": "driver_training_age_days", "label": "driver training age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 77, "comparison": "min",
        "finding": "driver training age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_automation_roi_pct_20(record):
    """Evaluate automation ROI for control WP-0634-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("automation_roi_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-20", "metric": "automation_roi_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-20", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-20", "metric": "automation_roi_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-20", "metric": "automation_roi_pct", "label": "automation ROI",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "automation ROI must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

def assess_supplier_license_days_left_21(record):
    """Evaluate supplier license validity for control WP-0634-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_license_days_left")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-21", "metric": "supplier_license_days_left",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-21", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-21", "metric": "supplier_license_days_left", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-21", "metric": "supplier_license_days_left", "label": "supplier license validity",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier license validity must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "cycle counting",
    }

def assess_supplier_root_cause_completeness_pct_22(record):
    """Evaluate supplier root-cause completeness for control WP-0634-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_root_cause_completeness_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-22", "metric": "supplier_root_cause_completeness_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 87,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-22", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-22", "metric": "supplier_root_cause_completeness_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 87
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-22", "metric": "supplier_root_cause_completeness_pct", "label": "supplier root-cause completeness",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 87, "comparison": "max",
        "finding": "supplier root-cause completeness exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "cycle counting",
    }

def assess_supplier_indexation_variance_pct_23(record):
    """Evaluate supplier indexation variance for control WP-0634-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_indexation_variance_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-23", "metric": "supplier_indexation_variance_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 26,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-23", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-23", "metric": "supplier_indexation_variance_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 26
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-23", "metric": "supplier_indexation_variance_pct", "label": "supplier indexation variance",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 26, "comparison": "min",
        "finding": "supplier indexation variance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "cycle counting",
    }

def assess_supplier_document_version_gap_count_24(record):
    """Evaluate supplier document-version gaps for control WP-0634-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_document_version_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0634-24", "metric": "supplier_document_version_gap_count",
            "status": "insufficient_data",
            "severity": "medium", "unit": "events",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0634-24", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0634-24", "metric": "supplier_document_version_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0634-24", "metric": "supplier_document_version_gap_count", "label": "supplier document-version gaps",
        "status": "breach", "severity": "medium", "unit": "events",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier document-version gaps must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "cycle counting",
    }

RULES = (assess_accuracy_pct_01, assess_fraud_signal_score_02, assess_partial_shipment_pct_03, assess_pallet_stability_score_04, assess_restricted_item_count_05, assess_incident_ack_minutes_06, assess_forecast_bias_pct_07, assess_cold_exposure_minutes_08, assess_supplier_credit_age_days_09, assess_recall_drill_age_days_10, assess_dangerous_goods_declaration_pct_11, assess_safety_walk_age_days_12, assess_emergency_alarm_test_age_days_13, assess_software_bill_of_materials_age_days_14, assess_rfid_read_rate_pct_15, assess_stock_age_median_days_16, assess_packaging_damage_pct_17, assess_sanctions_screen_gap_count_18, assess_driver_training_age_days_19, assess_automation_roi_pct_20, assess_supplier_license_days_left_21, assess_supplier_root_cause_completeness_pct_22, assess_supplier_indexation_variance_pct_23, assess_supplier_document_version_gap_count_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

