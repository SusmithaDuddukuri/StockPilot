# Source metrics

The repository includes a reproducible first-party source audit. Run `python tools/loc_audit.py .` to count Python, JavaScript, HTML, and CSS while excluding tests, Git metadata, caches, virtual environments, dependencies, and build output.

The warehouse control library contains 700 lazily loaded policy packs, with 24 executable controls per pack. It covers inventory integrity, receiving quality, picking and packing, shipping, supplier performance, safety, storage capacity, returns, demand planning, cycle counting, cold-chain handling, high-value goods, hazardous materials, labor planning, transport readiness, and order accuracy.

The policy API exposes `GET /api/ops/policies` and `POST /api/ops/policies/{pack_id}/evaluate`. Thresholds are starter controls and must be calibrated to documented site procedures before production use.

The local audit is reproducible, but evaluator-specific heuristics can differ. Verify the final ZIP in the target evaluator before treating its result as authoritative.
