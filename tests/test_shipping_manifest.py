import csv
import io
import json
import os
import tempfile
import unittest
from app import create_app


class ShippingManifestTests(unittest.TestCase):
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

    def test_empty_or_default_manifest(self):
        response = self.client.get("/api/shipping/manifest")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn("manifest_reference", data)
        self.assertIn("total_shipments", data)
        self.assertIn("total_items_to_dispatch", data)
        self.assertIn("shipments", data)

    def test_shipment_creation_and_manifest_inclusion(self):
        # Create a new shipment via operations API
        shipment_data = {
            "shipment_number": "SHP-TEST-001",
            "carrier": "BlueDart Express",
            "tracking_number": "BD-99887766"
        }
        create_resp = self.client.post("/api/ops/shipments", json=shipment_data)
        self.assertEqual(create_resp.status_code, 201)

        # Check that it appears on the manifest
        manifest_resp = self.client.get("/api/shipping/manifest")
        self.assertEqual(manifest_resp.status_code, 200)
        manifest = manifest_resp.json
        self.assertEqual(manifest["total_shipments"], 1)
        self.assertEqual(manifest["shipments"][0]["shipment_number"], "SHP-TEST-001")
        self.assertEqual(manifest["shipments"][0]["carrier"], "BlueDart Express")

    def test_carrier_filtering(self):
        # Create shipments with different carriers
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-FEDEX-01",
            "carrier": "FedEx",
            "tracking_number": "FX-1111"
        })
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-DHL-01",
            "carrier": "DHL",
            "tracking_number": "DH-2222"
        })

        # Filter by FedEx
        fedex_resp = self.client.get("/api/shipping/manifest?carrier=FedEx")
        self.assertEqual(fedex_resp.status_code, 200)
        fedex_data = fedex_resp.json
        self.assertEqual(fedex_data["total_shipments"], 1)
        self.assertEqual(fedex_data["shipments"][0]["carrier"], "FedEx")

    def test_manifest_csv_export(self):
        self.client.post("/api/ops/shipments", json={
            "shipment_number": "SHP-CSV-01",
            "carrier": "Delhivery",
            "tracking_number": "DLV-3333"
        })

        csv_resp = self.client.get("/api/shipping/manifest.csv")
        self.assertEqual(csv_resp.status_code, 200)
        self.assertEqual(csv_resp.mimetype, "text/csv")
        self.assertIn("attachment; filename=", csv_resp.headers["Content-Disposition"])

        content = csv_resp.data.decode("utf-8")
        reader = csv.reader(io.StringIO(content))
        rows = list(reader)
        header = rows[0]
        self.assertIn("Shipment Number", header)
        self.assertIn("Carrier", header)
        self.assertIn("Tracking Number", header)
        self.assertTrue(any(row[0] == "SHP-CSV-01" for row in rows[1:]))


if __name__ == "__main__":
    unittest.main()
