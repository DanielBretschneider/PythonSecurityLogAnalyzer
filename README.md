# PythonSecurityLogAnalyzer
A Python‑based security analysis tool that parses, filters, and evaluates systemd journal logs to detect suspicious activity, authentication anomalies, and potential security incidents on Linux systems.

Still in progress!

---

## 📌 Overview

The **Security Log Analyzer for systemd** helps security analysts, system administrators, and researchers identify unusual or malicious behavior by analyzing logs collected through `journald`.  

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

## 📝 journalctl Cheatsheet

### Basic Usage

| Command               | Description                           |
|-----------------------|----------------------------------------|
| `journalctl`          | Show all logs                          |
| `journalctl -r`       | Show logs in reverse order             |
| `journalctl -f`       | Follow new logs (tail -f)              |
| `journalctl -n 50`    | Show last 50 lines                     |
| `journalctl -e`       | Jump to end of logs                    |
| `journalctl -x`       | Show explanatory messages              |

### By Unit / Service

| Command                               | Description                               |
|----------------------------------------|--------------------------------------------|
| `journalctl -u nginx`                  | Logs for a service                         |
| `journalctl -u nginx -u php-fpm`       | Logs for multiple units                    |
| `journalctl -u nginx --since today`    | Logs from today                            |
| `journalctl -u nginx -f`               | Follow service logs                        |
| `journalctl -u nginx -n 100`           | Last 100 lines for a service               |
| `journalctl -u nginx --no-pager`       | Print directly without pager               |
| `journalctl -u nginx --output=short-iso` | Service logs with ISO timestamps         |

### Time Filters

| Command                                                        | Description                     |
|----------------------------------------------------------------|---------------------------------|
| `journalctl --since "2026-02-01"`                              | Logs since date                 |
| `journalctl --since "1 hour ago"`                              | Logs from last hour             |
| `journalctl --since "yesterday"`                               | Logs since yesterday            |
| `journalctl --since "2026-02-01 10:00" --until "2026-02-01 12:00"` | Logs in time window        |
| `journalctl --since today --until now`                         | Logs for the current day        |
| `journalctl --since "30 min ago" -p err`                       | Recent errors only              |

### Boot Logs

| Command                         | Description                         |
|----------------------------------|--------------------------------------|
| `journalctl -b`                 | Current boot logs                    |
| `journalctl -b -1`              | Previous boot logs                   |
| `journalctl --list-boots`       | List boot IDs                        |
| `journalctl -b <ID>`            | Logs for a boot ID                   |
| `journalctl -b -1 -p warning`   | Warnings from previous boot          |
| `journalctl -b --since "10 min ago"` | Current boot logs in recent window |

### By Process / Source

| Command                          | Description                         |
|----------------------------------|--------------------------------------|
| `journalctl _COMM=sshd`          | Logs from process name               |
| `journalctl _EXE=/usr/sbin/sshd` | Logs from executable path            |
| `journalctl _PID=1234`           | Logs from a specific PID             |
| `journalctl SYSLOG_IDENTIFIER=nginx` | Logs by syslog identifier        |
| `journalctl _UID=1000`           | Logs from a specific user ID         |
| `journalctl _SYSTEMD_UNIT=nginx.service` | Filter with explicit unit field |

### Priority and Kernel

| Command                | Description                     |
|------------------------|----------------------------------|
| `journalctl -p err`    | Errors and above                 |
| `journalctl -p warning`| Warnings and above               |
| `journalctl -p 3`      | Priority number (0–7)            |
| `journalctl -k`        | Kernel messages                  |
| `journalctl -k -b`     | Kernel messages for current boot |
| `journalctl -k -p err -b -1` | Previous boot kernel errors |

### Output Formats

| Command                | Description                     |
|------------------------|----------------------------------|
| `journalctl -o short-iso`     | ISO timestamps            |
| `journalctl -o short-precise` | High precision timestamps |
| `journalctl -o json`          | JSON output               |
| `journalctl -o json-pretty`   | Pretty JSON               |
| `journalctl -o cat`           | Message text only         |
| `journalctl -o short-unix`    | UNIX epoch timestamps     |

### User Journal

| Command                   | Description                     |
|---------------------------|----------------------------------|
| `journalctl --user`       | Current user journal             |
| `journalctl --user -u pipewire` | User unit logs            |
| `journalctl --user -b`    | User logs for current boot       |
| `journalctl --user -f`    | Follow user logs                 |

### Filtering and Search

| Command                                           | Description                         |
|---------------------------------------------------|--------------------------------------|
| `journalctl -g "failed"`                          | Filter messages by pattern           |
| `journalctl -u nginx -g "timeout"`                | Pattern search within a unit         |
| `journalctl -u ssh --since "1 day ago" -g "invalid user"` | Time + unit + pattern        |
| `journalctl -u nginx -n 200 | grep -i upstream`   | Pipe to grep for advanced matching   |

### Export and Integration

| Command                                           | Description                         |
|---------------------------------------------------|--------------------------------------|
| `journalctl -u nginx -o json-pretty > nginx.json` | Export unit logs as JSON             |
| `journalctl --since "today" --no-pager > today.log` | Export current day logs            |
| `journalctl -u mysql -n 300 -o cat`               | Message-only output                  |
| `journalctl -u nginx --since "1 hour ago" | less` | Send filtered logs to pager         |

### Disk Usage and Cleanup

| Command                         | Description                     |
|----------------------------------|----------------------------------|
| `journalctl --disk-usage`        | Show journal size                |
| `journalctl --vacuum-size=1G`    | Limit journal to 1 GB            |
| `journalctl --vacuum-time=7d`    | Keep logs for 7 days             |
| `journalctl --vacuum-files=10`   | Keep last 10 journal files       |
| `journalctl --rotate`            | Rotate journal files now         |
| `journalctl --verify`            | Verify journal file integrity    |


## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/security-log-analyzer.git
cd security-log-analyzer
pip install -r requirements.txt

