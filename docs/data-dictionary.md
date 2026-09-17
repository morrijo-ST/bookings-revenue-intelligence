# Data Dictionary — Bookings & Revenue Intelligence

| Table | Field | Type | Description |
|---|---|---|---|
| dim_customer | customer_id | string | Synthetic customer key |
| dim_customer | customer_name | string | Fictional customer name |
| fact_bookings | booking_id | string | Booking key |
| fact_bookings | customer_id | string | Customer foreign key |
| fact_bookings | booking_date | date | Booking date |
| fact_bookings | booking_value | decimal | Booking value |
| fact_renewals | renewal_id | string | Renewal event key |
| fact_renewals | customer_id | string | Customer foreign key |
| fact_renewals | renewal_date | date | Renewal date |
| fact_renewals | expiring_value | decimal | Value up for renewal |
| fact_revenue | revenue_id | string | Revenue record key |
| fact_revenue | stage | string | Revenue stage |
| fact_revenue | revenue_period | date | Reporting period |
| fact_revenue | revenue_value | decimal | Revenue amount |
| fact_forecast | snapshot_date | date | Forecast snapshot date |
| fact_forecast | forecast_period | date | Forecast period |
| fact_forecast | forecast_value | decimal | Forecast amount |
| fact_adjustments | adjustment_id | string | Management adjustment key |
| fact_adjustments | adjustment_value | decimal | Adjustment amount |
| fact_adjustments | reason | string | Documented rationale |

All public data is synthetic.