# StockPilot — Warehouse Inventory & Fulfilment

StockPilot is a warehouse operations prototype for small distribution teams. It combines a responsive inventory dashboard with operational workflows for procurement, inbound receiving, stock transfers, cycle counts, reverse logistics, shipments, audit events and CSV reporting. This is a different domain from the supplied education/LMS reference project.

## Features

- Live dashboard metrics: SKU count, units on hand, inventory value, low-stock alerts, and open orders.
- Searchable inventory with category and stock-health filters.
- Create products with SKU uniqueness and numeric validation.
- Stock adjustments for receipts, damaged goods, count corrections, and fulfilment; stock can never fall below zero.
- Persistent movement audit trail with reason and timestamp.
- Order workflow with validated status updates.
- Inventory CSV export.
- Operations workspace at `/operations` for supplier records, purchase orders, receipts, transfers, returns, shipments, cycle counts, reorder recommendations and audit history.
- Purchase-order receiving enforces ordered quantity limits and updates stock, receipt ledger, movement history and audit trail in a single transaction.
- Cycle-count reconciliation records expected/actual quantities and variance; return restocking updates inventory with duplicate-close protection.
- Shipment status transitions prevent a delivered shipment from moving backwards.
- Supplier and customer directory endpoints, inventory valuation reports and activity exports.
- Responsive desktop/mobile UI, notification panel, workspace profile, help playbook, and form feedback.
- SQLite persistence, health endpoint, API tests, Docker support, dependency manifest and lock file.

## Requirements

- Python 3.10 or newer
- pip

## Run on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.lock
python run.py
```

Open `http://127.0.0.1:8000`.

## Run on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python run.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

Or install the optional test dependency and run `pytest`.

## Docker

```bash
docker compose up --build
```

## API overview

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Service health |
| GET | `/api/overview` | Dashboard metrics and recent movements |
| GET | `/api/products?q=&category=&state=` | Search/filter inventory |
| POST | `/api/products` | Add a product |
| POST | `/api/movements` | Record a stock movement |
| GET | `/api/movements` | Latest movement history |
| GET | `/api/orders` | List fulfilment orders |
| POST | `/api/orders/<id>/status` | Update order status |
| GET | `/api/export.csv` | Download inventory CSV |

Operational workflows and all `/api/ops/*` routes are documented in [API_REFERENCE.md](API_REFERENCE.md). Visit `/operations` in the running application to use the workflow workspace.

### Example stock movement

```json
{"sku":"SKU-1042","delta":12,"note":"Stock received"}
```

## Data and security notes

The app seeds fictional demonstration data into SQLite on first run. The default secret key is for local development only; set `STOCKPILOT_SECRET` before any deployment and configure `STOCKPILOT_DB` for a chosen database path. This prototype does not implement user authentication and should not be exposed publicly without an authentication and deployment security layer.

## Repository quality

The project includes tests, pinned direct dependencies, a lock-style requirements file, a pyproject manifest, Docker files, and a Git repository with meaningful local commits. GitHub pull requests and their merge records are hosted remotely and cannot be manufactured inside a ZIP archive. See `METRICS.md` for what is and is not claimed.


## Repository hygiene and dependency locking

- `example.env` is a safe configuration template; copy it to `.env` locally and never commit the copied file.
- `.gitignore` excludes local environment files, virtual environments, databases, build output and test artifacts.
- `package-lock.json` locks the JavaScript package metadata for the static UI's Node validation script. Python runtime pins remain in `requirements.txt` and `requirements.lock`.
- The former generated policy catalog was removed from the production tree because it inflated raw file size without adding maintainable application logic.

Run checks:

```powershell
python -m compileall -q app run.py
pytest -q
npm run check
```

## Quality checks and honest scope

```powershell
python -m compileall -q app run.py
python -m unittest discover -s tests -v
npm run check
```

The codebase is a functional warehouse prototype with explicit domain services, validation, operational REST endpoints, a browser workspace, persistent SQLite storage and integration tests. Its current implementation is **not** a 500,000-production-LOC enterprise codebase. Generated records, duplicated code, tests, build output and Git history are not production source. A 500,000-line target requires a sustained engineering effort and independently useful functionality; a ZIP cannot honestly meet it by padding a catalog. Hosted pull requests also require a real remote repository and actual reviewed merges.

## Demand planning and inventory intelligence

The Operations workspace includes a Demand planning view backed by `/api/ops/planning/replenishment`. Planning APIs also provide:

