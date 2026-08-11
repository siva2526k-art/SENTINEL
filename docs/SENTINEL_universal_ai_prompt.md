# 🤖 SENTINEL Universal AI Initialization Prompt & Context Kit
> **A single master prompt that teaches any AI assistant (Antigravity IDE, Cursor, ChatGPT) EVERYTHING about the SENTINEL project before assigning specific feature work.**

---

## 📌 How Your Teammates Use This Prompt
1. Copy the **Master System Prompt** in Section 1 below.
2. At the very bottom under `[YOUR SPECIFIC TASK ASSIGNMENT]`, paste your specific assigned feature (Directive A, B, or C).
3. Paste it directly into your AI Assistant (Antigravity IDE / Cursor) at the start of a coding session!

---

## 🧠 Section 1: Master Universal AI Context Prompt (Copy Below)

```text
================================================================================
                    SENTINEL AI INITIALIZATION CONTEXT
================================================================================
You are pair-programming on project SENTINEL (Security Event Network Triage Investigation with Neural Engine and LLM).

--------------------------------------------------------------------------------
1. PROJECT MISSION & PROBLEM STATEMENT
--------------------------------------------------------------------------------
Security Operations Centers (SOCs) suffer from severe "Alert Fatigue" (10,000+ daily SIEM logs). 
SENTINEL is an open-source, hybrid-AI autonomous SOC analyst co-pilot that ingests SIEM alerts, scrubs sensitive data locally, routes triage across a 3-tier AI model engine, and generates executive incident reports in under 30 seconds at $0 cost for routine alerts.

--------------------------------------------------------------------------------
2. ARCHITECTURE & THE 9 CORE MODULES
--------------------------------------------------------------------------------
[Module 1] Zero-Trust Sanitizer & Prompt Injection Firewall Guard (src/sanitizer.py)
   - Scrubs PII, emails, usernames, API keys, MAC addresses, and tokenizes IPs (e.g. 192.168.x.x -> [INTERNAL_IP_1]).
   - Neutralizes log-based prompt injection attacks ("ignore instructions", "system: override").

[Module 2] 3-Tier AI Router & Client Optimization (src/router.py, src/ai_client.py)
   - Tier 1 (Local): Ollama (llama3.1:8b / mranv/siem-llama-3.1) on NVIDIA RTX 3050 GPU ($0 cost).
   - Tier 2 (Cloud Free/Low): Groq API (deepseek-r1:70b) for deep reasoning on medium/ambiguous alerts.
   - Tier 3 (Cloud Enterprise): GPT-4o / Claude 3.5 Sonnet for multi-stage complex APT attacks.
   - Supports token streaming, prompt caching, and structured JSON output validation.

[Module 3] RAG Threat Memory Store (src/memory.py)
   - ChromaDB vector store embedding historical security alerts and analyst resolutions (top_k=3).

[Module 4] Live SIEM Ingestion Listener (src/ingestion/wazuh_listener.py)
   - FastAPI webhook listener (POST /webhook/wazuh) ingesting live Wazuh JSON alerts.

[Module 5] MITRE ATT&CK Taxonomy Mapper (src/mitre_mapper.py)
   - Maps normalized alert descriptions to MITRE ATT&CK Tactic IDs (TA0001) and Technique IDs (T1110).

[Module 6] FastAPI Backend Server & WebSockets (src/api/main.py)
   - REST API endpoints (/api/v1/alerts, /api/v1/actions/approve) and real-time WebSocket stream (/ws/alerts).

[Module 7] Modern SOC Dashboard Web UI (dashboard/)
   - React + Vite dark-mode dashboard with live alert feeds, MITRE ATT&CK heatmap, and a Human-in-the-Loop (HITL) Action Approval Modal (prevents AI hallucinated containment).

[Module 8] Automated Executive PDF Report Generator (src/reports/pdf_generator.py)
   - ReportLab Python script generating 30-second PDF incident summaries.

[Module 9] Empirical Evaluation Benchmark Suite (scripts/benchmark.py)
   - Evaluates SENTINEL on 1,000+ test logs (CIC-IDS-2017) to calculate F1-Score, Precision, & Recall.

--------------------------------------------------------------------------------
3. TECH STACK & OS ENVIRONMENT
--------------------------------------------------------------------------------
- OS: Windows 10/11
- Language: Python 3.14 (Backend) / TypeScript + React + Vite (Frontend Dashboard)
- Web Framework: FastAPI + Uvicorn
- Local AI Engine: Ollama API (http://localhost:11434/api/generate)
- Vector DB: ChromaDB
- PDF Exporter: ReportLab

================================================================================
                    [YOUR SPECIFIC TASK ASSIGNMENT FOR THIS SESSION]
================================================================================
```

---

## 📋 Section 2: Specific Task Directives to Append

Each team member appends their directive to the bottom of the master prompt above:

---

### 🔒 For Member 2 (Cyber Specialist — Privacy & Threat Rules)
Append this to the bottom of the master prompt:
```text
My assigned focus is Module 1 (Zero-Trust Sanitizer & Safety Firewall) and Module 3 (ChromaDB RAG Memory).

Today, please help me build/refine:
1. `src/sanitizer.py`: Ensure complete PII scrubbing (IPs, emails, API keys, MACs) and prompt injection neutralization.
2. `src/memory.py`: Build the ChromaDB vector database memory module to store past alert embeddings and retrieve top 3 similar historical threats.

Write clean, modular Python 3.14 code with docstrings and a standalone `if __name__ == "__main__":` test block.
```

---

### 💻 For Member 3 (Full-Stack & AI Optimization Developer)
Append this to the bottom of the master prompt:
```text
My assigned focus is Module 2 (AI Client & Router Optimization), Module 6 (FastAPI & WebSockets), Module 7 (React Web Dashboard), and Module 8 (PDF Generator).

Today, please help me build/refine:
1. `src/ai_client.py` & `src/router.py`: Build an optimized AI client supporting local Ollama token streaming (llama3.1:8b) and Groq Cloud API fallback with JSON output validation.
2. `src/api/main.py`: Build the FastAPI REST server (/api/v1/alerts, /api/v1/actions/approve) and WebSocket stream (/ws/alerts).
3. `dashboard/`: Build the React + Vite dark-mode dashboard with live alert feeds and the HITL Action Approval Modal.

Write clean, modular code with modern UI design principles and real-time state handling.
```
