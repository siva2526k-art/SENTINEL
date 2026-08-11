# 🔍 Project Teardown 3: Wazuh-Ollama Active Response Hook
> **GitHub Overlap Score: 82%**

---

## 📌 Project Overview
* **Repository**: `github.com/mranv/wazuh-ollama-soc`
* **Core Goal**: Active response script hooked into Wazuh Manager to trigger local LLM triage on high-severity events.

---

## 🏗️ Architecture & Features

```
[ Wazuh Manager Rule Trigger (Level 7+) ] ──► [ Active Response Script (custom-ollama.py) ]
                                                              │
                                                              ▼
[ Wazuh Manager Alert Log Entry ] ◄── [ Ollama Local API Response ]
```

### Key Technical Capabilities:
1. **Wazuh Active Response Hook**: Uses Wazuh's native `ossec.conf` active-response system to trigger Python scripts immediately when a rule level exceeds 7.
2. **Seamless Logging**: Writes the AI's triage assessment directly back into `/var/ossec/logs/active-responses.log`.

---

## ⚔️ Comparison with SENTINEL

| Feature | Wazuh-Ollama Active Response | SENTINEL |
| :--- | :--- | :--- |
| **Ingestion Method** | Local Wazuh script execution | Webhook Listener / File Tailer / SIEM Ingestion |
| **Data Sanitization** | None (Sends raw alert log) | 🔒 **Zero-Trust Data Sanitizer** |
| **User Interface** | Raw Wazuh log entries | 💻 **Modern Dark-Mode Web Dashboard + HITL Modal** |

---

## 💡 Key Takeaways for SENTINEL
* **Lesson 1**: We can provide a pre-built `custom-sentinel.py` script for users who want direct Wazuh Active Response integration!
