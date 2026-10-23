"""Runtime dispatcher for the warehouse operational control library."""
from app.warehouse_controls import catalog_page, load_pack

def list_packs(offset=0, limit=50):
    return {"total_packs": 700, "packs": catalog_page(offset, limit)}

def evaluate_records(pack_id, records):
    if not isinstance(records, list):
        raise ValueError("records must be a list")
    if len(records) > 200:
        raise ValueError("at most 200 records may be evaluated per request")
    try:
        pack = load_pack(int(pack_id))
    except (TypeError, ValueError) as exc:
        raise ValueError(str(exc)) from exc
    results = []
    for index, record in enumerate(records):
        findings = pack.evaluate(record)
        results.append({"record_index": index, "finding_count": len(findings), "findings": findings})
    all_findings = [finding for result in results for finding in result["findings"]]
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    all_findings.sort(key=lambda finding: (severity_order.get(finding.get("severity"), 4), finding.get("rule_id", "")))
    return {"pack_id": int(pack_id), "records_evaluated": len(records), "findings_count": len(all_findings),
            "severity_counts": {severity: sum(f.get("severity") == severity for f in all_findings) for severity in severity_order},
            "results": results, "prioritized_findings": all_findings}
