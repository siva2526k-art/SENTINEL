# 🛡️ SENTINEL Master Architecture Blueprint & Implementation Plan

> **Goal**: Define the complete end-to-end technical specification, system architecture, component modules, and gap-closing solutions for SENTINEL before building, ensuring total clarity across all 3 team members (2 Cyber + 1 Full-Stack).

---

## 🏗️ Overall System Architecture Flow

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

## 📦 Detailed Module Specifications

### Module 1: Zero-Trust Data Sanitizer & Prompt Injection Firewall
- **File**: [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py)
- **Role**: Cyber Specialist 2
- **Functionality**:
  - Scrubs sensitive PII (Emails, Usernames, API Keys, Passwords, Internal IPs, Hostnames).
  - **Prompt Injection Firewall**: Scans incoming log strings for adversarial instructions (e.g., `"Ignore previous instructions"`, `"System:"`, `"DROP TABLE"`, delimiter attacks) and strips or neutralizes them before passing to the AI.
  - Maintains reversible token map (`[INTERNAL_IP_1]`, `[USER_1]`) stored strictly in local memory.

### Module 2: 3-Tier AI Router & Classification Engine
- **File**: `src/router.py`
- **Role**: Cyber Specialist 2
- **Functionality**:
  - Classifies incoming alert severity (Low, Medium, High, Critical) and threat type.
  - **Tier 1 (Local)**: Routes 90% of routine alerts to Ollama (`llama3.1:8b` / `deepseek-r1:8b`) on NVIDIA RTX 3050 ($0 cost).
  - **Tier 2 (Cloud Free/Low)**: Escalates ambiguous/medium alerts to Groq API (`deepseek-r1:70b`).
  - **Tier 3 (Cloud Enterprise)**: Escalates multi-stage high-severity APT attacks to GPT-4o / Claude 3.5 Sonnet.

### Module 3: RAG Threat Memory (ChromaDB Vector Store)
- **File**: `src/memory.py`
- **Role**: Cyber Lead 1
- **Functionality**:
  - Stores historical alert embeddings and previous analyst resolutions in a local **ChromaDB** vector database.
  - Performs similarity search (`top_k=3`) to retrieve relevant past incidents and feed context into the LLM prompt.

### Module 4: Wazuh SIEM & Live Log Ingestion Engine
- **File**: `src/ingestion/wazuh_listener.py`
- **Role**: Cyber Lead 1
- **Functionality**:
  - Receives live JSON webhook payloads from Wazuh SIEM (or reads log files).
  - Normalizes raw log formats into SENTINEL's unified JSON schema: `{alert_id, timestamp, source, severity_score, raw_log}`.

### Module 5: MITRE ATT&CK Taxonomy Mapper
- **File**: `src/mitre_mapper.py`
- **Role**: Cyber Lead 1
- **Functionality**:
  - Maps normalized alerts and AI triage verdicts to official MITRE ATT&CK Tactics (e.g., `TA0001 Initial Access`) and Technique IDs (e.g., `T1110 Brute Force`, `T1059 Command Scripting`).
  - Generates ATT&CK matrix coverage data for UI heatmaps.

### Module 6: FastAPI Backend & Human-in-the-Loop (HITL) WebSocket Server
- **File**: `src/api/main.py`
- **Role**: Full-Stack Developer 3
- **Functionality**:
  - Serves REST API endpoints for alert feeds, triage summaries, and PDF report triggers.
  - Provides real-time WebSocket connection to stream alerts instantly to the dashboard.
  - **HITL Action Approval Endpoint**: Enforces human analyst confirmation (`/api/v1/actions/approve`) before executing destructive containment actions (e.g., firewall block).

### Module 7: Modern SOC Dashboard Web UI
- **Directory**: `dashboard/` (React + Vite)
- **Role**: Full-Stack Developer 3
- **Functionality**:
  - Live Alert Feed with severity color indicators.
  - Interactive MITRE ATT&CK Coverage Heatmap.
  - **HITL Modal**: Popup prompting human analyst to "Approve" or "Reject" recommended firewall blocks.
  - 1-Click PDF Incident Report Exporter.

### Module 8: Automated PDF Report Generator
- **File**: `src/reports/pdf_generator.py`
- **Role**: Full-Stack Developer 3
- **Functionality**:
  - Produces executive-ready, high-resolution PDF incident reports in ~30 seconds using ReportLab.

### Module 9: Empirical Benchmark & Evaluation Suite
- **File**: `scripts/benchmark.py`
- **Role**: Cyber Lead 1 & 2
- **Functionality**:
  - Runs SENTINEL against 1,000+ benchmark security logs (CIC-IDS-2017 / Wazuh sample logs).
  - Calculates Precision, Recall, F1-Score, Mean Time to Triage (MTTT), and total API cost savings.

---

## 🛠️ Step-by-Step Execution Plan

### Phase 1: Core Engine & Safety (Week 1–2)
1. Implement Prompt Injection Defense inside [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py).
2. Implement 3-Tier AI Router (`src/router.py`) with Ollama and Groq fallback.
3. Build normalized JSON log schema and test script.

### Phase 2: Ingestion, RAG Memory & MITRE Mapping (Week 3–4)
1. Build `src/ingestion/wazuh_listener.py` for live SIEM webhook listening.
2. Build `src/memory.py` using ChromaDB for threat vector memory.
3. Build `src/mitre_mapper.py` for MITRE ATT&CK technique mapping.

### Phase 3: FastAPI Backend & HITL Web Dashboard (Week 5–6)
1. Build FastAPI REST & WebSocket server (`src/api/main.py`).
2. Build React + Vite dark-mode SOC dashboard with live alert feeds, MITRE heatmap, and HITL action approval modal.
3. Integrate 1-click PDF Report generator.

### Phase 4: Benchmarking & Academic Paper (Week 7–8)
1. Run `scripts/benchmark.py` on 1,000+ test logs.
2. Compile F1-score, Precision, and MTTT graphs.
3. Finalize IEEE paper draft and launch GitHub repository.

---

## 🧪 Verification Plan

### Automated Testing
- `pytest tests/test_sanitizer.py` (Verify PII scrubbing + prompt injection neutralizing).
- `pytest tests/test_router.py` (Verify Tier 1 local vs Tier 2 cloud routing thresholds).
- `python scripts/benchmark.py` (Generate benchmark performance graphs).

### Manual Verification
- Stream simulated SSH brute force alerts through `wazuh_listener.py`.
- Verify real-time alert feed, HITL action approval modal, and PDF report generation in the Web Dashboard.
