# StockPilot API reference

All operational endpoints are under `/api/ops`. Requests that create or update records use JSON. Errors return a JSON `error` message and an appropriate 4xx response.

## Partner and customer data

- `GET /api/ops/suppliers?active=1` — list suppliers, optionally filtering active status.
- `POST /api/ops/suppliers` — create supplier (`code`, `name`, optional contact fields, `lead_days`).
- `PATCH /api/ops/suppliers/<id>` — update supported supplier fields.
- `GET /api/ops/customers` and `POST /api/ops/customers` — customer directory.

## Procurement and inbound

- `GET /api/ops/purchase-orders` — order headers with line counts and cost totals.
- `POST /api/ops/purchase-orders` — create approved PO with `po_number`, `supplier_id`, optional `expected_date`, and `lines: [{"sku":"SKU-1042","quantity":10,"unit_cost":79.99}]`.
- `GET /api/ops/purchase-orders/<id>` — PO header and lines.
- `POST /api/ops/purchase-orders/<id>/receive` — receive `sku`, `quantity`, `receipt_number`, optional `received_by` and `note`.
- `GET /api/ops/receipts` — receipt ledger.

Receiving validates that the SKU belongs to the PO and that the quantity does not exceed the outstanding ordered amount. Inventory, movement history, PO line quantities, and audit events are updated in one SQLite transaction.

## Warehouse controls

- `POST /api/ops/transfers` — create transfer with `transfer_number`, `sku`, `quantity`, `from_location`, `to_location`, optional `note`.
- `GET /api/ops/transfers` — transfer ledger.
- `POST /api/ops/cycle-counts` — physical count with `count_number`, `sku`, `counted_qty`, optional `counted_by`, `note`. The variance is recorded and stock is reconciled.
- `GET /api/ops/cycle-counts` — cycle-count history.
- `GET /api/ops/reorder-recommendations?limit=100` — items at or below reorder point, suggested quantities, estimated replenishment cost.

## Reverse logistics and shipping

- `POST /api/ops/returns` — create a return using `return_number`, `sku`, `quantity`, `reason`, `disposition`, optional `customer_name`.
- `GET /api/ops/returns` — return ledger.
- `PATCH /api/ops/returns/<return-number>` — resolve using `{"status":"Inspected"}`, `Restocked`, `Scrapped`, or `Rejected`. Restocking adds inventory once; terminal returns cannot be closed twice.
- `POST /api/ops/shipments` — create shipment with `shipment_number`, `carrier`, optional `order_id`, `tracking_number`.
- `GET /api/ops/shipments` — shipment ledger.
- `PATCH /api/ops/shipments/<shipment-number>` — update status among `Label created`, `Ready for pickup`, `In transit`, `Delivered`, `Exception`, `Returned`. Delivered shipments cannot move backwards.

## Audit and reporting

- `GET /api/ops/health` — subsystem health and inventory metrics.
- `GET /api/ops/audit?limit=100` — recent domain events.
- `GET /api/ops/reports/summary` — inventory, order, PO, receipt, return and shipment summary.
- `GET /api/ops/reports/valuation.csv` — inventory valuation export.
- `GET /api/ops/reports/activity.csv` — audit activity export.

## Example requests

```bash
curl -X POST http://127.0.0.1:8000/api/ops/transfers \
  -H 'Content-Type: application/json' \
  -d '{"transfer_number":"TR-1001","sku":"SKU-1042","quantity":2,"from_location":"A-03-02","to_location":"A-04-01"}'
```

```bash
curl -X POST http://127.0.0.1:8000/api/ops/cycle-counts \
  -H 'Content-Type: application/json' \
  -d '{"count_number":"CC-1001","sku":"SKU-1042","counted_qty":31,"counted_by":"Shift lead"}'
```

## Prototype boundaries

This is a local runnable prototype. It does not provide identity management, multi-tenant access controls, external carrier integration, barcode scanner hardware integration, or a distributed database. Do not expose it to the public internet without authentication, authorization, production secret management, deployment hardening, and operational monitoring.
