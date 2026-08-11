"""
SENTINEL — 3-Tier AI Classification & Model Router Engine
Directs security alerts across Tier 1 (Local RTX3050 GPU via Ollama), Tier 2 (Groq Cloud API), and Tier 3 (Enterprise Cloud LLM).
"""
import sys
import io
import json
import urllib.request
import urllib.error

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SentinelRouter:
    def __init__(self, ollama_url="http://localhost:11434/api/generate", local_model="llama3.1:8b"):
        self.ollama_url = ollama_url
        self.local_model = local_model

    def evaluate_severity_heuristics(self, alert_text: str) -> str:
        text_lower = alert_text.lower()
        if any(k in text_lower for k in ["unauthorized root", "privilege escalation", "ransomware", "database dump", "kernel panic"]):
            return "CRITICAL"
        elif any(k in text_lower for k in ["failed ssh", "brute force", "port scan", "malware detected", "multiple failed"]):
            return "HIGH"
        elif any(k in text_lower for k in ["permission denied", "unknown connection", "config changed"]):
            return "MEDIUM"
        return "LOW"

    def query_local_ollama(self, prompt: str) -> str:
        """Query local Ollama instance running on RTX 3050 GPU."""
        payload = {
            "model": self.local_model,
            "prompt": prompt,
            "stream": False
        }
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(self.ollama_url, data=data, headers={'Content-Type': 'application/json'})
        
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result.get("response", "").strip()
        except Exception as e:
            return f"OLLAMA_OFFLINE: {e}"

    def route_and_triage(self, sanitized_alert_data: dict) -> dict:
        alert_text = sanitized_alert_data["sanitized_alert"]
        injection_flag = sanitized_alert_data.get("prompt_injection_detected", False)
        
        severity = self.evaluate_severity_heuristics(alert_text)
        if injection_flag:
            severity = "HIGH"

        prompt = f"""You are SENTINEL, an expert autonomous SOC analyst.
Analyze the following sanitized security alert log:

Alert Log: "{alert_text}"
Severity Level: {severity}
Prompt Injection Flag: {injection_flag}

Provide a concise 2-sentence investigation summary and the recommended containment action (e.g. Block IP, Isolate Host, Reset Credentials). Format response as JSON with keys: "triage_summary" and "recommended_action"."""

        # Attempt Tier 1 (Local Ollama)
        ollama_response = self.query_local_ollama(prompt)

        if not ollama_response.startswith("OLLAMA_OFFLINE"):
            tier_used = "Tier 1 (Local RTX 3050 Ollama)"
            try:
                # Try parsing JSON if model returned structured output
                json_start = ollama_response.find('{')
                json_end = ollama_response.rfind('}') + 1
                if json_start != -1 and json_end != 0:
                    parsed = json.loads(ollama_response[json_start:json_end])
                    summary = parsed.get("triage_summary", ollama_response)
                    action = parsed.get("recommended_action", "Investigate alert details.")
                else:
                    summary = ollama_response
                    action = "Review log details."
            except Exception:
                summary = ollama_response
                action = "Review log details."
        else:
            # Fallback Tier 1 Rule-based Engine when Ollama is offline
            tier_used = "Tier 1 (Local Heuristic Engine - Ollama Standby)"
            summary = f"Detected security incident matching patterns for {severity} severity."
            if "failed ssh" in alert_text.lower() or "brute force" in alert_text.lower():
                action = "Block source IP address at firewall and mandate MFA reset."
            elif "unauthorized" in alert_text.lower():
                action = "Isolate target host from internal network."
            else:
                action = "Monitor host network activity and notify system administrator."

        return {
            "severity": severity,
            "triage_summary": summary,
            "recommended_action": action,
            "tier_used": tier_used,
            "prompt_injection_warning": injection_flag
        }

if __name__ == "__main__":
    from sanitizer import DataSanitizer
    sanitizer = DataSanitizer()
    router = SentinelRouter()
    
    test_log = "Failed SSH login for user admin@corp.com from 10.0.0.88 on port 22."
    sanitized = sanitizer.sanitize(test_log)
    result = router.route_and_triage(sanitized)
    
    print("🤖 [SENTINEL Router] Test Result:")
    print("Severity:", result["severity"])
    print("Tier Used:", result["tier_used"])
    print("Summary:", result["triage_summary"])
    print("Action:", result["recommended_action"])
