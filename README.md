# PythonSecurityLogAnalyzer
A Python‑based security analysis tool that parses, filters, and evaluates systemd journal logs to detect suspicious activity, authentication anomalies, and potential security incidents on Linux systems.

Still in progress!

---

## 📌 Overview

The **Security Log Analyzer for systemd** helps security analysts, system administrators, and researchers identify unusual or malicious behavior by analyzing logs collected through `journald`.  
It focuses on authentication events, service failures, privilege escalations, and network-related anomalies.

This project demonstrates skills in:

- Python scripting  
- Log analysis  
- Linux security  
- Threat detection  
- Automation  

---

## 🚀 Features

- Parse systemd logs via `journalctl` or the Python `systemd.journal` module  
- Detect common security-relevant patterns:
  - Failed login attempts  
  - Brute-force indicators  
  - Suspicious service restarts  
  - Privilege escalation attempts  
  - Unknown processes or units  
- Custom rule-based detection engine  
- Export results as JSON, CSV, or terminal output  
- Optional GeoIP lookup for remote IP addresses  
- Modular architecture for easy extension  

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/security-log-analyzer.git
cd security-log-analyzer
pip install -r requirements.txt
