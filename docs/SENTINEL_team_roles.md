# 👥 SENTINEL Team Role Allocation & Strategy
> **Customized Task Matrix for 2 Cybersecurity Specialists + 1 Full-Stack & AI Optimization Developer**

---

## 🎯 Team Composition Overview

| Team Member | Role Title | Primary Focus Area | Key Technologies / Tools |
| :--- | :--- | :--- | :--- |
| **Member 1 (You / Lead)** | 🛡️ Cyber Lead — Detection & SIEM | Wazuh SIEM, Log Parsing, MITRE ATT&CK Mapping, Benchmark Suite | Wazuh, Elastic, Suricata, Python, Linux |
| **Member 2** | 🔒 Cyber Specialist — Privacy & Threat Rules | Zero-Trust Sanitizer, Prompt Injection Firewall, ChromaDB RAG Memory | Regex, ChromaDB, Security Prompts, Threat Rules |
| **Member 3** | 💻 Full-Stack & AI Optimization Dev | Dashboard UI, FastAPI, WebSockets, AI Client Optimization (Ollama/Groq), PDF Exporter | React / Vite, FastAPI, Ollama Streaming, Groq API, ReportLab PDF |

---

## 🛠️ Detailed Responsibilities & Roadmap by Role

```
                              ┌──────────────────────────────────────────────┐
                              │           Wazuh SIEM / Live Logs             │
                              └──────────────────────┬───────────────────────┘
                                                     │
                                      (🛡️ Cyber Lead 1: SIEM Ingestion)
                                                     │
                                                     ▼
                              ┌──────────────────────────────────────────────┐
                              │  Zero-Trust Data Sanitizer & Threat Rules    │
                              └──────────────────────┬───────────────────────┘
                                                     │
                                      (🔒 Cyber Spec 2: Privacy Shield)
                                                     │
                                                     ▼
                              ┌──────────────────────────────────────────────┐
                              │ FastAPI API, AI Optimization & Web Dashboard │
                              └──────────────────────────────────────────────┘
                                      (💻 Full-Stack & AI Opt Dev 3)
```

---

### 🛡️ Cybersecurity Teammate 1 — Detection & SIEM Specialist
* **Responsibilities**:
  1. Set up and configure the **Wazuh SIEM** lab (in VirtualBox / Docker).
  2. Build `src/ingestion/wazuh_listener.py` to stream live Wazuh alerts into SENTINEL.
  3. Map incoming alerts directly to **MITRE ATT&CK** Tactics & Techniques (`src/mitre_mapper.py`).
  4. Build empirical evaluation suite (`scripts/benchmark.py`) to measure F1-Score, Precision, and Recall on CIC-IDS datasets.

---

### 🔒 Cybersecurity Teammate 2 — Privacy Shield & Threat Rules Specialist
* **Responsibilities**:
  1. Expand the **Zero-Trust Data Sanitizer** ([src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py)) to scrub PII, usernames, internal IPs, API keys, and MAC addresses.
  2. Implement the **Prompt Injection Firewall Guard** inside `sanitizer.py` to neutralize adversarial prompt override attacks.
  3. Build `src/memory.py` using **ChromaDB Vector Database** for long-term threat memory and historical alert similarity search (`top_k=3`).

---

### 💻 Full-Stack & AI Optimization Developer 3 — Dashboard, API & AI Client Integration
* **Responsibilities**:
  1. Build a modern, dark-mode **SOC Dashboard UI** (React + Vite) with live alert feeds, MITRE ATT&CK heatmaps, and a **Human-in-the-Loop (HITL) Action Approval Modal**.
  2. Create a **FastAPI backend** (`src/api/main.py`) serving REST endpoints and real-time WebSockets.
  3. **AI Model Optimization & Client Integration**:
     - Implement token streaming (Server-Sent Events / WebSockets) from local Ollama GPU (`llama3.1:8b` on RTX 3050).
     - Integrate fast Groq Cloud API (`deepseek-r1:70b`) for Tier 2 fallback.
     - Implement prompt caching, context truncation reduction, and structured JSON output validation.
  4. Build an automated **PDF Incident Report Generator** (`src/reports/pdf_generator.py`) using ReportLab.
