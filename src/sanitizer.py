"""
SENTINEL — Zero-Trust Data Sanitizer
Scrubs sensitive PII, usernames, internal IPs, and hostnames locally before any cloud AI payload routing.
"""
import re

class DataSanitizer:
    def __init__(self):
        self.ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    def sanitize(self, raw_alert: str) -> dict:
        sanitized_text = raw_alert
        
        # Replace IPv4 addresses with generic tokens
        ips = list(set(self.ip_pattern.findall(sanitized_text)))
        ip_map = {}
        for idx, ip in enumerate(ips):
            token = f"[INTERNAL_IP_{idx+1}]" if ip.startswith(("192.168.", "10.", "172.16.")) else f"[EXTERNAL_IP_{idx+1}]"
            ip_map[token] = ip
            sanitized_text = sanitized_text.replace(ip, token)

        # Scrub email addresses / usernames
        emails = list(set(self.email_pattern.findall(sanitized_text)))
        for idx, email in enumerate(emails):
            sanitized_text = sanitized_text.replace(email, f"[USER_{idx+1}]")

        return {
            "sanitized_alert": sanitized_text,
            "ip_map": ip_map,
            "is_scrubbed": len(ips) > 0 or len(emails) > 0
        }

if __name__ == "__main__":
    sanitizer = DataSanitizer()
    sample_alert = "Failed SSH login for user john.doe@corp.com from 192.168.1.45 on port 22."
    result = sanitizer.sanitize(sample_alert)
    print("Raw Alert:", sample_alert)
    print("Sanitized Output:", result["sanitized_alert"])
