# Bookings & Revenue Intelligence

An executive analytics reference for bookings, weighted pipeline, renewals, revenue stages, and forecast performance across a Snowflake-backed BI architecture.

> **Live demo:** https://bookings-revenue-intelligence.onrender.com

> **Working public demo:** Includes deterministic synthetic bookings data, executable forecast/revenue logic, an interactive Streamlit app, tests, and run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** Employer-specific data, internal names, credentials, customer information, and proprietary business logic are excluded.

## Try It

**Hosted:** https://bookings-revenue-intelligence.onrender.com

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Business Problem

Finance and commercial teams need a consistent view of bookings, forecast stages, renewals, revenue, and management expectations. The challenge is aligning those sources and definitions into a governed analytical model rather than producing isolated reports.

## Demo Capabilities

- Closed Won bookings
- Commit / Best Case / Pipeline stage analysis
- probability-weighted pipeline
- recognized revenue
- renewal value
- weekly trend analysis
- regional performance

## Reference Architecture

```text
CRM / Renewal / Revenue / Adjustment Data
                  |
                  v
              Snowflake
                  |
         Curated finance model
                  |
        Power BI semantic layer
                  |
    Forecast / Variance / Revenue logic
                  |
          Executive dashboards
```

## Technology

`Snowflake` `Power BI` `DAX` `SQL` `Python` `Streamlit` `Plotly` `FP&A` `Forecasting` `Revenue Analytics`

## Demo Status

- [x] Public-safe project definition
- [x] Synthetic bookings / renewal / revenue dataset
- [x] Executable weighted-pipeline and revenue logic
- [x] Interactive dashboard demo
- [x] Automated tests
- [x] Finance documentation / controls
- [x] Hosted live-demo URL
- [ ] Sanitized Power BI screenshot gallery
- [ ] Recorded walkthrough
