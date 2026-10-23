import json
import os
import tempfile
import unittest
from app import create_app


class DeadstockAnalysisTests(unittest.TestCase):
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

    def test_deadstock_analysis_endpoint_structure(self):
        response = self.client.get("/api/reports/deadstock-analysis")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn("analyzed_sku_count", data)
        self.assertIn("deadstock_sku_count", data)
        self.assertIn("total_tied_up_capital", data)
        self.assertIn("total_at_risk_units", data)
        self.assertIn("items", data)
        self.assertGreater(data["analyzed_sku_count"], 0)

    def test_category_filter(self):
        response = self.client.get("/api/reports/deadstock-analysis?category=Packaging")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(all(item["category"].lower() == "packaging" for item in data["items"]))

    def test_deadstock_classification_with_movement(self):
        # Initial seed items without movements should be Deadstock or Slow-moving
        response = self.client.get("/api/reports/deadstock-analysis")
        data = response.json
        first_item = data["items"][0]
        self.assertIn(first_item["classification"], ["Deadstock", "Slow-moving", "Active", "Depleted"])

        # Add movement for a specific SKU
        sku = first_item["sku"]
        move_resp = self.client.post("/api/movements", json={
            "sku": sku,
            "delta": 5,
            "note": "Cycle count replenishment adjustment"
        })
        self.assertEqual(move_resp.status_code, 201)

        # Re-check report
        updated_resp = self.client.get("/api/reports/deadstock-analysis")
        updated_items = {i["sku"]: i for i in updated_resp.json["items"]}
        self.assertGreaterEqual(updated_items[sku]["movement_count"], 1)


if __name__ == "__main__":
    unittest.main()
