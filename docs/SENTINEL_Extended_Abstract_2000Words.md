# SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM

**Department**: Department of Computer Science & Engineering, Sri Sai Ram Engineering College, Chennai  
**Academic Year**: 2026–2027  
**Domain**: Cybersecurity, Artificial Intelligence & Autonomous Systems  

---

### EXECUTIVE ABSTRACT

Security Operations Centers (SOCs) face critical operational bottlenecks caused by overwhelming alert volume, high false-positive rates, and severe analyst fatigue. Enterprise networks routinely ingest over 5,000 security logs daily, requiring 30 to 45 minutes of manual investigation per incident. Consequently, nearly 70% of security notifications remain unexamined, expanding attacker dwell time. Furthermore, transmitting raw telemetry containing internal IP topographies, employee emails, and credentials to commercial cloud AI services introduces catastrophic data privacy leakage and violates statutory regulations.

**SHIELD AI** is a privacy-preserving, AI-assisted SOC triage and security intelligence framework engineered to solve these challenges. Operating on a Zero-Trust architecture, SHIELD AI ingests real-time SIEM logs via non-blocking FastAPI webhooks. An inline Data Sanitizer performs local regular-expression (Regex) tokenization—scrubbing IPv4/v6 addresses, emails, MAC addresses, and API keys into synthetic handles (`[USER_1]`, `[INTERNAL_IP_1]`) while holding lookup tables strictly within volatile RAM memory. An integrated Prompt-Injection Firewall neutralizes adversarial prompt overrides in raw logs before processing.

Triage queries are dispatched through a Three-Tier AI Router: Tier 1 executes locally on workstation GPUs using open-weights models (Ollama `deepseek-r1:8b`) for 100% offline triage with zero data egress, while policy-controlled cloud fallbacks (Groq/Gemini) receive only anonymized tokens. Sanitized incidents are mapped to MITRE ATT&CK tactics and techniques, correlated into Directed Acyclic Attack Graphs (DAGs), and matched against historical cases via ChromaDB vector embeddings. To ensure safety, an AST Code Sandbox parses script syntax trees to block dangerous primitives, and a Human-in-the-Loop (HITL) gate requires explicit analyst approval before executing containment actions. Audit milestones are recorded in append-only JSONL trails, and ReportLab compiles executive PDF incident briefs.

*Keywords*: Privacy-Preserving AI, SOC Triage, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Sandbox, Human-in-the-Loop.
