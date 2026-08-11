# 🚀 SENTINEL — Team Onboarding & Task Allocation Kit
> **Complete Task Segregation, Repository Ownership, and Ready-to-Use AI Prompts for All 3 Team Members**

---

## 📌 1. Project Overview & Architecture Summary

**SENTINEL** (**S**ecurity **E**vent **N**etwork **T**riage **I**nvestigation with **N**eural **E**ngine and **L**LM) is an open-source, hybrid-AI autonomous Security Operations Center (SOC) analyst. 

It solves **Alert Fatigue** by ingesting SIEM logs (from Wazuh / Elastic), scrubbing PII and prompt injection attacks locally, and routing investigations across a 3-Tier AI Architecture:
- **Tier 1 (Local)**: 100% offline triage using Ollama (`llama3.1:8b` / `mranv/siem-llama-3.1`) on an RTX 3050 ($0 cost).
- **Tier 2 (Cloud Free)**: High-speed reasoning via Groq API (`deepseek-r1:70b`).
- **Tier 3 (Enterprise)**: GPT-4o / Claude 3.5 Sonnet for multi-stage complex APT attacks.

```
                                  ┌──────────────────────────────────────────┐
                                  │      Wazuh SIEM / Log Ingestion          │
                                  └────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                  ┌──────────────────────────────────────────┐
                                  │   Module 1: Zero-Trust Sanitizer         │
                                  │  + Prompt Injection Firewall Guard       │
                                  └────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                  ┌──────────────────────────────────────────┐
                                  │   Module 3: RAG & Threat Memory          │
                                  │     (ChromaDB Vector Store)              │
                                  └────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                  ┌──────────────────────────────────────────┐
                                  │   Module 2: 3-Tier AI Model Router       │
                                  │  (Tier 1: Local RTX3050 | Tier 2/3 Cloud) │
                                  └────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                  ┌──────────────────────────────────────────┐
                                  │   Module 5: MITRE ATT&CK Mapper          │
                                  └────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                  ┌──────────────────────────────────────────┐
                                  │   Module 6: FastAPI Backend & WebSockets │
                                  └────────────────────┬─────────────────────┘
                                                       │
                           ┌───────────────────────────┴───────────────────────────┐
                           ▼                                                       ▼
        ┌──────────────────────────────────────────┐            ┌──────────────────────────────────────────┐
        │  Module 7: Modern SOC Web Dashboard UI   │            │ Module 8: Automated PDF Report Generator │
        │  + HITL Analyst Action Approval Modal    │            └──────────────────────────────────────────┘
        └──────────────────────────────────────────┘
```

---

## 👥 2. Task Segregation & Repository File Ownership

### 🛡️ Team Member 1: Cybersecurity Lead (SIEM Ingestion & MITRE Specialist)
* **File Ownership**: `src/ingestion/`, `src/mitre_mapper.py`, `scripts/benchmark.py`
* **Assigned Tasks**:
  1. **Task 1.1 — Build Ingestion Listener**: Create `src/ingestion/wazuh_listener.py` using FastAPI to receive live HTTP webhooks from Wazuh SIEM Manager.
  2. **Task 1.2 — Build MITRE ATT&CK Mapper**: Create `src/mitre_mapper.py` to map security alerts to MITRE ATT&CK Tactics (e.g., `TA0001 Initial Access`) and Technique IDs (e.g., `T1110 Brute Force`).
  3. **Task 1.3 — Empirical Benchmarking**: Build `scripts/benchmark.py` to evaluate SENTINEL against 1,000+ benchmark logs (CIC-IDS-2017) and compute F1-Score, Precision, and Recall.

---

