# STUDENT ACTIVITY FILE — INNOVATIVE DESIGN LAB (IDL) - I
**Academic Year**: 2026-2027  
**Department**: Computer Science and Engineering  
**Institution**: Sri Sai Ram Engineering College, Chennai  
**Title of the Project**: **SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine**  

---

## SECTION 0: COVER PAGE & METADATA

| Field | Details |
| :--- | :--- |
| **Academic Year** | 2026-2027 |
| **Department & Section** | Computer Science and Engineering &nbsp;\|&nbsp; Section: A & C |
| **Innovation Ecosystem Project ID** | SAIRAM-IDL1-2026-CSE-09 |
| **Title of the Project** | **SENTINEL: Autonomous Hybrid-AI SOC Analyst & Investigative Engine** |
| **Inter disciplinary Project** | [X] Yes &nbsp;&nbsp; [ ] No Team |
| **Members (Max. 3)** | 1. **Gokula Kannan M** — SEC25CS196 — CSE-A<br/>2. **Lakshan M** — SEC25CS036 — CSE-A<br/>3. **Sivabalan T** — SEC25CS101 — CSE-C |
| **Project Version** | [X] Version 1 – New Project &nbsp;&nbsp; [ ] Version 2 – Pass out Student Project |
| **Domain Name** | Cybersecurity, Artificial Intelligence & Autonomous Systems |
| **IEEE Society & Community** | IEEE Computer Society &nbsp;\|&nbsp; IEEE Student Branch Sairam |
| **Club and Cells** | Sairam Innovation Ecosystem / Cyber Security Club |
| **Name of Department IDL - I Coordinator** | Dr. A. SHEELA &nbsp;\|&nbsp; Faculty ID: IDL-FAC-01 |
| **Name of the Supervisor** | Dr. A. SHEELA &nbsp;\|&nbsp; Faculty ID: IDL-FAC-02 |
| **Name of External Guide** | Senior Tech Leads & Cyber Forensic Specialists |
| **Designation & Organization** | Cyberdome Investigations / Zoho Corporation |

---

## SECTION 1: SUSTAINABLE DEVELOPMENT GOALS (SDG) MAPPING

| SDG | Goal Number With Name | SAP Code with Explanation |
| :--- | :--- | :--- |
| **Primary SDG** | **SDG 9: Industry, Innovation, and Infrastructure** | 1. **SAP-SDG9-CYBER-01**: Resilient cyber infrastructure & AI SOC automation.<br/>2. **SAP-SDG9-CYBER-02**: Zero-trust cloud-edge security architecture.<br/>3. **SAP-SDG9-CYBER-03**: Scalable threat intelligence platform. |
| **Secondary SDG** | **SDG 16: Peace, Justice, and Strong Institutions** | 1. **SAP-SDG16-SEC-01**: Evidence privacy & chain-of-custody enforcement.<br/>2. **SAP-SDG16-SEC-02**: Citizen PII protection in digital investigation.<br/>3. **SAP-SDG16-SEC-03**: Transparent forensic audit logging. |
| **Tertiary SDG** | **SDG 8: Decent Work and Economic Growth** | 1. **SAP-SDG8-AUTO-01**: Reduction of SOC analyst alert fatigue.<br/>2. **SAP-SDG8-AUTO-02**: Decreasing MTTR from 45 mins to < 30 seconds.<br/>3. **SAP-SDG8-AUTO-03**: Workforce efficiency & burnout prevention. |

---

## SECTION 2: ACTIVITY LOG INDEX TABLE (WEEKS 1 - 13)

| S.No. | Title | Start Date | Completion Date | Mark (Out of 10) | Remarks | Signature of IDL - I Coordinator |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **Orientation & Entrepreneurial Mindset** | **01/08/2026** | **07/08/2026** | **10** | **Completed** | |
| **2** | **Problem Identification & Passion CV** | **08/08/2026** | **14/08/2026** | **10** | **Completed** | |
| 3 | Customer Segmentation & Persona Creation & JTBD | 15/08/2026 | 21/08/2026 | | In Progress | |
| 4 | Ideation, Market Size & Competitor Analysis | 22/08/2026 | 28/08/2026 | | Upcoming | |
| 5 | Milestone1:Problem-Solution Fit Presentation | 29/08/2026 | 04/09/2026 | | Upcoming | |

---

