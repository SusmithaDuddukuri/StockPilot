import sqlite3
from contextlib import contextmanager

SEED = [
 ("SKU-1042", "Wireless barcode scanner", "Hardware", 34, 12, 79.99, "A-03-02", "Northstar Devices"),
 ("SKU-1088", "Thermal label roll", "Packaging", 180, 40, 8.50, "B-01-04", "PackRight Supply"),
 ("SKU-1130", "Shipping carton — medium", "Packaging", 22, 30, 1.25, "C-02-01", "PackRight Supply"),
 ("SKU-1205", "USB-C docking station", "Hardware", 61, 15, 119.00, "A-01-07", "Northstar Devices"),
 ("SKU-1266", "Protective mailer", "Packaging", 240, 60, 0.42, "C-01-03", "EcoShip Co."),
 ("SKU-1301", "Inventory shelf tag", "Operations", 9, 25, 2.10, "D-04-02", "LabelWorks"),
 ("SKU-1389", "Pallet stretch wrap", "Operations", 48, 20, 14.75, "D-01-01", "EcoShip Co."),
 ("SKU-1414", "Compact receipt printer", "Hardware", 17, 10, 156.00, "A-02-05", "Northstar Devices"),
]

@contextmanager
def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
        db.commit()
    finally:
        db.close()

def init_db(path):
    with connect(path) as db:
        db.executescript('''
        CREATE TABLE IF NOT EXISTS products (
          sku TEXT PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL,
          quantity INTEGER NOT NULL CHECK(quantity >= 0), reorder_level INTEGER NOT NULL CHECK(reorder_level >= 0),
          unit_cost REAL NOT NULL CHECK(unit_cost >= 0), location TEXT NOT NULL, supplier TEXT NOT NULL,
          updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS movements (
          id INTEGER PRIMARY KEY AUTOINCREMENT, sku TEXT NOT NULL REFERENCES products(sku),
          delta INTEGER NOT NULL CHECK(delta != 0), note TEXT NOT NULL,
          created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS orders (
          id INTEGER PRIMARY KEY AUTOINCREMENT, customer TEXT NOT NULL, status TEXT NOT NULL,
          item_count INTEGER NOT NULL, destination TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        ''')
        if db.execute("SELECT COUNT(*) FROM products").fetchone()[0] == 0:
            db.executemany("INSERT INTO products(sku,name,category,quantity,reorder_level,unit_cost,location,supplier) VALUES(?,?,?,?,?,?,?,?)", SEED)
        if db.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 0:
            db.executemany("INSERT INTO orders(customer,status,item_count,destination) VALUES(?,?,?,?)", [
             ("Juniper Market", "Picking", 12, "Hyderabad"), ("Orbit Office Co.", "Packed", 7, "Bengaluru"),
             ("Maple & Main", "Awaiting stock", 4, "Chennai"), ("Bluebird Retail", "Shipped", 19, "Pune")])

