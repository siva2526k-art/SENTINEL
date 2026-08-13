"""
SENTINEL — 3-Tier System-Level MoE AI Classification & Model Router Engine
Directs security alerts across Tier 1 (Local RTX 3050 GPU via Ollama), Tier 2 (Groq Cloud API), and Tier 3 (Enterprise Cloud LLM).
"""
import sys
import json
from ai_client import SentinelAIClient

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SentinelRouter:
    def __init__(self):
        self.ai_client = SentinelAIClient()

    def evaluate_severity_heuristics(self, alert_text: str) -> str:
        text_lower = alert_text.lower()
        if any(k in text_lower for k in ["unauthorized root", "privilege escalation", "ransomware", "database dump", "zero-day", "kernel panic"]):
            return "CRITICAL"
        elif any(k in text_lower for k in ["failed ssh", "brute force", "port scan", "malware detected", "multiple failed"]):
            return "HIGH"
        elif any(k in text_lower for k in ["permission denied", "unknown connection", "config changed"]):
            return "MEDIUM"
        return "LOW"

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

        # Smart Free-Tier Cascade Decision Gate:
        # 1. Massive Log (> 4,000 chars) -> Google Gemini 2.0 Flash (2M Token Context, 4M Free Tokens/day)
        # 2. Standard Routine Alert -> Tier 1 Local Ollama (deepseek-r1:8b $0 cost)
        # 3. Failover / High Severity -> Groq Cloud (DeepSeek 70B @ 300 tokens/sec) -> Gemini Flash -> OpenRouter 671B
        
        if len(alert_text) > 4000:
            res = self.ai_client.query_tier2_gemini_free(prompt)
            if res["status"] != "success":
                res = self.ai_client.query_tier1_ollama(prompt)
        else:
            res = self.ai_client.query_tier1_ollama(prompt)
            if res["status"] != "success":
                # Cascade 1: Groq Cloud DeepSeek 70B
                res = self.ai_client.query_tier2_groq(prompt)
                if res["status"] != "success":
                    # Cascade 2: Google AI Studio Gemini 2.0 Flash
                    res = self.ai_client.query_tier2_gemini_free(prompt)
                    if res["status"] != "success":
                        # Cascade 3: OpenRouter Free 671B DeepSeek-R1
                        res = self.ai_client.query_tier3_openrouter_free(prompt)

        if res["status"] == "success":
            tier_used = res.get("tier", "AI Engine")
            raw_response = res["content"]
        else:
            # Fallback Tier 1 Local Rule-based Engine when offline
            tier_used = "Tier 1 (Local Heuristic Engine - Offline Standby Mode)"
            summary = f"Detected security incident matching patterns for {severity} severity."
            if "failed ssh" in alert_text.lower() or "brute force" in alert_text.lower():
                action = "Block source IP address at firewall and mandate MFA reset."
            elif "unauthorized" in alert_text.lower() or "exfiltration" in alert_text.lower():
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

        # Parse JSON output from AI response
        try:
            json_start = raw_response.find('{')
            json_end = raw_response.rfind('}') + 1
            if json_start != -1 and json_end != 0:
                parsed = json.loads(raw_response[json_start:json_end])
                summary = parsed.get("triage_summary", raw_response)
                action = parsed.get("recommended_action", "Investigate alert details.")
            else:
                summary = raw_response
                action = "Review log details."
        except Exception:
            summary = raw_response
            action = "Review log details."

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
