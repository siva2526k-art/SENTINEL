# 🚀 SENTINEL — Team Onboarding & Task Allocation Kit
> **Complete Task Segregation, Repository Ownership, and Ready-to-Use AI Prompts for All 3 Team Members**

---

## 📌 1. Project Overview & Architecture Summary

**SENTINEL** (**S**ecurity **E**vent **N**etwork **T**riage **I**nvestigation with **N**eural **E**ngine and **L**LM) is an open-source, hybrid-AI autonomous Security Operations Center (SOC) analyst. 

It solves **Alert Fatigue** by ingesting SIEM logs (from Wazuh / Elastic), scrubbing PII and prompt injection attacks locally, and routing investigations across a 3-Tier AI Architecture:
- **Tier 1 (Local)**: 100% offline triage using Ollama (`llama3.1:8b` / `mranv/siem-llama-3.1`) on an RTX 3050 ($0 cost).
- **Tier 2 (Cloud Free)**: High-speed reasoning via Groq API (`deepseek-r1:70b`).
- **Tier 3 (Enterprise)**: GPT-4o / Claude 3.5 Sonnet for multi-stage complex APT attacks.

---

## 👥 2. Task Segregation & Repository File Ownership

### 🛡️ Team Member 1: Cybersecurity Lead (SIEM Ingestion & MITRE Specialist)
* **File Ownership**: `src/ingestion/`, `src/mitre_mapper.py`, `scripts/benchmark.py`
* **Assigned Tasks**:
  1. **Task 1.1 — Build Ingestion Listener**: Create `src/ingestion/wazuh_listener.py` using FastAPI to receive live HTTP webhooks from Wazuh SIEM Manager.
  2. **Task 1.2 — Build MITRE ATT&CK Mapper**: Create `src/mitre_mapper.py` to map security alerts to MITRE ATT&CK Tactics (e.g., `TA0001 Initial Access`) and Technique IDs (e.g., `T1110 Brute Force`).
  3. **Task 1.3 — Empirical Benchmarking**: Build `scripts/benchmark.py` to evaluate SENTINEL against 1,000+ benchmark logs (CIC-IDS-2017) and compute F1-Score, Precision, and Recall.

---

### 🔒 Team Member 2: Cybersecurity Specialist (Zero-Trust Privacy & Threat Rules)
* **File Ownership**: [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py), `src/memory.py`
* **Assigned Tasks**:
  1. **Task 2.1 — Expand Zero-Trust Sanitizer**: Enhance [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py) to scrub IPs, usernames, API keys, MAC addresses, and neutralize prompt injection attacks (`"Ignore previous instructions"`).
  2. **Task 2.2 — Build ChromaDB RAG Vector Store**: Create `src/memory.py` using ChromaDB to store past alert embeddings and retrieve similar historical incidents (`top_k=3`).
  3. **Task 2.3 — Security Prompts & Rules**: Craft domain-specific SOC prompt templates and threat evaluation rules.

---

### 💻 Team Member 3: Full-Stack & AI Optimization Developer (Dashboard, API, AI Client & Reports)
* **File Ownership**: `src/api/main.py`, [src/router.py](file:///c:/Users/siva2/Projects/SENTINEL/src/router.py), `src/ai_client.py`, `dashboard/`, `src/reports/pdf_generator.py`
* **Assigned Tasks**:
  1. **Task 3.1 — Build FastAPI Core Server & WebSockets**: Create `src/api/main.py` providing REST routes (`/api/v1/alerts`, `/api/v1/actions/approve`) and real-time WebSockets.
  2. **Task 3.2 — AI Client & Router Optimization**: Refine [src/router.py](file:///c:/Users/siva2/Projects/SENTINEL/src/router.py) and create `src/ai_client.py` for token streaming (Ollama RTX 3050 & Groq Cloud API), prompt caching, latency reduction, and structured JSON output validation.
  3. **Task 3.3 — Build Modern Dark-Mode SOC Dashboard**: Build React + Vite web dashboard showing real-time alert feeds, MITRE heatmaps, and a **Human-in-the-Loop (HITL) Action Approval Modal**.
  4. **Task 3.4 — Automated PDF Report Generator**: Create `src/reports/pdf_generator.py` using ReportLab to export executive PDF incident summaries in 30 seconds.

---

## 💬 3. Ready-to-Copy Master Prompts for Each Team Member

---

### 💻 Updated Prompt for Member 3 (Full-Stack & AI Optimization Developer)

```text
You are working on the SENTINEL project (Security Event Network Triage Investigation with Neural Engine and LLM).
Your goal is to build Module 2 (AI Router & Client Optimization), Module 6 (FastAPI Server & WebSockets), Module 7 (React SOC Dashboard UI), and Module 8 (Automated PDF Generator).

Please generate clean, documented code for:
1. `src/ai_client.py` & `src/router.py`: Optimized Python AI client supporting local Ollama streaming (http://localhost:11434/api/generate with llama3.1:8b on RTX 3050 GPU) and Groq Cloud API fallback for Tier 2. Implement JSON response validation, context window optimization, and prompt caching.
2. `src/api/main.py`: FastAPI backend server providing REST routes (/api/v1/alerts, /api/v1/triage, /api/v1/actions/approve) and WebSocket broadcasting (/ws/alerts).
3. `dashboard/`: A modern dark-mode React + Vite web dashboard displaying live security alerts with color-coded severity badges, an interactive MITRE ATT&CK coverage heatmap, and a Human-in-the-Loop (HITL) Action Approval modal prompting the analyst to approve or reject firewall containment actions.
4. `src/reports/pdf_generator.py`: A ReportLab Python script that generates professional executive-ready PDF incident reports containing threat summaries, severity badges, and recommended remediation steps.

Ensure all code follows modern web design standards, supports real-time token streaming, and handles state cleanly!
```
