# 👥 SENTINEL Team Role Allocation & Strategy
> **Customized Task Matrix for 2 Cybersecurity Specialists + 1 Full-Stack Developer**

---

## 🎯 Team Composition Overview

| Team Member | Role Title | Primary Focus Area | Key Technologies / Tools |
| :--- | :--- | :--- | :--- |
| **Member 1 (You / Lead)** | 🛡️ Cyber Lead — Detection & SIEM | Wazuh SIEM, Log Parsing, MITRE ATT&CK Mapping | Wazuh, Elastic, Suricata, Python, Linux |
| **Member 2** | 🔒 Cyber Specialist — Privacy & Threat AI | Zero-Trust Sanitizer, Threat Intel & Red-Teaming LLMs | Regex, Ollama (`llama3.1:8b`, `deepseek-r1`), Groq API, Threat Intel |
| **Member 3** | 💻 Full-Stack Developer — Dashboard & APIs | Web UI, Fast API Backend, Real-time WebSockets & PDF Reports | React / Vite / Streamlit, FastAPI, WebSockets, ReportLab / PDFkit |

---

## 🛠️ Detailed Responsibilities & Roadmap by Role

```
                              ┌──────────────────────────────────────────────┐
                              │           Wazuh SIEM / Live Logs             │
                              └──────────────────────┬───────────────────────┘
                                                     │
                                        (Cyber Lead 1: SIEM Ingestion)
                                                     │
                                                     ▼
                              ┌──────────────────────────────────────────────┐
                              │  Zero-Trust Data Sanitizer & AI Engine       │
                              └──────────────────────┬───────────────────────┘
                                                     │
                                        (Cyber Spec 2: Privacy & LLM Triage)
                                                     │
                                                     ▼
                              ┌──────────────────────────────────────────────┐
                              │  FastAPI Backend & Interactive Web UI        │
                              └──────────────────────────────────────────────┘
                                        (Full-Stack Dev 3: App & Dashboard)
```

---

### 🛡️ Cybersecurity Teammate 1 — Detection & SIEM Specialist
* **Responsibilities**:
  1. Set up and configure the **Wazuh SIEM** lab (in VirtualBox / Docker).
  2. Configure Wazuh rules to forward high-priority alerts (Severity 7+) to SENTINEL via webhooks/log streaming.
  3. Map incoming alerts directly to **MITRE ATT&CK** Tactics & Techniques (TTPs).
  4. Perform threat triage validation to ensure false positives are reduced.
* **Deliverables**:
  - `src/ingestion/wazuh_listener.py` (Receives live Wazuh JSON alerts).
  - `src/mitre_mapper.py` (Translates alert IDs to MITRE ATT&CK IDs like `T1110 - Brute Force`).

---

### 🔒 Cybersecurity Teammate 2 — Privacy Shield & AI Prompt Engineering
* **Responsibilities**:
  1. Expand the **Zero-Trust Data Sanitizer** ([src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py)) to cover internal hostnames, JWT tokens, API keys, and custom PII formats.
  2. Craft system prompts for Tier 1 Ollama (`llama3.1:8b`, `deepseek-r1:8b`) to prevent prompt injection and guarantee structured JSON output.
  3. Red-team local LLMs to verify they do not output sensitive tokens or hallucinate false security advice.
* **Deliverables**:
  - `src/sanitizer.py` (Production-grade PII & secret obfuscation engine).
  - `src/prompts/triage_prompts.py` (Structured SOC investigation prompts).
  - `src/router.py` (3-tier decision engine between Ollama, Groq, and Claude/GPT-4o).

---

### 💻 Full-Stack Developer Teammate 3 — Dashboard, API & PDF Reports
* **Responsibilities**:
  1. Build a modern, dark-mode **SOC Dashboard UI** to display live alerts, severity badges, and AI triage summaries.
  2. Create a **FastAPI backend** that connects the Wazuh ingestion pipeline, Sanitizer, AI Router, and Web UI.
  3. Build an automated **PDF Incident Report Generator** so analysts can download executive incident summaries with 1 click.
  4. Implement real-time alert popups via WebSockets or Server-Sent Events (SSE).
* **Deliverables**:
  - `dashboard/` (React + Vite or Streamlit interactive web interface).
  - `src/api/main.py` (FastAPI REST & WebSocket server).
  - `src/reports/pdf_generator.py` (PDF report generator using ReportLab / WeasyPrint).

---

## 🗓️ How the 3 Roles Collaborate Across Semesters

### Semester 3 & 4: Core Engine & Lab Setup
* **Cyber 1**: Deploys Wazuh SIEM lab + feeds raw alerts into local file.
* **Cyber 2**: Builds regex sanitizer + tests local Ollama model on RTX 3050.
* **Full-Stack**: Builds initial CLI dashboard & basic FastAPI endpoints.

### Semester 5: Integrated Hybrid Platform (v0.5)
* **Cyber 1**: Integrates MITRE ATT&CK heatmap data.
* **Cyber 2**: Configures Groq Cloud API for Tier 2 reasoning.
* **Full-Stack**: Integrates interactive web dashboard + MITRE heatmap visualizations.

### Semester 6: Production Polish & Launch (v1.0 MVP)
* **Cyber 1 & 2**: Drafts IEEE/USENIX research paper (methodology & benchmark evaluation).
* **Full-Stack**: Adds PDF report exporter + optimizes UI animations and demo scripts.
* **All Three**: Launches open-source GitHub repository & presents final live demo!
