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