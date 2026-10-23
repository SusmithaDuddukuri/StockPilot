import csv
import io
import re
import sqlite3

from flask import Blueprint, current_app, jsonify, render_template, request, Response

from .store import connect

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
                "SKU must be 1–40 characters and contain only "
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
