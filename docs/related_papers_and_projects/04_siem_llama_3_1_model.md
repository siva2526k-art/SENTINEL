# 🔍 Project Teardown 4: SIEM-Llama-3.1 Fine-Tuned Model
> **GitHub / Ollama Overlap Score: 85%**

---

## 📌 Model Overview
* **Model Name**: `mranv/siem-llama-3.1` (Ollama Library)
* **Core Goal**: A specialized fine-tuned Llama-3.1 8B GGUF model trained on security log datasets and Wazuh alert structures.

---

## 🛠️ Key Capabilities & Performance
1. **SIEM Log Understanding**: Specifically trained to interpret raw Syslog, Windows Event Logs (EVTX), and JSON Wazuh alerts.
2. **Standardized Severity Scoring**: Outputs structured severity scores (LOW, MEDIUM, HIGH, CRITICAL) with threat explanations.
3. **Optimized for Ollama**: Can be loaded directly into local GPU memory:
   ```bash
   ollama run mranv/siem-llama-3.1
   ```

---

## ⚔️ Comparison with SENTINEL

* **Model vs System**: `siem-llama-3.1` is a *single model*, whereas **SENTINEL** is an *entire software platform* (Ingestion + Sanitizer + Router + RAG + Dashboard + Reports).
* **Integration Strategy**: SENTINEL can optionally use `mranv/siem-llama-3.1` as a default local Ollama model in Tier 1 for superior SIEM log parsing performance!
