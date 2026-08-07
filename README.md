# 🛡️ SENTINEL — Security Event Network Triage Investigation with Neural Engine and LLM

> **An Open-Source, Hybrid-AI Autonomous SOC Analyst for Real-Time Security Alert Triage, Incident Response, and Privacy-Aware Threat Investigation.**

---

## 📌 Project Overview
SENTINEL is a 4-year undergraduate flagship cybersecurity project designed to solve **Alert Fatigue** in Security Operations Centers (SOCs). 

It ingests security alerts (from SIEMs like Wazuh, Elastic, or logs), runs local PII/network sanitization, and routes investigations across a **Hybrid AI Architecture**:
* **Tier 1 (Local)**: Fast, 100% offline triage using Ollama (`llama3.1:8b` / `deepseek-r1:8b`) on an RTX 3050.
* **Tier 2 (Cloud Free)**: High-reasoning deep analysis via Groq (`deepseek-r1:70b` / `llama-3.1-70b`).
* **Tier 3 (Cloud Enterprise)**: Optional GPT-4o / Claude 3.5 Sonnet routing for complex multi-stage attacks.

---

## 🏗️ Architecture & Features
* 🔒 **Zero-Trust Data Sanitizer**: Automatically scrubs PII, usernames, internal IPs, and sensitive hostnames locally before sending any payload to cloud models.
* ⚡ **3-Tier AI Router**: Directs routine alerts locally for $0 cost, and complex APT alerts to high-capacity cloud models.
* 📊 **MITRE ATT&CK Mapping**: Auto-maps incoming alerts to MITRE ATT&CK techniques and generates coverage heatmaps.
* 📄 **Automated Incident Reports**: Produces executive-ready PDF incident reports in 30 seconds instead of 45 minutes of manual triage.

---

## 📁 Repository Structure
```
SENTINEL/
├── docs/
│   ├── SENTINEL_master_plan.md      # Full 4-year undergraduate roadmap
│   ├── lab_setup_guide.md           # Lab setup instructions (VirtualBox, Kali, Wazuh)
│   └── SENTINEL_project_brief.html  # Interactive project brief (Exportable to PDF)
├── src/
│   ├── sanitizer.py                # Local PII & network data scrubbing engine
│   ├── router.py                   # 3-Tier AI classification & routing logic
│   └── triage_agent.py             # Main SENTINEL triage loop
├── README.md                       # Project overview
└── SENTINEL_Conversation.md        # Full mentor discussion log
```

---

## 🎯 Quick Start Guide
1. Open this folder in **Antigravity IDE**:
   - Go to `File` -> `Open Folder...`
   - Select `C:\Users\siva2\Projects\SENTINEL`
2. Start your local AI engine:
   - `ollama run llama3.1:8b` (or `deepseek-r1:8b`)
3. Run initial test triage:
   - `python src/triage_agent.py`
