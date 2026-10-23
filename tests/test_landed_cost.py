import json
import os
import tempfile
import unittest
from app import create_app
from app.services.landed_cost import compute_landed_unit_cost


class LandedCostTests(unittest.TestCase):
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

    def test_compute_landed_unit_cost_formula(self):
        # 10 units at $100 base cost, $50 freight, 10% duty, 2% insurance, $20 handling
        # Unit freight = 5.0, Unit duty = 10.0, Unit insurance = 2.0, Unit handling = 2.0
        # Total overhead = 19.0 -> Landed cost = 119.0
        res = compute_landed_unit_cost(
            base_unit_cost=100.0,
            quantity=10,
            total_freight_charge=50.0,
            customs_duty_pct=10.0,
            cargo_insurance_pct=2.0,
            drayage_handling_fee=20.0
        )
        self.assertEqual(res["final_landed_unit_cost"], 119.0)
        self.assertEqual(res["total_landed_shipment_value"], 1190.0)
        self.assertEqual(res["overhead_markup_percentage"], 19.0)

    def test_api_calculate_landed_cost(self):
        resp = self.client.post("/api/finance/landed-cost/calculate", json={
            "sku": "SKU-1042",
            "base_unit_cost": 50.0,
            "quantity": 20,
            "freight_charge": 100.0,
            "customs_duty_pct": 5.0
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertEqual(data["sku"], "SKU-1042")
        self.assertIn("final_landed_unit_cost", data)
        self.assertGreater(data["final_landed_unit_cost"], 50.0)

    def test_api_catalog_estimates(self):
        resp = self.client.get("/api/finance/landed-cost/catalog-estimates")
        self.assertEqual(resp.status_code, 200)
        data = resp.json
        self.assertIn("catalog_size", data)
        self.assertIn("total_catalog_base_valuation", data)
        self.assertIn("total_catalog_landed_valuation", data)
        self.assertGreater(data["total_catalog_landed_valuation"], data["total_catalog_base_valuation"])


if __name__ == "__main__":
    unittest.main()
