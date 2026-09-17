# Business Rules — Bookings & Revenue Intelligence

**BR-001 — Booking recognition**  
Only records meeting the approved booking status and period criteria are included in booked value.

**BR-002 — Renewal classification**  
Renewal transactions must be distinguishable from new business, expansion, contraction, and non-renewal.

**BR-003 — Forecast hierarchy**  
Forecast logic must use a documented precedence for booked, committed, pipeline, and management-adjusted values.

**BR-004 — Snapshot comparison**  
Variance analysis compares consistent snapshot dates and avoids mixing refresh times.

**BR-005 — Revenue-stage mapping**  
Each revenue-stage label must map to one governed stage definition.

**BR-006 — Manual adjustments**  
Management adjustments remain separately identifiable from system-generated values.

**BR-007 — Customer hierarchy**  
Bookings and revenue roll through one governed customer hierarchy.

**BR-008 — Fiscal period alignment**  
All measures use the approved fiscal calendar.

**BR-009 — Missing mappings**  
Unmapped region, customer, or stage values are surfaced for review rather than silently reassigned.

**BR-010 — Variance explainability**  
Material forecast movement should be traceable to customer, contract, stage, or management adjustment drivers.