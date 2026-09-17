# Operations Runbook — Bookings & Revenue Intelligence

## Refresh Sequence
1. Validate source-system refresh completion.
2. Confirm Snowflake views are current.
3. Validate booking, renewal, revenue, and forecast row counts.
4. Reconcile headline totals to control reports.
5. Refresh the Power BI semantic model.
6. Review variance outputs and management adjustments.
7. Publish executive reporting only after reconciliation.

## Common Failures
### Snapshot mismatch
Confirm prior/current snapshots use comparable cut-off times and fiscal periods.

### Forecast discrepancy
Review forecast precedence, manual adjustments, stage mappings, and filter context.

### Missing customer / region mapping
Route to the mapping exception list and correct upstream logic where possible.

### Revenue-stage issue
Validate the source stage and governed stage mapping before publication.

## Publication Control
Bookings, forecast, and revenue totals should reconcile to approved source controls before executive distribution.