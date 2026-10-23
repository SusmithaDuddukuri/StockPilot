import json
import os
import tempfile
import unittest
from app import create_app
from app.services.carrier_compliance import compute_carrier_scorecard


class CarrierComplianceTests(unittest.TestCase):
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

    def test_carrier_scorecard_calculation(self):
        shipments = [
            {"status": "Delivered"},
            {"status": "Delivered"},
            {"status": "Delivered"},
            {"status": "Exception"}
        ]
        card = compute_carrier_scorecard("BlueDart", shipments)
        self.assertEqual(card["carrier"], "BlueDart")
        self.assertEqual(card["total_shipments"], 4)
        self.assertEqual(card["delivered_count"], 3)
        self.assertEqual(card["exception_count"], 1)
        self.assertEqual(card["on_time_percentage"], 75.0)
        self.assertEqual(card["tier_rating"], "Tier 4 - SLA Breach")
        self.assertTrue(card["penalty_rebate_applicable"])

    def test_api_carrier_scorecards(self):
        # Create shipments
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-SLA-01",
            "carrier": "FedEx",
            "tracking_number": "FX-900"
        })
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-SLA-02",
            "carrier": "FedEx",
            "tracking_number": "FX-901"
        })

        resp = self.client.get("/api/carrier-compliance/scorecards")
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertIn("scorecards", data)
        self.assertTrue(any(c["carrier"] == "FedEx" for c in data["scorecards"]))

    def test_api_audit_summary(self):
        resp = self.client.get("/api/carrier-compliance/audit-summary")
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertIn("total_network_parcels", data)
        self.assertIn("network_on_time_performance", data)
        self.assertIn("network_status", data)


if __name__ == "__main__":
    unittest.main()
