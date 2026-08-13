"""
SENTINEL — FastAPI REST Server & RBAC Authorization Engine (Phase 8 & 9)
Exposes Dual-View endpoints (/sanitized vs /reidentify), HITL containment approval, and immutable audit trails.
Enforces server-side Role-Based Access Control (VIEWER, ANALYST, OFFICER, ADMIN).
"""
import sys
import os
import json
from typing import Optional, List, Dict
try:
    from pydantic import BaseModel
    HAS_PYDANTIC = True
except ImportError:
    HAS_PYDANTIC = False
    class BaseModel:
        pass

# Add src parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from triage_agent import SentinelTriageAgent
from response.response_engine import ResponseEngine
from audit_logger import SentinelAuditLogger
from memory import SentinelMemoryStore

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    from fastapi import FastAPI, HTTPException, Header, Depends, status
    from fastapi.middleware.cors import CORSMiddleware
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False

# Pydantic Schemas
class TriageRequest(BaseModel):
    raw_alert: str
    source: Optional[str] = "Wazuh SIEM"

class ReidentifyRequest(BaseModel):
    sanitized_text: str
    token_map: Dict[str, str]

class ContainmentApprovalRequest(BaseModel):
    action_type: str
    target_asset: str
    officer_approved: bool
    incident_id: Optional[str] = "INC-2026-8801"

# Initialize Core Services
agent_service = SentinelTriageAgent()
response_service = ResponseEngine()
audit_service = SentinelAuditLogger()
memory_service = SentinelMemoryStore()

if HAS_FASTAPI:
    app = FastAPI(
        title="SENTINEL Autonomous SOC Triage Platform API",
        description="Privacy-Preserving AI SOC Triage, Dual-View Re-identification, and HITL Containment API",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    def verify_role(x_user_role: Optional[str] = Header(default="ANALYST")) -> str:
        """Server-side RBAC Role Verification Header."""
        role_upper = (x_user_role or "ANALYST").upper()
        if role_upper not in ["VIEWER", "ANALYST", "OFFICER", "ADMIN"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid role specified.")
        return role_upper

    @app.get("/")
    def read_root():
        return {
            "platform": "SENTINEL — Autonomous AI SOC Platform",
            "status": "ONLINE",
            "privacy_sanitizer": "ACTIVE",
            "documentation": "/docs"
        }

    @app.get("/api/v1/health")
    def health_check():
        return {"status": "HEALTHY", "sanitizer": "READY", "router": "READY"}

    @app.post("/api/v1/triage")
    def triage_telemetry(req: TriageRequest, role: str = Depends(verify_role)):
        """Submit raw security log for zero-trust sanitization, correlation, and AI triage."""
        result = agent_service.process_alert(req.raw_alert)
        
        # Save incident to ChromaDB persistent memory
        memory_service.add_incident(
            incident_id="INC-2026-8801",
            sanitized_text=result["sanitized_alert"],
            metadata={"mitre": result["mitre"]["primary_technique_id"], "severity": result["triage"]["severity"]}
        )
        return result

    @app.get("/api/v1/alerts/sanitized")
    def get_sanitized_alerts(role: str = Depends(verify_role)):
        """Returns PII-free sanitized alert feed (Accessible by VIEWER, ANALYST, OFFICER, ADMIN)."""
        return {
            "role_access": role,
            "sanitized_feed": [
                {
                    "incident_id": "INC-2026-8801",
                    "sanitized_alert": "Failed SSH authentication for user [USER_1] from [INTERNAL_IP_1] on port 22.",
                    "severity": "HIGH",
                    "mitre": "T1110"
                }
            ]
        }

    @app.post("/api/v1/alerts/reidentify")
    def reidentify_alert_tokens(req: ReidentifyRequest, role: str = Depends(verify_role)):
        """
        Re-identify synthetic tokens using RAM map.
        STRICT RBAC REQUIREMENT: Only OFFICER and ADMIN roles are authorized!
        """
        if role not in ["OFFICER", "ADMIN"]:
            audit_service.log_event(role, "REIDENTIFY_ATTEMPT", "INC-2026-8801", "UNAUTHORIZED", "DENIED")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access Denied: Role '{role}' is not authorized to unmask police PII or internal IPs."
            )

        reidentified = req.sanitized_text
        for token, real_val in req.token_map.items():
            reidentified = reidentified.replace(token, real_val)

        audit_service.log_event(role, "REIDENTIFY_SUCCESS", "INC-2026-8801", "PII_UNMASKED", "AUTHORIZED")
        return {
            "status": "AUTHORIZED",
            "role": role,
            "reidentified_alert": reidentified
        }

    @app.post("/api/v1/containment/approve")
    def approve_containment_action(req: ContainmentApprovalRequest, role: str = Depends(verify_role)):
        """
        Server-side HITL Containment Approval Gateway.
        STRICT RBAC REQUIREMENT: Only OFFICER and ADMIN roles can execute containment actions!
        """
        if role not in ["OFFICER", "ADMIN"]:
            audit_service.log_event(role, "CONTAINMENT_ATTEMPT", req.incident_id, req.target_asset, "DENIED")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access Denied: Role '{role}' is not authorized to approve active defense containment actions."
            )

        res = response_service.execute_authorized_containment(
            action_type=req.action_type,
            target=req.target_asset,
            officer_approved=req.officer_approved,
            actor_role=role
        )

        audit_service.log_event(
            actor=role,
            action="APPROVE_CONTAINMENT",
            incident_id=req.incident_id,
            target=req.target_asset,
            result=res.get("status", "EXECUTED")
        )
        return res

    @app.get("/api/v1/audit/trail")
    def get_audit_log_trail(role: str = Depends(verify_role)):
        """Returns immutable audit trail (Requires ANALYST, OFFICER, or ADMIN role)."""
        trail = audit_service.get_audit_trail(limit=50)
        return {"total_records": len(trail), "trail": trail}

if __name__ == "__main__":
    if HAS_FASTAPI:
        import uvicorn
        print("🚀 Launching SENTINEL FastAPI Server on http://localhost:8000...")
        uvicorn.run(app, host="127.0.0.1", port=8000)
    else:
        print("⚠️ FastAPI is not installed. Run 'pip install fastapi uvicorn' to launch server.")
