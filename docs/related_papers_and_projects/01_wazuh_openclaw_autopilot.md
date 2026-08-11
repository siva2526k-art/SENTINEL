# 🔍 Project Teardown 1: Wazuh Openclaw Autopilot
> **GitHub Overlap Score: 90%**

---

## 📌 Project Overview
* **Repository**: `github.com/OpenClaw/wazuh-openclaw-autopilot`
* **Core Goal**: Autonomous SOC layer built on top of Wazuh SIEM.
* **Target Environment**: Enterprise SOCs & Air-Gapped Networks.

---

## 🏗️ Architecture & Features

```
[ Wazuh Manager Alert ] ──► [ OpenClaw Ingestion Agent ] ──► [ Entity Extractor (IP/User/Hash) ]
                                                                      │
                                                                      ▼
[ Executive PDF Report ] ◄── [ Response Planner ] ◄── [ Local Ollama / vLLM Inference ]
```

### Key Technical Capabilities:
1. **Entity Extraction**: Automatically parses raw alert JSON to extract IPv4/IPv6 addresses, domain names, usernames, and file hashes.
2. **Local Model Support**: Runs with local Ollama or vLLM inference servers in air-gapped environments.
3. **MITRE ATT&CK Auto-Tagging**: Tags extracted entities and log text with official ATT&CK technique IDs.
4. **48+ Tool Connectors**: Integrates via Model Context Protocol (MCP) to query external threat intelligence feeds (VirusTotal, AbuseIPDB).

---

## ⚔️ Comparison with SENTINEL

| Feature | OpenClaw Autopilot | SENTINEL |
| :--- | :--- | :--- |
| **PII Data Sanitizer** | Basic regex entity extraction | 🔒 **Zero-Trust Tokenization & Prompt Injection Firewall** |
| **Model Routing** | Single local or cloud model | ⚡ **3-Tier AI Router** (Local GPU ➡️ Groq Cloud ➡️ Enterprise) |
| **SIEM Compatibility** | Deeply coupled with Wazuh | Ingests Wazuh + Generic SIEM JSON logs |
| **Human-in-the-Loop** | CLI / API approval | 💻 **Interactive React Web Dashboard Modal** |

---

## 💡 Key Takeaways for SENTINEL
* **Lesson 1**: Use MCP or clean REST endpoints to connect threat intelligence lookups (AbuseIPDB) before LLM prompt assembly.
* **Lesson 2**: Ensure local Ollama models are configured with high context windows (`OLLAMA_NUM_CTX=32768`).
