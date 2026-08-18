# SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM

**Department**: Department of Computer Science & Engineering, Sri Sai Ram Engineering College, Chennai  
**Academic Year**: 2026–2027  
**Domain**: Cybersecurity, Artificial Intelligence & Autonomous Systems  

---

### EXECUTIVE ABSTRACT

Security Operations Centers (SOCs) struggle daily with excessive alert volume and analyst burnout. Enterprise networks routinely generate over 5,000 security logs every 24 hours, taking 30 to 45 minutes of manual triage per incident. Because of this delay, nearly 70% of alerts end up unexamined. At the same time, sending raw log data—full of internal IP maps, staff emails, and auth tokens—to public cloud AI models risks major privacy leaks and violates data protection laws.

**SHIELD AI** addresses these operational and privacy hurdles through a zero-trust, hybrid architecture. Built around non-blocking FastAPI webhooks, the system processes raw SIEM logs locally. An inline Data Sanitizer uses regular expressions to strip out IP addresses, email handles, MAC addresses, and API keys, replacing them with dummy tokens like `[USER_1]` or `[INTERNAL_IP_1]`. Sensitive mapping dictionaries stay isolated in volatile RAM. Before any reasoning occurs, an integrated firewall scans for and neutralizes prompt-injection commands inside raw log strings.

A three-tier model router directs the anonymized logs. Routine alerts run 100% offline on local workstation GPUs using Ollama (`deepseek-r1:8b`) at zero marginal cost. Higher-severity incidents escalate to cloud APIs (Groq or Gemini) using scrubbed tokens only. The platform maps alerts to MITRE ATT&CK tactics, correlates events into attack graphs (DAGs), and retrieves similar past incidents via ChromaDB vector embeddings. Safe Python AST parsing checks de-obfuscation scripts before execution, and a human-in-the-loop gate mandates explicit analyst approval for any containment action. Finally, JSONL audit trails log system milestones while ReportLab compiles clean PDF reports.

*Keywords*: Privacy-Preserving AI, SOC Triage, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Sandbox, Human-in-the-Loop.
