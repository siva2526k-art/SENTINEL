# 🔍 Project Teardown 2: AI-SOC (Local-First Triage & RAG)
> **GitHub Overlap Score: 88%**

---

## 📌 Project Overview
* **Repository**: `github.com/zhadyz/AI_SOC`
* **Core Goal**: Local-first autonomous SOC alert triage system integrating Wazuh SIEM with Ollama and ChromaDB.
* **Target Environment**: Universities, Research Labs, and On-Premise SOCs.

---

## 🏗️ Architecture & Features

```
[ Wazuh alert.json ] ──► [ Python Listener ] ──► [ RAG Memory Search (ChromaDB) ]
                                                            │
                                                            ▼
[ Structured Triage JSON ] ◄── [ Ollama local inference ] ◄─┘
```

### Key Technical Capabilities:
1. **Local-First Processing**: 100% offline triage using Ollama models (`llama-3.1-8b`, `mistral-nemo`).
2. **RAG Vector Search**: Uses **ChromaDB** vector database to store historical incident logs and query similar past attack patterns.
3. **Structured JSON Output**: Forces local LLM to return strict JSON formatting: `{triage_level, incident_summary, mitre_technique}`.

---

## ⚔️ Comparison with SENTINEL

| Feature | AI-SOC (zhadyz) | SENTINEL |
| :--- | :--- | :--- |
| **Privacy / Sanitization** | Relies on local execution only | 🔒 **Active Zero-Trust PII Scrubbing + Prompt Injection Defense** |
| **RAG Vector Memory** | Integrated ChromaDB RAG | Planned for Semester 5 (Will borrow ChromaDB pattern!) |
| **Multi-Tier Routing** | Only local Ollama | ⚡ **3-Tier Router** (Local RTX 3050 ➡️ Groq Cloud ➡️ Enterprise) |
| **Report Generation** | Raw JSON output | 📄 **Automated Executive PDF Reports** |

---

## 💡 Key Takeaways for SENTINEL
* **Lesson 1**: We can adapt their ChromaDB vector store setup for SENTINEL's RAG memory module (`src/memory.py`).
* **Lesson 2**: Enforce strict JSON output parsing in Python using Pydantic / JSON schema validators.