- `GET /api/ops/planning/kpis` for inventory, order and movement KPIs.
- `GET /api/ops/planning/abc` for ABC classification by extended inventory value.
- `GET /api/ops/planning/replenishment?horizon_days=14` for lead-time-aware stock prioritization.
- `POST /api/ops/planning/forecast` with `daily_units`, optional `horizon`, and optional `window` for a moving-average forecast.
- `POST /api/ops/planning/velocity` with `daily_units` to classify demand velocity and variability.
- `POST /api/ops/planning/stock-policy` with demand, lead time and holding/order cost inputs to estimate safety stock, reorder point and EOQ.
- `POST /api/ops/planning/variance` with `expected` and `counted` quantities for count variance calculations.

The forecast is a simple moving-average baseline rather than a machine-learning forecast; provide actual historical daily demand for meaningful estimates. Replenishment currently estimates average demand from the configured reorder level when no transaction-level demand history exists. It should be calibrated against sales/order-line history before being used for purchasing decisions.

Run planning service tests with `python -m unittest tests.test_planning` after installing the project dependencies.

## Warehouse intelligence endpoints

The operations API also exposes decision-support endpoints that return recommendations without silently mutating inventory:

- `GET /api/ops/intelligence/health-score` — inventory availability score and actionable alerts.
- `POST /api/ops/intelligence/capacity` — bin utilization and over-capacity locations (`{"locations":[{"location":"A-01","capacity_units":100,"on_hand":72}]}`).
- `POST /api/ops/intelligence/slotting` — forward-pick, bulk-reserve, and slow-mover zone recommendations (`{"items":[{"sku":"SKU-1","average_daily_demand":8,"quantity":24,"unit_cube":1.2,"location":"A-01"}]}`).
- `POST /api/ops/intelligence/pick-waves` — groups order lines into bounded waves (`{"order_lines":[{"order_id":"SO-1","sku":"SKU-1","quantity":3,"location":"A-01","priority":1}],"max_lines":50,"max_units":500}`).
- `POST /api/ops/intelligence/cycle-counts` — variance review (`{"counts":[{"sku":"SKU-1","expected":10,"counted":8}],"tolerance_percent":0}`).
- `POST /api/ops/intelligence/replenishment` — order recommendations and estimated cost; optionally accepts an `items` array, otherwise uses current products.
- `POST /api/ops/intelligence/supplier-lead-times` — summarizes dated receipt observations (`{"receipts":[{"ordered_date":"2026-01-01","received_date":"2026-01-05","promised_days":5}]}`).

See `LOC_STATUS.md` and run `python tools/loc_audit.py` for a transparent local source-line estimate. The project does **not** claim to meet 500,000 production LOC; that threshold requires a much larger body of independently useful, tested application code.

## Operations analytics expansion

The Operations workspace is reachable at `/operations` and now includes these additional views:

- **Alert center** (`GET /api/ops/analytics/alerts`): prioritizes stockouts, low stock, overdue purchase orders, pending returns, and shipment exceptions.
- **Location analysis** (`GET /api/ops/analytics/locations`): groups SKUs, units, extended inventory value, value share, and at-risk SKUs by storage location.
- **Supplier scorecards** (`GET /api/ops/analytics/suppliers`): summarizes order volume, completion, overdue orders, receipts, and units received. The on-time indicator is only a proxy based on overdue open orders, not a measured supplier SLA.
- **Order analytics** (`GET /api/ops/analytics/orders`): summarizes shipped/open orders, backlog units, ship rate, status distribution, and destination mix.
- **Movement analytics** (`GET /api/ops/analytics/movement?days=30`): groups inbound/outbound movement by day and lists the most active SKUs. The requested window is bounded to 1–365 days.

The analytics are calculated from the current SQLite records. They are operational summaries, not forecasts, and empty history is not interpreted as evidence of supplier or fulfillment performance.
## Operational policy engine

StockPilot includes 700 lazily loaded policy packs with 24 executable controls each. Packs cover inventory integrity, receiving, fulfilment, supplier performance, storage capacity, returns, safety, cold-chain handling, transport readiness, data quality, and related warehouse operations. A pack is imported only when requested, so the web application does not load the full library at startup.

- `GET /api/ops/policies?offset=0&limit=50` lists available packs.
- `POST /api/ops/policies/1/evaluate` evaluates up to 200 JSON records against pack 1. Send `{"records":[{"quantity":0,"temperature_c":9}]}`.
- Each result identifies triggered controls, severity, observed values, thresholds, and recommended corrective action. Missing and invalid measurements are surfaced rather than silently treated as passing.

The policy engine is an operational rule library; thresholds are starter controls and must be calibrated to each facility's documented SOPs and regulatory obligations before production use.
