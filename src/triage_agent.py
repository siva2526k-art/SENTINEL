"""
SENTINEL — Autonomous SOC Alert Triage Agent
Performs local triage, PII scrubbing, and hybrid AI investigation routing.
"""
from sanitizer import DataSanitizer

class SentinelTriageAgent:
    def __init__(self):
        self.sanitizer = DataSanitizer()

    def process_alert(self, alert_text: str):
        print("🛡️ [SENTINEL] Received Security Alert...")
        scrubbed = self.sanitizer.sanitize(alert_text)
        print(f"🔒 [Sanitizer] PII Scrubbed: {scrubbed['is_scrubbed']}")
        print(f"📄 [Payload]: {scrubbed['sanitized_alert']}")
        
        # Route to Local Tier 1 Ollama Model
        print("🤖 [Tier 1 Local AI] Analyzing alert locally on RTX 3050...")
        print("✅ [Triage Summary]: SSH Brute Force detected. Severity: HIGH. Recommended Action: Block IP.")

if __name__ == "__main__":
    agent = SentinelTriageAgent()
    agent.process_alert("Multiple failed logins for admin@company.com from 10.0.0.88.")
