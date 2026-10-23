import csv
import io
import re
import sqlite3

from flask import Blueprint, current_app, jsonify, render_template, request, Response

from .store import connect
from .services import planning
from .services.audit import record_event
from .services import barcode_service

bp = Blueprint("main", __name__)


def db():
    return connect(current_app.config["DATABASE"])


def product_dict(row):
    return dict(row)


def validate_sku(value):
    if not isinstance(value, str):
        return False

    sku = value.strip().upper()

    if not sku or len(sku) > 40:
        return False

    return re.fullmatch(r"[A-Z0-9][A-Z0-9_-]*", sku) is not None


@bp.get("/")
def home():
    return render_template("index.html")


@bp.get("/operations")
def operations_workspace():
    return render_template("operations.html")


@bp.get("/api/overview")
def overview():
    with db() as cx:
        total = cx.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        units = cx.execute(
            "SELECT COALESCE(SUM(quantity), 0) FROM products"
        ).fetchone()[0]

        low = cx.execute(
            "SELECT COUNT(*) FROM products WHERE quantity <= reorder_level"
        ).fetchone()[0]

        value = cx.execute(
            "SELECT COALESCE(SUM(quantity * unit_cost), 0) FROM products"
        ).fetchone()[0]

        orders = cx.execute(
            "SELECT COUNT(*) FROM orders WHERE status != 'Shipped'"
        ).fetchone()[0]

        recent = cx.execute(
            """
            SELECT m.*, p.name
            FROM movements m
            JOIN products p USING(sku)
            ORDER BY m.id DESC
            LIMIT 6
            """
        ).fetchall()

    return jsonify({
        "products": total,
        "units": units,
        "low_stock": low,
        "inventory_value": round(value, 2),
        "open_orders": orders,
        "recent": [dict(row) for row in recent]
    })


@bp.get("/api/products")
def products():
    search = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    state = request.args.get("state", "").strip()

    sql = """
        SELECT *
        FROM products
        WHERE (sku LIKE ? OR name LIKE ? OR supplier LIKE ?)
    """

    params = [f"%{search}%"] * 3

    if category:
        sql += " AND category = ?"
        params.append(category)

    if state == "low":
        sql += " AND quantity <= reorder_level"
    elif state == "healthy":
        sql += " AND quantity > reorder_level"

    sql += """
        ORDER BY
            CASE WHEN quantity <= reorder_level THEN 0 ELSE 1 END,
            name
    """

    with db() as cx:
        rows = cx.execute(sql, params).fetchall()

    return jsonify([product_dict(row) for row in rows])


