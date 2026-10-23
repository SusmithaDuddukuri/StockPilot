"""Audit event writer and read helpers."""
from .validation import optional_text

def record_event(cx, event_type, entity_type, entity_id, summary, actor='Warehouse team'):
    cx.execute('INSERT INTO audit_events(event_type,entity_type,entity_id,summary,actor) VALUES(?,?,?,?,?)',
               (event_type[:60], entity_type[:60], str(entity_id)[:80], summary[:240], actor[:100]))

def recent_events(cx, limit=100):
    limit = max(1, min(int(limit), 500))
    rows = cx.execute('SELECT * FROM audit_events ORDER BY id DESC LIMIT ?', (limit,)).fetchall()
    return [dict(row) for row in rows]
