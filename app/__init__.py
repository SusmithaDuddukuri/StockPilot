import os
from flask import Flask
from .routes import bp
from .store import init_db
from .api.operations import bp as operations_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("STOCKPILOT_SECRET") or os.urandom(32).hex(),
        DATABASE=os.environ.get("STOCKPILOT_DB", os.path.join(app.instance_path, "stockpilot.sqlite3")),
    )
    if test_config:
        app.config.update(test_config)
    os.makedirs(app.instance_path, exist_ok=True)
    init_db(app.config["DATABASE"])
    app.register_blueprint(bp)
    app.register_blueprint(operations_bp)

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        response.headers.setdefault("Cache-Control", "no-store")
        return response
    @app.get("/health")
    def health():
        return {"status": "ok", "service": "StockPilot"}
    return app