@bp.post("/api/products")
def add_product():
    data = request.get_json(silent=True) or {}

    raw_sku = data.get("sku")

    if not validate_sku(raw_sku):
        return jsonify(
            error=(
                "SKU must be 1Ã¢â‚¬â€œ40 characters and contain only "
                "letters, numbers, hyphens, or underscores."
            )
        ), 400

    required = [
        "sku",
        "name",
        "category",
        "quantity",
        "reorder_level",
        "unit_cost",
        "location",
        "supplier"
    ]

    if any(
        data.get(key) is None or str(data.get(key)).strip() == ""
        for key in required
    ):
        return jsonify(error="Complete every product field."), 400

    try:
        quantity = int(data["quantity"])
        reorder_level = int(data["reorder_level"])
        unit_cost = float(data["unit_cost"])

        if (
            quantity < 0
            or reorder_level < 0
            or unit_cost < 0
        ):
            raise ValueError

    except (TypeError, ValueError):
        return jsonify(
            error="Quantity, reorder level and cost must be non-negative numbers."
        ), 400

    sku = raw_sku.strip().upper()

    try:
        with db() as cx:
            cx.execute(
                """
                INSERT INTO products
                (
                    sku,
                    name,
                    category,
                    quantity,
                    reorder_level,
                    unit_cost,
                    location,
                    supplier
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    sku,
                    data["name"].strip(),
                    data["category"].strip(),
                    quantity,
                    reorder_level,
                    unit_cost,
                    data["location"].strip(),
                    data["supplier"].strip()
                )
            )

            if quantity > 0:
                cx.execute(
                    """
                    INSERT INTO movements (sku, delta, note)
                    VALUES (?, ?, ?)
                    """,
                    (sku, quantity, "Initial stock")
                )

    except sqlite3.IntegrityError:
        return jsonify(
            error="That SKU already exists or the values are invalid."
        ), 409

    return jsonify(message="Product created."), 201


@bp.post("/api/movements")
def movement():
    data = request.get_json(silent=True) or {}

    try:
        delta = int(data.get("delta", 0))
    except (TypeError, ValueError):
        delta = 0

    sku = str(data.get("sku", "")).strip().upper()
    note = str(data.get("note", "Stock adjustment")).strip()[:160]

    if not sku or delta == 0:
        return jsonify(
            error="Choose a SKU and enter a non-zero quantity change."
        ), 400

    with db() as cx:
        item = cx.execute(
            "SELECT quantity FROM products WHERE sku = ?",
            (sku,)
        ).fetchone()

        if not item:
            return jsonify(error="Product not found."), 404

        if item["quantity"] + delta < 0:
            return jsonify(error="Stock cannot fall below zero."), 400

        cx.execute(
            """
            UPDATE products
            SET quantity = quantity + ?, updated_at = CURRENT_TIMESTAMP
            WHERE sku = ?
            """,
            (delta, sku)
        )

        cx.execute(
            """
            INSERT INTO movements (sku, delta, note)
            VALUES (?, ?, ?)
            """,
            (sku, delta, note or "Stock adjustment")
        )

    return jsonify(message="Stock movement saved."), 201


@bp.get("/api/movements")
def movements():
    with db() as cx:
        rows = cx.execute(
            """
            SELECT m.*, p.name
            FROM movements m
            JOIN products p USING(sku)
            ORDER BY m.id DESC
            LIMIT 100
            """
        ).fetchall()

    return jsonify([dict(row) for row in rows])


@bp.get("/api/orders")
def orders():
    with db() as cx:
        rows = cx.execute(
            "SELECT * FROM orders ORDER BY id DESC"
        ).fetchall()

    return jsonify([dict(row) for row in rows])


@bp.post("/api/orders/<int:order_id>/status")
def update_order(order_id):
    data = request.get_json(silent=True) or {}
    status = data.get("status")

    allowed = {
        "Picking",
        "Packed",
        "Awaiting stock",
        "Shipped"
    }

    if status not in allowed:
        return jsonify(error="Choose a valid order status."), 400

    with db() as cx:
        cur = cx.execute(
            "UPDATE orders SET status = ? WHERE id = ?",
            (status, order_id)
        )

        if not cur.rowcount:
            return jsonify(error="Order not found."), 404

    return jsonify(message="Order status updated.")


@bp.get("/api/export.csv")
def export_csv():
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                sku,
                name,
                category,
                quantity,
                reorder_level,
                unit_cost,
                location,
                supplier,
                updated_at
            FROM products
            ORDER BY name
            """
        ).fetchall()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "SKU",
        "Product",
        "Category",
        "Quantity",
        "Reorder level",
        "Unit cost",
        "Location",
        "Supplier",
        "Updated at"
    ])

    for row in rows:
        writer.writerow(list(row))

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
                "attachment; filename=stockpilot-inventory.csv"
        }
    )

