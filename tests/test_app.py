import json
import os
import tempfile
import unittest
from app import create_app

class StockPilotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.app = create_app({"TESTING": True, "DATABASE": os.path.join(self.temp.name, "test.sqlite3"), "SECRET_KEY": "test"})
        self.client = self.app.test_client()
    def tearDown(self): self.temp.cleanup()
    def test_home_and_health(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/health').json['status'], 'ok')
    def test_overview_seed_data(self):
        d = self.client.get('/api/overview').json
        self.assertGreaterEqual(d['products'], 8)
        self.assertGreater(d['units'], 0)
        self.assertGreater(d['low_stock'], 0)
    def test_product_search_and_filters(self):
        r = self.client.get('/api/products?q=barcode')
        self.assertEqual(r.status_code, 200)
        self.assertTrue(any('barcode' in x['name'].lower() for x in r.json))
        low = self.client.get('/api/products?state=low').json
        self.assertTrue(all(x['quantity'] <= x['reorder_level'] for x in low))
    def test_create_product_and_duplicate_sku(self):
        p = {"sku":"SKU-9000","name":"Test carton","category":"Packaging","quantity":5,"reorder_level":2,"unit_cost":3.5,"location":"Z-01","supplier":"Test Supply"}
        self.assertEqual(self.client.post('/api/products', json=p).status_code, 201)
        self.assertEqual(self.client.post('/api/products', json=p).status_code, 409)
    def test_reject_invalid_product(self):
        self.assertEqual(self.client.post('/api/products', json={"sku":"X"}).status_code, 400)
    def test_stock_increase_and_audit(self):
        r = self.client.post('/api/movements', json={"sku":"SKU-1042","delta":7,"note":"Receipt"})
        self.assertEqual(r.status_code, 201)
        product = next(x for x in self.client.get('/api/products').json if x['sku']=='SKU-1042')
        self.assertEqual(product['quantity'], 41)
        self.assertEqual(self.client.get('/api/movements').json[0]['note'], 'Receipt')
    def test_prevent_negative_stock(self):
        r = self.client.post('/api/movements', json={"sku":"SKU-1042","delta":-999,"note":"bad"})
        self.assertEqual(r.status_code, 400)
    def test_unknown_sku_and_zero_movement(self):
        self.assertEqual(self.client.post('/api/movements', json={"sku":"NOPE","delta":1}).status_code, 404)
        self.assertEqual(self.client.post('/api/movements', json={"sku":"SKU-1042","delta":0}).status_code, 400)
    def test_order_status_update(self):
        self.assertEqual(self.client.post('/api/orders/1/status', json={"status":"Packed"}).status_code, 200)
        self.assertEqual(next(x for x in self.client.get('/api/orders').json if x['id']==1)['status'], 'Packed')
    def test_invalid_order_status_and_missing_order(self):
        self.assertEqual(self.client.post('/api/orders/1/status', json={"status":"Teleporting"}).status_code, 400)
        self.assertEqual(self.client.post('/api/orders/999/status', json={"status":"Packed"}).status_code, 404)
    def test_csv_export(self):
        r = self.client.get('/api/export.csv')
        self.assertEqual(r.status_code, 200)
        self.assertIn('text/csv', r.content_type)
        self.assertIn(b'SKU,Product,Category', r.data)




    def test_replenishment_recommendations_endpoint(self):
        r = self.client.get('/api/replenishment/recommendations')
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn('recommendations', data)
        self.assertIn('total_estimated_budget', data)
        self.assertTrue(all('suggested_order_units' in item for item in data['recommendations']))

    def test_export_catalog_manifest_endpoint(self):
        r = self.client.get('/api/export/catalog-manifest')
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data['format'], 'StockPilot Catalog Exchange')
        self.assertGreater(data['item_count'], 0)
        self.assertIn('total_valuation', data)
        self.assertTrue(all('stock_status' in item for item in data['catalog']))

    def test_category_valuation_report(self):
        r = self.client.get('/api/reports/category-valuation')
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn('categories', data)
        self.assertGreater(data['category_count'], 0)
        self.assertIn('portfolio_value', data)
        self.assertTrue(all('portfolio_share_percent' in c for c in data['categories']))

    def test_warehouse_bin_utilization(self):
        r = self.client.get('/api/warehouse/bin-utilization')
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn('bins', data)
        self.assertGreater(data['bin_count'], 0)
        self.assertIn('overall_utilization_percent', data)
        self.assertTrue(all('zone' in b for b in data['bins']))

if __name__ == '__main__': unittest.main()

class OperationsAPITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = create_app({'TESTING': True, 'DATABASE': os.path.join(self.tmp.name, 'operations.sqlite3'), 'SECRET_KEY': 'test-key'})
        self.client = self.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()




    def test_safety_inspection_workflow(self):
        created = self.client.post('/api/ops/inspections', json={
            'inspection_number': 'SAFE-AUDIT-A',
            'zone': 'Aisle A - Pallet Racking',
            'inspector': 'Lead Auditor',
            'status': 'Passed',
            'findings': 'Aisle clear and fire equipment accessible',
            'action_required': 'None'
        })
        self.assertEqual(created.status_code, 201)
        inspections = self.client.get('/api/ops/inspections').get_json()
        self.assertTrue(any(i['inspection_number'] == 'SAFE-AUDIT-A' for i in inspections))

    def test_fulfillment_velocity_endpoint(self):
        response = self.client.get('/api/ops/analytics/fulfillment-velocity')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('status_distribution', data)
        self.assertIn('shipped_rate_percent', data)
        self.assertGreater(data['total_orders'], 0)

    def test_supplier_performance_tiers_endpoint(self):
        response = self.client.get('/api/ops/suppliers/performance-tiers')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('tiers', data)
        self.assertGreaterEqual(data['supplier_count'], 4)
        self.assertTrue(all('tier' in s and 'composite_score' in s for s in data['tiers']))

    def test_operational_health_and_seeded_suppliers(self):
        health = self.client.get('/api/ops/health')
        self.assertEqual(health.status_code, 200)
        self.assertEqual(health.json['status'], 'ok')
        suppliers = self.client.get('/api/ops/suppliers')
        self.assertEqual(suppliers.status_code, 200)
        self.assertGreaterEqual(len(suppliers.json), 4)

    def test_cycle_count_updates_stock_and_audit(self):
        response = self.client.post('/api/ops/cycle-counts', json={
            'count_number': 'CC-TEST-001', 'sku': 'SKU-1042', 'counted_qty': 30,
            'counted_by': 'Test operator', 'note': 'Counted aisle A'
        })
        self.assertEqual(response.status_code, 201, response.get_json())
        products = self.client.get('/api/products').get_json()
        product = next(row for row in products if row['sku'] == 'SKU-1042')
        self.assertEqual(product['quantity'], 30)
        events = self.client.get('/api/ops/audit').get_json()
        self.assertTrue(any(event['event_type'] == 'inventory.cycle_count' for event in events))

    def test_return_restocking_increases_inventory(self):
        before = next(row for row in self.client.get('/api/products').get_json() if row['sku'] == 'SKU-1042')['quantity']
        created = self.client.post('/api/ops/returns', json={
            'return_number': 'RET-TEST-001', 'sku': 'SKU-1042', 'quantity': 2,
            'reason': 'Customer return', 'disposition': 'Restock', 'customer_name': 'Test Customer'
        })
        self.assertEqual(created.status_code, 201, created.get_json())
        resolved = self.client.patch('/api/ops/returns/RET-TEST-001', json={'status': 'Restocked'})
        self.assertEqual(resolved.status_code, 200, resolved.get_json())
        after = next(row for row in self.client.get('/api/products').get_json() if row['sku'] == 'SKU-1042')['quantity']
        self.assertEqual(after, before + 2)

    def test_invalid_cycle_count_is_rejected(self):
        response = self.client.post('/api/ops/cycle-counts', json={
            'count_number': 'CC-TEST-002', 'sku': 'SKU-1042', 'counted_qty': -1
        })
        self.assertEqual(response.status_code, 400)

    def test_reorder_and_report_endpoints(self):
        self.assertEqual(self.client.get('/api/ops/reorder-recommendations').status_code, 200)
        summary = self.client.get('/api/ops/reports/summary')
        self.assertEqual(summary.status_code, 200)
        self.assertIn('inventory', summary.json)
        self.assertEqual(self.client.get('/api/ops/reports/valuation.csv').status_code, 200)

class AnalyticsFeatureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.app = create_app({'TESTING': True, 'DATABASE': os.path.join(self.tmp.name, 'analytics.sqlite3'), 'SECRET_KEY': 'analytics-test'})
        self.client = self.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def test_operations_workspace_is_reachable(self):
        response = self.client.get('/operations')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alert center', response.data)
        self.assertIn(b'Supplier scorecards', response.data)

    def test_alert_center_returns_actionable_stock_alerts(self):
        response = self.client.get('/api/ops/analytics/alerts')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json['count'], 1)
        self.assertTrue(any(item['type'] == 'low_stock' for item in response.json['alerts']))

    def test_location_analytics_sums_inventory_value(self):
        response = self.client.get('/api/ops/analytics/locations')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.json['location_count'], 0)
        self.assertGreater(response.json['inventory_value'], 0)
        self.assertTrue(all('value_share_percent' in row for row in response.json['locations']))

    def test_supplier_scorecards_include_seeded_suppliers(self):
        response = self.client.get('/api/ops/analytics/suppliers')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json), 4)
        self.assertTrue(all('completion_rate' in row for row in response.json))

    def test_order_analytics_reports_backlog(self):
        response = self.client.get('/api/ops/analytics/orders')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.json['total_orders'], 0)
        self.assertEqual(response.json['total_orders'], response.json['shipped_orders'] + response.json['open_orders'])

    def test_movement_analytics_bounds_requested_window(self):
        response = self.client.get('/api/ops/analytics/movement?days=9999')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['window_days'], 365)
