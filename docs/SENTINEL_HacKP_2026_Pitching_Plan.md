# 🛡️ SENTINEL — Hac'KP 2026 Official Pitching Plan
**Event**: Hac'KP 2026 (7th Edition National Hackathon by Kerala Police Cyberdome)  
**Pitch Venue**: Zoho Corporation (In-Person Pitching Round)  
**Pitch Date**: August 14, 2026 | 9:00 AM  
**Project**: **SENTINEL** (*Security Event Network Triage Investigation with Neural Engine and LLM*)

---

## 🎯 Executive Summary & Hackathon Problem Alignment

Kerala Police Cyberdome’s **Hac'KP 2026** revolves around the central theme:  
> **"Agentic AI for Investigations: From Evidence to Intelligence"**

Law enforcement cyber cells and Security Operations Centers (SOCs) are overwhelmed by millions of raw digital logs, forensic artifacts, and SIEM alerts daily. Cyber investigators face three critical bottlenecks:
1. **Data Privacy & Chain-of-Custody Constraints**: Cyber crime evidence contains sensitive Personal Identifiable Information (PII), confidential citizen data, and internal network topographies that **cannot be sent to public commercial cloud LLMs (OpenAI/Claude)** due to privacy laws and leakage risks.
2. **Alert Fatigue & Slow Manual Triage**: Manual log parsing takes 30–45 minutes per alert, causing crucial cyber threats (ransomware, APTs, child exploitation networks) to slip through.
3. **Unstructured Data to Actionable Intelligence**: Turning raw PCAP, Syslog, or memory dump alerts into structured MITRE ATT&CK threat graphs requires deep domain expertise that is scarce.

---

## 💡 SENTINEL Solution Matrix

| Kerala Police Problem | SENTINEL Feature Solution | Technical Advantage |
| :--- | :--- | :--- |
| **Confidential Evidence & Cloud Leakage Risk** | **Zero-Trust Local Data Sanitizer** | Scrubs PII, IP addresses, emails, and hostnames *on-device* before routing; supports 100% air-gapped execution. |
| **Air-Gapped Infrastructure vs. Cloud Power** | **3-Tier Hybrid AI Router** | **Tier 1**: 100% local inference (Ollama `llama3.1:8b` / `deepseek-r1:8b`) on local workstation GPUs.<br>**Tier 2**: Privacy-sanitized Groq Cloud fallback for complex reasoning. |
| **Slow Manual Triage (45 mins/alert)** | **Autonomous Agentic Triage Engine** | Analyzes alerts, extracts IOCs, calculates risk scores, and generates PDF incident briefs in **< 30 seconds**. |
| **Fragmented Forensic Logs** | **Automated MITRE ATT&CK Mapping** | Automatically tags attack tactics/techniques (e.g., T1110 SSH Brute Force, T1059 Command execution) & renders visual heatmaps. |

---

## 📊 10-Slide Pitch Deck Framework (5-Minute Pitch)

```mermaid
flowchart LR
    A[Slide 1: Hook & Problem] --> B[Slide 2: Law Enforcement Bottlenecks]
    B --> C[Slide 3: Introducing SENTINEL]
    C --> D[Slide 4: Zero-Trust Sanitizer]
    D --> E[Slide 5: 3-Tier AI Router]
    E --> F[Slide 6: MITRE Graph & Automation]
    F --> G[Slide 7: Architecture & Tech Stack]
    G --> H[Slide 8: Live Demo Scenario]
    H --> I[Slide 9: Impact & Cyberdome Fit]
    I --> J[Slide 10: Conclusion & Call to Action]
```

---

### 🎙️ Slide-by-Slide Script & Content

#### **Slide 1: Title & Opening Hook**
* **Visual**: Bold title graphic with Kerala Police Cyberdome logo & SENTINEL shield graphic.
* **Header**: SENTINEL: Autonomous Hybrid-AI Analyst for Next-Gen Cyber Investigations.
* **Speaker Script (30s)**:  
  *"Respected judges, officers of Kerala Police Cyberdome, and industry experts from Zoho. Every single day, your cyber investigators are flooded with thousands of security alerts and forensic logs. While cybercriminals operate at machine speed, our investigation triage is still bound by human speed. Today, we introduce **SENTINEL** — an autonomous, privacy-aware, hybrid-AI SOC analyst that transforms raw evidence into actionable intelligence in under 30 seconds."*

