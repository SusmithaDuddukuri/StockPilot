"""Executable warehouse control packs, imported lazily by pack identifier."""
from importlib import import_module

SLUGS = ("inventory_integrity", "receiving_quality", "pick_pack", "shipment_service",
         "supplier_performance", "warehouse_safety", "storage_capacity", "returns_control",
         "demand_planning", "cycle_counting", "cold_chain", "high_value_goods",
         "hazardous_materials", "labor_planning", "transport_readiness", "order_accuracy")
SCOPES = ("inventory integrity", "receiving quality", "pick and pack", "shipment service",
          "supplier performance", "warehouse safety", "storage capacity", "returns control",
          "demand planning", "cycle counting", "cold-chain handling", "high-value goods",
          "hazardous material handling", "labor planning", "transport readiness", "order accuracy")

def load_pack(pack_id):
    if not isinstance(pack_id, int) or not 1 <= pack_id <= 700:
        raise ValueError("pack_id must be between 1 and 700")
    module_name = f"app.warehouse_controls.{SLUGS[(pack_id - 1) % len(SLUGS)]}_{pack_id:04d}"
    return import_module(module_name)

def catalog_page(offset=0, limit=50):
    offset = max(0, int(offset))
    limit = max(1, min(100, int(limit)))
    return [{"pack_id": i, "module": f"{SLUGS[(i - 1) % len(SLUGS)]}_{i:04d}",
             "rule_count": 24, "scope": SCOPES[(i - 1) % len(SCOPES)]}
            for i in range(offset + 1, min(700, offset + limit) + 1)]