@bp.get("/api/alerts/low-stock")
def low_stock_alerts():
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                sku,
                name,
                category,
                quantity,
                reorder_level,
                location,
                supplier,
                CASE
                    WHEN quantity = 0 THEN 'Out of stock'
                    ELSE 'Low stock'
                END AS alert_type,
                MAX(0, reorder_level - quantity) AS shortage
            FROM products
            WHERE quantity <= reorder_level
            ORDER BY
                CASE WHEN quantity = 0 THEN 0 ELSE 1 END,
                quantity ASC,
                name ASC
            """
        ).fetchall()

    return jsonify({
        "count": len(rows),
        "alerts": [dict(row) for row in rows]
    })
@bp.get("/api/warehouse/bin-utilization")
def warehouse_bin_utilization():
    """Calculate storage bin utilization and zone distribution from live products."""
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                location,
                COUNT(sku) AS sku_count,
                COALESCE(SUM(quantity), 0) AS total_units,
                COALESCE(SUM(quantity * unit_cost), 0.0) AS total_value
            FROM products
            GROUP BY location
            ORDER BY total_units DESC, location ASC
            """
        ).fetchall()

    bins = []
    default_bin_capacity = 250
    total_capacity = 0
    total_occupied = 0

    for row in rows:
        loc = row["location"]
        units = int(row["total_units"])
        val = round(float(row["total_value"]), 2)
        skus = int(row["sku_count"])
        cap = default_bin_capacity
        total_capacity += cap
        total_occupied += units
        util_pct = round((units / cap) * 100, 2) if cap else 0.0

        if util_pct >= 90.0:
            status = "Near capacity"
        elif util_pct >= 40.0:
            status = "Balanced"
        else:
            status = "Underutilized"

        zone = loc.split("-")[0] if "-" in loc else "General"

        bins.append({
            "location": loc,
            "zone": zone,
            "sku_count": skus,
            "units": units,
            "capacity": cap,
            "utilization_percent": util_pct,
            "status": status,
            "inventory_value": val
        })

    overall_utilization = round((total_occupied / total_capacity * 100), 2) if total_capacity else 0.0

    return jsonify({
        "bin_count": len(bins),
        "total_units": total_occupied,
        "total_capacity": total_capacity,
        "overall_utilization_percent": overall_utilization,
        "bins": bins
    })
@bp.get("/api/reports/category-valuation")
def category_valuation_report():
    """Generate category-level breakdown of inventory volume, valuation, and portfolio share."""
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                category,
                COUNT(sku) AS sku_count,
                COALESCE(SUM(quantity), 0) AS total_units,
                COALESCE(AVG(unit_cost), 0.0) AS avg_unit_cost,
                COALESCE(SUM(quantity * unit_cost), 0.0) AS total_value,
                SUM(CASE WHEN quantity <= reorder_level THEN 1 ELSE 0 END) AS low_stock_skus
            FROM products
            GROUP BY category
            ORDER BY total_value DESC, category ASC
            """
        ).fetchall()

    portfolio_value = sum(float(row["total_value"]) for row in rows)
    portfolio_units = sum(int(row["total_units"]) for row in rows)

    breakdown = []
    for row in rows:
        val = round(float(row["total_value"]), 2)
        share = round((val / portfolio_value * 100), 2) if portfolio_value else 0.0
        breakdown.append({
            "category": row["category"],
            "sku_count": int(row["sku_count"]),
            "total_units": int(row["total_units"]),
            "average_unit_cost": round(float(row["avg_unit_cost"]), 2),
            "total_value": val,
            "portfolio_share_percent": share,
            "low_stock_skus": int(row["low_stock_skus"])
        })

    return jsonify({
        "category_count": len(breakdown),
        "portfolio_units": portfolio_units,
        "portfolio_value": round(portfolio_value, 2),
        "categories": breakdown
    })
@bp.get("/api/export/catalog-manifest")
def export_catalog_manifest():
    """Export standardized JSON manifest of inventory catalog with status flags and checksum."""
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                sku,
                name,
                category,
                quantity,
                reorder_level,
                unit_cost,
                location,
                supplier,
                updated_at
            FROM products
            ORDER BY sku ASC
            """
        ).fetchall()

    items = []
    total_valuation = 0.0
    total_units = 0

    for row in rows:
        qty = int(row["quantity"])
        cost = float(row["unit_cost"])
        reorder = int(row["reorder_level"])
        extended = round(qty * cost, 2)
        total_valuation += extended
        total_units += qty

        if qty == 0:
            stock_status = "Stockout"
            urgency = "Critical"
        elif qty <= reorder:
            stock_status = "Low stock"
            urgency = "High"
        elif qty >= (reorder * 3):
            stock_status = "Surplus"
            urgency = "Low"
        else:
            stock_status = "Optimal"
            urgency = "Normal"

        items.append({
            "sku": row["sku"],
            "name": row["name"],
            "category": row["category"],
            "quantity": qty,
            "reorder_level": reorder,
            "unit_cost": cost,
            "extended_value": extended,
            "location": row["location"],
            "supplier": row["supplier"],
            "stock_status": stock_status,
            "replenishment_urgency": urgency,
            "last_synced_at": row["updated_at"]
        })

    return jsonify({
        "format": "StockPilot Catalog Exchange",
        "item_count": len(items),
        "total_units": total_units,
        "total_valuation": round(total_valuation, 2),
        "catalog": items
    })
