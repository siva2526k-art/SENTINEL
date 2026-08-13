# 📜 SENTINEL — Open-Source References & Attribution Record

**Project**: SENTINEL (Security Event Network Triage Investigation with Neural Engine and LLM)  
**Lead Architect**: SIVABALAN T & Team SENTINEL  
**Compliance Standard**: Cleanroom Software Engineering & 17 U.S.C. § 102(b) Idea-Expression Separation

---

## 🏛️ Prior-Art & Architecture Inspiration Records

SENTINEL was developed independently from first principles. To maintain 100% legal transparency, the following open-source cybersecurity projects were studied as high-level architectural references:

### 1️⃣ AiSOC (`github.com/beenuar/AiSOC`)
- **License**: MIT / Open Source
- **Role**: Prior-art reference for multi-agent triage workflows.
- **Concepts Studied**: Vector threat memory retrieval and multi-agent task breakdown.
- **SENTINEL Independent Implementation**: Built original Zero-Trust Sanitizer (`sanitizer.py`), RAM identity mapping, 3-Tier MoE router, and AST code execution sandbox.
- **Code Copying**: ❌ **ZERO CODE COPIED**. All source code written independently.

### 2️⃣ SentinelForge (`github.com/cwccie/sentinelforge`)
- **License**: Apache 2.0 / Open Source
- **Role**: Prior-art reference for active defense playbooks.
- **Concepts Studied**: Incident response containment playbooks and post-action verification.
- **SENTINEL Independent Implementation**: Built safe mock response engine (`src/response/`), server-side HITL approval gateways, and courtroom PDF report generation.
- **Code Copying**: ❌ **ZERO CODE COPIED**. All source code written independently.

### 3️⃣ AI_SOC (`github.com/zhadyz/AI_SOC`)
- **License**: MIT / Open Source
- **Role**: Prior-art reference for Wazuh SIEM telemetry ingestion.
- **Concepts Studied**: HTTP webhook listener for Wazuh manager alerts.
- **SENTINEL Independent Implementation**: Built asynchronous FastAPI Syslog listener (`src/ingestion/wazuh_listener.py`) with automatic zero-trust PII scrubbing.
- **Code Copying**: ❌ **ZERO CODE COPIED**. All source code written independently.

---

## ⚖️ Cleanroom Verification Statement

All code in `src/`, `scripts/`, `docs/`, and `data/` has been authored independently from first principles. SENTINEL maintains complete legal purity and copyright compliance.
