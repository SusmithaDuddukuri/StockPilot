import pytest
from app.services.validation import ValidationError
from app.services.warehouse_intelligence import (
    warehouse_capacity, slotting_recommendations, build_pick_waves,
    cycle_count_variances, inventory_health_score, supplier_lead_time_summary,
    replenishment_batch,
)


def test_capacity_reports_overflow_and_totals():
    result = warehouse_capacity([
        {'location': 'A-01', 'capacity_units': 10, 'on_hand': 12},
        {'location': 'B-01', 'capacity_units': 20, 'on_hand': 10},
    ])
    assert result['total_capacity_units'] == 30
    assert result['total_occupied_units'] == 22
    assert result['over_capacity_locations'] == 1
    assert result['locations'][0]['location'] == 'A-01'


def test_capacity_rejects_duplicate_locations():
    with pytest.raises(ValidationError):
        warehouse_capacity([
            {'location': 'A-01', 'capacity_units': 10, 'on_hand': 1},
            {'location': 'a-01', 'capacity_units': 10, 'on_hand': 2},
        ])


def test_slotting_prioritizes_fast_movers():
    rows = slotting_recommendations([
        {'sku': 'SLOW-01', 'average_daily_demand': 0, 'quantity': 10},
        {'sku': 'FAST-01', 'average_daily_demand': 12, 'quantity': 30},
    ])
    assert rows[0]['sku'] == 'FAST-01'
    assert rows[0]['recommended_zone'] == 'Forward pick'


def test_pick_waves_preserve_every_line_and_obey_limits():
    lines = [
        {'order_id': 'O-1', 'sku': 'SKU-1', 'quantity': 4, 'location': 'A'},
        {'order_id': 'O-2', 'sku': 'SKU-2', 'quantity': 4, 'location': 'B'},
        {'order_id': 'O-3', 'sku': 'SKU-3', 'quantity': 4, 'location': 'C'},
    ]
    result = build_pick_waves(lines, max_lines=2, max_units=8)
    assert result['line_count'] == 3
    assert result['wave_count'] == 2
    assert sum(wave['line_count'] for wave in result['waves']) == 3
    assert all(wave['unit_count'] <= 8 for wave in result['waves'])


def test_cycle_count_flags_variance():
    result = cycle_count_variances([
        {'sku': 'A-1', 'expected': 10, 'counted': 10},
        {'sku': 'B-1', 'expected': 10, 'counted': 7},
    ])
    assert result['matched_skus'] == 1
    assert result['investigate_skus'] == 1
    assert result['net_variance_units'] == -3


def test_inventory_health_score_explains_alerts():
    result = inventory_health_score([
        {'sku': 'A', 'category': 'Parts', 'quantity': 0, 'reorder_level': 2, 'unit_cost': 3},
    ])
    assert result['score'] == 0
    assert result['grade'] == 'D'
    assert any('out of stock' in alert for alert in result['alerts'])


def test_supplier_lead_time_ignores_invalid_dates():
    result = supplier_lead_time_summary([
        {'ordered_date': '2026-01-01', 'received_date': '2026-01-05', 'promised_days': 5},
        {'ordered_date': 'bad', 'received_date': '2026-01-06'},
    ])
    assert result['receipt_count'] == 1
    assert result['average_lead_time_days'] == 4
    assert result['on_time_rate'] == 1


def test_replenishment_batch_estimates_purchase_cost():
    result = replenishment_batch([
        {'sku': 'A-1', 'quantity': 2, 'reorder_level': 5, 'average_daily_demand': 1, 'lead_days': 2, 'unit_cost': 3},
    ], review_horizon_days=5)
    assert result['skus_to_reorder'] == 1
    assert result['total_suggested_units'] == 5
    assert result['estimated_purchase_cost'] == 15
