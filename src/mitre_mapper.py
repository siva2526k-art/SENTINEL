"""
SENTINEL — MITRE ATT&CK Taxonomy Mapper Module
Converts security observations and AI triage verdicts into official MITRE ATT&CK Tactics & Technique IDs.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class MitreMapper:
    def __init__(self):
        # Database of signature rules to MITRE ATT&CK mappings
        self.technique_rules = [
            {
                "keywords": ["failed ssh", "brute force", "failed login", "authentication failure", "invalid user"],
                "tactic": "TA0001 - Initial Access / Credential Access",
                "technique_id": "T1110",
                "technique_name": "Brute Force",
                "sub_technique": "T1110.001 - Password Guessing"
            },
            {
                "keywords": ["powershell", "-enc", "encodedcommand", "cmd.exe", "bash -i"],
                "tactic": "TA0002 - Execution",
                "technique_id": "T1059",
                "technique_name": "Command and Scripting Interpreter",
                "sub_technique": "T1059.001 - PowerShell"
            },
            {
                "keywords": ["privilege escalation", "sudo abuse", "uac bypass", "runas", "getsystem"],
                "tactic": "TA0004 - Privilege Escalation",
                "technique_id": "T1548",
                "technique_name": "Abuse Elevation Control Mechanism",
                "sub_technique": "T1548.002 - Bypass User Account Control"
            },
            {
                "keywords": ["exfiltration", "data upload", "large curl", "sftp dump", "scp transfer"],
                "tactic": "TA0010 - Exfiltration",
                "technique_id": "T1041",
                "technique_name": "Exfiltration Over C2 Channel",
                "sub_technique": "T1041 - Exfiltration Over Web / SSH"
            },
            {
                "keywords": ["prompt injection", "neutralized_prompt_injection", "ignore instructions"],
                "tactic": "TA0005 - Defense Evasion",
                "technique_id": "T1562",
                "technique_name": "Impair Defenses",
                "sub_technique": "T1562.001 - Disable or Evade Security Tools"
            }
        ]

    def map_alert(self, alert_text: str) -> dict:
        text_lower = alert_text.lower()
        matched_techniques = []

        for rule in self.technique_rules:
            if any(k in text_lower for k in rule["keywords"]):
                matched_techniques.append({
                    "tactic": rule["tactic"],
                    "technique_id": rule["technique_id"],
                    "technique_name": rule["technique_name"],
                    "sub_technique": rule["sub_technique"]
                })

        if not matched_techniques:
            matched_techniques.append({
                "tactic": "TA0007 - Discovery",
                "technique_id": "T1087",
                "technique_name": "Account Discovery",
                "sub_technique": "T1087.001 - Local Account Discovery"
            })

        primary = matched_techniques[0]
        return {
            "primary_tactic": primary["tactic"],
            "primary_technique_id": primary["technique_id"],
            "primary_technique_name": primary["technique_name"],
            "all_matches": matched_techniques
        }

if __name__ == "__main__":
    mapper = MitreMapper()
    sample = "Failed SSH login for user [USER_1] from [INTERNAL_IP_1] on port 22."
    result = mapper.map_alert(sample)
    print("🗺️ MITRE ATT&CK Mapping Result:")
    print("Primary Tactic:", result["primary_tactic"])
    print("Technique ID:", result["primary_technique_id"])
    print("Technique Name:", result["primary_technique_name"])
