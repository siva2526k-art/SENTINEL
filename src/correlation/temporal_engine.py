"""
SENTINEL — Temporal Engine Module
Builds chronological attack timelines, sorting and grouping security events chronologically.
"""
import sys
import json
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class TemporalEngine:
    def __init__(self):
        pass

    def _parse_time(self, ts_str: str) -> float:
        if not ts_str:
            return 0.0
        try:
            dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
            return dt.timestamp()
        except Exception:
            return 0.0

    def build_timeline(self, alerts: list) -> list:
        """
        Sort alerts by timestamp and format into a human-readable attack timeline.
        """
        if not alerts:
            return []

        # Sort by timestamp ascending (missing timestamps default to 0.0)
        sorted_alerts = sorted(alerts, key=lambda x: self._parse_time(x.get("timestamp", "")))

        timeline = []
        for idx, alert in enumerate(sorted_alerts, 1):
            ts = alert.get("timestamp", "Timestamp Missing")
            summary = alert.get("sanitized_alert") or alert.get("summary") or alert.get("raw_alert", "Security Event")
            technique = alert.get("mitre_technique_id") or alert.get("mitre", {}).get("primary_technique_id", "T1087")
            tactic = alert.get("mitre_tactic") or alert.get("mitre", {}).get("primary_tactic", "TA0007 Discovery")
            user = alert.get("user") or alert.get("sanitized_user", "Unknown")
            host = alert.get("host") or alert.get("hostname", "Unknown Host")

            timeline.append({
                "step": idx,
                "timestamp": ts,
                "tactic": tactic,
                "technique": technique,
                "host": host,
                "user": user,
                "summary": summary
            })

        return timeline

if __name__ == "__main__":
    engine = TemporalEngine()
    test_alerts = [
        {"timestamp": "2026-08-13T10:05:00Z", "mitre_technique_id": "T1059.001", "summary": "PowerShell execution", "user": "[USER_1]", "host": "POLICE-HQ-PC04"},
        {"timestamp": "2026-08-13T10:01:00Z", "mitre_technique_id": "T1110", "summary": "Failed SSH login", "user": "[USER_1]", "host": "POLICE-HQ-PC04"},
        {"timestamp": "2026-08-13T10:12:00Z", "mitre_technique_id": "T1041", "summary": "Outbound SFTP transfer", "user": "[USER_1]", "host": "POLICE-HQ-PC04"}
    ]

    timeline = engine.build_timeline(test_alerts)
    print("⏰ Attack Timeline:")
    print(json.dumps(timeline, indent=2))
