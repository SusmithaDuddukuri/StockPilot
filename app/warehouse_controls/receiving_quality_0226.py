"""Operational control pack for receiving quality; rules are executable against warehouse records."""
from math import isfinite

def assess_supplier_port_dependency_pct_01(record):
    """Evaluate supplier port dependency for control WP-0226-01."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_port_dependency_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-01", "metric": "supplier_port_dependency_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-01", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-01", "metric": "supplier_port_dependency_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-01", "metric": "supplier_port_dependency_pct", "label": "supplier port dependency",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier port dependency must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_data_retention_gap_count_02(record):
    """Evaluate supplier data-retention gaps for control WP-0226-02."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_data_retention_gap_count")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-02", "metric": "supplier_data_retention_gap_count",
            "status": "insufficient_data",
            "severity": "critical", "unit": "events",
            "observed": None,
            "threshold": 83,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-02", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-02", "metric": "supplier_data_retention_gap_count", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 83
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-02", "metric": "supplier_data_retention_gap_count", "label": "supplier data-retention gaps",
        "status": "breach", "severity": "critical", "unit": "events",
        "observed": observed,
        "threshold": 83, "comparison": "max",
        "finding": "supplier data-retention gaps exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_working_capital_score_03(record):
    """Evaluate supplier working-capital score for control WP-0226-03."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_working_capital_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-03", "metric": "supplier_working_capital_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 85,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-03", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-03", "metric": "supplier_working_capital_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 85
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-03", "metric": "supplier_working_capital_score", "label": "supplier working-capital score",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 85, "comparison": "min",
        "finding": "supplier working-capital score falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_end_of_life_plan_pct_04(record):
    """Evaluate supplier end-of-life plan completeness for control WP-0226-04."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_end_of_life_plan_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-04", "metric": "supplier_end_of_life_plan_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-04", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-04", "metric": "supplier_end_of_life_plan_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-04", "metric": "supplier_end_of_life_plan_pct", "label": "supplier end-of-life plan completeness",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier end-of-life plan completeness must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_event_visibility_pct_05(record):
    """Evaluate supplier event visibility for control WP-0226-05."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_event_visibility_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-05", "metric": "supplier_event_visibility_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-05", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-05", "metric": "supplier_event_visibility_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-05", "metric": "supplier_event_visibility_pct", "label": "supplier event visibility",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier event visibility must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_measurement_calibration_pct_06(record):
    """Evaluate supplier measurement calibration for control WP-0226-06."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_measurement_calibration_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-06", "metric": "supplier_measurement_calibration_pct",
            "status": "insufficient_data",
            "severity": "critical", "unit": "percent",
            "observed": None,
            "threshold": 103,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-06", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-06", "metric": "supplier_measurement_calibration_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 103
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-06", "metric": "supplier_measurement_calibration_pct", "label": "supplier measurement calibration",
        "status": "breach", "severity": "critical", "unit": "percent",
        "observed": observed,
        "threshold": 103, "comparison": "max",
        "finding": "supplier measurement calibration exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_labor_compliance_score_07(record):
    """Evaluate supplier labor compliance for control WP-0226-07."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_labor_compliance_score")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-07", "metric": "supplier_labor_compliance_score",
            "status": "insufficient_data",
            "severity": "low", "unit": "points",
            "observed": None,
            "threshold": 34,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-07", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-07", "metric": "supplier_labor_compliance_score", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 34
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-07", "metric": "supplier_labor_compliance_score", "label": "supplier labor compliance",
        "status": "breach", "severity": "low", "unit": "points",
        "observed": observed,
        "threshold": 34, "comparison": "min",
        "finding": "supplier labor compliance falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_bankruptcy_signal_08(record):
    """Evaluate supplier bankruptcy signal for control WP-0226-08."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_bankruptcy_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-08", "metric": "supplier_bankruptcy_signal",
            "status": "insufficient_data",
            "severity": "medium", "unit": "binary",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-08", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-08", "metric": "supplier_bankruptcy_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-08", "metric": "supplier_bankruptcy_signal", "label": "supplier bankruptcy signal",
        "status": "breach", "severity": "medium", "unit": "binary",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier bankruptcy signal must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_management_review_age_days_09(record):
    """Evaluate supplier management review age for control WP-0226-09."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_management_review_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-09", "metric": "supplier_management_review_age_days",
            "status": "insufficient_data",
            "severity": "high", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-09", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-09", "metric": "supplier_management_review_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-09", "metric": "supplier_management_review_age_days", "label": "supplier management review age",
        "status": "breach", "severity": "high", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier management review age must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_ai_redteam_age_days_10(record):
    """Evaluate supplier AI red-team age for control WP-0226-10."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_ai_redteam_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-10", "metric": "supplier_ai_redteam_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 123,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-10", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-10", "metric": "supplier_ai_redteam_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 123
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-10", "metric": "supplier_ai_redteam_age_days", "label": "supplier AI red-team age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 123, "comparison": "max",
        "finding": "supplier AI red-team age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_log_redaction_pct_11(record):
    """Evaluate supplier log redaction for control WP-0226-11."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_log_redaction_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-11", "metric": "supplier_log_redaction_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 78,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-11", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-11", "metric": "supplier_log_redaction_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 78
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-11", "metric": "supplier_log_redaction_pct", "label": "supplier log redaction",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 78, "comparison": "min",
        "finding": "supplier log redaction falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_dynamic_analysis_age_days_12(record):
    """Evaluate supplier dynamic analysis age for control WP-0226-12."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_dynamic_analysis_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-12", "metric": "supplier_dynamic_analysis_age_days",
            "status": "insufficient_data",
            "severity": "medium", "unit": "days",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-12", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-12", "metric": "supplier_dynamic_analysis_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-12", "metric": "supplier_dynamic_analysis_age_days", "label": "supplier dynamic analysis age",
        "status": "breach", "severity": "medium", "unit": "days",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier dynamic analysis age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_access_certification_pct_13(record):
    """Evaluate supplier access certification for control WP-0226-13."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_access_certification_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-13", "metric": "supplier_access_certification_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-13", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-13", "metric": "supplier_access_certification_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-13", "metric": "supplier_access_certification_pct", "label": "supplier access certification",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier access certification must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_supplier_round_sum_signal_14(record):
    """Evaluate supplier round-sum signal for control WP-0226-14."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_round_sum_signal")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-14", "metric": "supplier_round_sum_signal",
            "status": "insufficient_data",
            "severity": "critical", "unit": "binary",
            "observed": None,
            "threshold": 143,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-14", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-14", "metric": "supplier_round_sum_signal", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 143
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-14", "metric": "supplier_round_sum_signal", "label": "supplier round-sum signal",
        "status": "breach", "severity": "critical", "unit": "binary",
        "observed": observed,
        "threshold": 143, "comparison": "max",
        "finding": "supplier round-sum signal exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_supplier_schedule_ack_pct_15(record):
    """Evaluate schedule acknowledgement for control WP-0226-15."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_schedule_ack_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-15", "metric": "supplier_schedule_ack_pct",
            "status": "insufficient_data",
            "severity": "low", "unit": "percent",
            "observed": None,
            "threshold": 27,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-15", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-15", "metric": "supplier_schedule_ack_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 27
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-15", "metric": "supplier_schedule_ack_pct", "label": "schedule acknowledgement",
        "status": "breach", "severity": "low", "unit": "percent",
        "observed": observed,
        "threshold": 27, "comparison": "min",
        "finding": "schedule acknowledgement falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_supplier_asn_upload_age_hours_16(record):
    """Evaluate supplier ASN upload age for control WP-0226-16."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_asn_upload_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-16", "metric": "supplier_asn_upload_age_hours",
            "status": "insufficient_data",
            "severity": "medium", "unit": "hours",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-16", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-16", "metric": "supplier_asn_upload_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-16", "metric": "supplier_asn_upload_age_hours", "label": "supplier ASN upload age",
        "status": "breach", "severity": "medium", "unit": "hours",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "supplier ASN upload age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_supplier_endpoint_cutover_pct_17(record):
    """Evaluate supplier endpoint cutover for control WP-0226-17."""
    if not isinstance(record, dict):
        return None
    raw = record.get("supplier_endpoint_cutover_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-17", "metric": "supplier_endpoint_cutover_pct",
            "status": "insufficient_data",
            "severity": "high", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-17", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-17", "metric": "supplier_endpoint_cutover_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-17", "metric": "supplier_endpoint_cutover_pct", "label": "supplier endpoint cutover",
        "status": "breach", "severity": "high", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "supplier endpoint cutover must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_order_age_hours_18(record):
    """Evaluate order age for control WP-0226-18."""
    if not isinstance(record, dict):
        return None
    raw = record.get("order_age_hours")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-18", "metric": "order_age_hours",
            "status": "insufficient_data",
            "severity": "critical", "unit": "hours",
            "observed": None,
            "threshold": 163,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-18", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-18", "metric": "order_age_hours", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 163
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-18", "metric": "order_age_hours", "label": "order age",
        "status": "breach", "severity": "critical", "unit": "hours",
        "observed": observed,
        "threshold": 163, "comparison": "max",
        "finding": "order age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_training_expiry_days_19(record):
    """Evaluate training validity for control WP-0226-19."""
    if not isinstance(record, dict):
        return None
    raw = record.get("training_expiry_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-19", "metric": "training_expiry_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 71,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-19", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-19", "metric": "training_expiry_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 71
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-19", "metric": "training_expiry_days", "label": "training validity",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 71, "comparison": "min",
        "finding": "training validity falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_lot_traceability_pct_20(record):
    """Evaluate lot traceability for control WP-0226-20."""
    if not isinstance(record, dict):
        return None
    raw = record.get("lot_traceability_pct")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-20", "metric": "lot_traceability_pct",
            "status": "insufficient_data",
            "severity": "medium", "unit": "percent",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-20", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-20", "metric": "lot_traceability_pct", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-20", "metric": "lot_traceability_pct", "label": "lot traceability",
        "status": "breach", "severity": "medium", "unit": "percent",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "lot traceability must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

def assess_backorder_units_21(record):
    """Evaluate backordered units for control WP-0226-21."""
    if not isinstance(record, dict):
        return None
    raw = record.get("backorder_units")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-21", "metric": "backorder_units",
            "status": "insufficient_data",
            "severity": "high", "unit": "units",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-21", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-21", "metric": "backorder_units", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed != 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-21", "metric": "backorder_units", "label": "backordered units",
        "status": "breach", "severity": "high", "unit": "units",
        "observed": observed,
        "threshold": 0, "comparison": "zero",
        "finding": "backordered units must be reconciled to zero.",
        "recommendation": "Reconcile source records and approve any adjustment.",
        "scope": "receiving quality",
    }

def assess_vehicle_inspection_age_days_22(record):
    """Evaluate vehicle inspection age for control WP-0226-22."""
    if not isinstance(record, dict):
        return None
    raw = record.get("vehicle_inspection_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-22", "metric": "vehicle_inspection_age_days",
            "status": "insufficient_data",
            "severity": "critical", "unit": "days",
            "observed": None,
            "threshold": 183,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-22", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-22", "metric": "vehicle_inspection_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed > 183
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-22", "metric": "vehicle_inspection_age_days", "label": "vehicle inspection age",
        "status": "breach", "severity": "critical", "unit": "days",
        "observed": observed,
        "threshold": 183, "comparison": "max",
        "finding": "vehicle inspection age exceeds the control ceiling.",
        "recommendation": "Reduce exposure or initiate corrective action.",
        "scope": "receiving quality",
    }

def assess_credential_rotation_age_days_23(record):
    """Evaluate credential rotation age for control WP-0226-23."""
    if not isinstance(record, dict):
        return None
    raw = record.get("credential_rotation_age_days")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-23", "metric": "credential_rotation_age_days",
            "status": "insufficient_data",
            "severity": "low", "unit": "days",
            "observed": None,
            "threshold": 20,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-23", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-23", "metric": "credential_rotation_age_days", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed < 20
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-23", "metric": "credential_rotation_age_days", "label": "credential rotation age",
        "status": "breach", "severity": "low", "unit": "days",
        "observed": observed,
        "threshold": 20, "comparison": "min",
        "finding": "credential rotation age falls below the control floor.",
        "recommendation": "Increase the value or review the process.",
        "scope": "receiving quality",
    }