# Operational subsystems are created independently so upgrades remain safe for
# installations that already contain the original inventory tables.
OPERATIONAL_SCHEMA = '''
CREATE TABLE IF NOT EXISTS suppliers (
 id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL UNIQUE, name TEXT NOT NULL,
 contact_name TEXT NOT NULL DEFAULT '', email TEXT NOT NULL DEFAULT '', phone TEXT NOT NULL DEFAULT '',
 lead_days INTEGER NOT NULL DEFAULT 7 CHECK(lead_days >= 0), active INTEGER NOT NULL DEFAULT 1,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS customers (
 id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL UNIQUE, name TEXT NOT NULL,
 email TEXT NOT NULL DEFAULT '', phone TEXT NOT NULL DEFAULT '', address TEXT NOT NULL DEFAULT '',
 active INTEGER NOT NULL DEFAULT 1, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS purchase_orders (
 id INTEGER PRIMARY KEY AUTOINCREMENT, po_number TEXT NOT NULL UNIQUE, supplier_id INTEGER NOT NULL REFERENCES suppliers(id),
 status TEXT NOT NULL DEFAULT 'Draft', expected_date TEXT NOT NULL DEFAULT '', notes TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS purchase_order_lines (
 id INTEGER PRIMARY KEY AUTOINCREMENT, purchase_order_id INTEGER NOT NULL REFERENCES purchase_orders(id) ON DELETE CASCADE,
 sku TEXT NOT NULL REFERENCES products(sku), ordered_qty INTEGER NOT NULL CHECK(ordered_qty > 0),
 received_qty INTEGER NOT NULL DEFAULT 0 CHECK(received_qty >= 0), unit_cost REAL NOT NULL CHECK(unit_cost >= 0)
);
CREATE TABLE IF NOT EXISTS receipts (
 id INTEGER PRIMARY KEY AUTOINCREMENT, receipt_number TEXT NOT NULL UNIQUE,
 purchase_order_id INTEGER REFERENCES purchase_orders(id), sku TEXT NOT NULL REFERENCES products(sku),
 quantity INTEGER NOT NULL CHECK(quantity > 0), received_by TEXT NOT NULL DEFAULT 'Warehouse team',
 note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS stock_transfers (
 id INTEGER PRIMARY KEY AUTOINCREMENT, transfer_number TEXT NOT NULL UNIQUE, sku TEXT NOT NULL REFERENCES products(sku),
 quantity INTEGER NOT NULL CHECK(quantity > 0), from_location TEXT NOT NULL, to_location TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'Completed', note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS returns (
 id INTEGER PRIMARY KEY AUTOINCREMENT, return_number TEXT NOT NULL UNIQUE, sku TEXT NOT NULL REFERENCES products(sku),
 quantity INTEGER NOT NULL CHECK(quantity > 0), reason TEXT NOT NULL, disposition TEXT NOT NULL DEFAULT 'Inspection',
 status TEXT NOT NULL DEFAULT 'Open', customer_name TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS shipments (
 id INTEGER PRIMARY KEY AUTOINCREMENT, shipment_number TEXT NOT NULL UNIQUE, order_id INTEGER REFERENCES orders(id),
 carrier TEXT NOT NULL DEFAULT '', tracking_number TEXT NOT NULL DEFAULT '', status TEXT NOT NULL DEFAULT 'Label created',
 shipped_at TEXT NOT NULL DEFAULT '', delivered_at TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS cycle_counts (
 id INTEGER PRIMARY KEY AUTOINCREMENT, count_number TEXT NOT NULL UNIQUE, sku TEXT NOT NULL REFERENCES products(sku),
 expected_qty INTEGER NOT NULL, counted_qty INTEGER NOT NULL, variance INTEGER NOT NULL,
 counted_by TEXT NOT NULL DEFAULT 'Warehouse team', note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS audit_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT, event_type TEXT NOT NULL, entity_type TEXT NOT NULL,
 entity_id TEXT NOT NULL, summary TEXT NOT NULL, actor TEXT NOT NULL DEFAULT 'System',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_purchase_order_status ON purchase_orders(status);
CREATE INDEX IF NOT EXISTS idx_receipts_sku ON receipts(sku, created_at);
CREATE INDEX IF NOT EXISTS idx_audit_created ON audit_events(created_at DESC);
CREATE TABLE IF NOT EXISTS safety_inspections (
 id INTEGER PRIMARY KEY AUTOINCREMENT, inspection_number TEXT NOT NULL UNIQUE, zone TEXT NOT NULL,
 inspector TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Passed', findings TEXT NOT NULL DEFAULT '',
 action_required TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_safety_zone ON safety_inspections(zone, created_at DESC);
CREATE TABLE IF NOT EXISTS inventory_quarantine (
 id INTEGER PRIMARY KEY AUTOINCREMENT, quarantine_number TEXT NOT NULL UNIQUE, sku TEXT NOT NULL REFERENCES products(sku),
 quantity INTEGER NOT NULL CHECK(quantity > 0), reason TEXT NOT NULL, inspector TEXT NOT NULL DEFAULT 'Quality Assurance',
 status TEXT NOT NULL DEFAULT 'Under Inspection', disposition TEXT NOT NULL DEFAULT 'Pending',
 note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_quarantine_sku ON inventory_quarantine(sku, status);
'''

_original_init_db = init_db
def init_db(path):
    _original_init_db(path)
    with connect(path) as db:
        db.executescript(OPERATIONAL_SCHEMA)
        if db.execute('SELECT COUNT(*) FROM suppliers').fetchone()[0] == 0:
            db.executemany('INSERT INTO suppliers(code,name,contact_name,email,phone,lead_days) VALUES(?,?,?,?,?,?)', [
                ('SUP-001','Northstar Devices','Anika Rao','orders@northstar.example','+91-80000-10001',5),
                ('SUP-002','PackRight Supply','Rahul Mehta','sales@packright.example','+91-80000-10002',3),
                ('SUP-003','EcoShip Co.','Mira Das','supply@ecoship.example','+91-80000-10003',8),
                ('SUP-004','LabelWorks','Kiran Shah','support@labelworks.example','+91-80000-10004',4),
            ])
        if db.execute('SELECT COUNT(*) FROM customers').fetchone()[0] == 0:
            db.executemany('INSERT INTO customers(code,name,email,phone,address) VALUES(?,?,?,?,?)', [
                ('CUS-001','Juniper Market','warehouse@juniper.example','+91-80000-20001','Hyderabad'),
                ('CUS-002','Orbit Office Co.','ops@orbit.example','+91-80000-20002','Bengaluru'),
                ('CUS-003','Maple & Main','orders@maple.example','+91-80000-20003','Chennai'),
            ])
