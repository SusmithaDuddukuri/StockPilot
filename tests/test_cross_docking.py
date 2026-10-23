import json
import os
import tempfile
import unittest
from app import create_app
from app.services.cross_docking import plan_cross_dock_allocation


class CrossDockingTests(unittest.TestCase):
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

    def test_plan_cross_dock_allocation_direct(self):
        orders = [
            {"id": 101, "customer": "Acme", "item_count": 10},
            {"id": 102, "customer": "Beta", "item_count": 15}
        ]
        # Inbound 20 units: 10 to Acme, 10 to Beta, 0 to putaway
        res = plan_cross_dock_allocation("SKU-1042", 20, orders, "BAY-01")
        self.assertEqual(res["cross_docked_units"], 20)
        self.assertEqual(res["putaway_units"], 0)
        self.assertEqual(res["routing_decision"], "Direct Cross-Dock")
        self.assertEqual(len(res["matched_orders"]), 2)

    def test_plan_cross_dock_allocation_surplus(self):
        orders = [
            {"id": 101, "customer": "Acme", "item_count": 5}
        ]
        # Inbound 12 units: 5 to Acme, 7 to putaway
        res = plan_cross_dock_allocation("SKU-1042", 12, orders, "BAY-01")
        self.assertEqual(res["cross_docked_units"], 5)
        self.assertEqual(res["putaway_units"], 7)

    def test_cross_dock_api_match(self):
        resp = self.client.post("/api/cross-dock/match", json={
            "sku": "SKU-1042",
            "quantity": 10,
            "bay": "BAY-IN-02"
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertEqual(data["sku"], "SKU-1042")
        self.assertIn("cross_docked_units", data)
        self.assertIn("putaway_units", data)
        self.assertIn("matched_orders", data)

    def test_cross_dock_lanes_endpoint(self):
        resp = self.client.get("/api/cross-dock/lanes")
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertIn("staging_lanes", data)
        self.assertGreater(len(data["staging_lanes"]), 0)


if __name__ == "__main__":
    unittest.main()