@bp.get("/api/replenishment/recommendations")
def replenishment_recommendations():
    """Generate intelligent replenishment suggestions based on buffer gaps and supplier lead times."""
    with db() as cx:
        rows = cx.execute(
            """
            SELECT
                p.sku,
                p.name,
                p.category,
                p.quantity,
                p.reorder_level,
                p.unit_cost,
                p.supplier,
                COALESCE(s.lead_days, 7) AS lead_days
            FROM products p
            LEFT JOIN suppliers s ON s.name = p.supplier AND s.active = 1
            ORDER BY
                CASE WHEN p.quantity = 0 THEN 0 ELSE 1 END,
                (p.reorder_level - p.quantity) DESC,
                p.name ASC
            """
        ).fetchall()

    recommendations = []
    total_estimated_budget = 0.0

    for r in rows:
        qty = int(r["quantity"])
        reorder = int(r["reorder_level"])
        cost = float(r["unit_cost"])
        lead = int(r["lead_days"])

        target_buffer = max(reorder * 2, 20)
        suggested_order_qty = max(0, target_buffer - qty)

        if suggested_order_qty > 0:
            est_cost = round(suggested_order_qty * cost, 2)
            total_estimated_budget += est_cost

            if qty == 0:
                urgency = "Critical"
                action = "Expedited procurement needed immediately"
            elif qty <= (reorder // 2):
                urgency = "High"
                action = "Issue purchase order promptly"
            elif qty <= reorder:
                urgency = "Moderate"
                action = "Include in weekly vendor replenishment cycle"
            else:
                urgency = "Routine"
                action = "Monitor stock run-rate"

            recommendations.append({
                "sku": r["sku"],
                "name": r["name"],
                "category": r["category"],
                "on_hand": qty,
                "reorder_level": reorder,
                "lead_days": lead,
                "target_buffer": target_buffer,
                "suggested_order_units": suggested_order_qty,
                "unit_cost": cost,
                "estimated_order_cost": est_cost,
                "supplier": r["supplier"],
                "urgency": urgency,
                "recommended_action": action
            })

    return jsonify({
        "item_count": len(recommendations),
        "total_estimated_budget": round(total_estimated_budget, 2),
        "recommendations": recommendations
    })


@bp.get("/api/reports/deadstock-analysis")
def deadstock_analysis():
    """Identify slow-moving and deadstock inventory with liquidation markdown recommendations."""
    category_filter = request.args.get("category", "").strip()

    with db() as cx:
        query = """
            SELECT 
                p.sku,
                p.name,
                p.category,
                p.quantity,
                p.reorder_level,
                p.unit_cost,
                p.location,
                p.supplier,
                p.updated_at,
                COUNT(m.id) as movement_count,
                COALESCE(MAX(m.created_at), p.updated_at) as last_activity
            FROM products p
            LEFT JOIN movements m ON p.sku = m.sku
        """
        params = []
        if category_filter:
            query += " WHERE LOWER(p.category) = LOWER(?)"
            params.append(category_filter)

        query += " GROUP BY p.sku ORDER BY p.quantity * p.unit_cost DESC"
        rows = cx.execute(query, params).fetchall()

    items = []
    total_deadstock_value = 0.0
    total_deadstock_units = 0

    for r in rows:
        qty = int(r["quantity"])
        cost = float(r["unit_cost"])
        reorder = int(r["reorder_level"])
        val = round(qty * cost, 2)
        movements = int(r["movement_count"])

        if qty > 0 and movements == 0:
            classification = "Deadstock"
            liquidation_discount = 0.40
            liquidation_channel = "Secondary Wholesale / Clearance Auction"
            recommended_action = "Initiate immediate inventory liquidation"
            total_deadstock_value += val
            total_deadstock_units += qty
        elif qty > (reorder * 2) and movements <= 2:
            classification = "Slow-moving"
            liquidation_discount = 0.20
            liquidation_channel = "Flash Sale / Bundle Offer"
            recommended_action = "Apply promotional bundle pricing to accelerate turnover"
            total_deadstock_value += val
            total_deadstock_units += qty
        elif qty == 0:
            classification = "Depleted"
            liquidation_discount = 0.0
            liquidation_channel = "N/A"
            recommended_action = "Review SKU continuation or archive"
        else:
            classification = "Active"
            liquidation_discount = 0.0
            liquidation_channel = "Standard Channels"
            recommended_action = "Maintain regular replenishment cycle"

        estimated_recovery_value = round(val * (1.0 - liquidation_discount), 2)

        items.append({
            "sku": r["sku"],
            "name": r["name"],
            "category": r["category"],
            "quantity": qty,
            "unit_cost": cost,
            "inventory_value": val,
            "location": r["location"],
            "supplier": r["supplier"],
            "movement_count": movements,
            "last_activity": r["last_activity"],
            "classification": classification,
            "recommended_discount_pct": int(liquidation_discount * 100),
            "estimated_recovery_value": estimated_recovery_value,
            "liquidation_channel": liquidation_channel,
            "recommended_action": recommended_action
        })

    deadstock_items = [i for i in items if i["classification"] in ("Deadstock", "Slow-moving")]

    return jsonify({
        "analyzed_sku_count": len(items),
        "deadstock_sku_count": len(deadstock_items),
        "total_tied_up_capital": round(total_deadstock_value, 2),
        "total_at_risk_units": total_deadstock_units,
        "items": items
    })


@bp.get("/api/replenishment/dynamic-safety-stock")
def dynamic_safety_stock():
    """Calculate statistical safety stock, dynamic reorder points, and stockout risk."""
    service_level = request.args.get("service_level", "95").strip()
    service_factors = {
        "90": 1.28,
        "95": 1.65,
        "99": 2.33,
    }
    z_factor = service_factors.get(service_level, 1.65)

    with db() as cx:
        products = cx.execute("""
            SELECT 
                p.sku,
                p.name,
                p.category,
                p.quantity,
                p.reorder_level,
                p.unit_cost,
                p.supplier,
                COALESCE(s.lead_days, 7) as lead_days
            FROM products p
            LEFT JOIN suppliers s ON p.supplier = s.name
            ORDER BY p.sku ASC
        """).fetchall()

        movements = cx.execute("""
            SELECT sku, delta
            FROM movements
            WHERE delta < 0
        """).fetchall()

    demand_map = {}
    for m in movements:
        sku = m["sku"]
        if sku not in demand_map:
            demand_map[sku] = []
        demand_map[sku].append(abs(int(m["delta"])))

    skus = []
    total_reorder_cost = 0.0
    at_risk_count = 0
    reorder_count = 0

    for p in products:
        sku = p["sku"]
        on_hand = int(p["quantity"])
        static_reorder = int(p["reorder_level"])
        cost = float(p["unit_cost"])
        lead_time = max(1, int(p["lead_days"]))

        observed_demand = demand_map.get(sku, [max(1.0, round(static_reorder / 7.0, 2))])
        velocity = planning.demand_velocity(observed_demand)
        avg_daily = max(0.1, velocity["average_daily_units"])
        stddev = velocity["standard_deviation"] if velocity["standard_deviation"] > 0 else round(avg_daily * 0.25, 2)

        calculated_ss = planning.safety_stock(z_factor, stddev, lead_time)
        dynamic_rop = planning.reorder_point(avg_daily, lead_time, calculated_ss)

        if on_hand == 0:
            posture = "Stockout"
            priority = "Emergency"
            at_risk_count += 1
        elif on_hand < calculated_ss:
            posture = "Critical Safety Breach"
            priority = "High"
            at_risk_count += 1
        elif on_hand <= dynamic_rop:
            posture = "Reorder Triggered"
            priority = "Elevated"
        elif on_hand > (dynamic_rop * 2.5):
            posture = "Overstocked"
            priority = "Low"
        else:
            posture = "Optimal Buffer"
            priority = "Normal"

        suggested_order_qty = max(0, (dynamic_rop * 2) - on_hand)
        if suggested_order_qty > 0 and posture in ("Stockout", "Critical Safety Breach", "Reorder Triggered"):
            reorder_count += 1
            line_cost = round(suggested_order_qty * cost, 2)
            total_reorder_cost += line_cost
        else:
            suggested_order_qty = 0
            line_cost = 0.0

        skus.append({
            "sku": sku,
            "name": p["name"],
            "category": p["category"],
            "on_hand": on_hand,
            "static_reorder_level": static_reorder,
            "lead_time_days": lead_time,
            "average_daily_demand": avg_daily,
            "demand_stddev": stddev,
            "calculated_safety_stock": calculated_ss,
            "dynamic_reorder_point": dynamic_rop,
            "stock_posture": posture,
            "priority": priority,
            "suggested_order_units": suggested_order_qty,
            "estimated_reorder_cost": line_cost,
            "supplier": p["supplier"]
        })

    return jsonify({
        "service_level_target": f"{service_level}%",
        "z_score": z_factor,
        "total_skus_evaluated": len(skus),
        "at_risk_sku_count": at_risk_count,
        "recommended_reorder_count": reorder_count,
        "total_recommended_reorder_cost": round(total_reorder_cost, 2),
        "skus": skus
    })


@bp.get("/api/shipping/manifest")
def shipping_manifest():
    """Generate carrier trailer dispatch manifest and bill of lading report."""
    carrier_filter = request.args.get("carrier", "").strip()
    status_filter = request.args.get("status", "").strip()

    with db() as cx:
        query = """
            SELECT 
                sh.id,
                sh.shipment_number,
                sh.carrier,
                sh.tracking_number,
                sh.status,
                sh.shipped_at,
                sh.delivered_at,
                sh.created_at,
                COALESCE(o.customer, 'Direct Client') as customer,
                COALESCE(o.destination, 'Distribution Hub') as destination,
                COALESCE(o.item_count, 1) as item_count,
                COALESCE(o.status, 'Ready for Dispatch') as order_status
            FROM shipments sh
            LEFT JOIN orders o ON sh.order_id = o.id
        """
        clauses = []
        params = []
        if carrier_filter:
            clauses.append("LOWER(sh.carrier) = LOWER(?)")
            params.append(carrier_filter)
        if status_filter:
            clauses.append("LOWER(sh.status) = LOWER(?)")
            params.append(status_filter)

        if clauses:
            query += " WHERE " + " AND ".join(clauses)

        query += " ORDER BY sh.created_at DESC"
        rows = cx.execute(query, params).fetchall()

    shipments = []
    total_packages = len(rows)
    total_units = 0
    destinations = set()
    carriers = set()

    for r in rows:
        units = int(r["item_count"])
        total_units += units
        destinations.add(r["destination"])
        carriers.add(r["carrier"])

        shipments.append({
            "shipment_number": r["shipment_number"],
            "order_status": r["order_status"],
            "carrier": r["carrier"],
            "tracking_number": r["tracking_number"] or "PENDING-LABEL",
            "status": r["status"],
            "recipient_customer": r["customer"],
            "destination_city": r["destination"],
            "package_item_count": units,
            "created_at": r["created_at"],
            "shipped_at": r["shipped_at"] or None,
            "dispatch_verified": bool(r["shipped_at"] or r["status"] in ("In transit", "Delivered"))
        })

    manifest_id = f"MNF-{abs(hash(carrier_filter or 'ALL')) % 100000:05d}"

    return jsonify({
        "manifest_reference": manifest_id,
        "carrier_filter": carrier_filter or "ALL_CARRIERS",
        "status_filter": status_filter or "ALL_STATUSES",
        "total_shipments": total_packages,
        "total_items_to_dispatch": total_units,
        "distinct_destinations_count": len(destinations),
        "active_carriers": sorted(list(carriers)),
        "shipments": shipments
    })


@bp.get("/api/shipping/manifest.csv")
def export_shipping_manifest_csv():
    """Export shipping manifest as a carrier-compliant CSV document."""
    carrier_filter = request.args.get("carrier", "").strip()
    status_filter = request.args.get("status", "").strip()

    with db() as cx:
        query = """
            SELECT 
                sh.shipment_number,
                sh.carrier,
                sh.tracking_number,
                sh.status,
                COALESCE(o.customer, 'Direct Client') as customer,
                COALESCE(o.destination, 'Distribution Hub') as destination,
                COALESCE(o.item_count, 1) as item_count,
                sh.created_at
            FROM shipments sh
            LEFT JOIN orders o ON sh.order_id = o.id
        """
        clauses = []
        params = []
        if carrier_filter:
            clauses.append("LOWER(sh.carrier) = LOWER(?)")
            params.append(carrier_filter)
        if status_filter:
            clauses.append("LOWER(sh.status) = LOWER(?)")
            params.append(status_filter)

        if clauses:
            query += " WHERE " + " AND ".join(clauses)

        query += " ORDER BY sh.created_at DESC"
        rows = cx.execute(query, params).fetchall()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Shipment Number", "Carrier", "Tracking Number", "Status",
        "Customer", "Destination", "Item Count", "Created At"
    ])

    for r in rows:
        writer.writerow([
            r["shipment_number"],
            r["carrier"],
            r["tracking_number"] or "N/A",
            r["status"],
            r["customer"],
            r["destination"],
            r["item_count"],
            r["created_at"]
        ])

    csv_data = output.getvalue()
    filename = f"shipping-manifest-{carrier_filter or 'all'}.csv"
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )


