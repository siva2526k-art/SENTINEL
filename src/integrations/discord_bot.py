"""
SENTINEL — Discord Webhook Notifier
====================================
Sends real-time, richly formatted SOC triage alerts to a Discord channel
using Discord Webhooks (no bot token required — works with a Webhook URL alone).

Setup:
  1. In your Discord server: Server Settings → Integrations → Webhooks → New Webhook
  2. Copy the Webhook URL
  3. Paste it into .env as:  DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
  4. Run this file standalone to test: python src/integrations/discord_bot.py

Features:
  • Rich Discord Embeds with colour-coded severity (RED=CRITICAL, ORANGE=HIGH, YELLOW=MEDIUM, GREEN=LOW)
  • MITRE ATT&CK Tactic / Technique display
  • 3-Tier AI Routing tier indicator
  • Dual-View PII isolation summary
  • Human-in-the-Loop (HITL) approval reminder
  • Automatic graceful fallback if webhook not configured
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime
from dotenv import load_dotenv

# ── Load .env so DISCORD_WEBHOOK_URL is available ─────────────────────────────
_env_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(dotenv_path=_env_path)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Severity → Discord embed colour (decimal RGB) ─────────────────────────────
_SEVERITY_COLOURS = {
    "CRITICAL": 15158332,   # Red    #E74C3C
    "HIGH":     15105570,   # Orange #E67E22
    "MEDIUM":   16776960,   # Yellow #FFFF00
    "LOW":      3066993,    # Green  #2ECC71
    "UNKNOWN":  9807270,    # Grey   #95A5A6
}


class SentinelDiscordNotifier:
    """
    Posts SENTINEL triage results as rich Discord Embeds via a webhook.

    Usage:
        notifier = SentinelDiscordNotifier()
        notifier.send_alert(triage_result)   # pass the dict from TriageAgent.process_alert()
    """

    def __init__(self, webhook_url: str | None = None):
        self.webhook_url = webhook_url or os.getenv("DISCORD_WEBHOOK_URL", "")
        if not self.webhook_url or self.webhook_url == "YOUR_DISCORD_WEBHOOK_URL_HERE":
            print("⚠️  [SENTINEL Discord] No webhook URL configured — notifications will be skipped.")
            print("   → Add DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/... to your .env file.")
            self.enabled = False
        else:
            self.enabled = True
            print(f"✅ [SENTINEL Discord] Notifier ready — posting to webhook.")

    # ─────────────────────────────────────────────────────────────────────────
    # Public API
    # ─────────────────────────────────────────────────────────────────────────

    def send_alert(self, triage_result: dict) -> bool:
        """
        Send a full SOC triage result as a Discord embed.

        Args:
            triage_result: The dict returned by SentinelTriageAgent.process_alert()

        Returns:
            True if the message was delivered, False otherwise.
        """
        if not self.enabled:
            return False

        embed = self._build_triage_embed(triage_result)
        payload = {
            "username": "🛡️ SENTINEL SOC Bot",
            "avatar_url": "https://raw.githubusercontent.com/siva2526k-art/SENTINEL/master/docs/sentinel_logo.png",
            "embeds": [embed]
        }
        return self._post(payload)

    def send_startup_ping(self) -> bool:
        """Send a simple heartbeat message so you know SENTINEL is live."""
        if not self.enabled:
            return False
        payload = {
            "username": "🛡️ SENTINEL SOC Bot",
            "content": (
                "✅ **SENTINEL is ONLINE and monitoring.**\n"
                f"🕐 Session started: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}`\n"
                "All 10 architectural levels armed. Awaiting incoming telemetry…"
            )
        }
        return self._post(payload)

    def send_hitl_request(self, triage_result: dict) -> bool:
        """
        Post a Human-in-the-Loop (HITL) approval request to Discord.
        The message pings @here so officers see it immediately.
        """
        if not self.enabled:
            return False

        severity = triage_result.get("triage", {}).get("severity", "UNKNOWN")
        action   = triage_result.get("triage", {}).get("recommended_action", "Unknown Action")
        target   = triage_result.get("triage", {}).get("target_asset", "Unknown Asset")
        colour   = _SEVERITY_COLOURS.get(severity, _SEVERITY_COLOURS["UNKNOWN"])

        embed = {
            "title":       "⚠️  HUMAN-IN-THE-LOOP: ACTION APPROVAL REQUIRED",
            "description": (
                f"**Severity**: `{severity}`\n"
                f"**Recommended Action**: `{action}`\n"
                f"**Target Asset**: `{target}`\n\n"
                "React with ✅ to **APPROVE** or ❌ to **REJECT** this containment action."
            ),
            "color": colour,
            "footer": {"text": "SENTINEL · Zero-Trust SOC Platform"},
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

        payload = {
            "username": "🛡️ SENTINEL SOC Bot",
            "content": "@here 🚨 **OFFICER ACTION REQUIRED** — please approve or reject below:",
            "embeds": [embed]
        }
        return self._post(payload)

    def send_custom_message(self, message: str) -> bool:
        """Post any plain-text message to the Discord channel."""
        if not self.enabled:
            return False
        payload = {"username": "🛡️ SENTINEL SOC Bot", "content": message}
        return self._post(payload)

    # ─────────────────────────────────────────────────────────────────────────
    # Private helpers
    # ─────────────────────────────────────────────────────────────────────────

    def _build_triage_embed(self, result: dict) -> dict:
        triage   = result.get("triage", {})
        mitre    = result.get("mitre", {})
        sanitizer = result.get("sanitizer", {})
        sandbox  = result.get("sandbox_result", {})
        rag      = result.get("rag_matches", [])
        graph    = result.get("attack_graph", {})

        severity  = triage.get("severity", "UNKNOWN").upper()
        colour    = _SEVERITY_COLOURS.get(severity, _SEVERITY_COLOURS["UNKNOWN"])

        fields = [
            {
                "name":   "🔒 Zero-Trust Sanitizer",
                "value":  (
                    f"PII Scrubbed: `{'✅ YES' if sanitizer.get('is_scrubbed') else '❌ NO'}`\n"
                    f"Injection Blocked: `{'⚠️ YES' if sanitizer.get('prompt_injection_detected') else '✅ NONE'}`\n"
                    f"AI View: ```{result.get('sanitized_alert', 'N/A')[:120]}```"
                ),
                "inline": False
            },
            {
                "name":   "🗺️ MITRE ATT&CK",
                "value":  (
                    f"Tactic: `{mitre.get('primary_tactic', 'N/A')}`\n"
                    f"Technique: `{mitre.get('primary_technique_id', 'N/A')} — {mitre.get('primary_technique_name', 'N/A')}`"
                ),
                "inline": True
            },
            {
                "name":   "🤖 AI Router",
                "value":  (
                    f"Tier Used: `{triage.get('tier_used', 'N/A')}`\n"
                    f"Recommended: `{triage.get('recommended_action', 'N/A')}`"
                ),
                "inline": True
            },
            {
                "name":   "🔒 AST Sandbox",
                "value":  (
                    f"Code Safe: `{'✅ PASSED' if sandbox.get('is_safe') else '❌ BLOCKED'}`\n"
                    f"Status: `{sandbox.get('status', 'N/A')}`"
                ),
                "inline": True
            },
            {
                "name":   "🕸️ Attack Graph",
                "value":  (
                    f"Nodes: `{len(graph.get('nodes', []))}`  Edges: `{len(graph.get('edges', []))}`"
                ),
                "inline": True
            },
            {
                "name":   "🧠 RAG Memory",
                "value":  f"Historical Matches: `{len(rag)}`",
                "inline": True
            },
        ]

        return {
            "title":       f"🛡️ SENTINEL TRIAGE ALERT — Severity: {severity}",
            "description": (
                f"**Triage Summary**\n> {triage.get('triage_summary', 'No summary available.')}"
            ),
            "color":  colour,
            "fields": fields,
            "footer": {
                "text": "SENTINEL · Zero-Trust AI SOC Platform · Sri Sairam Engineering College"
            },
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

    def _post(self, payload: dict) -> bool:
        """Send a JSON payload to the Discord webhook endpoint."""
        try:
            data    = json.dumps(payload).encode("utf-8")
            request = urllib.request.Request(
                self.webhook_url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.status in (200, 204):
                    print("📨 [SENTINEL Discord] ✅ Alert posted to Discord successfully!")
                    return True
                else:
                    print(f"⚠️  [SENTINEL Discord] Unexpected status: {response.status}")
                    return False
        except urllib.error.HTTPError as e:
            print(f"❌ [SENTINEL Discord] HTTP error {e.code}: {e.reason}")
            try:
                body = e.read().decode("utf-8")
                print(f"   Discord error body: {body}")
            except Exception:
                pass
            return False
        except Exception as e:
            print(f"❌ [SENTINEL Discord] Failed to post alert: {e}")
            return False


# ─────────────────────────────────────────────────────────────────────────────
# Standalone test — run this file directly to verify your webhook works
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 65)
    print("🛡️  SENTINEL Discord Notifier — Standalone Webhook Test")
    print("=" * 65)

    notifier = SentinelDiscordNotifier()

    # 1. Send a startup heartbeat
    print("\n[1] Sending startup ping…")
    notifier.send_startup_ping()

    # 2. Send a fake triage result to test the rich embed
    fake_result = {
        "sanitized_alert": "Failed SSH login for [USER_1] from [INTERNAL_IP_1] on port 22.",
        "sanitizer": {"is_scrubbed": True, "prompt_injection_detected": False},
        "mitre": {
            "primary_tactic":        "Credential Access",
            "primary_technique_id":  "T1110",
            "primary_technique_name": "Brute Force",
        },
        "triage": {
            "tier_used":          "Tier 1 — Local GPU (deepseek-r1:8b)",
            "severity":           "HIGH",
            "triage_summary":     "Repeated SSH brute-force from suspicious internal IP.",
            "recommended_action": "Block [INTERNAL_IP_1] at perimeter firewall immediately.",
        },
        "sandbox_result": {"is_safe": True, "status": "EXECUTED_SAFELY"},
        "attack_graph": {"nodes": ["USER_1", "INTERNAL_IP_1", "SSH"], "edges": [("INTERNAL_IP_1", "SSH"), ("SSH", "USER_1")]},
        "rag_matches": [{"sanitized_summary": "Similar SSH brute-force from different IP — 3 days ago."}],
    }

    print("\n[2] Sending sample SOC triage alert embed…")
    notifier.send_alert(fake_result)

    # 3. Send a HITL approval request
    print("\n[3] Sending HITL action approval request…")
    notifier.send_hitl_request(fake_result)

    print("\n✅ Done. Check your Discord channel for the messages!")
