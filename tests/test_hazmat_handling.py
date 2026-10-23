import json
import os
import tempfile
import unittest
from app import create_app
from app.services.hazmat import validate_hazmat_storage


class HazmatHandlingTests(unittest.TestCase):
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

    def test_flammable_in_valid_location(self):
        res = validate_hazmat_storage("CLASS_3_FLAMMABLE", "HAZ-FLAM-01-A")
        self.assertTrue(res["compliant"])
        self.assertTrue(res["prefix_compliant"])
        self.assertTrue(res["secondary_containment_required"])

    def test_flammable_in_invalid_location(self):
        res = validate_hazmat_storage("CLASS_3_FLAMMABLE", "AISLE-C-02")
        self.assertFalse(res["compliant"])
        self.assertFalse(res["prefix_compliant"])

    def test_segregation_incompatibility(self):
        # Flammable + Corrosive neighboring should fail segregation
        res = validate_hazmat_storage("CLASS_3_FLAMMABLE", "HAZ-FLAM-01", neighboring_classes=["CLASS_8_CORROSIVE"])
        self.assertFalse(res["compliant"])
        self.assertFalse(res["segregation_passed"])

    def test_api_validate_endpoint_valid(self):
        resp = self.client.post("/api/hazmat/validate-storage", json={
            "sku": "SKU-SOLVENT-01",
            "hazard_class": "CLASS_3_FLAMMABLE",
            "location": "HAZ-FLAM-BAY-03"
        })
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json["compliant"])

    def test_api_validate_endpoint_rejected(self):
        resp = self.client.post("/api/hazmat/validate-storage", json={
            "sku": "SKU-ACID-01",
            "hazard_class": "CLASS_8_CORROSIVE",
            "location": "STANDARD-RACK-01"
        })
        self.assertEqual(resp.status_code, 422)
        self.assertFalse(resp.json["compliant"])

    def test_hazard_classes_catalog_endpoint(self):
        resp = self.client.get("/api/hazmat/hazard-classes")
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertIn("supported_classes", data)
        self.assertIn("CLASS_3_FLAMMABLE", data["supported_classes"])
        self.assertIn("CLASS_8_CORROSIVE", data["supported_classes"])


if __name__ == "__main__":
    unittest.main()
