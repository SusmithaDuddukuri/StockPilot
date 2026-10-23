import json
import os
import tempfile
import unittest
from app import create_app


class BackorderAllocationTests(unittest.TestCase):
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

    def test_backorder_queue_inspection(self):
        response = self.client.get("/api/orders/backorders/queue")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn("backorder_count", data)
        self.assertIn("total_units_demanded", data)
        self.assertIn("available_units_in_pool", data)
        self.assertIn("allocation_queue", data)

        # In default seed data, 'Maple & Main' is 'Awaiting stock' (item_count = 4)
        self.assertGreaterEqual(data["backorder_count"], 1)
        first_item = data["allocation_queue"][0]
        self.assertEqual(first_item["customer"], "Maple & Main")
        self.assertEqual(first_item["item_count"], 4)
        self.assertEqual(first_item["allocation_posture"], "Fully Allocatable")

    def test_release_single_backorder(self):
        # Locate the backordered order
        queue_data = self.client.get("/api/orders/backorders/queue").json
        order_id = queue_data["allocation_queue"][0]["order_id"]

        # Release this order to picking
        release_resp = self.client.post("/api/orders/backorders/release-to-picking", json={
            "order_id": order_id
        })
        self.assertEqual(release_resp.status_code, 200)
        self.assertIn("released from backorder queue to Picking", release_resp.json["message"])

        # Verify it is no longer in backorder state
        updated_queue = self.client.get("/api/orders/backorders/queue").json
        self.assertFalse(any(o["order_id"] == order_id for o in updated_queue["allocation_queue"]))

    def test_release_invalid_order_state(self):
        # Order 1 in seed is "Picking", not "Awaiting stock"
        invalid_resp = self.client.post("/api/orders/backorders/release-to-picking", json={
            "order_id": 1
        })
        self.assertEqual(invalid_resp.status_code, 400)
        self.assertIn("is not in backorder state", invalid_resp.json["error"])

    def test_bulk_release_all_backorders(self):
        bulk_resp = self.client.post("/api/orders/backorders/release-to-picking", json={})
        self.assertEqual(bulk_resp.status_code, 200)

        # Queue should now be empty
        empty_queue = self.client.get("/api/orders/backorders/queue").json
        self.assertEqual(empty_queue["backorder_count"], 0)


if __name__ == "__main__":
    unittest.main()