### 🔒 Team Member 2: Cybersecurity Specialist (Zero-Trust Privacy & AI Triage)
* **File Ownership**: [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py), [src/router.py](file:///c:/Users/siva2/Projects/SENTINEL/src/router.py), `src/memory.py`
* **Assigned Tasks**:
  1. **Task 2.1 — Expand Zero-Trust Sanitizer**: Enhance [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py) to scrub IPs, usernames, API keys, MAC addresses, and neutralize prompt injection attacks (`"Ignore previous instructions"`).
  2. **Task 2.2 — Enhance 3-Tier AI Router**: Refine [src/router.py](file:///c:/Users/siva2/Projects/SENTINEL/src/router.py) connecting local Ollama (`llama3.1:8b` / `mranv/siem-llama-3.1` on RTX 3050) with Groq Cloud API fallback.
  3. **Task 2.3 — Build ChromaDB RAG Vector Store**: Create `src/memory.py` using ChromaDB to store past alert embeddings and retrieve similar historical incidents (`top_k=3`).

---

### 💻 Team Member 3: Full-Stack Developer (Dashboard, API & Reports)
* **File Ownership**: `src/api/main.py`, `dashboard/`, `src/reports/pdf_generator.py`
* **Assigned Tasks**:
  1. **Task 3.1 — Build FastAPI Core Server**: Create `src/api/main.py` providing REST endpoints (`/api/v1/alerts`, `/api/v1/actions/approve`) and real-time WebSockets.
  2. **Task 3.2 — Build Modern Dark-Mode SOC Dashboard**: Build React + Vite web dashboard showing real-time alert feeds, MITRE heatmaps, and a **Human-in-the-Loop (HITL) Action Approval Modal**.
  3. **Task 3.3 — Automated PDF Report Generator**: Create `src/reports/pdf_generator.py` using ReportLab to export executive PDF incident summaries in 30 seconds.

---

## 💬 3. Ready-to-Copy Master Prompts for Each Team Member

Copy and paste these exact prompts into Antigravity IDE or your AI assistant to start building immediately:

---

### 🤖 Prompt for Member 1 (Cyber Lead — Ingestion & MITRE Specialist)

```text
You are working on the SENTINEL project (Security Event Network Triage Investigation with Neural Engine and LLM).
Your goal is to implement Module 4 (Wazuh Ingestion Listener) and Module 5 (MITRE ATT&CK Mapper).

Please generate clean, documented Python code for:
1. `src/ingestion/wazuh_listener.py`: A FastAPI webhook endpoint listening on POST `/webhook/wazuh` that receives raw Wazuh JSON alerts, extracts alert severity, rule ID, description, and agent hostname, and normalizes them into SENTINEL's unified JSON schema.
2. `src/mitre_mapper.py`: A Python module that takes normalized alert strings and maps them to MITRE ATT&CK Tactic IDs (e.g., TA0001 Initial Access) and Technique IDs (e.g., T1110 Brute Force, T1059 Command Scripting) using a dictionary lookup and regex matcher.

Ensure all outputs use clean docstrings, handle exceptions gracefully, and include standalone main test blocks!
```

---

### 🔒 Prompt for Member 2 (Cyber Specialist — Privacy & AI Triage)

```text
You are working on the SENTINEL project (Security Event Network Triage Investigation with Neural Engine and LLM).
Your goal is to build Module 1 (Zero-Trust Sanitizer & Prompt Injection Firewall), Module 2 (3-Tier AI Router), and Module 3 (ChromaDB RAG Memory).

Please generate clean, documented Python code for:
1. Review `src/sanitizer.py` and ensure regex patterns cover IPv4/v6, email addresses, usernames, API keys/JWT tokens, MAC addresses, and neutralize prompt injection attacks (e.g., "ignore previous instructions", "system: override").
2. Review `src/router.py` to route sanitized payloads to local Ollama (http://localhost:11434/api/generate using llama3.1:8b) for Tier 1 triage, with fallback heuristics if offline.
3. `src/memory.py`: A Python module using ChromaDB to embed sanitized alerts and retrieve the top 3 most similar historical incidents to supply context to the LLM prompt.

Ensure all outputs handle UTF-8 text safely on Windows and return structured JSON verdicts!
```

---

### 💻 Prompt for Member 3 (Full-Stack Developer — Dashboard & API)

```text
You are working on the SENTINEL project (Security Event Network Triage Investigation with Neural Engine and LLM).
Your goal is to build Module 6 (FastAPI Server & WebSockets), Module 7 (React SOC Dashboard UI), and Module 8 (Automated PDF Generator).

Please generate clean, documented code for:
1. `src/api/main.py`: FastAPI backend server providing REST routes (/api/v1/alerts, /api/v1/triage, /api/v1/actions/approve) and WebSocket broadcasting (/ws/alerts).
2. `dashboard/`: A modern dark-mode React + Vite web dashboard displaying live security alerts with color-coded severity badges, an interactive MITRE ATT&CK coverage heatmap, and a Human-in-the-Loop (HITL) Action Approval modal prompting the analyst to approve or reject firewall containment actions.
3. `src/reports/pdf_generator.py`: A ReportLab Python script that generates professional executive-ready PDF incident reports containing threat summaries, severity badges, and recommended remediation steps.

Ensure all code follows modern design practices, includes hover states, and handles state cleanly!
```

---

## 📁 Quick Start Commands for Team Members

```bash
# 1. Clone the repository
git clone <YOUR_GITHUB_REPO_URL>
cd SENTINEL

# 2. Check documentation and master blueprint
cat docs/SENTINEL_system_blueprint.md
cat docs/SENTINEL_team_onboarding_kit.md

# 3. Start development on your assigned branch
git checkout -b feature/your-assigned-module
```
