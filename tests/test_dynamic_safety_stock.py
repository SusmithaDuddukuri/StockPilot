import json
import os
import tempfile
import unittest
from app import create_app


class DynamicSafetyStockTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.app = create_app({
            "TESTING": True,
            "DATABASE": os.path.join(self.temp.name, "test.sqlite3"),
            "SECRET_KEY": "test"
        })
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def test_default_safety_stock_endpoint(self):
        response = self.client.get("/api/replenishment/dynamic-safety-stock")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["service_level_target"], "95%")
        self.assertEqual(data["z_score"], 1.65)
        self.assertGreater(data["total_skus_evaluated"], 0)
        self.assertIn("at_risk_sku_count", data)
        self.assertIn("recommended_reorder_count", data)
        self.assertIn("total_recommended_reorder_cost", data)
        self.assertIn("skus", data)

        first_sku = data["skus"][0]
        self.assertIn("calculated_safety_stock", first_sku)
        self.assertIn("dynamic_reorder_point", first_sku)
        self.assertIn("stock_posture", first_sku)
        self.assertIn("priority", first_sku)

    def test_service_level_scaling(self):
        resp_90 = self.client.get("/api/replenishment/dynamic-safety-stock?service_level=90")
        resp_99 = self.client.get("/api/replenishment/dynamic-safety-stock?service_level=99")

        self.assertEqual(resp_90.status_code, 200)
        self.assertEqual(resp_99.status_code, 200)

        data_90 = resp_90.json
        data_99 = resp_99.json

        # Higher service level should yield greater or equal total safety stock
        sum_ss_90 = sum(item["calculated_safety_stock"] for item in data_90["skus"])
        sum_ss_99 = sum(item["calculated_safety_stock"] for item in data_99["skus"])
        self.assertGreaterEqual(sum_ss_99, sum_ss_90)

    def test_outbound_movement_influences_demand(self):
        initial = self.client.get("/api/replenishment/dynamic-safety-stock").json
        sku = initial["skus"][0]["sku"]

        # Record substantial outbound fulfillment
        self.client.post("/api/movements", json={
            "sku": sku,
            "delta": -10,
            "note": "Bulk store order fulfillment"
        })

        updated = self.client.get("/api/replenishment/dynamic-safety-stock").json
        updated_sku_map = {item["sku"]: item for item in updated["skus"]}
        # Demand calculations should reflect active movement
        self.assertGreater(updated_sku_map[sku]["average_daily_demand"], 0)


if __name__ == "__main__":
    unittest.main()
