"""
SENTINEL — Active Defense Response Engine Orchestrator
Orchestrates policy validation, Human-in-the-Loop officer approval, action execution, and post-action verification.
"""
import sys
import json
from .firewall_controller import FirewallController
from .process_controller import ProcessController
from .host_isolator import HostIsolator

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class ResponseEngine:
    def __init__(self):
        self.firewall = FirewallController()
        self.process = ProcessController()
        self.isolator = HostIsolator()

    def execute_authorized_containment(self, action_type: str, target: str, officer_approved: bool = False, actor_role: str = "OFFICER") -> dict:
        """
        Execute an authorized containment action with HITL officer approval check.
        """
        if not officer_approved:
            print(f"❌ [RESPONSE DENIED]: Action '{action_type}' requires explicit Human-in-the-Loop Officer approval!")
            return {
                "status": "DENIED",
                "reason": "Officer authorization required.",
                "verified": False
            }

        if actor_role not in ["OFFICER", "ADMIN"]:
            print(f"❌ [RESPONSE DENIED]: Role '{actor_role}' is not authorized to execute active defense actions!")
            return {
                "status": "UNAUTHORIZED_ROLE",
                "reason": "Insufficient role permissions.",
                "verified": False
            }

        print(f"\n⚡ [EXECUTING CONTAINMENT]: Action='{action_type}', Target='{target}', ApprovedBy='{actor_role}'")

        action_upper = action_type.upper()
        if "BLOCK" in action_upper or "IP" in action_upper:
            res = self.firewall.block_ip(target)
        elif "PROCESS" in action_upper or "KILL" in action_upper:
            res = self.process.kill_process(target)
        elif "ISOLATE" in action_upper or "HOST" in action_upper:
            res = self.isolator.isolate_host(target)
        else:
            res = self.firewall.block_ip(target)

        res["officer_approved"] = True
        res["actor_role"] = actor_role
        return res

if __name__ == "__main__":
    engine = ResponseEngine()
    print("🔒 Test 1: Executing containment WITHOUT officer approval...")
    res1 = engine.execute_authorized_containment("BLOCK_IP", "192.168.1.45", officer_approved=False)
    print(json.dumps(res1, indent=2))

    print("\n✅ Test 2: Executing containment WITH officer approval...")
    res2 = engine.execute_authorized_containment("BLOCK_IP", "192.168.1.45", officer_approved=True, actor_role="OFFICER")
    print(json.dumps(res2, indent=2))
