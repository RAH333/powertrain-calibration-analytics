# powertrain-calibration-analytics
Automated Engine Calibration &amp; Emission Data Analysis Pipeline. 

This showcases understanding about engine architecture, steady-state performance, data acquisition tools (like INCA), emission cycles, and Python scripting for engineering tasks.

# Automated Powertrain Calibration & Emission Analysis Tool

This repository provides an end-to-end Python pipeline engineered for **Automotive Calibration Engineers** to parse engine test bench data, monitor emission limits, identify transient calibration anomalies, and execute automated Root Cause Analysis (RCA).

## Features
- **Data Ingestion**: Parses raw test scripts simulating inputs from acquisition tools like ETAS INCA.
- **Homologation Check**: Flags EGT, Lambda, and NOx anomalies outside emission framework regulations (WLTP/RDE).
- **RCA Automation**: Maps issues directly to optimization actions using engineering-driven scripts.

## Installation & Execution
1. Clone this repo: `git clone https://github.com`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute analysis pipeline: `python main.py`



```
powertrain-calibration-analytics/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── wltp_test_log_raw.csv
│   └── processed/
│       └── clean_calibration_data.csv
├── config/
│   └── calibration_limits.json
├── src/
│   ├── __init__.py
│   ├── data_parser.py
│   ├── calibration_engine.py
│   └── visualization.py
└── main.py
```
