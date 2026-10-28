# Linux CLI System Log & Security Scanner

A lightweight, Python-based Command Line Interface (CLI) utility designed to parse system log files within Linux environments. The script automatically detects potential security anomaly patterns, such as repeated failed login attempts, unauthorized access, SQL injections, and directory traversal attacks.

## Features
- **Regex Pattern Matching:** Detects common security threat signatures (`Failed password`, `directory traversal`, `UNION SELECT`, etc.).
- **Automated Summary Reporting:** Generates line-by-line security alerts along with a clean total anomaly count.
- **Cross-Environment Ready:** Works with custom sample logs or live Linux auth logs (`/var/log/auth.log`).

## Getting Started

### Prerequisites
- Python 3.x
- Linux / Unix-based Environment (Kali Linux, Ubuntu, WSL, etc.)

### Usage

1. Clone this repository:
```bash
git clone https://github.com/nawal-io/Linux-CLI-System-Log-Security-Scanner.git
cd Linux-CLI-System-Log-Security-Scanner
```

2. Run the scanner against the included sample log:
```bash
python3 log_scanner.py
```

3. (Optional) Run against live Linux auth logs:
```bash
sudo python3 log_scanner.py
```

## Author
- **Nawal Aulia Hasan Hunaifa** - [nawal-io](https://github.com/nawal-io)
