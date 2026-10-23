import json
import os
import tempfile
import unittest
from app import create_app
from app.services.delivery_exceptions import evaluate_exception_action


class DeliveryExceptionsTests(unittest.TestCase):
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

    def test_evaluate_action_unvailable_under_threshold(self):
        res = evaluate_exception_action("CUSTOMER_UNAVAILABLE", attempt_count=2)
        self.assertEqual(res["shipment_state_target"], "Exception")
        self.assertIn("Redeliver", res["resolution_action"])

    def test_evaluate_action_unavailable_exceeds_threshold(self):
        res = evaluate_exception_action("CUSTOMER_UNAVAILABLE", attempt_count=3)
        self.assertEqual(res["shipment_state_target"], "Returned")
        self.assertIn("RTS", res["resolution_action"])

    def test_evaluate_action_reroute(self):
        res = evaluate_exception_action("REROUTE_REQUESTED", amended_address="Plot 42, Tech Park, Hyderabad")
        self.assertEqual(res["shipment_state_target"], "In transit")
        self.assertEqual(res["new_destination"], "Plot 42, Tech Park, Hyderabad")

    def test_record_and_resolve_api_workflow(self):
        # Create a shipment via ops API
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-EX-001",
            "carrier": "BlueDart",
            "tracking_number": "TRK-001"
        })

        # Record delivery exception
        rec_resp = self.client.post("/api/shipping/exceptions/record", json={
            "shipment_number": "SHP-EX-001",
            "exception_type": "CUSTOMER_UNAVAILABLE",
            "attempt_count": 1
        })
        self.assertEqual(rec_resp.status_code, 200)
        self.assertEqual(rec_resp.json["new_status"], "Exception")

        # Verify active exceptions list
        active_resp = self.client.get("/api/shipping/exceptions/active")
        self.assertEqual(active_resp.status_code, 200)
        self.assertTrue(any(s["shipment_number"] == "SHP-EX-001" for s in active_resp.json["shipments"]))

        # Resolve exception with amended address
        res_resp = self.client.post("/api/shipping/exceptions/resolve", json={
            "shipment_number": "SHP-EX-001",
            "exception_type": "REROUTE_REQUESTED",
            "amended_destination": "Sector 5, Salt Lake, Kolkata"
        })
        self.assertEqual(res_resp.status_code, 200)
        self.assertEqual(res_resp.json["resolved_status"], "In transit")


if __name__ == "__main__":
    unittest.main()