def assess_work_queue_age_minutes_24(record):
    """Evaluate work queue age for control WP-0226-24."""
    if not isinstance(record, dict):
        return None
    raw = record.get("work_queue_age_minutes")
    if raw is None or raw == "":
        return {
            "rule_id": "WP-0226-24", "metric": "work_queue_age_minutes",
            "status": "insufficient_data",
            "severity": "medium", "unit": "minutes",
            "observed": None,
            "threshold": 0,
            "recommendation": "Capture the metric before this control can be cleared.",
        }
    try:
        observed = float(raw)
    except (TypeError, ValueError, OverflowError):
        return {"rule_id": "WP-0226-24", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    if not isfinite(observed):
        return {"rule_id": "WP-0226-24", "metric": "work_queue_age_minutes", "status": "invalid_data", "observed": str(raw)[:80]}
    failed = observed <= 0
    if not failed:
        return None
    return {
        "rule_id": "WP-0226-24", "metric": "work_queue_age_minutes", "label": "work queue age",
        "status": "breach", "severity": "medium", "unit": "minutes",
        "observed": observed,
        "threshold": 0, "comparison": "positive",
        "finding": "work queue age must be greater than zero.",
        "recommendation": "Confirm the measurement and restore a valid positive value.",
        "scope": "receiving quality",
    }

RULES = (assess_supplier_port_dependency_pct_01, assess_supplier_data_retention_gap_count_02, assess_supplier_working_capital_score_03, assess_supplier_end_of_life_plan_pct_04, assess_supplier_event_visibility_pct_05, assess_supplier_measurement_calibration_pct_06, assess_supplier_labor_compliance_score_07, assess_supplier_bankruptcy_signal_08, assess_supplier_management_review_age_days_09, assess_supplier_ai_redteam_age_days_10, assess_supplier_log_redaction_pct_11, assess_supplier_dynamic_analysis_age_days_12, assess_supplier_access_certification_pct_13, assess_supplier_round_sum_signal_14, assess_supplier_schedule_ack_pct_15, assess_supplier_asn_upload_age_hours_16, assess_supplier_endpoint_cutover_pct_17, assess_order_age_hours_18, assess_training_expiry_days_19, assess_lot_traceability_pct_20, assess_backorder_units_21, assess_vehicle_inspection_age_days_22, assess_credential_rotation_age_days_23, assess_work_queue_age_minutes_24,)

def evaluate(record):
    """Run this pack against one record and return every triggered control."""
    findings = []
    for rule in RULES:
        result = rule(record)
        if result is not None:
            findings.append(result)
    return findings

