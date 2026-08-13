"""
SENTINEL — Immutable Audit Logger Module (Phase 13)
Records structured, append-only JSON audit logs for logins, re-identifications, AI escalations, officer approvals, and response verification.
STRICT PRIVACY RULE: NEVER log the real identity_map or raw unmasked PII.
"""
import os
import sys
import json
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SentinelAuditLogger:
    def __init__(self, log_dir=r"C:\Users\siva2\Projects\SENTINEL\data\audit"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, "sentinel_audit_trail.jsonl")

    def _get_utc_timestamp(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def log_event(self, actor: str, action: str, incident_id: str, target: str, result: str, metadata: dict = None) -> dict:
        """
        Record a structured audit log entry to persistent audit_trail.jsonl file.
        """
        entry = {
            "timestamp": self._get_utc_timestamp(),
            "actor": actor or "SYSTEM",
            "action": action,
            "incident": incident_id or "INC-UNKNOWN",
            "target": target or "N/A",
            "result": result,
            "metadata": metadata or {}
        }

        # Privacy Check: Ensure no raw unmasked identity map is present in metadata
        if "identity_map" in entry["metadata"]:
            del entry["metadata"]["identity_map"]
        if "ip_map" in entry["metadata"]:
            del entry["metadata"]["ip_map"]

        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"⚠️ Audit Log Exception: {e}")

        return entry

    def get_audit_trail(self, limit: int = 50) -> list:
        """Read recent audit trail entries."""
        if not os.path.exists(self.log_file):
            return []

        entries = []
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        entries.append(json.loads(line.strip()))
        except Exception as e:
            print(f"⚠️ Audit Log Read Exception: {e}")

        return entries[-limit:]

if __name__ == "__main__":
    logger = SentinelAuditLogger()
    
    # Log sample events
    logger.log_event(
        actor="OFFICER_SHARMA",
        action="APPROVE_CONTAINMENT",
        incident_id="INC-2026-8801",
        target="[INTERNAL_IP_1]",
        result="SUCCESS",
        metadata={"technique": "T1110", "mode": "MOCK"}
    )
    
    logger.log_event(
        actor="ANALYST_KUMAR",
        action="REQUEST_REIDENTIFICATION",
        incident_id="INC-2026-8802",
        target="[USER_1]",
        result="AUTHORIZED",
        metadata={"role": "OFFICER"}
    )

    trail = logger.get_audit_trail()
    print("📜 Recent Immutable Audit Trail:")
    print(json.dumps(trail, indent=2))
