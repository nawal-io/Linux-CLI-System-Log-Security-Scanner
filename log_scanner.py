import os
import re

SUSPICIOUS_PATTERNS = [
    "Failed password",
    "directory traversal",
    "../",
    "UNION SELECT",
    "<script>",
    "unauthorized access",
    "permission denied"
]

def scan_log_file(file_path):
    print(f"[+] Scanning file: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"[-] Error: File '{file_path}' not found.")
        return

    detected_alerts = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line_num, line in enumerate(file, 1):
            for pattern in SUSPICIOUS_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    detected_alerts.append((line_num, pattern, line.strip()))

    print("\n" + "="*50)
    print("      SECURITY SCAN SUMMARY REPORT")
    print("="*50)
    print(f"Total Anomalies Found: {len(detected_alerts)}\n")

    if detected_alerts:
        for line_num, pattern, line in detected_alerts:
            print(f"[ALERT] Line {line_num} | Pattern: '{pattern}'")
            print(f"        Log: {line}\n")
    else:
        print("[OK] No suspicious patterns detected.")

if __name__ == "__main__":
    target_log = "/var/log/auth.log"
    scan_log_file(target_log)
