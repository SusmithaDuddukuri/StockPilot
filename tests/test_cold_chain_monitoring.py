import json
import os
import tempfile
import unittest
from app import create_app
from app.services.cold_chain import evaluate_temperature_reading


class ColdChainMonitoringTests(unittest.TestCase):
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

    def test_refrigerated_evaluation_optimal(self):
        eval_res = evaluate_temperature_reading("refrigerated", 4.5)
        self.assertEqual(eval_res["severity"], "Optimal")
        self.assertFalse(eval_res["is_excursion"])

    def test_refrigerated_evaluation_warning(self):
        eval_res = evaluate_temperature_reading("refrigerated", 7.5)
        self.assertEqual(eval_res["severity"], "Warning")
        self.assertFalse(eval_res["is_excursion"])

    def test_refrigerated_evaluation_critical_high(self):
        eval_res = evaluate_temperature_reading("refrigerated", 11.2)
        self.assertEqual(eval_res["severity"], "Critical High Excursion")
        self.assertTrue(eval_res["is_excursion"])

    def test_api_log_reading_and_audit_event(self):
        # Normal reading
        resp = self.client.post("/api/cold-chain/log-reading", json={
            "zone": "Vaccine-Freezer-A",
            "zone_type": "frozen",
            "temperature_celsius": -20.0
        })
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json["severity"], "Optimal")

        # Excursion reading
        excursion_resp = self.client.post("/api/cold-chain/log-reading", json={
            "zone": "Vaccine-Freezer-A",
            "zone_type": "frozen",
            "temperature_celsius": -5.0
        })
        self.assertEqual(excursion_resp.status_code, 200)
        self.assertTrue(excursion_resp.json["is_excursion"])

    def test_cold_chain_status_endpoint(self):
        status_resp = self.client.get("/api/cold-chain/status")
        self.assertEqual(status_resp.status_code, 200)
        self.assertIn("supported_profiles", status_resp.json)
        self.assertIn("frozen", status_resp.json["supported_profiles"])
        self.assertIn("refrigerated", status_resp.json["supported_profiles"])


if __name__ == "__main__":
    unittest.main()
