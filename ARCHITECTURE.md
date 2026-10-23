# Architecture

- `run.py` creates the Flask application.
- `app/__init__.py` configures paths and registers routes.
- `app/routes.py` implements the JSON API and page route.
- `app/store.py` owns SQLite initialization, schema, seed data, and connection lifecycle.
- `app/templates/index.html` defines the accessible page structure and forms.
- `app/static/app.js` drives API requests, navigation, filters, dialogs, and feedback.
- `app/static/style.css` provides responsive layout and component styling.
- `tests/test_app.py` covers happy paths, validation, stock boundaries, order status, and CSV export.

SQLite writes are committed per request operation. Foreign keys and quantity constraints are enabled. The server validates product fields, stock deltas, and order statuses before writes.
