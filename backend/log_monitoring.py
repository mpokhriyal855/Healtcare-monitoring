# backend/log_monitoring.py
import re
from email_alerts import send_email_alert

def monitor_logs(log_message):
    # Simple pattern for detecting suspicious log entries (e.g., failed login attempts)
    suspicious_patterns = ["failed login", "unauthorized access", "error"]

    for pattern in suspicious_patterns:
        if re.search(pattern, log_message, re.IGNORECASE):
            send_email_alert("Suspicious activity detected in logs", log_message)
            break