## SECTION 3: OUTSIDE WORLD PROJECTION

### Details of the Competition Attended (Hackathon / Idea Pitching)
| S.No | Name | Date | Place | Remark | Signature |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **1** | **Hac'KP 2026** (7th Edition National Hackathon by Kerala Police Cyberdome) | **14/08/2026** | **Zoho Corporation, Chennai** | **Selected for National In-Person Pitching Round** | |

### Design Patent / Idea Patent Publication / Conference Paper
| S.No | Title / Forum | Date | Place / Journal | Remark | Signature |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **1** | **Confidentiality-Preserving Autonomous SOC Triage via Tokenized Edge-Cloud Multi-Agent Systems** | **August 2026** | **IEEE / USENIX Track** | **Paper Manuscript & Patent Drafted** | |

---

## WEEK – 1: Orientation & Entrepreneurial Mindset

### • Understand entrepreneurship & innovation
Security Operations Centers (SOCs) generate over 10,000 security logs daily, creating severe alert fatigue where human analysts spend 30–45 minutes manually triaging single events. Commercial AI endpoints cannot be deployed directly due to data privacy regulations and risks of uploading confidential network payloads to external servers.

The proposed solution, SENTINEL, introduces Reversible Tokenized Pseudonymization, scrubbing 100% of sensitive PII, IP addresses, and hostnames locally before AI reasoning occurs. This enables enterprise-grade autonomous triage at $0 operational cost for 90% of routine alerts using local consumer GPU hardware (NVIDIA RTX 3050).

### • Opportunity recognition, entrepreneurial traits and growth mindset
The global SIEM automation and threat intelligence market is valued at $13.2 Billion+ with an 18.5% CAGR. Primary target markets include Enterprise SOCs, Managed Security Service Providers (MSSPs), Air-Gapped Defense Networks, Cyber Crime Units, and Startups. Technical resourcefulness is demonstrated by quantizing 70B parameter models down to 4-bit (IQ3_M) GGUF format to execute high-capacity intelligence on edge workstations.

### • Startup journey from idea to venture
1. **Problem Formulation**: Identifying SOC alert fatigue and data privacy constraints.
2. **Proof-of-Concept**: Engineering local Zero-Trust Data Sanitizer (`src/sanitizer.py`).
3. **MVP Architecture**: Building 3-Tier Hybrid AI Router (`src/router.py`).
4. **Validation & Pitching**: Selected for National Pitching Round at Hac'KP 2026 @ Zoho Corporation.
5. **Commercialization**: Deploying open-source SaaS framework and enterprise MSSP engine.

---

## WEEK – 2: Problem Identification & Passion CV

### • Identify real-world problems based on personal interests
Modern digital investigations face a severe bottleneck where human triage speed cannot match machine-speed cyber attacks. Public commercial cloud LLMs violate legal data privacy and chain-of-custody mandates when processing un-sanitized evidence.

### • Skills, experiences, and societal needs
Small businesses, hospitals, and educational institutions are unable to afford $100k+/year enterprise SIEM subscriptions (e.g., Splunk or Cortex XSOAR), leaving critical infrastructure vulnerable to ransomware. SENTINEL addresses this societal gap by delivering a self-hosted, privacy-compliant, autonomous AI co-pilot operating on standard hardware.

### • Prepare a Passion CV to identify potential entrepreneurial opportunities

**Gokula Kannan M (SEC25CS196 | CSE-A)**  
* Software Architecture, Systems Engineering, Project Governance & Venture Strategy.  
* Project Contribution: Overall system architecture, sprint management, and leading the national pitch at Hac'KP 2026 @ Zoho Corporation.  

**Lakshan M (SEC25CS036 | CSE-A)**  
* Full-Stack Web Development, React.js UI, WebSockets Integrations.  
* Project Contribution: Real-time incident dashboard engineering and Human-in-the-Loop (HITL) action approval interface.  

**Sivabalan T (SEC25CS101 | CSE-C)**  
* AI Engine Architecture, Zero-Trust Privacy Engineering, Quantization & Vector RAG.  
* Project Contribution: Development of Zero-Trust Data Sanitizer (`src/sanitizer.py`) and 3-Tier AI Router (`src/router.py`).  

**Faculty Supervisor**: Dr. A. SHEELA (Associate Professor, Department of Computer Science & Engineering, Sri Sai Ram Engineering College).
