from app.services.policy_engine import evaluate_records, list_packs


def test_policy_catalog_is_paginated_and_reports_total():
    result = list_packs(offset=0, limit=3)
    assert result["total_packs"] == 700
    assert len(result["packs"]) == 3
    assert result["packs"][0]["rule_count"] == 24


def test_policy_engine_reports_threshold_breach():
    result = evaluate_records(1, [{"return_rate_pct": 80}])
    assert result["records_evaluated"] == 1
    assert result["findings_count"] > 0
    assert any(item["rule_id"] == "WP-0001-01" and item["status"] == "breach"
               for item in result["prioritized_findings"])


def test_policy_engine_rejects_invalid_pack_and_oversized_batch():
    try:
        evaluate_records(701, [])
    except ValueError:
        pass
    else:
        raise AssertionError("out-of-range pack ID should be rejected")
    try:
        evaluate_records(1, [{}] * 201)
    except ValueError:
        pass
    else:
        raise AssertionError("batches over 200 records should be rejected")
