"""
SENTINEL — Incident Correlator Module
Correlates multiple security alerts across multi-factor entities, MITRE techniques, and temporal proximity.
"""
import sys
import json
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class IncidentCorrelator:
    def __init__(self, high_threshold=0.85, medium_threshold=0.60):
        self.high_threshold = high_threshold
        self.medium_threshold = medium_threshold

    def _parse_timestamp(self, ts_str: str) -> float:
        """Helper to parse ISO timestamp string to epoch seconds."""
        if not ts_str:
            return 0.0
        try:
            dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
            return dt.timestamp()
        except Exception:
            return 0.0

    def compute_correlation_score(self, alert_a: dict, alert_b: dict) -> float:
        """
        Calculate correlation score between 0.0 and 1.0 based on entity overlap and temporal proximity.
        """
        score = 0.0
        weight_total = 0.0

        # 1. User Token Match (Weight: 0.25)
        user_a = alert_a.get("user") or alert_a.get("sanitized_user")
        user_b = alert_b.get("user") or alert_b.get("sanitized_user")
        if user_a and user_b:
            weight_total += 0.25
            if user_a == user_b:
                score += 0.25

        # 2. IP Token Match (Source/Destination) (Weight: 0.30)
        ips_a = set(alert_a.get("ip_tokens", []) + [alert_a.get("source_ip"), alert_a.get("target_ip")])
        ips_b = set(alert_b.get("ip_tokens", []) + [alert_b.get("source_ip"), alert_b.get("target_ip")])
        ips_a = {ip for ip in ips_a if ip}
        ips_b = {ip for ip in ips_b if ip}
        
        if ips_a and ips_b:
            weight_total += 0.30
            overlap = ips_a.intersection(ips_b)
            if overlap:
                score += 0.30

        # 3. Hostname / Host Token Match (Weight: 0.20)
        host_a = alert_a.get("host") or alert_a.get("hostname")
        host_b = alert_b.get("host") or alert_b.get("hostname")
        if host_a and host_b:
            weight_total += 0.20
            if host_a == host_b:
                score += 0.20

        # 4. MITRE Technique Match (Weight: 0.15)
        mitre_a = alert_a.get("mitre_technique_id") or alert_a.get("mitre", {}).get("primary_technique_id")
        mitre_b = alert_b.get("mitre_technique_id") or alert_b.get("mitre", {}).get("primary_technique_id")
        if mitre_a and mitre_b:
            weight_total += 0.15
            if mitre_a == mitre_b or mitre_a.split('.')[0] == mitre_b.split('.')[0]:
                score += 0.15

        # 5. Temporal Proximity (Weight: 0.10)
        ts_a = self._parse_timestamp(alert_a.get("timestamp", ""))
        ts_b = self._parse_timestamp(alert_b.get("timestamp", ""))
        if ts_a > 0 and ts_b > 0:
            weight_total += 0.10
            diff_mins = abs(ts_a - ts_b) / 60.0
            if diff_mins <= 15:
                score += 0.10
            elif diff_mins <= 60:
                score += 0.05

        # Normalize score if weight_total < 1.0
        if weight_total > 0:
            final_score = min(1.0, round(score / weight_total, 2))
        else:
            final_score = 0.0

        return final_score

    def correlate_alerts(self, alerts: list) -> list:
        """
        Group a list of sanitized alert dicts into correlated incident clusters.
        """
        if not alerts:
            return []

        clusters = []
        visited = set()

        for i, alert in enumerate(alerts):
            if i in visited:
                continue

            current_cluster = [alert]
            visited.add(i)

            for j in range(i + 1, len(alerts)):
                if j in visited:
                    continue

                other_alert = alerts[j]
                score = self.compute_correlation_score(alert, other_alert)
                if score >= self.medium_threshold:
                    current_cluster.append(other_alert)
                    visited.add(j)

            # Build incident summary object
            cluster_id = f"INC-CORR-{len(clusters) + 1:03d}"
            max_score = 1.0 if len(current_cluster) > 1 else 0.0
            if len(current_cluster) > 1:
                max_score = max(self.compute_correlation_score(current_cluster[0], a) for a in current_cluster[1:])

            clusters.append({
                "incident_id": cluster_id,
                "correlation_score": max_score,
                "confidence": "HIGH" if max_score >= self.high_threshold else ("MEDIUM" if max_score >= self.medium_threshold else "LOW"),
                "alert_count": len(current_cluster),
                "alerts": current_cluster
            })

        return clusters

if __name__ == "__main__":
    correlator = IncidentCorrelator()
    alert1 = {
        "alert_id": "ALT-01",
        "user": "[USER_1]",
        "source_ip": "[INTERNAL_IP_1]",
        "host": "POLICE-HQ-PC04",
        "mitre_technique_id": "T1110",
        "timestamp": "2026-08-13T10:00:00Z"
    }
    alert2 = {
        "alert_id": "ALT-02",
        "user": "[USER_1]",
        "source_ip": "[INTERNAL_IP_1]",
        "host": "POLICE-HQ-PC04",
        "mitre_technique_id": "T1059.001",
        "timestamp": "2026-08-13T10:05:00Z"
    }
    alert3 = {
        "alert_id": "ALT-03",
        "user": "[USER_99]",
        "source_ip": "[EXTERNAL_IP_88]",
        "host": "GUEST-WIFI-01",
        "mitre_technique_id": "T1087",
        "timestamp": "2026-08-13T14:00:00Z"
    }

    score = correlator.compute_correlation_score(alert1, alert2)
    print(f"🔗 Correlation Score (Alert 1 & 2): {score}")

    result = correlator.correlate_alerts([alert1, alert2, alert3])
    print(f"📦 Correlated Incident Clusters: {len(result)}")
    print(json.dumps(result, indent=2))