@bp.post("/api/barcode/verify")
def verify_barcode_endpoint():
    """Verify barcode symbology compliance and calculate check digits."""
    data = request.get_json(silent=True) or {}
    code = data.get("barcode", "")
    symbology = data.get("symbology", "Code128")
    sku = data.get("sku")

    result = barcode_service.verify_barcode(code, symbology)

    if sku:
        with db() as cx:
            product = cx.execute("SELECT sku, name, location FROM products WHERE sku = ?", (sku,)).fetchone()
            if product:
                result["linked_product"] = {
                    "sku": product["sku"],
                    "name": product["name"],
                    "location": product["location"]
                }
            else:
                result["linked_product"] = None

    status_code = 200 if result.get("valid") else 422
    return jsonify(result), status_code


@bp.get("/api/barcode/label-spec/<sku>")
def get_label_spec(sku):
    """Generate standardized shelf and packaging label specification for a SKU."""
    with db() as cx:
        product = cx.execute(
            "SELECT sku, name, category, location, unit_cost FROM products WHERE sku = ?",
            (sku,)
        ).fetchone()

    if not product:
        return jsonify(error="Product not found."), 404

    # Calculate default EAN-13 payload based on SKU numbers or fallback
    digits = re.sub(r"\D", "", sku)
    if len(digits) >= 12:
        ean_base = digits[:12]
    else:
        ean_base = (digits + "000000000000")[:12]

    ean_check = barcode_service.calculate_ean13_check_digit(ean_base)
    ean13_code = f"{ean_base}{ean_check}"

    return jsonify({
        "sku": product["sku"],
        "name": product["name"],
        "category": product["category"],
        "warehouse_location": product["location"],
        "primary_symbology": "Code 128",
        "barcode_payload": product["sku"],
        "ean13_payload": ean13_code,
        "label_dimensions_mm": {
            "width": 101.6,
            "height": 50.8
        },
        "print_specifications": {
            "dpi": 300,
            "quiet_zone_mm": 6.35,
            "human_readable_text": True,
            "barcode_height_mm": 25.4
        }
    })


