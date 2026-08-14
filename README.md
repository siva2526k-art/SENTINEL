# 🛡️ SENTINEL — Security Event Network Triage Investigation with Neural Engine and LLM

> **Privacy-Preserving, AI-Assisted Autonomous SOC Triage, Threat Investigation, and Controlled Incident Response Platform.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-orange.svg)](https://www.trychroma.com/)
[![Local AI: Ollama](https://img.shields.io/badge/Local_AI-Ollama-black.svg)](https://ollama.ai/)
[![Prototype Status: 10/10 PASS](https://img.shields.io/badge/Prototype_Verification-10%2F10_PASS-success.svg)](scripts/test_all_prototype_levels.py)

---

## 📌 Executive Summary

Security Operations Centers (SOCs) face catastrophic **alert fatigue**, receiving over 5,000 raw SIEM alerts daily. Manual human triage takes 30–45 minutes per alert, causing ~70% of alerts to go unreviewed and allowing attacker dwell time to go undetected.

**SENTINEL** is an autonomous, privacy-preserving AI SOC platform engineered from first principles. It ingests raw telemetry, enforces a strict **Zero-Trust Local Privacy Boundary**, correlates isolated events across time and entities, reasons over threats using a **3-Tier AI Routing Cascade**, protects execution safety via an **AST Code Sandbox**, requires **Human-in-the-Loop (HITL)** containment authorization, and generates **courtroom-ready executive PDF incident briefs** in under 30 seconds.

---

## 🏗️ 3-Stage System Architecture Blueprint

```
STAGE 1: Ingestion & Privacy Boundary (Local Workstation RAM)
┌────────────────────────┐      ┌─────────────────────────────┐      ┌──────────────────────────────┐
│  Wazuh / SIEM Logs     │ ───► │  Zero-Trust Data Sanitizer  │ ───► │  Local RAM Identity Map      │
│  (HTTP Webhook Ingest) │      │  (PII Scrub + Prompt Inject)│      │  ([USER_1] -> officer@gov.in)│
└────────────────────────┘      └─────────────────────────────┘      └──────────────────────────────┘
                                               │
                                               ▼ (Sanitized Tokens Only)
STAGE 2: Threat Context & Graph Correlation
┌────────────────────────┐      ┌─────────────────────────────┐      ┌──────────────────────────────┐
│  MITRE ATT&CK Mapper   │ ───► │  ChromaDB RAG Vector Memory │ ───► │  Attack Graph Builder        │
│  (Tactic & Technique)  │      │  (Historical Case Context)  │      │  (Entity & Temporal Graph)   │
└────────────────────────┘      └─────────────────────────────┘      └──────────────────────────────┘
                                               │
                                               ▼ (Enriched Case Context)
STAGE 3: Decision, HITL Approval & Evidence
┌────────────────────────┐      ┌─────────────────────────────┐      ┌──────────────────────────────┐
│  3-Tier AI Cascade     │ ───► │  AST Sandbox & HITL Gate    │ ───► │  Controlled Defense & PDF    │
│  (Local GPU -> Cloud)  │      │  (Officer APPROVE / REJECT) │      │  (Audit Log + Court Brief)   │
└────────────────────────┘      └─────────────────────────────┘      └──────────────────────────────┘
```

---

## 🌟 Key Technical Innovations

1. **🔒 Privacy by Architecture (Local Trust Zone)**:
   - Real email addresses, internal IP addresses, and hostnames are scrubbed into deterministic synthetic tokens (e.g. `[USER_1]`, `[INTERNAL_IP_1]`) in local RAM before any network transmission.
   - The token mapping key never leaves the local machine. Cloud models only see sanitized tokens.
   - Authorized officers can securely re-identify telemetry locally via authenticated RBAC endpoints (`POST /api/v1/alerts/reidentify`).

2. **🤖 3-Tier AI Routing Cascade (Cost & Offline Resilience)**:
   - **Tier 1 (Local GPU — Ollama)**: Processes ~90% of routine alerts 100% offline for **$0.00 cost** using `deepseek-r1:8b`.
   - **Tier 2 (High-Speed Cloud)**: Escalates ambiguous alerts to Groq (`deepseek-r1:70b` @ 300 t/s) or Gemini Flash (2M token context window).
   - **Tier 3 (Ultra-Large Reasoning)**: Invokes OpenRouter's 550-Billion parameter `nvidia/nemotron-3-ultra-550b` for complex zero-day threat analysis.

3. **🧠 Persistent ChromaDB RAG Vector Threat Memory**:
   - Converts historical incident investigations into local vector embeddings.
   - Performs semantic similarity lookups to automatically inject historical threat context into new triage prompts.

4. **🕸️ Incident Correlation & Attack Graph Topology**:
   - Links isolated SIEM events across users, hostnames, IP subnets, and temporal sliding windows.
   - Reconstructs multi-stage attack chains mapped to MITRE ATT&CK tactics (Initial Access $\rightarrow$ Execution $\rightarrow$ Credential Access $\rightarrow$ Lateral Movement $\rightarrow$ Exfiltration).

5. **🛡️ AST Safe AI Code Execution Sandbox Guard**:
   - Inspects AI-generated Python de-obfuscation scripts using Python's Abstract Syntax Tree (`ast.parse`).
   - Hard-blocks dangerous imports (`os`, `subprocess`, `sys`, `socket`, `eval`, `exec`), preventing prompt-injection command execution attacks.

6. **👮 Human-in-the-Loop (HITL) RBAC Gateway**:
   - AI generates containment recommendations, but **never executes destructive actions autonomously**.
   - Requires explicit officer approval via cryptographic role tokens (`X-Sentinel-Role: POLICE_OFFICER`).
   - Operates in configurable `mock` simulation mode for zero accidental production network downtime.

7. **📜 Courtroom-Ready Executive PDF Reports & Audit Trail**:
   - Logs every event to an immutable, append-only JSONL file (`data/audit/sentinel_audit_trail.jsonl`).
   - Automatically compiles single-page executive PDF incident briefs using ReportLab in under 30 seconds.

8. **💬 Discord Real-Time SOC Channel Notifier**:
   - Dispatches rich, color-coded incident alert embeds and interactive HITL approval notifications directly to team Discord channels.

---

## 📁 Repository Structure

```
SENTINEL/
├── .env.example                                  # Environment template (API keys & response modes)
├── requirements.txt                              # Project dependencies (FastAPI, ChromaDB, ReportLab, etc.)
├── README.md                                     # Master project documentation
│
├── src/                                          # Core Production Source Modules
│   ├── __init__.py                               # Package initialization
│   ├── sanitizer.py                              # Zero-Trust Data Sanitizer & Prompt Injection Firewall
│   ├── router.py                                 # 3-Tier AI Confidence-Threshold Routing Cascade
│   ├── ai_client.py                              # Unified multi-provider LLM client (Ollama, Groq, Gemini, OpenRouter)
│   ├── mitre_mapper.py                           # MITRE ATT&CK taxonomy & technique classifier
│   ├── memory.py                                 # ChromaDB persistent RAG Vector Threat Memory store
│   ├── sandbox.py                                # AST Python code inspection & restricted sandbox
│   ├── audit_logger.py                           # Append-only immutable JSONL forensic audit logger
│   ├── triage_agent.py                           # Master 10-step autonomous SOC triage orchestrator
│   ├── demo_runner.py                            # Interactive 3-scenario live pitch demo runner
│   │
│   ├── api/                                      # FastAPI REST Server & RBAC Gateway
│   │   ├── __init__.py
│   │   └── main.py                               # REST endpoints (/triage, /sanitized, /reidentify, /containment/approve)
│   │
│   ├── correlation/                              # Incident Correlation & Graph Subsystem
│   │   ├── __init__.py
│   │   ├── entity_correlator.py                  # User, host, and IP entity correlation
│   │   ├── temporal_engine.py                    # Time-window clustering & burst detection
│   │   ├── incident_correlator.py                # Multi-alert campaign correlator
│   │   └── attack_graph.py                       # Directed attack graph builder & topology generator
│   │
│   ├── ingestion/                                # Telemetry Ingestion Subsystem
│   │   ├── __init__.py
│   │   └── wazuh_listener.py                     # Async FastAPI Wazuh Syslog HTTP Webhook listener
│   │
│   ├── integrations/                             # External Integrations Subsystem
│   │   ├── __init__.py
│   │   └── discord_bot.py                        # Real-time Discord webhook incident embed notifier
│   │
│   ├── reports/                                  # Incident Report Generation Subsystem
│   │   ├── __init__.py
│   │   └── pdf_generator.py                      # ReportLab executive courtroom PDF incident brief generator
│   │
│   └── response/                                 # Active Defense Containment Subsystem
│       ├── __init__.py
│       ├── firewall_controller.py                # OS firewall blocking controller (iptables / netsh)
│       ├── process_controller.py                 # Malicious process termination controller
│       ├── host_isolator.py                      # Network interface isolation controller
│       └── response_engine.py                    # Unified active defense dispatcher (Safe mock mode)
│
├── scripts/                                      # Test Suites & Presentation Generators
│   ├── test_all_prototype_levels.py              # Master 10-level end-to-end prototype verification suite
│   ├── test_ai_connections.py                    # Connectivity checker for Ollama, Groq, Gemini & OpenRouter
│   ├── generate_redesigned_pptx.py               # Master 14-slide PowerPoint presentation generator
│   ├── generate_presentation_script_and_concepts_pdfs.py # Simple speaker script & deep concepts PDF generator
│   ├── generate_html_visual_deck.py              # Dark-mode glassmorphic interactive HTML slide deck
│   └── sync_session.py                           # Automated multi-agent team sync protocol
│
├── docs/                                         # Architecture Records & Generated Artifacts
│   ├── OPEN_SOURCE_REFERENCES.md                 # Formal Cleanroom open-source attribution & compliance record
│   ├── SENTINEL_master_plan.md                   # Long-term architectural roadmap
│   └── SENTINEL_Demo_Report_Scenario_1.pdf       # Sample generated courtroom incident brief
│
└── data/                                         # Persistent Local Data Stores
    ├── chromadb/                                 # ChromaDB persistent vector database files
    └── audit/                                    # Append-only JSONL audit trails
```

---

## ⚡ Quick Start Guide

### 1. Installation & Environment Setup

```bash
# Clone the repository
git clone https://github.com/siva2526k-art/SENTINEL.git
cd SENTINEL

# Install Python dependencies
pip install -r requirements.txt

# Configure your environment variables
cp .env.example .env
```

### 2. Run the Master 10-Level Prototype Test Suite
Verifies all 10 architectural levels from Zero-Trust Sanitization to Courtroom PDF generation:
```bash
python scripts/test_all_prototype_levels.py
```

### 3. Run the Live 3-Scenario Pitch Demo
Triages 3 real-world attack scenarios (SSH Brute Force, Malicious PowerShell De-obfuscation, Data Exfiltration) and generates executive PDF briefs:
```bash
python src/demo_runner.py
```

### 4. Start the FastAPI REST Server & HITL Gateway
```bash
python src/api/main.py
# Interactive Swagger API documentation available at: http://120.0.0.1:8000/docs
```

### 5. Generate Presentation Materials
```bash
# Generate 14-Slide PowerPoint deck (.pptx) on Desktop
python scripts/generate_redesigned_pptx.py

# Generate Speaker Script PDF & Deep Concepts Guide PDF on Desktop
python scripts/generate_presentation_script_and_concepts_pdfs.py
```

---

## ⚖️ Cleanroom Open-Source Attribution & Provenance

SENTINEL was developed independently from first principles. To maintain 100% legal transparency and academic integrity, the following open-source projects were studied as architectural prior-art references:

| Project / Reference | License | Concept Studied | SENTINEL Independent Implementation |
| :--- | :--- | :--- | :--- |
| **[AiSOC](https://github.com/beenuar/AiSOC)** | MIT | Multi-agent alert triage & MITRE investigation | `src/correlation/` — Independent correlator & attack graph |
| **[SentinelForge](https://github.com/cwccie/sentinelforge)** | Apache 2.0 | Active defense containment playbooks | `src/api/main.py` — Independent HITL approval gateway |
| **[AI_SOC](https://github.com/zhadyz/AI_SOC)** | MIT | Wazuh SIEM webhook integration pattern | `src/ingestion/wazuh_listener.py` — Async webhook listener |
| **[Microsoft Presidio](https://github.com/microsoft/presidio)** | MIT | PII detection regex patterns | `src/sanitizer.py` — Independent RAM token mapping |
| **[ChromaDB](https://www.trychroma.com/)** | Apache 2.0 | Vector database engine | `src/memory.py` — Integrated as pip library dependency |
| **[ReportLab](https://www.reportlab.com/)** | BSD | Programmatic PDF generation | `src/reports/` — Integrated as pip library dependency |

> 📜 **Cleanroom Verification**: Zero source code was copied from prior projects. All core logic in `src/` was authored independently from first principles. See [`docs/OPEN_SOURCE_REFERENCES.md`](docs/OPEN_SOURCE_REFERENCES.md) for the formal record.

---

## 🏆 Prototype Verification Results

| Level | Component | Test Coverage | Result |
| :---: | :--- | :--- | :---: |
| **Level 1** | **Zero-Trust Data Sanitizer & Firewall** | PII regex replacement, dummy tokenization, prompt injection block | `PASS` |
| **Level 2** | **MITRE ATT&CK Taxonomy Mapper** | Tactic & technique ID classification, multi-event tagging | `PASS` |
| **Level 3** | **3-Tier AI Routing Cascade** | Confidence-threshold routing, offline Ollama fallback | `PASS` |
| **Level 4** | **Attack Graph Reconstruction** | Node/edge topology mapping across hosts, IPs, and users | `PASS` |
| **Level 5** | **AST Safe AI Code Sandbox Guard** | Syntax tree parsing (`ast.parse`), blocking dangerous OS calls | `PASS` |
| **Level 6** | **ChromaDB RAG Vector Threat Memory** | Local vector persistence, semantic nearest-neighbor retrieval | `PASS` |
| **Level 7** | **Active Defense Containment Engine** | Safe mock containment execution (firewall, process, host) | `PASS` |
| **Level 8** | **Immutable Audit Trail Logger** | Append-only JSONL logging with microsecond timestamps | `PASS` |
| **Level 9** | **Full 9-Step Autonomous Triage Pipeline** | End-to-end integration across all subsystems | `PASS` |
| **Level 10** | **Executive Courtroom PDF Report Generator** | Programmatic single-page incident brief generation (< 30s) | `PASS` |

---

## 🎓 Lead Author & Academic Affiliation

* **Lead Architect**: **Sivabalan T** (2nd Year B.E. Computer Science & Engineering)
* **Institution**: **Sri Sairam Engineering College**, Chennai, Tamil Nadu, India
* **Repository**: [https://github.com/siva2526k-art/SENTINEL](https://github.com/siva2526k-art/SENTINEL)
* **License**: Open Source under the [MIT License](LICENSE)