#### **Slide 2: The Crisis in Digital Investigations**
* **Visual**: Split screen showing (1) Investigator drowning in raw JSON logs, (2) Risk icon highlighting PII cloud data leak dangers.
* **Key Points**:
  - **Alert Fatigue**: 70%+ alerts ignored due to workload.
  - **The Privacy Dilemma**: Police evidence cannot be uploaded to public AI tools (ChatGPT/Claude) without violating chain-of-custody and IT laws.
  - **Cost & Latency**: Running massive cloud AI models for millions of logs is economically impossible.
* **Speaker Script (30s)**:  
  *"When a cyber incident occurs, speed is everything. But police analysts face a major dilemma: You can't just feed sensitive case evidence into commercial cloud LLMs due to strict privacy and chain-of-custody regulations. Yet manual analysis takes up to 45 minutes per alert. How can law enforcement get the intelligence of advanced AI without sacrificing data privacy?"*

#### **Slide 3: Introducing SENTINEL**
* **Visual**: System diagram showing raw logs entering SENTINEL and outputting an Executive Incident PDF + MITRE Heatmap.
* **Header**: SENTINEL — Privacy-Aware Agentic Intelligence.
* **Speaker Script (30s)**:  
  *"SENTINEL is built specifically to bridge this gap. It is an open-source, hybrid-AI agentic platform designed for air-gapped police networks and enterprise SOCs. It ingests raw logs, scrubs sensitive data locally, performs multi-tier AI analysis, and outputs executive-ready investigative briefs instantly."*

#### **Slide 4: Innovation #1 — Zero-Trust Data Sanitizer**
* **Visual**: Interactive visual showing raw log `admin@keralapolice.gov.in` $\rightarrow$ Sanitizer $\rightarrow$ `[USER_1]`.
* **Technical Spec**: Local regex + NER engine scrubbing IPs, emails, usernames, and hostnames *before* any payload leaves the local machine.
* **Speaker Script (30s)**:  
  *"At the heart of SENTINEL is our Zero-Trust Data Sanitizer. Before any AI processing happens, SENTINEL locally obfuscates all PII, internal IP ranges, and officer credentials. Even if high-tier cloud models are used, zero sensitive state data ever leaves the local network boundary."*

#### **Slide 5: Innovation #2 — 3-Tier Hybrid AI Architecture**
* **Visual**: Tiered pyramid:
  - **Tier 1 (Local - 100% Offline)**: Ollama (`llama3.1:8b` / `deepseek-r1:8b`) running on local RTX GPUs ($0 Cloud Cost).
  - **Tier 2 (Cloud Fast)**: Groq API for ultra-fast deep reasoning on anonymized payloads.
  - **Tier 3 (Cloud Enterprise)**: High-capacity multi-modal models for complex APT multi-stage analysis.
* **Speaker Script (45s)**:  
  *"We solve the cost and privacy problem using a 3-Tier Hybrid Routing Engine. 90% of routine alerts are processed 100% offline on Tier 1 using local LLMs running on standard hardware like an RTX GPU. Only complex, multi-stage attacks are scrubbed and escalated to Tier 2 or 3. This reduces cloud operational costs by up to 85% while guaranteeing offline operational capability for air-gapped police units."*

#### **Slide 6: Innovation #3 — MITRE ATT&CK Mapping & Evidence Chain**
* **Visual**: Sample MITRE ATT&CK heatmap grid with highlighted technique boxes (e.g., T1110 Brute Force, T1059 Command Scripting).
* **Speaker Script (30s)**:  
  *"SENTINEL doesn't just summarize logs—it parses digital forensics into intelligence. It automatically correlates alerts to the MITRE ATT&CK framework, identifies adversary tactics, and maps out the attack progression, turning raw evidence into a courtroom-ready incident report."*

#### **Slide 7: Technical Architecture & Code Readiness**
* **Visual**: Full modular architecture flow:
  `Raw Alert (Wazuh/Syslog)` $\rightarrow$ `Sanitizer Engine` $\rightarrow$ `Tier Router` $\rightarrow$ `Agentic Reasoning Engine` $\rightarrow$ `PDF / Heatmap Output`.
* **Speaker Script (30s)**:  
  *"Our codebase is fully modular, written in Python, and integrated with open-source SIEMs like Wazuh. It runs locally with Ollama, features structured JSON response parsing, and generates full PDF reports automatically."*

