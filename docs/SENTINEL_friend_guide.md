# 🛡️ Everything You Need to Know About SENTINEL
> **The Easy-to-Understand Guide to Our Flagship Cybersecurity AI Project**

---

## 💡 1-Minute Elevator Pitch (What is SENTINEL?)

Imagine a security guard sitting in front of hundreds of security camera screens 24/7. Every time a leaf blows past a camera, an alarm blares. Soon, the guard gets exhausted, stops paying attention, and misses an actual break-in. 

In cybersecurity, this is called **"Alert Fatigue"** in a **SOC (Security Operations Center)**. Security systems generate thousands of alerts every day, and human analysts burn out trying to investigate every single one manually.

**SENTINEL** is our **AI Autonomous SOC Analyst**. It acts like an AI co-pilot that automatically inspects every incoming security alarm, scrubs sensitive company secrets so privacy is 100% safe, analyzes the attack using local and cloud AI models, and generates an incident report in **30 seconds** instead of 45 minutes of manual work.

---

## ❓ The Big Problem We Are Solving

1. **Too Many Alarms**: A typical company gets 10,000+ security logs a day. Analysts can't keep up.
2. **Privacy Risks with AI**: You can't just copy-paste confidential company logs into ChatGPT or public AI models because it leaks private customer names, internal IP addresses, and passwords.
3. **High Cloud Costs**: Running every single log through expensive AI APIs (like GPT-4) costs tens of thousands of dollars.

---

## ⚡ How SENTINEL Solves It (The 4-Step Process)

```
[ Security Log / Alarm ] 
          │
          ▼
1. 🔒 Zero-Trust Sanitizer ──► Scrubs passwords, emails, names & IPs locally
          │
          ▼
2. 🤖 Smart 3-Tier AI Router ──► Decides whether local GPU or Cloud AI handles it
          │
          ▼
3. 📊 MITRE ATT&CK Mapping ──► Identifies the exact hacker technique used
          │
          ▼
4. 📄 Auto Incident Report ──► Creates a clean summary for human analysts in 30 sec!
```

---

## 🧠 The 3-Tier AI Brain (Cost $0 to Enterprise Power)

Instead of using one expensive AI, SENTINEL uses a smart routing system:

1. **Tier 1 — Local Offline AI (Free & Private)**
   - **Where it runs**: On our local computer GPU (NVIDIA RTX 3050) using `Ollama` (`llama3.1:8b` or `deepseek-r1:8b`).
   - **Cost**: **$0.00**
   - **Job**: Handles routine alarms (like standard password guess attempts) quickly without sending anything over the internet.
2. **Tier 2 — Free Cloud AI (Deep Reasoning)**
   - **Where it runs**: Fast cloud models via Groq (`deepseek-r1:70b`).
   - **Cost**: Free / Extremely Low.
   - **Job**: Used when an alert looks suspicious and needs deeper logical reasoning.
3. **Tier 3 — Enterprise AI (Heavyweight)**
   - **Where it runs**: GPT-4o or Claude 3.5 Sonnet.
   - **Job**: Reserved only for complex, multi-stage advanced cyberattacks (APT threats).

---

## 🔒 The Privacy Shield (Zero-Trust Data Sanitizer)

Before **ANY** security data leaves the computer, SENTINEL's sanitizer engine ([src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py)) scrubs sensitive information:

* **Real Email**: `john.doe@company.com` ➡️ **Scrubbed**: `[USER_1]`
* **Internal IP**: `192.168.1.45` ➡️ **Scrubbed**: `[INTERNAL_IP_1]`
* **External IP**: `203.0.113.5` ➡️ **Scrubbed**: `[EXTERNAL_IP_1]`

The AI analyzes the threat without ever seeing sensitive real-world identity data!

---

## 🧪 Live Demo Example (What happens in code)

When you run `python src/triage_agent.py`:

### **Input (Raw Security Log)**:
> *"Failed SSH login for user john.doe@corp.com from 192.168.1.45 on port 22."*

### **SENTINEL Output**:
1. 🔒 **Sanitized Payload**: *"Failed SSH login for user [USER_1] from [INTERNAL_IP_1] on port 22."*
2. 🤖 **AI Triage Verdict**: *SSH Brute Force Attack detected.*
3. ⚠️ **Severity**: *HIGH*
4. 🛠️ **Recommended Action**: *Automatically block IP [INTERNAL_IP_1] at the firewall.*

---

## 🎓 The 4-Year Master Roadmap

| Semester | Goal / Milestone | Deliverable |
| :--- | :--- | :--- |
| **Semester 3** | Fundamentals & Setup | Python Log Parser + Local Ollama AI on RTX 3050 |
| **Semester 4** | SIEM Ingestion (ARES v0.1) | Live Wazuh SIEM alerts feeding into local AI |
| **Semester 5** | Hybrid Routing (v0.5) | 3-Tier AI Router + MITRE ATT&CK Heatmaps |
| **Semester 6** | Open-Source MVP (v1.0) | PDF Report Generator + IEEE Research Paper |

---

## 🌟 Why This Project is a Major Flex on Resumes

- **Solves a $13 Billion Problem**: Top cybersecurity firms (Microsoft, CrowdStrike, Palo Alto Networks) are actively looking for engineers who can integrate AI with SIEM systems.
- **Privacy-First Engineering**: Demonstrates zero-trust software design.
- **Hardware Optimized**: Runs on standard consumer laptops/GPUs (RTX 3050) rather than requiring $10,000 server racks.
