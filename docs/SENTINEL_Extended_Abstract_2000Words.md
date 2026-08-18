# SHIELD AI — AUTONOMOUS CYBER DEFENCE AND SECURITY INTELLIGENCE PLATFORM

**Department**: Department of Computer Science & Engineering, Sri Sai Ram Engineering College, Chennai  
**Academic Year**: 2026–2027  
**Domain**: Cybersecurity, Artificial Intelligence & Autonomous Systems  

---

### EXECUTIVE ABSTRACT

Security Operations Centers struggle every day with massive log volume and analyst burnout. A typical enterprise network churns out over 5,000 security events daily. Investigating just one alert manually takes 30 to 45 minutes, meaning roughly 70% of security notifications get skipped entirely. Worse yet, feeding raw event logs—which contain internal IP maps, staff email addresses, and auth tokens—into cloud AI models creates serious privacy risks and violates data protection laws.

We built **SHIELD AI** to solve these operational and data privacy issues using a zero-trust hybrid architecture. The platform receives raw SIEM telemetry through non-blocking FastAPI webhooks. Our inline Data Sanitizer uses regular expressions to automatically redact IP addresses, email handles, MAC addresses, and API keys, replacing them with synthetic tokens like `[USER_1]` or `[INTERNAL_IP_1]`. De-anonymization lookup tables stay isolated in volatile RAM. Before running any AI model, a built-in firewall scans for and neutralizes prompt-injection commands hidden inside incoming log payloads.

An intelligent three-tier router handles the anonymized logs. Routine alerts run 100% offline on local workstation GPUs using Ollama (`deepseek-r1:8b`) at zero extra cost. High-severity incidents escalate to cloud APIs (Groq or Gemini) using scrubbed tokens only. SHIELD AI maps events to MITRE ATT&CK tactics, correlates alerts into attack graphs (DAGs), and pulls up similar past cases through ChromaDB vector embeddings. To maintain safety, an AST Code Sandbox checks de-obfuscation scripts before execution, and a human-in-the-loop approval gate requires analyst sign-off before running containment actions. Detailed JSONL audit logs record every step while ReportLab generates clean PDF incident reports.

*Keywords*: Privacy-Preserving AI, SOC Triage, Zero-Trust Sanitization, MITRE ATT&CK, Attack Graphs, AST Sandbox, Human-in-the-Loop.
