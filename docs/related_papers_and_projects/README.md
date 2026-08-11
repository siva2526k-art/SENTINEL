# 📂 SENTINEL Related Projects & Research Library (90% Overlap)

> **Curated Deep-Dive Library of Open-Source Projects and Academic Papers Matching SENTINEL's Core Architecture (>80-90% Overlap)**

---

## 🎯 Purpose of This Library
To prevent reinventing the wheel and to rectify architectural flaws early, this directory contains detailed technical teardowns of existing open-source projects, models, and academic papers that share an 80-90% design overlap with SENTINEL.

Review these documents to extract best practices, pipeline code patterns, and benchmark data!

---

## 📑 Open-Source Projects Index

| File | Project / Paper Name | Overlap | Primary Focus | Key Technology Stack |
| :--- | :--- | :--- | :--- | :--- |
| [01_wazuh_openclaw_autopilot.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/related_papers_and_projects/01_wazuh_openclaw_autopilot.md) | **Wazuh Openclaw Autopilot** | **90%** | Autonomous SOC layer for Wazuh SIEM | Python, MCP Protocol, Local Ollama / vLLM, MITRE ATT&CK |
| [02_ai_soc_local_ollama.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/related_papers_and_projects/02_ai_soc_local_ollama.md) | **AI-SOC (zhadyz/AI_SOC)** | **88%** | Local-first Wazuh alert triage & RAG | Python, Ollama, ChromaDB RAG, MITRE Mapping |
| [03_wazuh_ollama_active_response.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/related_papers_and_projects/03_wazuh_ollama_active_response.md) | **Wazuh-Ollama Active Response** | **82%** | Wazuh Manager hook triggering local LLM triage | Bash / Python, Wazuh Active Response API, Ollama |
| [04_siem_llama_3_1_model.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/related_papers_and_projects/04_siem_llama_3_1_model.md) | **SIEM-Llama-3.1 Fine-Tuned Model** | **85%** | Fine-tuned Llama-3.1 model for SIEM logs | GGUF / Ollama Model (`mranv/siem-llama-3.1`) |
| [05_ieee_arxiv_paper_teardowns.md](file:///c:/Users/siva2/Projects/SENTINEL/docs/related_papers_and_projects/05_ieee_arxiv_paper_teardowns.md) | **Top IEEE & arXiv Paper Teardowns** | **90%** | Academic benchmarks & evaluation metrics | IEEE Access, IEEE EMBC, Expert Systems, arXiv |

---

## 💡 Key Lessons to Apply to SENTINEL

1. **Keep Execution Read-Only**: All top projects enforce that the LLM makes *recommendations*, while human analysts retain approval authority for destructive network containment (validating SENTINEL's **HITL Analyst Dashboard**).
2. **Context Window Tuning**: Setting `OLLAMA_NUM_CTX=32768` is critical to prevent prompt truncation when feeding long log payloads into local Ollama models.
3. **Structured JSON Enforcement**: Prompting LLMs to output strict JSON schemas allows smooth parsing into backend databases and web UI dashboards.
