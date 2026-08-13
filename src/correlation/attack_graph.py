"""
SENTINEL — Attack Graph Reconstruction Module
Generates machine-readable JSON graph representations (nodes & edges) of security incidents.
"""
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class AttackGraphBuilder:
    def __init__(self):
        pass

    def build_attack_graph(self, incident_data: dict) -> dict:
        """
        Build nodes and edges graph representation for a given incident or list of alerts.
        """
        nodes = []
        edges = []
        node_ids = set()

        def add_node(nid: str, label: str, ntype: str):
            if nid and nid not in node_ids:
                node_ids.add(nid)
                nodes.append({"id": nid, "label": label, "type": ntype})

        def add_edge(source: str, target: str, relationship: str):
            if source and target and source in node_ids and target in node_ids:
                edges.append({"source": source, "target": target, "relationship": relationship})

        # Incident Node
        inc_id = incident_data.get("incident_id", "INC-001")
        add_node(inc_id, f"Incident {inc_id}", "incident")

        alerts = incident_data.get("alerts", [incident_data])

        for idx, alert in enumerate(alerts, 1):
            user = alert.get("user") or alert.get("sanitized_user")
            host = alert.get("host") or alert.get("hostname", "POLICE-HQ-PC04")
            process = alert.get("process") or "powershell.exe"
            mitre = alert.get("mitre_technique_id") or alert.get("mitre", {}).get("primary_technique_id", "T1110")
            ip_tokens = alert.get("ip_tokens", [])
            
            # Nodes
            if user:
                add_node(user, user, "user")
                add_edge(inc_id, user, "involved_user")

            if host:
                add_node(host, host, "host")
                if user:
                    add_edge(user, host, "authenticated_to")

            if process:
                proc_id = f"{host}_{process}"
                add_node(proc_id, process, "process")
                if host:
                    add_edge(host, proc_id, "executed")

            if mitre:
                add_node(mitre, f"MITRE {mitre}", "technique")
                if process:
                    proc_id = f"{host}_{process}"
                    add_edge(proc_id, mitre, "exploited")

            for ip in ip_tokens:
                add_node(ip, ip, "IP")
                if host:
                    add_edge(host, ip, "connected_to")

        return {
            "incident_id": inc_id,
            "nodes": nodes,
            "edges": edges
        }

if __name__ == "__main__":
    builder = AttackGraphBuilder()
    sample_incident = {
        "incident_id": "INC-CORR-001",
        "alerts": [
            {
                "user": "[USER_1]",
                "host": "POLICE-HQ-PC04",
                "process": "ssh.exe",
                "mitre_technique_id": "T1110",
                "ip_tokens": ["[INTERNAL_IP_1]"]
            },
            {
                "user": "[USER_1]",
                "host": "POLICE-HQ-PC04",
                "process": "powershell.exe",
                "mitre_technique_id": "T1059.001",
                "ip_tokens": ["[EXTERNAL_IP_2]"]
            }
        ]
    }

    graph = builder.build_attack_graph(sample_incident)
    print("🕸️ Attack Graph (Nodes & Edges):")
    print(json.dumps(graph, indent=2))