@bp.get("/api/orders/backorders/queue")
def backorder_queue():
    """Evaluate and rank pending backorders with inventory allocation estimates."""
    with db() as cx:
        orders = cx.execute("""
            SELECT id, customer, status, item_count, destination, created_at
            FROM orders
            WHERE LOWER(status) = 'awaiting stock'
            ORDER BY created_at ASC, id ASC
        """).fetchall()

        inventory_sum = cx.execute("SELECT COALESCE(SUM(quantity), 0) FROM products").fetchone()[0]

    total_backordered_units = sum(int(o["item_count"]) for o in orders)
    available_pool = int(inventory_sum)
    remaining_pool = available_pool

    queue = []
    for rank, o in enumerate(orders, start=1):
        req = int(o["item_count"])
        allocated = min(req, remaining_pool)
        remaining_pool -= allocated
        shortage = req - allocated

        fulfillment_pct = round((allocated / req) * 100, 1) if req > 0 else 100.0
        status_flag = "Fully Allocatable" if shortage == 0 else ("Partially Allocatable" if allocated > 0 else "Blocked by Stockout")

        queue.append({
            "queue_position": rank,
            "order_id": o["id"],
            "customer": o["customer"],
            "destination": o["destination"],
            "item_count": req,
            "units_allocatable": allocated,
            "units_shortage": shortage,
            "fulfillment_percentage": fulfillment_pct,
            "allocation_posture": status_flag,
            "created_at": o["created_at"]
        })

    return jsonify({
        "backorder_count": len(orders),
        "total_units_demanded": total_backordered_units,
        "available_units_in_pool": available_pool,
        "total_units_allocatable": available_pool - remaining_pool,
        "unmet_shortage_units": max(0, total_backordered_units - available_pool),
        "allocation_queue": queue
    })


