import json
import os
import tempfile
import unittest
from app import create_app
from app.services.barcode_service import calculate_ean13_check_digit, verify_barcode


class BarcodeVerificationTests(unittest.TestCase):
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

    def test_ean13_check_digit_calculation(self):
        # 400638133393 -> 1
        check = calculate_ean13_check_digit("400638133393")
        self.assertEqual(check, 1)

    def test_code128_verification(self):
        res = verify_barcode("SKU-1042-TEST", "Code128")
        self.assertTrue(res["valid"])
        self.assertEqual(res["grade"], "A")
        self.assertEqual(res["symbology"], "Code 128")

    def test_verify_barcode_api_valid(self):
        response = self.client.post("/api/barcode/verify", json={
            "barcode": "SKU-1042",
            "symbology": "Code128",
            "sku": "SKU-1042"
        })
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(data["valid"])
        self.assertEqual(data["grade"], "A")
        self.assertIsNotNone(data["linked_product"])
        self.assertEqual(data["linked_product"]["sku"], "SKU-1042")

    def test_verify_barcode_api_invalid_check_digit(self):
        # 12 digits: 400638133393 has check digit 1. Supplying 9 should fail.
        response = self.client.post("/api/barcode/verify", json={
            "barcode": "4006381333939",
            "symbology": "EAN-13"
        })
        self.assertEqual(response.status_code, 422)
        data = response.json
        self.assertFalse(data["valid"])
        self.assertEqual(data["grade"], "F")

    def test_label_specification_endpoint(self):
        response = self.client.get("/api/barcode/label-spec/SKU-1042")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["sku"], "SKU-1042")
        self.assertIn("ean13_payload", data)
        self.assertIn("label_dimensions_mm", data)
        self.assertIn("print_specifications", data)


if __name__ == "__main__":
    unittest.main()
