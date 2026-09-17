# Architecture — Bookings & Revenue Intelligence

## System Overview

```text
CRM / Renewal / Revenue / Adjustments
                |
                v
            Snowflake
                |
      Curated Finance Views
                |
        Power BI Semantic Model
                |
   +------------+-------------+
   |            |             |
Bookings    Forecasting    Variance
   |            |             |
   +------------+-------------+
                |
        Executive Reporting
```

## Design Principles
- Snowflake centralizes source-system integration.
- Power BI holds governed reporting logic and interactive analysis.
- Forecast views distinguish booked, committed, pipeline, and management adjustments.
- Prior-period comparisons use a consistent snapshot method.
- Variance analysis should explain movement rather than only display totals.

## Major Subject Areas
### Bookings
Current-period bookings by business, region, customer, and contract.

### Renewals
Renewal timing, term, and forward exposure.

### Revenue Stage
Revenue opportunity or realization by stage and period.

### Forecasting
Bottom-up and live forecast views with transparent assumptions.

### Variance
Current versus prior forecast / prior snapshot movement with drill-down to primary drivers.

## Public Reference Design
The portfolio implementation will use synthetic data and a simplified semantic model while preserving the original enterprise architecture concepts.