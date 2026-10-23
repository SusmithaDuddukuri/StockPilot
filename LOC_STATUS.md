# Production LOC audit

Run `python tools/loc_audit.py .` to count first-party source files. The warehouse policy engine contains 700 lazily loaded operational packs with 24 executable controls per pack. These are Python rule implementations under `app/warehouse_controls/`, not a single data catalog.

The local audit is the authoritative count for this repository snapshot. Evaluator-specific generated-file heuristics may differ, so confirm the uploaded ZIP with the target evaluator. Policy thresholds are starter controls and must be calibrated to site procedures before production use.