@bp.post("/api/orders/backorders/release-to-picking")
def release_backorders_to_picking():
    """Transition allocatable backorders from 'Awaiting stock' to 'Picking'."""
    data = request.get_json(silent=True) or {}
    order_id = data.get("order_id")

    with db() as cx:
        if order_id is not None:
            order = cx.execute(
                "SELECT id, status, customer, item_count FROM orders WHERE id = ?",
                (order_id,)
            ).fetchone()
            if not order:
                return jsonify(error="Order not found."), 404
            if order["status"].lower() != "awaiting stock":
                return jsonify(error=f"Order is not in backorder state (current: {order['status']})."), 400

            cx.execute("UPDATE orders SET status = 'Picking' WHERE id = ?", (order_id,))
            record_event(cx, "orders.backorder_released", "order", str(order_id),
                         f"Backorder released to picking for {order['customer']} ({order['item_count']} units).")
            return jsonify(message=f"Order #{order_id} released from backorder queue to Picking.", released_orders=[order_id])

        backorders = cx.execute(
            "SELECT id, customer, item_count FROM orders WHERE LOWER(status) = 'awaiting stock' ORDER BY created_at ASC"
        ).fetchall()

        if not backorders:
            return jsonify(message="No pending backorders to release.", released_count=0, released_orders=[])

        released_ids = []
        for o in backorders:
            cx.execute("UPDATE orders SET status = 'Picking' WHERE id = ?", (o["id"],))
            record_event(cx, "orders.backorder_released", "order", str(o["id"]),
                         f"Automated release to picking for {o['customer']}.")
            released_ids.append(o["id"])

        return jsonify({
            "message": f"Successfully released {len(released_ids)} backorders to Picking.",
            "released_count": len(released_ids),
            "released_orders": released_ids
        })
