# Inventory Business Rules

- Validate product identifiers before processing stock movements.
- Reject invalid or non-positive quantities where the operation requires positive quantities.
- Prevent stock balances from becoming negative unless an explicitly approved business rule permits it.
- Record adjustments with timestamps and responsible actors.
- Preserve an auditable history of inventory changes.
- Test concurrent updates to avoid lost stock movements.
