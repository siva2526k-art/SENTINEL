"""
SENTINEL — Entity Correlator Module
Tracks relationships between sanitized identifiers (USER, HOST, IP, PROCESS, FILE HASH, DOMAIN, URL, ACCOUNT, SESSION).
"""
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class EntityCorrelator:
    def __init__(self):
        # In-memory graph structure: entity_id -> dict of relationships
        self.entity_map = {}

    def add_relationship(self, entity_a: str, type_a: str, relationship: str, entity_b: str, type_b: str):
        """Add a directed relationship between two sanitized entities."""
        if not entity_a or not entity_b:
            return

        if entity_a not in self.entity_map:
            self.entity_map[entity_a] = {"type": type_a, "relations": []}

        if entity_b not in self.entity_map:
            self.entity_map[entity_b] = {"type": type_b, "relations": []}

        relation_entry = {"relation": relationship, "target": entity_b, "target_type": type_b}
        if relation_entry not in self.entity_map[entity_a]["relations"]:
            self.entity_map[entity_a]["relations"].append(relation_entry)

    def process_sanitized_alert(self, sanitized_alert_data: dict):
        """Extract sanitized entities and record their relationships."""
        user = sanitized_alert_data.get("user") or sanitized_alert_data.get("sanitized_user")
        host = sanitized_alert_data.get("host") or sanitized_alert_data.get("hostname")
        ip_tokens = sanitized_alert_data.get("ip_tokens", [])
        process = sanitized_alert_data.get("process")
        domain = sanitized_alert_data.get("domain")

        if user and host:
            self.add_relationship(user, "USER", "authenticated_to", host, "HOST")

        if host and process:
            self.add_relationship(host, "HOST", "executed", process, "PROCESS")

        if process and domain:
            self.add_relationship(process, "PROCESS", "connected_to", domain, "DOMAIN")

        for ip in ip_tokens:
            if user:
                self.add_relationship(user, "USER", "accessed_from", ip, "IP")
            if host:
                self.add_relationship(host, "HOST", "network_bound", ip, "IP")

    def get_entity_graph(self) -> dict:
        """Return full entity map graph."""
        return self.entity_map

if __name__ == "__main__":
    correlator = EntityCorrelator()
    sample_alert = {
        "user": "[USER_1]",
        "host": "POLICE-HQ-PC04",
        "ip_tokens": ["[INTERNAL_IP_1]", "[EXTERNAL_IP_2]"],
        "process": "powershell.exe",
        "domain": "malicious.example.com"
    }

    correlator.process_sanitized_alert(sample_alert)
    graph = correlator.get_entity_graph()
    print("🕸️ Entity Relationship Map:")
    print(json.dumps(graph, indent=2))