#### **Slide 8: Live Demo Plan (The 60-Second Wow Moment)**
* **Visual**: Terminal screen recording / live demo environment.
* **Demo Narrative**:
  1. Trigger a simulated high-severity SSH Brute Force + Data Exfiltration alert containing sensitive email addresses & internal IPs.
  2. Run `python src/triage_agent.py`.
  3. Show local terminal output: **PII Scrubbed in 12ms**, **Tier 1 Local AI Triage Completed in 2.1s**, **MITRE T1110 Mapped**, **PDF Incident Report Generated**.
* **Speaker Script (45s)**:  
  *"Let us show you SENTINEL in action. Here is a live alert containing internal police network IPs and emails. Watch SENTINEL scrub the data locally in milliseconds, analyze the threat using our local LLM, map it to MITRE T1110, and output a complete incident summary."*

#### **Slide 9: Law Enforcement & Cyberdome Integration Potential**
* **Visual**: Deployment roadmap showing integration with Kerala Police Cyberdome lab, State SOCs, and District Cyber Police Stations.
* **Key Benefits**:
  - Deployable on air-gapped forensic workstations.
  - Zero subscription fees for Tier 1 local mode.
  - Standardized automated reporting for cyber crime investigators.
* **Speaker Script (30s)**:  
  *"SENTINEL is built for real-world deployment. It can be plugged directly into Kerala Police Cyberdome’s investigative workflows, assisting officers at district cyber cells to triage cases faster, protect evidence privacy, and maintain a seamless digital chain-of-custody."*

#### **Slide 10: Conclusion & Call to Action**
* **Visual**: High-impact summary slide: **Fast. Private. Autonomous. Open Source.**
* **Speaker Script (15s)**:  
  *"SENTINEL turns evidence into intelligence at machine speed without compromising privacy. Thank you, and we look forward to bringing SENTINEL to Kerala Police Cyberdome. We are open for your questions!"*

---

## 🎯 Judges Q&A Defense Playbook

### **Q1: "Police evidence often operates in air-gapped networks. How does SENTINEL work without internet access?"**
> **Answer**:  
> *"SENTINEL is designed offline-first. Our Tier 1 engine runs 100% locally using lightweight open-source models (like `llama3.1:8b` or `deepseek-r1:8b`) via Ollama directly on local workstation GPUs or edge servers. Zero internet connectivity is required for core triage, data sanitization, and report generation."*

### **Q2: "LLMs can hallucinate. How can police rely on AI for digital forensic evidence?"**
> **Answer**:  
> *"SENTINEL uses strict JSON schema enforcement and system prompting grounded in deterministic evidence (log fields, exact IP mappings, standard MITRE ATT&CK IDs). Furthermore, SENTINEL acts as a **Copilot for the Investigator**—it provides structured recommendations and confidence scores while preserving human-in-the-loop verification."*

### **Q3: "How does SENTINEL protect the digital chain of custody?"**
> **Answer**:  
> *"SENTINEL’s Data Sanitizer creates a deterministic, reversible hash/token map stored only in encrypted local session memory. Raw forensic files remain untouched on the evidence drive, and all AI-generated investigative steps are logged with cryptographic timestamps."*

### **Q4: "How does SENTINEL compare to commercial SOAR tools like Palo Alto Cortex XSOAR or Splunk Phantom?"**
> **Answer**:  
> *"Commercial SOAR tools rely on rigid rule-based playbooks that fail on novel attack vectors, cost hundreds of thousands of dollars, and require cloud connectivity. SENTINEL brings **agentic LLM reasoning**, runs **locally at zero software licensing cost**, and adapts dynamically to complex logs."*

---

## 🛠️ Checklist for August 14 In-Person Pitching at Zoho

1. **Presentation Setup**:
   - Laptop charged + HDMI adapter ready.
   - Backup slide deck in PDF format on USB drive + Google Drive.
2. **Live Demo Environment (Offline Ready)**:
   - Ensure Ollama is running locally with `llama3.1:8b` pre-loaded in VRAM (`ollama run llama3.1:8b`).
   - Have test sample alert JSON files ready in `src/` directory.
   - Test PDF report generation script locally beforehand.
3. **Team Preparation**:
   - Assign roles: Lead Pitcher (Speaker), Tech & Architecture Presenter, Live Demo Operator.
   - Practice the 5-minute pitch timing strictly (aim for 4 mins 30 secs to leave buffer).

---
*Created for SIVABALAN T & Team SENTINEL — Hac'KP 2026 Pitching Round.*
