import unittest
from app.services.planning import (
    demand_velocity, forecast_sma, reorder_point, safety_stock,
    economic_order_quantity, inventory_abc, supplier_scorecard,
    allocation_plan, inventory_variance, prioritize_replenishment,
)
from app.services.validation import ValidationError


class DemandPlanningTests(unittest.TestCase):
    def test_velocity_reports_mean_and_variability(self):
        result = demand_velocity([1, 2, 3, 4, 5])
        self.assertEqual(result['observations'], 5)
        self.assertEqual(result['total_units'], 15)
        self.assertEqual(result['average_daily_units'], 3)

    def test_forecast_is_repeatable_and_non_negative(self):
        result = forecast_sma([2, 4, 6], horizon=3, window=2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(row['forecast_units'] == 5 for row in result))

    def test_forecast_rejects_invalid_horizon(self):
        with self.assertRaises(ValidationError):
            forecast_sma([1, 2], horizon=500)

    def test_stock_policy_calculations(self):
        self.assertEqual(reorder_point(4, 5, 3), 23)
        self.assertEqual(safety_stock(2, 3, 4), 12)
        self.assertGreater(economic_order_quantity(1000, 20, 2), 0)

    def test_abc_classification_prioritizes_value(self):
        result = inventory_abc([
            {'sku': 'LOW', 'quantity': 1, 'unit_cost': 1},
            {'sku': 'HIGH', 'quantity': 10, 'unit_cost': 100},
        ])
        self.assertEqual(result[0]['sku'], 'HIGH')
        self.assertEqual(result[0]['abc_class'], 'A')

    def test_supplier_scorecard_is_bounded(self):
        result = supplier_scorecard([
            {'on_time': True, 'ordered_qty': 10, 'received_qty': 10, 'defective_qty': 0},
            {'on_time': False, 'ordered_qty': 10, 'received_qty': 9, 'defective_qty': 1},
        ])
        self.assertGreaterEqual(result['score'], 0)
        self.assertLessEqual(result['score'], 100)

    def test_allocation_does_not_overcommit_stock(self):
        result = allocation_plan([
            {'order_id': 'A', 'sku': 'SKU1', 'quantity': 7, 'priority': 1},
            {'order_id': 'B', 'sku': 'SKU1', 'quantity': 7, 'priority': 2},
        ], {'SKU1': 10})
        self.assertEqual(sum(row['allocated_qty'] for row in result['lines']), 10)
        self.assertEqual(result['lines'][1]['backorder_qty'], 4)

    def test_variance_handles_zero_expected(self):
        self.assertEqual(inventory_variance(0, 3)['result'], 'Surplus')

    def test_replenishment_prioritizes_zero_stock(self):
        result = prioritize_replenishment([
            {'sku': 'A', 'quantity': 0, 'reorder_level': 5, 'average_daily_demand': 2, 'lead_days': 3},
            {'sku': 'B', 'quantity': 20, 'reorder_level': 5, 'average_daily_demand': 1, 'lead_days': 2},
        ])
        self.assertEqual(result[0]['sku'], 'A')
        self.assertEqual(result[0]['urgency'], 'Critical')


if __name__ == '__main__':
    unittest.main()
